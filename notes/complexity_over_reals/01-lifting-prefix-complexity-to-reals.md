---
title: "Lifting Prefix Complexity to Reals"
label: section:Lifting_Prefix_Complexity_to_Reals
---

{term}`Prefix complexity` may be lifted to {term}`infinitary objects <Infinitary object>` via {term}`finitary <Finitary object>` approximations. We state the following results how they were originally presented: over Euclidean space. Analogous statements also hold over Cantor space.

## Lifting Conditional Complexity

Take any ambient dimensions $m, n \in \omega$, points $x \in \mathbb{R}^m$ and $y \in \mathbb{R}^n$, and precision-levels $r, s \in \omega$. A straightforward definition of the complexity of $x$ given $y$ up to these precision-levels would be to evaluate the complexity: $K(\restrict{x}{r} \mid \restrict{y}{s})$.

An alternative lift comes from the intuition offered by A. Shen and N. Vereshchagin in {cite:t}`SV02`: that for rationals $p \in \mathbb{Q}^m$ and $q \in \mathbb{Q}^n$, the conditional complexity $K(p \mid q)$ could be understood as the complexity of the problem $Q \to P$, where $P$ is the problem “construct $p$” and $Q$ is the problem “construct $q$.” So, the lift of conditional complexity to arbitrary subsets $X \subseteq \mathbb{R}^m$ given $Y \subseteq \mathbb{R}^n$ should reflect the complexity of constructing a point $p \in X \cap \mathbb{Q}^m$ from any point $q \in Y \cap \mathbb{Q}^n$. This definition was made explicit by J. Lutz and N. Lutz in {cite:t}`LL18`.

In particular, they defined the **conditional prefix complexity of $X$ given $Y$** to be:

$$
\begin{aligned}
\Kc{X}{Y} := \max_{q} \set{\min_{p} \set{\Kc{p}{q}}{p \in X \cap \mathbb{Q}^m}}{q \in Y \cap \mathbb{Q}^n},
\end{aligned}
$$

or $+\infty$ if either set is empty. Notice that this notion of complexity is governed only by the rational elements of the sets involved. Unconditionally, the **prefix complexity of $X$** is:

$$
\begin{aligned}
\K{X} := \min\set{\K{p}}{p \in X \cap \mathbb{Q}^m},
\end{aligned}
$$

or $+\infty$ whenever $X$ contains no rationals. Thus, a set is as simple as its simplest, rational element.

Now, for any $x \in \mathbb{R}^m$ and $y \in \mathbb{R}^n$, the **conditional prefix complexity of $x$ to precision-level $r$ given $y$ to precision-level $s$** is:

$$
\begin{aligned}
\KcAt{r \mid s}{x}{y} := \Kc{B_{2^{-r}}(x)}{B_{2^{-s}}(y)},
\end{aligned}
$$

while the **prefix complexity of $x$ to precision-level $r$ (possibly given $q \in \mathbb{Q}^n$)** is:

$$
\begin{aligned}
K_r(x \mid q) &:= K(B_{2^{-r}}(x) \mid \seq{q}), \text{ and}\\
K_r(x) &:= K(B_{2^{-r}}(x)).
\end{aligned}
$$

In the coming subsection, we will compare $K_{r \mid s}(x \mid y)$ to $K(\restrict{x}{r} \mid \restrict{y}{s})$.

It will also serve us to identify rational elements of a subset which witness the set's prefix complexity. We borrow the nomenclature of A Case. and J. Lutz {cite:p}`CL14`.

:::{prf:definition}
:label: definition:K_minimizer
Let $X \subseteq \mathbb{R}^m$, and suppose $x \in X \cap \mathbb{Q}^m$ satisfies $K(x) \leq K(X) + \varepsilon$ for some $\varepsilon \geq 0$. We say that $x$ is an **$\varepsilon$-approximate $K$-minimizer** of $X$. And if this holds for $\varepsilon = 0$, then $x$ is a **$K$-minimizer** of $X$.
:::

## Results on Lifted Conditional Complexity

We recall two lemmas about $K_{r \mid s}$ known as its **linear sensitivities**.

:::{prf:lemma} Linear Sensitivity of $K_r$ in $r$; Lemma 3.8 of {cite:t}`CL14`
:label: lemma:linearity_r_no_condition
For all $m \in \omega$, there exists $c \in \omega$ such that for all $x \in \mathbb{R}^m$ and $r, \Delta r \in \omega$,

$$
\begin{aligned}
K_r(x) \leq K_{r + \Delta r}(x) \leq K_r(x) + K(r) + m \Delta r + a_{\Delta r} + c,
\end{aligned}
$$

