---
title: "Lifting Prefix Complexity to Reals"
label: section:Lifting_Prefix_Complexity_to_Reals
---

Prefix complexity may be lifted to infinitary objects via finitary approximations. We state the following results how they were originally presented: over Euclidean space. Analogous statements also hold over Cantor space.

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

One may then conclude an approximate symmetry of information for prefix complexity on Euclidean space. Again, this is a weak form of symmetry of information.

::::{prf:theorem} Approximate Chain Rule; Lemma 4 of {cite:t}`LS16`
:label: theorem:approximate_SOI_conditional
For any $m, n \in \omega$, $x \in \mathbb{R}^m$, $y \in \mathbb{R}^n$, and $r \geq s \in \omega$,

:::{div}
:class: roman-list
1. $\abs{K_{r \mid r}(x \mid y) + K_r(y) - K_{r}(x, y)} \leq O_{m, n}(\log r) + O_n(\log \log \norm{y}) + O_{m, n}(1)$;
1. $\abs{K_{r \mid s}(x \mid x) + K_s(x) - K_r(x)} \leq O_m(\log r) + O_m(\log \log \norm{x}) + O_m(1)$.
:::
::::

We note that when computing with infinitary objects such as infinite binary strings or Euclidean reals, one must distinguish between **oracle** and **conditional** accesses. While oracle access permits computations with approximations of the given data to arbitrary precisions, conditional access places a firm limit on the precision-level to which one may access the given data.

:::{prf:lemma} Lemma 14 of {cite:t}`LL18`
:label: oracle_access_to_conditional
For all $m, n \in \omega$, there exists a constant $c \in \omega$ such that, for all $x \in \mathbb{R}^m$, $y \in \mathbb{R}^n$, and $r, s \in \omega$,

$$
\begin{aligned}
K^y_r(x) \leq K_{r \mid s}(x \mid y) + K(s) + c.
\end{aligned}
$$
:::
