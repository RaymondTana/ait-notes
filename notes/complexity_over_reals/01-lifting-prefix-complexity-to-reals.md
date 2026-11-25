---
title: "Lifting Prefix Complexity to Reals"
label: section:Lifting_Prefix_Complexity_to_Reals
description: "The standard lift of prefix Kolmogorov complexity to Euclidean space: conditional complexity of sets via rational approximations, after Shen–Vereshchagin and Lutz–Lutz."
---

This page discusses how our measures of incompressibility (via Kolmogorov complexity) can be lifted to quantity the (limiting) incompressibility of points in Euclidean space. In general, {term}`prefix complexity` may be lifted to {term}`infinitary objects <Infinitary object>` via {term}`finitary <Finitary object>` approximations. We state the following results how they were originally presented: over Euclidean space. Analogous statements also hold over Cantor space.

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

## Lifts via Dyadic Cubes

The dyadic cubes serve as a convenient geometric basis over which to measure complexity along the reals.

As illustrated above, the standard method for lifting prefix complexity to points in a metric space is via a computable, dense subset. Recall that the complexity of an arbitrary subset $X \subseteq \mathbb{R}^m$ was defined as the minimal complexity of a rational in $X$ (or $+\infty$ if no such rational exists). Intuitively, this definition captures the idea that a set is *simple* if it contains a point that is simple to describe, and complex otherwise. Likewise, the complexity of an arbitrary point $x \in \mathbb{R}^m$ is definable to some precision-level $r \in \omega$ as the minimum complexity of a rational in the open $2^{-r}$-ball about $x$. And, as we saw above, this is essentially equivalent to evaluating the complexity of the dyadic truncation of $x$ up to precision $2^{-r}$ as in Lemma [%s](#maxmin_truncation_for_r), or to finding a $K$-minimizer to $B_{2^{-r}}(x)$ as in Lemma 4.9 of {cite:t}`CL14`.

Something similar is true in the conditional case using either the max-min or min-max definitions of conditional prefix complexity $K_{r \mid s}$ as discussed later in section [%s](#section:Robustness_of_the_Lift). Already, Lemma [%s](#maxmin_truncation_for_r_s) shows the ability for dyadic truncation to approximate $K_{r \mid s}$, while Proposition [%s](#lemma:conditional_K_minimizers_suffice) will do the same via $K$-minimizers.

Let us now introduce a family of lifts of prefix complexity to Euclidean space via dyadic cubes. Note that a dyadic cube $Q \in \mathcal{Q}^m$ may be regarded in two ways:
1. as a subset of $\mathbb{R}^m$, having prefix complexity $K(Q) = \min \set{K(q)}{q \in Q \cap \mathbb{Q}^m}$ equal to that of its simplest rational element, or 
2. as a finitary object: write $\ulcorner Q \urcorner$ for the index of $Q$ in a standard, computable enumeration of $\mathcal{Q}^m$, so that $K(\ulcorner Q \urcorner)$ is the complexity of describing the cube $Q$ itself. 

The two readings differ by at most the cost of describing the depth of $Q$.

:::{prf:observation}
:label: observation:cube_code_vs_cube_set
For all $m \in \omega$, oracles $A$, depths $r \in \omega$, and dyadic cubes $Q \in \mathcal{Q}^m_r$,

$$
\begin{aligned}
K^A(Q) - O_m(1) \leq K^A(\ulcorner Q \urcorner) \leq K^A(Q) + K(r) + O_m(1).
\end{aligned}
$$
:::

:::{prf:proof}
The left inequality follows from the fact that the center of $Q$ is a rational element of $Q$, which is computable from $\ulcorner Q \urcorner$ and $m$. 

The right inequality follows from the fact that, for any rational $q \in \mathbb{Q}^m$, a description of $Q_r(q)$ is computable from $r$, $q$, and $m$.
:::

Let

$$
\begin{aligned}
H_r(x) := \min \set{K(\ulcorner Q \urcorner)}{Q \in \mathcal{Q}^m \text{ and } Q \subseteq B_{2^{-r}}(x)},
\end{aligned}
$$

(or $+\infty$ if the minimum is taken over $\varnothing$) denote another lift of complexity to points in $\mathbb{R}^m$. Intuitively, this definition captures the idea that a point is *simple* if there are always sufficiently simple dyadic cubes in its vicinity. Clearly, $H_r(x) \geq^+ K_r(x)$, as any dyadic cube $Q \subseteq B_{2^{-r}}(x)$ has its center in $B_{2^{-r}}(x)$, too. In fact, these two notions do not significantly differ.

:::{prf:proposition}
:label: prop:H_and_K_Euclidean
For all $m \in \omega$, oracles $A$, $x \in \mathbb{R}^m$, and $r \in \omega$,

$$
\begin{aligned}
H^A_r(x) = K^A_r(x) \pm o(r),
\end{aligned}
$$

where $o(r)$ is a sub-linear term in $r$ independent of $A$ and $x$.
:::

:::{prf:proof}
By Lemma [%s](#maxmin_truncation_for_r), it suffices to show $H_r(x) = K(\restrict{x}{r}) \pm o(r)$.

Suppose we are given any dyadic cube $Q \subseteq B_{2^{-r}}(x)$. In particular, its center is rational and computable from $\ulcorner Q \urcorner$, and approximates $\restrict{x}{r}$ to a precision $O(2^{-r})$. Thus,

$$
\begin{aligned}
K(\restrict{x}{r}) \leq K(\ulcorner Q \urcorner) + O(1) \implies K(\restrict{x}{r}) \leq H_r(x) + O(1).
\end{aligned}
$$

In the other direction, notice that $\restrict{x}{r}$ is a dyadic rational inside $B_{2^{-r}}(x)$. A simple geometric fact states that there must be one dyadic cube $Q$ of side-length at least $\frac{1}{\sqrt{m}} \cdot 2^{-r}$ which is a subset of the expanded ball: $B_{2 \cdot 2^{-r}}(\restrict{x}{r})$. And by comparing volumes, there can be no more than $(4 / \sqrt{m})^m$ many such dyadic cubes. Given $\restrict{x}{r}$, we may effectively enumerate all dyadic cubes which are subsets of $B_{2 \cdot 2^{-r}}(\restrict{x}{r})$ and simply specify any one of them by providing its index in that enumeration. Such an index requires no more than $\log((4 / \sqrt{m})^m) = O(m \log m)$ many bits to specify. And for any dyadic cube $Q \subseteq B_{2^{-r}}(x)$, it follows from the triangle inequality that $Q \subseteq B_{2 \cdot 2^{-r}}(\restrict{x}{r})$, and so,

$$
\begin{aligned}
H_r(x) \leq K(\ulcorner Q \urcorner) \leq K(\restrict{x}{r}) + K(r) + O(m \log m) + O(1).
\end{aligned}
$$
:::

Yet another lift (which does not significantly differ from the rest) may be defined as follows:

$$
\begin{aligned}
G_r(x) := \min \set{K(\ulcorner Q \urcorner)}{x \in Q \in \mathcal{Q}^m \text{ and } \diam(Q) \leq 2^{-r}},
\end{aligned}
$$

(or $+\infty$ if the minimum is taken over $\varnothing$). Intuitively, this definition captures the idea that a point is *simple* if there are sufficiently small and simple dyadic cubes covering it. Compared to $H_r(x)$, the fourth notion $G_r(x)$ minimizes prefix complexity over a smaller class of dyadic cubes, since $x \in Q$ and $\diam(Q) \leq 2^{-r}$ imply $Q \subseteq B_{2^{-r}}(x)$, but not vice versa. Nevertheless, we observe asymptotic coincidence between the two notions.

:::{prf:proposition}
:label: prop:G_and_K_Euclidean
For all $m \in \omega$, oracles $A$, $x \in \mathbb{R}^m$, and $r \in \omega$,

$$
\begin{aligned}
G^A_r(x) = K^A_r(x) \pm o(r),
\end{aligned}
$$

for some fixed $o(r)$ term in $r$ independent of $A$ and $x$.
:::

The proof of Proposition [%s](#prop:G_and_K_Euclidean) is nearly identical to that of Proposition [%s](#prop:H_and_K_Euclidean), noting that exactly one of the at most $(4 / \sqrt{m})^m$ dyadic cubes in $B_{2 \cdot 2^{-r}}(\restrict{x}{r})$ must contain $x$.

Next, regarding dyadic cubes as subsets instead, the complexity of the single cube $Q_r(x)$ of depth $r$ containing $x$ also approximates $K_r(x)$:

:::{prf:lemma}
:label: lemma:cube_vs_point_complexity
For all $m \in \omega$, oracles $A$, $x \in \mathbb{R}^m$, and $r \in \omega$,

$$
\begin{aligned}
K^A(Q_r(x)) = K^A_r(x) \pm o(r),
\end{aligned}
$$

for some fixed $o(r)$ term in $r$ independent of $A$ and $x$.
:::

:::{prf:proof}
Take any $q \in B_{2^{-r}}(x) \cap \mathbb{Q}^m$ minimizing $K(q)$. By a small geometric argument, at most $3^m$ dyadic cubes from $\mathcal{Q}^m_r$ may pass within $\pm 2^{-r}$ of $q$ along each axis simultaneously. So we may compute the rational center of $Q_r(x)$ using $q$, $r$, $m$ and an index of $Q_r(x)$ in a standard computable enumeration of these $3^m$ cubes. This shows $K(Q_r(x)) \leq K_r(x) + o(r)$.

In the other direction, take any $q \in Q_r(x) \cap \mathbb{Q}^m$ minimizing $K(q)$, and let $d := \ceil{\log \sqrt{m}}$. Of course, $q$ and $r$ compute $Q_r(q) = Q_r(x)$. And they list its $2^{md}$ subcubes in $\mathcal{Q}^m_{r + d}$. The unique subcube containing $x$ has a center which lies within $\frac{\sqrt{m}}{2} 2^{-(r + d)} \leq 2^{-(r + 1)}$ of $x$. Thus, descriptions for $q$, $r$, and an $md$-bit index produce a rational in $B_{2^{-r}}(x)$. This shows $K_r(x) \leq K(Q_r(x)) + o(r)$.
:::

The final variant begins with a definition: let a **rational closed ball** be a set 

$$
\overline{B}_\delta(q) := \set{x \in \mathbb{R}^m}{\norm{x - q} \leq \delta}
$$ 
with $q \in \mathbb{Q}^m$ and $\delta \in \mathbb{Q}_{> 0}$. Fix a computable encoding of rational closed balls by strings, so that for each {term}`oracle` $A$ the machine $\mathbf{U}^A_{\operatorname{PF}}$ induces a partial map $\mathbf{U}^A$ from programs to rational closed balls, ignoring outputs that do not encode a ball. Its domain is prefix-free. The **ball complexity of $x$ at precision-level $r$ relative to $A$** is

$$
\begin{aligned}
L^{\mathbf{U}^A}_r(x) := \min \set{\operatorname{len}(\pi)}{\mathbf{U}^A(\pi) \downarrow \ni x \text{ and } \operatorname{diam} \mathbf{U}^A(\pi) \leq 2^{-r}}.
\end{aligned}
$$

This is the special case $\varphi = \mathbf{U}^A$ of the code length $L^\varphi_r(x)$ of an arbitrary prefix-free ball code $\varphi$ (Definition [%s](#definition:prefix_free_ball_code)). We see another asymptotic agreement due to Miyabe:

:::{prf:proposition} Proposition 5.7 of {cite:t}`Miy26`
:label: proposition:ball_vs_point_complexity
For all $m \in \omega$ there exists $c \in \omega$ such that for all oracles $A$, all $x \in \mathbb{R}^m$, and all $r \in \omega$,

$$
\begin{aligned}
K^A_r(x) \leq L^{\mathbf{U}^A}_r(x) + c \qquad \text{and} \qquad L^{\mathbf{U}^A}_r(x) \leq K^A_r(x) + 2K(r) + c.
\end{aligned}
$$
:::

:::{prf:proof}
If $\mathbf{U}^A(\pi) = \overline{B}_\delta(q)$ witnesses $L^{\mathbf{U}^A}_r(x)$, then $\norm{x - q} \leq \delta \leq 2^{-(r+1)} < 2^{-r}$, so a program that outputs the center $q$ witnesses the first inequality. Conversely, if $\norm{x - q} < 2^{-(r + 1)}$, then a program for $q$ together with a self-delimiting description of $r$ names $\overline{B}_{2^{-(r + 1)}}(q)$, which contains $x$ and has diameter $2^{-r}$. Then apply Lemma [%s](#lemma:linearity_r_no_condition) with $\Delta r = 1$. 
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
It is also continuous from below along arbitrary increasing sequences; and is continuous from above along decreasing sequences of compact sets. In the language of capacities, $\Pi_m$ is a maxitive Choquet capacity whose point density function is $m$ on $\mathbb{Q}^n$ and zero everywhere else. After normalization, we might further refer to this outer measure as a possibility measure with possibility distribution $g_m$. 

Always $\Pi_m \leq \mu_m$. 

In his doctoral dissertation, N. Lutz introduced the function $\boldsymbol{\kappa}(X) := 2^{-K(X)}$, where $K(X) := \min \{ K(q) : q \in X \cap \mathbb{Q}^n \}$, and zero if $X$ contains no rational points {cite:p}`Lut17b`. This is exactly $\Pi_m(X)$ for $m(q) := 2^{-K(q)}$, so it is an outer measure.

Relative to any oracle $A$, the Coding Theorem [%s](#theorem:coding_theorem) gives for any $X \subseteq \mathbb{R}^n$:

$$
\boldsymbol{\kappa}^A(X) =^* \Pi_{\mathbf{m}^A}(X).
$$

J. Lutz and N. Lutz showed that, while $\mu_{\mathbf{m}}$ is **globally optimal** (dominating every strongly finite, {term}`lower-semicomputable` outer measure up to a multiplicative constant on all subsets), $\boldsymbol{\kappa}$ is only **locally optimal** {cite:p}`LL20`. This contrast comes down to the inherent differences between the $\mu$ and $\Pi$ lifts. 

This motivates a comparison to how Case and Lutz extended the *a priori* probability and Kolmogorov complexity notations to sets of strings $S \subseteq 2^{<\omega}$ {cite:p}`CL14`:

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

Apply the LDS Coding theorem to $\mathbb{R}^n$: the layers $\mathcal{Q}^n_r$ of the half-open dyadic cubes can computably enumerate their blocks $(r, t)$. And the blocks of $\mathcal{Q}^n_r$ partition $\mathbb{R}^n$. This builds an LDS. Using [%s](#theorem:LDS_coding_theorem), we may conclude that $\Pi_{\mathbf{m}^A}$ and $\mu_{\mathbf{m}^A}$ essentially agree on half-open dyadic cubes.

:::{prf:corollary}
:label: corollary:sum_sup_dyadic
For every $n \in \omega$, oracle $A$, $r \in \omega$, and cube $Q \in \mathcal{Q}^n_r$,

$$
\Pi_{\mathbf{m}^A}(Q) \leq \mu_{\mathbf{m}^A}(Q) \leq 2^{K(r) + O(1)} \cdot \Pi_{\mathbf{m}^A}(Q).
$$
:::

That is, at each dyadic layer, the additive and maxitive extensions of $\mathbf{m}^A$ agree up to a factor of $2^{o(r)}$. This is the fact that J. Lutz and N. Lutz use to prove that $\boldsymbol{\kappa}$ is locally optimal {cite:p}`LL20`.

In fact, essentially the same LDS coding argument works for any finite measure whose values on dyadic cubes an oracle can approximate from below:

:::{prf:lemma}
:label: lemma:coding_bound_from_measure
Let $\nu$ be a finite Borel measure on $\mathbb{R}^n$, and let $A$ be an oracle relative to which $Q \mapsto \nu(Q)$ is lower-semicomputable on the domain $\mathcal{Q}^n$. Then there exists $c \in \omega$ such that for all $x \in \mathbb{R}^n$ and all $r \in \omega$,

$$
\begin{aligned}
K^A_r(x) \leq -\log \nu(Q_r(x)) + K(r) + c.
\end{aligned}
$$
:::
:::{prf:proof}
Fix a rational $M \geq \nu(\mathbb{R}^n)$, and put for each $Q \in \mathcal{Q}^n$:
$$
m(Q) := 2^{-K(\operatorname{depth}(Q))} \cdot \frac{\nu(Q)}{M}.
$$

Each layer $\mathcal{Q}^n_r$ partitions $\mathbb{R}^n$, so by the Kraft Inequality [%s](#theorem:kraft_inequality),
$$
\sum_{r \in \omega} \sum_{Q \in \mathcal{Q}^n_r} m(Q) \leq \sum_{r \in \omega} 2^{-K(r)} \leq 1.
$$ 

So, $m$ is a discrete semimeasure on $\mathcal{Q}^n$ which is lower-semicomputable in $A$. By the optimality of $\mathbf{m}^A$ and the Coding Theorem [%s](#theorem:coding_theorem) relativized to $A$, we derive for any $Q \in \mathcal{Q}^n_r$:

$$
\begin{aligned}
K^A(\ulcorner Q \urcorner) \leq^+ -\log m(Q) =^+ -\log \nu(Q) + K(r),
\end{aligned}
$$

where the constant may depend on $M$ and $\nu$, but not on $Q$. Finally, let $d := \ceil{\frac{1}{2} \log n}$. From $\ulcorner Q_r(x) \urcorner$ and the $nd$-bit index of $Q_{r+d}(x)$ among the $2^{nd}$ cubes of $\mathcal{Q}^n_{r+d}$ inside $Q_r(x)$, we can compute the center $q$ of $Q_{r+d}(x)$, which satisfies $\norm{x - q} \leq \frac{\sqrt{n}}{2} 2^{-(r + d)} \leq 2^{-r}$. So $K^A_r(x) \leq^+ K^A(\ulcorner Q_r(x) \urcorner)$. (Passing through the set $Q_r(x)$ and Lemma [%s](#lemma:cube_vs_point_complexity) instead would cost a second $K(r)$, since the code $\ulcorner Q_r(x) \urcorner$ already knows $r$ but a rational point of $Q_r(x)$ does not.)
:::

The reverse inequality fails pointwise: for Lebesgue measure $\lambda$ on $[0,1)^n$, we have $-\log \lambda(Q_r(x)) = nr$ for every $x \in [0,1)^n$, while $K_r(x) = O(\log r)$ whenever $x$ is computable. But it does hold almost everywhere!

:::{prf:lemma}
:label: lemma:measure_bound_almost_everywhere
Let $\nu$ be a finite Borel measure on $\mathbb{R}^n$, and let $A$ be any oracle. Then for $\nu$-almost every $x \in \mathbb{R}^n$, for all sufficiently large $r \in \omega$,

$$
\begin{aligned}
-\log \nu(Q_r(x)) \leq K^A_r(x) + K(r).
\end{aligned}
$$
:::

:::{prf:proof}
For each $r \in \omega$, let 
$$
\mathcal{S}_r := \set{Q \in \mathcal{Q}^n_r}{(\exists x \in Q) \left[\nu(Q) < 2^{-K(r)} \cdot 2^{-K^A_r(x)} \right]}.
$$

For each $Q \in \mathcal{S}_r$, fix such an $x_Q$, together with a rational $q_Q \in B_{2^{-r}}(x_Q)$ minimizing $K^A(q_Q)$. Each ball $B_{2^{-r}}(q)$ lies in a box of side-length $2^{1-r}$, which meets at most $3^n$ cubes from $\mathcal{Q}^n_r$. Thus, if $q = q_Q$, then $x_Q \in Q \cap B_{2^{-r}}(q)$, meaning $Q$ meets the box. Hence each rational $q$ equals $q_Q$ for at most $3^n$ cubes $Q \in \mathcal{S}_r$. Then by applying the Kraft Inequality ([%s](#theorem:kraft_inequality)) twice,

$$
\begin{aligned}
\nu\p{\textstyle\bigcup \mathcal{S}_r} \leq \sum_{Q \in \mathcal{S}_r} \nu(Q) &\leq 2^{-K(r)} \sum_{Q \in \mathcal{S}_r} 2^{-K^A(q_Q)}\\
&\leq 3^n \cdot 2^{-K(r)} \sum_{q \in \mathbb{Q}^n} 2^{-K^A(q)} \leq 3^n \cdot 2^{-K(r)},\\
\implies \sum_{r \in \omega} \nu\p{\textstyle\bigcup \mathcal{S}_r} &\leq 3^n \sum_{r \in \omega} 2^{-K(r)} \leq 3^n.
\end{aligned}
$$

By summability, the Borel–Cantelli Lemma guarantees that $\nu$-almost every $x$ lies in $\bigcup \mathcal{S}_r$ for only finitely many $r$. For such $x$ and all large $r$, $Q_r(x) \notin \mathcal{S}_r$, so $\nu(Q_r(x)) \geq 2^{-K(r)} \cdot 2^{-K^A_r(x)}$.
:::

So if $A$ is strong enough to lower-semicompute $\nu$ on $\mathcal{Q}^n$, then combining Lemmas [%s](#lemma:coding_bound_from_measure) and [%s](#lemma:measure_bound_almost_everywhere), for $\nu$-almost every $x$ and all sufficiently large $r$,

$$
\begin{aligned}
-\log \nu(Q_r(x)) = K^A_r(x) \pm o(r).
\end{aligned}
$$
---

In summary, we have shown a number of results for lifts of Kolmogorov complexity to the reals:
- $K_r(x) := K(B_{2^{-r}}(x)) = -\log \boldsymbol{\kappa}(B_{2^{-r}}(x)) =^+ -\log \Pi_{\mathbf{m}}(B_{2^{-r}}(x))$.
- The other lifts: $K(x \upharpoonright r)$, $H_r(x)$, $G_r(x)$, $K(Q_r(x))$, and $L^{\mathbf{U}}_r(x)$ agree with $K_r(x)$ up to logarithmic factors in $r$. 
- $\mu_{\mathbf{m}}$ agrees with $K_r(x)$ up to logarithmic factors *on dyadic cubes*.
- Finite Borel measures will have $-\log \nu(Q_r(x))$ agree with $K^A_r(x)$ up to logarithmic factors for almost every $x$ and $r$ and for all sufficiently strong oracles.