where $a_{\Delta r} := K(\Delta r) + 2 \log \p{\ceil{\frac{1}{2} \log m} + \Delta r + 3} + \p{\ceil{\frac{1}{2} \log m} + 3} m + K(m) + 2 \log m$.
:::

::::{prf:lemma} Linear Sensitivity of $K_{r \mid s}$ in $s$; Lemmas 7 and 8 of {cite:t}`LL18`
:label: lemma:linearity_with_condition
For all $m, n \in \omega$, there exists $c \in \omega$ such that for all $x \in \mathbb{R}^m$, $y \in \mathbb{R}^n$, $q \in \mathbb{Q}^n$, and $r, s, \Delta r, \Delta s \in \omega$,

:::{div}
:class: roman-list
1. $K_r(x \mid q) \leq K_{r + \Delta r}(x \mid q) \leq K_{r}(x \mid q) + m \Delta r + 2 \log(1 + \Delta r) + K(r, \Delta r) + c$;
1. $K_{r \mid s}(x \mid y) \geq K_{r \mid s + \Delta s}(x \mid y) \geq K_{r \mid s}(x \mid y) - n \Delta s - 2 \log(1 + \Delta s) + K(s, \Delta s) + c$.
:::
::::

A consequence of the linear sensitivities is that one may approximate the conditional prefix complexity of Euclidean points more simply via dyadic truncations.

:::{prf:lemma} Lemma A.1 of {cite:t}`LS16`
:label: maxmin_truncation_for_r
For all $m, n \in \omega$, there exists $c \in \omega$ such that for all $x \in \mathbb{R}^m$, $q \in \mathbb{Q}^n$, and $r \in \omega$,

$$
\begin{aligned}
\abs{\KcAt{r}{x}{q} - \Kc{\restrict{x}{r}}{q}} \leq \K{r} + c.
\end{aligned}
$$
:::

:::{prf:lemma} Lemma A.3 of {cite:t}`LS16`
:label: maxmin_truncation_for_r_s
For all $m, n \in \omega$, there exists $c \in \omega$ such that for all $x \in \mathbb{R}^m$, $y \in \mathbb{R}^n$, and $r, s \in \omega$,

$$
\begin{aligned}
\abs{\KcAt{r \mid s}{x}{y} - \Kc{\restrict{x}{r}}{\restrict{y}{s}}} \leq \K{r} + \K{s} + c.
\end{aligned}
$$
:::

One may then conclude an approximate {term}`symmetry of information` for prefix complexity on Euclidean space. Again, this is a weak form of symmetry of information.

::::{prf:theorem} Approximate Chain Rule; Lemma 4 of {cite:t}`LS16`
:label: theorem:approximate_SOI_conditional
For any $m, n \in \omega$, $x \in \mathbb{R}^m$, $y \in \mathbb{R}^n$, and $r \geq s \in \omega$,

:::{div}
:class: roman-list
1. $\abs{K_{r \mid r}(x \mid y) + K_r(y) - K_{r}(x, y)} \leq O_{m, n}(\log r) + O_n(\log \log \norm{y}) + O_{m, n}(1)$;
1. $\abs{K_{r \mid s}(x \mid x) + K_s(x) - K_r(x)} \leq O_m(\log r) + O_m(\log \log \norm{x}) + O_m(1)$.
:::
::::

We note that when computing with infinitary objects such as infinite binary strings or Euclidean reals, one must distinguish between *{term}`oracle`* and *conditional* accesses. While oracle access permits computations with approximations of the given data to arbitrary precisions, conditional access places a firm limit on the precision-level to which one may access the given data.

:::{prf:lemma} Lemma 14 of {cite:t}`LL18`
:label: oracle_access_to_conditional
For all $m, n \in \omega$, there exists a constant $c \in \omega$ such that, for all $x \in \mathbb{R}^m$, $y \in \mathbb{R}^n$, and $r, s \in \omega$,

$$
\begin{aligned}
K^y_r(x) \leq K_{r \mid s}(x \mid y) + K(s) + c.
\end{aligned}
$$
:::

## Lifting Discrete Semimeasures

