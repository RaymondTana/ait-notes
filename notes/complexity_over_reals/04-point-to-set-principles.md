---
title: "Point-to-Set Principles"
label: section:PTS
---

In this context, a point-to-set (PTS) principle will characterize the fractal dimension or measure content of a subset by some {term}`local dimension` or measure assigned to its elements. We summarize the few PTS principles known for {term}`Hausdorff dimension` and the $s$-dimensional {term}`Hausdorff outer measures <Hausdorff outer measure>` via algorithmically-restricted quantities.

## PTS for Hausdorff Dimension

Certain fractal dimension notions have pointwise, algorithmic characterizations (over simple spaces such as Cantor space and Euclidean space). This was originally shown for Hausdorff dimension in 2017 by J. Lutz and N. Lutz {cite:p}`LL18`.

:::{prf:theorem} Point-to-Set Principle; Theorem 1 of {cite:t}`LL18`
:label: theorem:PTS_for_H_dimension
For any $X \subseteq 2^\omega$ or $X \subseteq \mathbb{R}^m$, we have

$$
\begin{aligned}
\dim_{\operatorname{H}} X = \min_{B \in 2^{\leq \omega}} \sup_{x \in X} \dim^B(x).
\end{aligned}
$$
:::

Notably, this implies that for each subset $X$, there exists an {term}`oracle` $B \in 2^{\leq \omega}$ which is powerful enough to simulate Hausdorff dimension by ML-$B$-$s$-tests. Any such oracle is called a **Hausdorff oracle** for $X$. An analogous formula holds for classical packing dimension (see Theorem 2 of {cite:t}`LL18`), swapping weak effective dimension $\dim$ for {term}`strong dimension`: $\operatorname{Dim}$.

The main insight used to prove the Point-to-Set Principle involves the ability to build for a fixed set $X \subseteq \mathbb{R}^m$ an oracle $B$ with knowledge of how $X$ intersects with any given dyadic cube from $\mathcal{Q}^m$. Arbitrary covers of $X$ exhibiting $\dim_{\operatorname{H}} X$ may be approximated using covers comprising dyadic cubes, and so the Hausdorff dimension of $X$ is the supremum of the size of the intersection with $X$ along nested sequences of dyadic cubes. Suppose that the intersection of a nested sequence intersecting with $X$ is the singleton set containing $x \in X$. Then $\dim^B(x)$ exactly captures how much dimension $X$ takes on at $x$.

In practice, the power of the Point-to-Set Principle is in proving lower-bounds for Hausdorff dimension. As remarked to me by Ryan Bushling, one might as well consider this a **local-to-global** principle for the following reason: in order to witness a lower bound on $\dim_{\operatorname{H}}X$, it is not enough to find a single sufficiently-random element $x \in X$, for any countable number of reals could be coded into an oracle. Instead, one must demonstrate the existence of *many* highly-complex elements of $X$, which requires knowledge of a large portion of the set to do.

The Point-to-Set Principle has found applications across geometric measure theory, including in bounding the Hausdorff dimension of Furstenberg sets {cite:p}`LS16; Stu18`, lineal extensions {cite:p}`BF25`, distance sets {cite:p}`ABW23`, and pinned-distance sets {cite:p}`Stu22_pinned`; as well as in extending the Marstrand-Mattila Projection Theorem {cite:p}`Stu21`.

Well before the full Point-to-Set Principle was proved, L. Staiger {cite:p}`Sta89` and B. Ryabko {cite:p}`Rya93; Rya94` had already observed versions of the Point-to-Set Principle for simply-definable classes such as $\Sigma^0_2$-classes. This was slightly generalized by J. Hitchcock in {cite:t}`Hit05` in what he calls a **correspondence principle** between {term}`constructive dimension` and Hausdorff dimension {cite:p}`Hit05`. The spirit of any correspondence principle is to characterize a classical notion by unrelativized, effective means (i.e., avoiding oracles).

:::{prf:theorem} Correspondence Principle for Hausdorff dimension, Theorem 5.3 of {cite:t}`Hit05`
:label: theorem:correspondence_principle_for_H_dimension
For any $\Sigma^0_2$-class $X \subseteq 2^\omega$, we have

