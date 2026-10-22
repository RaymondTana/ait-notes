---
title: "Projective and Pinned-Distance Sets"
label: section:Projective_and_Pinned_Distance_Sets
---

In this section we present a simple effective argument which implies results for Hausdorff dimension in multiple geometric setups. These geometries will include pinned-distance sets, radial projections, and orthogonal projections.

:::{prf:definition}
Fix $0 \leq n \leq m$. Given any norm $\normAt{*}{\cdot}$ on $\mathbb{R}^m$, subset $X \subseteq \mathbb{R}^m$, point $z \in \mathbb{R}^m$, and subspace $V \in G(m, n)$, denote

- The **pinned-distance** of $X$ about $z$ by $\Delta^*_z(X) := \set{\normAt{*}{x - z}}{x \in X}$;
- The **radial projection** of $X$ about $z$ by $P_z^*(X) := \set{\frac{x - z}{\normAt{*}{x - z}}}{x \in X}$;
- The **orthogonal projection** of $X$ onto $V$ by $\Pi^*_V(X) := \set{\normAt{*}{\operatorname{proj}_V(x)}}{x \in X}$;

all with respect to the norm $\normAt{*}{\cdot}$. Simply write $\Delta_z(X)$, $P_z(X)$, and $\Pi_V(X)$ when taken with respect to the standard $L^2$-norm.
:::

We start by recalling a result about pinned-distance sets by D. Stull {cite:p}`Stu22_pinned`.

:::{prf:theorem} Theorem 1 in {cite:t}`Stu22_pinned`
:label: theorem:Stull_pinned_distance_theorem
Let $X \subseteq \mathbb{R}^2$ be an analytic set with Hausdorff dimension strictly greater than one. Then, for all $z \in \mathbb{R}^2$ outside a set of Hausdorff dimension at most one,

$$
\begin{aligned}
\dim_{\operatorname{H}}\p{\Delta_z X} \geq \frac{\dim_{\operatorname{H}}X}{4} + \frac{1}{2}.
\end{aligned}
$$
:::

In 2023, I. Altaf, R. Bushling, and B. Wilson proved a related lower-bound for the Hausdorff dimension of pinned-distance sets {cite:p}`ABW23`.

:::{prf:theorem} Theorem 1.2 in {cite:t}`ABW23`
:label: theorem:Bushling_pinned_distance_theorem
For each $m \in \omega$, norm $\normAt{*}{\cdot}$ on $\mathbb{R}^m$, point $z \in \mathbb{R}^m$, and subset $X \subseteq \mathbb{R}^m$,

$$
\begin{aligned}
\dim_{\operatorname{H}}\p{\Delta^*_z X} \geq \dim_{\operatorname{H}}X - (m - 1).
\end{aligned}
$$
:::

