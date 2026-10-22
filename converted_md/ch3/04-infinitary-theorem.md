---
title: "Infinitary Theorem"
label: section:Infinitary_Theorem
---

We leverage the finitary theorem [%s](#theorem:finitary) to prove the corresponding result about the effective dimension of points on the graph of a map in the family given by a CALF. The last component we require to do this is the oracle construction developed by N. Lutz and D. Stull in {cite:t}`LS16`.

::::{prf:lemma} Lemma 8 of {cite:t}`LS16`
:label: lemma:oracle_construction
Fix $m, r \in \omega$, $\mathbf{x} \in \mathbb{R}^m$, and rational $0 \leq \eta \leq \dim(\mathbf{x})$. Then there exists an oracle $X = X(\mathbf{x}, m, r, \eta)$ satisfying:

:::{div}
:class: roman-list
1. For each $k \leq r$,

   $$
   \begin{aligned}
   K^X_k(\mathbf{x}) = \min \seq{\eta r, K_k(\mathbf{x})} \pm O(\log r).
   \end{aligned}
   $$

1. For any $n, s \in \omega$ and $\mathbf{y} \in \mathbb{R}^n$,

   $$
   \begin{aligned}
   K^X_{s \mid r}(\mathbf{y} \mid \mathbf{x}) &= K_{s \mid r}(\mathbf{y} \mid \mathbf{x}) \pm O(\log r),\\
   K^{\mathbf{x}, X}_s(\mathbf{y}) &= K^{\mathbf{x}}_s(\mathbf{y}) \pm O(\log r).
   \end{aligned}
   $$
:::
::::

Part (i) of the construction claims $X$ can simplify the first $r$ many dyadic truncations of $\mathbf{x}$ to not exceed the limiting information density of $\mathbf{x}$, whereas part (ii) ensures that $X$ cannot meaningfully aid $\mathbf{x}$ in making computations.

:::{prf:theorem} Infinitary Lower Bound
:label: theorem:infinitary
Let $\Phi : \mathbb{R}^m \times \mathbb{R}^\ell \to \mathbb{R}^n$ be a CALF on domain $\Omega \times \Xi$. Then for every $\boldsymbol{\alpha} \in \Omega$, $x \in \Xi$, and $B \in 2^{\leq \omega}$,

$$
\begin{aligned}
\dim^B(x, \Phi^{\boldsymbol{\alpha}}(x)) \geq \dim^B(x | \boldsymbol{\alpha}) + \min \seq{\dim^B(\boldsymbol{\alpha}), \dim^{B, \boldsymbol{\alpha}}(x)}.
\end{aligned}
$$
:::

:::{prf:proof}
:nonumber:
The following argument may be relativized to an arbitrary oracle $B \in 2^{\leq \omega}$. Fix $\boldsymbol{\alpha} \in \Omega$ and $x \in \Xi$. The claim of the theorem is trivial when $\dim(x \mid \boldsymbol{\alpha}) = 0$ (in which case, by Lemma [%s](#oracle_access_to_conditional), $\dim^{\boldsymbol{\alpha}}(x) = 0$ as well). So consider the case of $\delta := \dim^{\boldsymbol{\alpha}}(x) > 0$, and let

$$
\begin{aligned}
d \in \mathbb{Q} \cap [0, \dim(\boldsymbol{\alpha})] \cap [0, \dim^{\boldsymbol{\alpha}}(x)).
\end{aligned}
$$

Clearly, $\delta > d$. Fix $r \gg 1$ sufficiently large so that $\restrict{\boldsymbol{\alpha}}{r} \in \Omega$ and $\restrict{x}{r} \in \Xi$. Let $X_r := X(\boldsymbol{\alpha}, m, r, d)$ be an oracle for $\boldsymbol{\alpha}$ at information density $d$ as guaranteed by Lemma [%s](#lemma:oracle_construction). We now check that we may apply Theorem [%s](#theorem:finitary) to $\restrict{\boldsymbol{\alpha}}{r}$ and $\restrict{x}{r}$ at precision-level $r$. Let $0 \leq k \leq r$. We skip writing $\restrict{(\restrict{\boldsymbol{\alpha}}{r})}{k} = \restrict{\boldsymbol{\alpha}}{k}$ and similar for $x$.

Then, the assumption (i) of Theorem [%s](#theorem:finitary) follows from Lemma [%s](#maxmin_truncation_for_r):

$$
\begin{aligned}
K(\restrict{\boldsymbol{\alpha}}{k}) = K_k(\boldsymbol{\alpha}) \pm o(k) \geq \dim(\boldsymbol{\alpha}) k - o(k) \geq dk - o(k).
\end{aligned}
$$

And the assumption (ii) similarly follows from Lemma [%s](#maxmin_truncation_for_r) relativized to $\boldsymbol{\alpha}$:

$$
\begin{aligned}
K^{\boldsymbol{\alpha}}(\restrict{x}{k}) = K^{\boldsymbol{\alpha}}_k(x) \pm o(k) \geq \dim^{\boldsymbol{\alpha}}(x) k - o(k) = \delta k - o(k).
\end{aligned}
$$

Therefore, we may apply Theorem [%s](#theorem:finitary) to $\restrict{\boldsymbol{\alpha}}{r}$ and $\restrict{x}{r}$. Note that if $\boldsymbol{\alpha}_r = \restrict{\boldsymbol{\alpha}}{r}$ and $x_r = \restrict{x}{r}$, then $K(\restrict{\Phi^{\boldsymbol{\alpha}}(x)}{r}) = K(\restrict{\Phi^{\boldsymbol{\alpha}_r}(x_r)}{r}) \pm o(r)$. This follows from $\Phi$ being scaling Lipschitz continuous. So,

$$
\begin{aligned}
\dim(x, \Phi^{\boldsymbol{\alpha}}(x)) &\geq \dim^{X_r}(x, \Phi^{\boldsymbol{\alpha}}(x))\\
&= \liminf_{r \to \infty} \frac{1}{r} K^{X_r}_r(x, \Phi^{\boldsymbol{\alpha}}(x))\\
&= \liminf_{r \to \infty} \frac{1}{r} K^{X_r}(\restrict{(x, \Phi^{\boldsymbol{\alpha}}(x))}{r}) & [\text{Lemma~\ref{maxmin_truncation_for_r} rel. to $X_r$}]\\
&= \liminf_{r \to \infty} \frac{1}{r} K^{X_r}(x_r, \restrict{\Phi^{\boldsymbol{\alpha}_r}(x_r)}{r}) & [\text{$\Phi$ is scaling Lipschitz}]\\
&\geq \liminf_{r \to \infty} \frac{1}{r} \brk{K^{X_r}(\boldsymbol{\alpha}_r, x_r) - m \cdot \frac{K^{X_r}(\boldsymbol{\alpha}_r) - dr}{\delta - d}} & \text{[Theorem~\ref{theorem:finitary} rel to $X_r$]}\\
&= \liminf_{r \to \infty} \frac{1}{r} \brk{K^{X_r}_r(\boldsymbol{\alpha}, x) - m \cdot \frac{K^{X_r}_r(\boldsymbol{\alpha}) - dr}{\delta - d}} & \text{[Lemma~\ref{maxmin_truncation_for_r} rel to $X_r$]}\\
&\geq \liminf_{r \to \infty} \frac{1}{r} K^{X_r}_r(\boldsymbol{\alpha}, x) & [\text{Lemma~\ref{lemma:oracle_construction}(i)}]\\
&\geq \liminf_{r \to \infty} \frac{1}{r} \brk{K^{X_r}_{r \mid r}(x \mid \boldsymbol{\alpha}) + K^{X_r}_r(\boldsymbol{\alpha})} & [\text{Theorem~\ref{theorem:approximate_SOI_conditional}}]\\
&= \liminf_{r \to \infty} \frac{1}{r} \brk{K_{r \mid r}(x \mid \boldsymbol{\alpha}) + dr} & [\text{Lemma~\ref{lemma:oracle_construction}(i),(ii)}]\\
&= \dim(x | \boldsymbol{\alpha}) + d.
\end{aligned}
$$

As $d$ was an arbitrary rational number in $[0, \dim(\boldsymbol{\alpha})] \cap [0, \dim^{\boldsymbol{\alpha}}(x))$, we conclude:

$$
\begin{aligned}
\dim(x, \Phi^{\boldsymbol{\alpha}}(x)) \geq \dim(x \mid \boldsymbol{\alpha}) + \min \seq{\dim(\boldsymbol{\alpha}), \dim^{\boldsymbol{\alpha}}(x)}.
\end{aligned}
$$
:::

Theorem [%s](#theorem:original_infinitary) follows as a consequence of Theorem [%s](#theorem:infinitary) as applied to the CALF $\Phi$ from Example [%s](#example:lines).
