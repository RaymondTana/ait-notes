---
title: "1.12 Point-to-Set Principles"
label: section:PTS
---

In this context, a point-to-set (PTS) principle will characterize the fractal dimension or measure content of a subset by some local dimension or measure assigned to its elements. We summarize the few PTS principles known for Hausdorff dimension and the $s$-dimensional Hausdorff outer measures via algorithmically-restricted quantities.

## 1.12.1 PTS for Hausdorff Dimension

Certain fractal dimension notions have pointwise, algorithmic characterizations (over simple spaces such as Cantor space and Euclidean space). This was originally shown for Hausdorff dimension in 2017 by J. Lutz and N. Lutz {cite:p}`LL18`.

:::{prf:theorem} Point-to-Set Principle; Theorem 1 of {cite:t}`LL18`
:label: theorem:PTS_for_H_dimension
:enumerator: 1.12.1
For any $X \subseteq 2^\omega$ or $X \subseteq \mathbb{R}^m$, we have

$$
\begin{aligned}
\dim_{\operatorname{H}} X = \min_{B \in 2^{\leq \omega}} \sup_{x \in X} \dim^B(x).
\end{aligned}
$$
:::

Notably, this implies that for each subset $X$, there exists an oracle $B \in 2^{\leq \omega}$ which is powerful enough to simulate Hausdorff dimension by ML-$B$-$s$-tests. Any such oracle is called a *Hausdorff oracle* for $X$. An analogous formula holds for classical packing dimension (see Theorem 2 of {cite:t}`LL18`), swapping weak effective dimension $\dim$ for strong dimension: $\operatorname{Dim}$.

The main insight used to prove the Point-to-Set Principle involves the ability to build for a fixed set $X \subseteq \mathbb{R}^m$ an oracle $B$ with knowledge of how $X$ intersects with any given dyadic cube from $\mathcal{Q}^m$. Arbitrary covers of $X$ exhibiting $\dim_{\operatorname{H}} X$ may be approximated using covers comprising dyadic cubes, and so the Hausdorff dimension of $X$ is the supremum of the size of the intersection with $X$ along nested sequences of dyadic cubes. Suppose that the intersection of a nested sequence intersecting with $X$ is the singleton set containing $x \in X$. Then $\dim^B(x)$ exactly captures how much dimension $X$ takes on at $x$.

In practice, the power of the Point-to-Set Principle is in proving lower-bounds for Hausdorff dimension. As remarked to me by Ryan Bushling, one might as well consider this a *local-to-global* principle for the following reason: in order to witness a lower bound on $\dim_{\operatorname{H}}X$, it is not enough to find a single sufficiently-random element $x \in X$, for any countable number of reals could be coded into an oracle. Instead, one must demonstrate the existence of *many* highly-complex elements of $X$, which requires knowledge of a large portion of the set to do.

The Point-to-Set Principle has found applications across geometric measure theory, including in bounding the Hausdorff dimension of Furstenberg sets {cite:p}`LS16; Stu18`, lineal extensions {cite:p}`BF25`, distance sets {cite:p}`ABW23`, and pinned-distance sets {cite:p}`Stu22_pinned`; as well as in extending the Marstrand-Mattila Projection Theorem {cite:p}`Stu21`.

Well before the full Point-to-Set Principle was proved, L. Staiger {cite:p}`Sta89` and B. Ryabko {cite:p}`Rya93; Rya94` had already observed versions of the Point-to-Set Principle for simply-definable classes such as $\Sigma^0_2$-classes. This was slightly generalized by J. Hitchcock in {cite:t}`Hit05` in what he calls a *correspondence principle* between constructive dimension and Hausdorff dimension {cite:p}`Hit05`. The spirit of any correspondence principle is to characterize a classical notion by unrelativized, effective means (i.e., avoiding oracles).

:::{prf:theorem} Correspondence Principle for Hausdorff dimension, Theorem 5.3 of {cite:t}`Hit05`
:label: theorem:correspondence_principle_for_H_dimension
:enumerator: 1.12.2
For any $\Sigma^0_2$-class $X \subseteq 2^\omega$, we have

$$
\begin{aligned}
\dim_{\operatorname{H}} X = \dim(X).
\end{aligned}
$$
:::

Hitchcock further showed that this correspondence broke down immediately beyond this level of the lightface Borel hierarchy.

## 1.12.2 PTS for Hausdorff Measures

The original Point-to-Set Principle has recently been refined to the $s$-dimensional Hausdorff outer measures by P. Lutz and J. Miller {cite:p}`LM24`. These results also expand on the complexity characterizations of various partial randomness notions from Theorem [1.11.2](#theorem:complexity_characterizations_of_randomness).

:::{prf:theorem}
:label: theorem:PTS_log_s_measure_and_sigma_finite
:enumerator: 1.12.3
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

By Theorem [1.11.2](#theorem:complexity_characterizations_of_randomness), $X$ is not $\sigma$-finite in dimension $s$ if and only if there is a strong Solovay-$B$-$s$-random element in $X$ for every oracle $B$.

:::{prf:corollary}
:label: corollary:PTS_null_or_finite
:enumerator: 1.12.4
For every $X \subseteq 2^\omega$ and $s \geq 0$,

$$
\begin{aligned}
\mathcal{H}^s(X) > 0 & \iff(\forall B \in 2^{\leq \omega})(\exists x \in X)\brk{\liminf_{r \to \infty} \operatorname{\Delta M}_s^B(\restrict{x}{r}) > -\infty}\\
& \iff(\forall B \in 2^{\leq \omega})(\exists x \in X)\brk{\liminf_{r \to \infty} \operatorname{\Delta P}_s^B(\restrict{x}{r}) > -\infty}, \\
\mathcal{H}^s(X) < \infty &\iff (\exists B \in 2^{\leq \omega}) \brk{\sup_{x \in X} \liminf_{r \to \infty} \operatorname{\Delta M}_s^B(\restrict{x}{r}) < \infty}.
\end{aligned}
$$
:::

Again by Theorem [1.11.2](#theorem:complexity_characterizations_of_randomness), $X$ is not $s$-null if and only if there is an ML-$B$-$s$-random element in $X$ for every oracle $B$.

In effect, these refined point-to-set principles demonstrate the usefulness of *a priori* complexity–defined by continuous semimeasures–in characterizing not just Hausdorff dimension but also the $s$-dimensional Hausdorff outer measures.
