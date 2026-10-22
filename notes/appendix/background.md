---
title: Miscellaneous Results
label: appendix:miscellaneous
numbering:
  title:
    enumerator: A
---

Statements of results from the literature that are cited in these notes or in later chapters of my [dissertation](https://raymondtana.github.io/my_assets/documents/Raymond%20Tana%20PhD%20Dissertation.pdf).

:::{prf:theorem} Marstrand-Mattila Projection Theorem; c.f. Theorem 5.8 in {cite:t}`Mat15`
:label: theorem:marstrand_projection_original
Let $0 < n < m$ and $X \subseteq \mathbb{R}^m$ be analytic. Then,

$$
\begin{aligned}
\dim_{\operatorname{H}} \pi_V(X) = \min \seq{\dim_{\operatorname{H}} X, n} \qquad \text{for $\gamma_{m, n}$-almost all $V \in G(m, n)$}.
\end{aligned}
$$
:::

:::{prf:theorem} Theorem 1.3 in {cite:t}`Orp21`
:label: theorem:Orponen_weak_Marstrand
Let $0 < n < m$ and $X \subseteq \mathbb{R}^m$. Then

$$
\begin{aligned}
\dim_{\operatorname{P}} \pi_V(X) = \min \seq{\dim_{\operatorname{H}} X, n} \qquad \text{for $\gamma_{m, n}$-almost all $V \in G(m, n)$}.
\end{aligned}
$$
:::

::::{prf:lemma} Lemma 2.3 in {cite:t}`Orp21`
:label: lemma:Lemma_2.3_of_Orponen
Let $0 \leq s \leq m$, $\delta > 0$, $C \geq 1$, and $X \subset \mathbb{R}^m$ be a bounded subset with $N(X, \delta) \leq C \cdot \delta^{-s}$. Then, for any $L \geq 1$, there exists a disjoint decomposition $X = X_{\operatorname{good}} \sqcup X_{\operatorname{bad}}$ such that

:::{div}
:class: roman-list
1. $\mathcal{H}^s_{\operatorname{I}}(X_{\operatorname{bad}}) \leq C_m / L$, where $C_m$ only depends on $m$, and
1. $X_{\operatorname{good}}$ is contained in the $\delta$-neighborhood of a $(CL, \delta, s)$-set.
:::
::::

:::{prf:theorem} Theorem 1 in {cite:t}`Stu22_pinned`
:label: theorem:Stull_pinned_distance_theorem
Let $X \subseteq \mathbb{R}^2$ be an analytic set with Hausdorff dimension strictly greater than one. Then, for all $z \in \mathbb{R}^2$ outside a set of Hausdorff dimension at most one,

$$
\begin{aligned}
\dim_{\operatorname{H}}\p{\Delta_z X} \geq \frac{\dim_{\operatorname{H}}X}{4} + \frac{1}{2}.
\end{aligned}
$$
:::

:::{prf:theorem} Theorem 1.2 in {cite:t}`ABW23`
:label: theorem:Bushling_pinned_distance_theorem
For each $m \in \omega$, norm $\normAt{*}{\cdot}$ on $\mathbb{R}^m$, point $z \in \mathbb{R}^m$, and subset $X \subseteq \mathbb{R}^m$,

$$
\begin{aligned}
\dim_{\operatorname{H}}\p{\Delta^*_z X} \geq \dim_{\operatorname{H}}X - (m - 1).
\end{aligned}
$$
:::

:::{prf:theorem} Theorem 7.9 of {cite:t}`Kec95`
:label: theorem:Polish_space_as_continuous_image_of_Baire
If $\Omega$ is a Polish space, then there exists a closed class $F \subseteq \omega^\omega$ and a continuous bijection $g: F \to \Omega$. Furthermore, if $\Omega \neq \emptyset$, then there is a continuous surjection $\hat{g}: \omega^\omega \to \Omega$ extending $g$.
:::
