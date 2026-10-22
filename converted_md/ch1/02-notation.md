---
title: "Notation"
label: section:Notation
---

Let $\mathbb{R}$ denote the set of real numbers, $\mathbb{Q}$ the set of rational numbers, and $\omega$ the set of natural numbers (including $0$). Let $\mathbb{D} \subset \mathbb{Q}$ denote the set of all dyadic rational numbers (i.e., numbers of the form $k / 2^l$ for integers $k, l \geq 0$), and $\mathbb{D}_r$ the set of all $r$-dyadic rational numbers (i.e., all simplified dyadic rationals where the power of $2$ in the denominator is no more than $r$). Let $2^n$ denote the set of length-$n$ binary strings, $2^{\leq n}$ the set of all binary strings length no greater than $n$, $2^{< \omega}$ the set of finite binary strings of any length, and analogous definitions for each of $2^{\geq n}$, $2^{> n}$, $2^\omega$, and $2^{\leq \omega}$. Similarly, $\omega^{<\omega}$ will denote the set of finite sequences of natural numbers, and $\omega^\omega$ the set of infinite sequences of natural numbers. Generally, for any space $X$, interpret $X^m$ as the set of length-$m$ tuples over $X$. In particular, elements of $(2^{\leq n})^m$ are $m$-tuples of binary strings of a common length less than or equal to $n$.

If $\delta > 0$ and $A$ is a subset of a metric space $(\Omega, d)$, then let us define the **$\delta$-neighborhood of $A$** to be $B_\delta(A) := \set{x \in \Omega}{d(x, A) < \delta}$. Then for any $x \in \Omega$, the set $B_\delta(x) := B_\delta(\seq{x})$ is the open ball of radius $\delta$ about $x$.

The cardinality of a set $A$ is denoted by $\abs{A}$. We also use $\abs{\cdot}$ for the absolute value on $\mathbb{R}$. Use $\lambda$ to denote the Lebesgue measure on both $2^\omega$ and $\mathbb{R}$. For any $p \in [0, \infty]$, $\normAt{p}{\cdot}$ denotes the $L^p$-norm on Euclidean space, and we may simply write $\norm{\cdot}$ for the standard $L^2$-norm unless specified otherwise. While $\log_b$ will denote the base-$b$ logarithm for any $0 < b \neq 1$, we will always take $\log$ to mean the base-$2$ logarithm. Also let $\mathcal{Q}^m$ be the collection of all the $m$-dimensional dyadic cubes in $\mathbb{R}^m$, consisting of the sets $Q(z, a, r)$ of the form:

$$
\begin{aligned}
[z_0 + a_0 \cdot 2^{-r}, z_0 + (a_0 + 1) \cdot 2^{-r}) \times \cdots \times [z_{m - 1} + a_{m - 1} \cdot 2^{-r}, z_{m - 1} + (a_{m - 1} + 1) \cdot 2^{-r}),
\end{aligned}
$$

where $z \in \mathbb{Z}^m$, $a \in \omega^m$, and $r \in \omega$. Collect into $\mathcal{Q}^m_r$ all the $m$-dimensional dyadic cubes $Q(z, a, r)$ with side-length $2^{-r}$.

It will often happen that certain equalities hold only up to an additive or multiplicative constant. For this reason we use the following notation: a statement of the form $f(x) \leq^+ g(x)$ for all $x \in X$ means that there exists a constant $c \in \mathbb{R}$ such that $f(x) \leq g(x) + c$ for all $x \in X$. Similarly $f(x) =^+ g(x)$ for all $x \in X$ means that $f(x) \leq^+ g(x) \leq^+ f(x)$ for all $x \in X$. Similarly, $f(x) \leq^* g(x)$ for all $x \in X$ will mean there exists a constant $c \in \mathbb{R}$ such that $f(x) \leq c \cdot g(x)$ for all $x \in X$, and similar for $f(x) =^* g(x)$. Similarly, the notation $f = O_{\boldsymbol{v}}(g)$ is to be interpreted as $f \leq^* g$ everywhere, where the implicit multiplicative constant may depend on the components in $\boldsymbol{v}$. And the notation $o(r)$ is used to represent a **sub-linear term**, or a term which satisfies $\lim_{r \to \infty} \frac{o(r)}{r} = 0$.

The length of a string $\sigma \in 2^{\leq \omega}$ may be denoted by $\operatorname{len}(\sigma)$ (infinite whenever $\sigma \in 2^\omega$). A string $\tau \in 2^{\leq \omega}$ **extends** another string $\sigma \in 2^{\leq \omega}$ if $\tau(n) = \sigma(n)$ for all $n < \operatorname{len}(\sigma)$, and this is denoted by $\sigma \preceq \tau$. Moreover, $\tau$ is a **proper extension** of $\sigma$ if $\sigma \preceq \tau$ yet $\sigma \neq \tau$. Two strings $\sigma$ and $\tau$ are **comparable** (denoted $\sigma \mid\mid \tau$) if either $\sigma \preceq \tau$ or $\tau \preceq \sigma$. String concatenation is denoted by $\sigma^\smallfrown \tau$ (or sometimes $\sigma \tau$, omitting the concatenation symbol) for any strings $\sigma \in 2^{<\omega}$ and $\tau \in 2^{\leq \omega}$. Formally, this is defined as the unique string of length $\operatorname{len}(\sigma) + \operatorname{len}(\tau)$ such that $\sigma \preceq \sigma^\smallfrown \tau$ and $(\sigma^\smallfrown \tau)(\operatorname{len}(\sigma) + n) = \tau(n)$ for all $0 \leq n < \operatorname{len}(\tau)$.

