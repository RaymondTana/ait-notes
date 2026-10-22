---
title: "Computable Absolutely Lipschitz Families"
label: section:CALF
---

## Definition of a CALF

We are interested in capturing the computability and algebraic properties of families of curves or surfaces like the planar lines. So we will only consider maps of the form $\Phi : \mathbb{R}^m \times \mathbb{R}^\ell \to \mathbb{R}^n$, where the first $m$ components of the arguments encode a parameterization of some function in the family, and the following $\ell$ components serve as input. Given any such $\Phi$ and open subsets $\Omega \subseteq \mathbb{R}^m$ and $\Xi \subseteq \mathbb{R}^\ell$ (which we call our **domains**), we might define the family of all parameterized, real-valued functions under $\Phi$ on domain $\Omega \times \Xi$:

$$
\begin{aligned}
\mathcal{F}_\Phi(\Omega \times \Xi) = \set{\Phi^{\boldsymbol{\alpha}}}{\boldsymbol{\alpha} \in \Omega},
\end{aligned}
$$

where $\Phi^{\boldsymbol{\alpha}} : \Xi \to \mathbb{R}^n$ denotes the map $x \mapsto \Phi(\boldsymbol{\alpha}, x)$. And since we are also interested in statements about finitary inputs, we further denote for any $r \in \omega$,

$$
\begin{aligned}
\Omega_r := \restrict{\Omega}{r} = \set{\restrict{\boldsymbol{\alpha}}{r}}{\boldsymbol{\alpha} \in \Omega} \subseteq \mathbb{D}^m_r,
\end{aligned}
$$

and let $\Omega_{<\omega}$ be the union of all $\Omega_r \subseteq \mathbb{D}^m$. Analogous notation will apply for $\Xi$.

Since the domain $\Omega$ is assumed to be open, we have for any $\boldsymbol{\alpha} \in \Omega$ that there exists $r \gg 1$ for which $\restrict{\boldsymbol{\alpha}}{r} \in \Omega_r \cap \Omega$. An analogous statement holds for $\Xi$. This will be useful for reducing our infinitary theorem to the finitary case.

Locally, certain parameter components may or may not (linearly) depend on the input $x$. Let us fix a way to distinguish between these two behaviors. Fix any two parameters $\boldsymbol{\alpha}, \boldsymbol{\beta} \in \Omega \subseteq \mathbb{R}^m$. A component $0 \leq i < m$ will be considered **roughly constant** for $\Phi$ at $\boldsymbol{\alpha}$ and $\boldsymbol{\beta}$ if, for each $\boldsymbol{\alpha}', \boldsymbol{\beta}'$ which differ from $\boldsymbol{\alpha}, \boldsymbol{\beta}$ only at component $i$, and for all $x \in \Xi$,

$$
\begin{aligned}
\norm{(\Phi^{\boldsymbol{\alpha'}}(x) - \Phi^{\boldsymbol{\beta'}}(x)) - (\Phi^{\boldsymbol{\alpha}}(x) - \Phi^{\boldsymbol{\beta}}(x))} \leq
O\p{\norm{\boldsymbol{\alpha}' - \boldsymbol{\alpha}} + \norm{\boldsymbol{\beta}' - \boldsymbol{\beta}}}
\end{aligned}
$$

independently of $x$. Otherwise, the component $i$ will be considered **co-Lipschitz** for $\Phi$. We collect into the tuple $(\boldsymbol{\alpha} - \boldsymbol{\beta})_{\operatorname{cL}}$ all differences $\boldsymbol{\alpha}_i - \boldsymbol{\beta}_i$ where $i$ is a co-Lipschitz component for $\Phi$ at $\boldsymbol{\alpha}$ and $\boldsymbol{\beta}$.

::::{prf:definition}
A **computable absolutely Lipschitz family (CALF)** on a domain $\Omega \times \Xi \subseteq \mathbb{R}^m \times \mathbb{R}^\ell$ is a partial-computable map $\Phi : \Omega \times \Xi \to \mathbb{R}^n$ such that