$$
\begin{aligned}
\dim_{\operatorname{H}} X = \dim(X).
\end{aligned}
$$
:::

Hitchcock further showed that this correspondence broke down immediately beyond this level of the {term}`lightface Borel hierarchy`.

## PTS by Coding on Balls

K. Miyabe observed that the point-to-set principle factors into a purely classical coding theorem, followed by an encoding of countable data into an oracle {cite:p}`Miy26`.

:::{prf:definition} Definitions 3.1, 3.2, and 4.1 of {cite:t}`Miy26`
:label: definition:prefix_free_ball_code
A **prefix-free ball code** is a map $\varphi : D \to \mathcal{B}$, where $D \subseteq 2^{<\omega}$ is {term}`prefix-free` and $\mathcal{B}$ is the collection of closed balls of positive radius in $\mathbb{R}^m$. For $x \in \mathbb{R}^m$ and $r \in \omega$, its **code length** is

$$
\begin{aligned}
L^\varphi_r(x) := \min \set{\operatorname{len}(\pi)}{\pi \in D,\ x \in \varphi(\pi),\ \operatorname{diam} \varphi(\pi) \leq 2^{-r}},
\end{aligned}
$$

or $+\infty$ if no such $\pi$ exists. The code is **rational** if all of its values are rational closed balls.
:::

Note that Miyabe writes $K_\varphi(x; r)$ where we write $L^\varphi_r(x)$.

:::{prf:theorem} Theorem 1.1 (Theorems 3.3 and 4.2) of {cite:t}`Miy26`
:label: theorem:ball_code_characterization
For every nonempty $X \subseteq \mathbb{R}^m$,

$$
\begin{aligned}
\dim_{\operatorname{H}} X &= \min_{\varphi} \sup_{x \in X} \liminf_{r \to \infty} \frac{L^\varphi_r(x)}{r} =: \min_\varphi \operatorname{bcdim}_\varphi(X), \\
\dim_{\operatorname{P}} X &= \min_{\varphi} \sup_{x \in X} \limsup_{r \to \infty} \frac{L^\varphi_r(x)}{r} =: \min_\varphi \operatorname{bcDim}_\varphi(X),
\end{aligned}
$$

where $\varphi$ ranges over prefix-free ball codes.
:::

One might view the Hausdorff dimension result above as a Euclidean, ball-based counterpart to B. Ryabko's coding theorem for combinatorial sources in $A^\omega$ {cite:p}`Rya86`.

Here, we reproduce the proof of Miyabe's Hausdorff dimension formula.

:::{prf:proof}
:nonumber:
Fix $\varphi$ and let $\alpha = \sup_{x \in X} L^\varphi_r(x) / r$.

*Lower bound*: To prove $\dim_{\operatorname{H}} X \leq \alpha$, consider any $t > \alpha$. Each $x \in X$ has infinitely many $r$ with a name $\pi$ such that $x \in \varphi(\pi)$, $\operatorname{diam} \varphi(\pi) \leq 2^{-r}$, and $\operatorname{len}(\pi) < tr$, so that $\operatorname{diam}(\varphi(\pi))^t < 2^{-\operatorname{len}(\pi)}$. A fixed name denotes a ball of fixed positive diameter, so it witnesses only finitely many $r$, and the lengths of the witnessing names tend to infinity. So for every $N$, the balls $\varphi(\pi)$ with $\operatorname{len}(\pi) \geq N$ and $\operatorname{diam}(\varphi(\pi))^t < 2^{-\operatorname{len}(\pi)}$ cover $X$, each with diameter less than $2^{-N/t}$, and

$$
\begin{aligned}
\mathcal{H}^t_{2^{-N/t}}(X) \leq \sum_{\pi \in D,\ \operatorname{len}(\pi) \geq N} 2^{-\operatorname{len}(\pi)} \longrightarrow 0
\end{aligned}
$$

by the {term}`Kraft Inequality`. Hence $\mathcal{H}^t(X) = 0$.

