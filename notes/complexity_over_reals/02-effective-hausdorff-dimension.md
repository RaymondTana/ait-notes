---
title: "Effective Hausdorff Dimension"
label: section:Effective_Hausdorff_Dimension
---

J. Lutz was the first to introduce a refinement to {term}`Hausdorff dimension` in the form of **constructive dimension** {cite:p}`Lut00`, which could distinguish between subsets of zero Hausdorff dimension by their algorithmically-exploitable patterns. Shortly after, E. Mayordomo demonstrated this quantity matched an algorithmic information density involving Kolmogorov complexity first studied by L. Staiger {cite:p}`May02; Sta89`. In this section, we review a few of the characterizations for effective dimension, but not necessarily in their historical order.

For simplicity, we define the effective dimension notions in this section over $2^\omega$. With slight adjustments, some may be extended to any $\mathbb{R}^m$.

Inspired by the definition of the local dimension of an outer measure in K. Falconer's book {cite:p}`Fal90`, define local dimension for outer measures and semimeasures as follows.

:::{prf:definition}
:label: definition:local_dimension
Let $\mu$ either be a {term}`discrete semimeasure`, {term}`continuous semimeasure`, or outer measure on $2^\omega$. Then the **(lower) local dimension** of a subset $X \subseteq 2^\omega$ with respect to $\mu$ is defined as:

$$
\begin{aligned}
\dim_{\operatorname{loc}} \mu(X) = \sup_{x \in X} \liminf_{r \to \infty} \frac{-\log \mu([\restrict{x}{r}])}{r},
\end{aligned}
$$

where $\mu([\restrict{x}{r}])$ is understood as $\mu(\restrict{x}{r})$ whenever $\mu$ is a semimeasure.
:::