:::{div}
:class: roman-list
1. $\Phi$ is **scaling Lipschitz continuous**. That is, for all $\boldsymbol{\alpha}, \boldsymbol{\beta} \in \Omega$ and $x_1, x_2 \in \Xi$,

   $$
   \begin{aligned}
   \norm{\Phi^{\boldsymbol{\alpha}}(x_1) - \Phi^{\boldsymbol{\beta}}(x_2)} \leq &\p{O(\norm{x_1}) + O(1) + o(1)} \cdot \norm{\boldsymbol{\alpha} - \boldsymbol{\beta}}\\
   &+ (O(\norm{\boldsymbol{\alpha}}) + O(1)) \cdot \norm{x_1 - x_2},
   \end{aligned}
   $$

   where the $o(1)$ term vanishes as $\norm{x_1 - x_2} \to 0$.

1. $\Phi$ has **scaling co-Lipschitz continuous differences**. That is, for all $\boldsymbol{\alpha}, \boldsymbol{\beta} \in \Omega_{< \omega}$, it holds that $\Phi^{\boldsymbol{\alpha}} - \Phi^{\boldsymbol{\beta}}$ is either constant or **scaling co-Lipschitz continuous**, meaning for all $x_1, x_2 \in \Xi$,

   $$
   \begin{aligned}
   \norm{(\boldsymbol{\alpha} - \boldsymbol{\beta})_{\operatorname{cL}}} \cdot \norm{x_1 - x_2} &= O_{\norm{x_1}, \norm{x_2}}\p{\norm{(\Phi^{\boldsymbol{\alpha}}(x_1) - \Phi^{\boldsymbol{\beta}}(x_1)) - (\Phi^{\boldsymbol{\alpha}}(x_2) - \Phi^{\boldsymbol{\beta}}(x_2))}},
   \end{aligned}
   $$

   where the constant may depend on $\norm{x_1}$ and $\norm{x_2}$; and there is an algorithm deciding this from $\boldsymbol{\alpha}$ and $\boldsymbol{\beta}$.

1. $\Phi$ has **dense intersections**. That is, for all $r \in \omega$, $\boldsymbol{\alpha} \in \Omega_{r}$, and $x \in \Xi$, there is an algorithm using $\restrict{x}{r}$ and $\restrict{\Phi^{\boldsymbol{\alpha}}(x)}{r}$ (as well as $r$, $m$, $n$, $\ell$, and $\restrict{\boldsymbol{\alpha}}{O(1)}$) to compute a $(2^{-r} \cdot O_{\norm{\boldsymbol{\alpha}}, \norm{x}, m, n}(1))$-approximation to some $\boldsymbol{\beta} \in B_{2^{-r} \cdot O_{\norm{\boldsymbol{\alpha}}, \norm{x}, m, n}(1)}(\boldsymbol{\alpha}) \cap \Omega_r$ satisfying $\Phi^{\boldsymbol{\alpha}} - \Phi^{\boldsymbol{\beta}}$ is scaling co-Lipschitz continuous with $-\log_2 \norm{(\boldsymbol{\alpha} - \boldsymbol{\beta})_{\operatorname{cL}}} \leq r - O_{\norm{\boldsymbol{\alpha}}, \norm{x}, m, n}(1)$.
:::
::::

:::{prf:definition}
Let $\Phi$ be a CALF on $\Omega \times \Xi$. We fix a measure of similarity between two parameters $\boldsymbol{\alpha}, \boldsymbol{\beta} \in \Omega$ as follows:

$$
\begin{aligned}
S(\boldsymbol{\alpha}, \boldsymbol{\beta}) = -\log \norm{(\boldsymbol{\alpha} - \boldsymbol{\beta})_{\operatorname{cL}}}.
\end{aligned}
$$

In particular, if $\restrict{\boldsymbol{\alpha}}{r} = \restrict{\boldsymbol{\beta}}{r}$, then $S(\boldsymbol{\alpha}, \boldsymbol{\beta}) \geq r - O(1)$.
:::

## Standard Example of a CALF

