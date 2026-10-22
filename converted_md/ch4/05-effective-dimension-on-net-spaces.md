---
title: "Effective Dimension on Net Spaces"
label: section:Effective_Dimension_on_Net_Spaces
---

In this section we extend the results of Section [%s](#section:Effective_Hausdorff_Dimension) by introducing and comparing multiple real-valued functions on a mesh space which attempt to capture the information density of individual points. For the rest of the section, fix a represented mesh space $(\Omega, \mathcal{N}, \mathscr{R})$. For notational convenience, if $\dim$ is a dimension on subsets of $\Omega$, we will sometimes use $\dim(x)$ for $\dim(\seq{x})$.

## Local Dimension of Semimeasures

From any mesh semimeasure, we may produce a Billingsley-type, algorithmic, pointwise dimension. Define the **local dimension** of a (discrete or continuous) mesh semimeasure as follows.

:::{prf:definition}
If $\mathsf{m}$ is a (discrete or continuous) mesh semimeasure on $\mathcal{N}$, the **(lower) local dimension of $x \in \Omega$ under $\mathsf{m}$ with respect to $\mathcal{N}$** is:

$$
\begin{aligned}
\dim_{\operatorname{loc}} \mathsf{m}(x) = \inf \set{\liminf_{n \to \infty} \frac{\log \mathsf{m}(i_n)}{\log \diam(i_n)}}{(i_n)_n \in \mathcal{R}(x)},
\end{aligned}
$$

where the ratio is defined to be zero whenever $\diam(i_n) = 0$. And if $X \subseteq \Omega$, then the **(lower) local dimension of $\mathsf{m}$ on $X$ with respect to $\mathcal{N}$** is:

$$
\begin{aligned}
\dim_{\operatorname{loc}} \mathsf{m}(X) = \sup_{x \in X} \dim_{\operatorname{loc}} \mathsf{m}(x).
\end{aligned}
$$
:::

Given a represented mesh space $(\Omega, \mathcal{N}, \mathscr{R})$, we let $\mathbf{M}_{\mathscr{R}}$ and $\mathbf{m}_{\mathscr{R}}$ be the optimal semimeasures constructed in Theorems [%s](#prop:exists_optimal) and [%s](#prop:exists_optimal_discrete), respectively. As $\mathscr{R}$ is fixed in this section, we may drop the reference to it in the notation, writing $\mathbf{M}$ and $\mathbf{m}$.

Just as $\mathbf{M}$ is a multiplicatively-largest, lower-semicomputable (in $\mathscr{R}$) continuous mesh semimeasure on $\mathcal{N}$, its local dimension $\dim_{\operatorname{loc}} \mathbf{M}$ is the multiplicatively-largest local dimension arising from lower-semicomputable continuous mesh semimeasures. We call $\dim_{\operatorname{loc}}\mathbf{M}(\cdot)$ the **(lower) continuous local dimension (with respect to mesh $(\Omega, \mathcal{N}, \mathscr{R})$)**, which is invariant under any choice of optimal semimeasure $\mathbf{M}$.

Similarly, as $\mathbf{m}$ is the multiplicatively-largest, lower-semicomputable (in $\mathscr{R}$) discrete mesh semimeasure on $\mathcal{N}$, its local dimension $\dim_{\operatorname{loc}} \mathbf{m}$ is the multiplicatively-largest local dimension arising from lower-semicomputable discrete mesh semimeasures. We call $\dim_{\operatorname{loc}}\mathbf{m}(\cdot)$ the **(lower) discrete local dimension (with respect to mesh $(\Omega, \mathcal{N}, \mathscr{R})$)**, which is invariant under any choice of optimal semimeasure $\mathbf{m}$.

## Constructive Dimension

Following J. Lutz's work over Cantor space in {cite:t}`Lut00`, we define the **constructive dimension** $\operatorname{cdim}(x)$ of a point $x$ as the infimum over all $s \geq 0$ for which there exists a constructive $s$-mesh-supergale succeeding on $x$.

:::{prf:definition}
For any subset $X \subseteq \Omega$, the **(weak) constructive dimension of $X$ (with respect to $(\Omega, \mathcal{N}, \mathscr{R})$)** is defined as:

$$
\begin{aligned}
\small
\operatorname{cdim}(X) &= \inf \set{s \geq 0}{\text{there is an $\mathscr{R}$-constructive $s$-mesh-supergale succeeding on $X$} }\\
&= \inf \set{s \geq 0}{\begin{array}{c} \text{there is am $\mathscr{R}$-lower-semicomputable continuous} \\ \text{mesh semimeasure $s$-succeeding on $X$} \end{array}}.
\end{aligned}
$$
:::

Note that we may as well define constructive dimension with respect to any optimal lower-semicomputable continuous mesh semimeasure, since if some $M \in \mathcal{M}$ were to indeed $s$-succeed on $X$, then so too would $\mathbf{M}$ $s$-succeed on $X$:

$$
\begin{aligned}
\operatorname{cdim}(X) &= \inf \set{s \geq 0}{(\exists M \in \mathcal{M})(\forall x \in X)(\exists (i_n)_n \in \mathcal{R}(x)) \brk{\limsup_{n \to \infty} \frac{M(i_n)}{\operatorname{diam}(i_n)^s} = + \infty}} \\
&= \inf \set{s \geq 0}{(\forall x \in X)(\exists (i_n)_n \in \mathcal{R}(x)) \brk{\limsup_{n \to \infty} \frac{\mathbf{M}(i_n)}{\operatorname{diam}(i_n)^s} = + \infty}}.
\end{aligned}
$$

As the success notions for continuous semimeasures and supergales coincide, we see:

:::{prf:proposition}
For any represented mesh space $(\Omega, \mathcal{N}, \mathscr{R})$ and any subset $X \subseteq \Omega$,

$$
\begin{aligned}
\dim_{\operatorname{loc}} \mathbf{M}(X) = \operatorname{cdim}(X).
\end{aligned}
$$
:::

## Incompressibility Dimension

:::{prf:definition}
The **(lower) incompressibility ratio of a subset $X \subseteq \Omega$ (with respect to $(\Omega, \mathcal{N}, \mathscr{R})$)** is defined in two manners:

$$
\begin{aligned}
\underline{\gamma}(X) := \sup_{x \in X} \liminf_{r \to \infty} \frac{\mathbf{G}_r(x)}{r}, \quad \text{and} \quad   \underline{\eta}(X) := \sup_{x \in X} \liminf_{r \to \infty} \frac{\mathbf{H}_r(x)}{r}.
\end{aligned}
$$
:::

Over net spaces, the incompressibility ratio $\underline{\gamma}$ and the local continuous dimension $\dim_{\operatorname{loc}}\mathbf{M}$ coincide.

:::{prf:theorem}
:label: theorem:incompressibility_ratio=local_dimension
For any represented net space $(\Omega, \mathcal{N}, \mathscr{R})$ and subset $X \subseteq \Omega$,

$$
\begin{aligned}
\dim_{\operatorname{loc}} \mathbf{M} (X) = \underline{\gamma}(X).
\end{aligned}
$$
:::

::::{prf:proof}
:nonumber:
Let us show that $\dim_{\operatorname{loc}} \mathbf{M}(X) \geq \underline{\gamma}(X)$. Take any rational $s > \dim_{\operatorname{loc}} \mathbf{M}(X)$. For each $\ell \in \omega$, define the set of indices:

$$
\begin{aligned}
A_\ell := \set{i \in \omega}{\frac{\mathbf{M}(i)}{\diam(i)^{s}} \geq 2^\ell}.
\end{aligned}
$$

Then, for any $\ell \in \omega$, since $\mathbf{M}$ is $[0,1]$-valued, it holds that for any $i \in A_\ell$,

```{math}
:label: eqn:i_in_A_ell
\begin{aligned}
\diam(i) \leq \p{\mathbf{M}(i) \cdot 2^{-\ell}}^{1 / s} \leq 2^{-\ell / s}.
\end{aligned}
```

**Claim**: If $\mathcal{E} \subseteq \omega$ is a prefix-free collection of indices of net elements (i.e., having a prefix-free collection of addresses in the forest $\mathcal{G}$ associated to $\mathcal{N}$), then for any $r \in \omega$,

$$
\begin{aligned}
\abs{B_r \cap \mathcal{E}} \leq 2^{-\ell + rs + s}, \quad \text{where} \quad B_r := \set{i \in A_\ell}{\diam(i) > 2^{- r - 1}}.
\end{aligned}
$$

:::{prf:proof}
:nonumber:
For each $k \in \omega$ satisfying $\operatorname{root}(k)$, let $\mathcal{E}^k$ denote the collection of indices in $\mathcal{E}$ for subsets of the root element with index $k$, i.e.,

$$
\begin{aligned}
\mathcal{E}^k := \set{i \in \mathcal{E}}{\operatorname{in}(i, k)}.
\end{aligned}
$$

Then, by $\mathcal{E}^k \sqsubseteq_{\operatorname{PF}} k$, the Generalized Kraft Inequality (Proposition [%s](#prop:generalized_Kraft_inequality)), the continuous net semimeasure property ([%s](#eqn:boundedness_continuous_mesh_semimeasure_condition)), and the definition of $B_r$:

$$
\begin{aligned}
1 \geq \sum_{\operatorname{root}(k)} \mathbf{M}(k) &\geq \sum_{\operatorname{root}(k)} \sum_{i \in B_r \cap \mathcal{E}^k} \mathbf{M}(i)\\
&\geq \sum_{\operatorname{root}(k)} \sum_{i \in B_r \cap \mathcal{E}^k} 2^{\ell} \cdot \diam(i)^s\\
&\geq \sum_{\operatorname{root}(k)} \sum_{i \in B_r \cap \mathcal{E}^k} 2^{\ell} \cdot 2^{s(- r - 1)} = \abs{B_r \cap \mathcal{E}} \cdot 2^{\ell - rs - s}.
\end{aligned}
$$
:::

One may enumerate the elements of $A_\ell$ effectively in $\mathscr{R}$. Build a set $\mathcal{E}_\ell \subseteq A_\ell$ of indices of mutually-incomparable net elements by only enumerating into $\mathcal{E}_\ell$ those newly enumerated indices of $A_\ell$ incomparable to all indices already enumerated into $\mathcal{E}_\ell$. For any $i \in \mathcal{E}_\ell$ with $\diam(i) > 0$, ([%s](#eqn:i_in_A_ell)) implies that there exists some natural number $r \geq \ceil{\ell / s}$ with $2^{-r - 1} < \diam(i) \leq 2^{-r}$, so $i \in B_r$. Using the two-part description of $i \in B_r \cap \mathcal{E}_\ell$, we see by the claim above that:

$$
\begin{aligned}
K^{\mathscr{R}}(i) \leq r s + s - \ell + O(\log r) + O(\log \ell).
\end{aligned}
$$

Fix $x \in X$. By assumption, $\mathbf{M}$ $s$-succeeds on $x$, so $x$ has an $\mathcal{N}$-name intersecting $A_\ell$ for arbitrary large $\ell \in \omega$. If that name settles on a net element of diameter zero, then $\mathbf{G}_r(x) = O(1)$ for sufficiently large $r$. Otherwise, for every $\ell \in \omega$, there exists $i_\ell \in \mathcal{E}_\ell$ with $\diam(i_\ell) > 0$ such that $x \in \iota(i_\ell)$, giving,

$$
\begin{aligned}
\liminf_{r \to \infty} \frac{\mathbf{G}_r(x)}{r} &\leq \liminf_{r \to \infty} \frac{rs + s - \ell + O(\log r) + O(\log \ell)}{r} \leq s.
\end{aligned}
$$

Taking a supremum over all $x \in X$, we finish the proof in this direction.

In the other direction, take rationals $s > s' > s'' > \underline{\gamma}(X)$. Put

$$
\begin{aligned}
A := \set{i \in \omega}{K^{\mathscr{R}}(i) \leq -s' \cdot \log \diam(i)},
\end{aligned}
$$

where $\log(0)$ is defined to be $-\infty$. This set is c.e. in $\mathscr{R}$. Define the map,

$$
\begin{aligned}
M(i) := \sum_{\substack{j \in A \\
\operatorname{in}(j, i)}} \diam(j)^{s'}.
\end{aligned}
$$

In words, the sum defining $M$ considers all net elements which are subsets of the $i$-th net element and which have bounded complexity. This map is well-defined (and, in fact, satisfies the bounding property ([%s](#eqn:boundedness_continuous_mesh_semimeasure_condition))) by the Kraft Inequality [%s](#theorem:kraft_inequality):

$$
\begin{aligned}
\sum_{\operatorname{root}(k)} M(k) \leq \sum_{j \in A} \diam(j)^{s'} \leq \sum_j 2^{-K^{\mathscr{R}}(j)} \leq 1.
\end{aligned}
$$

We claim $M$ is an $\mathscr{R}$-lower-semicomputable continuous net semimeasure.

Lower-semicomputability is clear from having computable access to the containment relation and $\diam$, as well as by $K^{\mathscr{R}}(i)$ being upper-semicomputable in $\mathscr{R}$. The continuous net semimeasure property ([%s](#eqn:continuous_mesh_semimeasure_condition)) holds since $M$ satisfies the recursive rule:

$$
\begin{aligned}
M(i) &= \sum_{\operatorname{pred}(i, j)} M(j) + \begin{cases}  \diam(i)^{s'} & \text{if } i \in A \\ 0 & \text{otherwise} \end{cases}\\
&\geq \sum_{\operatorname{pred}(i, j)} M(j).
\end{aligned}
$$

This follows from the net axiom $(\mathbf{N4})$. So, $M \in \mathcal{M}$. And for any $i \in A$,

```{math}
:label: eqn:i_in_A
\begin{aligned}
M(i) \geq \diam(i)^{s'}.
\end{aligned}
```

Fix $x \in X$. By assumption, there are infinitely many $r \in \omega$ for which $\mathbf{G}_r(x) \leq r s''$. For each such $r$, fix $i_r \in \omega$ such that $x \in \iota(i_r)$, $\diam(i_r) \leq 2^{-r}$ and $K^{\mathscr{R}}(i_r) \leq r s''$. If any $\diam(i_r) = 0$, we are done. Otherwise, these conditions imply $i_r \in A$, so by ([%s](#eqn:i_in_A)),

$$
\begin{aligned}
\frac{M(i_r)}{\diam(i_r)^s} \geq \frac{\diam(i_r)^{s'}}{\diam(i_r)^s} = \diam(i_r)^{s' - s} \geq 2^{r(s - s')} \to \infty \text{ as } r \to \infty.
\end{aligned}
$$

So $M$ $s$-succeeds on $x$, and so too does $\mathbf{M}$. Therefore, $\mathbf{M}$ $s$-succeeds on all of $X$.
::::

:::{prf:corollary}
For any represented net space $(\Omega, \mathcal{N}, \mathscr{R})$ and subset $X \subseteq \Omega$,

$$
\begin{aligned}
\dim_{\operatorname{loc}} \mathbf{m}(X) = \dim_{\operatorname{loc}} \mathbf{M}(X).
\end{aligned}
$$

Therefore, the universal semimeasures in both the discrete and continuous senses produce the same local dimension notion over $\Omega$.
:::

:::{prf:proof}
:nonumber:
By Theorem [%s](#theorem:incompressibility_ratio=local_dimension), it suffices to show that $\dim_{\operatorname{loc}} \mathbf{m}(X) = \underline{\gamma}(X)$. This latter equality holds even over mesh spaces.

Suppose $\underline{\gamma}(X) < s \in \mathbb{Q}$. Fix $x \in X$. Then there exists a strictly-increasing sequence $(r_n)_n$ of natural numbers and a sequence of net elements $(N_n)_n \subseteq \mathcal{N}$ satisfying $x \in N_n$, $\diam(N_n) \leq 2^{-r_n}$, and $K^{\mathscr{R}}(N_n) \leq s \cdot r_n$ for all $n \in \omega$. Then, $(i_n)_n := (\iota^{-1}(N_n))_n \in \mathcal{R}(x)$ is a $\mathcal{N}$-name of $x$ satisfying,

$$
\begin{aligned}
- \frac{K^{\mathscr{R}}(i_n)}{\log \diam(i_n)} \leq \frac{s \cdot r_n}{r_n} = s,
\end{aligned}
$$

where the left-hand side is defined as $0$ when $\diam(i_n) = 0$. Thus, by the Coding Theorem [%s](#theorem:coding_theorem) relativized to $\mathscr{R}$, we have $\dim_{\operatorname{loc}} \mathbf{m}(x) \leq s$. As $x \in X$ was arbitrary, $\dim_{\operatorname{loc}} \mathbf{m}(X) \leq s$.

In the other direction, suppose $\dim_{\operatorname{loc}} \mathbf{m}(X) < s' < s \in \mathbb{Q}$. Fix $x \in X$. Then, $\dim_{\operatorname{loc}} \mathbf{m}(x) < s'$ as well. Again by the Coding Theorem [%s](#theorem:coding_theorem) relativized to $\mathscr{R}$, there exists an $\mathcal{N}$-name $(i_r)_r \in \mathcal{R}(x)$ satisfying for each $r \in \omega$:

$$
\begin{aligned}
-\frac{K^{\mathscr{R}}(i_r)}{\log \diam(i_r)} \leq s.
\end{aligned}
$$

Passing to a subsequence $(r_n)_n$ such that $\diam(i_{r_n}) \leq 2^{-n}$, which is possible by $\diam(i_r) \to 0$, we see:

$$
\begin{aligned}
\underline{\gamma}(x) \leq \liminf_{n \to \infty} \frac{K(i_{r_n})}{- \log \diam(i_{r_n})} \leq s.
\end{aligned}
$$

Thus, $\underline{\gamma}(X) \leq s$ as well.
:::

## Effective Hausdorff Dimension

Let us now present the effectivized Hausdorff approach for effective dimension over a mesh space. See {cite:t}`May14` for a comparison to the same notion for metric spaces with computable nice covers, or {cite:p}`Rei04; LM24` for that on Cantor space.

We start by generalizing two of the weights found in Section [%s](#section:Algorithmic_Randomness) to collections of mesh elements.

:::{prf:definition}
Fix a premeasure $\rho$ and a mesh $\mathcal{N}$ on $\Omega$. If $\mathcal{V}$ is a collection of indices of elements in $\mathcal{N}$, define the

- **Direct $\rho$-weight** of $\mathcal{V}$: $\operatorname{DW}_\rho(\mathcal{V}) := \sum_{i \in \mathcal{V}} \rho(\iota(i))$, and
- **Prefix $\rho$-weight** of $\mathcal{V}$: $\operatorname{PW}_\rho(\mathcal{V}) := \sup \set{\operatorname{DW}_\rho(\mathcal{E})}{\mathcal{E} \sqsubseteq_{\operatorname{PF}} \mathcal{V}}$.
:::

We may similarly extend some of the test notions as to those defined in Section [%s](#section:Algorithmic_Randomness) but now for mesh spaces. As before, we restrict the premeasure to be upper-semicomputable in the fixed $\omega$-presentation $\mathscr{R}$ of $\mathcal{N}$.

:::{prf:definition}
Fix an $\mathscr{R}$-upper-semicomputable premeasure $\rho$ on the mesh $\mathcal{N}$. Suppose $\mathcal{U} = (U_n)_{n \in \omega}$ denotes a uniformly-$\mathscr{R}$-c.e. sequence of collections of (indices of) mesh elements from $\mathcal{N}$. Then, define $\mathcal{U}$ to be:

- a **Martin-Löf-$\mathscr{R}$-$\rho$-test** if $\operatorname{DW}_\rho(U_n) \leq 2^{-n}$ for all $n \in \omega$; and
- a **strong Martin-Löf-$\mathscr{R}$-$\rho$-test**: if $\operatorname{PW}_\rho(U_n) \leq 2^{-n}$ for all $n \in \omega$.

And suppose $\mathcal{V}$ denotes an $\mathscr{R}$-c.e. collection of (indices of) mesh elements from $\mathcal{N}$. Then, define $\mathcal{V}$ to be:

- a **Solovay-$\mathscr{R}$-$\rho$-test** if $\operatorname{DW}_\rho(\mathcal{V}) < + \infty$; and
- a **strong Solovay-$\mathscr{R}$-$\rho$-test** if $\mathcal{V}$ if $\operatorname{PW}_\rho(\mathcal{V}) < + \infty$.
:::

Similarly to the case of Cantor space, we say that a point $x \in \Omega$ is **covered** by a test if $x$ has an $\mathcal{N}$-name which is covered by the test.

:::{prf:definition}
For any $\mathscr{R}$-upper-semicomputable premeasure $\rho$ on the mesh $\mathcal{N}$ and any subset $X \subseteq \Omega$,

- Let $\mathcal{U} = (U_n)_{n \in \omega}$ be a (strong) ML-$\mathscr{R}$-$\rho$-test. Then $\mathcal{U}$ is said to **cover** $X$ if for each $x \in X$, there exists an $\mathcal{N}$-name $(i_n)_n \in \mathcal{R}(x)$ of $x$ such that $i_n \in \bigcap_n U_n$. Otherwise, $X$ is said to have **passed** $\mathcal{U}$.
- Let $\mathcal{V}$ be a (strong) Solovay-$\mathscr{R}$-$\rho$-test. Then $\mathcal{V}$ is said to **cover** $X$ if for all $x \in X$, there exists an $\mathcal{N}$-name $(i_n)_n \in \mathcal{R}(x)$ of $x$ such that $i_r \in \mathcal{V}$ for infinitely many $r \in \omega$. Otherwise, $X$ is said to have **passed** $\mathcal{V}$.
:::

A point $x \in X$ is **ML-$\mathscr{R}$-$\rho$-random** if no ML-$\mathscr{R}$-$\rho$-test covers $x$. Analogous definitions apply for all ML-type and Solovay-type tests. And as is the case over Cantor space, there exists a universal ML-$s$-test for each left-c.e. $s > 0$.

:::{prf:proposition}
:label: prop:exists_universal_ML_s_test
For each left-c.e. $s > 0$, there exists a universal ML-$\mathscr{R}$-$s$-test. That is, there exists an ML-$\mathscr{R}$-$s$-test $\mathcal{U}^s = \seq{U^s_n}_n$ such that for any $X \subseteq \Omega$,

$$
\begin{aligned}
\text{$X$ is covered by some ML-$\mathscr{R}$-$s$-test} \iff \mathcal{U}^s \text{ covers $X$}.
\end{aligned}
$$
:::

:::{prf:proof}
:nonumber:
It is possible to compute from $\mathscr{R}$ an enumeration $(\mathcal{U}^{(k)})_k$ of all ML-$\mathscr{R}$-$s$-tests. This essentially follows from $s$-$m$-$n$ Theorem (see Theorem 1.5.5 of {cite:t}`Soa16`). Intuitively, an enumeration of all $\mathscr{R}$-c.e. sets can be converted into an enumeration of all ML-$\mathscr{R}$-$s$-tests by only enumerating those strings into the test which keep the direct $s$-weight of the corresponding layer in the test below the required bound.

For each $n$, define

$$
\begin{aligned}
U^s_n := \bigcup_{k} U^{(k)}_{n + k + 1}.
\end{aligned}
$$

It is clear that $\mathcal{U}^s := (U^s_n)_n$ is a uniformly $\mathscr{R}$-c.e. sequence. It further holds that $\mathcal{U}^s$ is an ML-$\mathscr{R}$-$s$-test since for each $n \in \omega$:

$$
\begin{aligned}
\operatorname{DW}_s(U^s_n) \leq \sum_{k = 0}^\infty \operatorname{DW}_s(U^{(k)}_{n + k + 1}) \leq \sum_{k = 0}^\infty 2^{-(n + k + 1)} \leq 2^{-n}.
\end{aligned}
$$

It is straightforward to verify that $\mathcal{U}^s$ is indeed universal among all ML-$\mathscr{R}$-$s$-tests.
:::

:::{prf:definition}
The **effective Hausdorff dimension (with respect to $(\Omega, \mathcal{N}, \mathscr{R})$)** of a subset $X \subseteq \Omega$ is defined as:

$$
\begin{aligned}
\operatorname{effdim}(X) = \inf \set{s \geq 0}{\text{$\mathcal{U}^s$ covers $X$}}.
\end{aligned}
$$

For a singular point $x \in \Omega$, define its **effective Hausdorff dimension (with respect to $(\Omega, \mathcal{N}, \mathscr{R})$)** as:

$$
\begin{aligned}
\operatorname{effdim}(x) := \inf \set{s > 0}{\text{$x$ is not ML-$\mathscr{R}$-$s$-random}}.
\end{aligned}
$$
:::

We may use the existence of a universal ML-$\mathscr{R}$-$s$-test to establish the Pointwise Stability of effective Hausdorff dimension restricted to a mesh.

:::{prf:proposition} Pointwise Stability
:label: prop:pointwise_stability_effective_dimension
For any represented mesh space $(\Omega, \mathcal{N}, \mathscr{R})$ and $X \subseteq \Omega$,

$$
\begin{aligned}
\operatorname{effdim}(X) = \sup_{x \in X} \operatorname{effdim}(x).
\end{aligned}
$$
:::

:::{prf:proof}
:nonumber:
That $\operatorname{effdim}(X) \geq \sup_{x \in X} \operatorname{effdim}(x)$ is clear since any ML-$\mathscr{R}$-$s$-test covering $X$ will also cover $\seq{x}$ for each $x \in X$.

In the reverse direction, assume $s > \sup_{x \in X} \operatorname{effdim}(x)$. Then, each $x \in X$ is covered by some ML-$\mathscr{R}$-$s$-test. In particular, each $x \in X$ is covered by the universal ML-$\mathscr{R}$-$s$-test, $\mathcal{U}^s$. So, $\mathcal{U}^s$ covers $X$, meaning $s \geq \operatorname{effdim}(X)$.
:::

This immediately implies the **total stability** of effective Hausdorff dimension restricted to a mesh: i.e., if $X = \bigcup_{i \in \mathcal{I}} X_i$ for some collection of subsets $X_i \subseteq \Omega$ indexed by $\mathcal{I}$, then $\operatorname{effdim}(X) = \sup_{i \in \mathcal{I}} \operatorname{effdim}(X_i)$.

There is a natural identification between the effectivized Hausdorff dimension restricted to a net and the lower incompressibility ratio $\underline{\gamma}$ over a net space.

:::{prf:theorem}
:label: theorem:effdim_H=incompressibility_ratio
For any represented net space $(\Omega, \mathcal{N}, \mathscr{R})$ and subset $X \subseteq \Omega$,

$$
\begin{aligned}
\operatorname{effdim}(X) = \underline{\gamma}(X).
\end{aligned}
$$
:::

::::{prf:proof}
:nonumber:
Let us start by showing $\operatorname{effdim}(X) \geq \underline{\gamma}(X)$. We appeal to Theorem [%s](#theorem:incompressibility_ratio=local_dimension) and instead prove $\operatorname{effdim}(X) \geq \dim_{\operatorname{loc}} \mathbf{M}(X)$. To that end, take any rationals $s > s' > \operatorname{effdim}(X)$, and let $X$ being ML-$\mathscr{R}$-$s$-null be witnessed by some ML-$\mathscr{R}$-$s$-test $\mathcal{U} = (U_n)_n$. Define the map $M: \omega \to \mathbb{R}$:

$$
\begin{aligned}
M(i) := \frac{1}{2} \sum_n n \sum_{\substack{j \in U_n \\
\operatorname{in}(j, i)}} \diam(j)^s.
\end{aligned}
$$

**Claim 1**: $M$ is a lower-semicomputable continuous net semimeasure in $\mathscr{R}$.

:::{prf:proof}
:nonumber:
$M$ is $\mathscr{R}$-lower-semicomputable as each $U_n$ is $\mathscr{R}$-c.e. and the containment relation $\operatorname{in}$ and diameter function $\diam$ are computable from $\mathscr{R}$. Partial sums can approximate $M(N)$ from below computably in $\mathscr{R}$. We make use of $(\mathbf{N4})$ to check the continuous net semimeasure properties ([%s](#eqn:continuous_mesh_semimeasure_condition)) and ([%s](#eqn:boundedness_continuous_mesh_semimeasure_condition)). Across the roots, we see

$$
\begin{aligned}
\sum_{\operatorname{root}(k)} M(k) = \frac{1}{2} \sum_n n \sum_{j \in U_n} \diam(j)^s \leq \frac{1}{2} \sum_n \operatorname{DW}_s(U_n) \leq \sum_n n \cdot 2^{-(n + 1)} = 1.
\end{aligned}
$$

And for $i \in \omega$, the map satisfies the recursive rule:

$$
\begin{aligned}
M(i) &= \sum_{\operatorname{pred}(i, j)} M(j) + \begin{cases} \frac{1}{2} n \cdot \diam(i)^s & \text{if } i \in U_n \\ 0 & \text{otherwise} \end{cases}\\
&\geq \sum_{\operatorname{pred}(i, j)} M(j).
\end{aligned}
$$
:::

**Claim 2**: $M$ $s$-succeeds on $X$.

:::{prf:proof}
:nonumber:
Since $\mathcal{U}$ covers $X$, for each $x \in X$ and $n \in \omega$, there exists $i_n \in U_n$ such that $x \in \iota(i_n)$. Note that $\diam(i_n)^{s} \leq 2^{-n}$ since $\mathcal{U}$ is an ML-$\mathscr{R}$-$s$-test. Therefore, $(i_n)_n \in \mathcal{R}(x)$ is an $\mathcal{N}$-name of $x$. If ever $\diam(i_n) = 0$, then we are done. Otherwise, the name satisfies:

$$
\begin{aligned}
\limsup_n \frac{M(i_n)}{\diam(i_n)^s} \geq \limsup_n \frac{\frac{1}{2}  n \cdot \diam(i_n)^s}{\diam(i_n)^s} = \limsup_n \frac{n}{2}  = \infty.
\end{aligned}
$$

Thus, $M$ $s$-succeeds on $X$.
:::

This suffices to show that $s \geq \underline{\gamma}(x)$.

In the other direction, take some rationals $s > s' > s'' > \underline{\gamma}(X)$. There is a uniform algorithm in $\mathscr{R}$ to enumerate the following family of sets, where $n \in \omega$,

$$
\begin{aligned}
U_n := \set{i \in \omega}{K^{\mathscr{R}}(i) \leq -s \cdot \log \diam(i) - n},
\end{aligned}
$$

where $\log(0)$ is defined to be $-\infty$.

We claim that $f$ is an ML-$\mathscr{R}$-$s$-test covering $X$. First, the Kraft Inequality [%s](#theorem:kraft_inequality) implies that for each $n$,

$$
\begin{aligned}
\sum_{i \in U_n} \diam(i)^s \leq \sum_{i \in U_n} 2^{-K^{\mathscr{R}}(i) - n} \leq 2^{-n}.
\end{aligned}
$$

All that remains is to show that $\mathcal{U}$ covers $X$. Fix $x \in X$ and $n \in \omega$. Take $r_0 \in \omega$ to be sufficiently large such that for all $r \geq r_0$,

$$
\begin{aligned}
(s - s')r > n.
\end{aligned}
$$

Then, by $\underline{\gamma}(X) < s'' < s'$, we have that there are infinitely many $r \geq r_0$ for which $K^{\mathscr{R}}_r(x) < s' r$. For each such $r$, by the definition of $K^{\mathscr{R}}_r$, there exists a net element of index $i_r \in \omega$ such that $x \in \iota(i_r)$, $\diam(i_r) \leq 2^{-r}$, and $K^{\mathscr{R}}(i) < s' r$; thus,

$$
\begin{aligned}
K^{\mathscr{R}}(i_r) < s' r < sr - n \leq -s \cdot \log\diam(i_r) - n.
\end{aligned}
$$

That is, $i_r \in U_n$. Thus, $X \subseteq \bigcap_n \bigcup_{i \in U_n} \iota(i)$. And so, $s \geq \operatorname{effdim}(X)$.
::::

## Local Dimension of Outer Measures

Again inspired by the Billingsley-type definition on the local dimension of an outer measure as in Falconer {cite:p}`Fal90`, we define the **local net dimension** of an outer measure on a computable net space.

:::{prf:definition}
If $\mu$ is an outer measure on computable mesh space $(\Omega, d, \mathcal{N}, \mathscr{R}, \alpha)$, the **(lower) local net dimension of $x \in \Omega$ under $\mu$** is:

$$
\begin{aligned}
\dim_{\operatorname{loc}} \mu(x) = \inf \set{\liminf_{n \to \infty} \frac{\log \mu(\iota(i_n))}{\log \diam(i_n)}}{(i_n)_n \in \mathcal{R}(x)}.
\end{aligned}
$$

And if $X \subseteq \Omega$, then the **(lower) local net dimension of $\mu$ on $X$** is:

$$
\begin{aligned}
\dim_{\operatorname{loc}} \mu(X) = \sup_{x \in X} \dim_{\operatorname{loc}} \mu(x).
\end{aligned}
$$
:::

:::{prf:proposition}
:label: proposition:computable_grate_spaces_same_local_dimension
For any computable grate space $(\Omega, d, \mathcal{N}, \mathscr{R}, \alpha)$ with layered-disjoint grate $\mathcal{N}$, and any subset $X \subseteq \Omega$,

$$
\begin{aligned}
\dim_{\operatorname{loc}} \boldsymbol{\kappa}(X) = \dim_{\operatorname{loc}} \mathbf{m}(X).
\end{aligned}
$$
:::

:::{prf:proof}
:nonumber:
This holds by a short algebraic argument. Given $N \in \mathcal{N}$, Proposition [%s](#proposition:computable_grate_space_complexities_agree) implies:

$$
\begin{aligned}
- \log \boldsymbol{\kappa}(N) = \mathbf{K}(N) = K_{\mathcal{N}}(N) \pm o\p{- \log \diam_d(N)} = - \log \boldsymbol{\mu}(N) \pm o\p{- \log \diam_d(N)},
\end{aligned}
$$

and so, for any $X \subseteq \Omega$,

$$
\begin{aligned}
\dim_{\operatorname{loc}} \boldsymbol{\kappa}(X) &= \sup_{x \in X} \inf_{(i_n)_n \in \mathcal{R}(x)} \liminf_{n \to \infty} \frac{\log \boldsymbol{\kappa}(\iota(i_n))}{\log \diam(i_n)}\\
&= \sup_{x \in X} \inf_{(i_n)_n \in \mathcal{R}(x)} \liminf_{n \to \infty} \frac{\log \boldsymbol{\mu}(\iota(i_n)) \pm o\p{- \log \diam(i_n)}}{\log \diam(i_n)}\\
&= \sup_{x \in X} \inf_{(i_n)_n \in \mathcal{R}(x)} \liminf_{n \to \infty} \frac{\log \mathbf{m}(i_n)}{\log \diam(i_n)}\\
&= \dim_{\operatorname{loc}} \mathbf{m}(X).
\end{aligned}
$$
:::

Computable grate spaces with layered-disjoint grates thus offer the most asymptotic coincidences. In particular, over these spaces, every form of algorithmic complexity presented in this section induces the same effective dimension notion. Note that Proposition [%s](#proposition:computable_grate_spaces_same_local_dimension) holds even when $\boldsymbol{\kappa}$ is replaced by any globally or locally optimal outer measure, including $\boldsymbol{\theta}$, $\boldsymbol{\mu}$, $\mathbf{Q}$, and $\mathbf{R}$ from the previous section.

## Summary of Asymptotic Coincidences

To summarize, we have the following theorem stating the various equalities between effective measures of information density introduced in this section over net spaces and grate spaces.

:::{prf:theorem}
:label: theorem:effective_dimension_net_spaces
For any represented net space $(\Omega, \mathcal{N}, \mathscr{R})$ and any subset $X \subseteq \Omega$,

$$
\begin{aligned}
\dim_{\operatorname{loc}}\mathbf{M}(X) = \dim_{\operatorname{loc}}\mathbf{m}(X) = \operatorname{cdim}(X) = \underline{\gamma}(X) = \operatorname{effdim}(X).
\end{aligned}
$$

Moreover, if $(\Omega, d, \mathcal{N}, \mathscr{R}, \alpha)$ is a computable grate space with a layered-disjoint grate, these quantities further coincide with $\underline{\eta}(X)$ and $\dim_{\operatorname{loc}}\boldsymbol{\kappa}(X)$.
:::

These collected results respond to some open questions posed in {cite:t}`LLM23`. In particular, we have developed Billingsley-type algorithmic dimensions over mesh spaces via mesh semimeasures, and shown how these dimensions coincide over net spaces and grate spaces. Second, they asked whether–over separable metric spaces–one could characterize algorithmic dimension via gales. In light of Proposition [%s](#prop:K_and_H_and_G_grate), we have indeed shown how algorithmic dimension is equivalently characterized from the perspectives of incompressibility, typicality, and unpredictability under some basic assumptions.
