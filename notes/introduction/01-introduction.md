---
title: "Introduction"
label: section:Introduction
numbering:
  title: false
  headings: false
---

These notes concern algorithmic information theory (AIT) and its applications to geometric measure theory (GMT), inductive reasoning, and machine learning (ML).

These notes are partly motivated by the mounting evidence that mathematics under algorithmic restrictions offers insights into–and refinements to–the study of the fractal properties of sets.

These notes are also motivated in part by the incredible success of modern machine learning techniques for serving intelligent inference models. We wish to flesh out the deep relationship between the ability to *compress* information and the ability to *reason*.

The rest of this page is taken from the introduction to my [doctoral dissertation](https://raymondtana.github.io/my_assets/documents/Raymond%20Tana%20PhD%20Dissertation.pdf). 

The origins of algorithmic information theory began in the 1960s with the formalization of **{term}`Solomonoff induction`**: a rule for selecting an {term}`hypothesis` for the source from which some given data was produced. The rule substitutes a non-computable, {term}`universal prior distribution` into {term}`Bayes' rule`, and rewards algorithmically-simpler explanations {cite:p}`Sol60`. R. Solomonoff's conception of information content is most closely related to the {term}`algorithmic probability` of producing a piece of data with respect to a {term}`universal Turing machine`.

An independent origin came just a few years later when A. Kolmogorov defined the algorithmic (plain) complexity of individual objects, thereby refining the concept of classical Shannon information which only describes the mean information content across a distribution {cite:p}`Kol68; Kol68b`. So, Kolmogorov's concept of information content was based on the degree of incompressibility with respect to a universal Turing machine.

And shortly after, G. Chaitin also independently introduced {term}`plain complexity <Plain Kolmogorov complexity>` and established its {term}`symmetry of information` property, as well as establishing some initial notions of algorithmic randomness for infinite binary strings based on attaining maximal complexity along their prefixes {cite:p}`Cha66`.

P. Martin-Löf characterized algorithmic randomness for an infinite binary sequence instead as the inability to cover it to arbitrary precision by {term}`effectively open` statistical tests {cite:p}`Mar66`. This adjusted A. Church's original attempt: computable randomness, meant to achieve the intuitive property due to von Mises that random sequences ought to pass all standard statistical tests such as the Law of Large Numbers.

C. Schnorr showed that both Chaitin's and Martin-Löf's notions of algorithmic randomness for infinite binary sequences were equivalent to yet another: those sequences on which any effective betting strategy (i.e., **constructive martingale**) would fail to generate arbitrary gains when betting on subsequent bits {cite:p}`Sch71`. Thus, what is now commonly known as **Martin-Löf randomness** is considered robust for its equivalent characterizations in terms of Chaitin's notion of incompressibility, Martin-Löf's notion of typicality, and Schnorr's notion of unpredictability.

Moreover, L. Levin confirmed the equivalence between Solomonoff, Kolmogorov, and Chaitin's approaches to quantifying algorithmic information content {cite:p}`Lev73`. Levin's {term}`Coding Theorem` equated Solomonoff's universal prior with $2^{-K(\cdot)}$, where $K(\cdot)$ denotes **prefix-free** or **self-delimiting Kolmogorov complexity**, or the minimal description-length of some data with respect to a universal, prefix-free Turing machine.

Whether viewed as the branch of theoretical computer science dedicated to the properties of computably-generated objects, or as a refinement of classical Shannon information theory by measuring the information content of individual objects, or as a project to formalize randomness: algorithmic information theory clearly offers some extra structure to otherwise “classical” mathematics, or the mathematics unconstrained by effectivity.

Just as any natural, geometric object has an assignable geometric dimension that corresponds to the right “exponential factor” by which to measure its volume, the goal of many fractal dimension notions is to assign to a set an exponent appropriate to its geometry {cite:p}`DMR05`. For instance, the **{term}`Hausdorff dimension`** of a set is roughly defined as the critical value of $s$ for which the volume of the set as measured using exponent $s$ switches from being infinite to null. Thus, Hausdorff dimension is naturally associated to the family of **$s$-dimensional Hausdorff outer measures $\mathcal{H}^s$** (defined in Section [%s](#section:Measures_and_Hausdorff_Dimension)). These outer measures refine Lebesgue measure on null sets based on their covering properties. Yet, a further refinement to $\mathcal{H}^s$-nullness is exhibited by **partial randomness**.

Generalizing the constructive martingales of Schnorr, J. Lutz introduced **constructive $s$-supergales**, where $s \geq 0$ is a dimension parameter {cite:p}`Lut00`. Whenever a constructive $s$-supergale could make arbitrary gains betting on the subsequent bits of a given sequence (i.e., **{term}`succeed`** on the sequence), then that sequence would not be considered random with respect to $s$. Then, Lutz defined the **{term}`constructive dimension`** of a sequence to roughly be the minimal $s$ on which some constructive $s$-supergale could succeed.

Shortly after, E. Mayordomo elucidated the relationship between Lutz's constructive dimension and Kolmogorov complexity. In particular, the constructive dimension of a sequence matches L. Staiger's limit inferior of the normalized Kolmogorov complexities of the sequence's prefixes {cite:p}`May02; Sta89`.

Both Lutz's and Mayordomo's contributions were built on decades of prior work toward understanding Kolmogorov complexity, including bounds on plain complexity by Shannon entropy {cite:p}`Sta81`, as well as work by both B. Ryabko {cite:p}`Rya93; Rya94` and Staiger {cite:p}`Sta98` partially relating the limit inferior of the normalized Kolmogorov complexity of prefixes to the speed at which a computable martingale could make arbitrary gains on a given sequence.

Generalizing the work of Schnorr and Chaitin, K. Tadaki introduced notions of Martin-Löf tests and partial randomness tailored to a dimension parameter $s \geq 0$ {cite:p}`Tad02`, which in turn provided yet another characterization of constructive dimension as roughly the minimal value of $s$ for which a set could be covered by one of these tests. Thus, this effective notion of dimension serves as a refinement to Martin-Löf randomness, and similarly may be characterized in terms of incompressibility, typicality, and unpredictability.

In effect, effective dimension quantifies just *how random* a sequence behaves in the limit. In particular, it is possible for singleton sets to have nonzero effective dimension (in fact, most have full effective dimension). These would correspond to points which are not covered by a Martin-Löf-test appropriate for some dimension $s > 0$; or, equivalently, those admitting highly incompressible prefixes; or, those on which any constructive $s$-supergale would not succeed at making arbitrary gains for some $s > 0$.

In the recent past, computability theorists and geometric measure theorists alike have used some notions of effective dimension to prove classical results about the fractal dimension of certain sets. The so-called **{term}`Point-to-Set Principles <Point-to-Set Principle>`** by J. Lutz and N. Lutz have almost always served as the bridge between effective and “classical” results about Hausdorff or packing dimensions in Euclidean space {cite:p}`LL18`. For example, their formula in Theorem [%s](#theorem:PTS_for_H_dimension) characterizes the Hausdorff dimension of a set in a pointwise manner: a strange result given that all singleton sets are classically zero-dimensional. But, as we have discussed, most points are not forthright in revealing their own smallness by effective means. Essentially, sets of large fractal dimension must contain many sufficiently random points.

There are still many open questions in regards to the potential applications of algorithmic information theory to geometric measure theory, as well as to what settings AIT applies.