Continuing the discussion of section [%s](#section:Semimeasures), we might naturally extend a discrete semimeasure $m : \mathbb{Q}^n \to [0, 1]$ defined on the rationals to a set function over $\mathbb{R}^n$ in one of two ways:
$$
\begin{aligned}
\mu_m(X) &:= \sum_{q \in X \cap \mathbb{Q}^n} m(q), \\
\Pi_m(X) &:= \sup_{q \in X \cap \mathbb{Q}^n} m(q).
\end{aligned}
$$

The first, $\mu_m$, is a purely additive atomic measure defined on every subset of $\mathbb{R}^n$. Whereas the second, $\Pi_m$, is an outer measure on $\mathbb{R}^n$ with $\Pi_m(\mathbb{R}^n) \leq 1$, and it is **completely maxitive** in the sense that for every arbitrary index set $I$:
$$
\Pi_m \left(\bigcup_{i \in I} X_i\right) = \sup_{i \in I} \Pi_m(X_i).
$$
It is also continuous from below along arbitrary increasing sequences; and is continuous from above along decreasing sequences of compact sets. In the language of capacities, $\Pi_m$ is a maxitive Choquet capacity whose point density function is $g_m := m\upharpoonright_{\mathbb{Q}^n}$. After normalization, we might further refer to this outer measure as a possibility measure with possibility distribution $g_m$. 

Always $\Pi_m \leq \mu_m$. 

In his doctoral dissertation, N. Lutz introduced the function $\boldsymbol{\kappa}(X) := 2^{-K(X)}$, where $K(X) := \min \{ K(q) : q \in X \cap \mathbb{Q}^n \}$, and zero if $X$ contains no rational points {cite:p}`Lut17b`. This is exactly $\Pi_m(X)$ for $m(q) := 2^{-K(q)}$, so it is an outer measure. J. Lutz and N. Lutz showed that $\boldsymbol{\kappa}$ possesses many algorithmic optimality properties. In particular, J. Lutz and N. Lutz showed that $\boldsymbol{\kappa}$ is **locally optimal** among all the other strongly finite, {term}`lower-semicomputable` outer measures on $\mathbb{R}^n$ {cite:p}`LL20`. 

Relative to any oracle $A$, the Coding Theorem [%s](#theorem:coding_theorem) gives for any $X \subseteq \mathbb{R}^n$:

$$
\boldsymbol{\kappa}^A(X) =^* \Pi_{\mathbf{m}^A}(X).
$$

Compare this to how Case and Lutz extended the *a priori* probability and Kolmogorov complexity notations to sets of strings $S \subseteq 2^{<\omega}$ {cite:p}`CL14`:

$$
\begin{aligned}
Q(S) &:= \sum_{\mathbf{U}_{\operatorname{PF}}(\pi) \downarrow \in S} 2^{-\operatorname{len}(\pi)} = \sum_{\sigma \in S} Q(\sigma),\\
K(S) &:= \min_{\sigma \in S} K(\sigma).
\end{aligned}
$$

They define a **layered disjoint system** (LDS) as a set $B \subseteq \omega \times \omega \times 2^{<\omega}$ whose **blocks** $B_{r,t} := \{ \sigma : (r, t, \sigma) \in B \}$ are pairwise disjoint within each **layer** $r$: so $B_{r,s} \cap B_{r,t} = \emptyset$ whenever $s \neq t$.

:::{prf:theorem} LDS Coding Theorem, Theorem 3.1 of {cite:t}`CL14`
:label: theorem:LDS_coding_theorem
For every computably enumerable LDS $B$ there is a constant $c_B$ such that, for all $r, t \in \omega$,

$$
K(B_{r,t}) \leq -\log Q(B_{r,t}) + K(r) + c_B.
$$
:::

The reverse inequality $K(B_{r,t}) \geq -\log Q(B_{r,t}) - O(1)$ fails in general, since a block may contain many strings. The theorem says instead that the total mass of a block exceeds the mass of its best element by at most a factor $2^{K(r) + O(1)}$. Levin's Coding Theorem ([%s](#theorem:coding_theorem)) is the special case where every block is a singleton.

Apply the LDS Coding theorem to $\mathbb{R}^n$: the layers $\mathcal{Q}^n_r$ of the half-open dyadic cubes can computable enumerate their blocks $(r, t)$. And the blocks of $\mathcal{Q}^n_r$ partition $\mathbb{R}^n$. This builds an LDS. Using [%s](theorem:LDS_coding_theorem), we may conclude the that $\Pi_{\mathbf{m}^A}$ and $\mu_{\mathbf{m}^A}$ essentially agree on half-open dyadic cubes.

:::{prf:corollary}
:label: corollary:sum_sup_dyadic
For every oracle $A$, precision-level $r \in \omega$, and every half-open dyadic cube $D \in \mathcal{Q}^n_r$,

$$
\Pi_{\mathbf{m}^A}(D) \leq \mu_{\mathbf{m}^A}(D) \leq 2^{K(r) + O(1)} \cdot \Pi_{\mathbf{m}^A}(D).
$$
:::

That is, at each dyadic layer, the additive and maxitive extensions of $\mathbf{m}^A$ agree up to a factor of $2^{o(r)}$. This is the fact that J. Lutz and N. Lutz use to prove that $\boldsymbol{\kappa}$ is locally optimal {cite:p}`LL20`.
