---
title: "Optimal Oracles via Kolmogorov Complexity"
label: section:Optimal_Oracles_via_Kolmogorov_Complexity
---

By the {term}`Point-to-Set Principle` (Theorem [%s](#theorem:PTS_for_H_dimension)), every set $X \subseteq \mathbb{R}^m$ has a {term}`Hausdorff oracle`: that is, an oracle $A$ with $\sup_{x \in X} \dim^A(x) = \dim_{\operatorname{H}}(X)$. Inuitively, this means that a Hausdorff oracle is one which can compute approximations to *all* points of $X$ powerfully enough to recuperate the classical dimension of $X$.

But Hausdorff oracles are far from unique. Computing with extra oracle power can't meaningfully increase complexity, so if $A$ is a Hausdorff oracle for $X$, then so is the join of $A$ with any other oracle $B$. As $\dim_{\operatorname{H}}(X)$ is a lower-bound to $\sup_{x \in X} \dim^{A, B}(x)$, this oracle $B$ cannot lower the effective dimension assigned to most points of $X$ when joined with $A$. In this sense, $A$ is relatively "optimal" for $X$.

But recall that {term}`effective Hausdorff dimension` is the limit inferior of prefix complexity. It's still possible that $K^{A, B}_r(x)$ could fall significantly below $K^A_r(x)$ at infinitely many precision levels $r \in \omega$ and for some $x \in X$.

D. Stull asked for an oracle which rules this possibility out at almost every precision level, for at least one point of nearly full effective Hausdorff dimension against any join on that oracle {cite:p}`Stu21`. Such an oracle would be even moreso "optimal" for $X$. Stull's motivation was the {term}`Marstrand-Mattila Projection Theorem` (Theorem [%s](#theorem:marstrand_projection_original)): its classical proof needs $X$ to be analytic, while sets with optimal Hausdorff oracles satisfy its conclusion in the plane without any such assumption (Theorem [%s](#theorem:Marstrand_optimal_oracles)).
<!-- Conveniently, Stull's crtieria are well-suited for the types of requirements used for proving projection theorems. For instance, the projection estimate of J. Lutz and D. Stull (Theorem 21 of {cite:t}`Stu21`, from {cite:t}`LS17`) bounds $K^{C, \theta}_r(p_\theta z)$ from below only at those precisions $r$ where the oracle $(C, \theta)$ gives essentially no information about $z$, i.e., where $K^{C, \theta}_r(z) \geq K_r(z) - \varepsilon r$. -->

For the remainder of this page, let $X \subseteq \mathbb{R}^m$ and $s := \dim_{\operatorname{H}}(X) \geq 0$. 

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

So $N_X(A, B, \varepsilon)$ is non-empty. Any of its elements serve the second condition in Definition [%s](#definition:optimal_oracles).

($\implies$) Suppose instead that $d := \dim_{\operatorname{H}}(N_X(A, B, \varepsilon)) < s$. Then let $C$ be a Hausdorff oracle for $N_X(A, B, \varepsilon)$ and fix $0 < \delta < \min\seq{\varepsilon, s - d}$. 

The second condition of Definition [%s](#definition:optimal_oracles), applied to the additional oracle $B \oplus C$ and tolerance $\delta$, guarantees $\exists x \in X$ with $\dim^{A, B, C}(x) \geq s - \delta$ with

$$(\forall^\infty r) K^{A, B, C}_r(x) \geq K^A_r(x) - \delta r.$$

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

We can't ask much more than this: for no single point can serve every additional oracle in general. For instance, any $x \in N_X(A, x, \varepsilon)$, would have $K^A_r(x) \leq K^{A, x}_r(x) + \varepsilon r \leq K(r) + \varepsilon r + O(1)$ for all but finitely many $r$, so $\operatorname{Dim}^A(x) \leq \varepsilon$. By Point-to-Set Principle for packing dimension (Theorem [%s](#theorem:PTS_for_Packing_dimension)), $\dim_{\operatorname{H}}(X) \leq \dim_{\operatorname{P}}(X) \leq \varepsilon$, too. 

The proposition excludes dimension zero. That case is trivial.

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

Several (classical) classes of sets are known to have optimal oracles.

:::{prf:theorem} Theorem 13, Lemmas 15, 17, 32, and 34 of {cite:t}`Stu21`
:label: theorem:optimal_oracles_sufficient
1. Every [analytic set](https://en.wikipedia.org/wiki/Analytic_set) has both optimal Hausdorff oracles and optimal packing oracles.
2. Every {term}`weakly regular` set has both optimal Hausdorff oracles and optimal packing oracles. Moreover, the join of a Hausdorff oracle and a packing oracle for a weakly regular set is an optimal Hausdorff oracle for it.
3. Every {term}`Hausdorff measure-regular` set has optimal Hausdorff oracles.
4. Every {term}`Hausdorff gauge-regular` set has optimal Hausdorff oracles. 
5. Every {term}`s-set` has optimal Hausdorff oracles.
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
The following hold for any Hausdorff oracle $A$.

1. If $A$ is Hausdorff-fit for $X$ and $A_0$ is a Hausdorff oracle for $X$, then $A \oplus A_0$ is an optimal Hausdorff oracle for $X$. In particular, $X$ has optimal Hausdorff oracles if and only if some oracle is Hausdorff-fit for $X$.
2. If $\dim_{\operatorname{H}}(X) > 0$, then $A$ is Hausdorff-fit for $X$ if and only if $\dim_{\operatorname{H}}(N_X(A, B, \varepsilon)) = \dim_{\operatorname{H}}(X)$ for every oracle $B$ and every $\varepsilon > 0$.

An analogous statement holds for packing orcles under $\dim{\operatorname{P}}$.
:::

:::{prf:proof}
For the first part, $A \oplus A_0$ is a Hausdorff oracle because $A_0$ is. Given $B$ and $\varepsilon > 0$, apply the fitness of $A$ to the oracle $A_0 \oplus B$ with tolerance $\varepsilon / 2$. This gives $x \in X$ with $\dim^{A, A_0, B}(x) \geq \dim_{\operatorname{H}}(X) - \varepsilon / 2$ and, for all but finitely many $r$, so

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