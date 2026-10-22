---
title: "Subsets of Exact Measure"
label: section:subsets_of_exact_measure
---

A standard result in geometric measure theory is one by A. Besicovitch regarding for each closed set in Euclidean space of positive $\mathcal{H}^s$-measure finding a subset whose $\mathcal{H}^s$-measure is non-zero and finite {cite:p}`Bes52`. The result was quickly shown to hold more generally for analytic (or Souslin) sets by R. Davies {cite:p}`Dav52`. Such a result is trivial when $s$ equals the full dimension of the ambient space, since then $\mathcal{H}^s$ is a constant multiple of Lebesgue measure on that space. Without such a correspondence for smaller values of $s$, one must get around the fact that not all sets of infinite $\mathcal{H}^s$-measure are $\sigma$-finite for $\mathcal{H}^s$ (i.e., are not the countable union of subsets of finite $\mathcal{H}^s$-measure). Besicovitch circumvents this by using a net measure constructed over the net of dyadic cubes $\mathcal{Q}^m$ over Euclidean space $\mathbb{R}^m$ which is comparable to $\mathcal{H}^s$. As discussed in Chapter [%s](#chapter:AIT_on_Net_Spaces), D. Larman extended nets and net measures to generic metric spaces {cite:p}`Lar67`. Soon after, C. Rogers and Davies managed to extend Besicovitch's result on the existence of finite measure subsets to compact subsets of a net space under some weak assumptions about the net and net measure {cite:p}`Rog70`, presented below:

::::{prf:theorem} Theorem 54 of {cite:t}`Rog70`
:label: theorem:besicovitch_by_rogers_for_nets
Let $\mathcal{N}$ be a Rogers net on a metric space $(\Omega, d)$, and $\rho$ be a net premeasure for $\mathcal{N}$. Suppose further that

:::{div}
:class: roman-list
1. $\rho$ is finite-valued on $\mathcal{N}$,
1. Each $x \in \Omega$ is $\mathcal{H}^\rho$-finite, and
1. If $(F_n)_{n \in \infty}$ is a decreasing sequence of compact subsets of $\Omega$ with $\mathcal{H}^\rho\p{\bigcup_n F_n} = 0$, it holds for each $\delta > 0$ that $\mathcal{H}^\rho_\delta(F_n) \to 0$ as $n \to \infty$.
:::

Then, any compact set $F \subseteq \Omega$ with positive $\mathcal{H}^\rho$-measure contains a subset of positive, finite $\mathcal{H}^\rho$-measure.
::::

Rogers and Davies used their Increasing Sets Lemma [%s](#theorem:increasing_sets_lemma) and stability result [%s](#theorem:stability_for_net_measures) to prove Theorem [%s](#theorem:besicovitch_by_rogers_for_nets).

The goal of the present section is to obtain a stronger result for a slightly more restricted class of nets and net measures. In particular, we will prove a density result which applies to any finitely-branching, layered-disjoint net with consistently shrinking diameters across the rank levels and which generates the topology of the full space. And this result will apply for any Hausdorff net premeasure (i.e., net premeasure induced by a dimension function in the sense of Section [%s](#section:Measures_and_Hausdorff_Dimension)). We originally obtained the result over Cantor space by translating Besicovitch's original argument to the tree-representations of $\boldsymbol{\Pi}^0_1$-classes. This proof method then generalized to net spaces with the properties stated above.

:::{prf:definition}
Call a net $\mathcal{N}$ on a metric space $(\Omega, d)$ **scaling** if there exists a monotonically-decreasing function $\mathsf{d} : \omega \to (0, +\infty]$ with $\mathsf{d}(r) \to 0$ as $r \to \infty$ such that $\operatorname{rk}(N) = r$ implies $\operatorname{diam}(N) = \mathsf{d}(r)$.
:::

Many standard examples of nets are scaling, including the net of dyadic cubes $\mathcal{Q}^m$ on $\mathbb{R}^m$ with $\mathsf{d}(r) = \sqrt{m} \cdot 2^{-r}$, or the net of cylinder sets $\mathcal{B}$ on $2^\omega$ with $\mathsf{d}(r) = 2^{-r}$. Notice as well that the Rogers net guaranteed in Theorem [%s](#thm:Larman_net_on_finite_dimensional_compact_metric) for a compact metric space is also scaling for $\mathsf{d}(r) = 2^{-r}$.

:::{prf:definition}
For a fixed $0 < b \in \omega$, a net $\mathcal{N}$ on a metric space $(\Omega, d)$ is **$b$-branching** if $\mathcal{N}$ has a single root and each net element has exactly $b$-many children.
:::

Any $b$-branching net admits an indexing $\mathcal{N} = \set{N_\sigma}{\sigma \in b^{<\omega}}$ respecting the containment relation, following the addresses in the associated graph $\mathcal{G}$ as in Proposition [%s](#prop:tree_characterization_of_net).

A collection of subsets of a topological space $\Omega$ is said to be a **subbasis of $\Omega$** if it generates the same topology on $\Omega$. So, a net $\mathcal{N}$ is a subbasis of $(\Omega, d)$ whenever the topology it generates on $\Omega$ is compatible with the topology induced by the metric $d$.

Let $\mathcal{N}$ be a scaling, $b$-branching, layered-disjoint net on $(\Omega, d)$ with Hausdorff net premeasure $\rho_h$ based on a dimension function $h$. Suppose $F \subseteq \Omega$ is a non-empty, compact class.

As $F$ is compact and $\mathcal{N}$ is $b$-branching, the net axioms (**M3**) and (**N4**$'$) guarantee that we may represent $F$ as the set of paths through a tree $T_F \subseteq b^{<\omega}$. That is, it holds that any $x \in F$ may be uniquely associated with the path-wise intersection $\bigcap_{\sigma \in p} N_\sigma$, where $p \in [T_F]$ and $N_\sigma \in \mathcal{N}$ is the net element at address $\sigma \in b^{<\omega}$ in the associated graph $\mathcal{G}$.

Using $T_F$, we may represent the set of all non-empty, compact subclasses of $F$ as its own $\boldsymbol{\Pi}^0_1$-class $\mathcal{P}_F \subseteq 2^{\omega}$. To do this, we define the tree $T_{\mathcal{P}} \subseteq 2^{<\omega}$ coding $\mathcal{P}_F$ as follows. Identify $2^{<\omega}$ with $\omega$ using a standard computable bijection with the property that for each $n \in \omega$, all strings in $b^{<\omega}$ of length $n$ are enumerated before those of length $n + 1$. For any $\zeta \in 2^{<\omega}$, define $\zeta \in T_{\mathcal{P}}$ if $\zeta$ satisfies the following conditions for all $\sigma \in b^{<\omega}$ with $\zeta(\sigma) = 1$:

:::{div}
:class: roman-list
1. $\zeta(\tau) = 1$ for all $\tau \preceq \sigma$,
1. $\sigma \in T_F$,
1. If $\zeta$ is defined on all immediate successors $\sigma^\smallfrown i$ where $i \in \seq{0, ..., b - 1}$, then $\zeta(\sigma^\smallfrown i) = 1$ for at least one choice of $i$.
:::

It is straightforward to verify that these conditions make $T_{\mathcal{P}}$ a tree. Take any infinite path $Z \in [T_{\mathcal{P}}]$ through $T_{\mathcal{P}}$, and associate to it the set $T_Z = \set{\sigma \in b^{<\omega}}{Z(\sigma) = 1}$. By condition (i) above, $T_Z$ is a tree. By condition (ii), $T_Z$ is a sub-tree of $T_F$. And by condition (iii), $T_Z$ is pruned (i.e., each elements of $T_Z$ has a proper extension in $T_Z$). Further associate to $Z$ the compact set $E_Z \subseteq \Omega$ defined by

$$
\begin{aligned}
x \in E_Z \iff (\exists p \in [T_Z]) \brk{\bigcap_{\sigma \in p} N_\sigma = \seq{x}}.
\end{aligned}
$$

For any $Z \in [T_{\mathcal{P}}]$, since $T_Z$ is a pruned sub-tree of $T_F$ and $F$ is compact, the associated set $E_Z$ is a non-empty, compact subset of $F$. And any non-empty, compact subset of $F$ may be represented by an infinite, pruned sub-tree of $T_F$, so we have our desired correspondence: $\mathcal{P}_F = [T_{\mathcal{P}}]$.

This representation helps to prove the following result.

:::{prf:theorem}
:label: theorem:existence_of_compact_subset_exact_for_premeasure
Let $\mathcal{N}$ be a scaling, $b$-branching, layered-disjoint net and subbasis on $(\Omega, d)$ and having net Hausdorff premeasure $\rho$. Suppose $F \subseteq \Omega$ is compact with $(\restrict{\mathcal{H}}{\mathcal{N}})^\rho(F) = +\infty$. Then there exists a compact subset $E \subseteq F$ of arbitrarily large, finite $(\restrict{\mathcal{H}}{\mathcal{N}})^\rho$-measure.
:::

Any class $F$ with $(\restrict{\mathcal{H}}{\mathcal{N}})^\rho(F) > 0$ is certainly non-empty, so we may construct the associated class $\mathcal{P}_F$ as described above. Since $2^{\omega}$ is a complete metric space and $\mathcal{P}_F \subseteq 2^{\omega}$ is closed, $\mathcal{P}_F$ may be viewed as a complete metric space in its own right.

Our general outline will now be as follows:

:::{div}
:class: arabic-list
1. Find a non-empty, compact subset $\mathcal{S} \subseteq \mathcal{P}_F$ such that if $Z \in \mathcal{S},$ then the associated subclass $E_Z \subseteq F$ satisfies $(\restrict{\mathcal{H}}{\mathcal{N}})^\rho(E_Z) > 0$.
1. Find a countable sequence of non-empty, open sets $(\mathcal{U}^c_n)_n$ in $\mathcal{P}_F$ such that if $Z \in \bigcap_{n \in \omega} \mathcal{U}^c_n$, then the associated subclass $E_Z \subseteq F$ satisfies $(\restrict{\mathcal{H}}{\mathcal{N}})^\rho(E_Z) < +\infty$.
1. Show that each $\mathcal{U}^c_n$ is dense in the induced subspace $\mathcal{S} \subseteq \mathcal{P}_F$.
:::

Since $\mathcal{P}_F$ is complete, the closed subspace $\mathcal{S}$ in (1) will also be complete. And if each $\mathcal{U}^c_n$ is indeed dense in $\mathcal{S}$, then by the Baire Category Theorem, the intersection $\bigcap_{n \in \omega}\mathcal{U}^c_n$ will be dense in $\mathcal{S}$ as well. In particular, $\mathcal{S} \cap \bigcap_{n \in \omega}\mathcal{U}^c_n$ will be non-empty, and for any $Z$ in this intersection, the associated subclass $E_Z \subseteq F$ will satisfy $0 < (\restrict{\mathcal{H}}{\mathcal{N}})^\rho(E_Z) < +\infty$, as desired.

Suppose $U \subseteq b^{<\omega}$. Understand $\operatorname{DW}_\rho(U)$ to evaluate the direct $\rho$-weight of the collection of net elements $\set{N_\sigma}{\sigma \in U}$ whose addresses are in $U$.

For any natural numbers $n \leq m$, define a function $\phi_{n, m}: \mathcal{P}_F \to \mathbb{R}$ as follows:

$$
\begin{aligned}
\phi_{n, m}(Z) = \min_{U \subseteq b^{<\omega}} \set{\operatorname{DW}_\rho(U)}{(\forall \sigma \in U)\brk{n \leq \operatorname{len}(\sigma) \leq m} \text{ and } (\forall \sigma \in T_Z)(\exists \tau \in U)[\tau \preceq \sigma]}.
\end{aligned}
$$

That is, $\phi_{n, m}(Z)$ is defined as the minimum direct $\rho$-weight of any cover $U \subseteq b^{<\omega}$ of $[T_Z]$ by strings of length between $n$ and $m$, inclusive. There are only finitely many $U$ considered in the computation of $\phi_{n, m}(Z)$. Since $\mathcal{N}$ is scaling, any such sequence $U$ covering $[T_Z]$ may also be viewed as giving the minimal direct $\rho$-weight cover of $E_Z$ by net elements having diameter between $\mathsf{d}(m)$ and $\mathsf{d}(n)$, inclusive.

Fixing $c > 0$, define for each $n \in \omega$ the set

$$
\begin{aligned}
\mathcal{U}^c_n := \set{Z \in \mathcal{P}_F}{(\exists m \geq n)[\phi_{n, m}(Z) < c]}.
\end{aligned}
$$

For each $n \in \omega$, it only takes finitely bits of $Z$ to determine whether $\phi_{n, m}(Z) < c$, so each $\set{Z}{\phi_{n, m}(Z) < c}$ is clopen in the product topology of $2^\omega$. As the union of all such sets for $m \geq n$ intersected with $\mathcal{P}_F$, the set $U^c_n$ is open in $\mathcal{P}_F$. Moreover, each $U^c_n$ is non-empty, for if $Z \in \mathcal{P}_F$ codes the singleton set $E_Z = \seq{x}$, then since $\mathcal{N}$ is scaling, we have $\phi_{n, m}(Z) = h(\mathsf{d}(m))$, as witnessed by the unique length-$m$ string $\sigma$ with $Z(\sigma) = 1$. So, pick $m \gg n$ large enough so that $h(\mathsf{d}(m)) < c$ to witness that $Z \in \mathcal{U}^c_n$.

Finally, we observe that if $Z \in \bigcap_{n \in \omega}\mathcal{U}^c_n$ with $c > 0$ being fixed, then $(\restrict{\mathcal{H}}{\mathcal{N}})^\rho(E_Z) \leq c < +\infty$. Indeed, take any $\delta > 0$, and consider $n \in \omega$ for which $\mathsf{d}(n) < \delta$. By definition of $Z \in \mathcal{U}^c_n$, there is some $m \geq n$ for which $\phi_{n, m}(Z) < c$, implying there exists a $\mathsf{d}(n)$-cover of $E_Z$ using only elements of $\mathcal{N}$ and of direct $\rho$-weight less than $c$. Thus $(\restrict{\mathcal{H}}{\mathcal{N}})^\rho_\delta(E_Z) < c$. Taking the limit as $\delta \to 0$ gives $(\restrict{\mathcal{H}}{\mathcal{N}})^\rho(E_Z) \leq c$.

We now define the set $\mathcal{S}$ to witness being of positive $(\restrict{\mathcal{H}}{\mathcal{N}})^\rho$-measure. For each $c > 0$ and $n \in \omega$, define the set:

$$
\begin{aligned}
\mathcal{S}^c_n := \mathcal{P}_F \setminus \mathcal{U}^c_n = \set{Z \in \mathcal{P}_F}{(\forall m \geq n) [\phi_{n,m}(Z) \geq c]}.
\end{aligned}
$$

Note that each $\mathcal{S}^c_n$ is closed in $\mathcal{P}_F$ as the complement of $U^c_n$ in $\mathcal{P}_F$.

:::{prf:lemma}
:label: lemma:Hausdorff_measure_characterization_of_S_c_n
For any $Z \in \mathcal{P}_F$, $c > 0$, and $n \in \omega$,

$$
\begin{aligned}
(\restrict{\mathcal{H}}{\mathcal{N}})^\rho_{\mathsf{d}(n)}(E_Z) \geq c \iff Z \in \mathcal{S}^c_n.
\end{aligned}
$$
:::

:::{prf:proof}
:nonumber:
Suppose $(\restrict{\mathcal{H}}{\mathcal{N}})^\rho_{\mathsf{d}(n)}(E_Z) \geq c$. Then, any $\mathsf{d}(n)$-cover of $E_Z$ by net elements has direct $\rho$-weight at least $c$. By definition and the assumption that $\mathcal{N}$ is scaling, this includes all covers by net elements with addresses of length at least $n$. So, for any $m \geq n$, we have $\phi_{n, m}(Z) \geq c$, hence $Z \in S^c_n$.

In the reverse direction, assume $Z \in S^c_n$. Consider an arbitrary $\mathsf{d}(n)$-cover $U$ of $E_Z$ by net elements. Since $E_Z$ is compact, it follows by $\mathcal{N}$ being a subbasis of $(\Omega, d)$ that this cover has a finite subcover $U' = \seq{\sigma_1, ..., \sigma_t }$. Since $\mathcal{N}$ is scaling, each $\sigma_i \in b^{<\omega}$ is of length $\operatorname{len}(\sigma_i) \geq n$. Call $m$ the maximum length of all such $\sigma_i$. Without loss of generality, $U'$ may be restricted to just those $\sigma_i$ with an extension in $T_Z$, for any $\sigma_i$ without this property would not be needed in the cover of $E_Z$ and could thus be deleted from $U'$.

We claim that $U'$ is one of the covers considered in computing $\phi_{n, m}(Z)$. Indeed, since $Z$ codes a pruned tree, any $\sigma \in b^m$ with $Z(\sigma) = 1$ must have some extension in $E_Z$, which in turn must have some prefix $\sigma_i \in U'$ as $U'$ is a cover of $E_Z$ containing strings of length at most $m$.

So, by the assumption that $\phi_{n, m}(Z) \geq c$, it follows that $\operatorname{DW}_\rho(U') \geq c$. And, by monotonicity, the original cover $U$ of $E_Z$ must also have $\operatorname{DW}_\rho(U) \geq c$. Since this $\mathsf{d}(n)$-cover by net elements was arbitrary, we may conclude $(\restrict{\mathcal{H}}{\mathcal{N}})^\rho_{\mathsf{d}(n)}(E_Z) \geq c$, as claimed.
:::

By the assumption $(\restrict{\mathcal{H}}{\mathcal{N}})^\rho(F) = +\infty$, we have that for any $c > 0$ it must be $(\restrict{\mathcal{H}}{\mathcal{N}})^\rho_{\mathsf{d}(n)}(F) \geq c$ for all sufficiently large $n \gg 1$. Thus, by Lemma [%s](#lemma:Hausdorff_measure_characterization_of_S_c_n), the pruned tree representation of $F$ itself will be an element of all the classes $\mathcal{S}^c_n$, witnessing these classes to be non-empty.

Thus, to conclude Theorem [%s](#theorem:existence_of_compact_subset_exact_for_premeasure), it will suffice to show the following.

:::{prf:proposition}
:label: proposition:full_density_of_U_and_S
Let $0 < d < c,$ and let $n_0 \in \omega$ be such that $\mathcal{S}^d_{n_0}$ is non-empty. Then, for all $n \in \omega$, the set $\mathcal{U}^c_n$ is dense in $\mathcal{S}^d_{n_0}$.
:::

This result relies on a Baire Category argument, and points to a forcing notion.

Now, before we can prove Proposition [%s](#proposition:full_density_of_U_and_S), let us first focus on the case when the indices of these classes agree.

:::{prf:lemma}
:label: lemma:density_of_U_and_S_same_indices
Let $0 < d < c$, and let $n \in \omega$ be fixed. If $\mathcal{S}^d_n$ is non-empty, then $\mathcal{U}^c_n$ is dense in $\mathcal{S}_n^d$.
:::

::::{prf:proof}
:nonumber:
Fix a finite binary string $\zeta \in 2^{< \omega}$ having an infinite extension $Z \in \mathcal{S}^d_n$. We claim that $\zeta$ also has an extension in $\mathcal{U}^c_n \cap \mathcal{S}^d_n$. Without loss of generality, we may assume that $\zeta$ is defined for all strings of a fixed length $n' \geq n$ by extending $\zeta$ along $Z$. Call $k$ the number of length-$n'$ strings $\sigma$ for which $Z(\sigma) = 1$, and $\varepsilon := c - d > 0$. Choose $m \geq n'$ sufficiently large so that $h(\mathsf{d}(m)) < \min\seq{c / k, \varepsilon}$. And define $Y_0 \in \mathcal{P}_F$ to be an infinite binary string such that for all $\sigma \in b^{<\omega}$:

:::{div}
:class: roman-list
1. When $\operatorname{len}(\sigma) \leq n'$, set $Y_0(\sigma) = Z(\sigma)$,
1. When $n' < \operatorname{len}(\sigma) \leq m$, set $Y_0(\sigma) = 1$ if and only if $\sigma$ is the lexicographically-least of all extensions $\nu \succeq \restrict{\sigma}{n'}$ such that $Z(\nu) = 1$, and
1. When $\operatorname{len}(\sigma) > m$, set $Y_0(\sigma) = 1$ if and only if both $Y_0(\restrict{\sigma}{m})$ and $Z(\sigma) = 1$.
:::

It is straightforward to check that $Y_0$ satisfies all of the conditions for being in $\mathcal{P}_F$. Observe that by condition (ii), we will have exactly $k$ strings $\sigma$ of length $m$ for which $Y_0(\sigma) = 1$, since each of the $k$-many length-$n'$ strings represented in $Z$ will yield exactly one extension. Taking $U$ to consist of exactly these $k$ extensions of length $m$, then $\operatorname{DW}_\rho(U) = k \cdot h(\mathsf{d}(m)) < c$. This witnesses that $\phi_{n, m}(Y_0) < c$, and thus $Y_0 \in \mathcal{U}^c_n$. Note that $Y_0 \in [\zeta]$ by condition (i).

If $Y_0$ is also in $\mathcal{S}^d_n$, then we are done. Otherwise, let $\seq{\sigma_1, \dots , \sigma_t}$ be an enumeration of all of the strings in $b^m$ for which $Y_0(\sigma) = 0$ yet $Z(\sigma) = 1$. At least one such string exists, or else, $Y_0 = Z$, but $Z \in \mathcal{S}^d_n$.

Inductively define the infinite binary strings $Y_1, \dots, Y_t$ in $\mathcal{P}_F \cap [\zeta]$ as follows, where $0 \leq i < t$:

- If $Y_i(\sigma) = 1$, set $Y_{i + 1}(\sigma) = 1$, or
- If $Y_i(\sigma) = 0$, set $Y_{i + 1}(\sigma) = 1$ if and only if both $\sigma || \sigma_{i + 1}$ and $Z(\sigma) = 1$.

Again, it is straightforward to verify that these $Y_i$ are in fact elements of $\mathcal{P}_F \cap [\zeta]$. We also have that $Y_t = Z$, since any string $\sigma \in T_Z$ must be compatible either with something in $T_{Y_0}$ or with one of the strings from $\seq{\sigma_1, \dots , \sigma_t}$.

We claim that $Y_i$ must be in both $\mathcal{S}_n^d$ and $\mathcal{U}^c_n$ for some $1 \leq i \leq t$. For a fixed $m' \geq m$, consider the values of $\phi_{n, m'}(Y_0), \phi_{n, m'}(Y_1), \dots, \phi_{n, m'}(Y_t)$. We have that $\phi_{n, m'}(Y_0) < c$, since $\phi_{n, m}(Y_0) < c$ and $\phi$ is monotonically-decreasing in its second coordinate. We also have that $\phi_{n, m'}(Y_t) = \phi_{n, m'}(Z) \geq d$ by assumption. Moreover, we observe for each $0 \leq i < t$ that

$$
\begin{aligned}
\phi_{n, m'}(Y_i) \leq \phi_{n, m'}(Y_{i + 1}) < \phi_{n, m'}(Y_i) + \varepsilon.
\end{aligned}
$$

The first inequality follows from the fact that $Y_i(\sigma) = 1$ implies $Y_{i + 1}(\sigma) = 1$. So any valid cover for computing $\phi_{n, m'}(Y_{i + 1})$, after deleting any strings not present in $T_{Y_i}$, gives a cover for $Y_i$ of no greater direct $\rho$-weight, hence valid in computing $\phi_{n, m'}(Y_i)$. The second inequality follows from the fact that if $U$ is the minimal cover whose direct $\rho$-weight witnesses $\phi_{n, m'}(Y_i)$, then adding $\sigma_i$ to this cover would give a cover valid in computing $\phi_{n, m'}(Y_{i + 1})$. Thus, by the choice of $m$,

$$
\begin{aligned}
\phi_{n, m'}(Y_{i + 1}) \leq \phi_{n, m'}(Y_i) + h(\mathsf{d}(m)) < \phi_{n, m'}(Y_i) + \varepsilon.
\end{aligned}
$$

It follows that one of the values

$$
\begin{aligned}
\phi_{n, m'}(Y_0), \phi_{n, m'}(Y_1), ..., \phi_{n, m'}(Y_t),
\end{aligned}
$$

falls in the range $[d, d + \varepsilon) = [d, c)$, as $\phi_{n, m'}(Y_0) < c$ and $\phi_{n, m'}(Y_t) \geq d$. Let $Y^{(m')}$ denote the first element $Y_i$ for which $\phi_{n, m'}(Y_i) \in [d, c)$. Since we only have finitely many $Y_i$ to consider, at least one $Y_i$ must appear as $Y^{(m')}$ for infinitely many $m' \geq m$. For such a $Y_i$, we have $Y_i \in \mathcal{U}^c_n$, as any of these $m' \geq m \geq n$ will work as a witness for $\phi_{n, m'}(Y_i) < c$. But since we can find arbitrarily large values of $m' \geq n$ for which $\phi_{n, m'}(Y_i) \geq d$, it follows by monotonicity that we in fact have $\phi_{n, m'}(Y_i) \geq d$ for all $m' \geq n$, giving $Y_i \in \mathcal{S}^d_n$, as desired.
::::

Returning to Proposition [%s](#proposition:full_density_of_U_and_S), by induction it now suffices to prove that if $\mathcal{U}^c_n$ is dense in $\mathcal{S}_{n_0}^d$ for some $n \geq n_0$, we also must have $\mathcal{U}_{n + 1}^c$ being dense in $\mathcal{S}_{n_0}^d$. To do this, we would want to be able to pass from a cover witnessing $Z \in \mathcal{U}^c_n$ to a cover witnessing $Z \in \mathcal{U}^c_{n + 1}$. Of course, the length-$n$ strings in that original cover will need to be replaced by proper extensions. The following definitions identify strings which can be replaced without significantly increasing the direct $\rho$-weight of the cover.

:::{prf:definition}
Let $Z \in \mathcal{P}_F$ and $\tau \in b^{<\omega}.$ Then $Z^{\tau} \in \mathcal{P}_F$ denotes the infinite binary string defined by $Z^{\tau}(\sigma) = 1$ if and only if $\sigma \mid \mid \tau$ and $Z(\sigma) = 1$.
:::

:::{prf:definition}
Let $Z \in \mathcal{P}_F$ and $n \in \omega$. Define $Z$ to be **$n$-thin** if for every $\tau \in b^n$, we have

$$
\begin{aligned}
\lim_{m \to \infty} \phi_{n+1, m}(Z^\tau) \leq h(\mathsf{d}(n)).
\end{aligned}
$$

And let $\mathcal{T}_n$ denote the set of all $n$-thin sequences.
:::

As we will see, the $n$-thin sequences suffice for passing from $\mathcal{U}^c_n$ to $\mathcal{U}^c_{n+1}$.

:::{prf:lemma}
:label: lemma:use_n_thin_to_pass_n_to_n+1
For all $n \in \omega$ and $c > 0$, we have $\mathcal{U}^c_n \cap \mathcal{T}_n \subseteq \mathcal{U}^c_{n+1}.$
:::

:::{prf:proof}
:nonumber:
Take $Z \in \mathcal{U}^c_n \cap \mathcal{T}_n$, and let $U = \seq{\tau_1, ..., \tau_t}$ be a minimal cover for $Z$ witnessing that $\phi_{n, m}(Z) < c$ for some $m \geq n$.

If all strings in $U$ have length at least $n + 1$, then this cover also witnesses that $\phi_{n+1, m}(Z) < c$, yielding $Z \in \mathcal{U}^c_{n + 1}$, as desired.

Otherwise, assume without loss of generality that there is some $u$ with $1 \leq u \leq t$ for which $\tau_1, \tau_2, ..., \tau_u$ are exactly the strings in $U$ of length $n$. Since $\operatorname{DW}_\rho(U) < c$, we may choose $\varepsilon > 0$ small enough so that we also have $\operatorname{DW}_\rho(U) < c - \varepsilon.$ Since $Z$ is $n$-thin, we may choose $m' \geq m$ so large that for all $\tau_i$ in $U$ of length $n$, we have

$$
\begin{aligned}
\phi_{n+1, m'}(Z^{\tau_i}) < h(\mathsf{d}(n)) + \frac{\varepsilon}{u}.
\end{aligned}
$$

For each $1 \leq i \leq t$, let $V_i$ be a minimizing cover witnessing $\phi_{n + 1, m'}(Z^{\tau_i})$, and let $U'$ be the cover obtained by replacing each string $\tau_i$ in $U$ with the strings from $V_i$. It is straightforward to verify that $U'$ is still a valid cover for computing $\phi_{n+1, m'}(Z)$. And the direct $\rho$-weight of this new cover satisfies:

$$
\begin{aligned}
\operatorname{DW}_\rho(U') &= \sum_{1 \leq i \leq u} \operatorname{DW}_\rho(V_i) + \operatorname{DW}_\rho(\seq{\tau_{u + 1}, ..., \tau_t})\\
&< \sum_{1 \leq i \leq u} \p{h(\mathsf{d}(n)) + \frac{\varepsilon}{u}} + \operatorname{DW}_\rho(\seq{\tau_{u + 1}, ..., \tau_t}) = \operatorname{DW}_\rho(U) + \varepsilon < c.
\end{aligned}
$$

This proves that $Z$ is an element of $\mathcal{U}_{n+1}^c$, as desired.
:::

It remains to show that the $n$-thin elements are sufficiently numerous within each non-empty set $\mathcal{S}^d_{n_0}.$

:::{prf:lemma}
:label: lemma:n_thins_dense_in_complement
Let $d > 0$ and let $n_0 \in \omega$ be such that $\mathcal{S}^d_{n_0}$ is non-empty. Then for all $n \geq n_0$, the set $\mathcal{T}_n$ is dense in $\mathcal{S}^d_{n_0}$.
:::

:::{prf:proof}
:nonumber:
Fix $n \geq n_0$ and a finite binary string $\zeta \in 2^{< \omega}$ having an infinite extension $Z \in \mathcal{S}^d_{n_0}$. We claim that $\zeta$ has an extension in $\mathcal{T}_n \cap \mathcal{S}^d_{n_0}$. Without loss of generality, we may assume that $\zeta$ is defined for all strings of length $n$ by extending $\zeta$ along $Z$. For each $\tau \in b^n$, denote by $\zeta^\tau \in 2^{\operatorname{len}(\zeta)}$ the string defined by

$$
\begin{aligned}
\zeta^\tau(\sigma) = 1 \iff \sigma \mid \mid \tau \text{ and } \zeta(\sigma) = 1.
\end{aligned}
$$

We start by defining an element $Y \in \mathcal{T}_n \cap [\zeta]$, and later check that $Y \in \mathcal{S}^d_{n_0}$, witnessing $\mathcal{T}_n$ being dense in $\mathcal{S}^d_{n_0}$.

To define the element $Y \in \mathcal{P}_F$, it suffices to both specify $Y^\tau$ for each $\tau \in b^n$ and further ensure that each $Y^\tau$ extends $\zeta^\tau$. In this way, the final sequence $Y$ will be well-defined.

If a string $\sigma \in b^{<\omega}$ is compatible with two distinct strings $\tau_1, \tau_2 \in b^n$, then $\sigma$ must be a common prefix for both of these strings, implying $\operatorname{len}(\sigma) < n$. Therefore, $Y(\sigma)$ will be determined by $\zeta(\sigma)$ by the assumption that $\zeta$ is defined on all strings of length up to $n$. It is also straightforward to show that $Y$ will be an element of $\mathcal{P}_F$ so long as each $Y^\tau$ is.

Given $\tau \in b^n$, we say that $\tau$ is **$n$-thin for $Z$** if:

$$
\begin{aligned}
\lim_{m \to \infty} \phi_{n + 1, m}(Z^\tau) \leq h(\mathsf{d}(n)).
\end{aligned}
$$

We further collect into $\mathcal{T}^Z_n \subseteq b^n$ all the $n$-thin strings for $Z$. Now, define $Y^\tau = Z^\tau$ whenever $\tau \in \mathcal{T}^Z_n$. Noting that $\zeta^\tau \preceq Z^\tau$, the claim is satisfied for these $\tau$.

Otherwise, $\tau \not\in \mathcal{T}^Z_n$, so it must be that

$$
\begin{aligned}
\lim_{m \to \infty} \phi_{n + 1, m}(Z^\tau) > h(\mathsf{d}(n)),
\end{aligned}
$$

which, by monotonicity, implies that $\phi_{n + 1, m}(Z^\tau) > h(\mathsf{d}(n))$ for all $m \geq n + 1$, hence $Z^\tau \in \mathcal{S}_{n + 1}^{h(\mathsf{d}(n))}.$

Take $(r_i)_{i \in \omega}$ to be any decreasing sequence of positive real numbers converging to $0$. By Lemma [%s](#lemma:density_of_U_and_S_same_indices), it follows that $\mathcal{U}_{n + 1}^{h(\mathsf{d}(n)) + r_i}$ is dense in $\mathcal{S}_{n + 1}^{h(\mathsf{d}(n))}$ for each $i \in \omega$. And by the Baire Category Theorem, the intersection $\bigcap_i \mathcal{U}_{n + 1}^{h(\mathsf{d}(n)) + r_i}$ is also dense in $\mathcal{S}_{n + 1}^{h(\mathsf{d}(n))}$. And since $\zeta^\tau \preceq Z^\tau \in \mathcal{S}_{n + 1}^{h(\mathsf{d}(n))}$, it follows that $[\zeta^\tau] \cap \mathcal{S}_{n + 1}^{h(\mathsf{d}(n))} \neq \emptyset$. Thus, we may fix a sequence $Y^\tau \in [\zeta^\tau] \cap \mathcal{S}_{n + 1}^{h(\mathsf{d}(n))} \cap \bigcap_i \mathcal{U}_{n + 1}^{h(\mathsf{d}(n)) + r_i}$.

The fact that $Y^\tau \in \mathcal{S}_{n + 1}^{h(\mathsf{d}(n))}$ implies that $\phi_{n + 1, m}(Y^\tau) \geq h(\mathsf{d}(n))$ for all $m \geq n + 1$. Yet, for any $\varepsilon > 0$, one may choose $i \gg 1$ for which $r_i < \varepsilon$. Then, since $Y^\tau \in \mathcal{U}_{n + 1}^{h(\mathsf{d}(n)) + r_i}$, there exists some $m \geq n + 1$ for which

$$
\begin{aligned}
\phi_{n + 1, m}(Y^\tau) < h(\mathsf{d}(n)) + r_i < h(\mathsf{d}(n)) + \varepsilon.
\end{aligned}
$$

So, by the monotonicity of $\phi_{n + 1, m}(Y^\tau)$ in its second component, we conclude that

$$
\begin{aligned}
\lim_{m \to \infty} \phi_{n + 1, m}(Y^\tau) = h(\mathsf{d}(n)).
\end{aligned}
$$

This construction guarantees that $Y$ both extends $\zeta$ and is $n$-thin.

Now we show that $Y$ is indeed an element of $\mathcal{S}_{n_0}^d$, i.e., that $\phi_{n_0, m}(Y) \geq d$ for each $m \geq n_0$. By monotonicity, it suffices to only consider $m \geq n \geq n_0$. Fix such an $m \geq n$ and suppose $U \subseteq b^{<\omega}$ is a cover valid for computing $\phi_{n_0, m}(Y)$. We wish to show that $\operatorname{DW}_\rho(U) \geq d$.

Without loss of generality, we may take $U$ to be prefix-free, for any strings in $U$ having proper prefixes in $U$ may be deleted while maintaining the cover's validity in computing $\phi_{n_0, m}(Y)$ and not increasing the direct $\rho$-weight of the resulting cover. We plan to push the cover $U$ to a cover $U'$ valid instead for computing $\phi_{n_0, m}(Z)$ and satisfying $\operatorname{DW}_\rho(U') \leq \operatorname{DW}_\rho(U)$. Since $Z$ is an element of $\mathcal{S}_{n_0}^d$, this would yield $\operatorname{DW}_\rho(U) \geq \operatorname{DW}_\rho(U') \geq d$, putting $Y \in \mathcal{S}_{n_0}^d$, as $U$ was arbitrary.

Consider all $\tau \in b^n \setminus \mathcal{T}^Z_n$. Denote by $V_\tau$ the collection of all proper extensions of $\tau$ in $U$. If $V_\tau = \emptyset$, do nothing. Otherwise, replace in the cover $U$ all strings in $V_\tau$ by $\tau$ itself. Let us argue why this replacement will not increase the direct $\rho$-weight of the cover.

Note that all strings in $V_\tau$ have length between $n + 1$ and $m$, inclusive. And if $\sigma \in b^m$ is such that $Y^\tau(\sigma) = 1$, then $\sigma$ must extend some element of $V_\tau$. Given that the original set $U$ is a cover for $Y$, we have that $\sigma$ extends some element $\mu \in U$ compatible with $\tau$. If $\mu \preceq \tau$, then $\mu$ would be a proper prefix of any element in $V_\tau$, contradicting the fact that $V_\tau$ was non-empty and $U$ was prefix-free. Therefore, it must be that $\mu \succ \tau$, meaning $\mu \in V_\tau.$ Taken together, we see that $V_\tau$ is valid cover for computing $\phi_{n + 1, m}(Y^\tau)$. Since $\tau \not\in \mathcal{T}^Z_n$, the construction of $Y$ yields that $\phi_{n + 1, m}(Y^\tau) \geq h(\mathsf{d}(n))$, so $\operatorname{DW}_\rho(V_\tau) \geq h(\mathsf{d}(n)).$ So, as $\tau$ has length $n$, replacing all of $V_\tau$ with $\tau$ cannot increase the direct $\rho$-weight of $U$.

Let $U'$ be the cover obtained by performing this replacement for all $\tau \in b^n \setminus \mathcal{T}^Z_n$. It remains to check that $U'$ valid for computing $\phi_{n_0, m}(Z)$. Since the replacement process may only add strings of length $n$, and $n_0 \leq n \leq m$, the sequence $U'$ satisfies the length condition.

For the covering condition, suppose we have a string $\sigma \in b^m$ for which $Z(\sigma) = 1$. Let $\tau = \restrict{\sigma}{n}$. Suppose $\tau \in \mathcal{T}^Z_n$. Then by construction, we have $Y^\tau = Z^\tau$, so $Y^\tau(\sigma) = Z^\tau(\sigma) = 1$. As the original cover $U$ is valid for $\phi_{n_0, m}(Y)$, this implies that $U$ contains some prefix of $\sigma$ compatible with $\tau$. This prefix will still be in $U'$, since we only removed strings which extended elements of $b^n \setminus \mathcal{T}^Z_n$.

Otherwise, $\tau \notin \mathcal{T}^Z_n$. The original cover $U$ is valid for computing $\phi_{n_0, m}(Y)$, and hence valid for $\phi_{n_0, m}(Y^\tau)$, as well. Given that $\phi_{n + 1, m}(Y^\tau) \geq h(\mathsf{d}(n))$, there must be at least one string $\sigma' \in b^m$ such that $Y^\tau(\sigma') = 1$. So, this $\sigma'$ has a prefix $\mu \in U$ compatible with $\tau$. If $\mu \preceq \sigma$, then $\mu$ is also a prefix of $\sigma$ and is not removed when passing to the cover $U'$. Otherwise, $\mu$ **is** removed and replaced with $\tau$. Either way, we get that $U'$ contains a prefix of $\sigma$, completing the argument that $U'$ is a valid cover for computing $\phi_{n_0, m}(Z)$, as desired.
:::

Now we may prove the key density result.

:::{prf:proof} Proof of Proposition [%s](#proposition:full_density_of_U_and_S)
:nonumber:
By Lemma [%s](#lemma:density_of_U_and_S_same_indices) and since the sequence $(\mathcal{U}^c_n)_n$ is nested-decreasing, we get that $\mathcal{U}^c_n$ is dense in $\mathcal{S}^d_{n_0}$ for all $n \leq n_0$.

Assume we have shown that $\mathcal{U}^c_n$ is dense in $\mathcal{S}^d_{n_0}$ for some $n \geq n_0$. We now show that $\mathcal{U}^c_{n + 1}$ is dense in $\mathcal{S}^d_{n_0}$ as well.

Fix a finite binary string $\zeta \in 2^{<\omega}$ having an infinite extension $Z \in \mathcal{S}^d_{n_0} \cap \mathcal{U}^c_n$. Since the set $\mathcal{U}^c_n$ is open, we may choose an extension $\zeta \preceq \zeta' \prec Z$ for which $[\zeta'] \cap \mathcal{S}^d_{n_0} \subseteq \mathcal{U}^c_n$. Now, as $[\zeta'] \cap \mathcal{S}^d_{n_0} \neq \emptyset$ ($Z$ is contained in their intersection), Lemma [%s](#lemma:n_thins_dense_in_complement) implies there exists an $n$-thin sequence $Y \in [\zeta'] \cap \mathcal{S}^d_{n_0} \cap \mathcal{T}_n$. And by the choice of $\zeta'$, we have $Y \in \mathcal{T}_n \cap \mathcal{U}^c_n$, so by Lemma [%s](#lemma:use_n_thin_to_pass_n_to_n+1), $Y \in \mathcal{U}^c_{n + 1}$. This shows that $\mathcal{U}^c_{n + 1}$ is dense in $\mathcal{S}^d_{n_0}$. The result now follows by induction.
:::