A collection of finite binary strings $S \subseteq 2^{<\omega}$ is called **prefix-free** if no two elements of $S$ are comparable, i.e., $(\forall \sigma, \tau \in S)[\neg(\sigma \mid\mid \tau)]$. Then for any $S \subseteq 2^{<\omega}$, denote by $\widehat{S}$ the collection of all minimal elements of $S$ with respect to the prefix partial relation, i.e.,

$$
\begin{aligned}
\widehat{S} := \set{\sigma \in S}{\neg (\exists \tau \preceq \sigma)[\tau \in S]}.
\end{aligned}
$$

Notice that $\widehat{S}$ will always be a prefix-free subset of $S$.

For any finite binary string $\sigma \in 2^{<\omega}$, denote by $[\sigma]$ the **cylinder set above $\sigma$** comprising all infinite extensions of $\sigma$. Collect into $\mathcal{B}$ all of the cylinder sets above the finite strings from $2^{<\omega}$. Then $\mathcal{B}$ serves as a clopen basis for the product topology on $2^\omega$, in which every open set is of the form $[S] := \bigcup_{\sigma \in S} [\sigma]$, where $S \subseteq 2^{<\omega}$. Also, let $\bbrk{\sigma} := \set{\tau \in 2^{<\omega}}{\sigma \preceq \tau}$ denote the collection of finite binary strings extending $\sigma$. The truncation of a binary string $\sigma \in 2^{\leq \omega}$ up to the first $r \geq 0$ places is denoted by $\restrict{\sigma}{r} = (\sigma(i) : i < \min\seq{r, \operatorname{len}(\sigma)})$.

The length of a string tuple $\sigma = (\sigma_1, \sigma_2, ..., \sigma_m)$ is defined as

$$
\begin{aligned}
\operatorname{len}(\sigma) := \min \seq{\operatorname{len}(\sigma_1), \operatorname{len}(\sigma_2), ..., \operatorname{len}(\sigma_m)},
\end{aligned}
$$

or infinite when all components are of infinite length. We may extend the prefix relation to string tuples $\sigma, \tau \in (2^{\leq \omega})^m$ component-wise,

$$
\begin{aligned}
\sigma \preceq \tau :\iff (\sigma_1 \preceq \tau_1) \AND (\sigma_2 \preceq \tau_2) \AND \cdots \AND (\sigma_m \preceq \tau_m).
\end{aligned}
$$

The truncation of a real number $x \in \mathbb{R}$ up to precision-level $r \in \omega$ may be defined as $\restrict{x}{r} := 2^{-r} \cdot \floor{x \cdot 2^r}$. Under the standard association between real numbers and their infinite binary expansions (under the convention of only permitting infinite tails of zeros), these two notions of truncation agree in the following sense. Without loss of generality, consider $x \in [0, 1)$ and let $x$ have the infinite binary expansion $0.x(0)x(1)x(2) \cdots$. Then, for any $r \in \omega$, it holds that its length-$r$ truncation as a string (followed by an infinite tail of zeros) $0.x(0) x(1) \cdots x(r - 1)^\smallfrown 0^\omega$ is the infinite binary expansion of the real number $\restrict{x}{r}$.

Truncation for a real tuple $x = (x_1, x_2, ..., x_m) \in \mathbb{R}^m$ is taken component-wise:

$$
\begin{aligned}
\restrict{x}{r} := \p{\restrict{x_1}{r}, \restrict{x_2}{r}, ..., \restrict{x_m}{r}} \in B_{2^{-r} \sqrt{m}}(x) \cap \mathbb{D}_r^m.
\end{aligned}
$$

Consider the collections of natural numbers: $\omega$, finite binary strings: $2^{<\omega}$, or dyadic rationals: $\mathbb{D}$. For the purposes of computability theory, we assume that between each pair of these sets there exists a computable bijection. Other collections can be added to this list, including the cylinder sets: $\mathcal{B}$, all the finite subsets of $\omega$, the integers: $\mathbb{Z}$, the rationals: $\mathbb{Q}$, the collection of finite sequences of natural numbers: $\omega^{<\omega}$, and finite-products of such sets. We say that each such collection is composed of **finitary** objects, also known as **hereditarily finite objects**. Whenever a definition is appropriate for any finitary object, we will state the definition using the symbol $\mathscr{N}$ as a placeholder for any one of these collections.

For instance, given a standard collection of finitary objects $\mathscr{N}$ as described above and an element $n \in \mathscr{N}$, one might evaluate $\operatorname{len}(\cdot)$, truncation, or the prefix relation on the finite binary string to which $n$ is associated under a canonical, computable bijection between $\mathscr{N}$ and $2^{<\omega}$.

Finitary objects often give rise to **infinitary** objects via some limiting process and thus admit a notion of extension. For instance, any infinite binary string $x \in 2^\omega$ is the limiting sequence of its prefixes $\restrict{x}{r} \in 2^{<\omega}$ for $r \in \omega$. Any real $x \in \mathbb{R}$ is definable by Dedekind cuts over the rationals $\mathbb{Q}$. Any infinite subset of $\omega$ is the countable union of finite, nested subsets of $\omega$. Mappings between spaces of infinitary objects depend on the context, and each space of infinitary objects can take on extra metric or topological structure, so we will treat these spaces individually. Other examples include the set of countably-infinite sequences of natural numbers: $\omega^\omega$, and the set of infinite subsets of $\omega$ and their characteristic functions.