In the language of {term}`supergales <Supergale>`, the map $\boldsymbol{\delta}(\sigma) := 2^{s \cdot \operatorname{len}(\sigma)} \cdot \mathbf{M}(\sigma)$ is an **optimal** constructive $s$-supergale whenever $s \geq 0$ is left-c.e. It follows from our Theorem [%s](#theorem:continuous_semimeasure_is_supergale_is_strong_Solovay_tests) that $\dim_{\operatorname{loc}} \mathbf{M}$ matches J. Lutz's **constructive dimension** {cite:p}`Lut00; Lut03`. That is, for any $X \subseteq 2^\omega$,

$$
\begin{aligned}
\dim_{\operatorname{loc}} \mathbf{M}(X) &= \inf \set{s \geq 0}{\text{there exists a constructive $s$-supergale succeeding on $X$}}\\
&=: \operatorname{cdim}(X).
\end{aligned}
$$

In light of ([%s](#equation:classical_relationship_supergales_and_Hausdorff_dimension)), we may consider $\operatorname{cdim}$ to be an effective version of Hausdorff dimension. We will cite some other asymptotic coincidences further justifying this view.

In {cite:t}`May02`, Mayordomo proved that Lutz's constructive dimension of a point $x$ matches the **lower incompressibility ratio of prefix Kolmogorov complexity** of $x$:

$$
\begin{aligned}
\operatorname{cdim}(X) = \underline{\kappa}(X) := \sup_{x \in X} \liminf_{r \to \infty} \frac{K(\restrict{x}{r})}{r} = \dim_{\operatorname{loc}} \mathbf{m}(X),
\end{aligned}
$$

where the last equality follows from the {term}`Coding Theorem` [%s](#theorem:coding_theorem). So $\mathbf{M}$ and $\mathbf{m}$ produce the same local dimension notion on $2^\omega$.

Note that by definition, $\dim_{\operatorname{loc}} \mathbf{M}$ is itself the **lower incompressibility ratio with respect to a priori complexity**:

$$
\begin{aligned}
\dim_{\operatorname{loc}} \mathbf{M}(X) = \sup_{x \in X} \liminf_{r \to \infty} \frac{\operatorname{KM}(\restrict{x}{r})}{r}.
\end{aligned}
$$

One might also attempt to effectivize the definition of classical Hausdorff dimension directly. Suppose $\mathcal{U}$ is a Martin-Löf-$s$-test covering $X \subseteq 2^\omega$. Then, $\mathcal{U}$ acts as an effective witness to $X$ being $s$-null. In analogy with the definition of Hausdorff dimension in ([%s](#equation:definition_of_Hausdorff_dimension)), define the **effective Hausdorff dimension** of $X \in 2^\omega$ to be:

$$
\begin{aligned}
\operatorname{effdim}(X) := \inf \set{s \geq 0}{\text{$X$ is ML-$s$-null}}.
\end{aligned}
$$

Note that the same could be done for any other of the effective test notions defined above. We prefer to work with Martin-Löf-randomness because it admits universal tests. In particular, for each left-c.e. $s > 0$, there exists a **universal** ML-$s$-test $\mathcal{U}^s$. This means that if $\mathcal{U}$ is an ML-$s$-test covering some subset $X \subseteq 2^\omega$, then so too will $\mathcal{U}^s$ cover $X$. The existence of such a $\mathcal{U}^s$ implies the **pointwise stability** of effective Hausdorff dimension. That is, for any $X \subseteq 2^{\omega}$,

$$
\begin{aligned}
\operatorname{effdim}(X) = \sup_{x \in X} \operatorname{effdim}(\seq{x}).
\end{aligned}
$$

Martin-Löf-$s$-randomness relates to success by constructive $s$-supergales. That is, if there exists a constructive $s$-supergale {term}`succeeding <Succeed>` on $X$, then $X$ will be ML-$t$-null for all left-c.e. $t > s$. Conversely, if $s$ is left-c.e. and $X$ is ML-$s$-null, then there exists a constructive $s$-supergale succeeding on $X$. Therefore, $\operatorname{cdim}(X) = \operatorname{effdim}(X)$ on all sets $X \subseteq 2^\omega$.

In his doctoral dissertation, N. Lutz introduced the map $\boldsymbol{\kappa}(X) := 2^{-K(X)}$, an outer measure on $2^\omega$ (originally, $\mathbb{R}^m$) which possesses many algorithmic optimality properties as explored in both {cite:p}`Lut17b; LL20`. In particular, J. Lutz and N. Lutz showed that $\boldsymbol{\kappa}(X)$ is **locally optimal** among all the other strongly finite, {term}`lower-semicomputable` outer measures on $2^\omega$, and that any locally optimal outer measure $\boldsymbol{\mu}$ has local dimension $\dim_{\operatorname{loc}}\boldsymbol{\mu}$ matching the lower incompressibility ratio of {term}`prefix complexity` {cite:p}`LL20`.

We now summarize these standard asymptotic coincidences in the following theorem.

:::{prf:theorem} Effective Dimension
:label: theorem:asymptotic_coincidences_Cantor
For any $X \subseteq 2^\omega$, we have

$$
\begin{aligned}
\small
\operatorname{effdim}(X) = \dim_{\operatorname{loc}} \mathbf{M}(X) = \dim_{\operatorname{loc}} \mathbf{m}(X) = \dim_{\operatorname{loc}} \boldsymbol{\kappa}(X) = \operatorname{cdim}(X) = \underline{\kappa}(X).
\end{aligned}
$$
:::

We will use $\dim(\cdot)$ as a generic placeholder for any one of those listed in Theorem [%s](#theorem:asymptotic_coincidences_Cantor) over either Cantor space or Euclidean space. And $\dim(x)$ will stand for $\dim(\seq{x})$ for any $x \in 2^\omega$.

We further note that **effectivized packing dimension** (or **strong dimension**) coincides with the *upper* incompressibility ratio of prefix complexity, as first shown in {cite:t}`AHLE07`. So, we fix the notation:

$$
\begin{aligned}
\operatorname{Dim}(X) := \overline{\kappa}(X) = \sup_{x \in X} \limsup_{r \to \infty} \frac{K(\restrict{x}{r})}{r}.
\end{aligned}
$$
