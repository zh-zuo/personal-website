#!/usr/bin/env python3
"""
Blog publisher
==============

Workflow:
  1. Write  blog/posts/your-slug.md   (frontmatter format below)
  2. Run    python publish.py
  3. Done —  blog/posts/your-slug.html  is created
             blog/index.html            is regenerated (all post cards)
             index.html                 is updated (3 most recent cards)

Frontmatter
-----------
---
title:      Post Title Here
date:       2026-04-02            # YYYY-MM-DD, determines sort order
tag:        Stellar-mass BH       # text shown on card
tag_class:  tag-bh                # tag-bh | tag-smbh | tag-jet
excerpt:    |
  Two or three sentences shown on the blog card.
  Indent continuation lines by two spaces.
read_time:  7 min                 # optional
---

Full post in Markdown.
LaTeX: inline $E = mc^2$  or display  $$P_{\\rm BZ} \\propto \\Phi^2 a_*^2$$

Dependencies
------------
  pip install markdown
"""

import sys, re
from pathlib import Path
from datetime import datetime

ROOT       = Path(__file__).parent
POSTS_DIR  = ROOT / 'blog' / 'posts'      # markdown sources + output HTML live here
BLOG_INDEX = ROOT / 'blog' / 'index.html' # blog listing page
HOME_INDEX = ROOT / 'index.html'          # homepage

POSTS_DIR.mkdir(parents=True, exist_ok=True)

# ── Markdown ──────────────────────────────────────────────────────────
try:
    import markdown as _md
    def md_to_html(text):
        return _md.markdown(text, extensions=[
            'tables', 'footnotes', 'fenced_code', 'attr_list', 'toc',
        ])
except ImportError:
    sys.stderr.write(
        "  [!] 'markdown' not installed — run:  pip install markdown\n"
        "      Falling back to basic converter.\n\n"
    )
    def md_to_html(text):
        lines = text.split('\n')
        out, in_p = [], False
        for raw in lines:
            line = raw.rstrip()
            hm = re.match(r'^(#{1,4})\s+(.*)', line)
            if hm:
                if in_p: out.append('</p>\n'); in_p = False
                n = len(hm.group(1))
                out.append(f'<h{n}>{hm.group(2)}</h{n}>\n'); continue
            if not line.strip():
                if in_p: out.append('</p>\n'); in_p = False
                continue
            line = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', line)
            line = re.sub(r'\*(.+?)\*',     r'<em>\1</em>',         line)
            line = re.sub(r'`(.+?)`',       r'<code>\1</code>',     line)
            if not in_p: out.append('<p>'); in_p = True
            else: out.append(' ')
            out.append(line)
        if in_p: out.append('</p>\n')
        return ''.join(out)

# ── Frontmatter ───────────────────────────────────────────────────────
def parse_frontmatter(text):
    text = text.strip()
    if not text.startswith('---'):
        return {}, text
    rest = text[3:]
    end  = rest.find('\n---')
    if end == -1:
        return {}, text
    raw, body = rest[:end], rest[end + 4:].strip()
    meta = {}
    cur_key, block = None, []
    for line in raw.splitlines():
        if cur_key:
            if line.startswith('  ') or line.startswith('\t'):
                block.append(line.strip()); continue
            else:
                meta[cur_key] = ' '.join(block); cur_key = None; block = []
        if ':' in line:
            k, v = line.split(':', 1)
            k, v = k.strip(), v.strip()
            if v == '|': cur_key = k
            else: meta[k] = v
    if cur_key: meta[cur_key] = ' '.join(block)
    return meta, body

# ── Date helpers ──────────────────────────────────────────────────────
def fmt_long(d):
    try:    return datetime.strptime(str(d).strip(), '%Y-%m-%d').strftime('%-d %B %Y')
    except: return str(d)

def fmt_card(d):
    try:
        dt = datetime.strptime(str(d).strip(), '%Y-%m-%d')
        return f'{dt.year} — {dt.month:02d} — {dt.day:02d}'
    except: return str(d)

