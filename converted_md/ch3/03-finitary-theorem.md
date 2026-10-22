---
title: "Finitary Theorem"
label: section:Finitary_Theorem
---

The following geometric observation is known as the **Intersecting Tubes Lemma** in the case of planar lines: that the closer to perpendicular two intersecting lines are to one another, the more precisely one may describe their point of intersection. For us, that generalizes to a statement of the form: the more similar the co-Lipschitz parameters of two $\Phi$-curves are, the more precisely one may describe an input on which they approximately intersect.

:::{prf:observation} C.f. Observation A.5 in {cite:t}`LS16`
:label: observation:approximate_x_location_of_intersection
Take $\Phi : \mathbb{R}^m \times \mathbb{R}^\ell \to \mathbb{R}^n$ to be a CALF on domain $\Omega \times \Xi$. Fix $r \in \omega$, $x \in \Xi_r$, and $\boldsymbol{\alpha}, \boldsymbol{\beta} \in \Omega_r$ with $\Phi^{\boldsymbol{\alpha}} - \Phi^{\boldsymbol{\beta}}$ being scaling co-Lipschitz continuous. If $\norm{\Phi^{\boldsymbol{\alpha}}(x) - \Phi^{\boldsymbol{\beta}}(x)} \leq 2^{-r + O_n(1)}$, $k = S(\boldsymbol{\alpha}, \boldsymbol{\beta})$, and $r \geq k + O_{\norm{x}, n}(1)$, then there is an algorithm approximating $x$ to precision $2^{-r + k + O_{x, n}(1)}$ uniformly in $\boldsymbol{\alpha}$, $\boldsymbol{\beta}$, and $r$.
:::

