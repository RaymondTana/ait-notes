---
title: "Algorithmic Randomness"
label: section:Algorithmic_Randomness
---

We review the tests-based approach to algorithmic randomness, all with respect to a given {term}`premeasure`.

## Weights

:::{prf:definition}
:label: definition:weights
Let $\mathcal{V} \subseteq 2^{<\omega}$ be a collection of finite binary strings and $\rho$ be a premeasure on $2^\omega$. Define for $\mathcal{V}$ its:

- **Direct $\rho$-weight**: $\operatorname{DW}_\rho(\mathcal{V}) := \sum_{\sigma \in \mathcal{V}} \rho([\sigma])$,
- **Prefix $\rho$-weight**: $\operatorname{PW}_\rho(\mathcal{V}) := \sup \set{\operatorname{DW}_\rho(\mathcal{P})}{\mathcal{P} \subseteq \mathcal{V} \text{ is prefix-free}}$,
- **Vehement $\rho$-weight**: $\operatorname{VW}_\rho(\mathcal{V}) := \inf \set{\operatorname{DW}_\rho(\mathcal{W})}{\mathcal{W} \subseteq 2^{< \omega} \text{ and } [\mathcal{V}] \subseteq [\mathcal{W}]}$.
:::

When working with the $s$-dimensional {term}`Hausdorff premeasure` $\rho_s$ for some $s \geq 0$, we might simply write $\operatorname{DW}_s(\mathcal{V})$ for the **direct $s$-weight** of $\mathcal{V}$, and similar for the other weight notions.

