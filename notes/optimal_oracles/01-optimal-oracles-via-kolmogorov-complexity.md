---
title: "Optimal Oracles via Kolmogorov Complexity"
label: section:Optimal_Oracles_via_Kolmogorov_Complexity
---

By the {term}`Point-to-Set Principle` (Theorem [%s](#theorem:PTS_for_H_dimension)), every set $X \subseteq \mathbb{R}^m$ has a {term}`Hausdorff oracle`: an oracle $A$ with $\sup_{x \in X} \dim^A(x) = \dim_{\operatorname{H}}(X)$. Hausdorff oracles are far from unique. Extra information never increases complexity, so if $A$ is a Hausdorff oracle for $X$, then so is the join of $A$ with any other oracle $B$. Applying the Point-to-Set Principle to that join gives, for every $\varepsilon > 0$, a point $x \in X$ with

$$
\begin{aligned}
\dim^{A, B}(x) \geq \dim_{\operatorname{H}}(X) - \varepsilon \geq \dim^A(x) - \varepsilon.
\end{aligned}
$$

So the information in $B$ cannot lower the dimension of every point of $X$. But dimension is a limit inferior: $K^{A, B}_r(x)$ may still fall far below $K^A_r(x)$ at infinitely many precisions $r$. D. Stull asked for an oracle that rules this out at almost every precision, for at least one point of nearly full dimension, against every competitor $B$ {cite:p}`Stu21`. This is the form of information that projection theorems consume. For instance, the projection estimate of J. Lutz and D. Stull (Theorem 21 of {cite:t}`Stu21`, from {cite:t}`LS17`) bounds $K^{C, \theta}_r(p_\theta z)$ from below only at those precisions $r$ where the oracle $(C, \theta)$ gives essentially no information about $z$, i.e., where $K^{C, \theta}_r(z) \geq K_r(z) - \varepsilon r$.

Throughout this page, $X \subseteq \mathbb{R}^m$. We write $A \oplus B$ for the join of two oracles $A$ and $B$, which computes both and is computable from any oracle computing both. We abbreviate $K^{A, B}_r(x) := K^{A \oplus B}_r(x)$, and similarly $\dim^{A, B}(x)$ and $\operatorname{Dim}^{A, B}(x)$, where $\dim^A(x)$ and $\operatorname{Dim}^A(x)$ are the lower and upper limits of $K^A_r(x) / r$. A point $y \in \mathbb{R}^m$ serves as an oracle through the binary expansions of its coordinates. The quantifier $(\forall^\infty r)$ is as on the [Notation](#section:Notation) page.

## Optimal Oracles

:::{prf:definition} Definitions 3 and 26 of {cite:t}`Stu21`
:label: definition:optimal_oracles
An oracle $A$ is an **optimal Hausdorff oracle** for $X$ if:

1. $A$ is a Hausdorff oracle for $X$; and
2. for every oracle $B$ and every $\varepsilon > 0$, there is a point $x \in X$ such that $\dim^{A, B}(x) \geq \dim_{\operatorname{H}}(X) - \varepsilon$ and

$$
\begin{aligned}
(\forall^\infty r) \brk{K^{A, B}_r(x) \geq K^A_r(x) - \varepsilon r}.
\end{aligned}
$$

Likewise, $A$ is an **optimal packing oracle** for $X$ if $A$ is a {term}`packing oracle` for $X$ and, for every oracle $B$ and every $\varepsilon > 0$, there is a point $x \in X$ satisfying $\operatorname{Dim}^{A, B}(x) \geq \dim_{\operatorname{P}}(X) - \varepsilon$ and the same inequality. We say that $X$ **has optimal Hausdorff oracles** (resp. **optimal packing oracles**) if some oracle is an optimal Hausdorff (resp. packing) oracle for $X$.
:::

Stull says "$A$ is Hausdorff optimal (resp. packing optimal) for $X$". The second condition asks only for a single point whose complexity the competitor $B$ fails to reduce by a linear amount at almost every precision. It is equivalent to asking for many such points. To state this, collect the points satisfying the inequality.

:::{prf:definition}
:label: definition:preservation_set
For oracles $A$, $B$ and $\varepsilon > 0$, the **preservation set** is

$$
\begin{aligned}
N_X(A, B, \varepsilon) := \set{x \in X}{(\forall^\infty r) \brk{K^{A, B}_r(x) \geq K^A_r(x) - \varepsilon r}}.
\end{aligned}
$$
:::

Stull writes $N(A, B, \varepsilon)$.

:::{prf:proposition} Propositions 4 and 27 of {cite:t}`Stu21`
:label: proposition:full_dimensional_preservation
Let $A$ be an oracle.

1. If $\dim_{\operatorname{H}}(X) > 0$, then $A$ is an optimal Hausdorff oracle for $X$ if and only if $A$ is a Hausdorff oracle for $X$ and $\dim_{\operatorname{H}}(N_X(A, B, \varepsilon)) = \dim_{\operatorname{H}}(X)$ for every oracle $B$ and every $\varepsilon > 0$.
2. If $\dim_{\operatorname{P}}(X) > 0$, then $A$ is an optimal packing oracle for $X$ if and only if $A$ is a packing oracle for $X$ and $\dim_{\operatorname{P}}(N_X(A, B, \varepsilon)) = \dim_{\operatorname{P}}(X)$ for every oracle $B$ and every $\varepsilon > 0$.
:::

:::{prf:proof}
We prove the first part; the second is the same argument with $\operatorname{Dim}$, $\dim_{\operatorname{P}}$, packing oracles, and the packing Point-to-Set Principle. Let $s := \dim_{\operatorname{H}}(X)$, and fix an oracle $B$ and $\varepsilon > 0$.

($\Leftarrow$) Let $G := N_X(A, B, \varepsilon)$. By the Point-to-Set Principle, $s = \dim_{\operatorname{H}}(G) \leq \sup_{x \in G} \dim^{A, B}(x)$. Since $s > 0$, the set $G$ is non-empty, and some $x \in G$ has $\dim^{A, B}(x) \geq s - \varepsilon$. This $x$ satisfies the second condition of Definition [%s](#definition:optimal_oracles).

($\Rightarrow$) Suppose instead that $d := \dim_{\operatorname{H}}(G) < s$ for $G := N_X(A, B, \varepsilon)$. Let $C$ be a Hausdorff oracle for $G$ and fix $0 < \delta < \min\seq{\varepsilon, s - d}$. The second condition, applied to the oracle $B \oplus C$ and tolerance $\delta$, gives $x \in X$ with $\dim^{A, B, C}(x) \geq s - \delta$ and $K^{A, B, C}_r(x) \geq K^A_r(x) - \delta r$ for all but finitely many $r$. If $x \in G$, then $\dim^{A, B, C}(x) \leq \dim^C(x) \leq d < s - \delta$, a contradiction. If $x \notin G$, then for infinitely many $r$,

$$
\begin{aligned}
K^{A, B, C}_r(x) \leq K^{A, B}_r(x) + O(1) < K^A_r(x) - \varepsilon r + O(1),
\end{aligned}
$$

which contradicts $K^{A, B, C}_r(x) \geq K^A_r(x) - \delta r$ for large such $r$, since $\delta < \varepsilon$.
:::

So a single surviving point upgrades to a full-dimensional set of surviving points. That set depends on $B$ and $\varepsilon$, and no single set serves every competitor. Indeed, if $x \in N_X(A, x, \varepsilon)$, then $K^A_r(x) \leq K^{A, x}_r(x) + \varepsilon r \leq K(r) + \varepsilon r + O(1)$ for all but finitely many $r$, so $\operatorname{Dim}^A(x) \leq \varepsilon$. Hence every point of $\bigcap_B N_X(A, B, \varepsilon)$ has $\operatorname{Dim}^A(x) \leq \varepsilon$, and by the packing Point-to-Set Principle this intersection has packing dimension, hence also Hausdorff dimension, at most $\varepsilon$.

The proposition excludes dimension zero, where an empty preservation set would also have dimension zero. That case is trivial.

:::{prf:observation}
:label: observation:dimension_zero_optimal_oracles
Every non-empty $X \subseteq \mathbb{R}^m$ with $\dim_{\operatorname{H}}(X) = 0$ has optimal Hausdorff oracles, and every non-empty $X$ with $\dim_{\operatorname{P}}(X) = 0$ has optimal packing oracles.
:::

:::{prf:proof}
Take $x_0 \in X$ and a Hausdorff oracle $A_0$ for $X$, and put $A := A_0 \oplus x_0$. Then $A$ is still a Hausdorff oracle for $X$. Given $B$ and $\varepsilon > 0$, the point $x_0$ satisfies $\dim^{A, B}(x_0) \geq 0 = \dim_{\operatorname{H}}(X)$. Since $A$ computes $x_0$, we have $K^A_r(x_0) \leq K(r) + O(1) \leq \varepsilon r$ for all but finitely many $r$, so $K^{A, B}_r(x_0) \geq 0 \geq K^A_r(x_0) - \varepsilon r$. The packing case is identical.
:::

## Known Results

Unless stated otherwise, the results below are due to {cite:t}`Stu21`, and are numbered as in the STACS 2022 version. First, the class of sets with optimal oracles is closed under the natural operations.

:::{prf:theorem} Lemmas 5, 28, and 30, Observations 6 and 29, and Proposition 7 of {cite:t}`Stu21`
:label: theorem:optimal_oracles_closure
The following hold for optimal Hausdorff oracles, and also for optimal packing oracles with $\dim_{\operatorname{P}}$ in place of $\dim_{\operatorname{H}}$.

1. If $A$ is an optimal oracle for $X$, then so is $A \oplus B$ for every oracle $B$.
2. If $Y \subseteq X$ has $\dim_{\operatorname{H}}(Y) = \dim_{\operatorname{H}}(X)$ and $Y$ has optimal oracles, then $X$ has optimal oracles.
3. If $X = \bigcup_{n \in \omega} X_n$ and every $X_n$ has optimal oracles, then $X$ has optimal oracles.
:::

Several classes of sets are known to have optimal oracles. Recall that $X$ is {term}`weakly regular` if $\dim_{\operatorname{H}}(X) = \dim_{\operatorname{P}}(X)$ (Definition [%s](#definition:packing_dimension)).

:::{prf:theorem} Theorem 13, Lemmas 15, 17, 32, and 34 of {cite:t}`Stu21`
:label: theorem:optimal_oracles_sufficient
Let $s := \dim_{\operatorname{H}}(X)$.

1. Every analytic set has optimal Hausdorff oracles and optimal packing oracles.
2. Every weakly regular set has optimal Hausdorff oracles and optimal packing oracles. Moreover, the join of a Hausdorff oracle and a packing oracle for a weakly regular set is an optimal Hausdorff oracle for it.
3. Suppose there is a metric outer measure $\mu$ with $0 < \mu(X) < \infty$ such that either $\mu \ll \mathcal{H}^{s - \delta}$ for every $0 < \delta \leq s$, or both $\mathcal{H}^s \ll \mu$ and $\mathcal{H}^s(X) > 0$. Then $X$ has optimal Hausdorff oracles.
:::

Theorem 33 of {cite:t}`Stu21` is a packing analogue of the third item, stated with packing measures. In the proof of the third item, $\mu$ is encoded into an oracle $A$, and a Borel–Cantelli argument shows that each set on which some competitor $B$ saves $\varepsilon r$ bits infinitely often is $\mu$-null. Either hypothesis then guarantees that deleting a $\mu$-null set from $X$ leaves Hausdorff dimension $s$; that is, $\overline{\dim}_{\operatorname{H}}(\mu \llcorner X) = s$ (Proposition [%s](#proposition:full_upper_dimension)). Taking $\mu := \mathcal{H}^s$ shows that every $X$ with $0 < \mathcal{H}^s(X) < \infty$ has optimal Hausdorff oracles (Corollary 14 of {cite:t}`Stu21`).

Stull also states that the existence of an {term}`exact gauge` for $X$ (Section [%s](#section:Measures_and_Hausdorff_Dimension)) suffices for optimal Hausdorff oracles. His paper derives this from the third item for gauges such as $t \mapsto t^s \log(1/t)$, whose null sets compare with those of $\mathcal{H}^{s - \delta}$ or $\mathcal{H}^s$. Note that Stull's gauges are continuous and strictly increasing dimension functions, and that his gauged measures cover by balls.

Whether every set has optimal oracles depends on the axioms of set theory.

:::{prf:theorem} Corollary 16 of {cite:t}`Stu21`
:label: theorem:optimal_oracles_AD
Assuming the Axiom of Determinacy (AD), every $X \subseteq \mathbb{R}^m$ has optimal Hausdorff oracles.
:::

The proof combines the analytic case with the theorem of L. Crone, L. Fishman, and S. Jackson that, under AD, every set has a Borel subset of the same Hausdorff dimension {cite:p}`CFJ20`. Recall that AD contradicts the Axiom of Choice.

:::{prf:theorem} Lemma 18, Theorems 20, 35, and 37, and Corollary 36 of {cite:t}`Stu21`
:label: theorem:optimal_oracles_AC_CH
Assume the Axiom of Choice (AC) and the Continuum Hypothesis (CH).

1. For every $s \in (0, m)$, there is a set $X \subseteq \mathbb{R}^m$ with $\dim_{\operatorname{H}}(X) = s$ that does not have optimal Hausdorff oracles.
2. For every $0 < s_1 < s_2 \leq 1$, there are sets $X \subseteq \mathbb{R}$ with $\dim_{\operatorname{H}}(X) = s_1$ and $\dim_{\operatorname{P}}(X) = s_2$ realizing each of the following: neither optimal Hausdorff nor optimal packing oracles; optimal Hausdorff oracles but no optimal packing oracles; optimal packing oracles but no optimal Hausdorff oracles.
:::

The original motivation for optimal oracles is Marstrand's projection theorem. For $\theta \in [0, \pi]$, let $p_\theta : \mathbb{R}^2 \to \mathbb{R}$ be the projection $p_\theta(z) := z_1 \cos \theta + z_2 \sin \theta$.

:::{prf:theorem} Theorem 22 of {cite:t}`Stu21`
:label: theorem:Marstrand_optimal_oracles
If $X \subseteq \mathbb{R}^2$ has optimal Hausdorff oracles, then for almost every $\theta \in [0, \pi]$,

$$
\begin{aligned}
\dim_{\operatorname{H}}(p_\theta X) = \min\seq{\dim_{\operatorname{H}}(X), 1}.
\end{aligned}
$$
:::

By Theorem [%s](#theorem:optimal_oracles_sufficient), this recovers Marstrand's theorem for analytic sets and the extension of {cite:t}`LS17` to weakly regular sets. Some hypothesis is needed: assuming AC and CH, for every $s \in (0, 1)$ there is a set $X \subseteq \mathbb{R}^2$ with $\dim_{\operatorname{H}}(X) = 1 + s$ but $\dim_{\operatorname{H}}(p_\theta X) = s$ for every $\theta \in (\pi/4, 3\pi/4)$ (Theorem 23 of {cite:t}`Stu21`). Optimal oracles have since been used to construct universal sets of directions for projection theorems {cite:p}`FS24`.

## Witness and Fitness

The two conditions in Definition [%s](#definition:optimal_oracles) play different roles. The first is a **witness** condition: $A$ attains the minimum in a point-to-set principle. The second is a **fitness** condition: $A$ cannot be improved, at almost every precision, by any competitor. We will see the same pair of conditions again when we replace oracles by classical objects, so we name the second one on its own.

:::{prf:definition}
:label: definition:fit_oracle
An oracle $A$ is **Hausdorff-fit** for $X$ if it satisfies the second condition of Definition [%s](#definition:optimal_oracles), and **packing-fit** for $X$ if it satisfies the packing version of that condition.
:::

A fit oracle need not be a Hausdorff oracle. For example, let $A$ be an optimal Hausdorff oracle for some $Y \subseteq \mathbb{R}^m$ with $\dim_{\operatorname{H}}(Y) < m$, and let $z \in \mathbb{R}^m$ have $\dim^A(z) = m$. Then $A$ is Hausdorff-fit for $X := Y \cup \seq{z}$, since the witnesses for $Y$ still serve, but $A$ is not a Hausdorff oracle for $X$. The witness condition nevertheless costs nothing when we only ask whether optimal oracles exist.

:::{prf:proposition}
:label: proposition:witness_condition_is_free
The following hold for Hausdorff oracles, and also for packing oracles with $\dim_{\operatorname{P}}$ in place of $\dim_{\operatorname{H}}$.

1. If $A$ is fit for $X$ and $A_0$ is a Hausdorff oracle for $X$, then $A \oplus A_0$ is an optimal Hausdorff oracle for $X$. In particular, $X$ has optimal Hausdorff oracles if and only if some oracle is Hausdorff-fit for $X$.
2. If $\dim_{\operatorname{H}}(X) > 0$, then $A$ is Hausdorff-fit for $X$ if and only if $\dim_{\operatorname{H}}(N_X(A, B, \varepsilon)) = \dim_{\operatorname{H}}(X)$ for every oracle $B$ and every $\varepsilon > 0$.
:::

:::{prf:proof}
For the first part, $A \oplus A_0$ is a Hausdorff oracle because $A_0$ is. Given $B$ and $\varepsilon > 0$, apply the fitness of $A$ to the oracle $A_0 \oplus B$ with tolerance $\varepsilon / 2$. This gives $x \in X$ with $\dim^{A, A_0, B}(x) \geq \dim_{\operatorname{H}}(X) - \varepsilon / 2$ and, for all but finitely many $r$,

$$
\begin{aligned}
K^{A, A_0, B}_r(x) \geq K^A_r(x) - \tfrac{\varepsilon}{2} r \geq K^{A, A_0}_r(x) - \tfrac{\varepsilon}{2} r - O(1) \geq K^{A, A_0}_r(x) - \varepsilon r.
\end{aligned}
$$

For the second part, the proof of Proposition [%s](#proposition:full_dimensional_preservation) never uses the first condition of Definition [%s](#definition:optimal_oracles).
:::

The first part is a small variant of Lemma 5 of {cite:t}`Stu21`. Together, the two parts say that, for sets of positive dimension, having optimal Hausdorff oracles amounts to a single condition:

$$
\begin{aligned}
(\exists A)(\forall B)(\forall \varepsilon > 0) \brk{\dim_{\operatorname{H}}(N_X(A, B, \varepsilon)) = \dim_{\operatorname{H}}(X)}.
\end{aligned}
$$

In what follows, we replace the oracle $A$ and the competitor $B$ by classical objects, such as prefix-free ball codes (Definition [%s](#definition:prefix_free_ball_code)) and finite Borel measures. Each such replacement again comes with a witness condition and a fitness condition, and the analogue of Proposition [%s](#proposition:witness_condition_is_free) lets us work with the fitness condition alone.
