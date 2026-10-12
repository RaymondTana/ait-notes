---
title: "1.8 Semimeasures"
label: section:Semimeasures
---

This section presents an alternative approach to measuring the information-content or algorithmic-complexity of finitary objects through mass distribution.

## 1.8.1 Discrete Semimeasures

A function $m: 2^{<\omega} \to [0, 1]$ is said to be a *discrete semimeasure* on $2^\omega$ if it satisfies $\sum_{\sigma \in 2^{<\omega}} m(i) \leq 1$. There exists a (reference) *optimal* lower-semicomputable discrete semimeasure $\mathbf{m}$ on $2^\omega$. That is, if $m$ is any other lower-semicomputable discrete semimeasure, there exists a constant $\beta > 0$ such that for all $\sigma \in 2^{<\omega}$, we have $\mathbf{m}(\sigma) \geq \beta \cdot m(\sigma)$. Refer to Section 4.3 of {cite:t}`LV08` for more details.

There is a natural connection between prefix complexity and lower-semicomputable discrete semimeasures. Levin originally introduced the concept of an *information content measure*, or an upper-semicomputable, partial function $F : \subseteq 2^{<\omega} \to \omega$ satisfying $\sum_{\sigma \in 2^{<\omega}} 2^{-F(\sigma)} \leq 1$, as described in {cite:t}`DH10`. By the Kraft Inequality ([1.6.4](#theorem:kraft_inequality)) and the universality of $\mathbf{U}_{\operatorname{PF}}$, $K$ is considered to be minimal among the the information content measures. Similarly, $2^{-K(\cdot)}$ is maximal (i.e., optimal) among the lower-semicomputable discrete semimeasures.

This relationship is made more precise in *Levin's Coding Theorem*. We start by reviewing two classes of lower-semicomputable discrete semimeasures on $2^{<\omega}$.

:::{prf:definition}
:label: theorem-1-8-1
:enumerator: 1.8.1
Fix an oracle machine $M$ on $2^{<\omega}$, and $\sigma \in 2^{<\omega}$.

- Let $R_M(\sigma) := 2^{-C_M(\sigma)}$ denote the *algorithmic probability* of $\sigma$ under $M$.
- Let $Q_M(\sigma) := \sum_{M(\pi) \downarrow = \sigma} 2^{- \operatorname{len}(\pi)}$ denote the *a priori probability* of $\sigma$ under $M$.

When $M$ is the reference universal PF oracle machine, simply write $R \equiv R_{\mathbf{U}_{\operatorname{PF}}}$ and $T \equiv T_{\mathbf{U}_{\operatorname{PF}}}$.
:::

Levin proved that $\mathbf{m}$, $R$, and $Q$ all capture essentially the same quantity.

:::{prf:theorem} Levin's Coding Theorem, Theorem 3.9.4 of {cite:t}`DH10`
:label: theorem:coding_theorem
:enumerator: 1.8.2
For any $\sigma \in 2^{<\omega}$,

$$
\begin{aligned}
K(\sigma) = -\log R(\sigma) = -\log Q(\sigma) \pm O(1) = -\log \mathbf{m}(\sigma) \pm O(1).
\end{aligned}
$$
:::

One informal corollary of the Coding Theorem is that: having many *long* $\mathbf{U}_{\operatorname{PF}}$-descriptions implies having at least one *short* $\mathbf{U}_{\operatorname{PF}}$-description. To see this, suppose $\Pi$ is a collection of strings $\pi \in 2^{<\omega}$ all of a common length $\ell \in \omega$ and serving as $\mathbf{U}_{\operatorname{PF}}$-descriptions for the string $\sigma \in 2^L$. Then, the *a priori* probability of $\sigma$ will be at least:

$$
\begin{aligned}
Q(\sigma) &= \lambda([\set{\pi \in 2^{< \omega}}{\mathbf{U}_{\operatorname{PF}}(\pi) \downarrow = \sigma}]) \geq \lambda([\Pi]) = \sum_{\pi \in \Pi} 2^{-\operatorname{len}(\pi)} = \abs{\Pi} \cdot 2^{-\ell}.
\end{aligned}
$$

Thus, by the Coding Theorem [1.8.2](#theorem:coding_theorem), $\sigma$ has an appropriately shorter $\mathbf{U}_{\operatorname{PF}}$-description:

$$
\begin{aligned}
K(\sigma) \leq - \log Q(\sigma) + O(1) \leq \ell - \log \abs{\Pi} + O(1).
\end{aligned}
$$

## 1.8.2 Continuous Semimeasures

Discrete semimeasures do not take into account the topology of Cantor space, while a continuous semimeasure does by considering how mass distributes from a string to its extensions. In particular, a function $M: 2^{<\omega} \to [0, 1]$ is said to be a *continuous semimeasure* on $2^\omega$ if it satisfies $M(\sigma) \geq M(\sigma^\smallfrown 0) + M(\sigma ^\smallfrown 1)$ for all $\sigma \in 2^{<\omega}$. As in the discrete case, there exists a reference *optimal* lower-semicomputable continuous semimeasure $\mathbf{M}$ on $2^\omega$. That is, if $M$ is any other lower-semicomputable continuous semimeasure, there exists a constant $\beta > 0$ such that for all $\sigma \in 2^{<\omega}$, we have $\mathbf{M}(\sigma) \geq \beta \cdot M(\sigma)$. Refer to Section 4.5 of {cite:t}`LV08` for more details.

We denote by $\operatorname{KM}(\sigma) := - \log \mathbf{M}(\sigma)$ the *a priori complexity* of a string $\sigma \in 2^{<\omega}$. It is interesting to compare this complexity notion to prefix complexity. There are few satisfying bounds on their difference. Refer to {cite:p}`US96` and Section 4.5.5 of {cite:t}`DH10` for more details.

It is important to mention the fundamental role that constructive martingales have played in the development of algorithmic information theory. By 2000, J. Lutz had introduced algorithmically-restricted betting strategies called *constructive supergales* as a generalization to the constructive martingales in C. Schnorr's early work on algorithmic randomness {cite:p}`Lut00; Sch71`. Let us see why, for a certain class of premeasures, these betting strategies are interchangeable with the lower-semicomputable continuous semimeasures.

Given a premeasure $\rho$ on $2^\omega$, a *$\rho$-supergale* is a map $\delta : 2^{<\omega} \to [0, +\infty)$ such that

$$
\begin{aligned}
\delta(\sigma) \cdot \rho([\sigma]) \geq \delta(\sigma^\smallfrown 0) \cdot \rho([\sigma^\smallfrown 0]) + \delta(\sigma^\smallfrown 1) \cdot \rho([\sigma^\smallfrown 1]),
\end{aligned}
$$

for each $\sigma \in 2^{<\omega}$. If indeed $\rho = \rho_{s}$ for some $s \geq 0$, simply refer to $\delta$ as an *$s$-supergale*.

A $\rho$-supergale is said to *succeed* on a subset $X \subseteq 2^{\omega}$ if for each $x \in X$, we have $\limsup_{r \to \infty} \delta(\restrict{x}{r}) = + \infty$. Thus, to succeed on an infinite sequence $x \in 2^\omega$ is to earn arbitrarily much by taking bets on new bits of $x$ following the betting strategy $\delta$.

It had already been shown by J. Lutz in {cite:t}`Lut2000` that the Hausdorff dimension of a subset $X \subseteq 2^\omega$ may be characterized by the ability for $s$-supergales to succeed on $X$. That is,

```{math}
:label: equation:classical_relationship_supergales_and_Hausdorff_dimension
:enumerator: 1.8.5
\begin{aligned}
\dim_{\operatorname{H}}(X) = \inf \set{s \geq 0}{\text{there exists an $s$-supergale succeeding on $X$}}.
\end{aligned}
```

Lutz's subsequent idea was to restrict supergales by an effectivity condition and see whether they could still recover classical Hausdorff dimension. Call a $\rho$-supergale to be *constructive* if it is lower-semicomputable. If $\rho$ is length-invariant, strictly-positive, and computable on the cylinder sets $\mathcal{B}$ (e.g., any $s$-dimensional Hausdorff premeasure $\rho_{s}$ with computable $s \geq 0$), it holds that $\delta$ is a (constructive) $\rho$-supergale if and only if the map $M : \sigma \mapsto \delta(\sigma) \cdot \rho([\sigma])$ is a (lower-semicomputable) continuous semimeasure.

Thus, continuous semimeasures are also related to Hausdorff dimension in $2^\omega$, and we may extend the notion of success to them as follows: a continuous semimeasure $M$ is said to *$\rho$-succeed* on $X \subseteq 2^\omega$ if for each $x \in X$, we have $\limsup_{r \to \infty} M(\restrict{x}{r}) / \rho([\restrict{x}{r}]) = +\infty$. If $M$ is some lower-semicomputable continuous semimeasure which $\rho$-succeeds on $X$, then, by optimality, $\mathbf{M}$ also $\rho$-succeeds on $X$. When $\rho = \rho_{s}$, we refer to this as *$s$-success*.

From this perspective, the language of constructive supergales ports into the language of lower-semicomputable continuous semimeasures.

Another characterization of $s$-success for lower-semicomputable continuous semimeasures has to do with the existence of strong Solovay-$s$-tests of arbitrarily small prefix $s$-weight. Call $(q_n)_{n \in \omega} \subseteq \mathbb{Q}_{>0}$ *rapidly decreasing* if $\lim_{n \to \infty} q_n \cdot 2^n = 0$.

::::{prf:theorem}
:label: theorem:continuous_semimeasure_is_supergale_is_strong_Solovay_tests
:enumerator: 1.8.3
Fix $X \subseteq 2^\omega$ and computable $s > 0$. Then the following are equivalent.

:::{div}
:class: roman-list
1. There is a uniformly-c.e. sequence of strong Solovay-$s$-tests $(\mathcal{V}_n)_n$ and a computable, rapidly decreasing sequence $(q_n)_n$ where each $\mathcal{V}_n$ covers $X$ and satisfies $\operatorname{PW}_s(\mathcal{V}_n) \leq q_n$;
1. Some constructive $s$-supergale succeeds on $X$;
1. Some lower-semicomputable continuous semimeasure $s$-succeeds on $X$; and
1. $\mathbf{M}$ $s$-succeeds on $X$.
:::
::::

:::{prf:proof}
:nonumber:
It suffices to prove (i) $\iff$ (iii). First, suppose (i). For each $n \in \omega$, the map

$$
\begin{aligned}
M_n(\sigma) := \frac{1}{q_n} \operatorname{PW}_s(\set{\tau\in \mathcal{V}_n}{\sigma \preceq \tau})
\end{aligned}
$$

is a lower-semicomputable continuous semimeasure. And, whenever $\sigma \in \mathcal{V}_n$, it holds that $M_n(\sigma) \geq \frac{1}{q_n} \cdot 2^{-s \cdot \operatorname{len}(\sigma)}$. Now, define another lower-semicomputable continuous semimeasure

$$
\begin{aligned}
M(\sigma) := \sum_{n \in \omega} \frac{M_n(\sigma)}{2^{n + 1}}.
\end{aligned}
$$

Then, for each $\sigma \in \mathcal{V}_n$, we have $M(\sigma) \geq \frac{1}{q_n} \cdot 2^{-(n + 1) - s \cdot \operatorname{len}(\sigma)}$. Now, if $x \in X$ and $X$ is covered by each $\mathcal{V}_n$, it holds that for each $n \in \omega$, there exist infinitely many $r \in \omega$ for which $\restrict{x}{r} \in \mathcal{V}_n$. Hence,

$$
\begin{aligned}
\limsup_{r \to \infty} \frac{M(\restrict{x}{r})}{2^{-s \cdot \operatorname{len}(\restrict{x}{r})}} = \limsup_{r \to \infty} M(\restrict{x}{r}) \cdot 2^{s \cdot r} \geq \frac{1}{q_n} \cdot 2^{-(n + 1)} \to +\infty
\end{aligned}
$$

as $n \to +\infty$ since $(q_n)_n$ is rapidly decreasing. Thus, $M$ $s$-succeeds on $X$.

In the other direction, suppose (iii). Fix a computable, rapidly decreasing sequence $(q_n)_n$ and define for each $n \in \omega$ the c.e. set:

$$
\begin{aligned}
\mathcal{V}_n := \set{\sigma \in 2^{<\omega}}{M(\sigma) \cdot 2^{s \cdot \operatorname{len}(\sigma)} \geq \frac{1}{q_n}}.
\end{aligned}
$$

Notice that if $\mathcal{P} \subseteq \mathcal{V}_n$ is prefix-free, then

$$
\begin{aligned}
\operatorname{DW}_s(\mathcal{P}) = \sum_{\sigma \in \mathcal{P}} 2^{- s \cdot \operatorname{len}(\sigma)} \leq q_n \cdot \sum_{\sigma \in \mathcal{P}} M(\sigma) \leq q_n,
\end{aligned}
$$

so $\operatorname{PW}_s(\mathcal{V}_n) \leq q_n$ for all $n \in \omega$. Finally, for a fixed $n \in \omega$, if $x \in X$, then $M$ $s$-succeeding on $X$ implies there are infinitely many $r \in \omega$ for which $M(\restrict{x}{r}) \cdot 2^{s \cdot r} \geq \frac{1}{q_n}$, or $\restrict{x}{r} \in \mathcal{V}_n$. So, each $\mathcal{V}_n$ is a strong Solovay-$s$-test covering $X$, and the sequence $(\mathcal{V}_n)_n$ is uniformly-c.e.
:::
