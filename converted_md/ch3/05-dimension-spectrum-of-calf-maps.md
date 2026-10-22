---
title: "Dimension Spectrum of CALF Maps"
---

According to Theorem [%s](#theorem:original_infinitary), if $\Phi^{\boldsymbol{\alpha}}$ is a map from a CALF, then points $(x, \Phi^{\boldsymbol{\alpha}}(x))$ on its graph are at least somewhat complex. Our goal in this section is to understand the effective dimension of these points as a distribution: e.g., can the lower bound in Theorem [%s](#theorem:original_infinitary) be exact for most points along $\Phi^{\boldsymbol{\alpha}}$? The following results are direct generalizations of those from Section 4 of {cite:t}`Stu18`. For the remainder of the section, we fix a CALF $\Phi: \mathbb{R}^m \times \mathbb{R}^\ell \to \mathbb{R}^n$ on a domain $\Omega \times \Xi$.

The first result is an observation that directly follows from the approximate chain rule [%s](#theorem:approximate_SOI_conditional) and the density of intersections of $\Phi$.

:::{prf:observation}
:label: observation:computing_alpha_x_x'
For each $\boldsymbol{\alpha} \in \Omega$ and $x_1, x_2 \in \Xi$,

$$
\begin{aligned}
K_r(\boldsymbol{\alpha}) &+ K_r(x_1 \mid \boldsymbol{\alpha}) + K_r(x_2 \mid \boldsymbol{\alpha}, x_1) - O(\log r) \\
&\leq K_r(\boldsymbol{\alpha}, x_1, x_2) \\
&\leq K_r(x_1, \Phi^{\boldsymbol{\alpha}}(x_1)) + K_r(x_2, \Phi^{\boldsymbol{\alpha}}(x_2)) + O_{\norm{x_1}, \norm{x_2}}(1) + 2 \log \norm{x_1 - x_2}.
\end{aligned}
$$
:::

The final upper bound in Observation [%s](#observation:computing_alpha_x_x') involves two separate complexity terms which are not guaranteed to achieve their limiting lower densities at the same precision-levels, preventing us from immediately concluding a result relating the effective dimension of these objects. Yet, we may characterize the size of the set of instances when $K_r(x_1, \Phi^{\boldsymbol{\alpha}}(x_1))$ and $K_r(x_2, \Phi^{\boldsymbol{\alpha}}(x_2))$ are simultaneously minimal.

:::{prf:lemma}
:label: lemma:simultaneously_minimal_complexities
Let $\delta \in (0, \ell)$, $\boldsymbol{\alpha} \in \Omega$, $x_1 \in \Xi$, and $n, r \in \omega$ be such that $\frac{2}{\sqrt{r}} < \frac{1}{n}$. Assume that

$$
\begin{aligned}
\delta \cdot r \leq K_r^{\boldsymbol{\alpha}}(x_1, \Phi^{\boldsymbol{\alpha}}(x_1)), \quad \text{and} \quad K_r(x_1, \Phi^{\boldsymbol{\alpha}}(x_1)) &\leq \delta \cdot r + \frac{K_r(\boldsymbol{\alpha})}{2} - \frac{r}{n}.
\end{aligned}
$$

Then, for any other $x_2 \in \Xi$ satisfying $K_r(x_2, \Phi^{\boldsymbol{\alpha}}(x_2)) < \delta \cdot r + \frac{K_r(\boldsymbol{\alpha})}{2}$, it holds that either

$$
\begin{aligned}
- \log \norm{x_1 - x_2} \leq \sqrt{r} + O_{\norm{x_1}, \norm{x_2}}(1) + O(\log r), \quad \text{or} \quad K_r(x_2 \mid \boldsymbol{\alpha}, x_1) < \delta \cdot r.
\end{aligned}
$$
:::

In words, the following holds for all sufficiently large precision-levels. We suppose $x_1$ is sufficiently complex with respect to $\alpha$, while the pair $(x_1, \Phi^{\boldsymbol{\alpha}}(x_1))$ is not much more complex. Then, for any other input $x_2$ with a simple $(x_2, \Phi^{\boldsymbol{\alpha}}(x_2))$, either $x_2$ is sufficiently far from $x_1$, or $x_2$ is simple to describe from $\boldsymbol{\alpha}$ and $x_1$.

:::{prf:proof}
:nonumber:
Suppose the hypothesis holds but that neither condition is satisfied for some $x_2 \in \Xi$. Then by Observation [%s](#observation:computing_alpha_x_x'),

$$
\begin{aligned}
K_r(\boldsymbol{\alpha}) &+ 2 \delta r - O(\log r)
\\
&\leq
K_r(\boldsymbol{\alpha}) + K_r(x_1 \mid \boldsymbol{\alpha}) + K_r(x_2 \mid \boldsymbol{\alpha}, x_1) - O(\log r)\\
&\leq K_r(x_1, \Phi^{\boldsymbol{\alpha}}(x_1)) + K_r(x_2, \Phi^{\boldsymbol{\alpha}}(x_2)) + O_{\norm{x_1}, \norm{x_2}}(1) + 2 \log \norm{x_1 - x_2}\\
&< \brk{\delta r + \frac{K_r(\boldsymbol{\alpha})}{2} - \frac{r}{n}} + \brk{\delta r + \frac{K_r(\boldsymbol{\alpha})}{2}} + O_{\norm{x_1}, \norm{x_2}}(1) + 2 \log \norm{x_1 - x_2}.
\end{aligned}
$$

Since the first condition on $x_2$ fails, we deduce $\frac{1}{n} < \frac{2}{\sqrt{r}}$, a contradiction.
:::

Given $\delta \in (0, \ell)$, denote by

$$
\begin{aligned}
D^{\boldsymbol{\alpha}}(\delta) := \set{x \in \Xi}{\dim(x, \Phi^{\boldsymbol{\alpha}}(x)) < \delta + \frac{\dim(\boldsymbol{\alpha})}{2}}
\end{aligned}
$$

the set of inputs which map to the point $(x, \Phi^{\boldsymbol{\alpha}}(x))$ having effective dimension less than $\delta + \dim(\boldsymbol{\alpha}) / 2$. Now, we may state the main result for the dimension spectrum of $\Phi^{\boldsymbol{\alpha}}$.

:::{prf:theorem}
:label: theorem:dimension_spectrum_of_a_CALF
For every $\boldsymbol{\alpha} \in \Omega$ and $\delta \in (0, \ell)$, we have $\dim_{\operatorname{H}}(D^{\boldsymbol{\alpha}}(\delta)) \leq \delta$.
:::

That is, very few points along the graph of $\Phi^{\boldsymbol{\alpha}}$ may be of small effective dimension, and almost every input $x$ produces a point $(x, \Phi^{\boldsymbol{\alpha}}(x))$ of effective dimension at least $\ell$.

:::{prf:proof}
:nonumber:
Fix $\boldsymbol{\alpha} \in \Omega$ and $\delta \in (0, \ell)$. Really, we work with the sets:

$$
\begin{aligned}
D^{\boldsymbol{\alpha}}_n(\delta) := \set{x \in \Xi}{(\exists^\infty r \in \omega) \brk{K_r(x, \Phi^{\boldsymbol{\alpha}}(x)) < \delta \cdot r + \frac{K_r(\boldsymbol{\alpha})}{2} - \frac{r}{n}}},
\end{aligned}
$$

which cover $D^{\boldsymbol{\alpha}}(\delta)$, since if $x \in D^{\boldsymbol{\alpha}}(\delta)$ and $\varepsilon > 0$, there will exist infinitely many $r \in \omega$ for which

$$
\begin{aligned}
K_r(x, \Phi^{\boldsymbol{\alpha}}(x)) < \delta \cdot r + \frac{\dim(\boldsymbol{\alpha})}{2}  \cdot r - \varepsilon \cdot r < \delta \cdot r + \frac{K_r(\boldsymbol{\alpha}) + o(r)}{2} - \varepsilon \cdot r,
\end{aligned}
$$

meaning for sufficiently large values of $n \in \omega$, we have $x \in D^{\boldsymbol{\alpha}}_n(\delta)$. Therefore, by the countable stability of Hausdorff dimension, it suffices to show that $\dim_{\operatorname{H}}(D^{\boldsymbol{\alpha}}_n(\delta)) \leq \delta$ for all $n \in \omega$.

To begin, for each $r \in \omega$, fix a point $x_r \in \Xi$, if it exists, satisfying the hypotheses of Lemma [%s](#lemma:simultaneously_minimal_complexities), i.e.,

$$
\begin{aligned}
\delta \cdot r \leq K_r^{\boldsymbol{\alpha}}(x_r, \Phi^{\boldsymbol{\alpha}}(x_r)), \quad \text{and} \quad K_r(x_r, \Phi^{\boldsymbol{\alpha}}(x_r)) &\leq \delta \cdot r + \frac{K_r(\boldsymbol{\alpha})}{2} - \frac{r}{n}.
\end{aligned}
$$

And let $B \in 2^{\leq\omega}$ be an oracle encoding all the $(x_r)_{r \in \omega}$ which exist. We now consider three cases for a fixed $x \in D^{\boldsymbol{\alpha}}_n(\delta)$.

Suppose first that $K^{\boldsymbol{\alpha}}_r(x) \leq \delta \cdot r$ for infinitely many $r \in \omega$. Then, clearly, $\dim^{\boldsymbol{\alpha}}(x) \leq \delta$.

Otherwise, if $\norm{x - x_r} < 2^{-\sqrt{r} + O(\log r) + O(1)}$ for infinitely many $r \in \omega$, then for each such $r$,

$$
\begin{aligned}
K^B_{\sqrt{r}}(x') \leq O(\log r) + O(1) = O(\log \sqrt{r}),
\end{aligned}
$$

implying $\dim^B(x) = 0$.

Finally, if neither condition holds, take any one of the infinitely many $r \in \omega$ for which

$$
\begin{aligned}
K_r(x, \Phi^{\boldsymbol{\alpha}}(x)) < \delta r + \frac{K_r(\boldsymbol{\alpha})}{2} - \frac{r}{n}.
\end{aligned}
$$

Then, by Lemma [%s](#lemma:simultaneously_minimal_complexities), it must be that $K_r(x \mid \boldsymbol{\alpha}, x_r) < \delta \cdot r$, meaning $\dim^{B, \boldsymbol{\alpha}}(x) \leq \delta$. In any case, the Point-to-Set Principle [%s](#theorem:PTS_for_H_dimension) implies $\dim_{\operatorname{H}}(D^{\boldsymbol{\alpha}}_n(\delta)) \leq \delta$, as desired.
:::
