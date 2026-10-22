---
title: "Kolmogorov Complexity on Net Spaces"
label: section:Kolmogorov_Complexity_on_Net_Spaces
---

There are multiple senses in which one might lift the notion of Kolmogorov complexity from finitary objects to **points** in a mesh space. Each is inspired by its corresponding version over either Euclidean or Cantor space. That the various versions agree in the standard Euclidean and sequence spaces follows from the many orderly properties of the prototypical meshes on those spaces. We use this section to argue what properties lend themselves to asymptotic coincidence between these lifts.

## Kolmogorov Complexity on Euclidean Space

We continue the discussions of Sections [%s](#section:Lifting_Prefix_Complexity_to_Reals) and [%s](#section:Robustness_of_the_Lift) to better understand how the lifts of Kolmogorov complexity to Euclidean space might inspire lifts to mesh spaces.

The standard method for lifting prefix complexity to points in a metric space is via a computable, dense subset. Recall that the complexity of an arbitrary subset $X \subseteq \mathbb{R}^m$ was defined as the minimal complexity of a rational in $X$ (or $+\infty$ if no such rational exists). Intuitively, this definition captures the idea that a set is **simple** if it contains a point that is simple to describe, and complex otherwise. Likewise, the complexity of an arbitrary point $x \in \mathbb{R}^m$ is definable to some precision-level $r \in \omega$ as the minimum complexity of a rational in the open $2^{-r}$-ball about $x$. Note that this is equivalent (up to an additive constant) to evaluating the complexity of the dyadic truncation of $x$ up to precision $2^{-r}$ as in Lemma [%s](#maxmin_truncation_for_r) and to finding a $K$-minimizer to $B_{2^{-r}}(x)$ as in Lemma 4.9 of {cite:t}`CL14`.

Note that something similar is true in the conditional case using either the max-min or min-max definitions of conditional prefix complexity $K_{r \mid s}$ as discussed in Section [%s](#section:Robustness_of_the_Lift). Lemma [%s](#maxmin_truncation_for_r_s) shows the ability for dyadic truncation to approximate $K_{r \mid s}$, and Proposition [%s](#lemma:conditional_K_minimizers_suffice) does the same via $K$-minimizers.

Let us now introduce a third manner by which to approximate the lift of prefix complexity to Euclidean space.

In Section [%s](#section:Notation), we defined the collection $\mathcal{Q}^m$ of all dyadic rational cubes over $\mathbb{R}^m$. If $Q \in \mathcal{Q}^m$ is a dyadic cube, let $K(Q)$ denote the prefix complexity $K(i)$ of the index of $Q$ in a standard (computable) enumeration of $\mathcal{Q}^m$. Then, let

$$
\begin{aligned}
H_r(x) := \min \set{K(Q)}{Q \in \mathcal{Q}^m \text{ and } Q \subseteq B_{2^{-r}}(x)},
\end{aligned}
$$

or $+\infty$ if the minimum is taken over the empty set, denote a third lift of complexity to points in $\mathbb{R}^m$. Intuitively, this definition captures the idea that a point is **simple** if there are always sufficiently simple dyadic cubes in its vicinity. Clearly, $H_r(x) \geq^+ K_r(x)$, as the center $c_Q$ of any dyadic cube $Q$ satisfying $Q \subseteq B_{2^{-r}}(x)$ will satisfy $c_Q \in B_{2^{-r}}(x)$. Yet, these notions do not differ significantly.

:::{prf:proposition}
:label: prop:H_and_K_Euclidean
For all $m \in \omega$, $x \in \mathbb{R}^m$, and $r \in \omega$,

$$
\begin{aligned}
K_r(x) = H_r(x) \pm o(r),
\end{aligned}
$$

where $o(r)$ is a sub-linear term in $r$ independent of $x$.
:::

:::{prf:proof}
:nonumber:
By Lemma [%s](#maxmin_truncation_for_r), it suffices to show $H_r(x) = K(\restrict{x}{r}) \pm o(r)$.

Suppose we are given any dyadic cube $Q \subseteq B_{2^{-r}}(x)$. In particular, its center $c_Q$ is rational and computable from $Q$, and approximates $\restrict{x}{r}$ to a precision $O(2^{-r})$. Thus,

$$
\begin{aligned}
K(\restrict{x}{r}) \leq K(Q) + O(1) \implies K(\restrict{x}{r}) \leq H_r(x) + O(1).
\end{aligned}
$$

In the other direction, notice that $\restrict{x}{r}$ is a dyadic rational inside $B_{2^{-r}}(x)$. A simple geometric fact states that there must be one dyadic cube $Q$ of side-length at least $\frac{1}{\sqrt{m}} \cdot 2^{-r}$ which is a subset of the expanded ball: $B_{2 \cdot 2^{-r}}(\restrict{x}{r})$. And by comparing volumes, there can be no more than $(4 / \sqrt{m})^m$ many such dyadic cubes. Given $\restrict{x}{r}$, we may effectively enumerate all dyadic cubes which are subsets of $B_{2 \cdot 2^{-r}}(\restrict{x}{r})$ and simply specify any one of them by providing its index in that enumeration. Such an index requires no more than $\log((4 / \sqrt{m})^m) = O(m \log m)$ many bits to specify. And for any dyadic cube $Q \subseteq B_{2^{-r}}(x)$, it follows from the triangle inequality that $Q \subseteq B_{2 \cdot 2^{-r}}(\restrict{x}{r})$, and so,

$$
\begin{aligned}
H_r(x) \leq K(Q) \leq K(\restrict{x}{r}) + K(r) + O(m \log m) + O(1).
\end{aligned}
$$
:::

Another lift of prefix complexity to Euclidean space may be defined which does not significantly differ from the rest. Let

$$
\begin{aligned}
G_r(x) := \min \set{K(Q)}{x \in Q \in \mathcal{Q}^m \text{ and } \diam(Q) \leq 2^{-r}},
\end{aligned}
$$

or $+\infty$ if the minimum is taken over the empty set. Then, $G_r(x)$ denotes a fourth lift of prefix complexity to points in $\mathbb{R}^m$. Intuitively, this definition captures the idea that a point is **simple** if there are sufficiently small and simple dyadic cubes covering it. Compared to $H_r(x)$, this fourth notion $G_r(x)$ minimizes prefix complexity over a smaller class of dyadic cubes, since $x \in Q$ and $\diam(Q) \leq 2^{-r}$ imply $Q \subseteq B_{2^{-r}}(x)$, but not vice versa. Nevertheless, we observe asymptotic coincidence between the two notions.

:::{prf:proposition}
:label: prop:G_and_K_Euclidean
For all $m \in \omega$, $x \in \mathbb{R}^m$, and $r \in \omega$,

$$
\begin{aligned}
K_r(x) = G_r(x) \pm o(r),
\end{aligned}
$$

for some fixed $o(r)$ term independent of $x$ and $r$.
:::

The proof of Proposition [%s](#prop:G_and_K_Euclidean) is nearly identical to that of Proposition [%s](#prop:H_and_K_Euclidean), noting that exactly one of the at most $(4 / \sqrt{m})^m$ dyadic cubes in $B_{2 \cdot 2^{-r}}(\restrict{x}{r})$ must contain $x$.

## Kolmogorov Complexity on Mesh Spaces

In order to lift Kolmogorov complexity to points in a mesh space, we cannot necessarily make use of a computable, dense subset of points or some notion of truncation as is typically done over Euclidean space. Instead, we might measure a point's complexity by the complexity of the mesh elements falling in a ball about the point at some precision-level. This is exactly what $H_r(x)$ and $G_r(x)$ accomplish over Euclidean space with respect to the dyadic cubes net. Over mesh spaces, we will use boldface characters $\mathbf{H}$ and $\mathbf{G}$ for these finite-precision complexity notions.

:::{prf:definition}
For any $x \in \Omega$ and $r \in \omega$, define the **vicinity complexity of $x$ up to precision-level $r$ with respect to the mesh $\mathcal{N}$** as:

$$
\begin{aligned}
\mathbf{H}_r(x) := \min \set{K(i)}{\iota(i) \subseteq B_{2^{-r}}(x)}.
\end{aligned}
$$
:::

:::{prf:definition}
For any $x \in \Omega$ and $r \in \omega$, define the **covering complexity of $x$ up to precision-level $r$ with respect to the mesh $\mathcal{N}$** as:

$$
\begin{aligned}
\mathbf{G}_r(x) := \min \set{K(i)}{x \in \iota(i) \AND \diam(i) \leq 2^{-r}}.
\end{aligned}
$$
:::

In order to show asymptotic coincidence between these two notions of complexity, we will need to ask more from the mesh.

::::{prf:definition}
If $\mathcal{N}$ is a net on $\Omega$, we call $\mathcal{N}$ a **grate** on $\Omega$ if it further satisfies: there exist both a function $f : \omega \to [1, +\infty)$ and an $o(r)$ function $g: \omega \to \mathbb{R}$ such that for all precision-levels $r \in \omega$:

:::{div}
:class: labeled-list
- (**G5**) For all $x \in \Omega$, there exists $N \in \mathcal{N}$ such that $x \in N$ and $\diam_d(N) \in \brk{2^{-r - f(r)}, 2^{-r}}$;

- (**G6**) For all $N \in \mathcal{N}$ satisfying $\diam_d(N) \leq 2^{-r}$, it holds that

  $$
  \begin{aligned}
  \log \abs{\set{N' \in \mathcal{N}}{N \cap N' \neq \emptyset \text{ and } \diam_d(N') \in \brk{2^{-r - f(r)}, 2^{-r}}}} \leq g(r).
  \end{aligned}
  $$
:::

In words, the grate axioms ask that:

:::{div}
:class: labeled-list
- (**G5**) For each point there is a grate element covering it at every precision-level;
- (**G6**) For each grate element, there are no more than sub-exponentially many other grate elements non-trivially intersecting it at each smaller precision-level.
:::
::::

When $\mathcal{N}$ is a grate, we should additionally include $f$ and $g$ in the $\omega$-presentation $\mathscr{R}$ of the grate, as well as another relation encoding intersection between grate elements:

- $\operatorname{int}: \omega^2 \to \seq{\top, \bot}$ is a relation on pairs of indices encoding the non-trivial intersection relation; i.e., if $N_i, N_j \in \mathcal{N}$ satisfy $\iota(i) = N_i$ and $\iota(j) = N_j$, then,

  $$
  \begin{aligned}
  \operatorname{int}(i, j) \iff N_i \cap N_j \neq \emptyset.
  \end{aligned}
  $$

For any grate $\mathcal{N}$ on a metric space $(\Omega, d)$ represented by the $\omega$-presentation $\mathscr{R}$ as described above, we may call the pair $(\Omega, \mathcal{N})$ a **grate space** and the tuple $(\Omega, \mathcal{N}, \mathscr{R})$ a **represented grate space**.

We now show that vicinity and covering complexities agree asymptotically on grate spaces. Our proof of this agreement relies on the density of the mesh along each precision-level.

:::{prf:proposition}
:label: prop:H_and_G_grate
For any grate space $(\Omega, \mathcal{N})$, $x \in \Omega$, and $r \in \omega$,

$$
\begin{aligned}
\mathbf{H}_r(x) = \mathbf{G}_r(x) \pm o(r),
\end{aligned}
$$

for some sublinear term $o(r)$ independent of $x$.
:::

:::{prf:proof}
:nonumber:
Let $\iota$ index $\mathcal{N}$ while respecting containment. First, we immediately have that $\mathbf{H}_r(x) \leq \mathbf{G}_r(x)$, since $x \in \iota(i)$ and $\diam(i) \leq 2^{-r}$ together imply $\iota(i) \subseteq B_{2^{-r}}(x)$ via the triangle inequality.

In the other direction, let $i \in \omega$ satisfy the vicinity condition $\iota(i) \subseteq B_{2^{-r}}(x)$. Recall that for grate spaces, we have augmented their $\omega$-presentation to encode $f(r)$ and the non-trivial intersection relation, $\operatorname{int}$. So, using $i$ and $r$, we may computably enumerate in the $\omega$-presentation of the grate $\mathcal{N}$ all indices $j \in \omega$ satisfying:

$$
\begin{aligned}
\operatorname{int}(i, j) \quad \text{and} \quad \diam(j) \in \brk{2^{-r -f(r)}, 2^{-r}}.
\end{aligned}
$$

By (**G5**), one such $j = j^*$ further satisfies $x \in \iota(j^*)$. And by construction, $\diam(j^*) \leq 2^{-r}$, qualifying $j^*$ for the covering condition that defines $\mathbf{G}_r(x)$. Moreover, (**G6**) guarantees that this enumeration is not too large: there are no more than $2^{g(r)}$ many indices in the enumeration, where $g(r)$ is the $o(r)$ function guaranteed in the grate axioms. Therefore, using a two-part description for $j^*$ with respect to this enumeration, we conclude:

$$
\begin{aligned}
K(j^*) \leq K(i) + \ceil{g(r)} + K(r) + O(1) = K(i) + o(r),
\end{aligned}
$$

so, $\mathbf{G}_r(x) \leq \mathbf{H}_r(x) + o(r)$, as desired.
:::

We might take either one of these quantities $\mathbf{G}_r$ or $\mathbf{H}_r$ as our primary definition of prefix complexity over a mesh space. Anticipating the results of the following section, we select $K_r := \mathbf{G}_r$ as the **prefix complexity of $x$ with respect to the mesh $\mathcal{N}$**.

:::{prf:example}
:label: example:euclidean_has_grate
Continuing with the Lebesgue measure and the dyadic cube net $\mathcal{Q}^m$ on Euclidean space as introduced in Example [%s](#example:euclidean_has_dyadic_net), we show that $(\mathbb{R}^m, \mathcal{Q}^m)$ is a grate space. Note that the non-trivial intersection relation is also easily computable from the enumeration of $\mathcal{Q}^m$. Fixing $r \in \omega$ and $x \in \mathbb{R}^m$, it is clear that there exists a dyadic cube $Q$ of side-length $2^{- r - \ceil{ \log \sqrt{m}}}$ satisfying $x \in Q$. The diameter of this cube is:

$$
\begin{aligned}
\diam_d (Q) = 2^{- r - \ceil{ \log \sqrt{m}}} \cdot \sqrt{m} \leq 2^{- r}.
\end{aligned}
$$

Setting $f(r) := \ceil{\log \sqrt{m}}$, we conclude (**G5**). Note that non-trivial intersection between dyadic cubes implies comparability: one is a subset of the other. So, we may also bound from above the number of dyadic cubes having diameter in the interval $[2^{-r - f(r)}, 2^{-r}]$ and non-trivially intersecting $Q$:

$$
\begin{aligned}
\sum_{i = 1}^{\ceil{f(r)}} \p{2^{m}}^i \leq 2^{m\p{\ceil{f(r)} + 1}} = 2^{\p{\ceil{\log \sqrt{m}} + 1}}.
\end{aligned}
$$

Setting $g(r) := \ceil{\log \sqrt{m}} + 1 = O(1)$, we conclude (**G6**) as well. Thus, $(\mathbb{R}^m, \mathcal{Q}^m)$ is a grate space; so, by Proposition [%s](#prop:H_and_G_grate), $\mathbf{H}_r(x) = \mathbf{G}_r(x) \pm o(r)$ for all $x \in \mathbb{R}^m$, a fact we have already seen as a consequence of Propositions [%s](#prop:H_and_K_Euclidean) and [%s](#prop:G_and_K_Euclidean). We further have that the non-trivial intersection relation is equivalent to the containment relation for this grate, and $f(r)$ is a computable function, so $\mathcal{Q}^m$ has a computable $\omega$-presentation, meaning $\mathcal{Q}^m$ qualifies as an **effective grate** on $\mathbb{R}^m$. So $\mathbb{R}^m$ with $\mathcal{Q}^m$ is in fact a **computable grate space**.
:::

## Optimality of Outer Measures on Computable Net Spaces

We still have not explicitly defined the Kolmogorov complexity of an arbitrary **subset** of a mesh space. For instance, it is possible to view vicinity complexity as induced by the following complexity notion on subsets: for any $X \subseteq \Omega$,

$$
\begin{aligned}
\mathbf{H}(X) := \min \set{K(i)}{\iota(i) \subseteq X}, \quad \text{so} \quad \mathbf{H}_r(x) := \mathbf{H}(B_{2^{-r}}(x)).
\end{aligned}
$$

However, this complexity notion is not particularly useful. For instance, N. Lutz argues how the map $\kappa(X) := 2^{-K(X)}$, which possesses many algorithmic optimality properties, is an outer measure on $\mathbb{R}^m$ {cite:p}`Lut17b; LL20`. In contrast, $X \mapsto 2^{-\mathbf{H}(X)}$ is not even necessarily countably subadditive. This is because little is guaranteed about how the mesh behaves topologically: while each subset $X_i \subseteq \Omega$ in a countable sequence could contain only mesh elements of very high complexity, their union $\bigcup_i X_i$ could contain a much larger mesh element of low complexity. However, on computable net spaces, it is indeed possible to define a reasonably well-behaved complexity notion for arbitrary subsets.

Let us now extend some of the algorithmic optimality results found in {cite:t}`LL20` to any computable net space $(\Omega, d, \mathcal{N}, \mathscr{R}, \alpha)$. We use the notation $\mathcal{P}^{<\omega}(\alpha)$ to refer to the collection of finite subsets of the computable dense sequence $\alpha$. And, given an element $N \in \mathcal{N}$, denote by $K_{\mathcal{N}}(N) := K(i)$ the **net-complexity** of $N$, evaluated on its index: $\iota(i) = N$. The following three properties of an outer measure will comprise our notion of **global optimality**, an optimality notion similar to that of the optimal lower-semicomputable discrete semimeasure $\mathbf{m}$.

:::{prf:definition}
An outer measure $\mu$ on $\Omega$ is **finitely supported** on $\alpha$ if, for every $\varepsilon > 0$, there exists $A \in \mathcal{P}^{<\omega}(\alpha)$ such that $\mu(\Omega \setminus A) < \varepsilon$.
:::

:::{prf:definition}
An outer measure $\mu$ on $\Omega$ is **strongly finite** if $\mu$ is supported on $\alpha$ and

$$
\begin{aligned}
\sum_{q \in \alpha} \mu(\seq{q}) < +\infty.
\end{aligned}
$$
:::

:::{prf:definition}
An outer measure $\mu$ on $\Omega$ is **lower-semicomputable** if it is finitely supported on $\alpha$ and there is a computable function (witness) $\widehat{\mu} : \mathcal{P}^{<\omega}(\alpha) \times \omega \to \mathbb{Q} \cap [0, +\infty)$ such that for all $A \in \mathcal{P}^{<\omega}(\alpha)$ and $r \in \omega$,

$$
\begin{aligned}
\widehat{\mu}(A, r) \leq \widehat{\mu}(A, r + 1) \leq \mu(A), \quad \text{and} \quad
\lim_{r \to \infty} \widehat{\mu}(A, r) = \mu(A).
\end{aligned}
$$
:::

Let $\Theta$ be the set of all strongly finite, lower-semicomputable outer measures on $\Omega$.

:::{prf:definition}
An outer measure $\mu$ on $\Omega$ is **globally optimal** if $\mu \in \Theta$ and multiplicatively dominates any other $\theta \in \Theta$, i.e., for any $\theta \in \Theta$, there exists $\beta \in (0, +\infty)$ such that for each $X \subseteq \Omega$,

$$
\begin{aligned}
\mu(X) \geq \beta \cdot \theta(X).
\end{aligned}
$$
:::

By the same arguments found in {cite:t}`LL20` (see Lemma 3.3 and Theorem 3.4), there exist globally optimal outer measures on computable metric spaces.

:::{prf:proposition}
:label: prop:exists_globally_optimal
Over any computable metric space $(\Omega, d, \alpha)$, there exists a globally optimal strongly finite, lower-semicomputable outer measure $\boldsymbol{\theta}$.
:::

Their construction follows a similar format as Theorems [%s](#prop:exists_optimal) and [%s](#prop:exists_optimal_discrete), producing an optimal outer measure as a weighted sum of all those found in $\Theta$. We next define the **prefix complexity of an arbitrary subset $X \subseteq \Omega$** in a computable metric space $(\Omega, d, \alpha)$ as:

```{math}
:label: equation:boldface_K
\begin{aligned}
\mathbf{K}(X) := \min \set{\mathbf{K}(q)}{q \in X \cap \alpha},
\end{aligned}
```

where $\mathbf{K}(q)$ is defined as $K(i)$, and $q = \alpha_i = \chi(i)$ has index $i = \text{index}(q)$ in the enumeration of the computable dense subset.

From ([%s](#equation:boldface_K)), we define what we will refer to as the **prefix measure** of a subset $X \subseteq \Omega$ as follows:

$$
\begin{aligned}
\boldsymbol{\kappa}(X) := 2^{-\mathbf{K}(X)}.
\end{aligned}
$$

It is easy to check that $\boldsymbol{\kappa}$ is indeed an outer measure on $\Omega$, as well as lower-semicomputable and strongly finite. That $\boldsymbol{\kappa}$ is lower-semicomputable follows from the upper semicomputability of $K$. That $\boldsymbol{\kappa}$ is finitely supported on $\alpha$ follows from the fact that $A_\varepsilon := \set{q \in \alpha}{\mathbf{K}(q) \leq \log_2 \frac{1}{\varepsilon}}$ is a finite subset of $\alpha$ accounting for all but at most $\varepsilon$ amount of the measure that $\boldsymbol{\kappa}$ places on $\Omega$. And that $\boldsymbol{\kappa}$ is strongly finite then follows from the Kraft Inequality [%s](#theorem:kraft_inequality):

$$
\begin{aligned}
\sum_{q \in \alpha} \boldsymbol{\kappa}(\seq{q}) = \sum_{q \in \alpha} 2^{-\mathbf{K}\p{\seq{q}}} \leq 1.
\end{aligned}
$$

It turns out that $\boldsymbol{\kappa}$ is **not** globally optimal over $\Omega$. To see this, let us first define the subset-analogues of each of the equivalent quantities in Levin's Coding Theorem [%s](#theorem:coding_theorem):

$$
\begin{aligned}
\mathbf{\boldsymbol{\mu}}(X) &:= \sum_{q \in X \cap \alpha} \mathbf{\boldsymbol{\mu}}(q),\\
\mathbf{Q}(X) &:= \sum_{q \in X \cap \alpha} \mathbf{Q}(q) = \sum_{\mathbf{U}_{\operatorname{PF}}(\pi) \downarrow \in X \cap \alpha} 2^{-\operatorname{len}(\pi)},\\
\mathbf{R}(X) &:= \sum_{q \in X \cap \alpha} \mathbf{R}(q) = \sum_{q \in X \cap \alpha} 2^{-\mathbf{K}(q)},
\end{aligned}
$$

where $\mathbf{\boldsymbol{\mu}}(q)$, $\mathbf{Q}(q)$, and $\mathbf{R}(q)$ are evaluated as $\mathbf{m}(i)$, $Q(i)$, and $R(i)$, respectively, for index $i$ of $q$ in $\alpha$. Notice that for any $X \subseteq \Omega$,

$$
\begin{aligned}
\boldsymbol{\kappa}(X) \leq \mathbf{R}(X) \leq \mathbf{Q}(X).
\end{aligned}
$$

The same discussion in {cite:t}`LL20` works to show that each of these maps defined above is a strongly finite, lower-semicomputable outer measure on $\Omega$. In fact, each is globally optimal.

:::{prf:proposition}
:label: proposition:the_three_globally_optimal_outer_measures
Each of $\boldsymbol{\mu}$, $\mathbf{Q}$, and $\mathbf{R}$ is globally optimal on $\Omega$.
:::

:::{prf:proof}
:nonumber:
By Levin's Coding Theorem [%s](#theorem:coding_theorem), each of $\boldsymbol{\mu}$, $\mathbf{Q}$, and $\mathbf{R}$ multiplicatively dominate the others as functions on $\alpha$. So, by definition, $\boldsymbol{\mu}$, $\mathbf{Q}$, and $\mathbf{R}$ dominate each other as outer measures from $\Theta$. Moreover, for any $\theta \in \Theta$, we claim that $\boldsymbol{\mu}$ dominates $\theta$. Note that $\theta$ induces the discrete semimeasure: $i \mapsto \theta(\seq{\alpha_i})$. So, by the assumptions on $\theta$ as well as the optimality of $\mathbf{m}$ as a discrete semimeasure, we conclude there exists $\beta \in (0, +\infty)$ such that for any $X \subseteq \Omega$:

$$
\begin{aligned}
\theta(X) &\leq \theta(X \cap \alpha) + \theta(X \setminus \alpha)\\
&\leq \sum_{q \in X \cap \alpha} \theta(\seq{q}) + \theta(\Omega \setminus \alpha)\\
&\leq \frac{1}{\beta} \sum_{q \in X \cap \alpha} \boldsymbol{\mu}(\seq{q}) + 0\\
&= \frac{1}{\beta} \cdot \boldsymbol{\mu}(X).
\end{aligned}
$$
:::

Lemma 4.4 of {cite:t}`LL20` may be adapted to $(\Omega, d, \alpha)$ to find a family of subsets of $\Omega$ exhibiting $\boldsymbol{\kappa}$ failing to dominate $\boldsymbol{R}$. Given a constant $\beta > 0$, they construct a set $X_\beta = \set{q \in \alpha}{K(q) > \eta}$ for some sufficiently large constant $\eta > 0$ satisfying $\eta - O(\log \eta) <\log \beta$ and exhibiting $\boldsymbol{\kappa}(X_\beta) < \beta \cdot \mathbf{R}(X_\beta)$. Notice that by definition, $\boldsymbol{\kappa}(X_\beta) < 2^{-\eta}$, while

$$
\begin{aligned}
\mathbf{R}(X_\beta) = \sum_{q \in X_\beta \cap \alpha} 2^{-K(q)} &\geq \sum_{\substack{q \in X_\beta \cap \alpha\\
K(q) < \eta + O(\log \eta)}} 2^{-K(q)}\\
&\geq 2^{-(\eta + O(\log \eta))} \cdot \abs{\set{q \in \alpha}{K(q) \in (\eta, \eta + O(\log \eta))}}.
\end{aligned}
$$

Then, by a short counting argument, they lower-bound the cardinality of the set appearing above by $2^{\eta}$, giving $\mathbf{R}(X_\beta) \geq 2^{-O(\log \eta)}$. Thus, $\boldsymbol{\kappa}(X_\beta) < \beta \cdot \mathbf{R}(X_\beta)$, showing $\boldsymbol{\kappa}$ is not globally optimal.

:::{prf:definition}
:label: definition:domination_over_LDS
Let $\mu$ and $\theta$ be outer measures on $\Omega$ and $\mathcal{X}$ be a layered disjoint system over $\Omega$ (in the sense of {cite:t}`LL20`). Then $\mu$ is said to **dominate $\theta$ on $\mathcal{X}$** if there exists a map $\beta : \omega \to (0, +\infty)$ such that $-\log \beta(r) = o(r)$ as $r \to \infty$, and for each $r \in \omega$ and $X \in \mathcal{X}^{(r)}$ in the $r$-th layer of $\mathcal{X}$,

$$
\begin{aligned}
\mu(X) \geq \beta(r) \cdot \theta(X).
\end{aligned}
$$
:::

Recall that for any layered-disjoint net $\mathcal{N}$, the sequence of rank layers $(\mathcal{N}^{(r)})_{r \in \omega}$ induces a layered disjoint system in the sense of {cite:t}`LL20`. So we may discuss domination on any layered-disjoint net.

:::{prf:definition}
:label: definition:locally_optimal_for_net
An outer measure $\mu$ on net space $(\Omega, \mathcal{N})$ is **locally optimal** if $\mu \in \Theta$ and for each $\theta \in \Theta$, $\mu$ dominates $\theta$ on $\mathcal{N}$.
:::

:::{prf:theorem}
:label: theorem:kappa_is_locally_optimal_for_layered_disjoint_nets
Over any computable net space $(\Omega, d, \mathcal{N}, \mathscr{R}, \alpha)$ with a layered-disjoint net $\mathcal{N}$, we have that $\boldsymbol{\kappa}$ is locally optimal.
:::

:::{prf:proof}
:nonumber:
From before, $\boldsymbol{\kappa} \in \Theta$. We claim for each $\theta \in \Theta$, $\boldsymbol{\kappa}$ dominates $\theta$ on $\mathcal{N}$. Denote for each $i \in \omega$:

$$
\begin{aligned}
m_\theta(i) := \theta(\seq{\alpha_i}).
\end{aligned}
$$

Then $m_\theta$ is a lower-semicomputable discrete net semimeasure and hence multiplicatively dominated by $\mathbf{m}$: let $\gamma \in (0, +\infty)$ satisfy $\mathbf{m}(i) \geq \gamma \cdot m_\theta(i)$ for each $i \in \omega$. Recall the notation $\mathcal{N}^{(r)}$ for the collection of all net elements with rank $r$. Then $(\mathcal{N}^{(r)} : r \in \omega)$ is a layered disjoint system, and hence obeys the **LDS Coding Theorem** (Theorem 3.1 of {cite:t}`CL14`). In particular, we have for each $N \in \mathcal{N}^{(r)}$:

```{math}
:label: eqn:LDS_coding_theorem
\begin{aligned}
K_{\mathcal{N}}(N) \leq -\log \mathbf{Q}(N) + K(r) + O(1) \leq -\log \boldsymbol{\mu}(N) + K(r) + O(1).
\end{aligned}
```

Call $\beta(r) = \gamma \cdot 2^{-K(r) - O(1)}$ using the same additive constant as in the LDS Coding Theorem. Notice that indeed $-\log \beta(r) = o(r)$. Then for each $N \in \mathcal{N}^{(r)}$, we use that $\theta$ is both countably subadditive and finitely supported on $\alpha$, as well as ([%s](#eqn:LDS_coding_theorem)), to confirm:

$$
\begin{aligned}
\boldsymbol{\kappa}(N) &= 2^{-\mathbf{K}(N)}\\
&\geq 2^{-K_{\mathcal{N}}(N)}\\
&\geq 2^{-K(r) - O(1)} \cdot \boldsymbol{\mu}(N)\\
&= 2^{-K(r) - O(1)} \cdot \sum_{q \in N \cap \alpha} \boldsymbol{\mu}(q)\\
&\geq 2^{-K(r) - O(1)} \cdot \sum_{q \in N \cap \alpha} \gamma \cdot m_\theta(q)\\
&= \beta(r) \cdot \sum_{q \in N \cap \alpha} \theta(\seq{q})\\
&\geq \beta(r) \cdot \theta(N).
\end{aligned}
$$
:::

We now ask how the complexity $K_{\mathcal{N}}(N)$ of the address of an element $N$ with respect to the tree structure of $\mathcal{N}$ compares to the complexity $\mathbf{K}(N)$ as a subset of $\Omega$? We have already used the fact that $\mathbf{K}(N) \leq K_{\mathcal{N}}(N)$: if $\iota(i) = N$, then $\alpha_i \in N$, and $\mathbf{K}(\alpha_i) = K(i) = K_{\mathcal{N}}(N)$. The other direction follows given some stronger assumptions about the net.

:::{prf:proposition}
:label: proposition:computable_grate_space_complexities_agree
Let $(\Omega, d, \mathcal{N}, \mathscr{R}, \alpha)$ be a computable grate space. Then, for each $N \in \mathcal{N}$,

$$
\begin{aligned}
K_{\mathcal{N}}(N) = \mathbf{K}(N) \pm o\p{-\log \diam_d(N)},
\end{aligned}
$$

where the $o(\cdot)$ term vanishes like $\frac{o(-\log \operatorname{diam}_d(N))}{\log \operatorname{diam}_d(N)} \to 0$ as $\operatorname{diam}_d(N) \to 0$.
:::

:::{prf:proof}
:nonumber:
Let $f$ and $g$ be as in the definition of a grate space. Take $N \in \mathcal{N}$ and $r \in \omega$ such that $\diam_d(N) \in [2^{-r - f(r)}, 2^{-r}]$. Further suppose $i, j \in \omega$ are such that $\iota(i) = N$ and $\alpha_j \in N$ with minimal complexity $K(j)$. We may compute $i$ from $j$ as follows: by (**G6**), there are no more than $2^{g(r)}$ net elements non-trivially intersecting $\iota(j)$ with diameter in this same range $[2^{-r - f(r)}, 2^{-r}]$. Thus, $N$ may be computed by specifying an index in this collection, giving

$$
\begin{aligned}
K_{\mathcal{N}}(N) = K(i) \leq K(j) + \ceil{g(r)} + 1 + O(1) \leq \mathbf{K}(N) + o(-\log \diam_d(N)).
\end{aligned}
$$
:::

Finally, we ask whether $\mathbf{K}$ is compatible with $\mathbf{G}$ and $\mathbf{H}$ as complexity notions on points. In particular, we extend $\mathbf{K}$ to arbitrary points of the metric space at fixed precision-levels:

$$
\begin{aligned}
\mathbf{K}_r(x) := \mathbf{K}(B_{2^{-r}}(x)).
\end{aligned}
$$

Note that this complexity notion plays an analogous role to $C_\delta(x)$ in {cite:t}`LLM23`, where $\delta = 2^{-r}$.

:::{prf:proposition}
:label: prop:K_and_H_and_G_grate
For any grate space $(\Omega, \mathcal{N})$, $x \in \Omega$, and $r \in \omega$,

$$
\begin{aligned}
\mathbf{K}_r(x) = \mathbf{H}_r(x) \pm o(r) = \mathbf{G}_r(x) \pm o(r),
\end{aligned}
$$

for some sublinear terms $o(r)$ independent of $x$.
:::

The second equality above restates Proposition [%s](#prop:H_and_G_grate). And the proof of the above result mimics those of Propositions [%s](#prop:H_and_K_Euclidean) and [%s](#proposition:computable_grate_space_complexities_agree).