It is easy to see that under the conditions of Theorem [%s](#theorem:Stull_pinned_distance_theorem), D. Stull's lower bound is stronger than that of Theorem [%s](#theorem:Bushling_pinned_distance_theorem). But the latter applies more generally: there are no exceptional directions, no dimensionality assumptions on $X$, nor any specificity to the $L^2$-norm.

Recall that the Marstrand-Mattila Projection Theorem [%s](#theorem:marstrand_projection_original) bounds from below the Hausdorff dimension of the orthogonal projection of any analytic set $X \subseteq \mathbb{R}^m$ along all but a $\gamma_{m, n}$-null set of subspaces from $G(m, n)$. Is there a lower bound for orthogonal projections which, as in Theorem [%s](#theorem:Bushling_pinned_distance_theorem), applies without any exceptional directions?

To answer this question, we recall a well-known bound for the Hausdorff dimension of a set which can be decomposed into two components, and provide an effective proof based on that of Theorem [%s](#theorem:Bushling_pinned_distance_theorem).

:::{prf:theorem}
:label: theorem:meta_theorem_two_part_sets_dimension_bound
Let $m, n, \ell\in \omega$ and $X \subseteq \mathbb{R}^m$, $U \subseteq \mathbb{R}^n$, and $W \subseteq \R^\ell$. Suppose there is a locally Lipschitz continuous map $f: U \times W \to \mathbb{R}^m$ surjective on $X$. Then

$$
\begin{aligned}
\dim_{\operatorname{H}} X \leq \dim_{\operatorname{H}} U + \dim_{\operatorname{P}} W.
\end{aligned}
$$
:::

Classically, Theorem [%s](#theorem:meta_theorem_two_part_sets_dimension_bound) is proved by the following sequence of inequalities:

$$
\begin{aligned}
\dim_{\operatorname{H}} X &\leq \dim_{\operatorname{H}} f(U \times W) \leq \dim_{\operatorname{H}}(U \times W) \leq \dim_{\operatorname{H}} U + \dim_{\operatorname{P}} W.
\end{aligned}
$$

The first inequality follows from monotonicity of Hausdorff dimension under inclusion. The second inequality follows from monotonicity of Hausdorff dimension under locally Lipschitz continuous mappings (see Corollary 2.4 in {cite:t}`Fal90`). The final inequality originally follows from Theorem 3 in {cite:t}`Tri82`, which takes the most work to show.

With respect to computability, we may make use of the fact that any (locally) Lipschitz continuous map is computable in some oracle.

:::{prf:proof}
:nonumber:
Let $B \geq_{\operatorname{T}} f$ be a Hausdorff oracle for both $X$ and $U$, as well as a packing oracle for $W$. Notice that for any point $x \in X$ there exists $u \in U$ and $w \in W$ such that for any precision-level $r \in \omega$,

$$
\begin{aligned}
K^B_r(x) = K^B_r(f(u, w)) \leq K^B_r(u, w) + o(r) \leq K^B_r(u) + K^B_r(w) + o(r).
\end{aligned}
$$

Let $\varepsilon > 0$. Since $B$ is a Hausdorff oracle for $X$, there exists $x \in X$ such that $\dim_{\operatorname{H}} X \leq \dim^B(x) + \varepsilon$. Then, by the choice of $B$ and the subadditivity of $K$:

$$
\begin{aligned}
\dim_{\operatorname{H}} X - \varepsilon
&\leq \dim^B(x)\\
&= \liminf_{r \to \infty} \frac{K^B_r(x)}{r}\\
&\leq \liminf_{r \to \infty} \frac{K^B_r(u) + K^B_r(w)}{r}\\
&\leq \dim^B(u) + \Dim^B(w)\\
&\leq \dim_{\operatorname{H}} U + \dim_{\operatorname{P}} W.
\end{aligned}
$$
:::

Let us use Theorem [%s](#theorem:meta_theorem_two_part_sets_dimension_bound) to recreate the proof of Theorem [%s](#theorem:Bushling_pinned_distance_theorem).

:::{prf:proof} Proof of Theorem [%s](#theorem:Bushling_pinned_distance_theorem)
:nonumber:
Take $U = \Delta^*_z(X)$ and $W = B^*_1(0)$ the unit ball in $\mathbb{R}^m$ with respect to the norm $\normAt{*}{\cdot}$. Notice that for any $X \ni x \neq z$, we may express $x$ as follows:

$$
\begin{aligned}
x = \normAt{*}{x - z} \frac{x - z}{\normAt{*}{x - z}} + z.
\end{aligned}
$$

Since $\normAt{*}{x - z} \in \Delta^*_z(X)$ and $\frac{x - z}{\normAt{*}{x - z}} \in B^*_1(0)$, we have found a mapping $f : U \times W \to \mathbb{R}^m$, $f: (u, w) \mapsto u w + z$ which surjects onto $X$, is locally Lipschitz continuous, and is computable in $\seq{z}$ (if $x = z$, simply return $z$). Noting that $\dim_{\operatorname{H}} W = \dim_{\operatorname{P}} W = m - 1$, Theorem [%s](#theorem:meta_theorem_two_part_sets_dimension_bound) gives:

$$
\begin{aligned}
\dim_{\operatorname{H}} X \leq \dim_{\operatorname{H}}(\Delta^*_z(X)) + (m - 1).
\end{aligned}
$$
:::

:::{prf:proposition}
:label: proposition:Bushling_type_projection_theorem
For each $m \in \omega$, norm $\normAt{*}{\cdot}$ on $\mathbb{R}^m$, direction $e \in \mathbb{S}^{m - 1}$, and subset $X \subseteq \mathbb{R}^m$,

$$
\begin{aligned}
\dim_{\operatorname{H}}\p{\Pi^*_e X} \geq \dim_{\operatorname{H}} X - (m - 1),
\end{aligned}
$$

where $\Pi^*_e = \Pi^*_{\operatorname{span}(e)}$.
:::

:::{prf:proof}
:nonumber:
Take $U = \Pi^*_e(X) \subseteq \mathbb{R}$ and $W = \mathcal{O}_e := \set{w \in \mathbb{R}^m}{w \perp e} \in G(m, m - 1)$ the orthogonal subspace to $e$. Notice that for any $x \in X$, we may express $x$ as follows:

$$
\begin{aligned}
x = \normAt{*}{\operatorname{proj}_e(x)} e + (x - \normAt{*}{\operatorname{proj}_e(x)} e).
\end{aligned}
$$

Since $\normAt{*}{\operatorname{proj}_e(x)} \in \Pi^*_e(X)$ and $x - \normAt{*}{\operatorname{proj}_e(x)} e \in \mathcal{O}_e$, the mapping $f : U \times W \to \mathbb{R}^m$, $f : (u, w) \mapsto u e + w$ surjects onto $X$, is Lipschitz continuous, and is computable in $\seq{e}$. Furthermore, $\dim_{\operatorname{H}} W = \dim_{\operatorname{P}} W = m - 1$. So, by Theorem [%s](#theorem:meta_theorem_two_part_sets_dimension_bound),

$$
\begin{aligned}
\dim_{\operatorname{H}} X \leq \dim_{\operatorname{H}}(\Pi^*_e(X)) + (m - 1).
\end{aligned}
$$
:::

Since there is a bi-Lipschitz continuous map $\normAt{*}{\cdot}$ translating between $\Pi^*_e(X)$ and $\operatorname{proj}_e(X)$, Proposition [%s](#proposition:Bushling_type_projection_theorem) also gives

$$
\begin{aligned}
\dim_{\operatorname{H}}\p{\operatorname{proj}_e(X)} \geq \dim_{\operatorname{H}}X - (m - 1).
\end{aligned}
$$

We obtain another result of this kind for radial projections with a well-known corollary. We refer {cite:p}`Orp19` to as a standard source.

:::{prf:proposition}
:label: proposition:decomposition_result_for_radial_projections
For each $m \in \omega$, norm $\normAt{*}{\cdot}$ on $\mathbb{R}^m$, point $z \in \mathbb{R}^m$, and subset $X \subseteq \mathbb{R}^m$,

$$
\begin{aligned}
\dim_{\operatorname{H}}\p{P^*_z X} \geq \dim_{\operatorname{H}} X - 1.
\end{aligned}
$$
:::

The proof relies on the same geometry as that of Theorem [%s](#theorem:Bushling_pinned_distance_theorem), but with distinct interpretations for the sets involved in the decomposition.

:::{prf:proof}
:nonumber:
Take $U = P^*_z(X)$ and $W = \mathbb{R}$. Notice that for any $X \ni x \neq z$, we may express $x$ as follows:

$$
\begin{aligned}
x = \frac{x - z}{\normAt{*}{x - z}} \cdot \normAt{*}{x - z} + z.
\end{aligned}
$$

Since $\frac{x - z}{\normAt{*}{x - z}} \in P^*_z(X)$ and $\normAt{*}{x - z} \in \mathbb{R}$, we have found a mapping $f : U \times W \to \mathbb{R}^m$, $f: (u, w) \mapsto u w + z$ which surjects onto $X$, is locally Lipschitz continuous, and is computable in $\seq{z}$ (if $x = z$, simply return $z$). Noting that $\dim_{\operatorname{H}} W = \dim_{\operatorname{P}} W = 1$, Theorem [%s](#theorem:meta_theorem_two_part_sets_dimension_bound) gives:

$$
\begin{aligned}
\dim_{\operatorname{H}} X \leq \dim_{\operatorname{H}}(P^*_z(X)) + 1.
\end{aligned}
$$
:::

:::{prf:definition}
Let $z \in \mathbb{R}^m$. A subset $X \subseteq \mathbb{R}^m$ is said to be **totally invisible from $z$** if $\dim_{\operatorname{H}}(P_z(X \setminus \seq{z})) = 0$. Let $\operatorname{Inv}_{\operatorname{T}}(X)$ be the collection of all points from which $X$ is totally invisible.
:::

Suppose a subset $X$ of Hausdorff dimension greater than one were to be totally invisible from some point $z$; then Proposition [%s](#proposition:decomposition_result_for_radial_projections) would imply $\dim_{\operatorname{H}}(P_z(X \setminus \seq{z})) \geq \dim_{\operatorname{H}} X - 1$, which is positive, a contradiction. This gives the well-known corollary.

:::{prf:corollary}
For any subset $X \subseteq \mathbb{R}^m$ with $\dim_{\operatorname{H}} X > 1$, we have $\operatorname{Inv}_{\operatorname{T}}(X) = \emptyset$.
:::

In summary, Theorem [%s](#theorem:meta_theorem_two_part_sets_dimension_bound) may be applied to various geometries. Theorem [%s](#theorem:Bushling_pinned_distance_theorem) is an application to pinned-distance sets and the unit ball. Dually, Proposition [%s](#proposition:decomposition_result_for_radial_projections) is an application to radial projections and the real line. Likewise, Proposition [%s](#proposition:Bushling_type_projection_theorem) is an application to orthogonal projections and their orthogonal hyperplanes.
