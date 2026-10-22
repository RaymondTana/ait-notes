---
title: "The Primitives of Reasoning"
label: section:Primitives_of_Reasoning
---

This page summarizes many of the key terms, in sufficient generality for future discussions. Much of this content is inspired by {cite:t}`LV08`.

(reasoning:primitives)=
## The primitives of reasoning

Below we describe some of the essential concepts for discussing *{term}`reasoning`*:

- **Observations**: data observed from some source.
- **Hypothesis**: a model for describing the source of some {term}`observations`.
- **Likelihood**: a numerical measure of an {term}`hypothesis’ <Hypothesis>` credibility.
- **Complexity notion**: a numerical measure of an {term}`hypothesis’ <Hypothesis>` inherent complexity against some fixed set of simple primitives.
- **Selection**: any procedure for selecting or preferring an {term}`hypothesis`.
- **Reasoning**: any procedure for assigning and updating {term}`likelihoods <Likelihood>` to a class of {term}`hypotheses <Hypothesis>`.

(reasoning:principles)=
## Principles for selection and reasoning over hypotheses

Next we describe some of the principles that guide how we approach {term}`reasoning`:

- **Induction** (a.k.a., **inductive reasoning**): a form of {term}`reasoning` which reassigns {term}`likelihoods <Likelihood>` to {term}`hypotheses <Hypothesis>` upon receiving more {term}`observations`.
- **Epicurus’ Principle of Multiple Explanations**: a principle of {term}`induction` which asserts that each {term}`hypothesis` which is consistent with all {term}`observations` ought to be considered with some nonzero {term}`likelihood`.
- **Occam’s Razor Principle**: a principle of {term}`selection` which prefers the simplest {term}`hypothesis` which is consistent with all {term}`observations`.
    - Or, more generally, the principle of {term}`reasoning` which asserts that simpler {term}`hypotheses <Hypothesis>` ought to be assigned with greater {term}`likelihoods <Likelihood>`.
- **Minimum Description Length (MDL) Principle**: the principle of {term}`selection` which prefers the {term}`hypothesis` which simultaneously has the (1) simplest description and (2) simplest explanation of the {term}`observations`.
- **Bayes’ Rule**: a mathematical rule for {term}`induction` which quantifies how a {term}`hypothesis’s <Hypothesis>` {term}`likelihood` should be updated given additional {term}`observations`: via conditional probabilities.

(reasoning:computability)=
## Recap on Computability

- An **algorithm** is any procedure implementable by an {term}`oracle Turing machine <Oracle machine>` equipped with an appropriate {term}`oracle`.
- An **effective algorithm** is any procedure implementable by a regular {term}`Turing machine`, or an {term}`algorithm` realizable by any Turing-complete programming language. I.e., "computable" or "decidable".
- A **compression algorithm** is an {term}`algorithm` which is interpreted as finding alternative representations for its inputs. I.e., an algorithm over some domain of “{term}`finitary objects <Finitary object>`” which is algorithmically invertible over its whole domain: so there must exist another algorithm being the inverse map, and vice versa.
    - Usually interpret the forward map as the compression step, and the backward map as the decompression step.
    - Invertibility axiom ⇒ both the forward and backward maps are injective.
    - "Lossy" compression relaxes invertibility: usually just ask for the forward map to satisfy some property across its domain with respect to some notion of "resemblance" between the original input and a `recover(forward(input))` over the domain of the forward map.
- An **effective compression algorithm** is a {term}`compression algorithm` realized by {term}`effective <Effective algorithm>` forward and backward algorithms.
- A **complexity notion** is just a map which assigns some score (say, from some totally ordered set like $\mathbb{R}_{\geq 0}$) to its domain. A map $C: \text{domain}(C) \to \mathbb{R}$ is reasonably generic for our purposes. Interpret smaller values as signifying less complexity.
    - A complexity notion $C$ may be "algorithmic" if evaluating $C$ only involves answering questions about how {term}`algorithms <Algorithm>` interact with the input.
    - It might be **universal** with respect to some class of {term}`complexity notions <Complexity notion>` if it "dominates", "simulates", or otherwise reasonably approximates an extremal scoring among all the complexity notions from that class.
    - It might qualify as an **entropy** notion if it satisfies some {term}`universality <Universal complexity notion>` property across a class of other {term}`complexity notions <Complexity notion>`.
    - It might satisfy the *{term}`Kraft inequality <Kraft Inequality>`* if the sum $\sum 2^{-C(\text{input})} < \infty$ converges. While this may look arbitrary, it proves to be very useful for recasting {term}`entropy <Entropy notion>` in terms of measure theory.
- **Randomness** is the notion of inscrutability with respect to the tools available to you:
    - If the tool = all {term}`algorithms <Algorithm>` ⇒ Shannon entropy.
    - If the tool = all {term}`effective algorithms <Effective algorithm>` ⇒ {term}`Kolmogorov complexity <Plain Kolmogorov complexity>`.
    - If the tool = ~poly-time algorithms ⇒ epiplexity (via pseudo-randomness).


(reasoning:up_to_computability)=
## Reasoning up to computability

- **Perfect induction**: {term}`induction` by {term}`Bayes’ Rule` using the *true* prior distribution on {term}`hypotheses <Hypothesis>`, i.e., the distribution actually governing the source of the {term}`observations`. Its predictions are necessarily optimal.
- **Solomonoff Induction**: a method for performing “{term}`perfect <Perfect induction>`” induction over any {term}`computable <Effective algorithm>` prior probability distribution, using the {term}`optimal` {term}`lower semi-computable <Lower-semicomputable>` {term}`continuous semimeasure` $\mathbf{M}$ and by applying {term}`Bayes’ Rule`.
- **Universal prior distribution**: a {term}`lower semi-computable <Lower-semicomputable>`, {term}`continuous semi-measure <Continuous semimeasure>` (so, assigning non-negative {term}`likelihoods <Likelihood>` to all {term}`hypotheses <Hypothesis>` so that they sum to at most 100%) which can essentially play the role of *any* prior distribution on hypotheses in {term}`Solomonoff induction`, without significant sacrifice in {term}`reasoning` capabilities.