*Attainable*: Let $s := \dim_{\operatorname{H}} X$ and $t_k := s + 1/k$. Since $\mathcal{H}^{t_k}(X) = 0$, cover $X$ by rational closed balls $\overline{B}$ with $\operatorname{diam} \overline{B} \leq 2^{-k}$ and $\sum (\operatorname{diam} \overline{B})^{t_k} \leq 2^{-k}$. Request a name of length $\ceil{t_k \log (1 / \operatorname{diam} \overline{B})}$ for each such ball. The requests have total Kraft weight at most $\sum_k 2^{-k} \leq 1$, so the countable Kraft inequality (Lemma 3.6 of {cite:t}`Miy26`) provides a prefix-free code $\varphi$ with these lengths. Given $x \in X$ and $k$, choose $\overline{B} \ni x$ from the $k$-th cover and let $r := \floor{\log(1 / \operatorname{diam} \overline{B})} \geq k$. Then $L^\varphi_r(x) / r < t_k + (t_k + 1)/k$, so $\liminf_r L^\varphi_r(x) / r \leq s$.
:::

The effective version follows by rationalizing a minimizing code and storing it in an oracle.

:::{prf:lemma} Lemmas 5.2 and 5.4 of {cite:t}`Miy26`
:label: lemma:rationalize_and_encode_ball_codes
1. For every prefix-free ball code $\varphi$, there is a rational prefix-free ball code $\varphi'$ with $L^{\varphi'}_r(x) \leq L^\varphi_{r+1}(x)$ for all $x$ and $r$.
2. For every rational prefix-free ball code $\varphi$, there is an oracle $A$ with $L^{\mathbf{U}^A}_r(x) \leq L^\varphi_r(x) + O(1)$ for all $x$ and $r$.
:::

One can prove the first part by enlargening each ball of the original ball code to a rational closed ball of less than twice its diameter. For the second part: it suffices to encode both the domain and graph of the ball code.

:::{prf:theorem} Point-to-Set Principles via Ball Codes; Theorem 5.5 of {cite:t}`Miy26`
:label: theorem:PTS_coding_form
For every nonempty $X \subseteq \mathbb{R}^m$,

$$
\begin{aligned}
\dim_{\operatorname{H}} X &= \min_{A \in 2^{\leq \omega}} \sup_{x \in X} \liminf_{r \to \infty} \frac{L^{\mathbf{U}^A}_r(x)}{r} =: \min_{A \in 2^{\leq \omega}} \operatorname{bcdim}^{\mathbf{U}^A}(X), \\
\dim_{\operatorname{P}} X &= \min_{A \in 2^{\leq \omega}} \sup_{x \in X} \limsup_{r \to \infty} \frac{L^{\mathbf{U}^A}_r(x)}{r} =: \min_{A \in 2^{\leq \omega}} \operatorname{bcDim}^{\mathbf{U}^A}(X).
\end{aligned}
$$
:::

