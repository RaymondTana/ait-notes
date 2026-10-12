---
title: "2.1 Robustness of the Lift"
label: section:Robustness_of_the_Lift
---

## 2.1.1 An Alternate Lift

Recall that in Section [1.7](#section:Lifting_Prefix_Complexity_to_Reals), we specified the standard lift of conditional prefix complexity to Euclidean space. We claim that the order of maximum and minimum in its definition makes no difference asymptotically. That is, suppose we were to alternatively define for $B \subseteq \mathbb{R}^m$ and $C \subseteq \mathbb{R}^n$:

$$
\begin{aligned}
\mathcal{K}(B \mid C) := \min_p \set{\max_q \set{\Kc{p}{q}}{q \in C \cap \mathbb{Q}^n}}{p \in B \cap \mathbb{Q}^m},
\end{aligned}
$$

and for $x \in \mathbb{R}^m$, $q \in \mathbb{Q}^m$, $y \in \mathbb{R}^n$, and $r, s \in \omega$:

$$
\begin{aligned}
\mathcal{K}_{r \mid s}(x \mid y) &:= \mathcal{K}(B_{2^{-r}}(x) \mid B_{2^{-s}}(y)), \text{ and}\\
\mathcal{K}_s(p \mid y) &:= \mathcal{K}(\seq{p} \mid B_{2^{-s}}(y)).
\end{aligned}
$$

:::{prf:theorem} Robustness of Euclidean Conditional Kolmogorov Complexity
:label: theorem:maxmin_and_minmax_conditional_complexity_equal
:enumerator: 2.1.1
Let $m, n \in \omega$. Then, for any $x \in \mathbb{R}^m$, $y \in \mathbb{R}^n$, and $r, s \in \omega$,

$$
\begin{aligned}
\mathcal{K}_{r \mid s}(x \mid y) = K_{r \mid s}(x \mid y),
\end{aligned}
$$

where the equality holds up to $2K(r) + 2K(s) + O_{m, n}(1)$.
:::

We will obtain the above theorem by applying the same proof methods found in {cite:t}`CL14` on the linear sensitivities of $K$ in its precision parameters. In particular, both forms $K$ and $\mathcal{K}$ are well-approximated by dyadic truncation as in Lemma [1.7.5](#maxmin_truncation_for_r_s). We first recall an important geometric fact from {cite:t}`CL14`. In Euclidean space $\mathbb{R}^m$, it takes a sufficiently small scaling factor $\gamma > 0$ in order to guarantee at least one node in the lattice $\gamma \mathbb{Z}^m$ lies in a given ball of fixed radius.

:::{prf:observation} Observation 3.4 in {cite:t}`CL14`, Observation 3 in {cite:t}`LL18`
:label: observation:grid_in_open_ball
:enumerator: 2.1.2
For every $m \in \omega$, $r > 0$, and open ball $B \subseteq \mathbb{R}^m$ of radius $2^{-r}$,

$$
\begin{aligned}
B \cap 2^{-\p{r + \ceil{\log \sqrt{m}}}} \mathbb{Z}^m \neq \emptyset.
\end{aligned}
$$
:::

Now, we prove linear sensitivities for the alternate lift $\mathcal{K}$.

:::{prf:lemma} Linear Sensitivity in the Condition for $\mathcal{K}$
:label: minmax_linear_sensitivity_in_s
:enumerator: 2.1.3
For all $m, n \in \omega$, $p \in \mathbb{Q}^m$, $y \in \mathbb{R}^n$, and $s, \Delta s \in \omega$,

$$
\begin{aligned}
\KcaltAt{s + \Delta s}{p}{y} \leq \KcaltAt{s}{p}{y} \leq \KcaltAt{s + \Delta s}{p}{y} + n \Delta s + K(s) + O_n(\log \Delta s) + O_n(1).
\end{aligned}
$$
:::

:::{prf:proof}
:nonumber:
The first inequality follows by definition. Unpacking the notation, it suffices to show that for any fixed $q \in B_{2^{-s}}(y) \cap \mathbb{Q}^n$,

$$
\begin{aligned}
\Kc{p}{q} \leq \KcaltAt{s + \Delta s}{p}{y} + n \Delta s + K(s) + O_n(\log \Delta s) + O_n(1).
\end{aligned}
$$

Note that we have the ability to compute a rational element of the smaller open ball $B_{2^{-(s + \Delta s)}}(y)$ from the fixed, rational element $q$ of the larger open ball $B_{2^{-s}}(y)$: by Observation [2.1.2](#observation:grid_in_open_ball), there exists an integer tuple $z \in \mathbb{Z}^n$ such that $2^{-s^*} z \in B_{2^{-(s + \Delta s)}}(y - q)$, where $s^* = s + \Delta s + \ceil{\log \sqrt{n}}$. And set $q' := 2^{-s^*} z + q \in B_{2^{-(s + \Delta s)}}(y)$. Notice that

$$
\begin{aligned}
\norm{z} = 2^{s^*} \norm{2^{-s^*}z} \leq 2^{s^*} \p{2^{-s} + 2^{-\p{s + \Delta s}}} = 2^{\ceil{\log \sqrt{n}}} \p{2^{\Delta s} + 1} \leq 2^{\Delta s + \ceil{\log \sqrt{n}} + 1}.
\end{aligned}
$$

By ([1.6.4](#equation:K_bound_int_tuple)), we have

$$
\begin{aligned}
K(z) \leq n \Delta s + O_n(\log \Delta s) + O_n(1).
\end{aligned}
$$

So, we may conclude

$$
\begin{aligned}
\Kc{p}{q} &\leq \Kc{p}{q'} + \Kc{q'}{q} + O_n(1) \\
&\leq \KcaltAt{s + \Delta s}{p}{y} + \K{z} + \K{s, \Delta s} + O_n(1)\\
&\leq \KcaltAt{s + \Delta s}{p}{y} + n \Delta s + K(s) + O_n(\log \Delta s) + O_n(1).
\end{aligned}
$$
:::

:::{prf:lemma} Linear Sensitivity in the Input for $\mathcal{K}$
:label: minmax_linear_sensitivity_in_r
:enumerator: 2.1.4
For all $m, n \in \omega$, $x \in \mathbb{R}^m$, $y \in \mathbb{R}^n$, and $r, \Delta r, s \in \omega$,

$$
\begin{aligned}
\KcaltAt{r \mid s}{x}{y} \leq \KcaltAt{r + \Delta r \mid s}{x}{y} \leq \KcaltAt{r \mid s}{x}{y} + m \Delta r + K(r) + O_{m}(\log \Delta r) + O_{m, n}(1).
\end{aligned}
$$
:::

:::{prf:proof}
:nonumber:
The first inequality follows by definition. Unpacking the notation, it suffices to show for any fixed $p \in B_{2^{-r}}(x) \cap \mathbb{Q}^m$ that

$$
\begin{aligned}
\KcaltAt{r + \Delta r \mid s}{x}{y} \leq \KcaltAt{s}{p}{y} + m \Delta r + K(r) + O_{m}(\log \Delta r) + O_{m, n}(1).
\end{aligned}
$$

Note that we have the ability to compute some element of the smaller open ball $B_{2^{-(r + \Delta r)}}(x)$ from a fixed, rational element $p$ of the larger open ball $B_{2^{-r}}(x)$: by Observation [2.1.2](#observation:grid_in_open_ball), there exists an integer tuple $z \in \mathbb{Z}^m$ for which $2^{-r^*}z \in B_{2^{-(r + \Delta r)}}(x - p)$, where $r^* = r + \Delta r + \ceil{\log \sqrt{m}}$. Then, we take $p' := p + 2^{-r^*} z \in B_{2^{-(r + \Delta r)}}(x)$. Thus, by ([1.6.4](#equation:K_bound_int_tuple)),

$$
\begin{aligned}
\KcaltAt{r + \Delta r \mid s}{x}{y} &\leq  \KcaltAt{s}{p'}{y}\\
&\leq \KcaltAt{s}{p}{y} + \Kc{p'}{p} + O_{m, n}(1) \\
&\leq \KcaltAt{s}{p}{y} + \K{z} + \K{r, \Delta r} + O_{m, n}(1)\\
&\leq \KcaltAt{s}{p}{y} + m \Delta r + K(r) + O_{m}(\log \Delta r) + O_{m, n}(1).
\end{aligned}
$$
:::

:::{prf:lemma} Dyadic Truncation Suffices for Condition in $\mathcal{K}$
:label: minmax_truncation_for_s
:enumerator: 2.1.5
For all $m, n \in \omega$, $p \in \mathbb{Q}^m$, $y \in \mathbb{R}^n$, and $s \in \omega$,

$$
\begin{aligned}
\abs{\KcaltAt{s}{p}{y} - \Kc{p}{\restrict{y}{s}}} \leq \K{s}
+ O_n(1).
\end{aligned}
$$
:::

:::{prf:proof}
:nonumber:
In one direction, we have that $\restrict{y}{s}$ is a rational in a ball about $y$ of radius $2^{-s} \sqrt{n}$. So, $\restrict{y}{s}$ is considered in the evaluation of $\mathcal{K}_{s + \log \sqrt{n}}(p \mid y)$. We appeal to linear sensitivity [2.1.3](#minmax_linear_sensitivity_in_s) in $s$ and use the fact that $\restrict{y}{s} \in B_{2^{-s} \sqrt{n}}(y) \cap \mathbb{Q}^n$ to bound $\mathcal{K}_s(p \mid y)$ from below:

$$
\begin{aligned}
\KcaltAt{s}{p}{y} &\geq \KcaltAt{s - \log \sqrt{n}}{p}{y} - n \log \sqrt{n} - K(s) - O(\log \log \sqrt{n}) - O(1)\\
&\geq \Kc{p}{\restrict{y}{s}} - K(s) - O(n \log n) - O(1).
\end{aligned}
$$

In the other direction, unpacking the notation, it suffices to check that:

$$
\begin{aligned}
\Kc{p}{q} \leq \Kc{p}{\restrict{y}{s}} + K(s) + O_n(1)
\end{aligned}
$$

for any fixed $q \in B_{2^{-s}}(y) \cap \mathbb{Q}^n$. Because $\restrict{y}{s} \in B_{2^{-s} (1 + \sqrt{n})}(q) \cap \mathcal{Q}^n_s$ is contained in a set of cardinality no greater than the constant $(2(1 + \sqrt{n}))^n$, we may describe $\restrict{y}{s}$ using $q$, $s$, and a constant number of extra bits depending on $n$. So,

$$
\begin{aligned}
\Kc{p}{q} &\leq \Kc{p}{\restrict{y}{s}} + \Kc{\restrict{y}{s}}{q} + \K{s} + O_n(1) \\
&\leq \Kc{p}{\restrict{y}{s}} + K(s) + O_n(1).
\end{aligned}
$$
:::

:::{prf:lemma} Dyadic Truncation Suffices for both Parameters in $\mathcal{K}$
:label: minmax_truncation_for_r_s
:enumerator: 2.1.6
For all $m, n \in \omega$, $x \in \mathbb{R}^m$, $y \in \mathbb{R}^n$, and $r, s \in \omega$,

$$
\begin{aligned}
\abs{\KcaltAt{r \mid s}{x}{y} - \Kc{\restrict{x}{r}}{\restrict{y}{s}}} \leq K(r) + K(s) + O_{m, n}(1).
\end{aligned}
$$
:::

We could prove this lemma directly using the linear sensitivity of $\mathcal{K}$ in $r$ in Lemma [2.1.4](#minmax_linear_sensitivity_in_r). But there is a simpler proof using dyadic truncation.

:::{prf:proof}
:nonumber:
Dropping the logarithmic terms in the precision-levels and norms, and using the definitions of $K$ and $\mathcal{K}$:

$$
\begin{aligned}
\KcaltAt{r \mid s}{x}{y} &:= \min_p \set{\KcaltAt{s}{p}{y}}{p \in B_{2^{-r}}(x) \cap \mathbb{Q}^m}\\
&= \min_p \set{\Kc{p}{\restrict{y}{s}}}{p \in B_{2^{-r}}(x) \cap \mathbb{Q}^m} & [\text{Lemma~2.1.5}]\\
&= \KcAt{r}{x}{\restrict{y}{s}} \\
&= \Kc{\restrict{x}{r}}{\restrict{y}{s}}. & [\text{Lemma~1.7.4}]
\end{aligned}
$$
:::

Together, the dyadic truncation lemmas [1.7.5](#maxmin_truncation_for_r_s) and [2.1.6](#minmax_truncation_for_r_s) imply that $\Kc{\restrict{x}{r}}{\restrict{y}{s}}$ approximates both $\KcAt{r \mid s}{x}{y}$ and $\KcaltAt{r \mid s}{x}{y}$ up to logarithmic terms in $r$ and $s$, proving Theorem [2.1.1](#theorem:maxmin_and_minmax_conditional_complexity_equal).

## 2.1.2 Approximation by $K$-Minimizers

Conditional complexity is not only well-approximated by dyadic truncation, but also by $K$-minimizers. In particular, we prove conditional versions of the result from {cite:t}`CL14` stating that the lift of conditional complexity to Euclidean space can also be well-approximated by evaluating the conditional complexity of the corresponding $K$-minimizers. This will imply a conditionalized chain rule for conditional complexity.

Our method makes use of some basic facts established in {cite:t}`CL14` intuitively saying that any $K$-minimizer of an open ball represents the information content essentially possessed by all the other rational points in the ball.

:::{prf:lemma} Lemma 4.3 of {cite:t}`CL14`
:label: K_minimizers_know_least
:enumerator: 2.1.7
Let $m, n, \ell \in \omega$, $p \in \mathbb{Q}^m$, $w \in \mathbb{Q}^\ell$, $y \in \mathbb{R}^n$, and $s \in \omega$. If $q \in B_{2^{-s}}(y) \cap \mathbb{Q}^n$ and $q^*$ is a $K$-minimizer of $B_{2^{-s}}(y)$, then

$$
\begin{aligned}
K(p \mid q, w) \leq K(p \mid q^*, w) + K(K(q^*)) + O_n(\log s) + O_n(1).
\end{aligned}
$$
:::

:::{prf:corollary} Corollary 4.4 in {cite:t}`CL14`
:label: corollary:K_minimizer_not_complex
:enumerator: 2.1.8
Let $m \in \omega$ and $x \in \mathbb{R}^m$. Suppose $p^* \in \mathbb{Q}^m$ is a $K$-minimizer of $B_{2^{-r}}(x)$, and $p \in B_{2^{-r}}(x) \cap \mathbb{Q}^m$ is some other nearby rational. Then

$$
\begin{aligned}
K(p^* \mid p) = O_m(\log r) + O_m(1).
\end{aligned}
$$
:::

Now, we may conclude that $K$-minimizers suffice for computing conditional complexity. We use here that the two lifts of prefix complexity asymptotically agree: $K \approx \mathcal{K}$, where the approximate equality $\approx$ holds up to sub-linear terms in the precision-levels. For the rest of the section, we write (in)equalities up to the logarithmic terms:

```{math}
:label: equation:logarithmic_factors
:enumerator: 2.1.1
\begin{aligned}
O_m(\log r) + O_n(\log s) + O_{m, n}(1).
\end{aligned}
```

:::{prf:proposition} $K$-minimizers Suffice for Conditional Complexity
:label: lemma:conditional_K_minimizers_suffice
:enumerator: 2.1.9
Let $m, n \in \omega$, $x \in \mathbb{R}^m$, $y \in \mathbb{R}^n$, and $r, s \in \omega$. If $p^* \in \mathbb{Q}^m$ and $q^* \in \mathbb{Q}^n$ are each $K$-minimizers of $B_{2^{-r}}(x)$ and $B_{2^{-s}}(y)$, respectively, then

$$
\begin{aligned}
K_{r \mid s}(x \mid y) = K(p^* \mid q^*),
\end{aligned}
$$

where equality holds up to the logarithmic factors given by ([2.1.1](#equation:logarithmic_factors)).
:::

:::{prf:proof}
:nonumber:
Let $(p^*, q^*)$ be the $K$-minimizers for $x$ and $y$ at precisions $r$ and $s$, respectively. Additionally, let $(p', q')$ denote a witness pair to $\KcAt{r \mid s}{x}{y}$, and $(p'', q'')$ the same for $\KcaltAt{r \mid s}{x}{y}$. Then, dropping any logarithmic terms,

$$
\begin{aligned}
\KcAt{r \mid s}{x}{y} &= \KcaltAt{r \mid s}{x}{y} & [\text{Theorem~2.1.1}]\\
&= \Kc{p''}{q''}\\
&\leq \Kc{p^*}{q''}\\
&= \Kc{p^*}{q^*} + \Kc{q^*}{q''}\\
&= \Kc{p^*}{q^*} & [\text{Corollary~2.1.8}]\\
&= \Kc{p^*}{p'} + \Kc{p'}{q^*}\\
&\leq \Kc{p'}{q^*} & [\text{Corollary~2.1.8}]\\
&\leq \Kc{p'}{q'}\\
&= \KcAt{r \mid s}{x}{y}.
\end{aligned}
$$
:::

Now, we aim to prove an approximate, conditional chain rule for $K_{r, s \mid t}$. Theorem [1.10.1](#theorem:chain_rule_mutual_information_r_s) captures the approximate, unconditional chain rule for $K_{r \mid s}$, and it implicitly follows by applying the arguments in Section 4 of {cite:t}`CL14` under the distinct precision-levels $r$ and $s$. We may achieve the conditional version using approximations by $K$-minimizers.

::::{prf:lemma}
:label: lemma:conditional_pairwise_complexity_by_K_minimizers_and_dyadic_truncation
:enumerator: 2.1.10
Let $m, n, \ell \in \omega$, $x \in \mathbb{R}^m$, $y \in \mathbb{R}^n$, $z \in \mathbb{R}^\ell$, and $r, s, t \in \omega$. Denote by $p^*, q^*, w^*$ the $K$-minimizers of $B_{2^{-r}}(x)$, $B_{2^{-s}}(y)$, and $B_{2^{-t}}(z)$, respectively. Then the following equalities hold up to the logarithmic factors given by ([2.1.1](#equation:logarithmic_factors)):

:::{div}
:class: roman-list
1. $K_{r, s \mid t}(x, y \mid z) = K(p^*, q^* \mid w^*)$,
1. $K_{r \mid s, t}(x, y \mid z) = K(p^* \mid q^*, w^*)$.
:::
::::

:::{prf:proof}
:nonumber:
We have two competing notions of $K$-minimizer, now: either unconditional, or conditioned on some extra information $\zeta \in 2^{< \omega}$. Let $p^* \in \mathbb{Q}^m$ be a $K$-minimizer of $B_{2^{-r}}(x)$ and $p^*_\zeta \in \mathbb{Q}^m$ a witness to $K_r(x \mid \zeta)$. We first show that, no matter $\zeta$, the $K$-minimizer $p^*$ also approximately minimizes $K_r(x \mid \zeta)$. By definition,

```{math}
:label: K_minimizer_with_condition
:enumerator: 2.1.2
\begin{aligned}
K(p^*_\zeta \mid \zeta) &\leq K(p^* \mid \zeta)  \\
&\leq K(p^*_\zeta \mid \zeta) + K(p^* \mid p^*_\zeta)  \\
&\leq K(p^*_\zeta \mid \zeta) &  [\text{Lemma~2.1.7}]\\
&= K_r(x \mid \zeta).
\end{aligned}
```

This implies a conditional version of Corollary [2.1.8](#corollary:K_minimizer_not_complex), where for any $p \in B_{2^{-r}}(x) \cap \mathbb{Q}^m$,

```{math}
:label: K_minimizers_with_condition_know_least_when_conditioned
:enumerator: 2.1.3
\begin{aligned}
K(p^*_\zeta \mid p, \zeta) &\leq K(p^*_\zeta \mid p^*, \zeta) & [\text{Lemma~2.1.7}]  \\
&= K(p^*_\zeta \mid \zeta) + K(p^* \mid p^*_\zeta, \zeta) - K(p^* \mid \zeta) \\
&= K(p^* \mid p^*_\zeta, \zeta) & [\text{(2.1.2)}]  \\
&= 0. & [\text{Corollary~2.1.8}]
\end{aligned}
```

Now, we assert $K_{r, s \mid t}(x, y \mid z) \approx K(p^*, q^* \mid w^*)$. Call $w'$ a maximizing witness to $z$ in the definition of $K_{r, s \mid t}(x, y \mid z)$, and let $(p^*_{w'}, q^*_{w'})$ be minimizing witnesses of $K_r(x \mid w')$ and $K_{s}(y \mid w')$, respectively. We follow very similar steps to the proof of Proposition [2.1.9](#lemma:conditional_K_minimizers_suffice). In one direction:

$$
\begin{aligned}
K_{r, s \mid t}(x, y \mid z) = K_{r, s}(x, y \mid w') &= K(p^*_{w'}, q^*_{w'} \mid w') & [\text{Proposition~2.1.9}]\\
&= K(p^*_{w'} \mid w') + K(q^*_{w'} \mid p^*_{w'}, w')\\
&= K(p^* \mid w') + K(q^*_{w'} \mid p^*_{w'}, w') & [\text{(2.1.2)}]\\
&\leq K(p^* \mid w') + K(q^*_{w'} \mid p^*, w') & [\text{Lemma~2.1.7}]\\
&= K(q^*_{w'} \mid w') + K(p^* \mid q^*_{w'}, w')\\
&\leq K(q^* \mid w') + K(p^* \mid q^*, w') & [\text{Lemma~2.1.7}]\\
&= K(p^*, q^* \mid w')\\
&\leq K(p^*, q^* \mid w^*). & [\text{Lemma~2.1.7}]
\end{aligned}
$$

In the reverse direction:

$$
\begin{aligned}
K(p^*, q^* \mid w^*) &\leq K(p^*, q^* \mid w')\\
&= K(p^* \mid w') + K(q^* \mid p^*, w')\\
&\leq K(p^*_{w'} \mid w') + K(q^* \mid p^*_{w'}, w') + K(p^*_{w'} \mid p^*, w') & [\text{(2.1.2)}]\\
&= K(q^* \mid w') + K(p^*_{w'} \mid q^*, w') & [\text{(2.1.3)}]\\
&\leq K(q^*_{w'} \mid w') + K(p^*_{w'} \mid q^*_{w'}, w') + K(q^*_{w'} \mid q^*, w') & [\text{(2.1.2)}]\\
&= K(p^*_{w'}, q^*_{w'} \mid w') & [\text{(2.1.3)}]\\
&= K_{r, s \mid t}(x, y \mid z).
\end{aligned}
$$

Finally, we move on to proving $K_{r \mid s, t}(x \mid y, z) \approx K(p^* \mid q^*, w^*)$. Let $(q', w')$ be a pair of rationals witnesses for $y$ and $z$ in evaluating $K_{r \mid s, t}(x \mid y, z)$, and let $p^*_{q', w'} \in B_{2^{-r}}(x) \cap \mathbb{Q}^m$ minimize $K_{r}(x \mid q', w')$. Then,

$$
\begin{aligned}
K_{r \mid s, t}(x \mid y, z) \leq K(p^* \mid q', w') &\leq K(p^* \mid q^*, w^*) & [\text{Lemma~2.1.7}]\\
&\leq K(p^* \mid q', w')\\
&= K(p^*_{q', w'} \mid q', w')& [\text{(2.1.2)}]\\
&\leq \Kc{p'}{q', w'} = K_{r \mid s, t}(x \mid y, z).
\end{aligned}
$$
:::

Note that Lemma [1.7.5](#maxmin_truncation_for_r_s) stated with extra conditional information follows from an identical proof to the unconditional version. So, corresponding linear sensitivities hold for $K_{r, s \mid t}(x, y \mid z)$; and dyadic truncation also approximates prefix complexity well in this more general case: $K_{r, s \mid t}(x, y \mid z) \approx K(\restrict{x}{r}, \restrict{y}{s} \mid \restrict{z}{t})$.

The other prefix complexity term from the statement of Lemma [2.1.10](#lemma:conditional_pairwise_complexity_by_K_minimizers_and_dyadic_truncation) is likewise well-approximated through dyadic truncations:

$$
\begin{aligned}
K_{r \mid s, t}(x \mid y, z) &= K(p^* \mid q^*, w^*) - K(q^* \mid w^*)\\
&= K(\restrict{x}{r}, \restrict{y}{s} \mid \restrict{z}{t}) - K(\restrict{y}{s} \mid \restrict{z}{t}) & [\text{Lemma~1.7.5}]\\
&= K(\restrict{x}{r} \mid \restrict{y}{s}, \restrict{z}{t}).
\end{aligned}
$$

Finally, Lemma [2.1.10](#lemma:conditional_pairwise_complexity_by_K_minimizers_and_dyadic_truncation) yields the fully conditional chain rule for conditional prefix complexity over Euclidean space.

:::{prf:theorem} Conditional Chain Rule for Conditional Complexity
:label: theorem:SOI_conditional_complexity_r_s_t
:enumerator: 2.1.11
Let $m, n, \ell \in \omega$, $x \in \mathbb{R}^m$, $y \in \mathbb{R}^n$, $z \in \mathbb{R}^\ell$, and $r, s, t \in \omega$, then the following equalities hold up to the logarithmic factors given by ([2.1.1](#equation:logarithmic_factors)):

$$
\begin{aligned}
K_{r, s \mid t}(x, y \mid z) = K_{r \mid t}(x \mid z) + K_{s \mid r, t}(y \mid x, z).
\end{aligned}
$$
:::

:::{prf:proof}
:nonumber:
We simply follow the approximate equalities from the previous result:

$$
\begin{aligned}
K_{r, s \mid t}(x, y \mid z) &= K(p^*, q^* \mid w^*) & [\text{Lemma~2.1.10}]\\
&= K(p^* \mid w^*) + K(q^* \mid p^*, w^*)\\
&= K_{r \mid t}(x \mid z) + K_{s \mid r, t}(y \mid x, z). & [\text{Lemma~2.1.10}]
\end{aligned}
$$
:::