def sort_key(m):
    try:    return datetime.strptime(str(m.get('date','1970-01-01')).strip(), '%Y-%m-%d')
    except: return datetime(1970,1,1)

# ── Post page template ────────────────────────────────────────────────
def render_post_page(meta, content_html):
    title   = meta.get('title',     'Untitled')
    date_s  = fmt_long(meta.get('date', ''))
    tag     = meta.get('tag',       '')
    tag_cls = meta.get('tag_class', 'tag-bh')
    rt      = meta.get('read_time', '')
    rt_html = f'<span class="post-read">{rt} read</span>' if rt else ''

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Source+Serif+4:ital,opsz,wght@0,8..60,300;0,8..60,400;1,8..60,300&family=JetBrains+Mono:wght@300;400&display=swap" rel="stylesheet">
  <script>MathJax={{tex:{{inlineMath:[['$','$']],displayMath:[['$$','$$']],tags:'ams'}},options:{{skipHtmlTags:['script','noscript','style','textarea','pre']}}}};</script>
  <script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
  <style>
    :root{{--bg:#05050a;--gold:#e4a84a;--cyan:#4db8d4;--text:#d4d0e6;--muted:#5c5870;--border:rgba(228,168,74,0.10);}}
    *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0;}}
    html{{scroll-behavior:smooth;}}
    body{{background:var(--bg);color:var(--text);font-family:'Source Serif 4',Georgia,serif;font-weight:300;-webkit-font-smoothing:antialiased;}}
    nav{{position:fixed;inset:0 0 auto 0;z-index:200;display:flex;align-items:center;justify-content:space-between;padding:1.4rem 3.5rem;background:rgba(5,5,10,0.88);backdrop-filter:blur(14px);border-bottom:1px solid var(--border);}}
    .nav-logo{{font-family:'JetBrains Mono',monospace;font-size:0.68rem;letter-spacing:0.18em;text-transform:uppercase;color:var(--gold);text-decoration:none;}}
    .nav-links{{list-style:none;display:flex;gap:2.8rem;}}
    .nav-links a{{font-family:'JetBrains Mono',monospace;font-size:0.65rem;letter-spacing:0.14em;text-transform:uppercase;color:var(--muted);text-decoration:none;transition:color .25s;}}
    .nav-links a:hover{{color:var(--text);}} .nav-links a.active{{color:var(--gold);}}
    .post-wrap{{max-width:760px;margin:0 auto;padding:9rem 2rem 8rem;}}
    .back{{display:inline-flex;align-items:center;gap:.55rem;font-family:'JetBrains Mono',monospace;font-size:0.6rem;letter-spacing:0.16em;text-transform:uppercase;color:var(--muted);text-decoration:none;margin-bottom:3.5rem;transition:color .25s;}}
    .back:hover{{color:var(--gold);}}
    .post-meta{{display:flex;align-items:center;gap:1.2rem;margin-bottom:1.4rem;}}
    .tag{{font-family:'JetBrains Mono',monospace;font-size:0.56rem;letter-spacing:0.14em;text-transform:uppercase;padding:.22rem .65rem;border:1px solid;}}
    .tag-bh{{color:var(--gold);border-color:rgba(228,168,74,0.28);}}
    .tag-smbh{{color:#e8804a;border-color:rgba(232,128,74,0.28);}}
    .tag-jet{{color:var(--cyan);border-color:rgba(77,184,212,0.28);}}
    .tag-ai{{color:#b48afe;border-color:rgba(180,138,254,0.28);}}
    .post-date{{font-family:'JetBrains Mono',monospace;font-size:.6rem;letter-spacing:.1em;color:var(--muted);}}
    .post-read{{font-family:'JetBrains Mono',monospace;font-size:.6rem;letter-spacing:.1em;color:var(--muted);margin-left:auto;}}
    h1.post-title{{font-family:'Cormorant Garamond',serif;font-size:clamp(2.2rem,5vw,3.6rem);font-weight:300;line-height:1.1;letter-spacing:-0.02em;margin-bottom:2.8rem;padding-bottom:2.8rem;border-bottom:1px solid var(--border);}}
    .post-body{{font-size:1.05rem;line-height:1.92;}}
    .post-body p{{margin-bottom:1.6em;}}
    .post-body h2{{font-family:'Cormorant Garamond',serif;font-size:2rem;font-weight:400;letter-spacing:-0.015em;margin:2.8em 0 0.9em;color:#e8e4f4;}}
    .post-body h3{{font-family:'Cormorant Garamond',serif;font-size:1.5rem;font-weight:400;margin:2.2em 0 0.7em;color:#c8c4d8;}}
    .post-body h4{{font-family:'JetBrains Mono',monospace;font-size:0.72rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--gold);margin:2em 0 0.6em;}}
    .post-body strong{{font-weight:600;color:#e8e4f4;}}
    .post-body em{{font-style:italic;color:#c8c4d4;}}
    .post-body a{{color:var(--gold);text-underline-offset:3px;}}
    .post-body a:hover{{color:#f0c070;}}
    .post-body code{{font-family:'JetBrains Mono',monospace;font-size:0.82em;background:rgba(228,168,74,0.08);color:#d4c090;padding:.12em .4em;border-radius:2px;}}
    .post-body pre{{background:#0e0e18;border:1px solid var(--border);border-left:2px solid #8a5f20;padding:1.5rem;overflow-x:auto;margin:2em 0;}}
    .post-body pre code{{background:none;padding:0;font-size:0.85em;color:#c8c4e0;}}
    .post-body blockquote{{border-left:2px solid var(--gold);margin:2em 0;padding:.4em 1.5em;color:var(--muted);font-style:italic;font-size:1.05em;}}
    .post-body ul,.post-body ol{{margin:0 0 1.6em 1.5em;}}
    .post-body li{{margin-bottom:.4em;}}
    .post-body hr{{border:none;border-top:1px solid var(--border);margin:3em 0;}}
    .post-body table{{width:100%;border-collapse:collapse;margin:2em 0;font-size:.9rem;}}
    .post-body th,.post-body td{{padding:.6rem 1rem;border:1px solid var(--border);text-align:left;}}
    .post-body th{{font-family:'JetBrains Mono',monospace;font-size:0.65rem;letter-spacing:.08em;text-transform:uppercase;color:var(--gold);background:rgba(228,168,74,0.06);}}
    .post-body img{{max-width:100%;height:auto;display:block;margin:2.5em auto;border:1px solid var(--border);}}
    .post-body figure{{margin:2.5em 0;text-align:center;}}
    .post-body figcaption{{font-size:.82rem;color:var(--muted);margin-top:.8em;font-style:italic;}}
    .footnote{{font-size:.88rem;margin-top:4em;padding-top:1.5em;border-top:1px solid var(--border);color:var(--muted);}}
    .footnote ol{{margin-left:1.2em;}}
    .post-footer{{margin-top:5rem;padding-top:2.5rem;border-top:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;}}
    .post-footer-coords{{font-family:'JetBrains Mono',monospace;font-size:.55rem;letter-spacing:.1em;color:rgba(228,168,74,0.35);}}
  </style>
</head>
<body>
<nav>
  <a href="../../index.html" class="nav-logo">Zihao Zuo</a>
  <ul class="nav-links">
    <li><a href="../../index.html">Home</a></li>
    <li><a href="#">Research</a></li>
    <li><a href="#">Publications</a></li>
    <li><a href="../index.html" class="active">Blog</a></li>
    <li><a href="../../index.html#contact">Contact</a></li>
  </ul>
</nav>
<div class="post-wrap">
  <a href="../index.html" class="back">← Back to Blog</a>
  <div class="post-meta">
    <span class="tag {tag_cls}">{tag}</span>
    <span class="post-date">{date_s}</span>
    {rt_html}
  </div>
  <h1 class="post-title">{title}</h1>
  <div class="post-body">
{content_html}
  </div>
  <div class="post-footer">
    <a href="../index.html" class="back" style="margin:0">← Back to Blog</a>
    <span class="post-footer-coords">α 17<sup>h</sup>45<sup>m</sup>40<sup>s</sup> · Sgr A*</span>
  </div>
</div>
</body>
</html>"""

# ── Card HTML (shared by blog index and homepage) ─────────────────────
def render_card(meta, url):
    title   = meta.get('title',     'Untitled')
    tag     = meta.get('tag',       '')
    tag_cls = meta.get('tag_class', 'tag-bh')
    date_s  = fmt_card(meta.get('date', ''))
    excerpt = meta.get('excerpt',   '')
    rt      = meta.get('read_time', '')
    rt_html = f'<span class="read-time">~{rt} read</span>' if rt else '<span class="read-time"></span>'
    return f"""
    <a class="card" href="{url}">
      <div class="card-meta">
        <span class="tag {tag_cls}">{tag}</span>
        <span class="card-date">{date_s}</span>
      </div>
      <h3 class="card-title">{title}</h3>
      <p class="card-excerpt">{excerpt}</p>
      <div class="card-footer">
        {rt_html}
        <span class="card-arrow">Read more →</span>
      </div>
    </a>"""

# ── Inject cards between markers ──────────────────────────────────────
def inject(html, start_marker, end_marker, content):
    s = html.find(start_marker)
    e = html.find(end_marker)
    if s == -1 or e == -1:
        raise ValueError(f"Markers '{start_marker}' / '{end_marker}' not found.")
    return html[:s + len(start_marker)] + '\n' + content + '\n    ' + html[e:]

# ── Main ──────────────────────────────────────────────────────────────
def main():
    md_files = sorted(POSTS_DIR.glob('*.md'))
    if not md_files:
        print('No .md files found in blog/posts/ — create one and re-run.')
        return

    posts = []
    print()
    for md_path in md_files:
        text = md_path.read_text(encoding='utf-8')
        meta, body = parse_frontmatter(text)
        meta['_slug'] = md_path.stem
        content_html = md_to_html(body)
        out = POSTS_DIR / (md_path.stem + '.html')
        out.write_text(render_post_page(meta, content_html), encoding='utf-8')
        print(f'  ✓  blog/posts/{md_path.stem}.html')
        posts.append(meta)

    posts.sort(key=sort_key, reverse=True)

    # ── blog/index.html ──
    if not BLOG_INDEX.exists():
        print(f'\n  [!] {BLOG_INDEX} not found — skipping blog index update.')
    else:
        cards = ''.join(render_card(m, f'posts/{m["_slug"]}.html') for m in posts)
        html  = BLOG_INDEX.read_text(encoding='utf-8')
        try:
            html = inject(html, '<!-- POSTS_START -->', '<!-- POSTS_END -->', cards)
            BLOG_INDEX.write_text(html, encoding='utf-8')
            print(f'  ✓  blog/index.html  ({len(posts)} post{"s" if len(posts)!=1 else ""})')
        except ValueError as e:
            print(f'  [!] blog/index.html: {e}')

    # ── index.html (homepage — 3 most recent) ──
    if not HOME_INDEX.exists():
        print(f'  [!] {HOME_INDEX} not found — skipping homepage update.')
    else:
        recent = posts[:3]
        cards  = ''.join(render_card(m, f'blog/posts/{m["_slug"]}.html') for m in recent)
        html   = HOME_INDEX.read_text(encoding='utf-8')
        try:
            html = inject(html, '<!-- RECENT_POSTS_START -->', '<!-- RECENT_POSTS_END -->', cards)
            HOME_INDEX.write_text(html, encoding='utf-8')
            print(f'  ✓  index.html  ({len(recent)} recent post{"s" if len(recent)!=1 else ""})')
        except ValueError as e:
            print(f'  [!] index.html: {e}')

    print()

if __name__ == '__main__':
    main()
