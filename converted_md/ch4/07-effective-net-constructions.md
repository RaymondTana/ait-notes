---
title: "Effective Net Constructions"
label: section:Effective_Constructions_on_Net_Spaces
---

In {cite:t}`Rog70`, Rogers and Davies summarize a number of results on the existence of nets on certain classes of metric spaces, some of which further admit net measures comparable with the Hausdorff premeasures.

## Revisiting Examples

The first example in {cite:t}`Rog70` is due to A. Besicovitch.

:::{prf:theorem} Theorem 49 of {cite:t}`Rog70`
:label: thm:Theorem_49_Euclidean_comparability
There exists a net on Euclidean space $\mathbb{R}^m$ such that for any dimension function $h$, there exists a net premeasure $\rho$ on $\mathcal{N}$ satisfying:

$$
\begin{aligned}
\mathcal{H}^{\rho_h}_\delta(X) \leq \mathcal{H}^\rho_\delta(X) \leq 3^m 2^{m(m + 1)} \mathcal{H}^{\rho_h}_\delta(X),
\end{aligned}
$$

for all $\delta \in (0, 1)$ and all subsets $X \subseteq \mathbb{R}^m$. Furthermore,

$$
\begin{aligned}
\mathcal{H}^{\rho_h}(X) \leq \mathcal{H}^\rho(X) \leq 3^m 2^{m(m + 1)} \mathcal{H}^{\rho_h}(X),
\end{aligned}
$$

for all subsets $X \subseteq \mathbb{R}^m$.
:::

