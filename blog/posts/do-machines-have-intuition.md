---
title:      Do Machines Have Intuition?
date:       2026-04-16
tag:        AI
tag_class:  tag-ai
excerpt:    |
  What is intuition, computationally? We argue it is rapid causal structure
  matching — and that this framing reveals exactly why current AI systems
  cannot yet replicate genuine cross-domain scientific insight.
read_time:  10 min
---

In 1952, Otto Struve proposed that a planet crossing the disk of a distant star
would cause a periodic, predictable dimming of its light. The observation that
sparked this idea was unremarkable — stars dim. But Struve connected that
ordinary fact to a causal chain that would eventually enable the detection of
thousands of exoplanets. No logical rule compelled the leap from "stellar flux
decreases" to "a body may be occluding the source." It was, by most accounts,
an act of intuition.

What exactly happened in that inferential moment?

## The standard accounts fall short

The philosophical vocabulary for describing such moments — "insight,"
"abduction," "System 1 processing" — is descriptively useful but
computationally opaque. Kahneman's dual-process theory correctly captures the
phenomenological speed of insight, but offers no account of its *content*: why
does fast processing sometimes produce a correct cross-domain connection rather
than a stereotypical response?

Gentner's Structure Mapping Engine (1983) formalizes analogy as the alignment of
relational structures across domains — one of the most rigorous accounts of
cross-domain inference we have. But it operates on *pre-specified* symbolic
structures and does not address how those structures are extracted from raw
observations.

Pearl's causal hierarchy provides a principled account of causal representation,
but the causal inference literature focuses on reasoning *within* a single
domain given a known causal graph, not on recognizing that two graphs from
different domains share the same skeleton.

What is missing is a framework that begins with raw observations, extracts
causal representations, and performs matching across domains.

## Intuition as causal structure matching

We propose that cross-domain intuitive insight consists of three operations
performed in rapid, often unconscious succession:

**1. Causal abstraction.** Given an observation, extract a causal representation
that captures its essential structure, stripped of domain-specific surface
features. Struve's observation becomes: *"a measurable property of an emitter
varies periodically, consistent with a regularly-interposed occluder."*

**2. Cross-domain search.** Search a repository of causal representations drawn
from other domains for structurally isomorphic matches. The occlusion template
retrieves: *"when an opaque object periodically interposes between a source and
observer, the observed flux decreases."*

**3. Hypothesis generation.** When a match is found, generate a hypothesis: the
mechanisms underlying the two domains may be related. A planetary body may be
occluding the star.

This account is explicitly *causal* rather than merely associational. The
connection is not that "star dimming" and "shadow" co-occur in text corpora, but
that they share an underlying causal skeleton. This is why the insight is
*generative* — it licenses predictions and interventions, not just pattern
completion.

It also makes the role of domain expertise precise. Causal abstraction requires
understanding a domain well enough to extract its causal structure. A physicist
and a painter looking at a dimming star will extract different representations
and therefore retrieve different matches. Intuition is not domain-free pattern
recognition; it is structure-sensitive inference grounded in expert knowledge.

## The one-to-many problem

The formalization immediately reveals a central computational challenge. A single
observation is typically consistent with *multiple* causal representations. A
dimming star could be caused by an orbiting planet, a stellar companion in
eclipse, an accretion disk fluctuation, interstellar dust, instrumental noise,
or intrinsic stellar variability. Each generates a distinct causal graph.

If one observation produces $m$ candidate causal representations and the
repository contains $n$ representations each with $k$ abstraction levels, the
exhaustive matching space has size $O(m \cdot n \cdot k^2)$. For realistic
values — $m = 10$, $n = 10^4$, $k = 5$ — this is computationally prohibitive.

This is not merely a practical inconvenience. It is philosophically informative.
The intractability of brute-force matching explains why genuine cross-domain
insight is *rare*, *domain-sensitive*, and *expertise-dependent*. The requisite
information is available; the search space is simply too large to traverse
without powerful constraints.

## What makes human intuition tractable

Two mechanisms collapse the search space to manageable size:

**Hierarchical abstraction** converts matching from a single exhaustive search
into a cascade of increasingly specific filters. At the coarsest level,
*"a property of an emitter changes over time"* matches a vast number of causal
representations — cheap but uninformative. At finer levels, *"the change is
periodic"* and then *"consistent with a geometric occlusion model"* progressively
narrow the candidates. Complexity drops from $O(n \cdot k^2)$ to
$O(n \cdot k \cdot \log k)$, with early termination for mismatches.

**Problem-directed pruning** restricts the search to representations relevant to
the agent's current goal. An instrument engineer observing a dimming star
searches causal representations involving electronic noise and calibration
errors. Struve, whose active problem was the population of bodies orbiting other
stars, searches astrophysical representations involving orbital mechanics. The
problem state $Q$ restricts matching to a subspace $\Gamma_Q \ll \Gamma$.

Newton's apple produced an insight about gravity not because Newton was uniquely
perceptive, but because his active problem — accounting for the Moon's orbit —
had already primed a specific region of his causal representation space. The
problem itself was the search algorithm.

An important implication follows: *intuition is not a capacity that operates
independently of deliberate reasoning.* The slow, effortful work of formulating
a problem — defining what is surprising, what requires explanation, what the
relevant variables are — is precisely what makes fast intuitive matching
tractable. The two processes are complements, not alternatives.

## Why current AI systems cannot do this

Large language models can describe the history of transit photometry, explain
the physics of stellar occultation, and discuss the statistical methods used in
exoplanet detection. What they cannot do — at least not robustly — is perform
the *original act of connection*: given only the observation of periodic stellar
dimming and a repository of causal knowledge from other domains, generate the
hypothesis that a planetary body may be responsible.

The reason is architectural. LLMs learn distributional associations over
linguistic tokens — text that *describes* causal relationships — without
learning causal representations in the sense required for structure matching.
This is the distinction Pearl draws between the associational and interventional
levels of the causal hierarchy.

Embedding similarity, while capturing something real, is insufficient. Two
concepts may be statistically associated without sharing causal structure
(correlation without causation), and may share causal structure without being
statistically associated if they appear in different textual contexts. Transit
photometry and everyday shadow-casting share causal structure but would not, in
1952, have appeared in proximity in any text corpus.

## What would it take?

Building systems capable of genuine cross-domain insight would require, at
minimum:

- A mechanism for extracting causal representations from observations
- A cross-domain repository of such representations
- A matching algorithm that can identify structural isomorphisms
- A problem-representation module that constrains the search

None of these components individually is beyond the current state of the art.
Causal representation learning (Schölkopf et al. 2021) addresses the first.
Structure mapping theory (Gentner 1983) addresses the third. Library learning
systems like DreamCoder (Ellis et al. 2021) address hierarchical abstraction
within single domains. The challenge is their integration — and, critically,
extending them to operate *across* domain boundaries.

The cross-domain matching of learned causal representations is the computational
core of what we experience as scientific intuition. It remains largely
unaddressed as a unified research problem. Framing it precisely — as we have
attempted here — is a first step toward building systems that do not merely
describe past discoveries, but generate new ones.

---

*This post summarizes a longer manuscript: "Intuition as Causal Structure
Matching: A Computational Account of Cross-Domain Insight."*
