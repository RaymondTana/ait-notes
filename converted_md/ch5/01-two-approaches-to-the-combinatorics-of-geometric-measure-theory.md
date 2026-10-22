---
title: "Two Approaches to the Combinatorics of Geometric Measure Theory"
label: section:Effective_versions_of_Combinatorial_Proofs
---

We continue the discussion from Section [%s](#section:Algorithmic_Randomness) on $(C, \delta, s)$-sets and their relation with Hausdorff dimension. To set up our discussion, let us recall more notation from {cite:t}`Mat95`. For any natural numbers $0 < n < m$, the notation $G(m, n)$ refers to the **Grassmannian manifold** of all $n$-dimensional subspaces of $\mathbb{R}^m$. Whenever $V \in G(m, n)$, let $\pi_V : \mathbb{R}^m \to V$ denote to the orthogonal projection onto $V$. We take the usual operator norm $\norm{\cdot}$ for linear maps as our metric on $G(m, n)$. Let $\mathcal{O}(m)$ denote the **$m$-dimensional orthogonal group**, which consists of all linear maps $g : \mathbb{R}^m \to \mathbb{R}^m$ preserving the inner product in $\mathbb{R}^m$. Considering the **Haar measure** $\theta_m$ on $\mathcal{O}(m)$, which is an invariant probability measure uniformly distributed on $\mathcal{O}(m)$, then $\gamma_{m, n}$ will denote the unique orthogonally-invariant, Radon probability measure on $G(m, n)$ arising from this Haar measure. That is, for any $X \subseteq G(m, n)$ and any fixed $V_0 \in X$,

$$
\begin{aligned}
\gamma_{m, n}(X) :=  \theta_m(\set{g \in \mathcal{O}(m)}{g(V_0) \in X}).
\end{aligned}
$$

See Section 3.9 in {cite:t}`Mat95` for more details. One celebrated fact about how Hausdorff dimension behaves under orthogonal projections onto subspaces of $\mathbb{R}^m$ is commonly known as **the Marstrand-Mattila Projection Theorem**.

:::{prf:theorem} Marstrand-Mattila Projection Theorem; c.f. Theorem 5.8 in {cite:t}`Mat15`
:label: theorem:marstrand_projection_original
Let $0 < n < m$ and $X \subseteq \mathbb{R}^m$ be analytic. Then,

$$
\begin{aligned}
\dim_{\operatorname{H}} \pi_V(X) = \min \seq{\dim_{\operatorname{H}} X, n} \qquad \text{for $\gamma_{m, n}$-almost all $V \in G(m, n)$}.
\end{aligned}
$$
:::

The $n = 1$ case of Theorem [%s](#theorem:marstrand_projection_original)–as well as other basic facts about how Hausdorff dimension behaves under translations, intersections, and Cartesian products–now have alternative, effective proofs involving an application of the Point-to-Set Principle {cite:p}`LS17; Lut21`. Such effective proofs offer the advantage of refining what “almost all” means usually by finding a sufficiently strong notion of algorithmic randomness which witnesses the theorem.

In particular, N. Lutz and D. Stull in {cite:t}`LS17` found an effective proof that the conclusion of the $n = 1$ case of the Marstrand-Mattila Projection Theorem still holds under the alternate hypothesis that $\dim_{\operatorname{H}} X = \dim_{\operatorname{P}} X$. Shortly after, D. Stull extended this conclusion for a broader class of sets which are said to possess **optimal oracles** {cite:p}`Stu21`, a condition which has not yet been fully characterized in non-computability theoretic terms.

However, there was a non-computability theoretic response to the version of the Marstrand-Mattila Projection Theorem under the condition that Hausdorff and packing dimensions agree. Namely, T. Orponen in {cite:t}`Orp21` employed combinatorial methods to extend the result to all $0 < n < m$ (see Theorem 1.2 in {cite:t}`Orp21`).

He further proved that a weaker conclusion holds for **any** subset of $\mathbb{R}^m$.

:::{prf:theorem} Theorem 1.3 in {cite:t}`Orp21`
:label: theorem:Orponen_weak_Marstrand
Let $0 < n < m$ and $X \subseteq \mathbb{R}^m$. Then

$$
\begin{aligned}
\dim_{\operatorname{P}} \pi_V(X) = \min \seq{\dim_{\operatorname{H}} X, n} \qquad \text{for $\gamma_{m, n}$-almost all $V \in G(m, n)$}.
\end{aligned}
$$
:::

Two lemmas appear to be essential in Orponen's proofs of his Theorems 1.2 and 1.3. The first was the **Katz-Tao Lemma** (Lemma [%s](#lemma:Katz_Tao)) claiming the existence of $(C, \delta, s)$-sets strongly covering subsets of Hausdorff dimension less than $s$. The other lemma is stated below. Roughly, it claims that any bounded set appearing at precision $\delta$ to have upper box-counting dimension no more than $s$ can be partitioned into a “bad” part which has small $s$-dimensional $\infty$-content, and a “good” part covered by some $(C, \delta, s)$-set.

::::{prf:lemma} Lemma 2.3 in {cite:t}`Orp21`
:label: lemma:Lemma_2.3_of_Orponen
Let $0 \leq s \leq m$, $\delta > 0$, $C \geq 1$, and $X \subset \mathbb{R}^m$ be a bounded subset with $N(X, \delta) \leq C \cdot \delta^{-s}$. Then, for any $L \geq 1$, there exists a disjoint decomposition $X = X_{\operatorname{good}} \sqcup X_{\operatorname{bad}}$ such that

:::{div}
:class: roman-list
1. $\mathcal{H}^s_{\operatorname{I}}(X_{\operatorname{bad}}) \leq C_m / L$, where $C_m$ only depends on $m$, and
1. $X_{\operatorname{good}}$ is contained in the $\delta$-neighborhood of a $(CL, \delta, s)$-set.
:::
::::

Our main goal is to prove both these lemmas using incompressibility arguments. It is already well known that Kolmogorov complexity may be used for proving combinatorial statements, including in many of the examples from Chapter 6 of {cite:t}`LV08`. The typical advantage of an argument based on Kolmogorov complexity is in its ability to identify objects with a desired property as those which are sufficiently incompressible. And standard counting arguments show that most objects in a space should be incompressible. For simplicity, we will present these arguments over Cantor space. So let us tailor the definition of a $(C, \delta, s)$-set to this setting.

:::{prf:definition}
:label: definition:C_k_s_set
Fix $m \in \omega$ and let $s > 0$, $k \in \omega$, and $C \geq 1$. A finite set $P \subseteq (2^{<\omega})^m$ is called a **$(C, 2^{-k}, s)$-set** if for any $\tau \in (2^{\leq k})^m$,

$$
\begin{aligned}
\abs{P \cap \bbrk{\tau}} \leq C \cdot \p{\frac{2^{-\operatorname{len}(\tau)}}{2^{-k}}}^s.
\end{aligned}
$$
:::

Note that in this setting, if $P \subseteq (2^k)^m$ is a collection of $m$-tuple of strings all with equal length $k$, then $[P]$ is the $(\sqrt{m} \cdot 2^{-k})$-neighborhood about $P$ (regarding $P$ as the set of all its elements extended by an infinite tail of zeros).

We start with Lemma [%s](#lemma:Katz_Tao). The only change we have made to its statement is a small improvement in the constant term from $Ck^2$ to $Ck$.

:::{prf:proposition} Lemma [%s](#lemma:Katz_Tao), restated
:label: proposition:Katz_Tao_restated
Let $0 < s \leq m$ and let $X \subseteq (2^{\omega})^m$ be a subset with $\dim_{\operatorname{H}} X < s$. Then there exists a constant $C \geq 1$ depending only on $m$, $s$, and $\dim_{\operatorname{H}} X$ such that: for every $k \in \omega$, there exists a $(Ck, 2^{-k}, s)$-set $P_k$ such that the sequence $\p{B_{C_m \cdot 2^{-k}}(P_k)}_{k \in \omega}$ strongly covers $X$, where $C_m \geq 1$ only depends on $m$.
:::

:::{prf:proof}
:nonumber:
Let $B$ be a Hausdorff oracle for $X$. Fix $C_m = \sqrt{m}$ and take $\varepsilon \in \mathbb{Q}_{> 0}$ such that $\operatorname{dim}_{\operatorname{H}} X < s - \varepsilon$. Let us begin with a natural guess for such a strong cover. Start by defining the set of $m$-tuples of finite binary strings with bounded prefix complexity relative to $B$:

$$
\begin{aligned}
S := \set{\sigma \in \p{2^{< \omega}}^m}{K^B(\sigma) < (s - \varepsilon) \operatorname{len}(\sigma) + K^B(\operatorname{len}(\sigma)) - c},
\end{aligned}
$$

where the constant $c > 0$ comes from item (ii) in Chaitin's Counting Theorem [%s](#theorem:chaitin_counting_theorem) relativized to $B$. For a fixed $j \in \omega$, denote the slice of $S$ of length $j$:

$$
\begin{aligned}
S_j := S \cap (2^{j})^m.
\end{aligned}
$$

We claim that the sequence $([S_j])_{j \in \omega}$ must strongly cover $X$. The Point-to-Set Principle [%s](#theorem:PTS_for_H_dimension) guarantees that no $x \in X$ may have all but finitely many of its prefixes in $S$, or else $\dim_{\operatorname{H}} X \geq \dim^B(x) \geq s - \varepsilon$. Now, by the Counting Theorem [%s](#theorem:chaitin_counting_theorem),

$$
\begin{aligned}
\abs{S_j} \leq 2^{(s - \varepsilon) \cdot j}.
\end{aligned}
$$

Notice too that all elements in $S_j$ are mutually at a distance at least $2^{-j}$-apart, but $S_j$ is not necessarily a $(Cj, 2^{-j}, s)$-set. Instead, for each $j$, we let $S^*_j$ represent the the **$s$-optimal cover** of $S_j$ in the sense of Definition [%s](#definition:optimal_cover). That is, we find an $S^*_j$ consisting of $m$-tuples of strings of equal length at most $j$ such that $[S_j] \subseteq [S^*_j]$ and $S^*_j$ is of minimal direct $s$-weight. This minimum exists because we know the direct $s$-weight of $S_j$ satisfies:

$$
\begin{aligned}
\operatorname{DW}_s(S_j) = \sum_{\sigma \in S_j} 2^{- s \cdot \operatorname{len}(\sigma)} = \abs{S_j} \cdot 2^{-s \cdot j} \leq 2^{(s - \varepsilon) \cdot j} \cdot 2^{- s \cdot j} = 2^{- \varepsilon \cdot j}.
\end{aligned}
$$

This implies our search for $S^*_j$ should not consider strings of length shorter than $\varepsilon j / s$ (nor longer than $j$). Next, for fixed $j, k \in \omega$, stratify the elements of the optimal $s$-cover $S^*_j$ by their string-length $k$:

$$
\begin{aligned}
S^*_{j,k} := S^*_j \cap (2^{k})^m.
\end{aligned}
$$

We first claim that each $S^*_{j,k}$ is a $(C_m, 2^{-k}, s)$-set. Indeed, for any $k \in \omega$ and $\tau \in (2^{\leq k})^m$,

$$
\begin{aligned}
2^{-s \cdot k} \cdot \abs{S^*_{j,k} \cap \bbrk{\tau}} = \sum \set{2^{- s \cdot \operatorname{len}(\sigma)}}{\sigma \in S^*_{j, k} \AND \sigma \succeq \tau} \leq C_m \cdot 2^{-s \cdot \operatorname{len}(\tau)}.
\end{aligned}
$$

Now for each $k \in \omega$, collect into $P_k := \bigcup_{j \in \omega} S^*_{j, k}$ all the strings across the $S^*_{j, k}$. We claim that each such batch $P_k$ is a $(C k, 2^{-k}, s)$-set, where $C = C_m s / \varepsilon$. Since $S^*_{j, k} = \emptyset$ whenever $k < \varepsilon j / s$, we may more precisely write:

$$
\begin{aligned}
P_k = \bigcup_{j = 0}^{\floor{ks / \varepsilon}} S^*_{j, k}.
\end{aligned}
$$

So, for any $\tau \in (2^{\leq k})^m$, each $S^*_{j, k}$ being a $(C_m, 2^{-k}, s)$-set implies for any $k > 0$:

$$
\begin{aligned}
\abs{P_k \cap \bbrk{\tau}} \leq \sum_{j = 1}^{\floor{ks / \varepsilon}} \abs{S^*_{j, k} \cap \bbrk{\tau}} \leq C_m \cdot \frac{ks}{\varepsilon} \cdot \p{\frac{2^{-\operatorname{len}(\tau)}}{2^{-k}}}^s.
\end{aligned}
$$

Finally, we show that $X$ is indeed strongly covered by the sequence $([P_k])_{k \in \omega}$.

Fix $x \in X$. Since the $([S_j])_j$ strongly cover $X$, there exist infinitely many $j$ for which $x \in [S_j] \subseteq [S^*_j]$. For each such $j$, there exists a corresponding $k \geq \varepsilon j / s$ such that $x \in [S^*_{j, k}] \subseteq [P_k]$. Thus, it also holds that there exist infinitely many $k$ for which $x \in [P_k]$.
:::

Now we move on to Lemma 2.3 in {cite:t}`Orp21`.

::::{prf:proposition} Lemma 2.3 in {cite:t}`Orp21` over Cantor Space
:label: proposition:effective_good_bad_decomp_Cantor
Let $s \in [0, m]$, $k \in \omega$, $C \geq 1$, and $X \subseteq (2^\omega)^m$ be bounded with $N(X, 2^{-k}) \leq C \cdot 2^{s \cdot k}$. Then for any $L \geq 1$, there exists a disjoint decomposition $X = X_{\operatorname{good}} \sqcup X_{\operatorname{bad}}$ such that

:::{div}
:class: roman-list
1. $\mathcal{H}^s_{\operatorname{I}}(X_{\operatorname{bad}}) \leq C_m/L$, where $C_m$ only depends on $m$, and
1. $X_{\operatorname{good}}$ is contained in the $(C_m \cdot 2^{-k})$-neighborhood of a $(CL, 2^{-k}, s)$-set.
:::
::::

:::{prf:proof}
:nonumber:
Let us fix a set of “bad strings”: all those strings of length at most $k$ with an extension into $X$ and of sufficiently small complexity,

$$
\begin{aligned}
S_{\operatorname{bad}} := \set{\sigma \in (2^{\leq k})^m}{[\sigma] \cap X \neq \emptyset \quad \text{and} \quad K(\sigma) < s \cdot \operatorname{len}(\sigma) - \log L}.
\end{aligned}
$$

Take $X_{\operatorname{bad}} = [S_{\operatorname{bad}}]$ to be the open set generated by $S_{\operatorname{bad}}$. Then, by the Kraft Inequality [%s](#theorem:kraft_inequality),

$$
\begin{aligned}
\mathcal{H}^s_{\operatorname{I}}(X_{\operatorname{bad}}) \leq \operatorname{DW}_s(S_{\operatorname{bad}}) = \sum_{\sigma \in S_{\operatorname{bad}}} 2^{- s \cdot \operatorname{len}(\sigma)} \leq \frac{1}{L} \sum_{\sigma \in S_{\operatorname{bad}}} 2^{-K(\sigma)} \leq \frac{1}{L}.
\end{aligned}
$$

This verifies (i) in the claim. Now, put $X_{\operatorname{good}} := X \setminus X_{\operatorname{bad}}$, and $S_{\operatorname{good}} := \restrict{X_{\operatorname{good}}}{k} = \set{\sigma \in (2^{k})^m}{[\sigma] \cap X_{\operatorname{good}} \neq \emptyset}$. Then,

$$
\begin{aligned}
X_{\operatorname{good}} \subseteq [\restrict{X_{\operatorname{good}}}{k}] = [S_{\operatorname{good}}],
\end{aligned}
$$

i.e., $X_{\operatorname{good}}$ is contained in the $(C_m \cdot 2^{-k})$-neighborhood of $S_{\operatorname{good}}$.

It remains to show that $S_{\operatorname{good}}$ is a $(CL, 2^{-k}, s)$-set in order to conclude (ii). Fix an arbitrary $\tau \in (2^{\leq k})^m$. If $\tau \in S_{\operatorname{bad}}$, we would have $[\tau] \subseteq X_{\operatorname{bad}}$, so $S_{\operatorname{good}} \cap \bbrk{\tau} = \emptyset$. Now assume that $\tau \not\in S_{\operatorname{bad}}$.

By the assumption on $N(X, 2^{-k})$, we may bound the $k$-precision prefix complexity of any $x \in X$ from above via a two-part description for $\restrict{x}{k}$. Fixing an enumeration of the minimal-cardinality c.e. covering of $X$ by $2^{-k}$-balls,

$$
\begin{aligned}
K(\restrict{x}{k}) \leq \log N(X, 2^{-k}) + O(1) \leq s \cdot k + \log C + O(1).
\end{aligned}
$$

The same bound holds for any $\sigma \in \restrict{X}{k}$:

```{math}
:label: equation:complexity_bound_for_strings_in_X_k
\begin{aligned}
K(\sigma) \leq s \cdot \operatorname{len}(\sigma) + \log C + O(1).
\end{aligned}
```

Suppose $\sigma \succeq \tau$ for $\sigma \in \restrict{X}{k}$. Then by applying both the Coding Theorem [%s](#theorem:coding_theorem) and the Counting Theorem [%s](#theorem:chaitin_counting_theorem) (ii) to ([%s](#equation:complexity_bound_for_strings_in_X_k)), we deduce that $\tau$ has at most

$$
\begin{aligned}
2^{K(\sigma) - K(\tau) + K(k) + O(\log \operatorname{len}(\tau)) + O(1)}
\end{aligned}
$$

many descriptions of length $K(\sigma) + O(\log \operatorname{len}(\tau)) + O(1)$ (each $\sigma \in \restrict{X}{k}$ extending $\tau$ computes $\tau = \restrict{\sigma}{\operatorname{len}(\tau)}$). Now, use that $\tau \not\in S_{\operatorname{bad}}$ to bound the number of extensions of $\tau$ which are “good”:

$$
\begin{aligned}
\abs{S_{\operatorname{good}} \cap \bbrk{\tau}} &= \abs{\set{\sigma \in \restrict{X_{\operatorname{good}}}{k}}{\sigma \succeq \tau}}\\
&\leq \max \set{2^{K(\sigma) - K(\tau) +  K(k) + O(\log \operatorname{len}(\tau)) + O(1)}}{\sigma \in \restrict{X}{k}}\\
&\leq 2^{(s \cdot k + \log C + O(1)) - (s \operatorname{len}(\tau) - \log L) + o(k)}\\
&= 2^{s(k - \operatorname{len}(\tau)) + \log C + \log L + o(k)} \\
&\leq C' L \p{\frac{2^{-\operatorname{len}(\tau)}}{2^{-k}}}^s.
\end{aligned}
$$

One could adjust the definition of $S_{\operatorname{bad}}$ in the beginning to absorb the extra sub-exponential terms contributing to $C'$, resulting in a collection $S_{\operatorname{good}}$ which indeed is a $(C L, 2^{-k}, s)$-set.
:::

We discuss here how to relate the above proof with that found in {cite:t}`Orp21`. The original proof forms $X_{\operatorname{bad}}$ as a union of all so-called **heavy** dyadic cubes, i.e., those dyadic cubes $Q \in \mathcal{Q}^m$ which contain a sufficiently many smaller sub-cubes $Q'$ of a fixed side-length $2^{-k}$ intersecting with $X$:

$$
\begin{aligned}
\bigcup \set{Q}{\abs{\set{Q'}{\ell(Q') = 2^{-k} \text{ and }  Q' \subseteq Q \text{ and }  Q' \cap X \neq \emptyset}} \geq \alpha \cdot L \cdot \p{\frac{\ell(Q)}{2^{-k}}}^s},
\end{aligned}
$$

where $\alpha$ is $C$ times a small constant depending on $m$, and $\ell(Q)$ denotes the side-length of $Q$. Following a strict translation between Euclidean and Cantor spaces (and omitting relativization to Hausdorff oracles), our proof could have defined $X_{\operatorname{bad}}$ to be the union of all infinite extensions of **heavy** strings, i.e., finite strings which may be extended to sufficiently many strings of length $k$ whose infinite extension intersects with $X$:

$$
\begin{aligned}
\brk{\set{\sigma}{\abs{\set{\tau \succeq \sigma}{[\tau] \cap X \neq \emptyset \text{ and } K(\tau) \leq s \cdot \operatorname{len}(\tau)}} \geq \alpha \cdot L \cdot \p{\frac{2^{-\operatorname{len}(\sigma)}}{2^{-k}}}^s}}.
\end{aligned}
$$

The only liberty we have taken in the above translation is to add an incompressibility condition on $\tau$, making the “bad” set even more restrictive.

In particular, any such heavy string has many **long descriptions** using each of the length $k$ strings $\tau$ of bounded complexity extending $\sigma$ and intersecting with $X$. Together with $\operatorname{len}(\sigma)$, such a string $\tau$ suffices to compute $\sigma$ by truncation. The Coding Theorem [%s](#theorem:coding_theorem) guarantees that $\sigma$ having many such long descriptions implies that $\sigma$ has at least one short description. In particular, $\sigma$ having at least $\alpha \cdot L \cdot 2^{s(k - \operatorname{len}(\sigma)) + K(k)}$ many descriptions $\langle\tau^*, \operatorname{len}(\sigma) \rangle$ of length at most $K(\tau) + K(\operatorname{len}(\sigma)) + O(1) \leq sk + o(k)$ guarantees

$$
\begin{aligned}
K(\sigma) \leq \p{s \cdot k + o(k)} - \log \brk{\alpha \cdot L \cdot 2^{s(k - \operatorname{len}(\sigma)) + K(k)}} = s \cdot \operatorname{len}(\sigma) - \log L - \log \alpha + o(k).
\end{aligned}
$$

This essentially places $\sigma$ in the canonical $S_{\operatorname{bad}}$ set from our proof, or its open cylinder $\brk{\sigma}$ in the canonical $X_{\operatorname{bad}}$ from our proof. That is, we may view the effective analog of $S_{\operatorname{bad}}$ as defined by Orponen as a subset of our bad set of strings.

Finally, this result effectivizes for a restricted class of subsets. For instance,

::::{prf:corollary}
:label: corollary:effective_good_bad_decomp_Cantor
Let $s \in [0, m] \cap \mathbb{Q}$, $k \in \omega$, $C \geq 1$, and $X \subseteq (2^\omega)^m$ be a bounded $\Sigma^0_1$-class with $N(X, 2^{-k}) \leq C \cdot 2^{s \cdot k}$. Then for any rational $L \geq 1$, there exists a disjoint decomposition $X = X_{\operatorname{good}} \sqcup X_{\operatorname{bad}}$ with $X_{\operatorname{good}} \in \Pi^0_1$ and $X_{\operatorname{bad}} \in \Sigma^0_1$ such that

:::{div}
:class: roman-list
1. $\mathcal{H}^s_{\operatorname{I}}(X_{\operatorname{bad}}) \leq C_m/L$, where $C_m$ only depends on $m$, and
1. $X_{\operatorname{good}}$ is contained in the $(C_m \cdot 2^{-k})$-neighborhood of a $(CL, 2^{-k}, s)$-set.
:::
::::