The proof for Theorem [%s](#thm:Theorem_49_Euclidean_comparability) simply makes use of the prototypical dyadic net $\mathcal{Q}^m$ used in Example [%s](#example:euclidean_has_dyadic_net): on any $Q \in \mathcal{Q}^m_r$ with side-length $2^{-r}$, define the net premeasure $\rho$ as follows:

$$
\begin{aligned}
\rho(Q) := h(\diam_d(Q)) = h(\sqrt{m} \cdot 2^{-r}); \quad \rho(\emptyset) := 0.
\end{aligned}
$$

This premeasure is exactly $\rho = \restrict{\rho_h}{\mathcal{Q}^m}$.

The second example concerns separable, ultrametric spaces.

:::{prf:theorem} Theorem 50 of {cite:t}`Rog70`
:label: thm:Theorem_50_ultrametric_comparability
Let $\Omega$ be a separable ultrametric space with no isolated points, and let $h$ be any dimension function. Then there is a net on $\Omega$ and corresponding net premeasure $\rho$ such that:

$$
\begin{aligned}
\mathcal{H}^{\rho_h}_\delta(X) \leq \mathcal{H}^\rho_\delta(X) \leq 2 \mathcal{H}^{\rho_h}_{\delta / 2} (X),
\end{aligned}
$$

for all sufficiently small $\delta > 0$ and for all subsets $X \subseteq \Omega$. Furthermore,

$$
\begin{aligned}
\mathcal{H}^{\rho_h}(X) \leq \mathcal{H}^\rho(X) \leq 2 \mathcal{H}^{\rho_h} (X),
\end{aligned}
$$

for all subsets $X \subseteq \Omega$.
:::

The proof of [%s](#thm:Theorem_50_ultrametric_comparability) constructs a net $\mathcal{N}$ in the same manner as in Example [%s](#example:ultrametric_has_nets) for a fixed dimension function $h$ based on a sequence $(d_i)_i$ converging to zero appropriately slowly for $h$; i.e., satisfying for all $i \in \omega$:

$$
\begin{aligned}
d_{i + 1} > \frac{d_i}{2}, \qquad h(d_{i + 1}) > \frac{h(d_i)}{2},
\end{aligned}
$$

which exists because $h$ is both non-decreasing and continuous on the right. The corresponding net premeasure is simply defined as $\rho(N) := h(\diam_d(N))$ for each $N \in \mathcal{N}$, or $\rho(\emptyset) = 0$. This premeasure is exactly $\rho = \restrict{\rho_h}{\mathcal{N}}$.

## Compact Metric Spaces

Rogers also points to a result by D. Larman in {cite:t}`Lar67` on the existence of nets on “finite-dimensional,” compact metric spaces. For us, Larman's notion of **finite-dimensional** means being $\mathcal{H}^s$-null for some positive integer $s$.

::::{prf:theorem} Theorem 1 of {cite:t}`Lar67`
:label: thm:Larman_net_on_finite_dimensional_compact_metric
Let $(\Omega, d)$ be a compact metric space. Then, there exists a Rogers net $\mathcal{N} = \bigcup_{n = 1}^\infty \mathcal{N}^n$ being a union of layers $\mathcal{N}^n \subseteq \mathcal{P}(\Omega)$ satisfying for each $n \in \omega$:

:::{div}
:class: roman-list
1. There exists a finite collection $I^n \subset \omega^n$ of $n$-tuples such that $\mathcal{N}^n = \set{N(\mathbf{i})}{\mathbf{i} \in I^n}$ under an indexing $N: \bigcup_n I_n \to \mathcal{P}(\Omega)$, where $(i_1, ..., i_{n - 1}, i_n) \in I^n$ implies $(i_1, ..., i_{n - 1}) \in I^{n - 1}$ for any $n > 1$;

1. For all $\mathbf{i}, \mathbf{j} \in I^n$, we have $N(\mathbf{i}) \cap N(\mathbf{j}) \neq \emptyset$ if and only if $\mathbf{i} = \mathbf{j}$;

1. For each $\mathbf{i} \in I^n$, $\diam_d(N(\mathbf{i})) < 2^{-n}$;

1. $\bigcup_{\mathbf{i} \in I^n} N(\mathbf{i}) = \Omega$;

1. If $\mathbf{i} \in I^{n - 1}$, then

   $$
   \begin{aligned}
   \bigcup_{\mathbf{i}^\frown i_n \in I^n} N(\mathbf{i} ^\frown i_n) = N(\mathbf{i});
   \end{aligned}
   $$

1. Each net element of $\mathcal{N}$ is an $F_\sigma$ (i.e., $\mathbf{\Sigma}^0_2$) set.
:::

Moreover, if $\Omega$ is also $\mathcal{H}^s$-null for some positive integer $s$, then this net further satisfies:

:::{div}
:class: labeled-list
- (vii) For any $X \subseteq \Omega$ with $\diam_d(X) < 2^{-(n - 1)}$ for $n > 1$, it takes at most a positive constant $K$ many net elements from $\mathcal{N}^n$ to cover $X$.
:::
::::

:::{prf:lemma}
:label: lemma:Larman_compact_metric_space
Let $(\Omega, d)$ be a compact metric space and fix $r > 0$. Then, there exists a finite collection of points $\seq{x_i \in \Omega: i \in I}$ which are the centers of mutually-disjoint $r$-balls $\seq{B_r(x_i) : i \in I}$ such that their double-radius counterparts cover $\Omega$; i.e.,

$$
\begin{aligned}
\bigcup_{i \in I} B_{2r}(x_i) = \Omega.
\end{aligned}
$$
:::

:::{prf:lemma}
:label: lemma:Larman_beta_spaces
If $(\Omega, d)$ is a compact metric space, then the space is $\mathcal{H}^s$-null for some positive integer $s$ if and only if there exist positive reals $K, \delta, \alpha$ with $\alpha < \frac{1}{2}$ such that if $d \leq \delta$, then at most $K$ many mutually-disjoint, open balls of radius $\alpha \cdot d$ may meet any given open ball of radius $d$. In fact, it suffices to fix $\alpha = 2^{-7}$ and $\delta = 4$.
:::

Larman calls any space satisfying this latter condition a **$\beta$-space** {cite:p}`Lar67`.

::::{prf:proof} Proof of Theorem [%s](#thm:Larman_net_on_finite_dimensional_compact_metric)
:nonumber:
We first construct the net, which requires some setup.

For $n = 0$, put $r = r_0 = 2^{-5}$ into Lemma [%s](#lemma:Larman_compact_metric_space) and obtain the finite collection of points $X^0 := \seq{x_i : i \in I}$ as guaranteed. Put $I^0 := I$, and consider let $x(i) := x_i$ for each $i \in I^0$. Order $X^0$ by following how their indices in $I^0$ are ordered under the standard order on natural numbers.

We inductively build an order on each successive collection $X^n$ of the centers corresponding to level $n \in \omega$ as follows. Suppose $X^{n - 1} = \set{x(\mathbf{i})}{\mathbf{i} \in I^{n - 1}}$ has already been indexed by the finite collection $I^{n - 1} \subset \omega^{n - 1}$ and following the order induced by the lexicographic-order on $I^{n - 1}$ as a subset of $\omega^{n - 1}$. I.e., for $\mathbf{i}, \mathbf{j} \in I^{n - 1}$,

$$
\begin{aligned}
\mathbf{i} < \mathbf{j} :\iff (\exists 1 \leq k \leq n) [i_k <_{\omega} j_k \text{ while } (\forall 1 \leq \ell < k) [i_\ell = j_\ell]].
\end{aligned}
$$

Now for $n > 0$, substitute $r = r_n = 2^{-(n + 5)}$ into Lemma [%s](#lemma:Larman_compact_metric_space) and obtain the finite collection of centers $X^n := \seq{x_i : i \in I}$ as guaranteed. For each $\mathbf{i} \in I^{n - 1}$, denote:

$$
\begin{aligned}
X^n(\mathbf{i}) := \set{x \in X^n}{
\begin{array}{c}
(\forall \mathbf{j} \in I^{n - 1}) [\mathbf{j} < \mathbf{i} \implies B_{2 \cdot r_n}(x) \cap B_{2 \cdot r_{n - 1}}(x(\mathbf{j})) = \emptyset] \AND \\ B_{2 \cdot r_n}(x) \cap B_{2 \cdot r_{n - 1}}(x(\mathbf{i})) \neq \emptyset
\end{array}}.
\end{aligned}
$$

That is, collect all those level-$n$ centers whose double-radius balls meet this double-radius ball yet do not meet any of the previous double-radius balls from level $(n - 1)$. Denote by $I^n(\mathbf{i}) \subseteq I$ the indices of the centers from $X^n(\mathbf{i})$ under $I$. We may order $I^n(\mathbf{i})$ (and, thus, $X^n(\mathbf{i})$) by the standard ordering of natural numbers. Doing this across all $\mathbf{i} \in I^{n - 1}$, we must collect all $x \in X^n$ into exactly one such $X^n(\mathbf{i})$, since the lemma guarantees the double-radius balls cover $\Omega$. If $x = x_i \in X^n(\mathbf{i})$ for some $\mathbf{i} \in I^{n - 1}$ and $i \in I$, then we let its index at level $n$ be the $n$-tuple $\mathbf{i}^\frown i$, and call this $x(\mathbf{i} ^\frown i) := x_i$. Collect all such indices into $I^{n} \subset \omega^n$ and order $I^n$ (and, thus, $X^n$) lexicographically.

Just as $I^n$ indexes the collection of centers $X^n$ at level $n$, it also indexes the collection of double-radius open balls $B^n := \set{B_{2 \cdot r_n}(x)}{x \in X^n} = \set{B(\mathbf{i})}{\mathbf{i} \in I^n}$, where $B(\mathbf{i}) := B_{2 \cdot r_n}(x(\mathbf{i}))$.

We next recall some terminology from {cite:t}`Lar67`.

- A **chain** is a sequence $(B_n)_{n = n_0}^{n_1}$ of balls where $n_0 \leq n_1$ are natural numbers, each $B_n \in B^n$, and $B_{n + 1} \cap B_{n} \neq \emptyset$ for each $n = n_0, ..., n_1 - 1$.
- A point $x \in \Omega$ is **linked** to a ball $B \in B^n$ if there is a chain $(B_n)_{n = n_0}^{n_1}$ starting at $B_{n_0} = B$ and ending at some $B_{n_1}$ containing $x$.
- A point $x \in \Omega$ is **strongly linked** to a ball $B \in B^n$ if $x$ is both linked to $B$ and not linked to any previous ball in $B^n$.

Now we may define the $n$-th layer $\mathcal{N}^n$ of the net $\mathcal{N}$ to be the collection $\set{N(\mathbf{i})}{\mathbf{i} \in I^n}$, where,

$$
\begin{aligned}
N(\mathbf{i}) := \set{x \in \Omega}{x \text{ is strongly linked to } B(\mathbf{i})}.
\end{aligned}
$$

The rest of the proof verifies the desired properties as stated in the claim.

:::{div}
:class: roman-list
1. This follows directly from the construction.

1. No point of $\Omega$ may be strongly connected to more than one ball from $B^n$.

1. For any $x \in N(\mathbf{i})$ for some $\mathbf{i} \in I^{n_0}$, take any chain $(B_n)_{n = n_0}^{n_1}$ such that $B_{n_0} = B(\mathbf{i})$ and linking to $x$. Then it is easy to verify that:

   $$
   \begin{aligned}
   d(x, x(\mathbf{i})) \leq 2^{-(n + 2)}, \quad \text{so} \quad \diam(N(\mathbf{i})) < 2^{-n}.
   \end{aligned}
   $$

1. By choice, $\bigcup_{\mathbf{i} \in I^n} B(\mathbf{i}) = \Omega$. So any $x \in \Omega$ is strongly linked to at least one such $B(\mathbf{i}) \in B^n$.

1. If $\mathbf{i} \in I^{n - 1}$ and $x \in N(\mathbf{i})$, then $x$ is not linked to any ball $B(\mathbf{j})$ in $B^{n - 1}$ preceding $B(\mathbf{i})$. Then neither is $x$ linked to any open ball $B(\mathbf{j} ^\frown j_n) \in B^n$ for $\mathbf{j} ^\frown j_n \in I^n$ where $\mathbf{j} < \mathbf{i}$. Yet, there is a minimal $i_n \in \omega$ satisfying $\mathbf{i} ^\frown i_n \in I^n$ for which $x$ is linked to $B(\mathbf{i} ^\frown i_n) \in B^n$. Thus, $\bigcup_{\mathbf{i} ^\frown i_n \in I^n} N(\mathbf{i} ^\frown i_n) \supseteq N(\mathbf{i})$. Conversely, if $x \in N(\mathbf{i} ^\frown i_n)$, then $x$ is not linked to any $\mathbf{j}^\frown j_n \in I^n$ where $\mathbf{j} < \mathbf{i}$. So $x \in N(\mathbf{i})$. Thus, $\bigcup_{\mathbf{i} ^\frown i_n \in I^n} N(\mathbf{i} ^\frown i_n) \subseteq N(\mathbf{i})$.

1. For $\mathbf{i} \in I^n$, note that $N(\mathbf{i})$ is equal to the set:

   $$
   \begin{aligned}
   \small
   \set{x \in \Omega}{x \text{ is linked to } B(\mathbf{i})} \setminus \set{x \in \Omega}{x \text{ is linked to some ball in $B^{n}$ preceding $B(\mathbf{i})$}}.
   \end{aligned}
   $$

   Both sets in this difference are open as the unions of open balls, so $N(\mathbf{i})$ is $F_\sigma$.

1. Take some $x \in \Omega$ for which $X \subseteq B_{2^{-(n - 1)}}(x)$. Since $(\Omega, d)$ is compact and $\Omega$ is $\mathcal{H}^s$-null, and by the choice of the centers in $X^n$, Lemma [%s](#lemma:Larman_beta_spaces) gives:

   $$
   \begin{aligned}
   \abs{\set{\mathbf{i} \in I^n}{N(\mathbf{i}) \cap X \neq \emptyset}} & \leq \abs{\set{\mathbf{i} \in I^n}{x(\mathbf{i}) \in B_{2^{-(n - 2)}}(x)}}\\
   &\leq \abs{\set{B_{2^{-(n - 5)}}(x(\mathbf{i}))}{x(\mathbf{i}) \in B_{2^{-(n - 2)}} \text{ and } \mathbf{i} \in I^n}}\\
   &\leq K.
   \end{aligned}
   $$
:::

We claim that $\mathcal{N} := \bigcup_{n} \mathcal{N}^n$ is a Rogers net. The axioms (**M1**), (**M2**), and (**N4**$'$) are clear. And by (iii) and (iv), $\Omega$ is covered by a $2^{-n}$-net of open balls for each $n \in \Omega$, so we may conclude (**M3**) as well. The containment-respecting indexing $\iota$ on $\mathcal{N}$ can be made simply by concatenating the orders from each level $\mathcal{N}^n$ as $n$ increases.
::::

When $\Omega$ is both compact and $\mathcal{H}^s$-null for some positive integer $s$, the net constructed in Theorem [%s](#thm:Larman_net_on_finite_dimensional_compact_metric) almost qualifies as a nice cover $(\mathcal{N}^{n})_{n = 1}^\infty$ of $\Omega$ (satisfying nice cover axioms (**A1**), (**A2**), and (**A4**)), if not for the possibility for some net elements to be of zero diameter.

Something stronger may be said for effectively compact metric spaces as defined in Section [%s](#section:Computability_Theory). In order to do so, we establish an effective version of the covering lemma [%s](#lemma:Larman_compact_metric_space).

:::{prf:lemma}
:label: lemma:effectivized_Larman_compact_metric_space
Let $(\Omega, d, \alpha)$ be an effectively compact metric space and fix a positive rational $r$. Then, there exists a finite, computable collection of centers $\seq{x_i: i \in I}$ from the computable dense subset $\alpha$ whose $r$-balls $\seq{B_r(x_i) : i \in I}$ are mutually-disjoint while their $3r$-balls cover $\Omega$; i.e.,

$$
\begin{aligned}
\bigcup_{i \in I} B_{3r}(x_i) = \Omega.
\end{aligned}
$$
:::

:::{prf:proof}
:nonumber:
Given rational $r > 0$, let $k \in \omega$ satisfy $2^{-k} \leq r$. By effective compactness, one may compute a finite subset $\Lambda = \seq{x_i}_i \subseteq \alpha$ satisfying $\Omega = \bigcup_{x_i \in \Lambda} B_{2^{-k}}(x_i)$. We build a set $S$ by iterating through each $x_i \in \Lambda$: if $x_i$ is not yet covered by $B_{2r}(x_j)$ for some $x_j \in S$ already, then append $x_i$ to $S$. We test this by computably comparing $d(x_i, x_j) < 2r$ for each $x_j \in S$. This process is finite and computable.

It is immediate that $r$-balls centered at points in $S$ are mutually-disjoint: all elements of $S$ are at least $2r$ apart. Suppose $\bigcup_{x_j \in S} B_{3r}(x_j)$ does not cover $\Omega$: let $x \in \Omega$ fall outside this union. By assumption, there exists $x_i \in \Lambda$ such that $x \in B_{2^k}(x_i) \subseteq B_r(x_i)$. Then, for each $x_j \in S$:

$$
\begin{aligned}
d(x_i, x_j) \geq d(x, x_j) - d(x, x_i) > 3r - r = 2r.
\end{aligned}
$$

This contradicts the construction of $S$.
:::

:::{prf:corollary}
:label: corollary:Larman_effectively_compact_metric_space
Every effectively compact metric space $(\Omega, d, \alpha)$ admits a Rogers net $\mathcal{N}$ which is arithmetic and satisfies (i)-(vi) of Theorem [%s](#thm:Larman_net_on_finite_dimensional_compact_metric). In fact, the elements of $\mathcal{N}$ are all $\Sigma^0_2$-classes. If the space is also $\mathcal{H}^s$-null for some positive integer $s$, then $\mathcal{N}$ further satisfies (vii) from Theorem [%s](#thm:Larman_net_on_finite_dimensional_compact_metric).
:::

:::{prf:proof}
:nonumber:
Larman's construction of $\mathcal{N}$ in the proof of Theorem [%s](#thm:Larman_net_on_finite_dimensional_compact_metric) almost suffices for an effective result. We make a few modifications and discuss the consequences.

In light of the use of triple-radius balls in the effective Lemma [%s](#lemma:effectivized_Larman_compact_metric_space), we instead define each $B^n$ to collect triple-radius open balls $B(\mathbf{i}) := B_{3 \cdot r_n}(x(\mathbf{i}))$. Moreover, it is not necessarily computable to detect whether open balls non-trivially intersect. We replace any condition of non-trivial intersection by a condition comparing the sum of the balls' radii to the distance between their centers. This affects the definition of $X^n$: for each $\mathbf{i} \in I^{n - 1}$, denote:

$$
\begin{aligned}
X^n(\mathbf{i}) := \set{x \in X^n}{\begin{array}{c}
(\forall \mathbf{j} \in I^{n - 1}) [\mathbf{j} < \mathbf{i} \implies d(x, x(\mathbf{j})) \geq 3r_n + 3r_{n - 1}] \AND \\
d(x, x(\mathbf{i})) < 3r_n + 3r_{n - 1}
\end{array}}.
\end{aligned}
$$

Furthermore, we modify the definition of a chain to be a sequence $(B_n)_{n = n_0}^{n_1}$ of balls where $n_0 \leq n_1$, each $B_n \in B^n$, and such that their respective centers $x_n$ and $x_{n + 1}$ have distance less than the sum of their radii:

$$
\begin{aligned}
d(x_n, x_{n + 1}) < 3 r_n + 3 r_{n + 1}.
\end{aligned}
$$

This numerical comparison of distance versus radii is a weaker condition than checking for non-trivial intersection between their open balls, yet suffices for the construction.

Properties (i), (ii), (iv), and (v) are clear by the previous construction. We confirm that (iii) still holds under these modifications. For any $x \in N(\mathbf{i})$ with $\mathbf{i} \in I^{n_0}$, take any chain $(B_n)_{n = n_0}^{n_1}$ such that $B_{n_0} = B(\mathbf{i})$ and linking to $x$. It is clear by the triangle inequality that:

$$
\begin{aligned}
d(x, x(\mathbf{i})) \leq 3r_n + 2 \cdot 3 r_n \p{2^{-1} + 2^{-2} + \cdots} \leq 9 r_n = 9 \cdot 2^{-(n + 5)} \implies \diam_d(N(\mathbf{i})) < 2^{-n}.
\end{aligned}
$$

We note that the choice of centers forming each $X^n$ is computable when sourced from the effective Lemma [%s](#lemma:effectivized_Larman_compact_metric_space) and under the new definition of $X^{n}(\mathbf{i})$.

We next check the definability complexity of each net element as a subset of $\Omega$. Recall that for each $\mathbf{i} \in I^n$, the set $N(\mathbf{i})$ equals:

$$
\begin{aligned}
\small
\set{x \in \Omega}{x \text{ is linked to } B(\mathbf{i})} \setminus \set{x \in \Omega}{x \text{ is linked to some ball in $B^{n}$ preceding $B(\mathbf{i})$}}.
\end{aligned}
$$

Denote by $\mathsf{linked}(x, \mathbf{i})$ the predicate that holds if and only if $x$ is linked to $B(\mathbf{i})$. Then membership in $N(\mathbf{i})$ is equivalent to:

$$
\begin{aligned}
x \in N(\mathbf{i}) \iff \mathsf{linked}(x, \mathbf{i}) \AND \bigAND_{\mathbf{j} < \mathbf{i}} \NOT \mathsf{linked}(x, \mathbf{j}).
\end{aligned}
$$

Observe that $\mathsf{linked}(x, \mathbf{i})$ is $\Sigma^0_1$-definable: one may computably enumerate the sequences of indices of open balls forming a (finite) chain starting at $B(\mathbf{i})$ and eventually containing $x$. This follows by pairwise distances between elements of $\alpha$ being computable. Therefore, membership in $N(\mathbf{i})$ is a $\Sigma^0_2$-class.

An indexing on this net is arithmetically definable in the codes of its $\Sigma^0_2$ elements. And from the indexing, one may compute the inclusion and predecessor relations. Roots of the net are also computable using the effective lemma. Finally, implicit in the work of Moschovakis {cite:p}`Mos09` (e.g., Exercise 3C.9), the diameter function is arithmetic, as expressed by the following formulas:

$$
\begin{aligned}
\diam_d(N) > \delta &\iff (\exists p,q \in N \cap \alpha) [d(p, q) > \delta], \text{ and}\\
\diam_d(N) < \delta &\iff \NOT (\diam_d(N) \geq \delta)\\
&\iff \NOT (\forall \varepsilon > 0) (\exists p, q \in N \cap \alpha) [d(p, q) > \delta - \varepsilon].
\end{aligned}
$$

Therefore, this is an arithmetically-definable $\omega$-presentation of $\mathcal{N}$.
:::

In the case of compact, $\mathcal{H}^s$-null metric spaces, Theorem [%s](#thm:Larman_net_on_finite_dimensional_compact_metric) (vii) gives the following comparability result.

:::{prf:corollary} Lemma 1 of {cite:t}`Lar67`
:label: cor:Larman_net_on_finite_dimensional_compact_metric
Let $\Omega$ be a compact metric space which is $\mathcal{H}^s$-null for some positive integer $s$. Take $\mathcal{N}$ to be the net constructed in Theorem [%s](#thm:Larman_net_on_finite_dimensional_compact_metric) on $\Omega$ and $K > 0$ as in (vii), and let $h$ be a dimension function. Then, there exists a net premeasure $\rho$ (namely, $\restrict{\rho_h}{\mathcal{N}}$) on $\mathcal{N}$ such that,

$$
\begin{aligned}
\mathcal{H}^h_\delta(X) \leq \mathcal{H}^\rho_\delta(X) \leq K \cdot \mathcal{H}^h_{\delta} (X),
\end{aligned}
$$

for all $\delta > 0$ and for all subsets $X \subseteq \Omega$. Furthermore,

$$
\begin{aligned}
\mathcal{H}^h(X) \leq \mathcal{H}^\rho(X) \leq K \cdot \mathcal{H}^h (X),
\end{aligned}
$$

for all subsets $X \subseteq \Omega$.
:::

In summary, the numerical conditions found in Theorems [%s](#thm:Theorem_49_Euclidean_comparability) and [%s](#thm:Theorem_50_ultrametric_comparability), as well as Corollary [%s](#cor:Larman_net_on_finite_dimensional_compact_metric), help to ensure commensurateness and hence comparability between the guaranteed net premeasures and the $s$-dimensional Hausdorff outer measures.

## Polish Spaces

We now perform a similar investigation for Polish spaces. A metric space is called **Polish** if it is both complete and separable, i.e. has a countable dense subset. A standard result in descriptive set theory states that each non-empty Polish spaces is the continuous image of Baire space. We are interested in the proof of this result, which utilizes Lusin schemes. Refer to {cite:p}`Kec95` for more details.

::::{prf:definition}
:label: definition:Lusin_scheme
If $\Omega$ is a set and $\mathcal{A} := (A_\sigma : \sigma \in \omega^{<\omega})$ is a family of subsets $A_\sigma \subseteq \Omega$, we call $\mathcal{A}$ a **Lusin scheme on $\Omega$** if it satisfies for each $\sigma \in \omega^{<\omega}$ and $i, j \in \omega$:

:::{div}
:class: roman-list
1. $A_{\sigma ^\frown i} \cap A_{\sigma ^\frown j} \neq \emptyset \iff i = j$; and
1. $A_{\sigma ^\frown i} \subseteq A_\sigma$.
:::
::::

:::{prf:definition}
:label: def:vanishes_to_zero
A Lusin scheme $\mathcal{A} = (A_\sigma)_\sigma$ on a metric space $(\Omega, d)$ is said to **have vanishing diameter** if for each $\gamma \in \omega^\omega$,

$$
\begin{aligned}
\lim_n \diam_d(A_{\restrict{\gamma}{n}}) = 0.
\end{aligned}
$$

To any Lusin scheme with vanishing diameter we may associate the set $F_{\mathcal{A}}$ of representative addresses, as well as the representation map $f_{\mathcal{A}}: F_{\mathcal{A}} \to \Omega$, where

$$
\begin{aligned}
F_{\mathcal{A}} = \set{\gamma \in \omega^\omega}{\bigcap_n A_{\restrict{\gamma}{n}} \neq \emptyset}, \quad \text{and} \quad \seq{f_{\mathcal{A}}(\gamma)} = \bigcap_n A_{\restrict{\gamma}{n}} \quad \text{for all $\gamma \in F_{\mathcal{A}}$}.
\end{aligned}
$$

The associated map $f_{\mathcal{A}}$ is clearly continuous and injective.
:::

:::{prf:theorem} Theorem 7.9 of {cite:t}`Kec95`
:label: theorem:Polish_space_as_continuous_image_of_Baire
If $\Omega$ is a Polish space, then there exists a closed class $F \subseteq \omega^\omega$ and a continuous bijection $g: F \to \Omega$. Furthermore, if $\Omega \neq \emptyset$, then there is a continuous surjection $\hat{g}: \omega^\omega \to \Omega$ extending $g$.
:::

::::{prf:proof}
:nonumber:
The second claim follows from the first claim combined with the standard result in Proposition 2.8 of {cite:t}`Kec95` on retractions. Fix a compatible, complete metric $d \leq 1$ on $\Omega$. We will construct a Lusin scheme $\mathcal{A} = (A_\sigma)_\sigma$ on $\Omega$ further satisfying:

:::{div}
:class: roman-list
1. $A_\emptyset = \Omega$;
1. Each $A_\sigma$ is an $F_\sigma$ (i.e., $\mathbf{\Sigma}^0_2$) class;
1. Each $A_\sigma = \bigcup_{i \in \omega} A_{\sigma ^\frown i} = \bigcup_{i \in \omega} \overline{A_{\sigma ^\frown i}}$; and
1. Each $\diam_d(A_\sigma) \leq 2^{- \operatorname{len}(\sigma)}$.
:::

Notice that it suffices to prove that for each $F_\sigma$ set $A \subseteq \Omega$ and $\varepsilon > 0$, that $A = \bigcup_{i \in \omega} A_i$, where all $A_i$ are mutually-disjoint $F_\sigma$ sets of diameter $\diam_d(A_i) < \varepsilon$ and whose closures satisfy $\overline{A_i} \subseteq A$.

Since $A$ is $F_\sigma$, we may write $A = \bigcup_i C_i$, where each $C_i$ is closed and nested in the next: $C_i \subseteq C_{i + 1}$. Then, clearly,

$$
\begin{aligned}
A = \bigcup_i (C_{i + 1} \setminus C_i),
\end{aligned}
$$

giving $A$ as a union of mutually-disjoint, $\mathbf{\Delta}^0_2$-classes. We might also cover the entire space $\Omega = \bigcup_{n \in \omega} U_n$ by open sets of bounded diameter $\diam_d(U_n) < \varepsilon$. Putting:

$$
\begin{aligned}
D^{(i)}_n := U_n \cap (C_{i + 1} \setminus C_i), \quad E^{(i)}_n := D^{(i)}_n \setminus \p{\bigcup_{n' < n} D_{n'}^{(i)}},
\end{aligned}
$$

we get that each $C_{i + 1} \setminus C_i = \bigcup_n E^{(i)}_n$ and:

$$
\begin{aligned}
\overline{E^{(i)}_n} \subseteq \overline{C_{i + 1} \setminus C_i} \subseteq \overline{C_{i + 1}} = C_{i + 1} \subseteq A.
\end{aligned}
$$

Therefore, $A = \bigcup_{i, n} E^{(i)}_n$ is a union of mutually-disjoint, $F_\sigma$ sets of diameter $\diam_d(E^{(i)}_n) \leq \diam_d(U_n) < \varepsilon$ and whose closures lie in $A$.

The Lusin scheme $\mathcal{A}$ indeed vanishes to zero by the assumption (iv), and thus has associated to it the set $F_{\mathcal{A}}$ and map $f_{\mathcal{A}}$ as in Definition [%s](#def:vanishes_to_zero). Set $F := F_{\mathcal{A}}$. By the definition of a Lusin scheme and by the assumptions (i) and (iii), $f_{\mathcal{A}}(F) = f_{\mathcal{A}}(F_{\mathcal{A}}) = A_{\emptyset} = \Omega$. It remains to show that $F$ is closed.

Take $\gamma \in \omega^\omega$ and $(\gamma_k)_k \subseteq F$ such that $\gamma_k \to \gamma$. Notice that for all $\varepsilon > 0$, there exists $n_0 \in \omega$ such that $\diam_d(A_{\restrict{\gamma}{n_0}}) < \varepsilon$, as well as $k_0 \in \omega$ such that for all $k \geq k_0$, we have $\restrict{\gamma_{k}}{n_0} = \restrict{\gamma}{n_0}$. Therefore, for each $\varepsilon > 0$ and $k, k' \geq k_0$, we have $d(f_{\mathcal{A}}(\gamma_k), f_{\mathcal{A}}(\gamma_{k'})) < \varepsilon$.

So, $\p{f_{\mathcal{A}}(\gamma_k)}_k$ is a Cauchy sequence. But $(\Omega, d)$ is a complete metric space, so the sequence converges: $f_{\mathcal{A}}(\gamma_k) \to y \in \Omega$. But,

$$
\begin{aligned}
y \in \bigcap_{n \in \omega} \overline{A_{\restrict{\gamma}{n}}} = \bigcap_{n \in \omega} A_{\restrict{\gamma}{n}} \implies \gamma \in F_{\mathcal{A}} = F \quad \text{and} \quad f_{\mathcal{A}}(\gamma) = y.
\end{aligned}
$$

So, $F$ is closed, as desired.
::::

:::{prf:corollary}
Every Polish space admits a Rogers net.
:::

:::{prf:proof}
:nonumber:
Take $\mathcal{A}$ to be the Lusin scheme constructed in the proof of Theorem [%s](#theorem:Polish_space_as_continuous_image_of_Baire). Clearly, $\mathcal{A}$ is countable, and has the property that supersets of $A_\sigma$ are just those $A_\rho$ where $\rho$ is a prefix of $\sigma$, of which there are only finitely many. So $\mathcal{A}$ satisfies (**M1**) and (**M2**). Furthermore, any point $x$ in the Polish space has a preimage $\gamma \in \omega^\omega$ under the associated map $f_{\mathcal{A}}$. Notice that for each $n \in \omega$, we have $x \in A_{\restrict{\gamma}{n}}$, where $\diam_d(A_{\restrict{\gamma}{n}}) \leq 2^{-n}$, giving (**M3**). Now, by definition, non-empty intersection between two elements of the Lusin scheme implies comparability with respect to set-inclusion, giving (**N4**$'$). Note that we may index $\mathcal{A}$ by making use of a standard enumeration of $\omega^{<\omega}$ in a prefix-increasing manner. This indexing will necessarily respect set-inclusion.
:::

Once again, something more can be said about the definability complexity of the net for computable Polish spaces (under the assumption that they are also compact). Recall the definition of a computable Polish space from Section [%s](#section:Computability_Theory).

:::{prf:proposition}
:label: proposition:effective_net_over_Polish
Every compact, computable Polish space $(\Omega, d, \alpha)$ admits an arithmetically-definable Rogers net satisfying (i)-(iv) in the proof of Theorem [%s](#theorem:Polish_space_as_continuous_image_of_Baire). In fact, all of the elements of this net may be made to be $\Sigma^0_2$-classes.
:::

:::{prf:proof}
:nonumber:
The construction of the Lusin scheme in the proof of Theorem [%s](#theorem:Polish_space_as_continuous_image_of_Baire) goes through with all sets now being of the corresponding lightface Borel complexity. One considers the recursive rule applied to any $\Sigma^0_2$-class $A$, beginning with $A_\emptyset = \Omega$.

The lightface construction expresses $A$ as the countable union $\bigcup_{i, n} E^{(i)}_n$ of mutually-disjoint, uniformly-$\Sigma^0_2$-classes of diameter $\diam_d(E^{(i)}_n) \leq \diam_d(U_n) < \varepsilon$ and whose closures lie in $A$. By the compactness of $\Omega$, it is arithmetic to include only those $E^{(i)}_n$ which are non-empty. And so, the Lusin scheme $\mathcal{A}$ is constructed with its arithmetically-definable indexing as well.

We have already proved that $\mathcal{A}$ qualifies as a Rogers net. The inclusion and predecessor relations are computable from the indexing. The only root of the net is $A_\emptyset = \Omega$. And, as in the proof of Corollary [%s](#corollary:Larman_effectively_compact_metric_space), the diameter function on the net $\mathcal{A}$ is arithmetic. So, $\mathcal{A}$ has an arithmetically-definable $\omega$-presentation.
:::