:::{prf:example} Points on Planar Lines
:label: example:lines
Take $\Phi$ to be the computable map on $\mathbb{R}^2 \times \mathbb{R} \to \mathbb{R}$ given by

$$
\begin{aligned}
\Phi(a, b, x) = ax + b.
\end{aligned}
$$

We show that $\Phi$ is a CALF on its domain. The real-function family $\mathcal{F}_\Phi$ associated to this map consists of all the non-vertical, planar lines as expressed in slope-intercept form with parameters $a$ and $b$ and input $x$. Let us fix two sets of slope-intercept parameters $(a, b), (u, v) \in \mathbb{R}^2$ and two inputs $x_1, x_2 \in \mathbb{R}$.

It is easy to see that $\Phi$ is scaling Lipschitz continuous: we may check using the triangle inequality that:

$$
\begin{aligned}
\abs{\Phi^{(a, b)}(x_1) - \Phi^{(u, v)}(x_2)} \leq \norm{(a, b) - (u, v)} \cdot \p{\abs{x_1} + 1 + \abs{x_1 - x_2}} + \abs{a} \cdot \abs{x_1 - x_2}.
\end{aligned}
$$

Moreover, $\Phi^{(a, b)} - \Phi^{(u, v)}$ is constant if and only if $a = u$. In addition, the slope parameter is a co-Lipschitz parameter, while the intercept parameter is roughly constant in the sense defined above. Indeed, given different choices $a', b', u', v' \in \mathbb{R}$ and any $x \in \mathbb{R}$,

$$
\begin{aligned}
\abs{(\Phi^{(a', b)}(x) - \Phi^{(u', v)}(x)) - (\Phi^{(a, b)}(x) - \Phi^{(u, v)}(x))} &= \abs{(a' - a) - (u' - u)} \abs{x},\\
\abs{(\Phi^{(a, b')}(x) - \Phi^{(u, v')}(x)) - (\Phi^{(a, b)}(x) - \Phi^{(u, v)}(x))}&\leq \abs{(b' - b) - (v' - v)} \leq \abs{b' - b} + \abs{v' - v}.
\end{aligned}
$$

Thus, in this example, $\norm{((a, b) - (u, v))_{\operatorname{cL}}} = \abs{a - u}$. It is also straightforward to check that:

$$
\begin{aligned}
\abs{(\Phi^{(a, b)}(x_1) - \Phi^{(u, v)}(x_1)) - (\Phi^{(a, b)}(x_2) - \Phi^{(u, v)}(x_2))} &= \abs{a - u} \cdot \abs{x_1 - x_2}.
\end{aligned}
$$

So we also conclude that $\Phi$ has scaling co-Lipschitz continuous differences.

We finally argue that $\Phi$ has dense intersections. Fix $r \in \omega$, $(a, b) \in \mathbb{D}_r^2$, and $x \in \mathbb{R}$. We appeal to the the machine construction and geometric observations used in proving Lemma 6(i) of {cite:t}`LS16`. Their argument can be seen as constructing a Turing machine which receives a description for $(\restrict{x}{r}, \restrict{(ax + b)}{r})$, along with descriptions for $r$ and $\restrict{(a, b)}{1}$, to produce parameters $(u_0, v_0) \in B_{2^{-r}}(a, b)$ satisfying:

$$
\begin{aligned}
\abs{u_0 \cdot (\restrict{x}{r}) + v_0 - \restrict{(ax + b)}{r}} < 2^{-r} \cdot (\abs{u_0} + \abs{\restrict{x}{r}} + 3).
\end{aligned}
$$

By their Observation A.4(ii), there exists $(u, v) \in B_{2^{\gamma - r}}(u_0, v_0) \cap \mathbb{D}_r^2$ such that $u \neq a$, where $\gamma = \log(2 \abs{a} + \abs{x} + 5)$. These parameters $(u, v)$ will necessarily agree in output with $(a, b)$ at input $x$ up to precision $2^{-r} \cdot O(\abs{a} + \abs{x} +1)$.
:::
