---
title: "Net Measures"
label: section:Net_Measures
---

For this section, fix a metric space $(\Omega, d)$.

## Net Measures

Recall the essential definitions of geometric measure theory from Section [%s](#section:Measures_and_Hausdorff_Dimension). In particular, we continue to use Method II for building outer measures from premeasures.

:::{prf:definition}
Let $\mathcal{N}$ be a net on $\Omega$ be a collection of subsets, and $\rho$ a premeasure on $\mathcal{N} \cup \seq{\emptyset}$. We call $\rho$ a **net premeasure** for $\mathcal{N}$. Then for each $\delta > 0$, the **$\rho$-dimensional $\delta$-content** under Method II is denoted by $\mathcal{H}^\rho_\delta$, while $\mathcal{H}^\rho$ denotes the corresponding **net (outer) measure** associated to $\rho$ under Method II.
:::

It will serve us to establish a notion of **comparability** between premeasures.

:::{prf:definition}
If $\nu$ and $\rho$ are both premeasures on $\Omega$, we say that $\nu$ is **comparable** to $\rho$ (denoted $\nu \asymp \rho$) if for all $X \subseteq \Omega$,

$$
\begin{aligned}
\mathcal{H}^\nu(X) = 0 \iff \mathcal{H}^\rho(X) = 0.
\end{aligned}
$$
:::

:::{prf:lemma}
:label: lem:comparability_numerical_condition
Let $\nu$ and $\rho$ both be premeasures on $\Omega$. Suppose for each $X \subseteq \Omega$, there exist functions $f$ and $g$ satisfying:

- $f: [0, +\infty] \to [0, +\infty]$ is continuous on the right on $[0, +\infty)$ and $f(0) = 0$,
- $g: (0, +\infty) \to (0, +\infty)$ satisfies $g(\delta) \to 0^+$ as $\delta \to 0^+$,

such that for all $\delta > 0$,

```{math}
:label: ineq:comparability_numerical_condition
\begin{aligned}
\mathcal{H}^\nu_\delta(X) \leq \mathcal{H}^\rho_\delta(X) \leq f\p{\mathcal{H}^\nu_{g(\delta)}(X)}.
\end{aligned}
```

Then $\nu$ and $\rho$ are comparable.
:::

:::{prf:proof}
:nonumber:
It is clear from ([%s](#ineq:comparability_numerical_condition)) that $\mathcal{H}^\rho(X) = 0$ implies $\mathcal{H}^\nu(X) = 0$ for all $X \subseteq \Omega$. For the reverse direction, assume $\mathcal{H}^\nu(X) = 0$. Then by ([%s](#ineq:comparability_numerical_condition)) and the assumptions on $f$ and $g$,

$$
\begin{aligned}
\mathcal{H}^\rho(X) = \lim_{\delta \to 0^+} \mathcal{H}^\rho_\delta(X) \leq \lim_{\delta \to 0^+} f\p{\mathcal{H}^\nu_{g(\delta)}(X)} = f\p{\lim_{\delta \to 0^+} \mathcal{H}^\nu_{g(\delta)}(X)} = f(\mathcal{H}^\nu(X)) = 0.
\end{aligned}
$$
:::

We will also make use of a stronger form of comparability which we call **commensurate up to multiplicative constants**.

:::{prf:definition}
If $\nu$ and $\rho$ are both premeasures on $\Omega$, we say that $\nu$ and $\rho$ are **commensurate up to multiplicative constants** (denoted $\rho = \Theta(\nu)$) if there exist constants $0 < c \leq C < +\infty$ such that for all $X \subseteq \Omega$,

$$
\begin{aligned}
c \cdot \mathcal{H}^\nu(X) \leq \mathcal{H}^\rho(X) \leq C \cdot \mathcal{H}^\nu(X).
\end{aligned}
$$
:::

## Net Dimension

Let us now introduce a notion of Hausdorff dimension restricted to a net.

:::{prf:definition}
For any $X \subseteq \Omega$, denote by $\dim_{\mathcal{N}}(X)$ the **Hausdorff dimension of $X$ restricted to the net $\mathcal{N}$**, which is defined as:

$$
\begin{aligned}
\dim_{\mathcal{N}}(X) := \inf \set{s \geq 0}{(\exists \rho \asymp \rho_s) \brk{\text{$X$ is $\rho$-null for the net premeasure $\rho$ on $\mathcal{N}$}}},
\end{aligned}
$$

or $+\infty$ when the infimum is taken over the empty set.
:::

Equivalently, we may write this quantity in terms of the dimension functions:

$$
\begin{aligned}
\dim_{\mathcal{N}}(X) = \inf \set{s \geq 0}{\mathcal{H}^{\restrict{\rho_s}{\mathcal{N}}} (X) = 0},
\end{aligned}
$$

where, for any premeasure $\rho$ on $\Omega$, the notation $\restrict{\rho}{\mathcal{N}}$ denotes the premeasure obtained by restricting $\rho$ to $\mathcal{N} \cup \seq{\emptyset}$:

$$
\begin{aligned}
(\restrict{\rho}{\mathcal{N}})(X) =
\begin{cases}
\rho(X) & X \in \mathcal{N},\\
0 & X = \emptyset,\\
\text{undefined} & \text{otherwise}.
\end{cases}
\end{aligned}
$$

Unpacking the definitions, we may write Hausdorff dimension restricted to a net even more explicitly:

$$
\begin{aligned}
\dim_{\mathcal{N}}(X) &= \inf \set{s \geq 0}{(\restrict{\mathcal{H}}{\mathcal{N}})^s(X) = 0},
\end{aligned}
$$

where we may perform Method II on any premeasure $\rho$ by covers consisting only of elements from an arbitrary collection $\mathcal{N} \subseteq \mathcal{P}(\Omega)$:

$$
\begin{aligned}
(\restrict{\mathcal{H}}{\mathcal{N}})^\rho(X) &:= \sup_{\delta > 0} (\restrict{\mathcal{H}}{\mathcal{N}})^\rho_{\delta}(X), \quad \text{where}\\
(\restrict{\mathcal{H}}{\mathcal{N}})^\rho_{\delta}(X) &:= \inf_{(C_i)_{i \in \omega}} \set{\sum_{i} \rho(C_i)}{C_i \in \mathcal{N}, \diam_d(C_i) \leq \delta, \bigcup_i C_i \supseteq X}.
\end{aligned}
$$

For the same reasons as in the unrestricted case, this quantity is well-defined. Note that as $\restrict{\rho_s}{\mathcal{N}}$ is a net premeasure on $\mathcal{N}$, the computation of Hausdorff dimension restricted to $\mathcal{N}$ permits only those covers whose cover elements are sourced from the net $\mathcal{N}$. In the case of dyadic cubes $\mathcal{N} = \mathcal{Q}$ on Euclidean space, $(\restrict{\mathcal{H}}{\mathcal{Q}})^s_\delta$ matches K. Falconer's $\mathscr{M}^s_\delta$ in Chapter 5 of {cite:t}`Fal85`.

Note that one may also perform Method I restricted to an arbitrary collection $\mathcal{N} \subseteq \mathcal{P}(\Omega)$:

$$
\begin{aligned}
(\restrict{\mathcal{H}}{\mathcal{N}})^\rho_{\operatorname{I}}(X) &:= \inf_{(C_i)_{i \in \omega}} \set{\sum_{i} \rho(C_i)}{C_i \in \mathcal{N}, \bigcup_i C_i \supseteq X}.
\end{aligned}
$$

We may now introduce net dimension.

:::{prf:definition}
For any $X \subseteq \Omega$, define the **net dimension of $X$** to be:

$$
\begin{aligned}
\dim_{\operatorname{net}}(X) := \inf \set{\dim_{\mathcal{N}}(X)}{\mathcal{N} \text{ is a net on $\Omega$}},
\end{aligned}
$$

or $+\infty$ when the infimum is taken over the empty set.
:::

Net dimension captures the ability to evaluate the Hausdorff dimension of a subset only through the various nets that might exist on the underlying metric space.

## Basic Facts about Net Measures

A few results about net measures come directly from Rogers {cite:p}`Rog70`, including the **Increasing Sets Lemma** and a stability result. Both of these results apply to layered-disjoint nets, which satisfy the stronger incomparability axiom (**N4**$'$).

:::{prf:theorem} Increasing Sets Lemma, Theorem 52 of {cite:t}`Rog70`
:label: theorem:increasing_sets_lemma
Let $\mathcal{N}$ be a layered-disjoint net on a metric space $(\Omega, d)$, and $\rho$ be a net premeasure for $\mathcal{N}$, and $\delta > 0$. Then for any increasing sequence $(X_n)_{n \in \omega}$ of subsets of $\Omega$, we have $\mu\p{\bigcup_{n} X_n} = \sup_n \mu(X_n)$.
:::

:::{prf:theorem} Stability, Theorem 53 of {cite:t}`Rog70`
:label: theorem:stability_for_net_measures
Let $\mathcal{N}$ be a layered-disjoint net on a metric space $(\Omega, d)$ and $\rho$ be a net premeasure for $\mathcal{N}$. Define for each $n \in \omega$ the sub-net $\mathcal{N}^+_n$ by removing from $\mathcal{N}$ the first $n$ many elements of positive diameter under the indexing $\iota$. Then $\mathcal{H}^\rho_{\operatorname{I}}(X) = \sup_n (\restrict{\mathcal{H}}{\mathcal{N}^+_n})^{\rho}_{\operatorname{I}} = \sup_n \mathcal{H}^{\restrict{\rho}{{\mathcal{N}^+_n}}}_{\operatorname{I}}$.
:::
