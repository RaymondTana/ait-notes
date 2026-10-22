---
title: "Point-to-Set Principles on Net Spaces"
label: section:PTS_on_Net_Spaces
---

Recall the discussion of Section [%s](#section:PTS). It is already well known for Euclidean space that Hausdorff dimension has a pointwise, algorithmic characterization, as originally shown in 2017 by J. Lutz and N. Lutz {cite:p}`LL18`. Even more recently, P. Lutz and J. Miller succeeded at refining the Point-to-Set Principle for the $s$-dimensional Hausdorff outer measures {cite:p}`LM24`. We aim to establish the same point-to-set principles as in Theorem [%s](#theorem:PTS_for_H_dimension), Theorem [%s](#theorem:PTS_log_s_measure_and_sigma_finite), and Corollary [%s](#corollary:PTS_null_or_finite) but for net spaces.

## The Point-to-Set Principle for Hausdorff Dimension

The standard PTS for Hausdorff dimension holds when we restrict Hausdorff dimension to a fixed net. We call this the **Point-to-Net Principle**.

:::{prf:theorem} “Point-to-Net Principle” for Restricted Hausdorff Dimension
:label: theorem:point_to_net_for_single_net
For any net space $(\Omega, \mathcal{N})$ and any $X \subseteq \Omega$,

$$
\begin{aligned}
\dim_{\mathcal{N}}(X) = \inf_{\mathscr{R}} \sup_{x \in X} \operatorname{effdim}_{\mathscr{R}}(x),
\end{aligned}
$$

where the infimum on $\mathscr{R}$ ranges over all $\omega$-presentations of $\mathcal{N}$.
:::

:::{prf:proof}
:nonumber:
By Pointwise Stability [%s](#prop:pointwise_stability_effective_dimension), it suffices to check that

$$
\begin{aligned}
\dim_{\mathcal{N}}(X) = \inf_{\mathscr{R}} \operatorname{effdim}_{\mathscr{R}}(X).
\end{aligned}
$$

It is clear that $\dim_{\mathcal{N}}(X) \leq \inf_{\mathscr{R}} \operatorname{effdim}_{\mathscr{R}}(X)$, since the left-hand side has no computability restriction on the allowed covers.

We will take $\mathscr{R}$ to be an $\omega$-presentation of $\mathcal{N}$ powerful enough to witness $s > \dim_{\mathcal{N}}(X)$. That is, for each $\dim_{\mathcal{N}}(X) < s \in \mathbb{Q}$, there exists a sequence $(U^s_n)_{n \in \omega}$ where each $U^s_n \subseteq \omega$ satisfies $\operatorname{DW}_s(U^s_n) \leq 2^{-n}$ and $(U^s_n)_n$ covers $X$ in the sense of an ML-type test. Then we require $\mathscr{R} \geq_{\operatorname{T}} \bigoplus \set{(U^s_n)_n}{\dim_{\mathcal{N}}(X) < s \in \mathbb{Q}}$.

We claim that such an $\omega$-presentation $\mathscr{R}$ witnesses $\dim_{\mathcal{N}}(X) = \operatorname{effdim}_{\mathscr{R}}(X)$. By definition, if $s > \dim_{\mathcal{N}}(X)$, then $X$ is covered by $(U^s_n)_n$, which is an ML-$\mathscr{R}$-$s$-test. Therefore, $\operatorname{effdim}_{\mathscr{R}}(X) \leq s$ as well. So, by definition, $\operatorname{effdim}_{\mathscr{R}}(X) \leq \dim_{\mathcal{N}}(X)$.
:::

Moreover, if the metric space has a convenient family of nets that can compare to each $s$-dimensional Hausdorff premeasure, then the net dimension and Hausdorff dimension of $X$ should agree.

:::{prf:theorem}
:label: theorem:PTS_for_inf_over_nets
Let $(\Omega, d)$ be a metric space, and suppose that for any $s \geq 0$, there exists a net $\mathcal{N}^s$ on $(\Omega, d)$ and corresponding net premeasure $\rho^s$ comparable to the $s$-dimensional premeasure $\rho_s$. Then, for any $X \subseteq \Omega$,

$$
\begin{aligned}
\dim_{\operatorname{H}} X = \dim_{\operatorname{net}}(X) = \inf_{s \geq 0} \dim_{\mathcal{N}^s}(X) = \inf_{s \geq 0} \inf_{\mathscr{R}_s} \sup_{x \in X} \operatorname{effdim}_{\mathscr{R}_s}(x),
\end{aligned}
$$

where for each $s \geq 0$, the infimum on $\mathscr{R}_s$ ranges over all $\omega$-presentations of $\mathcal{N}^s$. The same conclusion holds if for any $s \geq 0$, there exists a net $\mathcal{N}^s$ such that $\restrict{\rho_s}{\mathcal{N}_s} \asymp \rho_s$.

In particular, if a given net $\mathcal{N}$ satisfies $\restrict{\rho_s}{\mathcal{N}} \asymp \rho_s$ for every $s \geq 0$, then for any $X \subseteq \Omega$:

$$
\begin{aligned}
\dim_{\operatorname{H}} X = \dim_{\operatorname{net}}(X) = \dim_{\mathcal{N}}(X) = \inf_{\mathscr{R}} \sup_{x \in X} \operatorname{effdim}_{\mathscr{R}}(x),
\end{aligned}
$$

where $\mathscr{R}$ can be any $\omega$-presentation of $\mathcal{N}$.
:::

:::{prf:proof}
:nonumber:
It is clear that $\dim_{\operatorname{H}} X \leq \dim_{\operatorname{net}}(X)$, as the collection of covers considered for net dimension are all permitted when computing Hausdorff dimension. For the other direction, take any rational $s > \dim_{\operatorname{H}} X$. Take $\mathcal{N}^s$ and $\rho^s$ as guaranteed for this $s$. By definition, $\mathcal{H}^s(X) = 0$. By the assumption that $\rho^s \asymp \rho_s$, it follows that $\mathcal{H}^{\restrict{\rho_s}{\mathcal{N}^s}}(X) = 0$, as well. So, by definition, $s \geq \dim_{\mathcal{N}^s}(X) \geq \dim_{\operatorname{net}}(X)$.

The final equality in the claim follows from the Point-to-Net Principle [%s](#theorem:point_to_net_for_single_net).
:::

Now, Theorems [%s](#theorem:effective_dimension_net_spaces) and [%s](#theorem:point_to_net_for_single_net) combine to give the usual Point-to-Set Principle.

:::{prf:corollary}
:label: corollary:PTS_for_computable_grate_spaces
Let $(\Omega, d, \mathcal{N}, \mathscr{R}, \alpha)$ be a computable grate space where $\mathcal{N}$ is layered-disjoint and satisfies $\restrict{\rho_s}{\mathcal{N}} \asymp \rho_s$ for every $s \geq 0$. Then, for any $X \subseteq \Omega$,

$$
\begin{aligned}
\dim_{\operatorname{H}} X = \min_{B \in 2^\omega} \sup_{x \in X} \dim^B(x),
\end{aligned}
$$

where $\dim$ is any of the following effective dimension notions: $\dim_{\operatorname{loc}}\mathbf{M}$, $\dim_{\operatorname{loc}}\mathbf{m}$, $\dim_{\operatorname{loc}}\boldsymbol{\kappa}$, $\operatorname{cdim}$, $\underline{\gamma}$, $\underline{\eta}$, or $\operatorname{effdim}$.
:::

## Point-to-Set Principles for Hausdorff Measures

We now confirm that the point-to-set principles regarding the family of $s$-dimensional Hausdorff outer measures by P. Lutz and J. Miller extend to any net space $(\Omega, \mathcal{N})$.

First, though, we should extend the complexity-characterizations of partial randomness which hold over Cantor space in Theorem [%s](#theorem:complexity_characterizations_of_randomness). Once again, the limiting behavior of the prefix discrepancy characterizes Martin-Löf and Solovay randomness, whereas the limiting behavior of the **a priori** discrepancy characterizes their strong forms.

::::{prf:theorem}
:label: theorem:entropy_characterizations_of_randomness
Let $s$ be left-c.e. and $(\Omega, \mathcal{N}, \mathscr{R})$ be a represented net space. Then, for any point $x \in \Omega$,

:::{div}
:class: roman-list
1. $x$ is ML-$\mathscr{R}$-$s$-random if and only if $\operatorname{\Delta P}^{\mathscr{R}}_s(i_n) \geq c$,
1. $x$ is Solovay-$\mathscr{R}$-$s$-random if and only if $\operatorname{\Delta P}^{\mathscr{R}}_s(i_n) \to + \infty$,
1. $x$ is strong ML-$\mathscr{R}$-$s$-random if and only if $\operatorname{\Delta M}^{\mathscr{R}}_s(i_n) \geq c$,
1. $x$ is strong Solovay-$\mathscr{R}$-$s$-random if and only if $\operatorname{\Delta M}^{\mathscr{R}}_s(i_n) \to + \infty$,
:::

for each $\mathcal{N}$-name $(i_n)_n \in \mathcal{R}(x)$ and some constant $c$ which may depend on $(i_n)_n$.
::::

To begin, consider the following lemma relevant to strong Solovay randomness.

::::{prf:lemma}
:label: lemma:strong_Solovay_test_vs_bounded_Delta_A
Let $s$ be left-c.e., $\mathscr{R}$ an $\omega$-presentation of the net $\mathcal{N}$, and $x \in \Omega$.

:::{div}
:class: roman-list
1. Suppose $\liminf_n \operatorname{\Delta M}^{\mathscr{R}}_s(i_n) \leq c$ for some $\mathcal{N}$-name $(i_n)_n \in \mathcal{R}(x)$ and constant $c$. Then there exists a c.e. strong Solovay-$\mathscr{R}$-$s$-test $\mathcal{V}$ covering $x$ with $\operatorname{PW}_s(\mathcal{V}) \leq 2^c$.

1. Suppose $(\mathcal{V}_k)_{k \in \omega}$ is a uniformly $\mathscr{R}$-c.e. sequence of strong Solovay-$\mathscr{R}$-$s$-tests and $\seq{c_k}_{k \in \omega}$ is an $\mathscr{R}$-computable sequence of integers such that for each $k$: $\operatorname{PW}_s(\mathcal{V}_k) \leq 2^{c_k}$. Then for any $x$ covered by all $\mathcal{V}_k$ using a common $\mathcal{N}$-name $(i_n)_n \in \mathcal{R}(x)$, and for each $k \in \omega$,

   $$
   \begin{aligned}
   \liminf_{n \to \infty} \operatorname{\Delta M}^{\mathscr{R}}_s(i_n) \leq^+ c_k + k,
   \end{aligned}
   $$

   where the additive constant does not depend on $x$ nor $k$.
:::
::::

::::{prf:proof}
:nonumber:
:::{div}
:class: roman-list
1. Define

   $$
   \begin{aligned}
   \mathcal{V} := \set{i \in \omega}{\operatorname{\Delta M}^{\mathscr{R}}_s(i) < c}.
   \end{aligned}
   $$

   Clearly, $\mathcal{V}$ covering $x$ is witnessed by the $\mathcal{N}$-name $(i_n)_n$ of $x$ from the assumption. Now, take any $\mathcal{E} \sqsubseteq_{\operatorname{PF}} \mathcal{V}$. By the definition of $\mathcal{V}$ and by Proposition [%s](#mutually_incomparable_continuous_semimeasure_property),

   $$
   \begin{aligned}
   \operatorname{DW}_s(\mathcal{E}) &= \sum_{i \in \mathcal{E}} \diam(i)^s \leq 2^c \sum_{i \in \mathcal{E}} 2^{-\operatorname{KM}^\mathscr{R}(i)} = 2^c \sum_{i \in \mathcal{E}} \mathbf{M}(i) \leq 2^c.
   \end{aligned}
   $$

   So, $\mathcal{V}$ is a strong Solovay-$\mathscr{R}$-$s$-test covering $x$ with $\operatorname{PW}_s(\mathcal{V}) \leq 2^c$.

1. For each $k \in \omega$ define the map $M_k: \omega \to [0, 1]$ (and $M: \omega \to [0, 1]$) as follows:

   $$
   \begin{aligned}
   M_k(i) := \frac{1}{2^{c_k + 1}} \operatorname{PW}_s(\set{j \in \mathcal{V}_k}{\operatorname{in}(j, i)}); \quad M(i) := \sum_{k \in \omega} \frac{M_k(i)}{2^{k + 1}}.
   \end{aligned}
   $$

   We claim that each $M_k$–as well as $M$–is an $\mathscr{R}$-lower-semicomputable continuous net semimeasure. Lower-semicomputability is clear since one may approximate the prefix $s$-weight from below by computing direct $s$-weights on prefix-free subsets. The sum of any $M_k$ across the roots of the net cannot exceed $\frac{1}{2^{c_k + 1}} \operatorname{PW}_s(\mathcal{V}_k) \leq \frac{2^{c_k + 1}}{2^{c_k + 1}} = 1$. And for any $i$ and $\mathcal{E} \sqsubseteq_{\operatorname{PF}} i$,

   $$
   \begin{aligned}
   \sum_{e \in \mathcal{E}} M_k(e) &= \frac{1}{2^{c_k + 1}} \sum_{e \in \mathcal{E}} \operatorname{PW}_s(\set{j \in \mathcal{V}_k}{\operatorname{in}(j, e)})\\
   &= \frac{1}{2^{c_k + 1}} \operatorname{PW}_s\p{ \bigcup_{e \in \mathcal{E}} \set{j \in \mathcal{V}_k}{\operatorname{in}(j, e)}}\\
   &\leq \frac{1}{2^{c_k + 1}} \operatorname{PW}_s(\set{j \in \mathcal{V}_k}{\operatorname{in}(j, i)})\\
   &= M_k(i).
   \end{aligned}
   $$

   The same inequalities extend to $M$. Furthermore, for any $i \in \mathcal{V}_k$, we have

   $$
   \begin{aligned}
   M_k(i) = \frac{1}{2^{c_k + 1}} \operatorname{PW}_s(\set{j \in \mathcal{V}_k}{\operatorname{in}(j, i)}) \geq \frac{1}{2^{c_k + 1}} \operatorname{DW}_s(\seq{i}) = \frac{1}{2^{c_k + 1}} \diam(i)^s.
   \end{aligned}
   $$

   Let $x \in \Omega$ be covered by all $\mathcal{V}_k$ as witnessed by a fixed $\mathcal{N}$-name $(i_n)_n \in \mathcal{R}(x)$. We conclude that for each $k$, there are infinitely many $n \in \omega$ for which

   $$
   \begin{aligned}
   \operatorname{KM}^{\mathscr{R}}(i_n) \leq^+ - \log M(i_n) \leq - s \log \diam(i_n) + (c_k + 1) + (k + 1).
   \end{aligned}
   $$
:::
::::

::::{prf:proof} Proof of Theorem [%s](#theorem:entropy_characterizations_of_randomness)
:nonumber:
:::{div}
:class: roman-list
1. First assume that $x$ is not ML-$\mathscr{R}$-$s$-random, hence covered by some ML-$\mathscr{R}$-$s$-test $\mathcal{U} = (U_n)_n$. For each $n \in \omega$, define the map $m_n : \omega \to \mathbb{R}$:

   $$
   \begin{aligned}
   m_n(i) := \begin{cases}
   \frac{n}{2} \diam(i)^s & \text{if } i \in U_n\\
   0 & \text{otherwise},
   \end{cases}
   \end{aligned}
   $$

   as well as the map $m: \omega \to \mathbb{R}$:

   $$
   \begin{aligned}
   m(i) := \sum_{n \in \omega} m_n(i).
   \end{aligned}
   $$

   Each $m_n$ is lower-semicomputable in $\mathscr{R}$ via $\mathscr{R}$-computable partial sums using the enumerations of each $U_n$ and by approximating $s$ from below. So too then is $m$ lower-semicomputable in $\mathscr{R}$. Moreover, all of these maps are discrete net semimeasures, which follows from the following bound:

   $$
   \begin{aligned}
   \sum_{i \in \omega} m(i) = \sum_{i \in \omega} \sum_{n \in \omega} m_n(i) = \sum_{n \in \omega} \frac{n}{2} \sum_{i \in U_n} \diam(i)^s = \sum_{n \in \omega} \frac{n}{2} \operatorname{DW}_s(U_n) \leq \sum_{n \in \omega} n \cdot 2^{-(n + 1)} = 1.
   \end{aligned}
   $$

   By the Coding Theorem [%s](#theorem:coding_theorem) relativized to $\mathscr{R}$, there exists constant $C$ such that $m(i) \leq C \cdot 2^{-K^{\mathscr{R}}(i)}$ for almost every $i \in \omega$. Take an $\mathcal{N}$-name $(i_n)_n \in \mathcal{R}(x)$ witnessing that $\mathcal{U}$ covers $x$. Fixing $n \geq \ceil{C} + 1$,

   $$
   \begin{aligned}
   K^{\mathscr{R}}(i_n) \leq - \log\p{\frac{m(i_n)}{C}} \leq - \log \p{\frac{n}{2C} \diam(i_n)^s} = -s \log \diam(i_n) - \log \p{\frac{n}{2C}},
   \end{aligned}
   $$

   so $\liminf_{n \to \infty} \Delta \operatorname{P}^{\mathscr{R}}_s(i_n) = - \infty$.

   In the other direction, define for each $n \in \omega$ the $\mathscr{R}$-c.e. set:

   $$
   \begin{aligned}
   U_n := \set{i \in \omega}{\Delta \operatorname{P}^{\mathscr{R}}_s(i) \leq - n}.
   \end{aligned}
   $$

   We assume that there is some $\mathcal{N}$-name $(i_n)_n \in \mathcal{R}(x)$ for which no constant $c$ satisfies $\Delta \operatorname{P}^{\mathscr{R}}_s(i_n) \geq c$. We may refine $(i_n)_n$ that to an $\mathcal{N}$-name of $x$ such that $\Delta \operatorname{P}^{\mathscr{R}}_s(i_n) \leq - n$. That is, $\mathcal{U} = (U_n)_n$ covers $x$. We confirm that $\mathcal{U}$ is an ML-$\mathscr{R}$-$s$-test by bounding the direct $s$-weights and applying the Kraft Inequality [%s](#theorem:kraft_inequality):

   $$
   \begin{aligned}
   \operatorname{DW}_s(U_n) = \sum_{i \in U_n} \diam(i)^s \leq \sum_{i \in U_n} 2^{-K^{\mathscr{R}}(i) - n} = 2^{-n} \sum_i 2^{-K^{\mathscr{R}}(i)} \leq 2^{-n}.
   \end{aligned}
   $$

   Thus, $x$ is not ML-$\mathscr{R}$-$s$-random.

1. Let $x$ not being Solovay-$\mathscr{R}$-$s$-random be witnessed by the Solovay-$\mathscr{R}$-$s$-test $\mathcal{V}$ in $\mathcal{N}$. Build an $\mathscr{R}$-c.e. sequence of **axioms** $\mathcal{A} := \seq{\langle i, \ceil{- s \cdot \log \diam(i)} \rangle}_{i \in \mathcal{V}}$ with

   $$
   \begin{aligned}
   \sum_{i \in \mathcal{V}} 2^{- \ceil{- s \cdot \log \diam(i)}} \leq \operatorname{DW}_s(\mathcal{V}) < +\infty.
   \end{aligned}
   $$

   A standard result attributed to Kraft and Chaitin implies one may demonstrate $K^{\mathscr{R}}(i) < - s \cdot \log \diam(i) + c$ effectively in $\mathscr{R}$ for some $c$ and for each $i \in \mathcal{V}$. This is done by producing a prefix oracle machine which, given $\mathscr{R}$ as the oracle, produces $i$ using a codeword of length approximately $- s \cdot \log \diam(i)$ for all such pairs in $\mathcal{A}$ {cite:p}`LV08`. Take $(i_n)_n \in \mathcal{R}(x)$ to be an $\mathcal{N}$-name of $x$ witnessing that $\mathcal{V}$ covers $x$. Then, for infinitely many $n \in \omega$, we have $i_n \in \mathcal{V}$, so

   $$
   \begin{aligned}
   \liminf_{n \to \infty} \operatorname{\Delta P}^{\mathscr{R}}_s(i_n) < c.
   \end{aligned}
   $$

   In the other direction, we assume that there is an $\mathcal{N}$-name $(i_n)_n \in \mathcal{R}(x)$ and constant $c \in \omega$ such that $\operatorname{\Delta P}^{\mathscr{R}}_s(i_n) < c$ for infinitely many $n \in \omega$. Then

   $$
   \begin{aligned}
   \mathcal{V} := \set{i \in \omega}{\operatorname{\Delta P}^{\mathscr{R}}_s(i_n) < c}
   \end{aligned}
   $$

   is an $\mathscr{R}$-c.e. set which covers $x$ via $(i_n)_n$. We confirm that $\mathcal{V}$ is a Solovay-$\mathscr{R}$-$s$-test using the Kraft Inequality [%s](#theorem:kraft_inequality):

   $$
   \begin{aligned}
   \operatorname{DW}_s(\mathcal{V}) = \sum_{i \in \mathcal{V}} \diam(i)^s \leq \sum_{i \in \mathcal{V}} 2^{c - K^{\mathscr{R}}(i)} \leq 2^c < +\infty.
   \end{aligned}
   $$

1. Suppose there is a strong ML-$\mathscr{R}$-$s$-test $\mathcal{U} = (U_n)_n$ covering $x$. Note that for each $k \in \omega$, we have $\mathcal{V}_k := \bigcup_{n > 2k} U_k$ is a strong Solovay-$\mathscr{R}$-$s$-test covering $x$ and with prefix $s$-weight:

   $$
   \begin{aligned}
   \operatorname{PW}_s(\mathcal{V}_k) \leq \sum_{n > 2k} \operatorname{PW}_s(U_n) \leq \sum_{n > 2k} 2^{-n} = 2^{-2k}.
   \end{aligned}
   $$

   And $(\mathcal{V}_k)_k$ is uniformly $\mathscr{R}$-c.e., so by Lemma [%s](#lemma:strong_Solovay_test_vs_bounded_Delta_A) (ii), there exists an $\mathcal{N}$-name $(i_n)_n \in \mathcal{R}(x)$ such that for each $k \in \omega$,

   $$
   \begin{aligned}
   \liminf_n \operatorname{\Delta M}^{\mathscr{R}}_s(i_n) \leq^+ -2k + k = -k \to -\infty.
   \end{aligned}
   $$

   In the other direction, we suppose there is an $\mathcal{N}$-name $(i_n)_n \in \mathcal{R}(x)$ for which $\liminf_n \operatorname{\Delta M}^{\mathscr{R}}_s(i_n) = - \infty$. Fixing $k \in \omega$, we have $\liminf_n \operatorname{\Delta M}^{\mathscr{R}}_s(i_n) \leq -k$, so by Lemma [%s](#lemma:strong_Solovay_test_vs_bounded_Delta_A) (i), there is a strong Solovay-$\mathscr{R}$-$s$-test $\mathcal{V}_k$ covering $x$ and with $\operatorname{PW}_s(\mathcal{V}_k) \leq 2^{-k}$. The proof of Lemma [%s](#lemma:strong_Solovay_test_vs_bounded_Delta_A) (i) also shows that this sequence $(\mathcal{V}_k)_k$ is uniformly $\mathscr{R}$-c.e., so forms a strong ML-$\mathscr{R}$-$s$-test covering $x$.

1. Suppose there is a strong Solovay-$\mathscr{R}$-$s$-test $\mathcal{V}$ covering $x$. Take $c \in \mathbb{Z}$ sufficiently large so that $\operatorname{PW}_s(\mathcal{V}) \leq 2^c$. By Lemma [%s](#lemma:strong_Solovay_test_vs_bounded_Delta_A) (ii), $\liminf_n \operatorname{\Delta M}^{\mathscr{R}}_s(i_n) \leq^+ c$ for some $\mathcal{N}$-name $(i_n)_n \in \mathcal{R}(x)$. In the other direction, if there were some $c$ and $\mathcal{N}$-name $(i_n)_n \in \mathcal{R}(x)$ for which infinitely many $n \in \omega$ satisfy $\operatorname{\Delta M}^{\mathscr{R}}_s(i_n) \leq c$, then Lemma [%s](#lemma:strong_Solovay_test_vs_bounded_Delta_A) (i) implies there exists a strong Solovay-$\mathscr{R}$-$s$-test $\mathcal{V}$ covering $x$.
:::
::::

The following lemma helps to relate the $s$-dimensional Hausdorff outer measure of a set restricted to a net to the existence of strong Solovay-$s$-tests in that net covering the set.

::::{prf:lemma}
:label: lemma:strong_Solovay_test_vs_s_measure
Let $s > 0$ be left-c.e., $\mathscr{R}$ an $\omega$-presentation of the net $\mathcal{N}$, and $x \in \Omega$.

:::{div}
:class: roman-list
1. Suppose $\mathcal{V}$ is a strong Solovay-$\mathscr{R}$-$s$-test covering $X$. Then $(\restrict{\mathcal{H}}{\mathcal{N}})^s(X) \leq \operatorname{PW}_s(\mathcal{V})$.
1. Suppose $(\restrict{\mathcal{H}}{\mathcal{N}})^s(X) < + \infty$. Then for any $\varepsilon > 0$, there exists an oracle $B \geq_{\operatorname{T}} \mathscr{R}$ and a strong Solovay-$B$-$s$-test $\mathcal{V}$ covering $X$ with $\operatorname{PW}_s(\mathcal{V}) \leq (\restrict{\mathcal{H}}{\mathcal{N}})^s(X) + \varepsilon$.
:::
::::

:::::{prf:proof}
:nonumber:
::::{div}
:class: roman-list
1. It is possible to build a sequence $\mathcal{U} = (U_n)_n$ of prefix-free subsets of $\mathcal{V}$ satisfying:

   - For each $i \in U_n$, we have $\diam(i) \leq 2^{-n}$; and
   - For each $i \in \mathcal{V}$ of $\diam(i) \leq 2^{-n}$, there exist $k \in \omega$ and $j \in U_k$ with $\operatorname{in}(i, j)$.

   Take an arbitrary $x \in X$. Notice that if $\mathcal{V}$ covers $x$, then there is an $\mathcal{N}$-name $(i_n)_n$ of $x$ such that for each $k \in \omega$, there exists $n \in \omega$ such that $i_n \in U_k$. Therefore, each $U_k$ covers $X$ by cover elements of diameter no greater than $2^{-k}$. And since $U_k \sqsubseteq_{\operatorname{PF}} \mathcal{V}$ with $\mathcal{V}$ being a strong Solovay-$\mathscr{R}$-$s$-test $\mathcal{V}$, we conclude:

   $$
   \begin{aligned}
   (\restrict{\mathcal{H}}{\mathcal{N}})^s(X) \leq \sup_{k \in \omega} \operatorname{DW}_s(U_k) \leq \operatorname{PW}_s(\mathcal{V}).
   \end{aligned}
   $$

1. We first build a sequence $\mathcal{U} = (U_n)_n$ subject to a few assumptions: for each $n \in \omega$,

   :::{div}
   :class: alpha-list
   1. $U_n \subseteq \omega$ is contains the indices of a prefix-free colleciton of net elements;
   1. For each $i \in U_n$, we have $\diam(i) \leq 2^{-n}$;
   1. $X \subseteq \bigcup_{i \in U_n} \iota(i)$;
   1. $\operatorname{DW}_s(U_n)$ is minimal to within $2^{-n}$ among all other $\mathcal{U}$ satisfying the above assumptions;
   1. $\operatorname{DW}_s(U_n)$ is minimal with respect to replacements of any collection of any indices by any net element non-trivially intersecting all of them, unless that set has diameter exceeding $2^{-n}$; and
   1. For each $i \in U_{n + 1}$, there exists $j \in U_n$ such that $\operatorname{in}(i, j)$.
   :::

   Given a collection $\mathcal{U}$ satisfying (a)-(e) yet with (f) failing for some smallest $n$ and $i \in U_{n + 1}$, it has to be that either $i$ non-trivially intersects some elements of $U_n$ or not. If so, one could replace $i$ by these intersecting indices in $U_{n + 1}$. Otherwise, since $U_n$ covers $X$, $i$ can be safely removed from $U_{n + 1}$ and still cover $X$. Either way, the problematic index can be resolved. This can be done for each $U_{n + 1}$ in succession, starting with any $U_0$ already satisfying (a)-(e).

   Define $\mathcal{V} := \bigcup_{n > n_0} U_n$ for some sufficiently large $n_0$ such that $2^{-n_0} \leq \varepsilon / 2$. Take $B \in 2^\omega$ to be an oracle powerful enough to both compute $\mathscr{R}$ and $\mathcal{U}$. Then $\mathcal{V}$ is certainly c.e. in $B$. We claim that $\mathcal{V}$ is a strong Solovay-$B$-$s$-test covering $X$.

   Observe that it suffices to bound $\operatorname{PW}_s(\mathcal{V})$ from above by proving the same bound on $\operatorname{DW}_s(\mathcal{E})$ for any finite $\mathcal{E} \sqsubseteq_{\operatorname{PF}} \mathcal{V}$. Fixing such an $\mathcal{E}$, let $n = \max_{i \in \mathcal{E}} \ceil{- \log \diam(i)}$. Then, for each $n' > n$, we have $\mathcal{E} \cap U_{n'} = \emptyset$.

   We now reduce to the case that $\mathcal{E} \subseteq U_n$ with little penalty incurred to the direct $s$-weight of $\mathcal{E}$. Suppose that $i \in \mathcal{E} \setminus U_n$. We replace $i$ in $\mathcal{E}$ with by all indices $j \in U_n$ of net elements non-trivially intersecting with $\iota(i)$. By the definition of $\mathcal{V}$, any such $i$ must have come from $U_k$ for some $k < n$. This proposed replacement could also be performed on $U_k$ itself. By (f), the resulting set would still cover $X$. Now call $\mathcal{E}'_k$ the result of doing this replacement for any violating $i \in \mathcal{E} \cap U_k \setminus U_n$, and $U'_k$ the same but on $U_k$. By (d),

   $$
   \begin{aligned}
   \operatorname{DW}_s(\mathcal{E}) - \operatorname{DW}_s(\mathcal{E}_k') = \operatorname{DW}_s(U_k) - \operatorname{DW}_s(U_k') \leq 2^{-k}.
   \end{aligned}
   $$

   So if $\mathcal{E}'$ denotes the final version of $\mathcal{E}$ after all replacements, we have:

   $$
   \begin{aligned}
   \operatorname{DW}_s(\mathcal{E}) - \operatorname{DW}_s(\mathcal{E}') \leq \sum_{k = n_0 + 1}^{n - 1} 2^{-k} < 2^{-n_0}.
   \end{aligned}
   $$

   Thus, by monotonicity,

   $$
   \begin{aligned}
   \operatorname{DW}_s(\mathcal{E}) < \operatorname{DW}_s(\mathcal{E}') + 2^{- n_0} &\leq \operatorname{DW}_s(U_n) + 2^{- n_0}\\
   &\leq (\restrict{\mathcal{H}}{\mathcal{N}})^s(X) + 2^{-n} + 2^{- n_0}\\
   &\leq (\restrict{\mathcal{H}}{\mathcal{N}})^s(X) + \varepsilon.
   \end{aligned}
   $$

   We conclude that $\operatorname{PW}_s(\mathcal{V}) \leq (\restrict{\mathcal{H}}{\mathcal{N}})^s(X) + \varepsilon$.
::::
:::::

Now we may prove the finer point-to-set principle for the $s$-dimensional Hausdorff outer measures restricted to a net using the limiting behavior of the **a priori** discrepancy.

:::{prf:theorem}
:label: theorem:point_to_set_s_measure
For any $s \geq 0$ and $x \in \Omega$,

```{math}
:label: eqn:log_hausdorff_s_measure
\begin{aligned}
\log (\restrict{\mathcal{H}}{\mathcal{N}})^s(X) =^+ \inf_{\mathscr{R}} \sup_{x \in X} \inf_{(i_n)_n \in \mathcal{R}(x)} \liminf_{n \to \infty} [\operatorname{KM}^{\mathscr{R}}(i_n) + s \cdot \log_2 \diam(i_n)],
\end{aligned}
```

where the infimum on $\mathscr{R}$ ranges over all $\omega$-presentations of $\mathcal{N}$.
:::

:::{prf:proof}
:nonumber:
Let us start by showing that $\log (\restrict{\mathcal{H}}{\mathcal{N}})^s(X)$ does not exceed the right-hand side of ([%s](#eqn:log_hausdorff_s_measure)). Fix an $\omega$-presentation $\mathscr{R}$ of $\mathcal{N}$ and a sufficiently large integer $c \gg 1$ such that

```{math}
:label: eqn:condition_for_Solovay_test_exists
\begin{aligned}
\sup_{x \in X} \inf_{(i_n)_n \in \mathcal{R}(x)} \liminf_{n \to \infty} \operatorname{\Delta M}^{\mathscr{R}}_s(i_n) \leq c.
\end{aligned}
```

By Lemma [%s](#lemma:strong_Solovay_test_vs_bounded_Delta_A) (i) relativized to $\mathscr{R}$, there exists a strong Solovay-$\mathscr{R}$-$s$-test $\mathcal{V}$ covering $X$ with $\operatorname{PW}_s(\mathcal{V}) \leq 2^c$. And so by Lemma [%s](#lemma:strong_Solovay_test_vs_s_measure) (i), $(\restrict{\mathcal{H}}{\mathcal{N}})^s(X) \leq \operatorname{PW}_s(\mathcal{V}) \leq 2^c$.

In the other direction, start by assuming $(\restrict{\mathcal{H}}{\mathcal{N}})^s(X) \leq 2^c < +\infty$ for some integer $c \gg 1$. By Lemma [%s](#lemma:strong_Solovay_test_vs_s_measure) (ii) applied to $\varepsilon := 2^c > 0$ and an $\omega$-presentation $\mathscr{R}_0$ of $\mathcal{N}$, there exists another $\omega$-presentation $\mathscr{R} \geq_{\operatorname{T}} \mathscr{R}_0$ and a strong Solovay-$\mathscr{R}$-$s$-test $\mathcal{V}$ covering $X$ with $\operatorname{PW}_s(\mathcal{V}) \leq 2^{c + 1}$. We can even ask that $\mathscr{R}$ be strong enough so that: $s$ is left-c.e. in $\mathscr{R}$, $(\mathcal{V}_k)_k$ is uniformly $\mathscr{R}$-c.e., and both of these have bounded sizes for their codes in $\mathscr{R}$. Then, by Lemma [%s](#lemma:strong_Solovay_test_vs_bounded_Delta_A) (ii) relativized to $\mathscr{R}$ and applied to $\mathcal{V}_0 := \mathcal{V}$ and $c_0 := c + 1$, ([%s](#eqn:condition_for_Solovay_test_exists)) holds up to an additive constant independent of $x$, $X$, and $s$.
:::

One interpretation of Theorem [%s](#theorem:point_to_set_s_measure) is that the map:

$$
\begin{aligned}
\zeta(X) := \inf_{\mathscr{R}} \sup_{x \in X} \inf_{(i_n)_n \in \mathcal{R}(x)} \liminf_{n \to \infty} \brk{2^{\operatorname{KM}^{\mathscr{R}}(i_n)} \cdot \diam(i_n)^s}
\end{aligned}
$$

is an outer measure on $\Omega$ commensurate with the $s$-dimensional Hausdorff outer measure $\restrict{\rho_s}{\mathcal{N}}$ restricted to $\mathcal{N}$. Now, under the various characterizations provided by Theorem [%s](#theorem:entropy_characterizations_of_randomness), it is straightforward to derive a few other characterizations of the $s$-dimensional Hausdorff outer measures (restricted to a net) from Theorem [%s](#theorem:point_to_set_s_measure).

::::{prf:corollary}
:label: corollary:point_to_set_non_null_and_finite
For any $s \geq 0$ and $X \subseteq \Omega$,

:::{div}
:class: roman-list
1. $(\restrict{\mathcal{H}}{\mathcal{N}})^s(X) > 0$ if and only if

   $$
   \begin{aligned}
   (\forall \mathscr{R} \text{ an $\omega$-presentation of $\mathcal{N}$})(\exists x \in X) \brk{\text{$x$
   is (strong) ML-$\mathscr{R}$-$s$-random}}.
   \end{aligned}
   $$

1. $(\restrict{\mathcal{H}}{\mathcal{N}})^s(X) < +\infty$ if and only if there exists an $\omega$-presentation $\mathscr{R}$ of $\mathcal{N}$ such that

   $$
   \begin{aligned}
   \sup_{x \in X} \inf_{(i_n)_n \in \mathcal{R}(x)} \liminf_{n \to \infty} [\operatorname{KM}^{\mathscr{R}}(i_n) + s \cdot \log_2 \diam(i_n)] < +\infty.
   \end{aligned}
   $$
:::
::::

:::{prf:theorem}
:label: theorem:point_to_set_s_measure_sigma_finiteness
For any $s \geq 0$ and $X \subseteq \Omega$, it holds that $X$ is not $\sigma$-finite with respect to $(\restrict{\mathcal{H}}{\mathcal{N}})^s$ if and only if

$$
\begin{aligned}
(\forall \mathscr{R} \text{ an $\omega$-presentation of $\mathcal{N}$})(\exists x \in X) \brk{\text{$x$
is strong Solovay-$\mathscr{R}$-$s$-random}}.
\end{aligned}
$$
:::

:::{prf:proof}
:nonumber:
We may start by assuming that there is an $\omega$-presentation $\mathcal{N}$ for which there is no element $x \in X$ which is strong Solovay-$\mathscr{R}$-$s$-random. Again by the $s$-$m$-$n$ Theorem, it is possible to uniformly-computably enumerate in $\mathscr{R}$ all of the strong Solovay-$\mathscr{R}$-$s$-tests $(\mathcal{V}_e)_{e \in \omega}$. By assumption, each $x \in X$ is covered by some such test, $\mathcal{V}_e$. By Lemma [%s](#lemma:strong_Solovay_test_vs_s_measure)(i), for each $e \in \omega$

$$
\begin{aligned}
(\restrict{\mathcal{H}}{\mathcal{N}})^s(\set{x \in \Omega}{x \text{ is covered by } \mathcal{V}_e}) \leq \operatorname{PW}_s(\mathcal{V}_e) < + \infty.
\end{aligned}
$$

Thus, $X$ is contained in a union of sets with finite $s$-dimensional Hausdorff outer measure.

In the other direction, suppose $X$ is $\sigma$-finite with respect to $(\restrict{\mathcal{H}}{\mathcal{N}})^s$. Let $(X_k)_{k \in \omega}$ be a sequence witnessing this: $X \subseteq \bigcup_k X_k$, where $(\restrict{\mathcal{H}}{\mathcal{N}})^s(X_k) < + \infty$ for each $k \in \omega$. By Lemma [%s](#lemma:strong_Solovay_test_vs_s_measure)(ii), for each $k \in \omega$, there exists an $\omega$-presentation $\mathscr{R}_k$ of $\mathcal{N}$ and a strong Solovay-$\mathscr{R}_k$-$s$-test $\mathcal{V}_k$ covering $X_k$. And so, letting $\mathscr{R}$ be an $\omega$-presentation which computes all these $\mathscr{R}_k$, we have that each $x \in X$ is covered by some strong Solovay-$\mathscr{R}$-$s$-test.
:::

Similar to Theorem [%s](#theorem:PTS_for_inf_over_nets), if the metric space has a net with net premeasure commensurate with the $s$-dimensional Hausdorff premeasure $\rho_s$, all of these results will apply to the unrestricted $s$-dimensional Hausdorff outer measure $\mathcal{H}^s$. That is, given $s \geq 0$, suppose there exists a net $\mathcal{N}$ and a corresponding net premeasure $\rho = \Theta(\rho_s)$ on $\mathcal{N}$. (Equivalently, one could ask that $\restrict{\rho_s}{\mathcal{N}} = \Theta(\rho_s)$.) Then, for any $X \subseteq \Omega$, the statements of Lemma [%s](#lemma:strong_Solovay_test_vs_s_measure), Theorem [%s](#theorem:point_to_set_s_measure), Corollary [%s](#corollary:point_to_set_non_null_and_finite), and Theorem [%s](#theorem:point_to_set_s_measure_sigma_finiteness) all apply to $\mathcal{H}^s$ in place of $(\restrict{\mathcal{H}}{\mathcal{N}})^s$.
