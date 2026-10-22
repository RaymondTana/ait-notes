---
title: "Effective Dimension under Uniformly Continuous Maps"
label: section:Effective_Dimension_under_Uniformly_Continuous_Maps
---

## Uniform and Lipschitz Continuities

A **uniformly continuous function** is a real function which has a modulus of uniform continuity.

:::{prf:definition}
A **modulus of uniform continuity** for the function $f : \mathbb{R}^m \to \mathbb{R}^n$ is any non-decreasing function $\mu : \omega \to \omega$ such that, for all $x_1, x_2 \in \mathbb{R}^m$ and $r \in \omega$,

$$
\begin{aligned}
\norm{x_1 - x_2} \leq 2^{-\mu(r)} \implies \norm{f(x_1) - f(x_2)} \leq 2^{-r}.
\end{aligned}
$$
:::

In particular, a uniformly continuous function is called **Hölder continuous** if it has a modulus of uniform continuity of the form $\mu(r) = \ceil{(r + c) / \alpha}$ where $\alpha > 0$ and $c \in \mathbb{R}$; and **Lipschitz continuous** if it has a modulus of uniform continuity of the form $\mu(r) = r + O(1)$.

An injection $f: \mathbb{R}^m \to \mathbb{R}^n$ is called **co-uniformly continuous** if it has a uniformly continuous inverse map. We use the prefix “co” similarly for maps with Hölder continuous or Lipschitz continuous inverses. Any modulus of uniform continuity for the inverse of a co-uniformly continuous map $f$ is called an **inverse-modulus** for $f$. A bijection $f : \mathbb{R}^m \to \mathbb{R}^m$ is called **bi-uniformly continuous** if $f$ is both uniformly continuous and co-uniformly continuous. We similarly use “bi” in the case of a map and its inverse both being Hölder or Lipschitz continuous.

Clearly, a map $f: \mathbb{R}^m \to \mathbb{R}^n$ is Lipschitz continuous if and only if there exists $L \geq 0$ such that for each $x_1, x_2 \in \mathbb{R}^m$,

$$
\begin{aligned}
\norm{f(x_1) - f(x_2)} \leq L \cdot \norm{x_1 - x_2}.
\end{aligned}
$$

We refer to $L$ as a **Lipschitz constant** for $f$.

Likewise, an injection $f: \mathbb{R}^m \to \mathbb{R}^n$ is co-Lipschitz continuous if and only if there exists $C \geq 0$ such that for each $x_1, x_2 \in \mathbb{R}^m$,

$$
\begin{aligned}
C \cdot \norm{x_1 - x_2} \leq \norm{f(x_1) - f(x_2)}.
\end{aligned}
$$

We refer to $C$ as a **co-Lipschitz constant** for $f$.

More generally, a map $f : \mathbb{R}^m \to \mathbb{R}^n$ is Hölder continuous if and only if there exist constants $\alpha > 0$ and $L > 0$ such that for each $x_1, x_2 \in \mathbb{R}^m$:

$$
\begin{aligned}
\norm{f(x_1) - f(x_2)} \leq L \cdot \norm{x_1 - x_2}^\alpha.
\end{aligned}
$$

We refer to $\alpha$ as an **exponent** for $f$.

There is also a notion of **local Lipschitz continuity**. Call a function $f : \mathbb{R}^m \to \mathbb{R}^n$ defined on open set to be **locally Lipschitz continuous** if for every $x \in \operatorname{dom}(f)$, there exist an open neighborhood $U \subseteq \operatorname{dom}(f)$ containing $x$ and a constant $L > 0$ such that for each $x_1, x_2 \in U$, we have

$$
\begin{aligned}
\norm{f(x_1) - f(x_2)} \leq L \cdot \norm{x_1 - x_2}.
\end{aligned}
$$

Analogous local definitions exist for the other uniform continuity notions.

## Known Results

Hausdorff dimension is invariant under bi-Lipschitz continuous transformations. This follows from the classical result about Hausdorff dimension under Hölder continuous transformations (see Proposition 2.2 of {cite:t}`Fal90`). Yet, there is also an effective proof due to J. Reimann {cite:p}`Rei04`. Reimann further effectivized the result to get a similar statement for effective dimension. In particular, let $f$ be a computable, Hölder continuous transformation on $2^\omega$ with exponent $\alpha > 0$. Then $f$ is **$\alpha$-expansive**, meaning for any $x \in 2^\omega$, we have $\operatorname{len}(\restrict{f(x)}{r}) \geq \alpha \cdot r$ for all but finitely many $r \in \omega$. This gives for each $x \in 2^\omega$ and $r \in \omega$:

$$
\begin{aligned}
K(\restrict{f(x)}{(\alpha \cdot r)}) \leq^+ K(f(\restrict{x}{r})) \leq^+ K(\restrict{x}{r}).
\end{aligned}
$$

