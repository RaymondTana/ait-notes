---
title: "Conditional, Mutual Dimension"
---

In Section [%s](#section:Conditional_and_Mutual_Dimensions), we reviewed two variants of effective dimension: **mutual** and **conditional** dimensions. Notice that for finitary objects, it was indeed possible to define a **conditional, mutual information** of the form $I(a : b \mid c)$: this intuitively measures the information content of the pair of objects $a$ and $b$ when given the data $c$. But mutual dimension is only defined in the unconditional sense. Can a useful notion of conditional, mutual dimension be defined? If $m, n, \ell \in \omega$, $x \in \mathbb{R}^m$, $y \in \mathbb{R}^n$, $z \in \mathbb{R}^\ell$, and $r, s, t \in \omega$, then one reasonable candidate definition would be:

$$
\begin{aligned}
\operatorname{mdim}(x : y \mid z) &:= \liminf_{r \to \infty} \frac{I_{r : r \mid r}(x : y \mid z)}{r}, \quad \quad I_{r : s \mid t}(x : y | z) := \min_u \seq{\min_{p, q} \seq{I(p : q \mid u)}},
\end{aligned}
$$

where the choices from $p$, $q$, and $u$ range in: $p \in B_{2^{-r}}(x) \cap \mathbb{Q}^m$, $q \in B_{2^{-s}}(y) \cap \mathbb{Q}^n$, and $u \in B_{2^{-t}}(z) \cap \mathbb{Q}^\ell$. The definition for $I_{r : s \mid t}$ is analogous to that of the conditional prefix complexity $K_{r \mid s}$.

Recall that conditional complexity admits an approximation by $K$-minimizers. That is, $K_{r \mid s}(x \mid y) \approx K(p^* \mid q^*)$, where $p^*$ and $q^*$ are $K$-minimizers of the balls $B_{2^{-r}}(x)$ and $B_{2^{-s}}(y)$, respectively (see Proposition [%s](#lemma:conditional_K_minimizers_suffice)). But in the case of conditional, mutual information, there is not as clear of a path towards showing the analogous statement: $I_{r : s \mid t}(x : y \mid z) \stackrel{?}{\approx} I(p^* : q^* \mid w^*)$, where each $p^*, q^*$, and $w^*$ are $K$-minimizers of the appropriate balls about $x$, $y$, and $z$, respectively. To be specific, while a quick calculation shows the approximate inequality $I_{r : s \mid t}(x : y \mid z) \geq I(p^* : q^* \mid w^*)$ in one direction, we are missing a proof of the reverse direction. The main issue is the lack of known results analogous to the linear sensitivities of conditional complexity: Lemmas [%s](#minmax_linear_sensitivity_in_s) and [%s](#minmax_linear_sensitivity_in_r).

If the approximation to $I_{r : s \mid t}$ by $K$-minimizers does hold up to logarithmic terms, then an analogous result to Theorem [%s](#theorem:SOI_conditional_complexity_r_s_t) should follow for mutual information, and one could go on to define a **conditional, mutual dimension** and compare it to the other variants to effective dimension.
