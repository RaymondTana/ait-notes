---
title: "Prefix Complexity"
label: section:Prefix_Comlexity
---

## Incompressibility

Recall the universal oracle machine $\mathbf{U}$ from Section [%s](#section:Computability_Theory). The universality of $\mathbf{U}$ implies some invariance and minimality properties in the following senses. Let $\sigma$ and $\tau$ be finite binary strings and $M$ to be an oracle Turing machine on finite binary strings. By universality, it holds that there exists a string $\nu_M$ which may be prepended to the input $\sigma$ to allow $\mathbf{U}$ to simulate $M$ on $\sigma$ given any oracle $B$, i.e., $\mathbf{U}^B(\nu_M\ ^\smallfrown \sigma) = M^B(\sigma)$. Define the **conditional plain Kolmogorov complexity of $\sigma$ given $\tau$ in $M$** to be

$$
\begin{aligned}
C_M(\sigma \mid \tau) = \min \set{\operatorname{len}(\pi)}{M^{\overline{\tau}}(\pi) \downarrow= \sigma},
\end{aligned}
$$

or $+\infty$ when minimizing over an empty set; where we map the condition $\tau$ into a prefix-free set of strings via $\overline{\tau} = \tau_0 \tau_0 \tau_1 \tau_1 \cdots \tau_{\operatorname{len}(\tau) - 1} \tau_{\operatorname{len}(\tau) - 1} 01$ (on account of the fact that the set of oracles on which a machine $M$ may converge on a fixed input $\sigma$ must be prefix-free; see {cite:t}`DH10` for more details). Then, call $C(\sigma \mid \tau) := C_{\mathbf{U}}(\sigma \mid \tau)$ the **conditional plain Kolmogorov complexity of $\sigma$ given $\tau$**. Under any other choice of universal machine $\mathbf{U}$, this quantity is invariant up to an additive constant independent of $\sigma$ and $\tau$. Conditional plain complexity also satisfies minimality, in that for any $M$:

$$
\begin{aligned}
C(\sigma \mid \tau) \leq C_M(\sigma \mid \tau) + O_M(1).
\end{aligned}
$$

for some constant term depending on $M$. The **plain Kolmogorov complexity** of a string $\sigma$ is simply $C(\sigma) = C(\sigma \mid \langle \rangle)$. We call any finitary object $\pi$ satisfying $M^{\overline{\tau}}(\pi) \downarrow = \sigma$ an **$M$-description** for “$\sigma \mid \tau$”. Any $M$-description $\pi$ of $\sigma \mid \tau$ for which $\operatorname{len}(\pi) = C_M(\sigma \mid \tau)$ is also called **minimal**.

A **prefix-free (PF) oracle machine** is an oracle machine on finite binary strings with prefix-free domain for any oracle. Any PF oracle machine $M$ computes a prefix-free partial function $\Psi_M :\subseteq 2^{<\omega} \to 2^{<\omega}$ as before. Again, by the Enumeration Theorem, there exists a **universal** PF oracle machine $\mathbf{U}_{\operatorname{PF}}$. That is, for each PF oracle machine $M$, there exists a coding string $\nu_M \in 2^{<\omega}$ such that given any oracle $B$ and input $\sigma \in 2^{<\omega}$, we have $\mathbf{U}_{\operatorname{PF}}^B(\nu_M\ ^\smallfrown \sigma) = M^B(\sigma)$. Once again, $\mathbf{U}_{\operatorname{PF}}$ admits an invariant and minimal complexity notion in the sense that for any other PF oracle machine $M$, there exists an additive constant term $O_M(1)$ such that for any $\sigma, \tau \in 2^{<\omega}$,

$$
\begin{aligned}
C_{\mathbf{U}_{\operatorname{PF}}}(\sigma \mid \tau) \leq C_M(\sigma \mid \tau) + O_M(1).
\end{aligned}
$$

We let $K(\sigma \mid \tau) = C_{\mathbf{U}_{\operatorname{PF}}}(\sigma \mid \tau)$ denote the **conditional prefix Kolmogorov complexity of $\sigma$ given $\tau$**. Both plain and prefix complexities may be relativized to any oracle by pairing the oracle and the condition string (see {cite:p}`DH10` for more details). Then $K^B(\sigma \mid \tau) := C^B_{\mathbf{U}_{\operatorname{PF}}}(\sigma \mid \tau)$ denotes the **conditional prefix Kolmogorov complexity of $\sigma$ given $\tau$ relative to $B$**.

These complexity notions may also be extended to any other standard collection of finitary objects $\mathscr{N}$ with a constant amount of overhead, meaning we would only need to sacrifice at most a constant number of bits to describe the computable bijection between $2^{<\omega}$ and $\mathscr{N}$.

## Results on Prefix Complexity

We review some standard results on prefix complexity.

First, one might refer to the following result as either the **symmetry of information** or the **chain rule** for conditional prefix Kolmogorov complexity. It was first shown by P. Gács {cite:p}`Gac74`. The first equation is the strong form and is a property specific to prefix complexity; whereas the second equation is a weak form (where equality holds up to logarithmic terms in the string lengths) shared by many Kolmogorov complexity notions.

:::{prf:theorem} Chain Rule for Conditional Prefix Kolmogorov Complexity; Theorem 1 of {cite:t}`Gac74`
:label: theorem:chain_rule_for_K
There exists a constant $c \in \omega$ such that for any $\sigma, \tau, \zeta \in 2^{<\omega}$,

$$
\begin{aligned}
\Kc{\sigma, \tau}{\zeta} &= \Kc{\sigma}{\zeta} + \Kc{\tau}{\sigma, \K{\sigma}, \zeta} \pm c\\
&= \Kc{\sigma}{\zeta} + \Kc{\tau}{\sigma, \zeta} \pm [O(\log \operatorname{len}(\sigma)) + c].
\end{aligned}
$$
:::

An easy consequence of the chain rule is the **subadditivity** of $K$: i.e., for any $\sigma, \tau \in 2^{<\omega}$,

$$
\begin{aligned}
K(\sigma^\smallfrown \tau) \leq K(\sigma, \tau) \leq K(\sigma) + K(\tau) + O(1).
\end{aligned}
$$

We may also say something about the growth-rate of $K$ as an integer function. Write $\operatorname{len}(n) + \operatorname{len}(\operatorname{len}(n)) + \cdots$ for the sum of nested applications of $\operatorname{len}$, including only those terms which are positive. Let $\log^*(n)$ denote the number of such terms in that sum. Thenm, for any natural number $n \in \omega$, the optimized prefix-codes in equation (3.2) of {cite:t}`LV08` demonstrate

```{math}
:label: equation:K_bound_for_naturals
\begin{aligned}
\K{n} &\leq \log^* n + \operatorname{len}(n) + \operatorname{len}(n)) + \operatorname{len}(\operatorname{len}(\operatorname{len}(n))) + \cdots + O(1) \\
&\leq \log(1 + n) + 2 \log \log (2 + n) + O(1) \\
&= O(\log n) + O(1) .
\end{aligned}
```

Intuitively, we consider $n$ to be a finite binary string of length $\operatorname{len}(n)$. One description of $n$ involves storing an index (of length no more than $\operatorname{len}(n)$) of where $n$ appears among all other strings of length $\operatorname{len}(n)$ when ordered lexicographically. This algorithm requires a description for $\operatorname{len}(n)$ to work, so we might iterate the argument on $\operatorname{len}(n)$ as appearing somewhere in the list of all strings of length $\operatorname{len}(\operatorname{len}(n))$, and so on. The $\log^* n$ term is necessary because our machine must be prefix-free.

Together, the chain rule [%s](#theorem:chain_rule_for_K) and the inequality in ([%s](#equation:K_bound_for_naturals)) imply the results of Example 3.1.6 of {cite:t}`LV08`. Namely, that for any finitary $n \in \omega$,

```{math}
:label: upper_limit_to_K
\begin{aligned}
\K{n} &\leq \Kc{n}{\operatorname{len}(n)} + \K{\operatorname{len}(n)} + O(1)  \\
&\leq \Kc{n}{\operatorname{len}(n)} + \log^* \operatorname{len}(n) + \operatorname{len}(\operatorname{len}(n))+ \cdots + O(1) \\
&\leq \Kc{n}{\operatorname{len}(n)} + \log \p{1 + \operatorname{len}(n)} + 2 \log \log (2 + \operatorname{len}(n)) + O(1)  \\
&= \Kc{n}{\operatorname{len}(n)} + O(\log \operatorname{len}(n)) + O(1).
\end{aligned}
```

This fact extends to a complexity bound for any integer tuple based on its Euclidean length (see Observation A.3 of {cite:t}`LL18`): for any tuple-length $m \in \omega$ and integer tuple $z \in \mathbb{Z}^m$,

```{math}
:label: equation:K_bound_int_tuple
\begin{aligned}
K(z) &\leq m \cdot \log \p{1 + \norm{z}} + 2 \cdot \log \log \p{2 + \norm{z}} + O_m(1).
\end{aligned}
```

The form of this inequality extends to any $r$-dyadic rational tuple $q \in \mathbb{D}^m_r$, where the constant term may depend on both $m$ and $r$.

We include here the conditional version of another standard observation for Kolmogorov complexity: that the complexity of the output of an algorithm is bounded from above by the the complexity of the input plus some overhead to describe the algorithm. This follows from the universality of $\mathbf{U}_{\operatorname{PF}}$.

:::{prf:theorem} Conditional version of Proposition 3.5.4 of {cite:t}`DH10`
:label: theorem:bounded_computable_output
Let $\Phi : \subseteq 2^{<\omega} \to 2^{<\omega}$ be partial computable. Then, there exists a constant $c \in \omega$ such that for any $\sigma \in \dom(\Phi)$ and $\tau \in 2^{<\omega}$,

$$
\begin{aligned}
K(\Phi(\sigma) \mid \tau) \leq K(\sigma \mid \tau) + c.
\end{aligned}
$$
:::

As a consequence, as noted on page 218 of {cite:t}`LV08`, one may conclude that $K$ is continuous as an integer function. That is, for any natural numbers $n, \Delta n \in \omega$,

$$
\begin{aligned}
\abs{\K{n + \Delta n} - \K{n}} \leq \K{\Delta n} + O(1).
\end{aligned}
$$

We might extend this and Theorem [%s](#theorem:bounded_computable_output) as follows. Define $\Phi : \subseteq 2^{<\omega} \to 2^{<\omega}$ to be **partial co-computable (p.c.c.)** if $\Phi$ is injective and has a partial computable inverse defined on the range of $\Phi$. And $\Phi$ is called **partial bi-computable (p.b.c.)** if $\Phi$ is both partial computable and partial co-computable.

:::{prf:proposition}
:label: proposition:bi_computable_K
Let $\Phi : \subseteq 2^{<\omega} \to 2^{<\omega}$. Then there exists a constant $c \in \omega$ such that for any $\sigma \in \dom(\Phi)$ and $\tau \in 2^{<\omega}$,

$$
\begin{aligned}
\Phi \text{ is p.c.} &\implies K(\Phi(\sigma) \mid \tau) \leq K(\sigma \mid \tau) + c \quad \text{and} \quad K(\tau \mid \sigma) \leq K(\tau \mid \Phi(\sigma)) + c,\\
\Phi \text{ is p.c.c.} &\implies K(\sigma \mid \tau) \leq K(\Phi(\sigma) \mid \tau) + c \quad \text{and} \quad K(\tau \mid \Phi(\sigma)) \leq K(\tau \mid \sigma) + c,\\
\Phi \text{ is p.b.c.} &\implies K(\Phi(\sigma) \mid \tau) = K(\sigma \mid \tau) \pm c \quad \text{and} \quad K(\tau \mid \Phi(\sigma)) = K(\tau \mid \sigma) \pm c.
\end{aligned}
$$
:::

Let us describe a general scheme for proving bounds for prefix complexity. Suppose we would like to prove a bound of the form:

$$
\begin{aligned}
K(a \mid b) \leq K(a_1 \mid b_1) + \cdots + K(a_k \mid b_k) + O(1),
\end{aligned}
$$

where $a, b$ and $a_1, b_1, ..., a_k, b_k$ are some finitary arguments and $O(1)$ may depend on $k$. In plainer language, this would read as “one may produce a description for $a$ given $b$ and given descriptions for each $a_i$ given $b_i$.”

Formally, to prove a bound of this form, one should construct an appropriate PF oracle machine exhibiting it. The machine $M$ should interpret its input as a tuple of $k$ strings: $\langle \pi_{\widehat{a}_1 \mid \widehat{b}_1}, ..., \pi_{\widehat{a}_k \mid \widehat{b}_k} \rangle$, and read a string $\widehat{b}$ from its oracle tape. The machine may use $\widehat{b}$ and any other results stored along the course of the computation to produce some strings called $\widehat{b}_i$ for any of the $1 \leq i \leq k$. Also, for any $1 \leq i \leq k$ for which $\widehat{b}_i$ is defined, the machine may also simulate $\mathbf{U}_{\operatorname{PF}}$ with oracle $\widehat{b}_i$ and input $\pi_{\widehat{a}_i \mid \widehat{b}_i}$ to compute and report a string called $\widehat{a}_i$ if the computation converges. Of course, it depends on the specific argument how exactly the machine will operate.

With this oracle machine now defined, one would pass into $M$ the oracle $b$ and the input consisting of minimal $\mathbf{U}_{\operatorname{PF}}$-descriptions $\pi_{a_i \mid b_i}$ for $a_i$ given $b_i$ for each $1 \leq i \leq k$. Supposing that $M$ was properly defined so as to halt on this choice of oracle and input and to correctly report $a$, we may then conclude:

$$
\begin{aligned}
K(a \mid b) &\leq C^b_M(a_1, ..., a_k \mid b_1, ..., b_k, k) + O(1)\\
&\leq \operatorname{len}(\pi_{a_1 \mid b_1}) + \cdots + \operatorname{len}(\pi_{a_k \mid b_k}) + K(k) + O(1)\\
&= K(a_1 \mid b_1) + \cdots + K(a_k \mid b_k) + K(k) + O(1).
\end{aligned}
$$

It is standard practice to instead verbally explain an (intuitive) algorithm which produces $a$ from $b$ and the other descriptions $a_i \mid b_i$, and then to appeal to the Church-Turing thesis to conclude there exists a prefix-free oracle machine simulating that process. Several of the proofs provided here follow this form for the sake of clarity.

One may use this scheme to prove Proposition [%s](#proposition:bi_computable_K). It also works for **two-part descriptions**. Let $\mathscr{N}$ be any standard collection of finitary objects and $n \in \mathscr{N}$. Given $n \in A$ for some finite set $A \subset \mathscr{N}$, we have that $K(n) \leq K(A) + \log \abs{A} + O(1)$. That is, a description (of a computable enumeration) of $A$, together with a description for the index $i$ when $n$ appears in that enumeration of $A$, suffice to describe $n$ as the $i$-th element enumerated into $A$. In this sense, the pair $(A, i)$ forms a two-part description for $n$. Two-part descriptions are also important in the study of algorithmic statistics {cite:p}`VS16`.

An easy consequence of $\mathbf{U}_{\operatorname{PF}}$ being prefix-free is the **Kraft Inequality**.

:::{prf:theorem} Kraft Inequality, Proposition 3.7.1 of {cite:t}`DH10`
:label: theorem:kraft_inequality
$$
\begin{aligned}
\sum_{\sigma \in 2^{<\omega}} 2^{-K(\sigma)} \leq 1.
\end{aligned}
$$
:::

Next, Chaitin's **Counting Theorem** offers useful bounds for the behavior of $K$ on the strings of some fixed length. This essentially follows from the universality of $\mathbf{U}_{\operatorname{PF}}$.

::::{prf:theorem} Chaitin's Counting Theorem {cite:p}`Cha76`, Theorem 3.7.6 of {cite:t}`DH10`
:label: theorem:chaitin_counting_theorem
There exists a constant $c \in \omega$ such that for any $n, r \in \omega$,

:::{div}
:class: roman-list
1. $\max \set{K(\sigma)}{\sigma \in 2^n} = n + K(n) \pm c$, and
1. $\abs{\set{\sigma \in 2^{n}}{K(\sigma) \leq n + K(n) - r}} \leq 2^{n - r + c}$.
:::
::::

It is interesting to note that the theory of prefix complexity (an algorithmic entropy notion) mimics that of Shannon entropy {cite:p}`Kol68`, and that $K$ satisfies the same linear inequalities true for all inputs as Shannon entropy $H$ up to a logarithmic term in the sum of the lengths of the strings involved. This may be made precise by translating between random variables with finite range and finite binary strings, as is done in {cite:t}`HRSV00`.
