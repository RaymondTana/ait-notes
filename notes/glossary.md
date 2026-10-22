---
title: "Glossary"
label: section:Glossary
numbering:
  title: false
  headings: false
---

Short descriptions of terms defined throughout these notes, each with a link to its full definition.

:::{glossary}
A priori complexity
: The complexity $\operatorname{KM}(\sigma) := -\log \mathbf{M}(\sigma)$ of a string, given by the optimal lower-semicomputable continuous semimeasure $\mathbf{M}$. See Section [%s](#section:Semimeasures).

A priori discrepancy
: The gap $\operatorname{\Delta M}_\rho(\sigma) := \operatorname{KM}(\sigma) + \log \rho([\sigma])$ between a string's a priori complexity and its mass under a premeasure $\rho$. See Definition [%s](#definition:algorithmic_discrepancies).

A priori probability
: The total weight $Q_M(a) := \sum_{M(\pi) \downarrow = a} 2^{-\operatorname{len}(\pi)}$ of all descriptions of a finitary object $a$ under a machine $M$. See Definition [%s](#definition:algorithmic_and_a_priori_probability).

Algorithm
: A procedure implementable by an oracle Turing machine equipped with an appropriate oracle. See Section [%s](#reasoning:computability).

Algorithmic probability
: The value $R_M(a) := 2^{-C_M(a)}$ given by a finitary object's shortest description under a machine $M$. See Definition [%s](#definition:algorithmic_and_a_priori_probability).

Arithmetic hierarchy
: Kleene's classification of sets of natural numbers into levels $\Sigma^0_n$, $\Pi^0_n$, $\Delta^0_n$ by the number of alternating quantifiers needed to define them from a computable relation. See Section [%s](#section:Computability_Theory).

Bayes’ Rule
: A rule for induction updating a hypothesis’s likelihood on additional observations via conditional probabilities. See Section [%s](#reasoning:principles).

Bi-uniformly continuous
: A bijection that is both uniformly continuous and co-uniformly continuous; "bi-Lipschitz" and "bi-Hölder" are used likewise. See Section [%s](#section:Effective_Dimension_under_Uniformly_Continuous_Maps).

Cauchy representation
: A sequence of dyadic approximations to a real point $x$, the $r$-th accurate to within $2^{-r}$; it is standard if each approximation rounds $x$ down. See Section [%s](#section:Computability_Theory).

Chain rule
: An approximate formula relating the complexity of a pair to a sum of complexities involving both terms. Originally, Gács's identity: $K(a, b \mid c) = K(a \mid c) + K(b \mid a, K(a), c) \pm O(1)$ for prefix complexity of finitary objects. Also called symmetry of information, analogous to that of Shannon information theory. See Theorem [%s](#theorem:chain_rule_for_K).

Co-Lipschitz constant
: A constant lower-bounding how much a function shrinks distances: no two points are mapped closer together than this many times their original distance. See Section [%s](#section:Effective_Dimension_under_Uniformly_Continuous_Maps).

Co-uniformly continuous
: An injection whose inverse is uniformly continuous; "co-Lipschitz" and "co-Hölder" are used likewise. See Section [%s](#section:Effective_Dimension_under_Uniformly_Continuous_Maps).

Coding Theorem
: Levin's theorem that prefix complexity and the negative logarithms of algorithmic probability, a priori probability, and the optimal lower-semicomputable discrete semimeasure all agree up to an additive constant. See Theorem [%s](#theorem:coding_theorem).

Comparable
: Two strings are comparable ($\sigma \mid\mid \tau$) if one extends the other. See the [Notation](#section:Notation) page.

Complexity notion
: A numerical measure of a hypothesis's inherent complexity against some fixed set of simple primitives. Usually a map assigning a score along its domain, with a smaller score meaning simpler. See Sections [%s](#reasoning:primitives) and [%s](#reasoning:computability).

Compression algorithm
: An algorithm on finitary objects with an algorithmic inverse on its whole domain, read as compression (forward) and decompression (backward). See Section [%s](#reasoning:computability).

Computable metric space
: A metric space with a dense sequence whose pairwise distances is computable. See Section [%s](#section:Computability_Theory).

Computable Polish space
: A computable metric space whose metric is complete. See Section [%s](#section:Computability_Theory).

Computable real function
: A function $f : \mathbb{R}^m \to \mathbb{R}^n$ computed by an oracle machine that turns any Cauchy representation of an input into a Cauchy representation of its output under $f$. See Section [%s](#section:Computability_Theory).

Computably compact
: A subset of a computable metric space that is empty or computably approximable, to any desired precision in Hausdorff distance, by finite subsets of the dense sequence. See Section [%s](#section:Computability_Theory).

Computably enumerable
: A set that is the domain of a Turing machine. Equivalently, a set which is either empty or the range of a total computable function. Abbreviated "c.e." See Section [%s](#section:Computability_Theory).

Conditional dimension
: The quantity $\dim(x \mid y)$ quantifying the asymptotic rate of conditional complexity per bit of precision of $x$ given $y$. See Section [%s](#section:Conditional_and_Mutual_Dimensions).

Constructive dimension
: J. Lutz's effective analogue of Hausdorff dimension, $\operatorname{cdim}(X)$: the infimum of $s$ such that some constructive $s$-supergale succeeds on $X$. See Section [%s](#section:Effective_Hausdorff_Dimension).

Constructive supergale
: A lower-semicomputable supergale. See Section [%s](#section:Semimeasures).

Continuous semimeasure
: A map on a sequence space whose value on each string is at least the combined value on its immediate extensions, so mass can only leak away as strings grow. See Section [%s](#section:Semimeasures).

Convex premeasure
: A premeasure on Cantor space whose value on each string is at most the combined value on its two one-bit extensions. See Section [%s](#section:Measures_and_Hausdorff_Dimension).

Counting Theorem
: Chaitin's bounds on prefix complexity over the strings of a fixed length $n$: the most complex have complexity about $n + K(n)$, and few strings fall far below it. See Theorem [%s](#theorem:chaitin_counting_theorem).

Cover
: A Martin-Löf-type test $(U_n)_n$ covers $X$ if $X$ is a subset of the union of all cover elements; a Solovay-type test covers $X$ if each point of $X$ has infinitely many prefixes in it. Otherwise $X$ passes the test. See Definition [%s](#definition:test_coverings).

Cylinder set
: The set $[\sigma]$ of all infinite binary strings extending a finite string $\sigma$. See the [Notation](#section:Notation) page.

Dimension function
: A non-negative, non-decreasing, right-continuous function $h$ on $[0, \infty)$ with $h(t) = 0$ exactly when $t = 0$. See Section [%s](#section:Measures_and_Hausdorff_Dimension).

Direct weight
: The total premeasure $\operatorname{DW}_\rho(\mathcal{V})$ of the cylinders of a collection of strings. See Definition [%s](#definition:weights).

Discrete semimeasure
: A map on a collection of finitary objects whose values sum to at most $1$. See Section [%s](#section:Semimeasures).

Effective algorithm
: An algorithm needing no oracle: a Turing machine, or a program in any Turing-complete language; i.e., computable. See Section [%s](#reasoning:computability).

Effective compression algorithm
: A compression algorithm whose forward and backward maps are both effective algorithms. See Section [%s](#reasoning:computability).

Effective Hausdorff dimension
: The infimum of $s$ for which $X$ is Martin-Löf-$s$-null; it coincides with constructive dimension and the lower incompressibility ratio. See Section [%s](#section:Effective_Hausdorff_Dimension).

Effectively closed
: The complement of an effectively open set; a $\Pi^0_1$-class. See Section [%s](#section:Computability_Theory).

Effectively compact
: A computable metric space that is computably compact in itself. See Section [%s](#section:Computability_Theory).

Effectively open
: A set $[S]$ of Cantor space generated by a c.e. set of strings $S$; a $\Sigma^0_1$-class. See Section [%s](#section:Computability_Theory).

Entropy notion
: A complexity notion satisfying some universality property across a class of other complexity notions. See Section [%s](#reasoning:computability).

Epicurus’ Principle of Multiple Explanations
: A principle of induction: every hypothesis consistent with all observations ought to keep some nonzero likelihood. See Section [%s](#reasoning:principles).

Expansive map
: A map $f$ on Cantor space is $\alpha$-expansive if, for all but finitely many $r$, the first $r$ bits of an input determine at least $\alpha \cdot r$ bits of its output. See Section [%s](#section:Effective_Dimension_under_Uniformly_Continuous_Maps).

Extension
: A string $\tau$ extends $\sigma$ ($\sigma \preceq \tau$) if it agrees with $\sigma$ on every position of $\sigma$; a proper extension is one with $\sigma \neq \tau$. See the [Notation](#section:Notation) page.

Finitary object
: An element of a standard countable collection such as $\omega$, $2^{<\omega}$, $\mathbb{D}$, or $\mathbb{Q}$, all identified by computable bijections; also called hereditarily finite. See the [Notation](#section:Notation) page.

Hausdorff dimension
: The infimum of $s \geq 0$ for which a set is null with repect to the $s$-dimensional outer Hausdorff measure. See Section [%s](#section:Measures_and_Hausdorff_Dimension).

Hausdorff distance
: The infimum of $\varepsilon > 0$ for which two sets are $\varepsilon$-close: every point of each lies within $\varepsilon$ of the other. See Section [%s](#section:Computability_Theory).

Hausdorff oracle
: An oracle that attains the minimum in the Point-to-Set Principle for a set. See Section [%s](#section:PTS).

Hausdorff outer measure
: A Method II outer measure induced by a Hausdorff premeasure. See Section [%s](#section:Measures_and_Hausdorff_Dimension).

Hausdorff premeasure
: The premeasure $\rho_h$ that applies a dimension function $h$ to the diameter of a set. See Section [%s](#section:Measures_and_Hausdorff_Dimension).

Hypothesis
: A model for describing the source of some observations. See Section [%s](#reasoning:primitives).

Hölder continuous
: Uniformly continuous with a modulus that needs about $1/\alpha$ bits of input precision per bit of output precision, where $\alpha$ is its exponent; equivalently, output distances are bounded by a constant times the $\alpha$-th power of input distances. See Section [%s](#section:Effective_Dimension_under_Uniformly_Continuous_Maps).

Induction
: Reasoning that reassigns likelihoods to hypotheses upon receiving more observations; also called inductive reasoning. See Section [%s](#reasoning:principles).

Infinitary object
: An object arising from finitary objects by a limiting process, such as an infinite binary string or a real number. See the [Notation](#section:Notation) page.

Information content measure
: Levin's notion: an upper-semicomputable partial function $F : \subseteq \mathscr{N} \to \omega$ on a collection of finitary objects with $\sum_a 2^{-F(a)} \leq 1$. See Section [%s](#section:Semimeasures).

Inverse-modulus
: A modulus of uniform continuity for the inverse of a co-uniformly continuous map. See Section [%s](#section:Effective_Dimension_under_Uniformly_Continuous_Maps).

K-minimizer
: A finitary element $x \in X$ witnessing the minimum complexity $K(x) = K(X)$; an $\varepsilon$-approximate $K$-minimizer has $K(x) \leq K(X) + \varepsilon$. See Definition [%s](#definition:K_minimizer).

Kraft Inequality
: The bound that $2^{-K}$, summed over any collection of finitary objects, is at most $1$; a consequence of the universal machine being prefix-free. See Theorem [%s](#theorem:kraft_inequality).

Left-approximator
: A computable map $\widehat{f}(i, r)$ that increases in $r$ to $f(i)$, witnessing that $f$ is lower-semicomputable. See Section [%s](#section:Computability_Theory).

Length-invariant
: A premeasure on Cantor space whose value on $\sigma$ depends only on $\operatorname{len}(\sigma)$. See Section [%s](#section:Measures_and_Hausdorff_Dimension).

Lightface Borel hierarchy
: The effective hierarchy of $\Sigma^0_n$-, $\Pi^0_n$-, and $\Delta^0_n$-classes of Cantor space, built up from effectively open sets. See Section [%s](#section:Computability_Theory).

Likelihood
: A numerical measure of a hypothesis's credibility. See Section [%s](#reasoning:primitives).

Linear sensitivity
: Bounds on how much $K_r(x)$ and $K_{r \mid s}(x \mid y)$ can change when a precision-level grows: at most linearly in the change. See Lemmas [%s](#lemma:linearity_r_no_condition) and [%s](#lemma:linearity_with_condition).

Lipschitz constant
: A constant upper-bounding how much a function stretches distances: no two points are mapped farther apart than this many times their original distance. See Section [%s](#section:Effective_Dimension_under_Uniformly_Continuous_Maps).

Lipschitz continuous
: Uniformly continuous with a modulus that costs only a constant number of extra bits of input precision; equivalently, having a Lipschitz constant. See Section [%s](#section:Effective_Dimension_under_Uniformly_Continuous_Maps).

Local dimension
: The (lower) local dimension of a set: the worst case, over its points, of the lower asymptotic rate at which a semimeasure or outer measure decays along their prefixes. See Definition [%s](#definition:local_dimension).

Locally Lipschitz continuous
: Lipschitz continuous on some open neighborhood of each point of the domain. See Section [%s](#section:Effective_Dimension_under_Uniformly_Continuous_Maps).

Locally optimal
: N. Lutz's optimality property for an outer measure among all strongly finite, lower-semicomputable outer measures. See Section [%s](#section:Effective_Hausdorff_Dimension).

Lower incompressibility ratio
: The worst case across all points in a set of the lower asymptotic prefix complexity per bit of their prefixes. See Section [%s](#section:Effective_Hausdorff_Dimension).

Lower-semicomputable
: A real number, or a real-valued map on a collection of finitary objects (such as a semimeasure), whose lower graph $\set{(n, q)}{q < f(n)}$ is c.e.; equivalently, one approximable from below by a computable left-approximator. Also called left-c.e. See Section [%s](#section:Computability_Theory).

Martin-Löf test
: A uniformly-c.e. sequence $(U_n)_n$ of sets of strings, each of which having direct weight at most $2^{-n}$; strong and vehement versions bound the prefix or vehement weight instead. See Definition [%s](#definition:tests).

Method II outer measure
: Rogers's outer measure $\mathcal{H}^\rho$ induced by a premeasure $\rho$, using covers of diameter at most $\delta$ (the $\delta$-contents $\mathcal{H}^\rho_\delta$) and letting $\delta \to 0$. See Section [%s](#section:Measures_and_Hausdorff_Dimension).

Minimal description
: A description $\pi$ of a finitary object $a$ (given $b$) of the least possible length; any $\pi$ with $M^{\overline{b}}(\pi) = a$ is an $M$-description. See Section [%s](#section:Prefix_Comlexity).

Minimum Description Length Principle
: A principle of selection preferring the hypothesis with both the simplest description and the simplest explanation of the observations. Abbreviated MDL. See Section [%s](#reasoning:principles).

Modulus and data processing inequalities
: Bounds on how conditional prefix complexity changes under computable, uniformly continuous maps, controlled by their moduli. See Lemma [%s](#lemma:forward_data_processing_conditional).

Modulus of uniform continuity
: A non-decreasing $\mu : \omega \to \omega$ telling how much input precision suffices for a desired output precision: inputs within $2^{-\mu(r)}$ of each other have outputs within $2^{-r}$. See Definition [%s](#definition:modulus_of_uniform_continuity).

Mutual dimension
: Case and Lutz's lower and upper mutual dimensions $\operatorname{mdim}(x : y)$ and $\operatorname{Mdim}(x : y)$: the asymptotic rates of mutual information per bit of precision shared by $x$ and $y$. See Section [%s](#section:Conditional_and_Mutual_Dimensions).

Mutual information
: The algorithmic information $I(a : b \mid c) := K(a \mid c) - K(a \mid b, c)$ shared by finitary objects, lifted to sets and to reals at given precision-levels. See Section [%s](#section:Conditional_and_Mutual_Dimensions).

Neighborhood
: The $\delta$-neighborhood of a subset of a metric space consists of all points within distance $\delta$ of that subset. See the [Notation](#section:Notation) page.

Null set
: A set of outer measure zero. In particular, $\mu$-null means $\mu(X) = 0$, and $s$-null means $\mathcal{H}^s(X) = 0$. See Section [%s](#section:Measures_and_Hausdorff_Dimension).

Observations
: Data observed from some source. See Section [%s](#reasoning:primitives).

Occam’s Razor Principle
: A principle of selection preferring the simplest hypothesis consistent with all observations; more generally, that simpler hypotheses ought to get greater likelihoods. See Section [%s](#reasoning:principles).

Optimal
: A notion of universality in which an element of a class (of semimeasures, supergales, outer measures, ...) dominates each other element of the class up to a multiplicative constant. E.g., $\mathbf{m}$ and $\mathbf{M}$ are optimal among the lower-semicomputable discrete and continuous semimeasures, respectively. See Section [%s](#section:Semimeasures).

Optimal cover
: A cover of a set of strings whose direct weight equals the vehement weight of the set. See Definition [%s](#definition:optimal_cover).

Oracle
: Extra information, given as a finite or infinite binary string (an infinite tape of data), that an oracle machine may consult during a computation. See Section [%s](#section:Computability_Theory).

Oracle machine
: A Turing machine that may also query, finitely often, the bits of an oracle during its computation; also called an oracle Turing machine or Turing functional. See Section [%s](#section:Computability_Theory).

Partial bi-computable
: Both partial computable and partial co-computable. Abbreviated p.b.c. See Section [%s](#section:Prefix_Comlexity).

Partial co-computable
: Injective, with a partial computable inverse on its range. Abbreviated p.c.c. See Section [%s](#section:Prefix_Comlexity).

Partial computable function
: A partial function computed by some Turing machine. Abbreviated p.c. See Section [%s](#section:Computability_Theory).

Perfect induction
: Induction by Bayes’ Rule using the true prior distribution on hypotheses, i.e., the one governing the source of the observations. See Section [%s](#reasoning:up_to_computability).

Plain Kolmogorov complexity
: The length $C(a \mid b)$ of a shortest description of a finitary object $a$ given $b$ by the universal machine. See Section [%s](#section:Prefix_Comlexity).

Point-to-Set Principle
: J. Lutz and N. Lutz's theorem that the Hausdorff dimension of a set is the least, over all oracles, of the supremum of its points' effective dimensions relative to that oracle. See Theorem [%s](#theorem:PTS_for_H_dimension).

Pointwise stability
: The property that the effective Hausdorff dimension of a set is the supremum of the effective dimensions of its points. See Section [%s](#section:Effective_Hausdorff_Dimension).

Prefix complexity
: The length $K(a \mid b)$ of a shortest description of a finitary object $a$ given $b$ by the universal prefix-free machine; it may be relativized to an oracle. See Section [%s](#section:Prefix_Comlexity).

Prefix complexity of a set
: The lift of conditional prefix complexity to subsets of Euclidean space, through their rational points. See Section [%s](#section:Lifting_Prefix_Complexity_to_Reals).

Prefix discrepancy
: The gap $\operatorname{\Delta P}_\rho(\sigma) := K(\sigma) + \log \rho([\sigma])$ between a string's prefix complexity and its mass under a premeasure $\rho$. See Definition [%s](#definition:algorithmic_discrepancies).

Prefix weight
: The supremum $\operatorname{PW}_\rho(\mathcal{V})$ of the direct weights of the prefix-free subsets of a collection of strings. See Definition [%s](#definition:weights).

Prefix-free
: A set of strings no two of which are comparable. See the [Notation](#section:Notation) page.

Prefix-free machine
: An oracle machine whose domain is prefix-free for every oracle. See Section [%s](#section:Prefix_Comlexity).

Premeasure
: A non-negative function on a collection of sets, which also evaluates to zero on the empty set. See Definition [%s](#definition:premeasure).

Random
: A sequence is $\mathcal{T}$-$\rho$-random if it passes every test of type $\mathcal{T}$ for the premeasure $\rho$; otherwise it is effectively $\mathcal{T}$-$\rho$-null. See Section [%s](#section:Algorithmic_Randomness).

Randomness
: Inscrutability with respect to the tools availabl. E.g., Shannon entropy for all algorithms, Kolmogorov complexity for effective algorithms, epiplexity for roughly polynomial-time ones. See Section [%s](#reasoning:computability).

Rapidly decreasing
: A sequence of positive rationals that tends to $0$ faster than $2^{-n}$. See Section [%s](#section:Semimeasures).

Reasoning
: Any procedure for assigning and updating likelihoods to a class of hypotheses. See Section [%s](#reasoning:primitives).

Relativization
: Generalizing notions or results from Turing machines to oracle machines with an arbitrary oracle. See Section [%s](#section:Computability_Theory).

Selection
: Any procedure for selecting or preferring a hypothesis. See Section [%s](#reasoning:primitives).

Solomonoff induction
: A method for performing perfect induction over any computable prior probability distribution, using Bayes’ Rule. See Section [%s](#reasoning:up_to_computability).

Solovay test
: A c.e. set of strings with finite direct weight; a strong Solovay test has finite prefix weight instead. See Definition [%s](#definition:tests).

Strong dimension
: The effective analogue of packing dimension: defined by the upper incompressibility ratio. See Section [%s](#section:Effective_Hausdorff_Dimension).

Strongly convex premeasure
: A premeasure on Cantor space whose value on each one-bit extension of a string is at least half its value on that string. See Section [%s](#section:Measures_and_Hausdorff_Dimension).

Strongly covers
: A sequence of sets strongly covers a set if every element of that set lies in infinitely many of them. See Definition [%s](#definition:strongly_covers).

Sub-linear term
: A term $o(r)$ that grows more slowly than any positive multiple of $r$. See the [Notation](#section:Notation) page.

Subadditivity
: The property of a function that its value on a whole is at most the sum of its values on the parts. E.g., prefix complexity is subadditive on pairs up to an additive constant, while outer measures are subadditive on unions. See Section [%s](#section:Prefix_Comlexity).

Succeed
: A supergale succeeds on a set if its capital is unbounded along every point of that set; a continuous semimeasure $\rho$-succeeds if its mass outpaces $\rho$ by an unbounded factor along the prefixes of every point. See Section [%s](#section:Semimeasures).

Supergale
: A betting strategy that wagers on the successive bits of an infinite binary string, recording its capital after each finite prefix, in a game whose odds are set by a premeasure $\rho$. See Section [%s](#section:Semimeasures).

Symmetry of information
: Another name for the chain rule for prefix complexity. See Theorem [%s](#theorem:chain_rule_for_K).

Total
: A partial function defined on the entire space of finitary objects. See Section [%s](#section:Computability_Theory).

Turing machine
: Turing's model of computation: a finite program reading and writing symbols on an unbounded tape. By the Church–Turing thesis, the functions Turing machines compute are exactly the intuitively computable ones. See Section [%s](#section:Computability_Theory).

Turing reducible
: $A \leq_{\operatorname{T}} B$ if some oracle machine computes $A$ from the oracle $B$; also called $B$-computable. See Section [%s](#section:Computability_Theory).

Two-part description
: A description of $a$ by a finite set $A \ni a$ together with $a$'s index in $A$, giving $K(a) \leq K(A) + \log \abs{A} + O(1)$. See Section [%s](#section:Prefix_Comlexity).

Uniformly continuous function
: A real function with a modulus of uniform continuity. See Section [%s](#section:Effective_Dimension_under_Uniformly_Continuous_Maps).

Universal complexity notion
: A complexity notion that dominates, simulates, or otherwise approximates an extremal score among a class of complexity notions. See Section [%s](#reasoning:computability).

Universal prior distribution
: A lower-semicomputable continuous semimeasure that dominates every other, up to a multiplicative constant. See Section [%s](#reasoning:up_to_computability).

Universal Turing machine
: A Turing machine computing a universal partial computable function which simulates every other machine. See Section [%s](#section:Computability_Theory).

Vehement weight
: The infimum of the direct weights of all collections of strings covering the open set generated by a set. See Definition [%s](#definition:weights).
:::
