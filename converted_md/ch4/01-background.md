---
title: "Background"
label: section:Nets_Background
---

As we have noted, algorithmic information theory has succeeded at characterizing certain fractal dimensions and outer measures on simple spaces in effective terms (e.g., the point-to-set principles [%s](#theorem:PTS_for_H_dimension) and [%s](#theorem:PTS_log_s_measure_and_sigma_finite)). These simple spaces include Euclidean space as well as spaces of infinite sequences over finite alphabets. Yet, classical fractal dimensions such as Hausdorff dimension and packing dimension are well-defined over **arbitrary** metric spaces. So, it is natural to investigate over which settings AIT may successfully be applied to GMT.

E. Mayordomo isolated for her **nicely covered spaces** some conditions under which a metric space would admit a subset of the effective dimension equalities found in Theorem [%s](#theorem:asymptotic_coincidences_Cantor){cite:p}`May14`. Even more recently, J. Lutz, N. Lutz, and Mayordomo extended the Point-to-Set Principle to all separable metric spaces via an incompressibility approach {cite:p}`LLM23`. They leave open the possibility for algorithmic dimension to be alternatively characterized in general metric spaces via effective mass distribution or betting strategies.

In this chapter, we develop the full algorithmic information theory framework for a broad class of metric spaces which comprises the two approaches known hitherto.

A standard result in geometric measure theory is one by A. Besicovitch claiming that within each compact subset of Euclidean space of positive $\mathcal{H}^s$-measure, one may find a subset whose $\mathcal{H}^s$-measure is in fact both non-zero and finite {cite:p}`Bes52`. Besicovitch's proof involved constructing outer measures from premeasures defined on the collection of dyadic cubes over Euclidean space. Besicovitch further noticed that these outer measures would assign a comparable measure to arbitrary subsets as the $s$-dimensional Hausdorff outer measures $\mathcal{H}^s$.

D. Larman later generalized these notions to metric spaces covered by **nets** {cite:p}`Lar67`: a net on a metric space may be described as a countable cover consisting of sufficiently nicely nested subsets; and a **net measure** is an outer measure produced from a given premeasure defined on a net. Call any metric space admitting a net to be a **net space**. C. Rogers and R. Davies succeeded at extending Besicovitch's result about compact sets to a broad class of net spaces using the properties of nets and net measures {cite:p}`Rog70`. The essential properties of the collection of dyadic cubes on Euclidean space also play a similar role in the study of maximal functions in harmonic analysis. Evidently, net spaces should constitute fruitful settings over which to consider geometric measure theory.

In the language of nets, Euclidean space was shown to admit a net of dyadic cubes rich enough to simulate Hausdorff dimension only by covers comprising elements of that net. Note that in general, not all metric spaces admit nets, and not all metric spaces which do admit nets have a rich enough family of nets to simulate Hausdorff dimension.

Net spaces are particularly suited to the development of algorithmic information theory. The computability arguments made on either the nicely covered spaces of {cite:t}`May14` or the separable metric spaces considered in {cite:t}`LLM23` make use of countable collections of subsets with nice covering and nesting properties. Our approach will take advantage of the countability and tree-like structure of a net under set-inclusion to extend algorithmic information theory to net spaces. Whether the effective dimension notions produced in this extension will correspond to the classical Hausdorff dimension on that space will depend on the existence of nets with net measures comparable to the family $(\mathcal{H}^s)_{s \geq 0}$.

From this perspective, the standard Point-to-Set Principle [%s](#theorem:PTS_for_H_dimension) for Euclidean space may be viewed as the combination of two results: first, that Hausdorff dimension restricted to covers by dyadic cubes admits a point-to-set principle using effective covers also by dyadic cubes; and second, that the dyadic cubes net on Euclidean space admits comparable measures to each $\mathcal{H}^s$.

## Meshes and Nets

::::{prf:definition}
We say that a collection $\mathcal{N}$ of non-empty subsets of a metric space $\Omega$ is a **mesh** on $\Omega$ if it satisfies the following properties:

:::{div}
:class: labeled-list
- (**M1**) $\mathcal{N}$ is countable;
- (**M2**) Each element of $\mathcal{N}$ has at most finitely many supersets also in $\mathcal{N}$;
- (**M3**) For any $x \in \Omega$ and $\varepsilon > 0$, $x$ is contained in an element of $\mathcal{N}$ of diameter less than $\varepsilon$.
:::

The pair $(\Omega, \mathcal{N})$ is then called a **mesh space**.
::::

For any two mesh elements $N_1, N_2 \in \mathcal{N}$, let $N_1 \mid\mid N_2$ denote that $N_1$ and $N_2$ are **comparable** (under the containment relation), which means either $N_1 \subseteq N_2$ or $N_2 \subseteq N_1$. Otherwise, $N_1$ and $N_2$ are said to be **incomparable**.

::::{prf:definition}
If $\mathcal{N}$ is a mesh on $\Omega$, we call $\mathcal{N}$ a **net** on $\Omega$ if it further satisfies:

:::{div}
:class: labeled-list
- (**N4**) No element of $\mathcal{N}$ is contained in two incomparable elements from $\mathcal{N}$. That is, $N \subseteq N_1 \cap N_2$ implies $N_1 \mid \mid N_2$ for all $N, N_1, N_2 \in \mathcal{N}$.
:::

The pair $(\Omega, \mathcal{N})$ is then called a **net space**.
::::

This definition of a net differs from the definition provided by C. Rogers and R. Davies in {cite:t}`Rog70` in the following ways. First, they ask that each element of a net be $F_\sigma$ (that is, $\mathbf{\Sigma}^0_2$) in order to get useful results about the regularity of their net measures, as well as on how such net measures behave on compact sets with positive measure. For most of our purposes, we will not need a bound on the descriptive complexity of net elements. Second, (**N4**) slightly generalizes the incomparability axiom of Rogers and Davies which asks that any two non-trivially intersecting net elements be comparable. As we will see, many results from algorithmic information theory still hold under our weaker incomparability axiom (**N4**). We will call any net which satisfies the following stronger axiom to be a **layered-disjoint net**:

:::{div}
:class: labeled-list
- (**N4**$'$) No two incomparable elements of $\mathcal{N}$ may meet non-trivially. That is, $N_1 \cap N_2 \neq \emptyset$ implies $N_1 \mid \mid N_2$ for all $N_1, N_2 \in \mathcal{N}$.
:::

The name is inspired by the **layered disjoint systems** of {cite:t}`CL14`. It will be clear that any net satisfying (**N4**$'$) induces a layered disjoint system in that sense. Any layered-disjoint net on $\Omega$ may also be viewed as a Lusin scheme on $\Omega$ in the sense of Definition [%s](#definition:Lusin_scheme) below. Whenever a layered-disjoint net comprises only $F_\sigma$ sets, we will more specifically call it a **Rogers net**.

The elements of a mesh and net are arranged in a tree-like structure. To argue this, let us first note that the containment relation $\supseteq$ is **well-founded** on a mesh or net. That is, $\supseteq$ is a partial binary relation on $\mathcal{N} \times \mathcal{N}$ which always admits minimal elements, i.e.,

$$
\begin{aligned}
(\forall \mathcal{E} \subseteq \mathcal{N}) \brk{\mathcal{E} \neq \emptyset \implies (\exists N \in \mathcal{E})(\forall N' \in \mathcal{E}) [N' \supseteq N \implies N' = N]}.
\end{aligned}
$$

Since $\supseteq$ is both transitive and antisymmetric, the mesh axiom (**M2**) gives us that the containment relation $\supseteq$ is well-founded over any mesh.

In particular, we claim in the following proposition that the containment relation on a mesh induces a **directed, acyclic graph (DAG)** on the mesh elements. If $G = (V, E)$ is a graph, and $\to$ is a partial binary relation on $V \times V$ satisfying $x \to y \iff (x, y) \in E$, then $G$ is a DAG if the transitive closure (i.e., the extended relation which relates two vertices so long as there is a finite directed path between them) of $\to$ is well-founded.

:::{prf:proposition}
:label: prop:DAG_characterization_of_mesh
To any mesh $\mathcal{N}$ on a metric space $\Omega$ may be associated a directed, acyclic graph $\mathcal{G}$ whose vertices are the elements of $\mathcal{N}$, and whose directed edge relation ($\rightarrow$) is given by the immediate-predecessor relation:

$$
N_1 \rightarrow N_2 \iff N_2 \subsetneq N_1 \AND (\forall N \in \mathcal{N}) [N_2 \subsetneq N \subseteq N_1 \implies N = N_1].
$$
:::

:::{prf:proof}
:nonumber:
By (**M2**), any set in $\mathcal{N}$ must have only finitely many supersets in $\mathcal{N}$. Therefore, all paths between vertices in $\mathcal{G}$ are of finite length. And by (**M1**), the degree of every vertex is countable, so $\mathcal{G}$ is a directed graph on $\mathcal{N}$. It remains to check that $\mathcal{G}$ is acyclic.

Let $\preceq_{\mathcal{N}}$ be the partial order on vertices of $\mathcal{G}$ induced by path-connectedness (i.e., the transitive closure of $\operatorname{pred}$): define $N_1 \preceq_{\mathcal{N}} N_2$ if and only if there is a finite path in $\mathcal{G}$ from $N_1$ to $N_2$ (or, if $N_1 = N_2$). Then, $N_1 \preceq N_2$ holds if and only if $N_2 \subseteq N_1$. And as the containment relation is well-founded, it follows that $\mathcal{G}$ is directed acyclic.
:::

By standard results on well-founded relations (e.g., Theorem 2.27 of {cite:t}`Jec03`), one may assign to any mesh element $N \in \mathcal{N}$ its **rank**, which is given by the length of the longest path in $\mathcal{G}$ from a root element (i.e., an element having no strict superset in the mesh) of $\mathcal{N}$ to $N$. This may be defined inductively as follows: the rank of any root element in $\mathcal{N}$ is taken to be zero, and for any other $N \in \mathcal{N}$:

$$
\begin{aligned}
\operatorname{rk}(N) := 1 + \max \set{\operatorname{rk}(N')}{N \subsetneq N' \in \mathcal{N}}.
\end{aligned}
$$

For any mesh $\mathcal{N}$ and natural number $r \in \omega$, let $\mathcal{N}^{(r)} := \set{N \in \mathcal{N}}{\operatorname{rk}(N) = r}$ denote the collection of elements in $\mathcal{N}$ with rank $r \in \omega$. Note that if $N \in \mathcal{N}^{(r)}$, then any superset of $N$ in $\mathcal{N}$ must be of rank less than $r$.

It is well-known that on any DAG one may perform topological sort. This formalizes for meshes as follows.

:::{prf:proposition}
:label: proposition:indexing_for_meshes
Any mesh $\mathcal{N}$ admits a bijective indexing $\iota: \omega \to \mathcal{N}$ respecting the containment relation. That is, for any $i, j \in \omega$, we have

$$
\iota(i) \subseteq \iota(j) \implies i \geq j.
$$
:::

:::{prf:proof}
:nonumber:
It suffices to find a bijection $\iota : \subseteq \omega \to \mathcal{N}$ respecting containment as in the statement. We take $\ang{\cdot, \cdot} : \omega^2 \to \omega$ to denote a standard, bi-computable, injective pairing function monotonically-increasing in both its components.

Begin by enumerating each rank layer $\mathcal{N}^{(r)} = \seq{N^{(r)}_0, N^{(r)}_1 ..., }$. We define $\iota$ inductively in the rank. For a given mesh element $N^{(0)}_e \in \mathcal{N}^{(0)}$, define the index of $N^{(0)}_e$ so that:

$$
\begin{aligned}
\iota : \ang{0, e} \mapsto N^{(0)}_e.
\end{aligned}
$$

For a fixed $r \in \omega$, suppose we have defined $\iota$ to surject onto all of $\mathcal{N}^{(r)}$, and take $N^{(r + 1)}_e \in \mathcal{N}^{(r + 1)}$. Assign an index to $N^{(r + 1)}_e$ as follows:

$$
\begin{aligned}
I^{(r + 1)}_e &:= \max_{f \in \omega} \set{\iota^{-1}\p{N^{(r)}_f}}{N^{(r + 1)}_e \subseteq N^{(r)}_f};\\
\iota &: \ang{r + 1, \ang{I^{(r + 1)}_e, e}} \mapsto N^{(r + 1)}_e.
\end{aligned}
$$

First, notice that by induction, $\iota$ indeed surjects onto $\mathcal{N}$ since $(\mathcal{N}^{(r)})_r$ partitions $\mathcal{N}$. The indexing is injective since $\ang{\cdot, \cdot}$ is injective. It remains to check that $\iota$ respects containment.

Suppose $i, j \in \omega$ are such that $\iota(i) \subseteq \iota(j)$. It holds that either $\iota(i) = \iota(j)$ (and hence, $i = j$), or $\iota(i) \subsetneq \iota(j)$, meaning $\operatorname{rk}(\iota(j)) < \operatorname{rk}(\iota(i))$. Without loss of generality, we may assume that $\operatorname{rk}(\iota(j)) = \operatorname{rk}(\iota(i)) - 1$ (the general case would then follow by induction). Suppose $i = \ang{r, \ang{I^{(r)}_e, e}}$ for some $r > 0$ and $e \in \omega$. Then, by definition, $I^{(r)}_e \geq j$, giving $i > j$ by the properties of $\ang{\cdot, \cdot}$.
:::

:::{prf:proposition}
:label: prop:tree_characterization_of_net
The associated graph $\mathcal{G}$ to a net $\mathcal{N}$ is a forest of countably many countable trees. That is, the net $\mathcal{N}$ is embeddable into $\omega^{<\omega}$.
:::

:::{prf:proof}
:nonumber:
Take $\mathcal{G}$ to be the directed, acyclic graph associated to $\mathcal{N}$ in Proposition [%s](#prop:DAG_characterization_of_mesh). With the net axiom (**N4**), it follows that each element of $\mathcal{N}$ has at most one immediate predecessor with respect to containment That is, each vertex of $\mathcal{G}$ has an in-degree of at most $1$. So $\mathcal{G}$ is graph-isomorphic to a countable collection of disjoint trees on $\omega^{<\omega}$.
:::

If $\mathcal{N}$ is a layered-disjoint net, then the sequence of rank layers $(\mathcal{N}^{(r)})_{r \in \omega}$ forms a layered disjoint system in the sense of {cite:t}`CL14`. Moreover, the infinite paths through the associated graph $\mathcal{G}$ which begin at indices of root elements (i.e., elements with no strict-superset in $\mathcal{N}$) are in a one-to-one correspondence with points in $\Omega$.

:::{prf:definition}
For $x \in \Omega$ and mesh $\mathcal{N}$ on $\Omega$ with indexing $\iota$, call any sequence $(i_n)_{n \in \omega} \subseteq \omega$ satisfying

$$
\begin{aligned}
x \in \bigcap_{n} \iota(i_n) \quad \text{and} \quad \diam(i_n) \to 0 \quad \text{as} \quad n \to \infty
\end{aligned}
$$

an **$\mathcal{N}$-name of $x$**. Collect all $\mathcal{N}$-names of $x$ in the set $\mathcal{R}(x)$.
:::

Since incomparable mesh elements may overlap (i.e., have nontrivial intersection), each $\mathcal{R}(x)$ may be a large collection in general. But layered-disjoint nets admit unique names.

## Computability for Meshes and Nets

Fix a mesh space $(\Omega, \mathcal{N})$, as well as an indexing $\iota: \omega \to \mathcal{N}$ respecting containment as in Proposition [%s](#proposition:indexing_for_meshes).

For the purposes of computability, we treat the mesh $\mathcal{N}$ as a structure with a corresponding $\omega$**-presentation** $\mathscr{R}$ to which we will assume to possess oracle access. We assume that $\mathscr{R}$ at least computes $\ang{\operatorname{in}, \operatorname{pred}, \operatorname{diam}, \operatorname{root}}$, where

- $\operatorname{in}: \omega^2 \to \seq{\top, \bot}$ is a relation on pairs of indices encoding the containment relation in the mesh; i.e., if $N_i, N_j \in \mathcal{N}$ satisfy $\iota(i) = N_i$ and $\iota(j) = N_j$, then

  $$
  \begin{aligned}
  \operatorname{in}(i, j) \iff N_i \subseteq N_j.
  \end{aligned}
  $$

- $\operatorname{pred}: \omega^2 \to \seq{\top, \bot}$ is a relation on pairs of indices encoding the predecessor relation in the mesh; i.e., if $N_i, N_j \in \mathcal{N}$ satisfy $\iota(i) = N_i$ and $\iota(j) = N_j$, then

  $$
  \begin{aligned}
  \operatorname{pred}(i, j) \iff N_j \subsetneq N_i \AND (\forall N \in \mathcal{N}) [N_j \subsetneq N \subseteq N_i \implies N = N_i].
  \end{aligned}
  $$

- $\operatorname{diam}: \omega \to [0, \infty]$ is a map from indices to non-negative extended reals encoding the diameter function for net elements; i.e., if $\iota(i) = N_i \in \mathcal{N}$, then

  $$
  \begin{aligned}
  \operatorname{diam}(i) = \diam_d(N_i) = \sup \set{d(x, y)}{x, y \in N_i}.
  \end{aligned}
  $$

- $\operatorname{root} : \omega \to \seq{\top, \bot}$ is the characteristic function for the set of indices of the root elements of the mesh; i.e., if $\iota(i) = N_i \in \mathcal{N}$, then

  $$
  \begin{aligned}
  \operatorname{root}(i) \iff (\forall N \in \mathcal{N})[N \supseteq N_i \implies N = N_i].
  \end{aligned}
  $$

Note that in net spaces, the predecessor relation is equivalently characterized as:

$$
\begin{aligned}
\operatorname{pred}(i, j) \iff N_j \subsetneq N_i \AND (\forall N \in \mathcal{N}) [N_j \subsetneq N \implies N_i \subseteq N].
\end{aligned}
$$

Given a mesh space $(\Omega, \mathcal{N})$ and an $\omega$-presentation $\mathscr{R}$ of $\mathcal{N}$ as described above, call the tuple $(\Omega, \mathcal{N}, \mathscr{R})$ a **represented mesh space**. If $\mathcal{N}$ is in fact a net, we might also call $(\Omega, \mathcal{N}, \mathscr{R})$ a **represented net space**.

Any computability notion considered over a mesh $\mathcal{N}$ must be taken with respect to some $\omega$-presentation $\mathscr{R}$ of $\mathcal{N}$. An **effective mesh** is a mesh with a computable $\omega$-presentation $\mathscr{R}$. We may drop the reference to a computable presentation, since having oracle access to it will not provide any extra computational power. Analogous definitions describe **effective nets** of each kind.

Recall the definition of a computable metric space from Section [%s](#section:Computability_Theory). We note that any separable metric space may be viewed as a computable metric space relative to some oracle which uniformly computes the pairwise distances between elements of the dense sequence.

Suppose the metric space $(\Omega, d)$ has an effective mesh $\mathcal{N}$ with a computable $\omega$-presentation $\mathscr{R}$. And suppose there is a map $\chi : \omega \to \Omega$ such that for each $i \in \omega$, we have $\chi(i) \in \iota(i)$ and such that the map $i, j \mapsto d(\chi(i), \chi(j))$ is computable. Denote by $\alpha = (\alpha_i)_{i \in \omega}$ with $\alpha_i = \chi(i)$ the sequence built from the range of $\chi$. Then, we call $(\Omega, d, \mathcal{N}, \mathscr{R}, \alpha)$ a **computable mesh space**. If $\mathscr{N}$ were in fact a net, we might also call this space a **computable net space**. And, without the mesh and its presentation, any computable mesh space is a computable metric space.

:::{prf:proposition}
If $(\Omega, d, \mathcal{N}, \mathscr{R}, \alpha)$ is a computable mesh space, then $(\Omega, d, \alpha)$ is a computable metric space.
:::

:::{prf:proof}
:nonumber:
We already have that the pairwise distances between elements of $\alpha$ are computable by the definition of a computable mesh space. It remains to show that this sequence is dense in $\Omega$. Take $x \in \Omega$ and $\delta > 0$. By the mesh axiom (**M3**), there exists a mesh element $N \in \mathcal{N}$ such that $x \in N$ and $\operatorname{diam}_d(N) < \delta$. By the triangle inequality, $N \subseteq B_\delta(x)$. But if $\iota(i) = N$ for some $i \in \omega$, then $\chi(i) \in N$ implies that $\chi(i) \in B_\delta(x)$ as well. So $(\chi(i))_i$ is dense in $\Omega$.
:::

Note that many of the basic examples of mesh or net spaces are also computable metric spaces. However, the notion of a space with an effective mesh is not generally comparable with the notion of a computable metric space.

## Examples

Let us begin by extending an example from {cite:t}`May14`.

:::{prf:example}
:label: example:euclidean_has_dyadic_net
For $m \in \omega$, $m$-dimensional Euclidean space $\mathbb{R}^m$–as a metric space whose metric is based on a Borel measure $\nu$ on $\mathbb{R}^m$–is a net space when paired with the net $\mathcal{Q}^m$ composed of all half-open, dyadic rational cubes (as defined in Section [%s](#section:Notation)). In fact, $\mathcal{Q}^m$ is a Rogers net on $\mathbb{R}^m$. We have (**M3**) since for each $x$ there exists a sequence $(Q_j)_j \subset \mathcal{Q}^m$ such that $\bigcap_j Q_j = \seq{x}$ and $\nu$ satisfies continuity from above. A simple dove-tailing algorithm can index $\mathcal{Q}^m$ while respecting the containment relation. Under this enumeration $(Q_i)_{i \in \omega}$, it is also straightforward to compute the containment relation, predecessor relation, and indices of any root elements (those cubes with $n = 0$).

In particular, $\mathbb{R}^m$ with the usual Euclidean metric has an effective Rogers net. Notice that $\diam(Q(\mathbf{z}, \mathbf{a}, n)) = \sqrt{m} \cdot 2^{-n}$ is a computable function. The centers of all cubes in $\mathcal{Q}^m$ constitute a dense subset of $\mathbb{R}^m$ with computable pairwise distances. Therefore, $\mathbb{R}^m$ under the Euclidean metric and dyadic cubes net make a computable net space.
:::

Another example comes from {cite:t}`Rog70`.

:::{prf:definition}
A metric space $(\Omega, d)$ is said to be an **ultrametric space** if, whenever $x, y, z \in \Omega$, then

$$
\begin{aligned}
d(x,z) \leq \max \seq{d(x,y), d(y, z)}.
\end{aligned}
$$
:::

:::{prf:example}
:label: example:ultrametric_has_nets
Let ($\Omega$, $d$) be a separable ultrametric space. Then $\Omega$ has many layered-disjoint nets. Fix a strictly-decreasing sequence of positive reals $(d_i)_{i \in \omega}$ converging to zero. And fix a countable, dense sequence $(x_j)_{j \in \omega}$ in $\Omega$. For any $x \in \Omega$ and $i \in \omega$, denote:

$$
\begin{aligned}
N(x, i) := \set{y \in \Omega}{d(y, x) \leq d_i}.
\end{aligned}
$$

We claim that the collection $\mathcal{N} := \set{N(x_j, i)}{i, j \in \omega}$ is a net on $\Omega$. Since $\Omega$ is an ultrametric space, each $N(x, i)$ is open and non-empty containing $x$. Again, $\Omega$ being an ultrametric space gives us the following fact: if ever we have for some $x, y \in \Omega$ and $0 \leq i \leq j$ that $N(x, i) \cap N(y, j) \neq \emptyset$, it follows that that exists $z$ in their intersection satisfying,

$$
\begin{aligned}
d(x, z) \leq d_i \text{ and } d(y, z) \leq d_j \implies d(x, y) \leq \max \seq{d_i, d_j} = d_i.
\end{aligned}
$$

Thus, for any $w \in N(y, j)$, both $d(x, y) \leq d_i$ and $d(y, w) \leq d_i$, giving $d(x, w) \leq d_i$ as well. Thus, $w \in N(x, i)$. This means that any nontrivial overlap between two elements implies the elements are comparable under containment, giving (**N4**$'$). Since $\diam_d(N(x, i)) \leq d_i$, the mesh axiom (**M3**) follows. Finally, if $x \in \Omega$ and $i \in \omega$, we consider which $N(y, j)$ might contain $N(x, i)$. And since $(d_i)_i$ is strictly-decreasing, there must exist some smallest $k + 1 \in \omega$ so that $N(x, k + 1)$ is a proper subset of $N(x, i)$. By (**N4**$'$), any $N(y, j) \supseteq N(x, i)$ must then match one of the finitely many elements $N(x, 1)$, $N(x, 2)$, ..., $N(x, k)$. This gives (**M2**). So $\mathcal{N}$ is indeed a layered-disjoint net on $\Omega$.
:::

:::{prf:example}
:label: example:Baire_space_has_net_Borel_measure
Take Baire space $\omega^{\omega}$, equipped with the product topology from the discrete topology on $\omega$ and the compatible metric:

$$
\begin{aligned}
d(\alpha, \beta) := \begin{cases}
0 & \alpha = \beta,\\
2^{-\min \set{i}{\alpha(i) \neq \beta(i)}} & \alpha \neq \beta,
\end{cases} \qquad \alpha, \beta \in \omega^{\omega}.
\end{aligned}
$$

First, notice that $d$ is in fact an ultrametric under which Baire space is separable and has no isolated points. By Example [%s](#example:ultrametric_has_nets), this ultrametric space has many layered-disjoint nets. We may find an effective one explicitly.

If $I \subset \omega$ is a finite set of indices with corresponding tuple of fixed values $\mathbf{x}_I = (x_i \in \omega : i \in I)$, then the **cylinder set above $\mathbf{x}_I$** is defined as the set:

$$
\begin{aligned}
C[\mathbf{x}_I] := \set{\alpha \in \omega^{\omega}}{\alpha(i) = x_i \text{ for all } i \in I}.
\end{aligned}
$$

Denote the countable collection of all such cylinder sets by $\mathcal{C}$: the usual collection of basic open sets which generates the product topology on Baire space. We see that $\mathcal{C}$ forms a mesh over Baire space. For any $n \in \omega$ and $\alpha \in \omega^{\omega}$, it holds that $\alpha \in C[\restrict{\alpha}{n}]$ and $\bigcap_n C[\restrict{\alpha}{n}] = \seq{\alpha}$, which forms an infinite, nesting sequence of net elements with diameters shrinking to zero under $d$. This gives (**M3**). But $\mathcal{C}$ is not a net on Baire space. The two incomparable cylinders $C[\alpha_0 = 0]$ and $C[\alpha_1 = 0]$ constitute a minimal counterexample to (**N4**): their intersection is yet another cylinder of the form $C[\restrict{\alpha}{2} = (0, 0)]$. Instead, we take the sub-collection $\mathcal{N} \subset \mathcal{C}$ comprising only those cylinders above tuples defined on initial segments of $\omega$: i.e., $\mathcal{N} := \set{C[\sigma]}{\sigma \in \omega^{<\omega}}$. In fact, this collection $\mathcal{N}$ generates the same product topology as $\mathcal{C}$ on Baire space, and further qualifies as a net.

Since any non-trivial intersection between two cylinders from $\mathcal{N}$ implies their comparability, we have (**N4**$'$). Notice too that the chain $\p{C[\restrict{\alpha}{n}]}_{n \in \omega} \subset \mathcal{C}$ we previously identified to represent a given sequence $\alpha$ only employs cylinders from $\mathcal{N}$. It is computable to obtain an enumeration of $\mathcal{N}$ respecting containment, and this enumeration can compute the containment relation, predecessor relation, and indices of any root elements (i.e., $C[()]$). Notice too that the diameter function on $\mathcal{N}$ is computable: for any $\sigma \in \omega^{<\omega}$,

$$
\begin{aligned}
\diam_d(C[\sigma]) = 2^{-\operatorname{len}(\sigma)}.
\end{aligned}
$$

So, the net $\mathcal{N}$ has a computable $\omega$-presentation $\mathscr{R}$, meaning $\mathcal{N}$ is an effective Rogers net on $(\omega^{\omega}, d)$. Moreover, selecting from each $C[\sigma]$ the point $\sigma ^\smallfrown 0^\omega$, one may effectively compute their pairwise distances using the enumeration of $\mathcal{N}$. So $(\omega^\omega, d, \mathcal{N}, \mathscr{R}, (\sigma^\smallfrown 0^\omega)_\sigma)$ constitutes a computable net space.
:::

:::{prf:example}
Consider the field of $p$-adic numbers $\mathbb{Q}_p$ where $p \in \omega$ is prime, along with the standard $p$-adic norm $\abs{\cdot}_p$. The $p$-adic norm actually induces an ultrametric on $\mathbb{Q}_p$ with computable dense subset $\mathbb{Q}$. By Example [%s](#example:ultrametric_has_nets), this ultrametric space has many layered-disjoint nets.

If $I$ is an initial segment of $\mathbb{Z}$ with corresponding tuple $\mathbf{a}_I = (a_i \in \seq{0, ..., p - 1} : i \in I)$ of fixed values–only finitely many of which may be non-zero–then the **cylinder set above $\mathbf{a}_I$** is defined as the set:

$$
\begin{aligned}
C[\mathbf{a}_I] := \set{x \in \mathbb{Q}_p}{x = \sum_{i \in \mathbb{Z}} x_i p^i, \quad \text{where} \quad x_i \in \seq{0, ..., p - 1}  \text{ and } x_i = a_i \text{ for all } i \in I}.
\end{aligned}
$$

We only permit tuples $\mathbf{a}_I$ of all zero values if $I$ is an initial segment containing $0$. Denote the countable collection of all cylinder sets above permitted tuples by $\mathcal{C}$: a collection of basic open sets which generates the product topology on $\mathbb{Q}_p$ (being the product of the topology on $\mathbb{Z}_p$, which is itself a product topology from the discrete topology on $\seq{0, ..., p - 1}$). We claim that $\mathcal{C}$ is an effective Rogers net on $\mathbb{Q}_p$.

Clearly, $\mathcal{C}$ is countable. A superset in $\mathcal{C}$ of a cylinder $C[\mathbf{a}_I] \in \mathcal{C}$ must be a cylinder above the nonzero restriction of $\mathbf{a}_I$ to some initial segment of $I$. There are only finitely many such restrictions, so we have (**M2**). For any $C[\mathbf{a}_I]$, if the restriction $C[\mathbf{a}_{I \setminus \seq{\max(I)}}]$ of $\mathbf{a}_I$ to the next shortest initial segment is a cylinder in $\mathcal{C}$, then $C[\mathbf{a}_{I \setminus \seq{\max(I)}}]$ is the immediate predecessor of $C[\mathbf{a}_I]$. Otherwise, $C[\mathbf{a}_I]$ has no immediate predecessor. It is straightforward to check that any two overlapping cylinders from $\mathcal{C}$ must be above tuples which agree on a common initial segment of $\omega$, so are necessarily comparable. This gives (**N4**$'$). Now, if $x \in \mathbb{Q}_p$, then $x$ is uniquely expressible in the form $p^{k} \cdot u$ for some $k \in \mathbb{Z}$ and invertible $u \in \mathbb{Z}^\times_p$, where $\mathbb{Z}_p$ is the ring of $p$-adic integers. Then $\p{C\brk{x [k, ..., k + n - 1]}}_{n \in \omega}$ is an infinite, nested chain of cylinders from $\mathcal{C}$ each containing $x$ and shrinking in diameter to zero, since,

$$
\begin{aligned}
\diam_p(C\brk{x[k, ..., k + n - 1]}) = p^{- (k + n)} \to 0 \quad \text{as} \quad n \to \infty.
\end{aligned}
$$

This gives (**M3**). We may index these cylinders by $\omega$ as follows: lexicographically order all of the tuples whose earliest non-zero value occurs at a common index $k$, where we consider the symbols to be ordered according to $0 < 1 < \cdots < p - 1 < \texttt{blank}$; then interleave those orders across all $k \in \mathbb{Z}$ in the fashion $k = 0, +1, -1, +2, -2, ...$. From this effective enumeration of $\mathcal{C}$, one may compute the containment relation, immediate predecessor relation, and the indices of all root elements (i.e., those tuples which are only non-zero on the last index of the initial segment on which they are defined). Moreover, the diameter function is computable from the index of the cylinder, so $\mathcal{C}$ is indeed an effective Rogers net on $\mathbb{Q}_p$. Finally, selecting the point $x = \sum_{i \in I} a_i p^i$ from $C[\mathbf{a}_I]$ provides a dense subset with computable pairwise distances. This dense subset and effective net $\mathcal{C}$ make $\mathbb{Q}_p$ a computable net space.
:::

## Comparison to Nicely Covered Metric Spaces

We may view the development of algorithmic information theory over net spaces as a generalization of the work done in {cite:t}`May14` for those metric spaces with computable nice covers. Let us recall the definition of a computably nicely covered metric space.

::::{prf:definition}
Let $(\Omega, d)$ be a metric space without isolated points. A **nice cover** of $\Omega$ is a sequence $(\mathcal{B}_n)_n$ with $\mathcal{B}_n \subseteq \mathcal{P}(\Omega)$ for each $n \in \omega$ satisfying the axioms:

:::{div}
:class: labeled-list
- (**A1**) For each $n \in \omega$ and each $U \in B_n$, we have $\abs{\set{V \in \mathcal{B}_{n + 1}}{V \subseteq U}} < \infty.$

- (**A2**) For each $n \in \omega$, each $U \in B_n$, and each $m < n$, there exists a unique $V \in \mathcal{B}_m$ such that $U \subseteq V$.

- (**A3**) For each $n \in \omega$, we have $\inf \set{\diam_d(U)}{U \in \mathcal{B}_n} > 0.$

- (**A4**) There exists $c \in \omega$ such that for each $A \subseteq \Omega$ with $0 < \diam_d(A) < 1$, there exists $\seq{U_1, ..., U_c} \subseteq \bigcup_n \mathcal{B}_n$ such that,

  $$
  \begin{aligned}
  A \subseteq \bigcup_{i = 1}^c U_i \quad \text{and} \quad (\forall i \in \omega) [\diam_d(U_i) < c \cdot \diam_d(A)].
  \end{aligned}
  $$
:::

Furthermore, if $(\mathcal{B}_n)_n$ is a nice cover of $\Omega$, $\Sigma$ is a finite alphabet, and $\delta: \Sigma^{<\omega} \to \bigcup_n \mathcal{B}_n$ is a bijection, then it is said that $(\Omega, (\mathcal{B}_n)_n, \delta)$ **has a computable nice cover** if both:

:::{div}
:class: labeled-list
- (**B1**) $\diam_d \circ\ \delta$ is a computable function, and
- (**B2**) The function $\operatorname{succ}: \Sigma^{<\omega} \times \omega \to \Sigma^{<\omega}$ on pairs $(w, n)$ satisfying $\delta(w) \in \mathcal{B}_n$, defined by $\operatorname{succ}(w, n) = \ang{w_1, ..., w_k}$ and $\set{V \in \mathcal{B}_{n + 1}}{V \subseteq \delta(w)} = \seq{\delta(w_1), ..., \delta(w_k)}$ is computable. That is, there is a computable map giving the indices of immediate successors of the cover element with the given index $w$.
:::
::::

:::{prf:proposition}
If $(\Omega, \delta)$ has a computable nice cover $(\mathcal{B}_n)_n$, then $\mathcal{N} := \bigcup_n \mathcal{B}_n$ is a layered-disjoint net on $\Omega$ with an $\omega$-presentation $\mathscr{R}$ computable in $\beta'$ (the Turing jump of $\beta$), where $\beta : \omega \to \Sigma^{<\omega}$ is some bijection such that $\delta \circ \beta : \omega \to \mathcal{N}$ is an indexing of $\mathcal{N}$ respecting set-inclusion.
:::

::::{prf:proof}
:nonumber:
We first check that the mesh and net axioms are met.

:::{div}
:class: labeled-list
- (**M1**) $\delta$ is a bijection between $\Sigma^{<\omega}$ and $\mathcal{N}$. So $\mathcal{N}$ is countable.

- (**M2**) By induction on the layer $n$, (**A2**) implies that the the number of supersets of an element of $\mathcal{N}$ is no greater than the layer at which the element lies.

- (**M3**) Let $x \in \Omega$ and fix $0 < \varepsilon < 1$. Since $x$ is not isolated, there exists a subset $x \in A \subseteq \Omega$ satisfying $0 < \diam_d(A) < \varepsilon$. Thus, by (**A4**), there exists $\seq{U_1, ..., U_c} \subseteq \mathcal{N}$ covering $A$ and satisfying $\diam_d (U_i) < c \cdot \diam_d (A)$ for each $1 \leq i \leq c$. Let $i$ be an index for which $x \in U_i$. Then,

  $$
  \begin{aligned}
  \diam_d(U_i) < c \cdot \diam_d(A) < c \cdot \varepsilon.
  \end{aligned}
  $$

  As $\varepsilon > 0$ was arbitrary, we may indeed find cover elements of arbitrarily small diameter covering $x$.

- (**N4**$'$) By induction on the layer $n$, no element of $\mathcal{N}$ may have two incomparable supersets from the cover $\mathcal{N}$ without violating (**A2**).
:::

Now, denote $\iota := \delta \circ \beta$. Then we may compute an $\omega$-presentation $\mathscr{R}$ of $\mathcal{N}$ as follows:

- By (**B2**), $\operatorname{in}: \omega^2 \to \seq{\top, \bot}$ may be defined by the $\Sigma_1$-formula in $\gamma$: that $\operatorname{in}(i, j)$ holds if and only if:

  $$
  \begin{aligned}
  \small
  (\exists n, C \in \omega) \brk{
  \begin{array}{l}
  (\text{$C$ is the code for the tuple $(i_1, ..., i_n) \in \omega^n$)}
  \\
  \AND \p{\beta(j) \in \operatorname{succ}\p{\beta(i), \operatorname{len}(\beta(i))}} \AND \cdots \AND \p{\beta(i_n) \in \operatorname{succ}\p{\beta(j), \operatorname{len}(\beta(j))}}
  \end{array}
  }.
  \end{aligned}
  $$

- By (**B2**), $\operatorname{pred}: \omega^2 \to \seq{\top, \bot}$ may be defined computably in $\beta$ by the formula:

  $$
  \begin{aligned}
  \operatorname{pred}(i, j) :\iff \beta(j) \in \operatorname{succ}\p{\beta(j), \operatorname{len}(\beta(j))}
  \end{aligned}
  $$

- By (**B1**), $\operatorname{diam}: \omega \to [0, \infty]$ may be defined computably in $\beta$ by the formula:

  $$
  \begin{aligned}
  \diam(i) := (\diam_d \circ\ \delta)(\beta(i)).
  \end{aligned}
  $$

- By (**B2**), $\operatorname{root} : \omega \to \seq{\top, \bot}$ may be defined by a $\Pi_1$-formula in $\beta$:

  $$
  \begin{aligned}
  \operatorname{root}(i) :\iff (\forall w \in \Sigma^{<\omega}) \brk{\beta(i) \not\in \operatorname{succ}(w, \operatorname{len}(w))}.
  \end{aligned}
  $$

Therefore, $\mathscr{R} = \ang{\operatorname{in}, \operatorname{pred}, \operatorname{diam}, \operatorname{root}}$ is an $\omega$-presentation of $\mathcal{N}$ computable from $\beta'$, as desired. Notice that the nice cover axioms (**A1**) and (**A3**) were not utilized in the course of this proof.
::::
