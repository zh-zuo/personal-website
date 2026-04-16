---
title:      Do Machines Have Intuition?
date:       2026-04-16
tag:        AI
tag_class:  tag-ai
excerpt:    |
  When AlphaGo played Move 37, commentators called it "intuitive."
  But is pattern recognition at superhuman scale the same thing as
  intuition — or something fundamentally different?
read_time:  9 min
---

In Game 2 of the 2016 match against Lee Sedol, AlphaGo placed a stone on a
position that no professional Go player would have considered. The commentators
were stunned. Fan Hui, the European Go champion who had been working with the
DeepMind team, later said he found the move "beautiful." It was quickly labelled
an act of machine intuition.

But was it?

## What we mean by intuition

In cognitive science, intuition is usually defined as **rapid, unconscious
pattern recognition** that produces a judgement without deliberate analytical
reasoning. When a chess grandmaster glances at a board and "feels" that a
position is dangerous, they are not running a minimax search — they are matching
the current configuration against tens of thousands of positions stored in
long-term memory.

Kahneman's dual-process framework calls this **System 1** thinking: fast,
automatic, and effortless. System 2 is the slow, deliberate, logical mode.
Intuition, in this framework, is System 1 operating in a domain where the
person has deep expertise.

By this definition, AlphaGo's Move 37 looks remarkably similar. The policy
network — trained on millions of professional games and then refined through
self-play — evaluated the position and assigned a high probability to a move
that no human's System 1 would have produced. It was fast. It was automatic.
It was not the result of explicit search (though search refined it afterward).

## The case for "yes"

If intuition is pattern recognition over a large experiential base, then neural
networks are intuition machines. They do exactly what the expert's System 1
does, just over a vastly larger training set and with a different substrate.

Consider:

- A radiologist who spots a subtle tumour on a scan is doing pattern matching
  over thousands of prior images. A convolutional neural network trained on
  millions of scans is doing the same thing, with more data and higher
  consistency.
- A physicist who "feels" that an equation is wrong before checking the algebra
  is recognising a structural pattern. A language model that flags an
  inconsistency in a derivation is doing something functionally similar.

The **functionalist** argument says: if it walks like intuition and quacks like
intuition — if it produces the same kind of rapid, accurate, non-deliberative
judgements — then it *is* intuition, regardless of whether the substrate is
carbon or silicon.

## The case for "no"

The counterargument comes in several flavours:

**1. Intuition requires experience, not just data.** Human intuition is
grounded in embodied experience — years of physically moving pieces, feeling
the weight of a decision, experiencing the emotional consequences of mistakes.
A neural network processes data but does not *experience* it. The question is
whether experience matters for the functional output, or whether it is a
contingent feature of the biological implementation.

**2. Intuition is context-sensitive in ways models are not.** A human expert's
intuition adapts fluidly to novel contexts — a surgeon who trained on adult
patients can intuit something useful about a paediatric case, even without
specific training. Current models are more brittle outside their training
distribution.

**3. Intuition carries uncertainty in a felt sense.** When a human expert has a
"bad feeling" about a situation, that feeling comes with phenomenal qualities —
unease, tension, a nagging sense that something is off. This **metacognitive
signal** is part of what makes human intuition useful: it tells the person not
just "something is wrong" but "you should pay closer attention." Whether
machines can replicate this without subjective experience is an open question.

**4. The binding problem.** Human intuition integrates information across
sensory modalities, episodic memory, emotional state, and social context in a
single unified judgement. Current AI systems, even multimodal ones, process
these channels in architecturally distinct ways and combine them through
learned weighted averages — not through anything resembling unified conscious
experience.

## A more useful framing

Perhaps the binary question — do machines have intuition, yes or no — is the
wrong question. A better framing might be:

> **Machines can produce outputs that are functionally equivalent to human
> intuition in narrow domains, but they arrive at those outputs through a
> process that lacks the experiential grounding, metacognitive awareness, and
> contextual flexibility that characterise human intuition in its fullest
> sense.**

This matters practically, not just philosophically. If machine "intuition" is
narrow and brittle, then we should not trust it in the same way we trust a
seasoned expert's gut feeling. The expert's intuition degrades gracefully
outside their domain; the model's can fail catastrophically.

## Implications for human–AI collaboration

The practical takeaway is this: treat machine pattern recognition as a powerful
but incomplete form of intuition.

- **Trust it in-distribution**: when the model is operating within its training
  domain, its "intuitions" are likely to be as good as or better than a human's.
- **Verify it out-of-distribution**: when the situation is novel, the model's
  confidence may be unfounded. This is where human intuition — with its
  contextual flexibility and metacognitive warning signals — becomes essential.
- **Never treat it as self-aware**: a model that says "I feel uncertain" is
  producing a text string, not reporting a phenomenal state. Calibrated
  uncertainty estimates are useful; anthropomorphised "feelings" are misleading.

The deepest insight from this question is not about machines at all — it is
about us. Asking whether machines have intuition forces us to define what
intuition actually is, and in doing so, to understand our own cognition more
precisely.

---

*Move 37 was not intuition. But it was something that, until 2016, only
intuition could produce. That distinction is worth sitting with.*