For any $\mathcal{V} \subseteq 2^{<\omega}$, we defined $\widehat{\mathcal{V}}$ on the [Notation](#section:Notation) page to include only those strings in $\mathcal{V}$ which are minimal with respect to the prefix relation. Then $\widehat{\mathcal{V}}$ is {term}`prefix-free` and satisfies $[\widehat{\mathcal{V}}] = [\mathcal{V}]$. Using this fact, it is straightforward to verify that the above weight notions are ordered as follows:

$$
\begin{aligned}
\operatorname{VW}_\rho(\mathcal{V}) \leq \operatorname{PW}_\rho(\mathcal{V}) \leq  \operatorname{DW}_\rho(\mathcal{V}).
\end{aligned}
$$

These covering weights also relate to the $s$-dimensional {term}`Hausdorff outer measures <Hausdorff outer measure>`. In particular, if $\mathcal{H}^s(X) < c$ for some dimension parameter $s \geq 0$, constant $c > 0$, and subset $X \subseteq 2^\omega$, then it follows that for every $r \in \omega$, there exists a collection of finite binary strings $S \subseteq 2^{\geq r}$ such that $X \subseteq [S]$ and $\operatorname{DW}_s(S) < c$.

## Tests

We introduce some test notions, or effective schemes for identifying null-sets with respect to some premeasure. For the rest of the section, we will only consider upper-semicomputable premeasures on $2^\omega$. This restriction is made to ensure the collection of all tests of some type is uniformly-c.e. By relativizing these tests to some {term}`oracle`, one could expand the class of premeasures considered to those which are upper-semicomputable in $B$.

:::{prf:definition}
:label: definition:tests
Let $\rho$ be an upper-semicomputable premeasure on $2^\omega$. Suppose $\mathcal{U} = (U_n)_{n \in \omega}$ is a uniformly-c.e. sequence of collections $U_n \subseteq 2^{<\omega}$ of finite binary strings. Then define $\mathcal{U}$ to be:

- a **Martin-Löf-$\rho$-test** if $\operatorname{DW}_\rho(U_n) \leq 2^{-n}$ for all $n \in \omega$,
- a **strong Martin-Löf-$\rho$-test** if $\operatorname{PW}_\rho(U_n) \leq 2^{-n}$ for all $n \in \omega$, and
- a **vehement Martin-Löf-$\rho$-test** if $\operatorname{VW}_\rho(U_n) \leq 2^{-n}$ for all $n \in \omega$.

And if $\mathcal{V} \subseteq 2^{<\omega}$ is a c.e. collection of finite binary strings, define $\mathcal{V}$ to be:

- a **Solovay-$\rho$-test** if $\operatorname{DW}_\rho(\mathcal{V}) < + \infty$, and
- a **strong Solovay-$\rho$-test** if $\operatorname{PW}_\rho(\mathcal{V}) < + \infty$.
:::

We use $\mathcal{T}$ as a placeholder for any one of the above test notions. Once again, for any Hausdorff premeasure $\rho_s$ with $s > 0$ being left-c.e., we simplify each of the above terms as **$\mathcal{T}$-$s$-tests**. And when $s = 1$, we might simply refer to them as **$\mathcal{T}$-tests**. Furthermore, any one of these test notions may be {term}`relativized <Relativization>` to an oracle $B \in 2^{\leq \omega}$, regarding computable-enumerability as in $B$. We may refer to such tests as **$\mathcal{T}$-$B$-$\rho$-tests**.

A Martin-Löf-$\rho$-test (or ML-$\rho$-test) is the strictest notion of test we have defined, meaning from any Martin-Löf-$\rho$-test $\mathcal{U}$, one may produce a $\mathcal{T}$-$\rho$-test for any of the other test notions $\mathcal{T}$. In fact, such a $\mathcal{U}$ is already both a strong and vehement ML-$\rho$-test, and generates the collection $\mathcal{V} := \bigcup_n U_n$ which is a (strong) Solovay-$\rho$-test. Of course, any strong ML-$\rho$-test is also a vehement ML-$\rho$-test, and any Solovay-$\rho$-test is already a strong Solovay-$\rho$-test.

## Covers

Tests act as effective covers of subsets of Cantor space.

:::{prf:definition}
:label: definition:test_coverings
Let $\rho$ be an upper-semicomputable premeasure on $2^\omega$ and $X \subseteq 2^\omega$ be a subset.

- Let $\mathcal{U} = (U_n)_{n \in \omega}$ be a (possibly strong or vehement) Martin-Löf-$\rho$-test. Then $\mathcal{U}$ is said to **cover** $X$ whenever $X \subseteq \bigcap_{n} U_n$. Otherwise, $X$ is said to have **passed** $\mathcal{U}$.
- Alternatively, let $\mathcal{V}$ be a (possibly strong) Solovay-$\rho$-test. Then $\mathcal{V}$ is said to **cover** $X$ whenever, for each $x \in X$, there are infinitely many $r \in \omega$ for which $\restrict{x}{r} \in \mathcal{V}$. Otherwise, $X$ is said to have **passed** $\mathcal{V}$.
:::

For a fixed test notion $\mathcal{T}$ (e.g., Martin-Löf) and upper-semicomputable premeasure $\rho$ on $2^\omega$, an infinite binary string $x \in 2^\omega$ is said to be $\mathcal{T}$-$\rho$-**random** if $\seq{x}$ passes all $\mathcal{T}$-$\rho$-tests. Otherwise, $\seq{x}$ is covered by some such test, exhibiting itself to be (effectively) **$\mathcal{T}$-$\rho$-null**.

Note that if $\rho$ is an upper-semicomputable, Hausdorff premeasure (i.e., the premeasure associated to an upper-semicomputable {term}`dimension function` $h$ as described in Section [%s](#section:Measures_and_Hausdorff_Dimension)), being $\mathcal{T}$-$\rho$-null for any of the test notions $\mathcal{T}$ defined here implies being $\mathcal{H}^\rho$-null. Suppose, for instance, that $\mathcal{U}$ were a vehement ML-$\rho$-test and $\delta > 0$. Then, it is possible to show that there exists a sequence $(W_n)_{n \in \omega}$ where each $W_n \subseteq 2^{<\omega}$ consists of strings of diameter no greater than $\delta$ and is such that $[U_n] \subseteq [W_n]$ and $\operatorname{DW}_\rho(W_n) \leq 2 \cdot 2^{-n}$. If $\mathcal{V} = \bigcup_n W_n$, then

$$
\begin{aligned}
\sum_{\sigma \in \mathcal{V}} \mathcal{H}_\delta^\rho([\sigma]) = \sum_n \sum_{\sigma \in W_n} \operatorname{DW}_\rho([\sigma]) = \sum_n \operatorname{DW}_\rho(W_n) \leq \sum_n 2 \cdot 2^{-n} < \infty.
\end{aligned}
$$

Since $\delta > 0$ was arbitrary, $\mathcal{H}^\rho$ is an outer measure, and $X \subseteq \limsup_{\sigma \in \mathcal{V}} [\sigma]$, the (first) Borel-Cantelli lemma implies $\mathcal{H}^\rho(X) = 0$. Additionally, supposing $\mathcal{V}$ were a strong Solovay-$\rho$-test covering $X$ and $\delta > 0$, then we could restrict $\mathcal{V}$ to only those strings of diameter no more than $\delta$ while maintaining $\mathcal{V}$ being a strong Solovay-$\rho$-test covering $X$. Then, for each $\varepsilon > 0$, it is possible to show that there exists a prefix-free subset $\mathcal{P} \subseteq \mathcal{V}$ such that $[\mathcal{V}] \subseteq [\mathcal{P}]$ and $\operatorname{DW}_\rho(\mathcal{P}) < \varepsilon$. Then, by monotonicity, $\mathcal{H}^\rho_\delta(X) \leq \operatorname{DW}_\rho(\mathcal{P}) < \varepsilon$. And since both $\delta, \varepsilon > 0$ were arbitrary, we conclude $X$ is $\mathcal{H}^\rho$-null.

For any upper-semicomputable premeasure $\rho$ on $2^\omega$ and any of the above test notions $\mathcal{T}$, it follows from the property that $\mathcal{H}^\rho$ is an outer measure that the set of non-$\mathcal{T}$-$\rho$-randoms is $\mathcal{H}^\rho$-null.

Weaker randomness notions come from stricter test notions. So, the class of Martin-Löf-$\rho$-randoms contains all the other classes of $\mathcal{T}$-$\rho$-randoms discussed here.

## More Covering Notions

Let us start by reviewing some definitions originally appearing in {cite:t}`KT01` (and re-appearing slightly differently in {cite:t}`Orp21`).

:::{prf:definition}
:label: definition:strongly_covers
A countable collection $(X_i)_{i \in \omega}$ of sets **strongly covers** another set $X$ if each element of $X$ is also an element of infinitely many $X_i$.
:::

Note that in Definition [%s](#definition:test_coverings), we consider $X$ to be covered by a Solovay-type test if that test strongly covers $X$ in the sense of Definition [%s](#definition:strongly_covers).

:::{prf:definition}
:label: definition:delta_ball_covering_number
For any (bounded) set $X \subseteq \mathbb{R}^m$ and $\delta > 0$, define,

$$
\begin{aligned}
N(X, \delta) := \min \set{\abs{Y}}{\text{$Y$ is a set of $\delta$-balls covering $X$}}.
\end{aligned}
$$
:::

The quantity $N(X, \delta)$ is exactly what appears in the definitions of the box-counting dimensions, as it captures the least number of $\delta$-balls required to cover $X$ (see {cite:p}`Fal90`). This fractal dimension always bounds the {term}`Hausdorff dimension` from above.

:::{prf:definition}
:label: definition:C_delta_s_set
Fix $m \in \omega$, and let $s, \delta > 0$ and $C \geq 1$. A finite set $P \subseteq \mathbb{R}^m$ is called a **$(C, \delta, s)$-set** if for any $x \in \mathbb{R}^m$ and $\delta \leq \varepsilon \leq 1$,

$$
\begin{aligned}
\abs{P \cap B_\varepsilon(x)} \leq C \cdot \p{\frac{\varepsilon}{\delta}}^s.
\end{aligned}
$$
:::

Suppose that $X \subseteq \mathbb{R}^m$ has $\dim_{\operatorname{H}} X = s$. Then any $(C, \delta, s)$-set will have no more points in $X$ than a constant times what any $\delta$-net on $X$ would. That is, $(C, \delta, s)$-sets are spread out such that they never dedicate many points to sets of small Hausdorff dimension.

Note that it is not vital that we use $r$-balls in these definitions for $N(X, \delta)$ or $(C, \delta, s)$-sets. For instance, replacing these with dyadic cubes of comparable side-lengths would produce roughly equivalent notions.

Over Euclidean space, there is a relationship between Hausdorff dimension and $(C, \delta, s)$-sets. For instance, a set of Hausdorff dimension less than $s$ will have a $(C, \delta, s)$-set whose $\delta$-neighborhood strongly covers the set. The precise result originally appeared in {cite:t}`KT01` by N. Katz and T. Tao, but was simplified and slightly generalized by T. Orponen in {cite:t}`Orp21`.

:::{prf:lemma} Lemma 7.5 of {cite:t}`KT01`; Lemma 2.1 of {cite:t}`Orp21`
:label: lemma:Katz_Tao
Let $0 < s \leq m$ and let $X \subseteq \mathbb{R}^m$ be a subset with $\dim_{\operatorname{H}} X < s$. Then, there exists a constant $C \geq 1$ depending only on $m$, $s$, and $\dim_{\operatorname{H}} X$ such that: for every $k \in \omega$, there exists a $(Ck^2, 2^{-k}, s)$-set $P_k$ such that the sequence $\p{B_{C_m \cdot 2^{-k}}(P_k)}_{k \in \omega}$ strongly covers $X$, where $C_m \geq 1$ only depends on $m$.
:::

The above lemma was leveraged by Orponen to generalize a weak form of the Marstrand-Mattila Projection Theorem for arbitrary subsets of Euclidean space (Theorem 1.3 of {cite:t}`Orp21`). We will present an effective proof of the Katz-Tao lemma later in Section [5.1](https://raymondtana.github.io/my_assets/documents/Raymond%20Tana%20PhD%20Dissertation.pdf#nameddest=section.5.1).

Also recall the related notion of an **optimal cover** originally by J. Miller {cite:p}`Mil11`.

:::{prf:definition}
:label: definition:optimal_cover
Let $\rho$ be a premeasure on $2^\omega$ and $S \subseteq 2^{<\omega}$. Then a **$\rho$-optimal cover** of $S$ is a set $S^* \subseteq 2^{<\omega}$ satisfying $[S] \subseteq [S^*]$ and $\operatorname{DW}_\rho(S^*) = \operatorname{VW}_\rho(S)$.
:::

Optimal covers witness the vehement $\rho$-weight of a set. In general, it is unclear whether optimal covers exist. However, a result by P. Hudelson proves a necessary condition for the existence of optimal covers.

:::{prf:lemma} Theorem 3.4.22 of {cite:t}`Hud13`
:label: lemma:exists_optimal_cover_for_convex
Let $\rho$ be a {term}`convex <Convex premeasure>` Hausdorff premeasure on $2^\omega$. Then, for all $S \subseteq 2^{<\omega}$, there exists a $\rho$-optimal cover of $S$.

In particular, if $\rho$ is also computable and $S$ is c.e., then one may find another c.e. set $A$ (uniformly in $\rho$ and $S$) such that $\widehat{A}$ is a $\rho$-optimal cover of $S$.
:::

Essential to the proof of Lemma [%s](#lemma:exists_optimal_cover_for_convex) is the fact that whenever $\rho$ is convex and $\sigma \in 2^{<\omega}$, then $\seq{\sigma}$ is the $\operatorname{DW}_\rho$-minimal cover of $[\sigma]$ among all other collections $S \subseteq \bbrk{\sigma}$ covering $[\sigma]$.

Observe that an optimal cover will necessarily be prefix-free by minimality. When $\rho = \rho^s$, simplify the term to an **$s$-optimal cover**. Optimal covers were originally employed by Miller to construct a $\Delta^0_2$-definable real with effective dimension equal to $1 / 2$ yet unable to compute any real of greater effective dimension {cite:p}`Mil11`. We will make use of optimal covers for effectivizing Lemma [%s](#lemma:Katz_Tao) in Section [5.1](https://raymondtana.github.io/my_assets/documents/Raymond%20Tana%20PhD%20Dissertation.pdf#nameddest=section.5.1).