So, for any $X \subseteq 2^\omega$, we have $\dim(f(X)) \leq \dim(X) / \alpha$ in the limit (see Theorem 2.27 of {cite:t}`Rei04`). Thus, effective dimension is invariant under bi-computable, bi-Lipschitz continuous maps. This fact extends to bi-computable maps which are only **locally** bi-Lipschitz continuous.

These basic results mimic the data processing inequalities for mutual dimension by A. Case and J. Lutz {cite:p}`CL14`. For instance, recall that Theorem [%s](#theorem:mutual_dimension_invariant_under_computable_bi_Lipshictz) states the mutual dimension between two reals is invariant under computable, bi-Lipschitz maps. Here, we establish analogous results for conditional dimension.

## Modulus and Data Processing for Conditional Dimension

We begin our analysis with an analogue of Lemma 6.3 from {cite:t}`CL14`–which applies to the lift of mutual information to Euclidean space–to clarify how conditional prefix complexity behaves under computable, uniformly continuous functions. If $f$ is a computable, Lipschitz continuous map, then there is a computable real number $L \in \mathbb{Q}^+$ serving as a Lipschitz constant for $f$. That is, $f$ has computable modulus $\mu(r) := r + \log L$. With this in mind, we may now state the **modulus and data processing inequalities** for conditional prefix Kolmogorov complexity lifted to Euclidean space.

Recall that we write any (in)equalities for Kolmogorov complexity for the rest of the section up to the sub-linear factors in the precision-levels given by ([%s](#equation:logarithmic_factors)). In contrast, the corresponding (in)equalities for effective dimension are exact.

::::{prf:lemma} Forward Modulus and Data Processing Inequalities for Conditional Complexity
:label: lemma:forward_data_processing_conditional
Let $m, n, k \in \omega$, $x \in \mathbb{R}^m$, $y \in \mathbb{R}^n$, and $r, s \in \omega$.

:::{div}
:class: roman-list
1. If $f: \mathbb{R}^m \to \mathbb{R}^k$ is computable and uniformly continuous with computable modulus $\mu$, then

   $$
   \begin{aligned}
   K_{r \mid s}(f(x) \mid y) \leq K_{\mu(r + 1) \mid s}(x \mid y).
   \end{aligned}
   $$

   In particular, if $f$ is also Lipschitz continuous,

   $$
   \begin{aligned}
   \dim(f(x) \mid y) \leq \dim(x \mid y).
   \end{aligned}
   $$

1. If $f: \mathbb{R}^n \to \mathbb{R}^k$ is computable and uniformly continuous with computable modulus $\mu$, then

   $$
   \begin{aligned}
   \KcAt{r \mid \mu(s + 1)}{x}{y} \leq \KcAt{r \mid s}{x}{f(y)}.
   \end{aligned}
   $$

   In particular, if $f$ is also Lipschitz continuous,

   $$
   \begin{aligned}
   \dim(x \mid y) \leq \dim(x \mid f(y)).
   \end{aligned}
   $$
:::
::::

:::{prf:proof}
:nonumber:
We start by proving (i). Let $p_{f(x)}^* \in B_{2^{-r}}(f(x))$, $p_x^* \in B_{2^{-\mu(r + 1)}}(x)$ and $q^* \in B_{2^{-s}}(y)$ be $K$-minimizers in their respective open balls. Since $f$ is computable, there is an oracle prefix-free Turing machine $M$ which approximates $f$ arbitrarily well at $p^*_x$ when given $p^*_x$ as an oracle; say, such that for any $r \in \omega$ we have $\abs{M^{p^*_x}(r) - f(p^*_x)} \leq 2^{-(r + 1)}$. Since $\mu$ is a modulus for $f$, $M$ also approximates $f$ arbitrarily well at $x$ when given $p^*_x$ as an oracle, since for any $r$,

$$
\begin{aligned}
\abs{M^{p^*_x}(r) - f(x)} \leq \abs{M^{p^*_x}(r) - f(p^*_x)} + \abs{f(p^*_x) - f(x)} \leq 2^{-(r + 1)} + 2^{-(r + 1)} = 2^{-r}.
\end{aligned}
$$

We use $M^{p^*_x}(r) \in B_{2^{-r}}(f(x))$ to conclude:

$$
\begin{aligned}
\KcAt{r \mid s}{f(x)}{y} &= \Kc{p^*_{f(x)}}{q^*} & [\text{Proposition~\ref{lemma:conditional_K_minimizers_suffice}}]\\
&\leq\Kc{p^*_{f(x)}}{M^{p^*_x}(r)} +  \Kc{M^{p^*_x}(r)}{q^*}\\
&\leq \Kc{M^{p^*_x}(r)}{q^*} & [\text{Corollary~\ref{corollary:K_minimizer_not_complex}}]\\
&\leq \Kc{p^*_x}{q^*} & [\text{Theorem~\ref{theorem:bounded_computable_output}}]\\
&= \KcAt{\mu(r + 1) \mid s}{x}{y}. & [\text{Proposition~\ref{lemma:conditional_K_minimizers_suffice}}]
\end{aligned}
$$

So, if $f$ is indeed Lipschitz continuous, then there is a computable modulus for $f$ of the form $\mu(r) = r + O(1)$, giving

$$
\begin{aligned}
\dim(f(x) \mid y) &= \liminf_{r \to \infty} \frac{K_{r \mid r}(f(x) \mid y)}{r}\\
&\leq \liminf_{r \to \infty} \frac{K_{\mu(r + 1) \mid r}(x \mid y)}{r}\\
&= \liminf_{r \to \infty} \frac{K_{r + O(1) \mid r}(x \mid y)}{r}\\
&= \liminf_{r \to \infty} \frac{K_{r \mid r}(x \mid y)}{r} & [\text{Lemma~\ref{lemma:linearity_with_condition}(i)}]\\
&= \dim(x \mid y).
\end{aligned}
$$

The proof of (ii) is similar. This time, let $p^* \in B_{2^{-r}}(x)$, $q_y^* \in B_{2^{-\mu(s + 1)}}(y)$, and $q_{f(y)}^* \in B_{2^{-s}}(f(y))$ be $K$-minimizers in their respective open balls. Since $f$ is computable, there is an oracle prefix-free Turing machine $M$ which approximates $f$ arbitrarily well at $q^*_y$ when given $q^*_y$ as an oracle: $\abs{M^{q^*_y}(s) - f(q^*_y)} \leq 2^{-(s + 1)}$. Since $\mu$ is a modulus for $f$, we get that $M$ also approximates $f$ arbitrarily well at $y$ when given $q^*_x$ as an oracle:

$$
\begin{aligned}
\abs{M^{q^*_y}(s) - f(y)} \leq \abs{M^{q^*_y}(s) - f(q^*_s)} + \abs{f(q^*_s) - f(y)} \leq 2^{-(s + 1)} + 2^{-(s + 1)} = 2^{-s}.
\end{aligned}
$$

We use $M^{q^*_y}(s) \in B_{2^{-s}}(f(y))$ to conclude:

$$
\begin{aligned}
\KcAt{r \mid \mu(s + 1)}{x}{y} &= \Kc{p^*}{q^*_y} & [\text{Proposition~\ref{lemma:conditional_K_minimizers_suffice}}]\\
&= \Kc{p^*}{M^{q^*_y}(s)} + \Kc{M^{q^*_y}(s)}{q^*_y}\\
&\leq \Kc{p^*}{M^{q^*_y}(s)} + \Kc{q^*_y}{q^*_y} & [\text{Theorem~\ref{theorem:bounded_computable_output}}]\\
&\leq \Kc{p^*}{q^*_{f(y)}} + \Kc{q^*_{f(y)}}{M^{q^*_y}(s)} \\
&= \Kc{p^*}{q^*_{f(y)}} & [\text{Corollary~\ref{corollary:K_minimizer_not_complex}}]\\
&= \KcAt{r \mid s}{x}{f(y)}. & [\text{Proposition~\ref{lemma:conditional_K_minimizers_suffice}}]
\end{aligned}
$$

So, if $f$ is indeed Lipschitz continuous, then there is a computable modulus for $f$ of the form $\mu(r) = r + O(1)$, giving

$$
\begin{aligned}
\dim(x \mid y) &= \liminf_{r \to \infty} \frac{K_{r \mid r}(x \mid y)}{r}\\
&= \liminf_{r \to \infty} \frac{K_{r \mid r + O(1)}(x \mid y)}{r} & [\text{Lemma~\ref{lemma:linearity_with_condition}(ii)}]\\
&= \liminf_{r \to \infty} \frac{K_{r \mid \mu(r + 1)}(x \mid y)}{r} \\
&\leq \liminf_{r \to \infty} \frac{K_{r \mid r}(x \mid f(y))}{r}\\
&= \dim(x \mid f(y)).
\end{aligned}
$$
:::

Analogous results hold for when the inverse of a function is computable and uniformly continuous.

::::{prf:lemma} Reverse Modulus and Data Processing Inequalities for Conditional Complexity
:label: lemma:reverse_data_processing_conditional
Let $m, n, k \in \omega$, $x \in \mathbb{R}^m$, $y \in \mathbb{R}^n$, and $r, s \in \omega$.

:::{div}
:class: roman-list
1. If $f: \mathbb{R}^m \to \mathbb{R}^k$ is a co-computable, co-uniformly continuous map with computable inverse-modulus $\mu$, then

   $$
   \begin{aligned}
   K_{r \mid s}(x \mid y) \leq K_{\mu(r + 1) \mid s}(f(x) \mid y).
   \end{aligned}
   $$

   In particular, if $f$ is also co-Lipschitz continuous,

   $$
   \begin{aligned}
   \dim(x \mid y) \leq \dim(f(x) \mid y).
   \end{aligned}
   $$

1. If $f: \mathbb{R}^n \to \mathbb{R}^k$ is is a co-computable, co-uniformly continuous map with computable inverse-modulus $\mu$, then

   $$
   \begin{aligned}
   \KcAt{r \mid \mu(s + 1)}{x}{f(y)} \leq \KcAt{r \mid s}{x}{y}.
   \end{aligned}
   $$

   In particular, if $f$ is also co-Lipschitz continuous,

   $$
   \begin{aligned}
   \dim(x \mid f(y)) \leq \dim(x \mid y).
   \end{aligned}
   $$
:::
::::

::::{prf:proof}
:nonumber:
Both parts follow by applying the corresponding result in the previous lemma.

:::{div}
:class: roman-list
1. Denote $z = f(x) \in \mathbb{R}^k$. Apply Lemma [%s](#lemma:forward_data_processing_conditional)(i) to $f^{-1}$ and $(f^{-1}(z), y)$.
1. Denote $z = f(y) \in \mathbb{R}^k$. Apply Lemma [%s](#lemma:forward_data_processing_conditional)(ii) to $f^{-1}$ and $(x, f^{-1}(z))$.
:::
::::

::::{prf:theorem}
:label: theorem:conditional_under_biLipschitz
Let $m, n \in \omega$, $x \in \mathbb{R}^m$, and $y \in \mathbb{R}^n$.

:::{div}
:class: roman-list
1. If $f: \mathbb{R}^m \to \mathbb{R}^m$ is a bi-computable, bi-Lipschitz continuous map, then

   $$
   \begin{aligned}
   K_{r \mid s}(f(x) \mid y) = K_{r \mid s}(x \mid y); \quad \text{so,} \quad \dim(f(x) \mid y) = \dim(x \mid y).
   \end{aligned}
   $$

1. If $f: \mathbb{R}^n \to \mathbb{R}^n$ a bi-computable, bi-Lipschitz continuous map, then

   $$
   \begin{aligned}
   K_{r \mid s}(x \mid f(y)) = K_{r \mid s}(x \mid y); \quad \text{so,} \quad \dim(x \mid f(y)) = \dim(x \mid y).
   \end{aligned}
   $$
:::
::::

::::{prf:proof}
:nonumber:
We combine Lemmas [%s](#lemma:forward_data_processing_conditional) and [%s](#lemma:reverse_data_processing_conditional),

:::{div}
:class: roman-list
1. That $f$ is both Lipschitz continuous and co-Lipschitz continuous implies:

   $$
   \begin{aligned}
   K_{r \mid s}(f(x) \mid y) &\leq K_{r + O(1) \mid s}(x \mid y) & [\text{Lemma~\ref{lemma:forward_data_processing_conditional}(i)}]\\
   &\leq K_{r \mid s}(x \mid y) & [\text{Lemma~\ref{lemma:linearity_with_condition}(i)}]\\
   &\leq K_{r + O(1)\mid s}(f(x) \mid y) & [\text{Lemma~\ref{lemma:reverse_data_processing_conditional}(i)}]\\
   &\leq K_{r \mid s}(f(x) \mid y) & [\text{Lemma~\ref{lemma:linearity_with_condition}(i)}].
   \end{aligned}
   $$

1. That $f$ is both Lipschitz continuous and co-Lipschitz continuous implies:

   $$
   \begin{aligned}
   K_{r \mid s}(x \mid f(y)) &\leq K_{r \mid s + O(1)}(x \mid f(y)) & [\text{Lemma~\ref{lemma:linearity_with_condition}(ii)}]\\
   &\leq K_{r \mid s}(x \mid y) & [\text{Lemma~\ref{lemma:reverse_data_processing_conditional}(ii)}]\\
   &\leq K_{r \mid s + O(1)}(x \mid y) & [\text{Lemma~\ref{lemma:linearity_with_condition}(ii)}]\\
   &\leq K_{r \mid s}(x \mid f(y)) & [\text{Lemma~\ref{lemma:forward_data_processing_conditional}(ii)}].
   \end{aligned}
   $$
:::
::::

By the properties of Hausdorff dimension, fractal geometry is considered to be the study of fractal properties invariant under the group of bi-Lipschitz continuous transformations {cite:p}`Kle93`. Given the previous result, we may say something similar for effectivized fractal geometry: we study fractal properties which are invariant under the group of bi-computable, bi-Lipschitz continuous transformations {cite:p}`Rei04`.
