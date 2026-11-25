---
title: "Optimal Oracles via Kolmogorov Complexity"
label: section:Optimal_Oracles_via_Kolmogorov_Complexity
description: "Stull's optimal Hausdorff oracles via Kolmogorov complexity, equivalent full-dimensional forms, which sets have them, and the connection to Marstrand's projection theorem."
---

By the {term}`Point-to-Set Principle` (Theorem [%s](#theorem:PTS_for_H_dimension)), every set $X \subseteq \mathbb{R}^m$ has a {term}`Hausdorff oracle`: that is, an oracle $A$ with $\sup_{x \in X} \dim^A(x) = \dim_{\operatorname{H}}(X)$. Intuitively, this means that a Hausdorff oracle is one which can compute approximations to *all* points of $X$ powerfully enough to recover the classical dimension of $X$.

But Hausdorff oracles are far from unique. Computing with extra oracle power can't meaningfully increase complexity, so if $A$ is a Hausdorff oracle for $X$, then so is the join of $A$ with any other oracle $B$. As $\dim_{\operatorname{H}}(X)$ is a lower-bound to $\sup_{x \in X} \dim^{A, B}(x)$, this oracle $B$ cannot lower the effective dimension assigned to most points of $X$ when joined with $A$. In this sense, $A$ is relatively "optimal" for $X$.

But recall that {term}`effective Hausdorff dimension` is the limit inferior of prefix complexity. It's still possible that $K^{A, B}_r(x)$ could fall significantly below $K^A_r(x)$ at infinitely many precision levels $r \in \omega$ and for some $x \in X$.

D. Stull asked for an oracle which rules this possibility out at almost every precision level, for at least one point of nearly full effective Hausdorff dimension against any join on that oracle {cite:p}`Stu21`. Such an oracle would be even more "optimal" for $X$. Stull's motivation was the {term}`Marstrand-Mattila Projection Theorem` (Theorem [%s](#theorem:marstrand_projection_original)) over $\mathbb{R}^2$: while its classical proof asks $X$ be analytic, Stull showed the conclusion holds for the broader class of sets with optimal Hausdorff oracles: see Theorem [%s](#theorem:Marstrand_optimal_oracles).

In this chapter, we work over Euclidean space $\mathbb{R}^m$.

## Optimal Oracles

The following is Stull's original, algorithmic information theoretic definition for *optimal oracles*. 

:::{prf:definition} Definitions 3 and 26 of {cite:t}`Stu21`
:label: definition:optimal_oracles
An oracle $A$ is an **optimal Hausdorff oracle** for $X$ if:

1. $A$ is a Hausdorff oracle for $X$; and
2. for every oracle $B$ and every $\varepsilon > 0$, there is a point $x \in X$ such that $\dim^{A, B}(x) \geq \dim_{\operatorname{H}}(X) - \varepsilon$ and

$$
\begin{aligned}
(\forall^\infty r) \brk{K^{A, B}_r(x) \geq K^A_r(x) - \varepsilon r}.
\end{aligned}
$$

We say that $X$ **has optimal Hausdorff oracles** if there exists an optimal Hausdorff oracle for $X$.

An analogous formulation defines **optimal packing oracles** via packing oracles and effective packing dimension $\operatorname{Dim}$.
:::

Notice that the second condition asks only for a single point whose complexity the additional oracle $B$ can't reduce by a linear amount at almost every precision. It turns out that this is equivalent to asking the same for *many* such points. Let's collect all the points satisfying this second condition into a set.

:::{prf:definition}
:label: definition:preservation_set
For oracles $A$, $B$ and $\varepsilon > 0$, denote

$$
\begin{aligned}
N_X(A, B, \varepsilon) := \set{x \in X}{(\forall^\infty r) \brk{K^{A, B}_r(x) \geq K^A_r(x) - \varepsilon r}}.
\end{aligned}
$$
:::

:::{prf:proposition} Propositions 4 and 27 of {cite:t}`Stu21`
:label: proposition:full_dimensional_preservation
Let $A$ be an oracle and $\dim_{\operatorname{H}}(X) > 0$. Then $A$ is an optimal Hausdorff oracle for $X$ if and only if $A$ is a Hausdorff oracle for $X$ and $\dim_{\operatorname{H}}(N_X(A, B, \varepsilon)) = \dim_{\operatorname{H}}(X)$ for every oracle $B$ and every $\varepsilon > 0$.

An analogous statement holds for optimal packing oracles, replacing all occurrences of $\dim_{\operatorname{H}}$ with $\dim_{\operatorname{P}}$.
:::

:::{prf:proof}
Let $s := \dim_{\operatorname{H}}(X)$, and fix an oracle $B$ and $\varepsilon > 0$.

($\impliedby$) Applying the Point-to-Set Principle (Theorem [%s](#theorem:PTS_for_H_dimension)) to $N_X(A, B, \varepsilon)$ yields:

$$
0 < s = \dim_{\operatorname{H}}(N_X(A, B, \varepsilon)) \leq \sup_{x \in N_X(A, B, \varepsilon)} \dim^{A, B}(x).
$$

so $N_X(A, B, \varepsilon)$ has elements $x \in X$ with $\dim^{A, B}(x) \geq s - \varepsilon$, each of which serves the second condition in Definition [%s](#definition:optimal_oracles).

($\implies$) Suppose instead that $d := \dim_{\operatorname{H}}(N_X(A, B, \varepsilon)) < s$. Then let $C$ be a Hausdorff oracle for $N_X(A, B, \varepsilon)$ and fix $0 < \delta < \min\seq{\varepsilon, s - d}$. 

The second condition of Definition [%s](#definition:optimal_oracles), applied to the additional oracle $B \oplus C$ and tolerance $\delta$, guarantees $\exists x \in X$ with $\dim^{A, B, C}(x) \geq s - \delta$ with

$$K^{A, B, C}_r(x) \geq K^A_r(x) - \delta r \quad (\forall^\infty r).$$

Does $x \stackrel{?}{\in} N_X(A, B, \varepsilon)$? If so, then by the Point-to-Set Principle (Theorem [%s](#theorem:PTS_for_H_dimension)),
$$
s - \delta \leq \dim^{A, B, C}(x) \leq \dim^C(x) \leq d,
$$ 
a contradiction to $d < s - \delta$. Otherwise, for infinitely many $r \in \omega$,

$$
\begin{aligned}
K^A_r(x) - \delta r \leq K^{A, B, C}_r(x) \leq^+ K^{A, B}_r(x) <^+ K^A_r(x) - \varepsilon r,
\end{aligned}
$$

a contradiction to $\delta < \varepsilon$.

The proof for optimal packing oracles follows the same form.
:::

We can't ask much more from the statement of Proposition [%s](#proposition:full_dimensional_preservation).

:::{prf:observation}
:label: observation:preservation_set_observations

**No single point may serve every additional oracle**. 

In particular, $\dim^{A, x}(x) = 0$ precludes $x$ from serving against itself: $B := x$.

**Few points can have their complexity under the original oracle always preserved**.

For a fixed $\varepsilon > 0$, the condition $x \in N_X(A, x, \varepsilon)$ implies
$$
K^A_r(x) \leq K^{A, x}_r(x) + \varepsilon r \leq^+ K(r) + \varepsilon r\quad (\forall^\infty r),
$$

so, $\operatorname{dim}^A(x) \leq \operatorname{Dim}^A(x) \leq \varepsilon$. That already shows that every $x \in X$ which lies in $N_X(A, B, \varepsilon)$ for all $B$ has $\operatorname{Dim}^A(x) \leq \varepsilon$. By the Point-to-Set Principle for packing dimension (Theorem [%s](#theorem:PTS_for_Packing_dimension)), this implies 
$$
\dim_{\operatorname{H}}\Big(\bigcap_B N_X(A, B, \varepsilon)\Big) \leq \dim_{\operatorname{P}}\Big(\bigcap_B N_X(A, B, \varepsilon)\Big) \leq \varepsilon.
$$

So, although each $N_X(A, B, \varepsilon)$ is full-dimensional, that set must change with $B$.
:::

Additionally, Proposition [%s](#proposition:full_dimensional_preservation) ignores dimension zero sets. That case is trivial.

:::{prf:observation}
:label: observation:dimension_zero_optimal_oracles
Every non-empty $X \subseteq \mathbb{R}^m$ with $\dim_{\operatorname{H}}(X) = 0$ has optimal Hausdorff oracles.

Similar for optimal packing oracles.
:::

:::{prf:proof}
Take $x_0 \in X$ and a Hausdorff oracle $A_0$ for $X$. Put $A := A_0 \oplus x_0$, which is still a Hausdorff oracle for $X$.

Fix $B$ and $\varepsilon > 0$. Trivially, $\dim^{A, B}(x_0) \geq 0 = \dim_{\operatorname{H}}(X)$. Since $A$ computes $x_0$, we have for all but finitely many $r \in \omega$ that:
$$
K^{A, B}_r(x_0) \geq 0 \geq K(r) - \varepsilon r \geq^+ K^A_r(x_0) - \varepsilon r.
$$
:::

## Known Results

The following are results of {cite:t}`Stu21` related to having optimal oracles. First, closure under natural operations on oracles and sets.

:::{prf:theorem} Lemmas 5, 28, and 30, Observations 6 and 29, and Proposition 7 of {cite:t}`Stu21`
:label: theorem:optimal_oracles_closure

1. If $A$ is an optimal Hausdorff oracle for $X$, then so is $A \oplus B$ for every oracle $B$.
2. If $Y \subseteq X$ has $\dim_{\operatorname{H}}(Y) = \dim_{\operatorname{H}}(X)$ and $Y$ has optimal Hausdorff oracles, then $X$ has optimal Hausdorff oracles.
3. If $X = \bigcup_{n \in \omega} X_n$ and each $X_n$ has optimal Hausdorff oracles, then $X$ has optimal Hausdorff oracles.

Analogous statements hold for optimal packing oracles under $\dim_{\operatorname{P}}$.
:::

Oracles can encode information about measures by, for instance, encoding countably much information on how they assign measure to sets. The following result by D. Stull uses this idea to find a strong enough oracle making $N_X(A, B, \varepsilon)$ take up most of $X$.

:::{prf:lemma} Cf. Lemma 12 of {cite:t}`Stu21`
:label: lemma:preservation_set_conull
Let $\mu$ be a metric outer measure on $\mathbb{R}^m$ with $0 < \mu(X) < \infty$. Then there exists an oracle $A$ such that for every oracle $B$ and every $\varepsilon > 0$, the set $N_X(A, B, \varepsilon)$ is $\mu$-conull in $X$.
:::

:::{prf:proof}
We claim that any oracle $A$ which can lower-semicompute the map $Q \mapsto \mu(X \cap Q)$ on $\mathcal{Q}^m$ suffices.

Since $\mu$ is metric, every Borel set is $\mu$-measurable, so $\nu(E) := \mu(X \cap E)$ defines a finite Borel measure on $\mathbb{R}^m$. By Lemma [%s](#lemma:coding_bound_from_measure) applied to $\nu$, there is a constant $c$ such that for all $x \in \mathbb{R}^m$ and all $r \gg 1$,

$$
\begin{aligned}
K^A_r(x) \leq -\log \mu(X \cap Q_r(x)) + c \log r.
\end{aligned}
$$

By Lemma [%s](#lemma:measure_bound_almost_everywhere) applied to $\nu$ relative to $A \oplus B$, after enlarging $c$, for $\nu$-almost every $x$ (call the exceptional set $E$) and all sufficiently large $r$ we have 
$$
K^{A, B}_r(x) \geq -\log \mu(X \cap Q_r(x)) - c \log r.
$$ 
Thus,
$$
K^{A, B}_r(x) \geq K^A_r(x) - 2c \log r \geq K^A_r(x) - \varepsilon r
$$ 
for all large $r$, so $x \in N_X(A, B, \varepsilon)$. 

The exceptional set $E$ is $\nu$-null, so $\mu(X \setminus N_X(A, B, \varepsilon)) \leq \mu(X \cap E) = \nu(E) = 0$.
:::

:::{prf:theorem} Theorem 13, Lemmas 15, 17, 32, and Corollary 14 of {cite:t}`Stu21`
:label: theorem:optimal_oracles_sufficient
Over Euclidean space:
1. Every {term}`weakly regular` set has optimal Hausdorff oracles.
2. Every {term}`Hausdorff measure-regular` set has optimal Hausdorff oracles.
3. Every {term}`Hausdorff gauge-regular` set has optimal Hausdorff oracles. 
4. Every {term}`s-set` has optimal Hausdorff oracles.
5. Every compact set has optimal Hausdorff oracles.
6. Every $\boldsymbol{\Sigma}^0_2$ set has optimal Hausdorff oracles.
7. Every [analytic set](https://en.wikipedia.org/wiki/Analytic_set) has optimal Hausdorff oracles.
:::
Let's recreate their proofs.
:::{prf:proof}
Many of these are simple consequences of the others. Let $X \subseteq \mathbb{R}^m$ be the set in question. By Observation [%s](#observation:dimension_zero_optimal_oracles), we may assume $\dim_{\operatorname{H}}(X) > 0$.
1. **Weakly regular sets**

Let $s := \dim_{\operatorname{H}}(X) = \dim_{\operatorname{P}}(X)$. We claim that the join $A_{\operatorname{H}} \oplus A_{\operatorname{P}}$ of any Hausdorff oracle $A_{\operatorname{H}}$ and any packing oracle $A_{\operatorname{P}}$ for $X$ is itself an optimal Hausdorff oracle for $X$. 

It's obvious by the Point-to-Set Principle (Theorem [%s](#theorem:PTS_for_H_dimension)) that the more powerful oracle $A_{\operatorname{H}} \oplus A_{\operatorname{P}}$ is still a Hausdorff oracle for $X$.

Now fix an oracle $B$ and $\varepsilon > 0$. Apply the Point-to-Set Principle again but to the oracle $A_{\operatorname{H}} \oplus A_{\operatorname{P}} \oplus B$ to pick an $x \in X$ with $\dim^{A_{\operatorname{H}}, A_{\operatorname{P}}, B}(x) > s - \tfrac{\varepsilon}{4}$; and derive for $r \gg 1$:

$$
\begin{aligned}
K_r^{A_{\operatorname{H}}, A_{\operatorname{P}}}(x) &\leq^+ K_r^{A_{\operatorname{P}}}(x)\\
&\leq \dim_{\operatorname{P}}(X) \cdot r + \frac{1}{4} \varepsilon r\\
&= \dim_{\operatorname{H}}(X) \cdot r + \frac{1}{4} \varepsilon r\\
&< \dim^{A_{\operatorname{H}}, A_{\operatorname{P}}, B}(x) \cdot r + \frac{1}{2} \varepsilon r\\
&\leq K_r^{A_{\operatorname{H}}, A_{\operatorname{P}}, B}(x) + \varepsilon r.
\end{aligned}
$$

This shows $A_{\operatorname{H}} \oplus A_{\operatorname{P}}$ is an optimal Hausdorff oracle.

2. **Hausdorff measure-regular sets**

Let $\mu$ witness the Hausdorff measure-regularity of $X$. Let $A_\mu$ be an oracle guaranteed by Lemma [%s](#lemma:preservation_set_conull) for $\mu$ and $X$, let $A_{\operatorname{H}}$ be a Hausdorff oracle for $X$ (which exists by the Point-to-Set Principle [%s](#theorem:PTS_for_H_dimension)), and let $A := A_{\operatorname{H}} \oplus A_\mu$. This more powerful oracle $A$ is still a Hausdorff oracle for $X$.

Now fix an oracle $B$ and $\varepsilon > 0$. By Lemma [%s](#lemma:preservation_set_conull) and its proof, the set $X \setminus N_X(A, B, \varepsilon)$ is $\mu$-null. Since $X$ is Hausdorff measure-regular, deleting a $\mu$-null set from $X$ does not lower its Hausdorff dimension, so

$$
\dim_{\operatorname{H}}(N_X(A, B, \varepsilon)) = \dim_{\operatorname{H}}(X).
$$

As $B$ and $\varepsilon$ were arbitrary, Proposition [%s](#proposition:full_dimensional_preservation) shows that $A$ is an optimal Hausdorff oracle for $X$.

3. **Hausdorff gauge-regular sets**

Every Hausdorff gauge-regular set is Hausdorff measure-regular. If $h$ is the exact gauge witnessing gauge-regularity, then its associated Method II metric outer measure $\mathcal{H}^h$ witnesses measure-regularity.

4. **$s$-sets**

Every $s$-set is Hausdorff gauge-regular, as witnessed by the gauge $h_s$.

5. **Compact sets**

Define $s_n := \dim_{\operatorname{H}}(X) - \frac{1}{n}$ for $n \gg 1$. Since $s_n < \dim_{\operatorname{H}}(X)$, $X$ is not $s_n$-null, so Theorem [%s](#theorem:compact_non_null_compact_s_set_subset) yields a sequence of $s_n$-sets $X_n \subset X$. By above, each $X_n$ has optimal Hausdorff oracles. So, by the third part of Theorem [%s](#theorem:optimal_oracles_closure), so does $\bigcup_n X_n \subseteq X$. But this set is of full dimension:
$$
\dim_{\operatorname{H}} \left(\bigcup_n X_n \right)  = \sup_n \dim_{\operatorname{H}} X_n = \sup_n s_n = \dim_{\operatorname{H}}(X).
$$
So, by the second part of Theorem [%s](#theorem:optimal_oracles_closure), $X$ also has optimal Hausdorff oracles.

6. **$\boldsymbol{\Sigma}^0_2$ sets**

In $\mathbb{R}^m$, one may write any $\boldsymbol{\Sigma}^0_2$ set (i.e., $F_\sigma$ set) as the countable union of compact subsets. Since we have just shown that compact subsets have optimal Hausdorff oracles, we need only apply the third part of Theorem [%s](#theorem:optimal_oracles_closure) to finish.

7. **Analytic sets**

By Theorem [%s](#theorem:Sigma_0_2_subsets_dimension), $X$ has a $\boldsymbol{\Sigma}^0_2$ subset of the same Hausdorff dimension. By above, this subset has optimal Hausdorff oracles. So, by the second part of Theorem [%s](#theorem:optimal_oracles_closure), $X$ does too.
:::

A quick consequence of Theorem [%s](#theorem:optimal_oracles_sufficient) and Proposition [%s](#proposition:full_upper_dimension) recovers Stull's Theorem 13: 

:::{prf:corollary} Theorem 13 of {cite:t}`Stu21`
:label: corollary:Stull_measure_conditions
Let $s := \dim_{\operatorname{H}}(X)$ and let $\mu$ be a metric outer measure with $0 < \mu(X) < \infty$. If either
1. $\mu \ll \mathcal{H}^{s - \varepsilon}$ for every $0 < \varepsilon \leq s$, or 
2. $\mathcal{H}^s \ll \mu$ and $\mathcal{H}^s(X) > 0$,

then $X$ has optimal Hausdorff oracles.
:::

But whether *every* set has optimal oracles actually depends on the axioms of set theory.

:::{prf:theorem} Corollary 16 of {cite:t}`Stu21`
:label: theorem:optimal_oracles_AD
Assuming the Axiom of Determinacy (AD), every $X \subseteq \mathbb{R}^m$ has optimal Hausdorff oracles.
:::

The proof combines the analytic case with the theorem of L. Crone, L. Fishman, and S. Jackson that, under AD, every set has a Borel subset of the same Hausdorff dimension {cite:p}`CFJ20`. Recall that AD contradicts the Axiom of Choice.

:::{prf:theorem} Lemma 18, Theorems 20, 35, and 37, and Corollary 36 of {cite:t}`Stu21`
:label: theorem:optimal_oracles_AC_CH
Assume the Axiom of Choice (AC) and the Continuum Hypothesis (CH).

1. For every $s \in (0, m)$, there is a set $X \subseteq \mathbb{R}^m$ with $\dim_{\operatorname{H}}(X) = s$ that does not have optimal Hausdorff oracles.
2. For every $0 < s_1 < s_2 \leq 1$, there is a set $X \subseteq \mathbb{R}$ with $\dim_{\operatorname{H}}(X) = s_1$ and $\dim_{\operatorname{P}}(X) = s_2$ realizing each of the following: having neither optimal Hausdorff nor optimal packing oracles; having optimal Hausdorff oracles but not optimal packing oracles; and having optimal packing oracles but not optimal Hausdorff oracles.
:::

The original motivation for optimal oracles is Marstrand's projection theorem (Theorem [%s](#theorem:marstrand_projection_original)), here in the planar case $m = 2$, $n = 1$. For $\theta \in [0, \pi]$, let $p_\theta : \mathbb{R}^2 \to \mathbb{R}$ be the projection $p_\theta(z) := z_1 \cos \theta + z_2 \sin \theta$.

:::{prf:theorem} Theorem 22 of {cite:t}`Stu21`
:label: theorem:Marstrand_optimal_oracles
If $X \subseteq \mathbb{R}^2$ has optimal Hausdorff oracles, then for almost every $\theta \in [0, \pi]$,

$$
\begin{aligned}
\dim_{\operatorname{H}}(p_\theta X) = \min\seq{\dim_{\operatorname{H}}(X), 1}.
\end{aligned}
$$
:::

By Theorem [%s](#theorem:optimal_oracles_sufficient), this recovers Marstrand's theorem for analytic sets and the extension of {cite:t}`LS17` to weakly regular sets. Some hypothesis is needed: assuming AC and CH, for every $s \in (0, 1)$ there is a set $X \subseteq \mathbb{R}^2$ with $\dim_{\operatorname{H}}(X) = 1 + s$ but $\dim_{\operatorname{H}}(p_\theta X) = s$ for every $\theta \in (\pi/4, 3\pi/4)$ (Theorem 23 of {cite:t}`Stu21`). Optimal oracles have since been used to construct universal sets of directions for projection theorems {cite:p}`FS24`.

## Witness and Fitness

The two conditions in Definition [%s](#definition:optimal_oracles) play different roles. The first is a **witness** condition: $A$ attains the minimum in a point-to-set principle. The second is a **fitness** condition: $A$ cannot be improved, at almost every precision, by any additional oracle.

:::{prf:definition}
:label: definition:fit_oracle
An oracle $A$ is **Hausdorff-fit** for $X$ if it satisfies the second condition of Definition [%s](#definition:optimal_oracles).
:::

A fit oracle need not be a Hausdorff oracle. For example, let $A$ be an optimal Hausdorff oracle for some $Y \subseteq \mathbb{R}^m$ with $\dim_{\operatorname{H}}(Y) < m$, and pick any $z \in \mathbb{R}^m$ sufficiently random relative to $A$ (so $\dim^A(z) = m$). Then $A$ is Hausdorff-fit for $X := Y \cup \seq{z}$, since the witnesses for $Y$ still serve, but $A$ is not a Hausdorff oracle for $X$.

:::{prf:proposition}
:label: proposition:witness_condition_is_free
The following hold for any oracle $A$.

1. If $A$ is Hausdorff-fit for $X$ and $A_0$ is a Hausdorff oracle for $X$, then $A \oplus A_0$ is an optimal Hausdorff oracle for $X$. In particular, $X$ has optimal Hausdorff oracles if and only if some oracle is Hausdorff-fit for $X$.
2. If $\dim_{\operatorname{H}}(X) > 0$, then $A$ is Hausdorff-fit for $X$ if and only if $\dim_{\operatorname{H}}(N_X(A, B, \varepsilon)) = \dim_{\operatorname{H}}(X)$ for every oracle $B$ and every $\varepsilon > 0$.

An analogous statement holds for packing oracles under $\dim_{\operatorname{P}}$.
:::

:::{prf:proof}
It is easy to see that additional oracle power on the Hausdorff oracle $A_0$ makes $A \oplus A_0$ a Hausdorff oracle for $X$, too.

Given $B$ and $\varepsilon > 0$, apply the fitness of $A$ to the oracle $A_0 \oplus B$ with tolerance $\varepsilon / 2$. This gives $x \in X$ with $\dim^{A, A_0, B}(x) \geq \dim_{\operatorname{H}}(X) - \varepsilon / 2$ and, for all but finitely many $r$:

$$
\begin{aligned}
K^{A, A_0, B}_r(x) \geq K^A_r(x) - \tfrac{\varepsilon}{2} r \geq^+ K^{A, A_0}_r(x) - \tfrac{\varepsilon}{2} r \geq K^{A, A_0}_r(x) - \varepsilon r.
\end{aligned}
$$

For the second part, the proof of Proposition [%s](#proposition:full_dimensional_preservation) never uses the first condition of Definition [%s](#definition:optimal_oracles).
:::

So, for sets of positive dimension, having optimal Hausdorff oracles amounts to a single condition:

$$
\begin{aligned}
(\exists A)(\forall B)(\forall \varepsilon > 0) \brk{\dim_{\operatorname{H}}(N_X(A, B, \varepsilon)) = \dim_{\operatorname{H}}(X)}.
\end{aligned}
$$