:::{prf:proof}
:nonumber:
Each $\mathbf{U}^A$ is a prefix-free ball code, so Theorem [%s](#theorem:ball_code_characterization) gives "$\geq$". For the reverse, take a minimizing code, rationalize it, and encode it into an oracle by Lemma [%s](#lemma:rationalize_and_encode_ball_codes).
:::

By Proposition [%s](#proposition:ball_vs_point_complexity), these are exactly $\dim^A(x)$ and $\operatorname{Dim}^A(x)$. So Theorem [%s](#theorem:PTS_coding_form) recovers Theorem [%s](#theorem:PTS_for_H_dimension) and its packing analogue (Corollary 5.9 of {cite:t}`Miy26`). Conversely, granting the point-to-set principle, the same two lemmas recover the rational-ball case of Theorem [%s](#theorem:ball_code_characterization).

## PTS for Hausdorff Measures

The original Point-to-Set Principle has recently been refined to the $s$-dimensional Hausdorff outer measures by P. Lutz and J. Miller {cite:p}`LM24`. These results also expand on the complexity characterizations of various partial randomness notions from Theorem [%s](#theorem:complexity_characterizations_of_randomness).

:::{prf:theorem}
:label: theorem:PTS_log_s_measure_and_sigma_finite
For every $X \subseteq 2^\omega$ and $s \geq 0$,

$$
\begin{aligned}
\log \mathcal{H}^s(X) =^+ \inf_{B \in 2^{\leq \omega}} \sup_{x \in X} \liminf_{r \to \infty}  \operatorname{\Delta M}^B_s(\restrict{x}{r}),
\end{aligned}
$$

and X is not $\sigma$-finite with respect to $\mathcal{H}^s$ if and only if

$$
\begin{aligned}
(\forall B \in 2^{\leq \omega})(\exists x \in X) \brk{ \liminf_{r \to \infty} \operatorname{\Delta M}^B_s(\restrict{x}{r}) = \infty }.
\end{aligned}
$$
:::

By Theorem [%s](#theorem:complexity_characterizations_of_randomness), $X$ is not $\sigma$-finite in dimension $s$ if and only if there is a strong Solovay-$B$-$s$-random element in $X$ for every oracle $B$.

:::{prf:corollary}
:label: corollary:PTS_null_or_finite
For every $X \subseteq 2^\omega$ and $s \geq 0$,

$$
\begin{aligned}
\mathcal{H}^s(X) > 0 & \iff(\forall B \in 2^{\leq \omega})(\exists x \in X)\brk{\liminf_{r \to \infty} \operatorname{\Delta M}_s^B(\restrict{x}{r}) > -\infty}\\
& \iff(\forall B \in 2^{\leq \omega})(\exists x \in X)\brk{\liminf_{r \to \infty} \operatorname{\Delta P}_s^B(\restrict{x}{r}) > -\infty}, \\
\mathcal{H}^s(X) < \infty &\iff (\exists B \in 2^{\leq \omega}) \brk{\sup_{x \in X} \liminf_{r \to \infty} \operatorname{\Delta M}_s^B(\restrict{x}{r}) < \infty}.
\end{aligned}
$$
:::

Again by Theorem [%s](#theorem:complexity_characterizations_of_randomness), $X$ is not $s$-null if and only if there is an ML-$B$-$s$-random element in $X$ for every oracle $B$.

In effect, these refined point-to-set principles demonstrate the usefulness of *a priori* complexity–defined by {term}`continuous semimeasures <Continuous semimeasure>`–in characterizing not just Hausdorff dimension but also the $s$-dimensional Hausdorff outer measures.

On $\mathbb{R}^m$, Miyabe's ball codes also give a classical characterization of nullity at a fixed exponent.

:::{prf:theorem} Hausdorff Nullity; Theorem 3.8 of {cite:t}`Miy26`
:label: theorem:ball_code_nullity
Let $s > 0$ and let $X \subseteq \mathbb{R}^m$ be nonempty. Then $\mathcal{H}^s(X) = 0$ if and only if there is a prefix-free ball code $\varphi$ such that, for every $x \in X$,

$$
\begin{aligned}
\liminf_{r \to \infty} \p{L^\varphi_r(x) - sr} = -\infty.
\end{aligned}
$$
:::

Effectivizing as in Theorem [%s](#theorem:PTS_coding_form) gives a Euclidean analogue of the $\operatorname{\Delta P}$ characterization in Corollary [%s](#corollary:PTS_null_or_finite).

:::{prf:corollary}
:label: corollary:ball_PTS_nullity
Let $s > 0$ and let $X \subseteq \mathbb{R}^m$ be nonempty. Then

$$
\begin{aligned}
\mathcal{H}^s(X) > 0 \iff (\forall B \in 2^{\leq \omega})(\exists x \in X) \brk{\liminf_{r \to \infty} \p{L^{\mathbf{U}^B}_r(x) - sr} > -\infty}.
\end{aligned}
$$
:::

:::{prf:proof}
:nonumber:
($\Leftarrow$): Each $\mathbf{U}^A$ is a prefix-free ball code, so appeal to Theorem [%s](#theorem:ball_code_nullity).

($\Rightarrow$): Suppose $\mathcal{H}^s(X) = 0$ and let $\varphi$ be the code guaranteed by Theorem [%s](#theorem:ball_code_nullity). Rationalize it, changing $L^\varphi_r(x) - sr$ by at most $s$. Then, encode it into an oracle $B$ by Lemma [%s](#lemma:rationalize_and_encode_ball_codes). Exchanging this $L^\varphi_r(x)$ for $L^{\mathbf{U}^B}_r(x)$ introduces at most $O(1)$ error. Thus, $\liminf_r (L^{\mathbf{U}^B}_r(x) - sr) = -\infty$ for every $x \in X$.
:::