:::{prf:proof}
:nonumber:
Whenever another $x' \in \Xi$ satisfies $\norm{\Phi^{\boldsymbol{\alpha}}(x') - \Phi^{\boldsymbol{\beta}}(x')} < 2^{-r + O_n(1)}$, then since $\Phi$ has co-Lipschitz continuous differences,

```{math}
:label: equation:close_outputs_close_x
\begin{aligned}
\norm{(\boldsymbol{\alpha} - \boldsymbol{\beta})_{\operatorname{cL}}} \cdot \norm{x - x'} &\leq O_{\norm{x}, \norm{x'}}(1) \cdot \norm{(\Phi^{\boldsymbol{\alpha}} - \Phi^{\boldsymbol{\beta}})(x) - (\Phi^{\boldsymbol{\alpha}} - \Phi^{\boldsymbol{\beta}})(x')}  \\
&\leq 2 \cdot O_{\norm{x}, \norm{x'}}(1) \cdot 2^{-r + O_n(1)}.
\end{aligned}
```

So, $\norm{x - x'} \leq 2^{-r + k + O_{\norm{x}, \norm{x'}, n}(1)}$. This informs our search: splitting $\mathbb{R}^\ell$ into cubes with side-length $2^{-r}$, we iterate through all dyadic rational $q \in \mathbb{D}^\ell_r$ and ask whether $\norm{\Phi^{\boldsymbol{\alpha}}(q) - \Phi^{\boldsymbol{\beta}}(q)} < 2^{-r + O_{\norm{q}, n}(1)}$. In light of ([%s](#equation:close_outputs_close_x)), the search must terminate on a test point $q \in B_{2^{-r + k + O_{\norm{x}, n}(1)}}(x)$.
:::

As a corollary to Observation [%s](#observation:approximate_x_location_of_intersection), we have the following fact for any two curves with parameters $\boldsymbol{\alpha}$ and $\boldsymbol{\beta}$ which approximately agree on some input $x$. Essentially, $\boldsymbol{\beta}$ can simultaneously describe the portion of the co-Lipschitz components of $\boldsymbol{\alpha}$ shared with $\boldsymbol{\beta}$ along with a complementary portion of the bits of $x$.

:::{prf:corollary} C.f. Lemma 7 in {cite:t}`LS16`
:label: corollary:lower_bound_simple_line_parameters
Take $\Phi : \mathbb{R}^m \times \mathbb{R}^\ell \to \mathbb{R}^n$ to be a CALF on domain $\Omega \times \Xi$. Fix $r \in \omega$, $x \in \Xi_r$, and $\boldsymbol{\alpha}, \boldsymbol{\beta} \in \Omega_r$ with $\Phi^{\boldsymbol{\alpha}} - \Phi^{\boldsymbol{\beta}}$ being scaling co-Lipschitz continuous. If $\norm{\Phi^{\boldsymbol{\alpha}}(x) - \Phi^{\boldsymbol{\beta}}(x)} \leq 2^{-r + O_n(1)}$ and $k = S(\boldsymbol{\alpha}, \boldsymbol{\beta})$, then for each $r \geq k + O_{\norm{x}, n}(1)$,

$$
\begin{aligned}
K(\boldsymbol{\beta}) \geq K(\restrict{\boldsymbol{\alpha}}{k}) + K(\restrict{x}{(r - k)} \mid \boldsymbol{\alpha}) - O_{\norm{\boldsymbol{\alpha}}, \norm{x}, n}(\log r).
\end{aligned}
$$
:::

:::{prf:proof}
:nonumber:
Suppose $r \geq k + O_{\norm{x}, n}(1)$ from Observation [%s](#observation:approximate_x_location_of_intersection). We perform symmetry of information [%s](#theorem:chain_rule_for_K) several times to confirm:

$$
\begin{aligned}
K(\boldsymbol{\beta}) &\geq K(\boldsymbol{\beta} \mid \boldsymbol{\alpha}) + \brk{K(\boldsymbol{\alpha}) - K(\boldsymbol{\alpha} \mid \boldsymbol{\beta})} - O(\log r)\\
&\geq K(\restrict{x}{(r - k)} \mid \boldsymbol{\alpha}) + \brk{K(\boldsymbol{\alpha}) - K(\boldsymbol{\alpha} \mid \restrict{\boldsymbol{\beta}}{k})} - O(\log r) & [\text{Observation~\ref{observation:approximate_x_location_of_intersection}}]\\
&\geq K(\restrict{x}{(r - k)} \mid \boldsymbol{\alpha}) + \brk{K(\boldsymbol{\alpha}) - K(\boldsymbol{\alpha} \mid \restrict{\boldsymbol{\alpha}}{k})} - O(\log r)\\
&= K(\restrict{x}{(r - k)} \mid \boldsymbol{\alpha}) + K(\restrict{\boldsymbol{\alpha}}{k}) - O(\log r).
\end{aligned}
$$
:::

::::{prf:theorem} Finitary Lower Bound
:label: theorem:finitary
Take $\Phi : \mathbb{R}^m \times \mathbb{R}^\ell \to \mathbb{R}^n$ to be a CALF on domain $\Omega \times \Xi$. Let $d < \delta \in [0, \ell]$, $r \in \omega$. Suppose $\boldsymbol{\alpha} \in \Omega_r$ and $x \in \Xi_r$ satisfy for each $k \leq r$,

:::{div}
:class: roman-list
1. $K(\restrict{\boldsymbol{\alpha}}{k}) \geq d k - o(k)$,
1. $K(\restrict{x}{k} \mid \boldsymbol{\alpha}) \geq \delta k - o(k)$.
:::

Then,

$$
\begin{aligned}
K(x, \Phi^{\boldsymbol{\alpha}}(x)) \geq K(\boldsymbol{\alpha}, x) - m \cdot \frac{K(\boldsymbol{\alpha}) - dr}{\delta - d} - o(r).
\end{aligned}
$$
::::

:::{prf:proof}
:nonumber:
Let $m$, $n$, $\ell$, $d$, $\delta$, $r$, $\boldsymbol{\alpha}$, and $x$ be as in the statement. Further denote by $y := \restrict{\Phi^{\boldsymbol{\alpha}}(x)}{r} \in \mathbb{D}^n_r$ the level-$r$ approximation to the output of $\Phi^{\boldsymbol{\alpha}}$ at $x$. Since $\Phi$ has density of intersections, we may fix $\boldsymbol{\beta} \in \Omega_r$ such that $\Phi^{\boldsymbol{\alpha}} - \Phi^{\boldsymbol{\beta}}$ is scaling co-Lipschitz continuous, $\norm{\boldsymbol{\alpha} - \boldsymbol{\beta}} \leq 2^{-r + O_{\norm{\boldsymbol{\alpha}}, \norm{x}, m, n}(1)}$, and $S(\boldsymbol{\alpha}, \boldsymbol{\beta}) \leq r - O_{\norm{\boldsymbol{\alpha}}, \norm{x}, m, n}(1)$. And since $\Phi$ is scaling Lipschitz continuous, this implies that the outputs $\Phi^{\boldsymbol{\alpha}}(x)$ and $\Phi^{\boldsymbol{\beta}}(x)$ agree to a similar precision:

$$
\begin{aligned}
\norm{\Phi^{\boldsymbol{\alpha}}(x) - \Phi^{\boldsymbol{\beta}}(x)} \leq O(\norm{\boldsymbol{\alpha}} + \abs{x} + 1) \cdot \norm{\boldsymbol{\alpha} - \boldsymbol{\beta}} \leq 2^{-r + \gamma},
\end{aligned}
$$

where $\gamma = 2^{O_{\norm{\boldsymbol{\alpha}}, \norm{x}, m, n}(1)}$.

Furthermore, by the density of intersections assumption, we see:

```{math}
:label: equation:u_v_x_computed
\begin{aligned}
K(\restrict{(\boldsymbol{\beta}, x)}{(r - \gamma)}) \leq K(x, y) + K_1(\boldsymbol{\alpha}) + K(r) + K(m, n, \ell) + O(1).
\end{aligned}
```

Let $k = S(\boldsymbol{\alpha}, \boldsymbol{\beta})$ and recall $r \geq k + O_{\norm{\boldsymbol{\alpha}}, \norm{x}, m, n}(1)$. Since $\boldsymbol{\alpha}$ can approximately compute $\boldsymbol{\beta}$, we deduce the following numerical condition:

$$
\begin{aligned}
K(\boldsymbol{\alpha}) &\geq K(\restrict{\boldsymbol{\beta}}{(r - \gamma)}) - o(r) & [\boldsymbol{\beta} \in B_{2^{\gamma - r}}(\boldsymbol{\alpha})]\\
&\geq K(\boldsymbol{\beta}) - o(r) & [\text{$\gamma = O_{\norm{\boldsymbol{\alpha}}, \norm{x}, m, n}(1)$}]\\
&\geq K(\restrict{\boldsymbol{\alpha}}{k}) + K(\restrict{x}{(r - k)} \mid \boldsymbol{\alpha}) - o(r) & [\text{Corollary~\ref{corollary:lower_bound_simple_line_parameters}}]\\
&\geq dk + \delta (r - k) - o(r) & [\text{Assumptions (i) \& (ii)}]\\
&= dr + (\delta - d) (r - k) - o(r),
\end{aligned}
$$

We rearrange to see:

```{math}
:label: equation:inequality_r_minus_k
\begin{aligned}
r - k \leq \frac{K(\boldsymbol{\alpha}) - dr}{\delta - d} + o(r),
\end{aligned}
```

which is well-defined as $\delta > d$. Notice by assumption that $B_{2^{-r}}(\boldsymbol{\beta}) \subseteq B_{2^{-k + o(r)}}(\boldsymbol{\alpha})$. We use this fact and the Chain Rule [%s](#theorem:chain_rule_for_K) to conclude:

$$
\begin{aligned}
K(x, y) &\geq K(\boldsymbol{\beta}, x) - o(r) & [\text{(\ref{equation:u_v_x_computed})}]\\
&\geq K(\restrict{\boldsymbol{\alpha}}{k}, x) - o(r)\\
&= K(\restrict{\boldsymbol{\alpha}}{k} \mid x) + K(x) - o(r)\\
&\geq K(\boldsymbol{\alpha} \mid x) - m \cdot (r - k) + K(x) - o(r)\\
&\geq K(\boldsymbol{\alpha}, x) - m \cdot \frac{K(\boldsymbol{\alpha}) - dr}{\delta - d} - o(r). & [(\ref{equation:inequality_r_minus_k})]
\end{aligned}
$$
:::
