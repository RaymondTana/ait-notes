---
title: "Net Semimeasures"
label: section:Net_Semimeasures
---

Recall that in Section [%s](#section:Semimeasures), we discussed two approaches towards mass spreading along the cylinder sets over Cantor space, each of which admitted optimal elements and corresponding complexity notions for points in Cantor space. We may extend these approaches to maps which spread mass across the elements of a mesh, obtaining analogous results about the existence of optimal elements and corresponding complexity notions. As in Cantor space, a **discrete** assessment would not distinguish between elements of the mesh, whereas a **continuous** assessment would respect the DAG structure between mesh elements encoded in the containment relation. We begin by defining a continuous mesh semimeasure on a represented mesh space. For the rest of the section, fix a metric space $(\Omega, d)$ and a represented mesh space $(\Omega, \mathcal{N}, \mathscr{R})$.

## Continuous Mesh Semimeasures

:::{prf:definition}
A function $M: \omega \to [0, 1]$ is a **continuous mesh semimeasure on $(\Omega, \mathcal{N})$** if it satisfies both:

```{math}
:label: eqn:continuous_mesh_semimeasure_condition
\begin{aligned}
M(i) &\geq \sum_{\operatorname{pred}(i, j)} M(j), \quad \text{and}
\end{aligned}
```

```{math}
:label: eqn:boundedness_continuous_mesh_semimeasure_condition
\begin{aligned}
1 &\geq \sum_{\operatorname{root}(i)} M(i),
\end{aligned}
```

where $\operatorname{root}$ is the predicate encoding the root elements of $\mathcal{N}$.
:::

In words, the **continuous semimeasure condition** in ([%s](#eqn:continuous_mesh_semimeasure_condition)) asks that the map spread measure in such a way so that the measure assigned to a fixed mesh element is never exceeded by the sum of the measure assigned to its immediate successors. The boundedness condition in ([%s](#eqn:boundedness_continuous_mesh_semimeasure_condition)) asks that the map begin with no more than unity amount of measure across all of the mesh's root elements. Note that the maps $M : i \mapsto 0$ for all $i \in \omega$ trivially qualifies as a continuous mesh semimeasure.

For a fixed mesh space $(\Omega, \mathcal{N})$ and indexing $\iota$, let $\mathcal{E} \sqsubseteq_{\operatorname{D}} i$ denote

$$
\begin{aligned}
[j \in \mathcal{E} \implies \iota(j) \subseteq \iota(i)] \AND [j, k \in \mathcal{E} \AND j \neq k \implies \iota(j) \cap \iota(k) = \emptyset],
\end{aligned}
$$

meaning $\mathcal{E}$ is a collection of indices of mutually-disjoint mesh elements which are all subsets of the $i$-th mesh element. If $(\Omega, \mathcal{N}, \mathscr{R})$ is in fact a represented net space, let $\mathcal{E} \sqsubseteq_{\operatorname{PF}} i$ denote that $\mathcal{E}$ contains the indices of a collection of net elements whose addresses in the associated forest $\mathcal{G}$ form a prefix-free collection all extending the address of the $i$-th net element. Of course, $\mathcal{E} \sqsubseteq_{\operatorname{D}} i$ implies $\mathcal{E} \sqsubseteq_{\operatorname{PF}} i$ over net spaces, and the two are equivalent over layered-disjoint nets.

A straightforward argument by induction gives the following result about how continuous mesh semimeasures spread measure across incomparable sequences of mesh elements. Compare this to Property 3.8 in {cite:t}`May14`.

:::{prf:proposition} Generalized Kraft Inequality
:label: prop:generalized_Kraft_inequality
Let $M$ be a continuous mesh semimeasure. If $\mathcal{E} \sqsubseteq_{\operatorname{D}} i$, then

$$
\begin{aligned}
M(i) \geq \sum_{e \in \mathcal{E}} M(e).
\end{aligned}
$$
:::

Moreover, we have an alternate characterization of **continuous net semimeasures** (i.e., the continuous mesh semimeasures over a net).

:::{prf:proposition}
:label: mutually_incomparable_continuous_semimeasure_property
$M$ is a continuous net semimeasure if and only if both $M$ satisfies ([%s](#eqn:boundedness_continuous_mesh_semimeasure_condition)) and, for all $i \in \omega$ and $\mathcal{E} \sqsubseteq_{\operatorname{PF}} i$,

$$
\begin{aligned}
M(i) \geq \sum_{e \in \mathcal{E}} M(e).
\end{aligned}
$$
:::

Recall the discussion from Section [%s](#section:Computability_Theory) on lower-semicomputability. A continuous mesh semimeasure $M$ on $(\Omega, \mathcal{N})$ is **lower-semicomputable** if its lower-graph is computably enumerable relative to the given $\omega$-presentation $\mathscr{R}$. Collect into $\mathcal{M}$ all lower-semicomputable continuous mesh semimeasures in $\mathcal{N}$ with respect to the given $\omega$-presentation $\mathscr{R}$. Then, as in the case of Cantor space, a continuous semimeasure from $\mathcal{M}$ is **optimal** if it multiplicatively dominates all other semimeasures from $\mathcal{M}$.

:::{prf:theorem}
:label: prop:exists_optimal
Over a given represented mesh space $(\Omega, \mathcal{N}, \mathscr{R})$, there exists an optimal lower-semicomputable continuous mesh semimeasure.
:::

Our proof will loosely follow the structure outlined in M. Li and P. Vitányi's Theorem 4.5.1 for constructing an optimal lower-semicomputable continuous semimeasure over some finitely-branching sequence space {cite:p}`LV08`. We will use that any element of $\mathcal{M}$ is $[0,1]$-valued, which follows from the second continuous mesh semimeasure property $(\ref{eqn:boundedness_continuous_mesh_semimeasure_condition})$.

::::{prf:proof}
:nonumber:
We build our optimal element using left-approximators to the continuous semimeasures in $\mathcal{M}$. In the first step of the construction, we obtain an enumeration of left-approximators $\widehat{f}$ to the non-negative, lower-semicomputable maps $f \geq 0$. Then, in the next step, each $\widehat{f}$ is turned into a left-approximator for some lower-semicomputable continuous mesh semimeasure. Finally, we take a weighted sum of all these left-approximators to the elements of $\mathcal{M}$; this defines a computable map which left-approximates an optimal element of $\mathcal{M}$.

First, note that it is possible to enumerate all $\mathscr{R}$-computable functions of the form $\phi : \omega^2 \to \mathbb{Q} \cap [0, +\infty)$. For any lower-semicomputable map $f: \omega \to [0, \infty)$, the discussion in Section [%s](#section:Computability_Theory), guarantees that at least one of the $\phi$ above will left-approximate $f$.

Next, use a given $\phi$ to define another map $\psi : \omega^2 \to \mathbb{R}$ meant to be a left-approximator to some semimeasure in $\mathcal{M}$. By dovetailing this staged process across the enumeration of all $\phi$, we will have described a uniform algorithm for approximating all elements of $\mathcal{M}$ from below (computably in $\mathscr{R}$), exactly what is needed for building an optimal element of $\mathcal{M}$.

:::{div}
:class: pseudocode
Stage $r = 0$:\
  Initialize $\psi(i, 0) = 0$ for all $i \in \omega$;\
Stage $r > 0$:\
  Initialize the temporary variable $\widetilde{\psi}_r(i) = 0$ for all $i \in \omega$;\
  For $i$ := $r - 1$,$r - 2$,...,$0$ do:\
    Set $\widetilde{\psi}_r(i) = \max \seq{\phi(i, r), \sum_{j < r} \set{\widetilde{\psi}_r(j)}{\operatorname{pred}(i, j)}}$;\
  If $\sum \set{\widetilde{\psi}_r(k)}{\operatorname{root}(k) \AND k < r} > 1$:\
    Set $\psi(i, r) := \psi(i, r - 1)$ for all $i \in \omega$;\
  Else:\
    Set $\psi(i, r) := \widetilde{\psi}_r(i)$ for all $i \in \omega$;\

:::

In words, we use $\phi(\cdot, r)$ to build a semimeasure $\widetilde{\psi}_r$ which only assigns non-zero values to indices below $r$. So long as the proposed $\widetilde{\psi}_r$ does not assign more than unit mass to the roots of the mesh, we use $\widetilde{\psi}_r$ to update $\psi(\cdot, r)$. Otherwise, we carry over the values of $\psi(\cdot, r - 1)$ from the previous stage.

If at any stage the construction attempts to assign more than unit mass across the root elements, the resulting $\psi$ will not be updated beyond that stage. Such a map will trivially satisfy $\psi(\cdot, r) : \omega \to \mathbb{R}$ being a continuous mesh semimeasure for each $r \in \omega$.

Otherwise, the map $\psi$ is updated successfully at each stage. We have that the limiting map $M_\phi : i \mapsto \lim_{r \to \infty} \psi(i, r)$ is a continuous mesh semimeasure on $\mathcal{N}$. The second condition ([%s](#eqn:boundedness_continuous_mesh_semimeasure_condition)) is clear, so it remains to demonstrate the first property ([%s](#eqn:continuous_mesh_semimeasure_condition)).

Fix $i \in \omega$. Should $i$ have only finitely many immediate successors $j$, then by stage $r > \max\set{j}{\operatorname{pred}(i, j)}$, it is guaranteed by construction that $\widetilde{\psi}_r(i) \geq \sum_{\operatorname{pred}(i,j)} \widetilde{\psi}_r(j)$. So, in the limit,

$$
\begin{aligned}
\psi(i, r) \geq \sum_{\operatorname{pred}(i, j)} \psi(j, r).
\end{aligned}
$$

Otherwise, $i$ has infinitely many immediate successors. Note that by assumption, $\sum_{\operatorname{pred}(i, j)} \psi(j) \leq 1$. In particular, this sum converges. Fix $\varepsilon > 0$. There exists a sufficiently large integer $J \gg 1$ so that the partial sum satisfies:

$$
\begin{aligned}
\sum_{\substack{\operatorname{pred}(i, j) \\
j < J}} \psi(j, r) \geq \sum_{\operatorname{pred}(i, j)} \psi(j, r) - \varepsilon.
\end{aligned}
$$

And for any stage $r > J$, it is guaranteed by construction that

$$
\begin{aligned}
\widetilde{\psi}_r(i) \geq \sum_{\substack{\operatorname{i, j} \\
j < J}} \widetilde{\psi}_r(j) \implies \psi(i, r) \geq \sum_{\substack{\operatorname{i, j} \\
j < J}} \psi(j, r) \geq \sum_{\operatorname{pred}(i, j)} \psi(j, r) - \varepsilon.
\end{aligned}
$$

Since $\varepsilon > 0$ is arbitrary, we have exhibited the continuous mesh semimeasure property.

Thus, no matter $\phi$, the limiting map $M_\phi : i \mapsto \lim_{r \to \infty} \psi(i, r)$ from this construction will always satisfy $M_\phi \in \mathcal{M}$.

Furthermore, for a given $M \in \mathcal{M}$, there exists an $\mathscr{R}$-computable left-approximator $\phi$ to $M$ where each map $i \mapsto \phi(i, r)$ is itself a continuous mesh semimeasure. In that case, the resulting map $\psi = \phi$, and so $M_\phi = M$ is the limiting map from this construction. Therefore, we have an algorithm for left-approximating all the elements of $\mathcal{M}$. Call $(\psi_n)_{n \in \omega}$ the enumeration of all $\mathscr{R}$-computable left-approximators constructed from our enumeration $(\phi_n)_{n \in \omega}$ of all maps $\phi$, and $(M_n)_{n \in \omega}$ the corresponding enumeration of all their limiting maps.

We now build another $\mathscr{R}$-computable map $\boldsymbol{\psi}$ as follows:

$$
\begin{aligned}
\boldsymbol{\psi} : \omega^2 \to \mathbb{Q} \cap [0,1], \qquad \boldsymbol{\psi}(i, r) := \sum_{n < r} \frac{\psi_n(i, r)}{2^{n + 1}},
\end{aligned}
$$

This map $\boldsymbol{\psi}$ is the left-approximator of some lower-semicomputable map $\mathbf{M}$ which satisfies:

$$
\begin{aligned}
\mathbf{M}: \omega \to [0, 1], \qquad \mathbf{M}(i) := \sum_n \frac{M_n(i)}{2^{n + 1}}.
\end{aligned}
$$

We see that $\mathbf{M}$ is a continuous mesh semimeasure on $\mathcal{N}$ because for any $i \in \omega$,

$$
\begin{aligned}
\mathbf{M}(i) &= \sum_n \frac{M_n(i)}{2^{n + 1}} \geq \sum_n \frac{1}{2^{n + 1}} \sum_{\operatorname{pred}(i,j)} M_n(j) = \sum_{\operatorname{pred}(i, j)} \sum_n \frac{M_n(j)}{2^{n + 1}} = \sum_{\operatorname{pred}(i, j)} \mathbf{M}(j).
\end{aligned}
$$

Moreover,

$$
\begin{aligned}
\sum_{\operatorname{root}(i)} \mathbf{M}(i) = \sum_{\operatorname{root}(i)} \sum_n \frac{M_n(i)}{2^{n + 1}} = \sum_n \frac{1}{2^{n + 1}} \sum_{\operatorname{root}(i)} M_n(i) \leq \sum_n \frac{1}{2^{n+ 1}} \cdot 1 = 1.
\end{aligned}
$$

Finally, we check that $\mathbf{M}$ is optimal. Fix $M \in \mathcal{M}$, and let $n \in \omega$ be its index in the enumeration of $\mathcal{M}$, giving $M \equiv M_n$. Thus, for any $i \in \omega$,

$$
\begin{aligned}
M(i) = M_n(i) \leq 2^{n + 1} \cdot \mathbf{M}(i).
\end{aligned}
$$
::::

As discussed in Section [%s](#section:Semimeasures), the language of continuous mesh semimeasures may be translated to that of supergales (also see {cite:t}`May14`). In particular, given any $\rho$ premeasure on $\Omega$, we might associate to the continuous mesh semimeasure $M$ the **$\rho$-mesh-supergale**:

$$
\begin{aligned}
\delta(i) := \begin{cases}
\frac{M(i)}{\rho(\iota(i))} & \rho(\iota(i)) > 0,\\
+\infty & \rho(\iota(i)) = 0.
\end{cases}
\end{aligned}
$$

It is straightforward to check that $\delta$ satisfies the **$\rho$-mesh-supergale condition**:

$$
\begin{aligned}
\delta(i) \cdot \rho(\iota(i)) \geq \sum_{\operatorname{pred}(i, j)} \delta(j) \cdot \rho(\iota(j)), \quad \text{for each $i \in \omega$}.
\end{aligned}
$$

In particular, whenever $\rho$ is a computable premeasure, the continuous mesh semimeasure $M$ is lower-semicomputable if and only if its corresponding $\rho$-mesh-supergale is **constructive**; i.e., lower-semicomputable in the $\omega$-presentation $\mathscr{R}$ of $\mathcal{N}$.

We might also extend the notion of an $\rho$-mesh-supergale **succeeding** on a point.

:::{prf:definition}
Fix a premeasure $\rho$ on the mesh $\mathcal{N}$. Then a $\rho$-mesh-supergale $\delta$ on $(\Omega, \mathcal{N})$ is said to **succeed on $x \in \Omega$** if there exists an $\mathcal{N}$-name $(i_n)_n \in \mathcal{R}(x)$ of $x$ such that:

$$
\begin{aligned}
\limsup_{n \to \infty} \delta(i_n) = + \infty.
\end{aligned}
$$
:::

This form of success then translates to the following for continuous mesh semimeasures.

:::{prf:definition}
Fix a premeasure $\rho$ on the mesh $\mathcal{N}$. Then a continuous mesh semimeasure $M$ is said to **$\rho$-succeed on $x \in \Omega$** if there exists an $\mathcal{N}$-name $(i_n)_n \in \mathcal{R}(x)$ of $x$ with

$$
\begin{aligned}
\limsup_{n \to \infty} \brk{\frac{M(i_n)}{\rho(\iota(i_n))}} = + \infty,
\end{aligned}
$$

where this ratio is defined as $+\infty$ whenever $\rho(\iota(i_n)) = 0$.
:::

These notions of success extend to subsets $X \subseteq \Omega$ by asking that the semimeasure or supergale succeed on **all** elements of $X$.

:::{prf:definition}
Let $M$ be a lower-semicomputable continuous mesh semimeasure on $\mathcal{N}$. For any index $i \in \omega$, define its **a priori mesh complexity under $M$** as follows:

$$
\begin{aligned}
\operatorname{KM}_M(i) := - \log M(i),
\end{aligned}
$$

or $+\infty$ whenever $M(i) = 0$. Call $\operatorname{KM} \equiv \operatorname{KM}_{\mathbf{M}}$ the **a priori mesh complexity**.
:::

Again, this notion of complexity depends on the $\omega$-presentation $\mathscr{R}$ of $\mathcal{N}$.

Note too that $\operatorname{KM}$ has an **invariance** property, stating that any optimal element of $\mathcal{M}$ defines the same **a priori** complexity notion up to an additive constant. Compare this to the invariance of the prefix complexity $K$ up to the choice of universal prefix machine.

## Discrete Mesh Semimeasures

:::{prf:definition}
A function $m: \omega \to [0, 1]$ is a **discrete semimeasure** on $(\Omega, \mathcal{N})$ if it satisfies:

```{math}
:label: eqn:discrete_mesh_semimeasure_condition
\begin{aligned}
\sum_{i \in \omega} m(i) \leq 1.
\end{aligned}
```
:::

In words, the **discrete semimeasure condition** in ([%s](#eqn:discrete_mesh_semimeasure_condition)) simply asks there not be more than unit mass distributed across the countably many mesh elements. We might refer to a discrete semimeasure defined on the $\iota$-indices of the mesh $\mathcal{N}$ to be a **discrete mesh semimeasure** with respect to $\mathcal{N}$.

As in the continuous case, a discrete mesh semimeasure $m$ on $(\Omega, \mathcal{N}, \mathscr{R})$ is **lower-semicomputable** if its lower-graph is computably enumerable relative to the given $\omega$-presentation $\mathscr{R}$. Collect into $\mathfrak{m}$ all the lower-semicomputable discrete mesh semimeasures in $\mathcal{N}$ with respect to the given $\omega$-presentation $\mathscr{R}$. Then, a discrete semimeasure from $\mathfrak{m}$ is **optimal** if it multiplicatively dominates all other semimeasures from $\mathfrak{m}$.

:::{prf:theorem}
:label: prop:exists_optimal_discrete
Over a given represented mesh space $(\Omega, \mathcal{N}, \mathscr{R})$, there exists an optimal lower-semicomputable discrete mesh semimeasure.
:::

Again, we loosely follow the proof structure from Li and Vitányi's Theorem 4.3.1, which shows the existence of an optimal lower-semicomputable discrete semimeasure over some finitely-branching sequence space {cite:p}`LV08`.

::::{prf:proof}
:nonumber:
We build our optimal element using left-approximators to the discrete semimeasures in $\mathfrak{m}$. In the first step of the construction, we obtain an enumeration of left-approximators $\widehat{f}$ to the non-negative, lower-semicomputable maps $f \geq 0$. Then, in the next step, each $\widehat{f}$ is turned into a left-approximator for some lower-semicomputable discrete mesh semimeasure. Finally, we take a weighted sum of all these left-approximators to the elements of $\mathfrak{m}$; this defines a computable map which left-approximates an optimal element of $\mathfrak{m}$.

First, note that it is possible to enumerate all $\mathscr{R}$-computable functions of the form $\phi : \omega^2 \to \mathbb{Q} \cap [0, +\infty)$. For any lower-semicomputable map $f: \omega \to [0, \infty)$, the discussion in Section [%s](#section:Computability_Theory) guarantees that at least one of the $\phi$ above will left-approximate $f$.

Next, use a given $\phi$ to define another map $\psi : \omega^2 \to \mathbb{R}$ meant to be a left-approximator to some semimeasure in $\mathfrak{m}$. By dovetailing this staged process across the enumeration of all $\phi$, we will have described a uniform algorithm for approximating all elements of $\mathfrak{m}$ from below (computably in $\mathscr{R}$), exactly what is needed for building an optimal element of $\mathfrak{m}$.

:::{div}
:class: pseudocode
Stage $r = 0$:\
  Initialize $\psi(i, 0) = 0$ for all $i \in \omega$;\
Stage $r > 0$:\
  If $\phi(0, r) + \cdots + \phi(r - 1, r) > 1$:\
    Set $\psi(i, r) = \psi(i, r - 1)$ for all $i \in \omega$;\
  Else:\
    Set $\psi(i, r) := \phi(i, r)$ for all $i \in \omega$;\

:::

In words, for a given stage $r > 0$, we only update $\psi$ when $\phi(\cdot, r)$ assigns no more than unit mass across the mesh elements. Otherwise, we carry over the values of $\psi(\cdot, r - 1)$ from the previous stage.

If at any stage the construction attempts to assign more than unit mass across the mesh elements, the resulting $\psi$ will not be updated beyond that stage. Such a map will trivially satisfy $\psi(\cdot, r) : \omega \to \mathbb{R}$ being a discrete mesh semimeasure for each $r \in \omega$.

Otherwise, the map $\psi$ is updated successfully at each stage. We that that the limiting map $m_\phi : i \mapsto \lim_{r \to \infty} \psi(i, r)$ is a discrete mesh semimeasure on $\mathcal{N}$.

Furthermore, for a given $m \in \mathfrak{m}$, there exists an $\mathscr{R}$-computable left-approximator $\phi$ to $m$ where each map $i \mapsto \phi(i, r)$ is itself a discrete mesh semimeasure. In that case, the resulting map $\psi = \phi$, and so $m_\phi = m$ is the limiting map from this construction. Therefore, we have an algorithm for left-approximating all the elements of $\mathfrak{m}$. Call $(\psi_n)_{n \in \omega}$ the enumeration of all $\mathscr{R}$-computable left-approximators constructed from our enumeration $(\phi_n)_{n \in \omega}$ of all maps $\phi$, and $(m_n)_{n \in \omega}$ the corresponding enumeration of all their limiting maps.

We now build another $\mathscr{R}$-computable map $\boldsymbol{\psi}$ as follows:

$$
\begin{aligned}
\boldsymbol{\psi} : \omega^2 \to \mathbb{Q} \cap [0,1], \qquad \boldsymbol{\psi}(i, r) := \sum_{n < r} \frac{\psi_n(i, r)}{2^{n + 1}},
\end{aligned}
$$

This map $\boldsymbol{\psi}$ is the left-approximator of some lower-semicomputable map $\mathbf{m}$ which satisfies:

$$
\begin{aligned}
\mathbf{m}: \omega \to [0, 1], \qquad \mathbf{m}(i) := \sum_n \frac{m_n(i)}{2^{n + 1}}.
\end{aligned}
$$

We see that $\mathbf{m}$ is a discrete mesh semimeasure on $\mathcal{N}$ because for any $i \in \omega$,

$$
\begin{aligned}
\sum_i \mathbf{m}(i) = \sum_i \sum_n \frac{m_n(i)}{2^{n + 1}} = \sum_n \frac{1}{2^{n + 1}} \sum_i m_n(i) \leq \sum_n \frac{1}{2^{n + 1}} \cdot 1 \leq 1.
\end{aligned}
$$

Finally, we check that $\mathbf{m}$ is optimal. Fix $m \in \mathfrak{m}$, and let $n \in \omega$ be its index in the enumeration of $\mathfrak{m}$, giving $m \equiv m_n$. Thus, for any $i \in \omega$,

$$
\begin{aligned}
m(i) = m_n(i) \leq 2^{n + 1} \cdot \mathbf{m}(i).
\end{aligned}
$$
::::
