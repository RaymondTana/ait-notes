---
title: "Background"
---

It is an interesting and difficult problem to describe how effective Hausdorff dimension behaves as a function over Euclidean space. One approach towards a partial characterization involves tracking the effective dimension along function graphs. For instance, given a function $f : \mathbb{R} \to \mathbb{R}$, we ask how $\dim(x, f(x))$ might relate to $\dim(x)$ and $f$? If $f$ is both computable and Lipschitz continuous, Lemma [%s](#lemma:forward_data_processing_conditional)(i) implies $\dim(x, f(x)) = \dim(x)$. But when $f$ is not computable nor Lipschitz continuous, showing a relation is more difficult. It may be that $f$ is parameterized by some real tuple $\boldsymbol{\alpha}$ and computable as a map given $\boldsymbol{\alpha}$ as an oracle. What sort of uniform continuity properties should $f$ possess in order to relate $\dim(x, f(x))$ back to the dimensions of $x$ and the parameters in $\boldsymbol{\alpha}$?

The following theorem was originally proved in 2017 by N. Lutz and D. Stull {cite:p}`LS16`. It states that the effective dimension of a point on a line in the Euclidean plane may be bounded from below by a sum of terms depending on the effective dimensions of the input, slope, and intercept.

:::{prf:theorem} Theorem 1 in {cite:t}`LS16`
:label: theorem:original_infinitary
For every $a, b, x \in \mathbb{R}$ and $B \in 2^{\leq \omega}$,

```{math}
:label: equation:original_lower_bound_result
\begin{aligned}
\dim^B(x, ax + b) \geq \dim^B(x | a, b) + \min \seq{\dim^B(a, b), \dim^{B, a, b}(x)}.
\end{aligned}
```

In particular, for almost every $x \in \mathbb{R}$, $\dim(x, ax + b) = 1 + \min \seq{\dim(a, b), 1}$.
:::

This is the prototypical example for relating $\dim(x, f(x))$ to the dimensions of $x$ and the parameterization of $f$. Lutz and Stull employed prefix Kolmogorov complexity to prove this result. And as a consequence, they achieved a better lower bound on the classical Hausdorff dimension of generalized sets of Furstenberg type than were known at the time (see Theorem 4.3 of {cite:t}`LS16`). The bound follows from an application of the Point-to-Set Principle [%s](#theorem:PTS_for_H_dimension).

The original proof method for Theorem [%s](#theorem:original_infinitary) might be described as following a sequence of three lemmas:

- **Inverse Lemma**: Lower-bounding the complexity of a point found in the intersection of many sufficiently complex tubes.
- **Enumeration Lemma**: Lower-bounding the complexity of tubes passing through a fixed point.
- **Oracle Construction**: Building an oracle with knowledge about a fixed tube passing through a fixed point, and not much more.

A simplified proof of Theorem [%s](#theorem:original_infinitary) might first attempt to “frontload” the Kolmogorov complexity methods to achieve a **finitary** theorem on finite binary strings. Then, one could pass to the limit-inferior and obtain an **infinitary** theorem about effective dimensions. This sort of separation of effective methods from the approximation step is made possible by the results covered in Section [%s](#section:Robustness_of_the_Lift). Initially, A. Case and J. Lutz proved prefix complexity could be approximated by $K$-minimizers: see Lemma 4.9 of {cite:t}`CL14`. We confirmed this for conditional complexity as well in Lemma [%s](#lemma:conditional_K_minimizers_suffice). Together, N. Lutz and D. Stull showed that conditional complexity is also approximated by dyadic truncations: see Lemma A.1 ([%s](#maxmin_truncation_for_r)) and Lemma A.3 ([%s](#maxmin_truncation_for_r_s)) of {cite:t}`LS16`.

A finitary result is not totally straightforward. The following example by Alexander Shen makes this apparent. Let us call two finitary objects $u$ and $v$ to be **independently random** if:

$$
\begin{aligned}
K(u, v) = K(u) + K(v) = \operatorname{len}(u) + \operatorname{len}(v),
\end{aligned}
$$

where each equality holds up to logarithmic terms in the lengths of $u$ and $v$.

:::{prf:example}
Fix $r \in \omega$ and the $r$-dyadic reals $a, b, x \in \mathbb{D}_r$ as follows. Take,

$$
\begin{aligned}
a = 0.\underbrace{0\cdots 0}_{\frac{r}{2} \text{-many}} \bar{a}_{\text{rand}}, \quad \text{and} \quad b = 0.\underbrace{0\cdots 0}_{\frac{r}{2} \text{-many}} \bar{b}_{\text{rand}},
\end{aligned}
$$

where the binary strings $\bar{a}_{\text{rand}}, \bar{b}_{\text{rand}} \in 2^{\floor{r / 2}}$ are independently random. And select $x$ to be independently random with respect to the pair $\ang{a, b}$.

It remains to see whether $a$, $b$, and $x$ satisfy a finitary version of ([%s](#equation:original_lower_bound_result)). Denote by $y = \restrict{(ax + b)}{r}$. We ask whether

```{math}
:label: equation:natural_hope_lower_bound_result
\begin{aligned}
K(x, y) \stackrel{?}{\geq} K(x \mid a, b) + \min \seq{K(a, b), K(x \mid a, b)}.
\end{aligned}
```

Note that $K(y) \leq \frac{r}{2}$ holds up to logarithmic terms in $r$, for the first approximately $\frac{r}{2}$-bits in the binary expansion of $y$ will be zero. Again dropping any logarithmic terms in $r$, we may calculate:

$$
\begin{aligned}
K(x, y) \leq K(x) + K(y) \leq r + \frac{r}{2} &= \frac{3r}{2}\\
&< 2r = r + r = K(x \mid a, b) + \min \seq{K(a, b), K(x \mid a, b)}.
\end{aligned}
$$

So, ([%s](#equation:natural_hope_lower_bound_result)) fails for such a choice of $a$, $b$, and $x$ for large enough $r$.
:::

This example illustrates the main issue in obtaining a finitary theorem from which to derive Theorem [%s](#theorem:original_infinitary): the line's parameters (or input) may not consistently achieve high complexity across their truncations, possibly producing too simple of an output. Theorem [%s](#theorem:finitary) below only applies to finitary parameters and inputs whose truncations grow at least as fast as some consistent rate.

We further consider the continuity and algorithmic properties of the family of planar lines which make Theorem [%s](#theorem:original_infinitary) possible. Any planar line $f$ may be represented in slope-intercept form: $f(x) = ax + b$, meaning the finite tuple $(a, b) \in \mathbb{R}^2$ serves as a parameterization of $f$ under slope-intercept form. Let $(u, v)$ be the slope-intercept representation of another planar line $g$. The first geometric property is referred to as the **Intersecting Tubes Lemma**, which approximately states that whenever $f(x) = g(x)$ yet $a \neq u$, one may approximate $x$ by the quantity $\frac{b - v}{u - a}$ up to a precision that improves as $a$ and $u$ become more orthogonal as slopes. This could be seen as a consequence of linear functions being co-Lipschitz continuous. Second, when represented in slope-intercept form, the function $f$ is nothing more than the composition of a single multiplication followed by a single addition on some input: $f(x) = ax + b$. Lines thereby have the following property: one may use rational approximations to $a$, $b$, and $x$ to compute a similarly precise approximation to the output, $f(x)$. This property is a bit weaker than Lipschitz continuity for $f$, since the precision to which we can approximate $f(x)$ will also depend (linearly) on the sizes of $\abs{a}$ and $\abs{x}$. We investigate whether any function family which is sufficiently Lipschitz and co-Lipschitz continuous as above should also admit a lower bound result of the same form as in Theorem [%s](#theorem:original_infinitary).
