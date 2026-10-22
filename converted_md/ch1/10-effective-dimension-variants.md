---
title: "Effective Dimension Variants"
label: section:Conditional_and_Mutual_Dimensions
---

We review two variants of effective dimension.

## Mutual Dimension

One variant of effective dimension is **mutual dimension**, which was originally defined in {cite:t}`CL14`. It intuitively captures the algorithmic information shared by two infinitary objects in the limit. In Shannon information theory, mutual information is a measure of the correlation between two distributions. A. Case and J. Lutz's algorithmic notion of mutual information serves as a refinement of the classical notion. Namely, the **(conditional) mutual information between two finitary objects $a, b \in \mathscr{N}$ given $c \in \mathscr{N}$** is

$$
\begin{aligned}
I(a : b \mid c) := K(a \mid c) - K(a \mid b, c).
\end{aligned}
$$

Extending their notation slightly, we define the **mutual information between subsets $X \subseteq \mathbb{R}^m$ and $Y \subseteq \mathbb{R}^n$** as:

$$
\begin{aligned}
I(X : Y) := \min \set{I(p : q)}{p \in X \cap \mathbb{Q}^m \text{ and } q \in Y \cap \mathbb{Q}^n},
\end{aligned}
$$

or zero if taken over the empty set. Then the **mutual information between $x \in \mathbb{R}^m$ to precision-level $r$ and $y \in \mathbb{R}^n$ to precision-level $s$** is defined as:

$$
\begin{aligned}
I_{r : s}(x : y) := I(B_{2^{-r}}(x) : B_{2^{-s}}(x)),
\end{aligned}
$$

Both $I$ and $I_{r : s}$ inherit many of their expected properties such as a chain rule and symmetry from $K$ and $K_{r \mid s}$. In particular, a slight generalization to Theorem 4.10 in {cite:t}`CL14` for distinct precision-levels proves the chain rule for $I_{r : s}$.

:::{prf:theorem} Chain Rule for Mutual Information, c.f. Theorem 4.10 of {cite:t}`CL14`
:label: theorem:chain_rule_mutual_information_r_s
For all $x \in \mathbb{R}^m$, $y \in \mathbb{R}^n$, and $r, s \in \omega$,

$$
\begin{aligned}
I_{r : s}(x : y) &= K_r(x) + K_s(y) - K_{r, s}(x, y) \pm (o(r) + o(s))\\
&= K_r(x) + K_{s \mid r}(y \mid x) \pm (o(r) + o(s)).
\end{aligned}
$$
:::

Case and Lutz further defined the **lower and upper mutual dimensions of $x \in \mathbb{R}^m$ and $y \in \mathbb{R}^n$** as follows:

$$
\begin{aligned}
\operatorname{mdim}(x : y) := \liminf_{r \to \infty} \frac{I_{r : r}(x : y)}{r}, \quad \text{and} \quad \operatorname{Mdim}(x : y) := \limsup_{r \to \infty} \frac{I_{r : r}(x : y)}{r}.
\end{aligned}
$$

Both mutual dimensions possess a few special properties. For instance, if $x \in \mathbb{R}^m$ and $y \in \mathbb{R}^n$, then $0 \leq \operatorname{mdim}(x : y) \leq \min \seq{\operatorname{mdim}(x), \operatorname{mdim}(y)}$. As well as symmetry: $\operatorname{mdim}(x : y) = \operatorname{mdim}(y : x)$. Analogous statements hold for $\operatorname{Mdim}$.

## Conditional Dimension

A conditional version of effective dimension was first defined in {cite:t}`LL18` using the lifted conditional prefix complexity $K_{r \mid s}$. The **lower and upper conditional dimensions of $x \in \mathbb{R}^m$ given $y \in \mathbb{R}^n$** were defined as:

$$
\begin{aligned}
\dim(x \mid y) = \liminf_{r \to \infty} \frac{K_{r \mid r}(x \mid y)}{r}, \quad \text{and} \quad \operatorname{Dim}(x \mid y) = \limsup_{r \to \infty} \frac{K_{r \mid r}(x \mid y)}{r}.
\end{aligned}
$$

Conditional dimension may equivalently be characterized in terms of semimeasures and supergales as in Theorem [%s](#theorem:asymptotic_coincidences_Cantor).

These conditional dimensions were shown to relate with the weak and strong effective dimensions as follows:

:::{prf:theorem} Chain Rule for Conditional Dimension; Corollary 13 of {cite:t}`LL18`
$$
\begin{aligned}
\dim(x) + \dim(y \mid x) \leq \dim(x, y) &\leq \dim(x) + \operatorname{Dim}(y \mid x) \leq \operatorname{Dim}(x, y) \leq \operatorname{Dim}(x) + \operatorname{Dim}(y \mid x).
\end{aligned}
$$
:::

## Results on Mutual and Conditional Dimensions

Both mutual dimensions behave predictably under computable, uniformly-continuous maps. We cite here just one corollary of this robustness.

:::{prf:theorem} Preservation of Mutual Dimension; Corollary 8.3 of {cite:t}`CL14`
:label: theorem:mutual_dimension_invariant_under_computable_bi_Lipshictz
If $f : \mathbb{R}^m \to \mathbb{R}^k$ and $g : \mathbb{R}^n \to \mathbb{R}^\ell$ are computable and bi-Lipschitz, then for all $x \in \mathbb{R}^m$ and $\mathbb{R}^n$,

$$
\begin{aligned}
\operatorname{mdim}(f(x) : g(y)) &= \operatorname{mdim}(x : y),\\
\operatorname{Mdim}(f(x) : g(y)) &= \operatorname{Mdim}(x : y).
\end{aligned}
$$
:::

In his dissertation {cite:p}`Rei04`, J. Reimann argues why effective dimension is also preserved under bi-computable, (locally) bi-Lipschitz continuous maps. This fact was used by N. Lutz to confirm an analog of Marstrand's Projection Theorem for the effective dimension of points {cite:p}`Lut17`. Results like these mimic the preservation of Hausdorff dimension under locally bi-Lipschitz continuous maps (e.g., Corollary 2.4 in {cite:t}`Fal90`). We will expand on this later in Section [%s](#section:Effective_Dimension_under_Uniformly_Continuous_Maps).

Finally, we summarize the known relations between mutual, conditional, and effective dimensions.

:::{prf:proposition}
:label: proposition:relating_mutual_dimension_and_conditional_dimension
For all $x \in \mathbb{R}^m$ and $y \in \mathbb{R}^n$,

$$
\begin{aligned}
\dim(x \mid y) & \leq \operatorname{dim}(x) - \operatorname{mdim}(x : y) \leq \operatorname{Dim}(x \mid y),\\
\dim(x \mid y) & \leq \operatorname{Dim}(x) - \operatorname{Mdim}(x : y) \leq \operatorname{Dim}(x \mid y).
\end{aligned}
$$
:::

We note that two of these inequalities were already proved in Corollary 11 of {cite:t}`LL18`. Our contribution is to add the uppermost bound in the top line, and the lowermost bound in the bottom line. All of these inequalities follow by re-expressing mutual dimension using the chain rules for $I_{r : r}$ and $K_{r \mid r}$ as in Theorems [%s](#theorem:chain_rule_mutual_information_r_s) and [%s](#theorem:approximate_SOI_conditional), respectively, and then distributing the limits inferior or superior appropriately over those terms.
