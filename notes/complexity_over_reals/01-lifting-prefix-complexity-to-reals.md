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

## Lifts via Dyadic Cubes

The dyadic cubes serve as a convenient geometric basis over which to measure complexity along the reals.

As illustrated above, the standard method for lifting prefix complexity to points in a metric space is via a computable, dense subset. Recall that the complexity of an arbitrary subset $X \subseteq \mathbb{R}^m$ was defined as the minimal complexity of a rational in $X$ (or $+\infty$ if no such rational exists). Intuitively, this definition captures the idea that a set is *simple* if it contains a point that is simple to describe, and complex otherwise. Likewise, the complexity of an arbitrary point $x \in \mathbb{R}^m$ is definable to some precision-level $r \in \omega$ as the minimum complexity of a rational in the open $2^{-r}$-ball about $x$. And, as we saw above, this is essentially equivalent to evaluating the complexity of the dyadic truncation of $x$ up to precision $2^{-r}$ as in Lemma [%s](#maxmin_truncation_for_r), or to finding a $K$-minimizer to $B_{2^{-r}}(x)$ as in Lemma 4.9 of {cite:t}`CL14`.

Something similar is true in the conditional case using either the max-min or min-max definitions of conditional prefix complexity $K_{r \mid s}$ as discussed later in section [%s](#section:Robustness_of_the_Lift). Already, Lemma [%s](#maxmin_truncation_for_r_s) shows the ability for dyadic truncation to approximate $K_{r \mid s}$, while Proposition [%s](#lemma:conditional_K_minimizers_suffice) will do the same via $K$-minimizers.

Let us now introduce a family of lifts of prefix complexity to Euclidean space via dyadic cubes.

On the [Notation](#section:Notation) page, we defined the collection $\mathcal{Q}^m$ of all dyadic rational cubes over $\mathbb{R}^m$. If $Q \in \mathcal{Q}^m$ is a dyadic cube, let $K(Q)$ denote the prefix complexity $K(i)$ of the index of $Q$ in a standard (computable) enumeration of $\mathcal{Q}^m$. 

First, let

$$
\begin{aligned}
H_r(x) := \min \set{K(Q)}{Q \in \mathcal{Q}^m \text{ and } Q \subseteq B_{2^{-r}}(x)},
\end{aligned}
$$

or $+\infty$ if the minimum is taken over the empty set, denote a third lift of complexity to points in $\mathbb{R}^m$. Intuitively, this definition captures the idea that a point is *simple* if there are always sufficiently simple dyadic cubes in its vicinity. Clearly, $H_r(x) \geq^+ K_r(x)$, as the center $c_Q$ of any dyadic cube $Q$ satisfying $Q \subseteq B_{2^{-r}}(x)$ will satisfy $c_Q \in B_{2^{-r}}(x)$. Yet, these notions do not differ significantly.

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

or $+\infty$ if the minimum is taken over the empty set. Then, $G_r(x)$ denotes a fourth lift of prefix complexity to points in $\mathbb{R}^m$. Intuitively, this definition captures the idea that a point is *simple* if there are sufficiently small and simple dyadic cubes covering it. Compared to $H_r(x)$, this fourth notion $G_r(x)$ minimizes prefix complexity over a smaller class of dyadic cubes, since $x \in Q$ and $\diam(Q) \leq 2^{-r}$ imply $Q \subseteq B_{2^{-r}}(x)$, but not vice versa. Nevertheless, we observe asymptotic coincidence between the two notions.

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
:nonumber:
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
For every oracle $A$, precision-level $r \in \omega$, and every half-open dyadic cube $D \in \mathcal{Q}^n_r$,

$$
\Pi_{\mathbf{m}^A}(D) \leq \mu_{\mathbf{m}^A}(D) \leq 2^{K(r) + O(1)} \cdot \Pi_{\mathbf{m}^A}(D).
$$
:::

That is, at each dyadic layer, the additive and maxitive extensions of $\mathbf{m}^A$ agree up to a factor of $2^{o(r)}$. This is the fact that J. Lutz and N. Lutz use to prove that $\boldsymbol{\kappa}$ is locally optimal {cite:p}`LL20`.

In summary, we have $K_r(x) = K(B_{2^{-r}}(x)) = -\log \boldsymbol{\kappa}(B_{2^{-r}}(x))$, while $\boldsymbol{\kappa} =^* \Pi_{\mathbf{m}}$. And the other lifts $K(x \upharpoonright r)$, $G_r(x)$, $H_r(x)$, and $L^{\mathbf{U}}_r(x)$ agree up to logarithmic factors in $r$. Likewise, $\mu_{\mathbf{m}}$ agrees up to logarithmic factors on dyadic cubes.