---
title: "Glossary"
label: section:Glossary
numbering:
  title: false
  headings: false
---

Short descriptions of terms defined throughout these notes, each with a link to its full definition. Link to an entry from anywhere with `` {term}`Name` `` or `` {term}`written form <Name>` ``.

:::{glossary}
A priori complexity
: The complexity $\operatorname{KM}(\sigma) := -\log \mathbf{M}(\sigma)$ of a string, given by the optimal lower-semicomputable continuous semimeasure $\mathbf{M}$. See Section [%s](#section:Semimeasures).

A priori discrepancy
: The gap $\operatorname{\Delta M}_\rho(\sigma) := \operatorname{KM}(\sigma) + \log \rho([\sigma])$ between a string's a priori complexity and its mass under a premeasure $\rho$. See Definition [%s](#definition:algorithmic_discrepancies).

A priori probability
: The total weight $Q_M(\sigma) := \sum_{M(\pi) \downarrow = \sigma} 2^{-\operatorname{len}(\pi)}$ of all descriptions of $\sigma$ under a machine $M$. See Definition [%s](#definition:algorithmic_and_a_priori_probability).

Algorithm
: A procedure implementable by an oracle Turing machine equipped with an appropriate oracle. See Section [%s](#reasoning:computability).

Algorithmic probability
: The value $R_M(\sigma) := 2^{-C_M(\sigma)}$ given by a string's shortest description under a machine $M$. See Definition [%s](#definition:algorithmic_and_a_priori_probability).

Arithmetic hierarchy
: Kleene's classification of sets of natural numbers into levels $\Sigma^0_n$, $\Pi^0_n$, $\Delta^0_n$ by the number of alternating quantifiers needed to define them from a computable relation. See Section [%s](#section:Computability_Theory).

Bayes’ Rule
: A rule for induction updating a hypothesis’s likelihood on additional observations via conditional probabilities. See Section [%s](#reasoning:principles).

Bi-uniformly continuous
: A bijection that is both uniformly continuous and co-uniformly continuous; "bi-Lipschitz" and "bi-Hölder" are used likewise. See Section [%s](#section:Effective_Dimension_under_Uniformly_Continuous_Maps).

Cauchy representation
: A map $\phi : \omega \to \mathbb{D}^m$ with $\phi(r) \in \mathbb{D}^m_r$ and $\abs{\phi(r) - x} \leq 2^{-r}$ for all $r$; it is standard if moreover $\phi(r) \leq x < \phi(r) + 2^{-r}$. See Section [%s](#section:Computability_Theory).

Chain rule
: Gács's identity $K(\sigma, \tau \mid \zeta) = K(\sigma \mid \zeta) + K(\tau \mid \sigma, K(\sigma), \zeta) \pm O(1)$ for prefix complexity, also called symmetry of information. See Theorem [%s](#theorem:chain_rule_for_K).

Co-Lipschitz constant
: A constant $C \geq 0$ with $C \cdot \norm{x_1 - x_2} \leq \norm{f(x_1) - f(x_2)}$ for all $x_1, x_2$. See Section [%s](#section:Effective_Dimension_under_Uniformly_Continuous_Maps).

Co-uniformly continuous
: An injection whose inverse is uniformly continuous; "co-Lipschitz" and "co-Hölder" are used likewise. See Section [%s](#section:Effective_Dimension_under_Uniformly_Continuous_Maps).

Coding Theorem
: Levin's theorem that $K(\sigma)$, $-\log R(\sigma)$, $-\log Q(\sigma)$, and $-\log \mathbf{m}(\sigma)$ agree up to an additive constant. See Theorem [%s](#theorem:coding_theorem).

Comparable
: Two strings are comparable ($\sigma \mid\mid \tau$) if one extends the other. See the [Notation](#section:Notation) page.

Complexity notion
: A numerical measure of a hypothesis's inherent complexity against some fixed set of simple primitives; more generally, any map assigning a score to its domain, smaller meaning simpler. See Sections [%s](#reasoning:primitives) and [%s](#reasoning:computability).

Compression algorithm
: An algorithm on finitary objects with an algorithmic inverse on its whole domain, read as compression (forward) and decompression (backward). See Section [%s](#reasoning:computability).

Computable metric space
: A metric space $(\Omega, d)$ with a dense sequence $(\alpha_i)$ for which $(i, j) \mapsto d(\alpha_i, \alpha_j)$ is computable. See Section [%s](#section:Computability_Theory).

Computable Polish space
: A computable metric space whose metric is complete. See Section [%s](#section:Computability_Theory).

Computable real function
: A function $f : \mathbb{R}^m \to \mathbb{R}^n$ computed by an oracle machine that turns any Cauchy representation of $x$ into one of $f(x)$. See Section [%s](#section:Computability_Theory).

Computably compact
: A subset of a computable metric space that is empty or approximable, computably, to within $2^{-k}$ in Hausdorff distance by finite subsets of the dense sequence. See Section [%s](#section:Computability_Theory).

Computably enumerable
: A set that is the domain of a Turing machine; equivalently, empty or the range of a total computable function. Abbreviated c.e. See Section [%s](#section:Computability_Theory).

Conditional dimension
: The lower and upper conditional dimensions $\dim(x \mid y)$ and $\operatorname{Dim}(x \mid y)$: the limits inferior and superior of $K_{r \mid r}(x \mid y) / r$. See Section [%s](#section:Conditional_and_Mutual_Dimensions).

Constructive dimension
: J. Lutz's effective analogue of Hausdorff dimension, $\operatorname{cdim}(X)$: the infimum of $s$ such that some constructive $s$-supergale succeeds on $X$. See Section [%s](#section:Effective_Hausdorff_Dimension).

Constructive supergale
: A lower-semicomputable supergale. See Section [%s](#section:Semimeasures).

Continuous semimeasure
: A map $M : 2^{<\omega} \to [0, 1]$ with $M(\sigma) \geq M(\sigma^\smallfrown 0) + M(\sigma^\smallfrown 1)$ for every string. See Section [%s](#section:Semimeasures).

Convex premeasure
: A premeasure on Cantor space with $\rho(\sigma) \leq \rho(\sigma^\smallfrown 0) + \rho(\sigma^\smallfrown 1)$ for every string. See Section [%s](#section:Measures_and_Hausdorff_Dimension).

Counting Theorem
: Chaitin's bounds on prefix complexity over the strings of a fixed length $n$: the maximum is $n + K(n) \pm O(1)$, and few strings fall far below it. See Theorem [%s](#theorem:chaitin_counting_theorem).

Cover
: A Martin-Löf-type test $(U_n)_n$ covers $X$ if $X \subseteq \bigcap_n [U_n]$; a Solovay-type test covers $X$ if each point of $X$ has infinitely many prefixes in it. Otherwise $X$ passes the test. See Definition [%s](#definition:test_coverings).

Cylinder set
: The set $[\sigma]$ of all infinite binary strings extending a finite string $\sigma$. See the [Notation](#section:Notation) page.

Dimension function
: A non-negative, non-decreasing, right-continuous function $h$ on $[0, \infty)$ with $h(t) = 0$ exactly when $t = 0$. See Section [%s](#section:Measures_and_Hausdorff_Dimension).

Direct weight
: The sum $\operatorname{DW}_\rho(\mathcal{V}) := \sum_{\sigma \in \mathcal{V}} \rho([\sigma])$ of the premeasures of a collection of strings. See Definition [%s](#definition:weights).

Discrete semimeasure
: A map $m : 2^{<\omega} \to [0, 1]$ whose values sum to at most $1$. See Section [%s](#section:Semimeasures).

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
: A map $f$ on Cantor space is $\alpha$-expansive if $\operatorname{len}(\restrict{f(x)}{r}) \geq \alpha \cdot r$ for all but finitely many $r$. See Section [%s](#section:Effective_Dimension_under_Uniformly_Continuous_Maps).

Extension
: A string $\tau$ extends $\sigma$ ($\sigma \preceq \tau$) if it agrees with $\sigma$ on every position of $\sigma$; a proper extension is one with $\sigma \neq \tau$. See the [Notation](#section:Notation) page.

Finitary object
: An element of a standard countable collection such as $\omega$, $2^{<\omega}$, $\mathbb{D}$, or $\mathbb{Q}$, all identified by computable bijections; also called hereditarily finite. See the [Notation](#section:Notation) page.

Hausdorff dimension
: The infimum of $s \geq 0$ for which a set is $\mathcal{H}^s$-null. See Section [%s](#section:Measures_and_Hausdorff_Dimension).

Hausdorff distance
: The infimum of $\varepsilon > 0$ for which two sets are $\varepsilon$-close: every point of each lies within $\varepsilon$ of the other. See Section [%s](#section:Computability_Theory).

Hausdorff oracle
: An oracle $B$ that attains the minimum in the Point-to-Set Principle for a set $X$. See Section [%s](#section:PTS).

Hausdorff outer measure
: A Method II outer measure induced by a Hausdorff premeasure; for $h_s(t) = t^s$ this is the $s$-dimensional Hausdorff outer measure $\mathcal{H}^s$. See Section [%s](#section:Measures_and_Hausdorff_Dimension).

Hausdorff premeasure
: The premeasure $\rho_h := h \circ \diam$ associated to a dimension function $h$. See Section [%s](#section:Measures_and_Hausdorff_Dimension).

Hypothesis
: A model for describing the source of some observations. See Section [%s](#reasoning:primitives).

Hölder continuous
: Uniformly continuous with a modulus of the form $\mu(r) = \ceil{(r + c) / \alpha}$; equivalently $\norm{f(x_1) - f(x_2)} \leq L \norm{x_1 - x_2}^\alpha$, where $\alpha$ is its exponent. See Section [%s](#section:Effective_Dimension_under_Uniformly_Continuous_Maps).

Induction
: Reasoning that reassigns likelihoods to hypotheses upon receiving more observations; also called inductive reasoning. See Section [%s](#reasoning:principles).

Infinitary object
: An object arising from finitary objects by a limiting process, such as an infinite binary string or a real number. See the [Notation](#section:Notation) page.

Information content measure
: Levin's notion: an upper-semicomputable partial function $F : \subseteq 2^{<\omega} \to \omega$ with $\sum_\sigma 2^{-F(\sigma)} \leq 1$. See Section [%s](#section:Semimeasures).

Inverse-modulus
: A modulus of uniform continuity for the inverse of a co-uniformly continuous map. See Section [%s](#section:Effective_Dimension_under_Uniformly_Continuous_Maps).

K-minimizer
: A rational point $x \in X$ with $K(x) = K(X)$; an $\varepsilon$-approximate $K$-minimizer has $K(x) \leq K(X) + \varepsilon$. See Definition [%s](#definition:K_minimizer).

Kraft Inequality
: The bound $\sum_{\sigma} 2^{-K(\sigma)} \leq 1$, a consequence of the universal machine being prefix-free. See Theorem [%s](#theorem:kraft_inequality).

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
: A constant $L \geq 0$ with $\norm{f(x_1) - f(x_2)} \leq L \cdot \norm{x_1 - x_2}$ for all $x_1, x_2$. See Section [%s](#section:Effective_Dimension_under_Uniformly_Continuous_Maps).

Lipschitz continuous
: Uniformly continuous with a modulus of the form $\mu(r) = r + O(1)$; equivalently, having a Lipschitz constant. See Section [%s](#section:Effective_Dimension_under_Uniformly_Continuous_Maps).

Local dimension
: The (lower) local dimension $\dim_{\operatorname{loc}} \mu(X) := \sup_{x \in X} \liminf_r -\log \mu([\restrict{x}{r}]) / r$ of a set with respect to a semimeasure or outer measure. See Definition [%s](#definition:local_dimension).

Locally Lipschitz continuous
: Lipschitz continuous on some open neighborhood of each point of the domain. See Section [%s](#section:Effective_Dimension_under_Uniformly_Continuous_Maps).

Locally optimal
: N. Lutz's optimality property of the outer measure $\boldsymbol{\kappa}(X) := 2^{-K(X)}$ among strongly finite, lower-semicomputable outer measures. See Section [%s](#section:Effective_Hausdorff_Dimension).

Lower incompressibility ratio
: The quantity $\underline{\kappa}(X) := \sup_{x \in X} \liminf_r K(\restrict{x}{r}) / r$, which equals constructive dimension; the same ratio can be taken with a priori complexity in place of $K$. See Section [%s](#section:Effective_Hausdorff_Dimension).

Lower-semicomputable
: A real number, or a real-valued map on a collection of finitary objects (such as a semimeasure), whose lower graph $\set{(n, q)}{q < f(n)}$ is c.e.; equivalently, one approximable from below by a computable left-approximator. For real numbers, also called left-c.e. See Section [%s](#section:Computability_Theory).

Martin-Löf test
: A uniformly-c.e. sequence $(U_n)_n$ of sets of strings with $\operatorname{DW}_\rho(U_n) \leq 2^{-n}$; strong and vehement versions bound the prefix or vehement weight instead. See Definition [%s](#definition:tests).

Method II outer measure
: Rogers's outer measure $\mathcal{H}^\rho$ induced by a premeasure $\rho$, using covers of diameter at most $\delta$ (the $\delta$-contents $\mathcal{H}^\rho_\delta$) and letting $\delta \to 0$. See Section [%s](#section:Measures_and_Hausdorff_Dimension).

Minimal description
: A description $\pi$ of $\sigma$ (given $\tau$) of the least possible length; any $\pi$ with $M^{\overline{\tau}}(\pi) = \sigma$ is an $M$-description. See Section [%s](#section:Prefix_Comlexity).

Minimum Description Length Principle
: A principle of selection preferring the hypothesis with both the simplest description and the simplest explanation of the observations. Abbreviated MDL. See Section [%s](#reasoning:principles).

Modulus and data processing inequalities
: Bounds on how conditional prefix complexity changes under computable, uniformly continuous maps, controlled by their moduli. See Lemma [%s](#lemma:forward_data_processing_conditional).

Modulus of uniform continuity
: A non-decreasing $\mu : \omega \to \omega$ with $\norm{x_1 - x_2} \leq 2^{-\mu(r)} \implies \norm{f(x_1) - f(x_2)} \leq 2^{-r}$. See Definition [%s](#definition:modulus_of_uniform_continuity).

Mutual dimension
: Case and Lutz's lower and upper mutual dimensions $\operatorname{mdim}(x : y)$ and $\operatorname{Mdim}(x : y)$: the limits inferior and superior of $I_{r : r}(x : y) / r$. See Section [%s](#section:Conditional_and_Mutual_Dimensions).

Mutual information
: The algorithmic information $I(a : b \mid c) := K(a \mid c) - K(a \mid b, c)$ shared by finitary objects, lifted to sets and to reals at given precision-levels. See Section [%s](#section:Conditional_and_Mutual_Dimensions).

Neighborhood
: The $\delta$-neighborhood $B_\delta(A) := \set{x}{d(x, A) < \delta}$ of a set $A$ in a metric space. See the [Notation](#section:Notation) page.

Null set
: A set of outer measure zero: $\mu$-null if $\mu(X) = 0$, and $s$-null if $\mathcal{H}^s(X) = 0$. See Section [%s](#section:Measures_and_Hausdorff_Dimension).

Observations
: Data observed from some source. See Section [%s](#reasoning:primitives).

Occam’s Razor Principle
: A principle of selection preferring the simplest hypothesis consistent with all observations; more generally, that simpler hypotheses ought to get greater likelihoods. See Section [%s](#reasoning:principles).

Optimal
: An element of a class (of semimeasures, supergales, outer measures, ...) that dominates every other element of the class up to a multiplicative constant: $\mu \geq \beta \cdot \nu$ for some constant $\beta > 0$ depending on $\nu$. Often called universal. For example, $\mathbf{m}$ and $\mathbf{M}$ are optimal among the lower-semicomputable discrete and continuous semimeasures, respectively. See Section [%s](#section:Semimeasures).

Optimal cover
: A cover $S^*$ of a set of strings $S$ whose direct weight equals the vehement weight of $S$. See Definition [%s](#definition:optimal_cover).

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
: Induction by Bayes’ Rule using the true prior distribution on hypotheses, i.e., the one actually governing the source of the observations. See Section [%s](#reasoning:up_to_computability).

Plain Kolmogorov complexity
: The length $C(\sigma \mid \tau)$ of a shortest description of $\sigma$ given $\tau$ by the universal machine. See Section [%s](#section:Prefix_Comlexity).

Point-to-Set Principle
: J. Lutz and N. Lutz's formula $\dim_{\operatorname{H}} X = \min_{B} \sup_{x \in X} \dim^B(x)$ expressing Hausdorff dimension through effective dimensions of points. See Theorem [%s](#theorem:PTS_for_H_dimension).

Pointwise stability
: The property $\operatorname{effdim}(X) = \sup_{x \in X} \operatorname{effdim}(x)$ of effective Hausdorff dimension. See Section [%s](#section:Effective_Hausdorff_Dimension).

Prefix complexity
: The length $K(\sigma \mid \tau)$ of a shortest description of $\sigma$ given $\tau$ by the universal prefix-free machine; it may be relativized to an oracle. See Section [%s](#section:Prefix_Comlexity).

Prefix complexity of a set
: The lift $K(X \mid Y)$ of prefix complexity to subsets of Euclidean space, through their rational points; applied to balls it gives $K_{r \mid s}(x \mid y)$ for reals at given precision-levels. See Section [%s](#section:Lifting_Prefix_Complexity_to_Reals).

Prefix discrepancy
: The gap $\operatorname{\Delta P}_\rho(\sigma) := K(\sigma) + \log \rho([\sigma])$ between a string's prefix complexity and its mass under a premeasure $\rho$. See Definition [%s](#definition:algorithmic_discrepancies).

Prefix weight
: The supremum $\operatorname{PW}_\rho(\mathcal{V})$ of the direct weights of the prefix-free subsets of a collection of strings. See Definition [%s](#definition:weights).

Prefix-free
: A set of strings no two of which are comparable. See the [Notation](#section:Notation) page.

Prefix-free machine
: An oracle machine whose domain is prefix-free for every oracle. See Section [%s](#section:Prefix_Comlexity).

Premeasure
: A function $\rho : \mathcal{C} \to [0, +\infty]$ on a collection of sets containing $\emptyset$, with $\rho(\emptyset) = 0$. See Definition [%s](#definition:premeasure).

Random
: A sequence is $\mathcal{T}$-$\rho$-random if it passes every test of type $\mathcal{T}$ for the premeasure $\rho$; otherwise it is effectively $\mathcal{T}$-$\rho$-null. See Section [%s](#section:Algorithmic_Randomness).

Randomness
: Inscrutability with respect to the tools available: Shannon entropy for all algorithms, Kolmogorov complexity for effective algorithms, epiplexity for roughly polynomial-time ones. See Section [%s](#reasoning:computability).

Rapidly decreasing
: A sequence $(q_n)_n$ of positive rationals with $q_n \cdot 2^n \to 0$. See Section [%s](#section:Semimeasures).

Reasoning
: Any procedure for assigning and updating likelihoods to a class of hypotheses. See Section [%s](#reasoning:primitives).

Relativization
: Generalizing notions or results from Turing machines to oracle machines with an arbitrary oracle. See Section [%s](#section:Computability_Theory).

Selection
: Any procedure for selecting or preferring a hypothesis. See Section [%s](#reasoning:primitives).

Solomonoff induction
: A method for performing perfect induction over any computable prior probability distribution, using Bayes’ Rule. See Section [%s](#reasoning:up_to_computability).

Solovay test
: A c.e. set of strings $\mathcal{V}$ with finite direct weight; a strong Solovay test has finite prefix weight instead. See Definition [%s](#definition:tests).

Strong dimension
: The effective analogue of packing dimension, $\operatorname{Dim}(X)$: the upper incompressibility ratio $\sup_{x \in X} \limsup_r K(\restrict{x}{r}) / r$. See Section [%s](#section:Effective_Hausdorff_Dimension).

Strongly convex premeasure
: A premeasure on Cantor space with $\rho(\sigma^\smallfrown i) \geq \rho(\sigma) / 2$ for every string $\sigma$ and bit $i$. See Section [%s](#section:Measures_and_Hausdorff_Dimension).

Strongly covers
: A sequence of sets strongly covers $X$ if every element of $X$ lies in infinitely many of them. See Definition [%s](#definition:strongly_covers).

Sub-linear term
: A term $o(r)$ with $o(r) / r \to 0$ as $r \to \infty$. See the [Notation](#section:Notation) page.

Subadditivity
: The bound $K(\sigma, \tau) \leq K(\sigma) + K(\tau) + O(1)$, a consequence of the chain rule. See Section [%s](#section:Prefix_Comlexity).

Succeed
: A supergale succeeds on $X$ if it wins unboundedly along every point of $X$; a continuous semimeasure $M$ $\rho$-succeeds if $M(\restrict{x}{r}) / \rho([\restrict{x}{r}])$ is unbounded along every point. See Section [%s](#section:Semimeasures).

Supergale
: A betting strategy $\delta$ with $\delta(\sigma) \rho([\sigma]) \geq \delta(\sigma^\smallfrown 0) \rho([\sigma^\smallfrown 0]) + \delta(\sigma^\smallfrown 1) \rho([\sigma^\smallfrown 1])$ for a premeasure $\rho$; an $s$-supergale when $\rho = \rho_s$. See Section [%s](#section:Semimeasures).

Symmetry of information
: Another name for the chain rule for prefix complexity. See Theorem [%s](#theorem:chain_rule_for_K).

Total
: A partial function defined on its whole domain, e.g. on all of $\omega$. See Section [%s](#section:Computability_Theory).

Turing machine
: Turing's model of computation: a finite program reading and writing symbols on an unbounded tape. By the Church–Turing thesis, the functions Turing machines compute are exactly the intuitively algorithmic ones. See Section [%s](#section:Computability_Theory).

Turing reducible
: $A \leq_{\operatorname{T}} B$ if some oracle machine computes $A$ from the oracle $B$; also called $B$-computable. See Section [%s](#section:Computability_Theory).

Two-part description
: A description of $n$ by a finite set $A \ni n$ together with $n$'s index in $A$, giving $K(n) \leq K(A) + \log \abs{A} + O(1)$. See Section [%s](#section:Prefix_Comlexity).

Uniformly continuous function
: A real function with a modulus of uniform continuity. See Section [%s](#section:Effective_Dimension_under_Uniformly_Continuous_Maps).

Universal complexity notion
: A complexity notion that dominates, simulates, or otherwise approximates an extremal score among a class of complexity notions. See Section [%s](#reasoning:computability).

Universal prior distribution
: A lower-semicomputable continuous semimeasure that can play the role of any prior distribution in Solomonoff induction without significant loss, such as the optimal continuous semimeasure $\mathbf{M}$. See Section [%s](#reasoning:up_to_computability).

Universal Turing machine
: A Turing machine computing a universal partial computable function $f(e, n) = \Phi_e(n)$, which simulates every other machine. See Section [%s](#section:Computability_Theory).

Vehement weight
: The infimum $\operatorname{VW}_\rho(\mathcal{V})$ of the direct weights of all collections of strings covering $[\mathcal{V}]$. See Definition [%s](#definition:weights).
:::
