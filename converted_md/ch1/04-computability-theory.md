---
title: "Computability Theory"
label: section:Computability_Theory
---

## Computability by Machines

We briefly review the necessary components of computability theory for discussing algorithmic randomness. In this dissertation, we accept Turing's model of computation as the “right” way to characterize **algorithmic** or **effective** procedures. According to the Church-Turing thesis, the subsets of the natural numbers or functions from natural numbers to natural numbers which are “intuitively algorithmic” are exactly those which may be computed by Turing machines. See {cite:t}`DH10` for more on the formalism of Turing machines.

To begin, we will consider partial functions of the form $\Phi : \subseteq \omega \to \omega$. If $\operatorname{dom}(\Phi) = \omega$, call $\Phi$ **total**. Each Turing machine $M$ **computes** a partial function $\Phi_M : \subseteq \omega \to \omega$ satisfying $n \in \operatorname{dom}(\Phi_M) \iff M(n) \downarrow$, and $n \in \operatorname{dom}(\Phi_M)$ implies $M(n) \downarrow= \Phi_M(n)$. All such $\Phi_M$ are called **partial computable (p.c.)** functions. Moreover, whenever $A = \operatorname{dom}\Phi_M$ is the domain of a Turing machine $M$, then $M$ is said to **computably enumerate** $A$, making $A$ **computably enumerable (c.e.)**. If both $A$ and its complement $\omega \setminus A$ are c.e., then $A$ is called **computable**.

Proposition 2.2.2 of {cite:t}`DH10` helps to motivate the name “computably enumerable.” It states that $A$ is c.e. if and only if either $A$ is empty or there is a total computable function $\Phi$ from $\omega$ onto $A$. That is, the non-empty c.e. sets are exactly those enumerated in some order by a Turing machine.

By the Enumeration Theorem (see Theorem 2.1.2 of {cite:t}`DH10`), there exists a single algorithm to enumerate all partial computable functions $(\Phi_e)_{e \in \omega}$. Thus, there exists a **universal** partial computable function $f$ of two variables such that $f(e, n) = \Phi_e(n)$ for all $e, n \in \omega$ (note that they could both diverge). Let $\mathbf{U}$ be a Turing machine computing $f$, which is called a **universal Turing machine**.

A similar result holds for oracle machines or Turing functionals (see {cite:p}`RS15` and {cite:p}`DH10` for more details). Intuitively, oracle machines are Turing machines which receive and may make use of the extra information encoded in some **oracle**. An oracle machine $M$ given oracle $B \in 2^{\leq \omega}$ is said to compute a **$B$-partial computable function** $\Phi^B_M : \subseteq \omega \to \omega$ as before. Similarly, there is a single oracle machine (also called $\mathbf{U}$) which, given an oracle $B \in 2^{\leq \omega}$, will enumerate all $B$-partial computable functions $(\Phi^B_e)_{e \in \omega}$.

If there is an oracle machine $M$ that computes the set $A \subseteq \omega$ given an oracle $B$, then $A$ is said to be **Turing reducible** to $B$, or **$B$-computable**. This is denoted by $A \leq_{\operatorname{T}} B$. Similarly, a set $A$ is **computably enumerable in $B$** (or, **$B$-c.e.**) whenever $A = \operatorname{dom} \Phi$ for some $B$-partial computable function $\Phi$. **Relativization** is the process of generalizing notions or results from Turing machines to oracle machines given arbitrary oracle-power. Most results we cite from computability theory may be relativized appropriately.

In later sections, we will also make use of lower- or upper-semicomputability. A real number $x \in \mathbb{R}$ is **lower-semicomputable** (or **left-c.e.**) if its Dedekind left cut $\set{q \in \mathbb{Q}}{q < x}$ is c.e. Similarly, a real-valued map $f: \omega \to \mathbb{R}$ is **lower-semicomputable** if its lower graph $\set{(n, q) \in \omega \times \mathbb{Q}}{q < f(n)}$ is c.e. If $f : \omega \to [a, \infty)$ has a known, computable codomain which is bounded from below, we may equivalently characterize lower-semicomputability by the ability to be approximated from below by some computable **left-approximator**. That is, suppose there exists a computable map $\widehat{f} : \omega \times \omega \to [a, b]$ satisfying:

$$
\begin{aligned}
\widehat{f}(i, r) \leq \widehat{f}(i, r + 1) \leq f(i), \quad \text{and} \quad \lim_{r \to \infty} \widehat{f}(i, r) = f(i),
\end{aligned}
$$

for all $i, r \in \omega$. Then, it is straightforward to argue that the lower graph of $f$ is computably enumerable. Conversely, from an enumeration of the lower graph of $f$, one may define such a left-approximator $\widehat{f}$ to $f$: for a given $i \in \omega$, one may approximate $f(i)$ as the largest rational $q$ such that $(i, q)$ has been enumerated into the lower graph of $f$. If no such rational has yet been approximated, we may take $\widehat{f}(i, r) = a$. Analogous definitions work for upper-semicomputability.

The definitions above are given for either subsets of the natural numbers or functions on the natural numbers, but they may be extended to the other standard collections of finitary objects discussed in Section [%s](#section:Notation) via a computable bijection.

## Computable Analysis

Now, let us import some notions from computable analysis as presented in {cite:t}`KF82`. For the rest of this section, fix the ambient dimensions $m, n \in \omega$ and an oracle machine $M$.

Fix a map $\phi : \omega \to \mathbb{D}^m$ from the natural numbers to dyadic rationals in $\mathbb{R}^m$ satisfying $\phi(r) \in \mathbb{D}^m_r$ for all $r \in \omega$. Then, $\phi$ is said to be a **Cauchy representation** of $x \in \mathbb{R}^m$ if $\abs{\phi(r) - x} \leq 2^{-r}$ for all $r \in \omega$. If $\phi$ is a Cauchy representation of $x$ further satisfying $\phi(r) \leq x < \phi(r) + 2^{-r}$ for all $r \in \omega$, then $\phi$ is said to be a **standard Cauchy representation** for $x$. Such a $\phi$ can compute the binary expansion of $x$ having no infinite tail of ones. For any $\phi: \omega \to \mathbb{D}^m$, we will denote by $M^\phi$ the partial map computed by $M$ given $\phi$ encoded as an infinite binary string for its oracle. And $M^x$ will denote the partial map computed by $M^\phi$, where $\phi$ is some standard Cauchy representation of $x$.

$M$ is said to **compute** a real function $f: \mathbb{R}^m \to \mathbb{R}^n$ if $\phi$ being a Cauchy representation for some $x \in \dom(f)$ implies $M^\phi$ is a Cauchy representation of $f(x)$.

Now, fix a metric space $(\Omega, d)$. Two subsets $X$ and $Y$ of $\Omega$ are said to be **$\varepsilon$-close** for $\varepsilon > 0$ if for each $x \in X$, there exists $y \in Y$ such that $d(x, y) < \varepsilon$, and vice versa. The **Hausdorff distance** between $X$ and $Y$ is then defined:

$$
\begin{aligned}
d_{\operatorname{H}}(X, Y) = \inf \set{\varepsilon > 0}{\text{$X$ is $\varepsilon$-close to $Y$}}.
\end{aligned}
$$

We may now recall the effective versions of certain metric spaces as presented in {cite:t}`IK21`.

The triple $\mathbf{\Omega} = (\Omega, d, \alpha)$ is a **computable metric space** if $\alpha = (\alpha_i)_{i \in \omega}$ is a dense sequence in $(\Omega, d)$ for which the function mapping $(i, j) \mapsto d(\alpha_i, \alpha_j)$ is computable.

Take $\mathbf{\Omega} = (\Omega, d, \alpha)$ to be a computable metric space. If $d$ happens to be a complete metric, call $\mathbf{\Omega}$ a **computable Polish space**. Any subset $X \subseteq \Omega$ of a computable metric space is called **computably compact** if either $X = \emptyset$ or there exists a computable map $f : \omega \to \omega$ such that for each $k \in \omega$,

$$
\begin{aligned}
d_{\operatorname{H}}(X, \Lambda_{f(k)}) < 2^{-k},
\end{aligned}
$$

where $\Lambda_e$ is the $e$-th collection enumerated in a standard, computable enumeration of all finite sub-collections of $\alpha$. Then, the computable metric space $\mathbf{\Omega}$ is called **effectively compact** if $\Omega$ is computably compact in $\mathbf{\Omega}$.

## Lightface Hierarchies

Kleene's **arithmetic hierarchy** assigns definability-complexity levels to subsets of the natural numbers. Any set $A \subseteq \omega$ is a **$\Sigma^0_n$-set** if there is a computable relation $R$ on $n + 1$ arguments such that

$$
\begin{aligned}
a \in A \iff \exists x_1 \forall x_2 \cdots Qx_n R(x_1, ..., x_n, a),
\end{aligned}
$$

where the quantifiers alternate and end with $Q$ being $\exists$ whenever $n$ is odd, and $\forall$ when $n$ is even. A **$\Pi^0_n$-set** is the complement of a $\Sigma^0_n$ set. And a set which is both $\Sigma^0_n$ and $\Pi^0_n$ is called $\Delta^0_n$. For convenience, each of $\Delta^0_0$, $\Sigma^0_0$, and $\Pi^0_0$ are defined as containing exactly the computable sets. Moreover, a set is computably enumerable if and only if it is $\Sigma^0_1$, and computable if and only if it is $\Delta^0_1$. This hierarchy may be relativized to any oracle by permitting the relation be Turing-reducible to it.

Suppose $S \subseteq 2^{<\omega}$ is a c.e. set of finite binary strings. Then $[S] := \bigcup_{\sigma \in S}[\sigma]$ is called a **$\Sigma^0_1$-class**, or an **effectively open** subset of Cantor space. The complement of a $\Sigma^0_1$-class is called a **$\Pi^0_1$-class**, or an **effectively closed** subset. Starting from these base classes, an analogous hierarchy to Kleene's arithmetic hierarchy forms for subsets of Cantor space. There are two ways to build higher levels of this lightface hierarchy. The first is by computable relations: a subset $U \subseteq 2^\omega$ is a **$\Sigma^0_n$-class** for $n \in \omega$ if there is a computable relation $R$ on $n$ arguments such that

$$
\begin{aligned}
\alpha \in U \iff \exists x_1 \forall x_2 \cdots Q x_n\ R(x_1, x_2, ..., \restrict{\alpha}{x_n}),
\end{aligned}
$$

again by alternating quantifiers with an appropriate choice for the innermost one $Q$. The complement of a $\Sigma^0_n$-class is a **$\Pi^0_n$-class**. But we may equivalently conceive of the $\Sigma^0_{n + 1}$-classes as uniformly-computable unions of $\Pi^0_n$-classes. This may be formalized using effective Borel codes. And a set which is both a $\Sigma^0_n$-class and a $\Pi^0_n$-class is also called a **$\Delta^0_n$-class**. These notions may be relativized to any oracle $B \in 2^{\leq \omega}$, notated with $B$ in the superscript: $\Sigma^{0, B}_n$, etc. The Fundamental Theorem of effective descriptive set theory states that for any $n \in \omega$, it holds that $\boldsymbol{\Sigma}^0_n = \bigcup_{B \in 2^{\leq \omega}} \Sigma^{0, B}_n$, where $\boldsymbol{\Sigma}^0_n$ denotes the corresponding level of the (boldface) Borel hierarchy from classical descriptive set theory. This motivates naming the hierarchy of $\Sigma^0_n$ and $\Pi^0_n$-classes as the **lightface Borel hierarchy**.
