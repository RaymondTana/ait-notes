The "Big refactor" section is really just a collection of edits an agent suggested to the rest of the content. Only reference it when necessary. 

- Big refactor: follow these steps
    
    ## Part A. Main findings
    
    ### A.1 Gaps in rigor
    
    1. **The Kraft–Carathéodory lemma (§8.2) assumes a hypothesis its main application violates, and (KC2) has a strictness gap.** The lemma assumes $\sum_{Q \in \mathcal{D}} a(Q) \leq 1$, but $\sum_{Q \in \mathcal{D}} \mu_A(Q) = \sum_r \mu_A(\mathbb{R}^n) = \infty$. The draft works around this, either by redoing the argument in §8.4 or by transferring through (17), but neither half of the proof uses summability of $a$, so the clean fix is to drop the hypothesis. Separately, (KC2) concludes the *strict* inequality $b > 2^{\eta r} a$, which fails on cubes with $a(Q) = 0$, and the "immaterial constant factor" doesn't repair that. A non-strict "targeted set" version makes the duality *exact at the same exponent*, with no $\eta < \varepsilon$ slack (C.5).
    2. **(17) and (18) need cleaner proofs.** For (17), Shannon–Fano coding needs a computable distribution. $\mu_A$ is only lower semicomputable relative to $A$, so the right tool is the relativized coding theorem applied to $(r, k) \mapsto 2^{-K(r)} \mu_A(Q_{r,k})$. The "index of $Q$" must also include $r$. For (18), the precision shift is handled by citing "the refinement estimate from Section 5.1," which no longer appears in §5.1. A subcube trick avoids it entirely and gives explicit constants: $K_r^Z(x) - c \leq C^Z(Q_r(x)) \leq K_r^Z(x) + K(r) + c$ (C.6).
    3. **The proofs in §7.2 and §7.3 skip a step each.** The Claim in §7.2 asserts $\Pi_m(K_i) \downarrow \Pi_m(K)$ without the argument that some heavy atom lies in every $K_i$. The (P2SC) lower bound doesn't justify that each point still lies in a *small* ball once the heavy atoms are removed (this needs $q_r \to x$, $q_r \neq x$, and finiteness of $\{a \geq c\}$), and it concludes $\mathcal{H}^t(E) = 0$ where it has shown $\mathcal{H}^t(E \setminus S) = 0$. Both are filled in C.1 and C.2.
    4. **Several references are undefined or stale.** These are (K)–(PC) (lines 980, 988), (KC) and $a_A$ (lines 1042, 1084), "Stull's bad preservation set $D$" (line 1305), and "the refinement estimate from Section 5.1" (line 1255). The first three were defined in the older report and lost in the edit.
    
    ### A.2 Simplifications that are themselves theorems
    
    1. **The $s = 0$ case is trivial.** If $\dim_H X = 0$ and $x_0 \in X$, then $A_0 \oplus x_0$ is an optimal Hausdorff oracle for any Hausdorff oracle $A_0$. 
        1. Since $K^{A}_r(x_0) \leq K(r) + O(1)$, $x_0$ witnesses preservation against every $B$, and the high-dimension clause $\dim^{A,B}(x_0) \geq 0 -\varepsilon$ is vacuous. Every theorem can be stated for $s > 0$ with a one-line remark, and the $s = 0$ clauses 
    2. **The minimizing clause is never needed for existence.** Robustness is upward closed in the base object, and minimizers always exist. So **Theorem E simplifies to: $X$ has an optimal Hausdorff oracle iff some finite Borel $\mu$ satisfies (PHE).** The same holds for (M) in Theorems A–C, attainment of (P2SC) in Theorem D, and Stull's [WITNESS] clause (C.7).
    3. **The first clauses of (H) and (CH) are redundant at the level of the definition.** Testing against $\varphi \vee \psi$, or against $\tfrac12 \max\{\Pi, \Lambda\}$, supplies them (C.4). Line 400 is right pointwise, but as a $\forall \psi\, \exists x$ statement the clause does follow. This also answers the "[but why not include $\varphi$…]" note in `some_comments.md`.
    4. **The witness measure can always be taken absolutely continuous with respect to Lebesgue measure.** What handles Berstein sets is that $\mu$ is *ambient*: Lebesgue measure itself witnesses a full-dimensional Bernstein set. 
    
    ### A.3 New results that make Theorem E usable as a GMT tool
    
    With upward closure, Theorem E gives short classical proofs, with no oracles, of the following (C.8). All of these results are already in Stull's paper, proved with oracles: Proposition 7, Observation 6, Theorem 13, Lemma 15, and Lemma 17. What's new is the oracle-free route.
    
    - Closure under countable unions, under full-dimensional supersets, and under deletion of lower-dimensional parts.
    - Stull's measure criterion: §9.1 becomes a three-line corollary.
    - Analytic sets, via Frostman.
    - Weakly regular sets. This is the one place where my proof uses the tilt, and it shows why $\eta > 0$ is there: if every point of $N$ has upper dyadic local dimension $\leq t$ and $\mathscr T_{\mu,\eta}(N) = 0$, then $\dim_H N \leq t - \eta$.
    
    **Exact gauges are not necessary, and without regularity they are not sufficient (C.9).**
    
    - *Not necessary.* A compact union of Ahlfors-regular Cantor sets of increasing dimension has optimal oracles but no exact gauge.
    - *Not sufficient without regularity.* Under AC + CH, Stull's own construction runs inside a regular Cantor set. Combined with a set built for an oscillating gauge, this gives a set that has an exact gauge in Stull's sense but no optimal Hausdorff oracle. So the implication in Stull's abstract needs the hypothesis (CMP), equivalently $\underline\alpha(h) = \dim_H X$.
    
    **Packing (C.10).** §11 relies on two facts.
    
    - The packing analogue of Stull's Proposition 4. Stull states it as his Proposition 33, but his proof of the backward direction is copied from the Hausdorff case, so C.10 supplies a corrected proof.
    - A packing "measure point-to-set" lemma. This is the packing half of Cutler's weak duality principle (C.7, Part F).
    
    **Theorem C ⟺ Theorem E without oracles (C.11).** Four transfer lemmas connect ball systems, measures, and dyadic weights, so oracles enter the whole development only in Theorem A.
    
    ---
    
    ## Part B. Line-by-line notes
    
    ### §7.5
    
    - **1042**: (KC) and $a_A$ are undefined; insert C.3.
    - **1047**: after rounding, the constant is $2^{-c-1}$. Harmless.
    - **1056**: the "smaller tolerance $\delta$" isn't needed, since only $O(1)$ losses occur here, so any $\delta < \varepsilon$ works. It's worth stating that **Theorem D's proof has no $O(\log r)$ losses at all**, unlike Theorem A's, because $K^A_r$ is exactly the capacity code length. That argues for making the capacity theorem the primary bridge to oracles.
    - **1078–1090**: $\delta$ appears in the converse without being introduced. Write "apply (CH)–(CP) with tolerance $\delta$."
    - **1092–1100**: the full-dimensional argument is correct. I checked both directions, including the case split on whether the witness lies in the good set.
    
    ### §7.6
    
    - **1112**: accurate as written (Part F). You could add that Lutz–Lutz also prove domination on dyadic cubes is equivalent to domination on balls. Their ball/cube lemma, $|K(B) - K(Q)| \leq K(r) + c$ for a radius-$2^{-r}$ ball $B$ meeting $Q \in \mathcal{D}_r$, is the centered-ball comparison the draft wants in §8.7.
    - **1114**: soften. Suggested text: "We do not know whether, for a fixed competitor $\Lambda$, the set $\bigcap_{k} W_X(\Pi, \Lambda, 1/k)$ of points with $2^{o(r)}$ domination must have full dimension. The good sets decrease as $\varepsilon \downarrow 0$ and Hausdorff dimension is not stable under countable decreasing intersections, so the naive argument fails. In the language of §8, this asks whether (PHE) holds for the $\sigma$ideal generated by $\mathcal{N}^+_\mu$ rather than for $\mathcal{N}^+_\mu$ itself."
    
    ### §8.1
    
    - **1126–1130**: $\mathcal{D}$ is also the name of the competitor Kraft system in §6.2 and in Theorem C. The notes write dyadic cubes as $\mathcal{Q}^m_r$; I'd switch.
    - **1149**: add three facts:
        - $\mathscr{T}_{\mu,\eta}$ is a metric outer measure (Method II). In the notes' notation it is the net measure $\mathcal{H}^{\rho_{\mu,\eta}}$ of the net premeasure (PG).
        - $\mathscr T_{\mu,\eta} \leq \mathscr T_{\mu,\eta'}$ for $\eta \leq \eta'$, so the null ideals shrink as $\eta$ grows. Hence (PHE) for all $\eta > 0$ is equivalent to (PHE) for all sufficiently small $\eta$.
        - $\mathscr T_{\mu,\eta} \geq \mu^*$, so tilted-null sets are $\mu$null.
    - **1154**: fine, but remove any suggestion that atoms are what matters (A.2.4).
    
    ### §8.2
    
    - **1158–1176**: replace the Kraft hypothesis on $a$ with "$a : \mathcal{D} \to [0, \infty)$ arbitrary" (A.1.1).
    - **1179–1180**: broken displays.
    - **1182–1188**: (KC1) already holds with $\eta = \varepsilon$, because the tilted cost of the bad cubes of rank $\geq m$ is at most $\sum_{\operatorname{rk} Q \geq m} b(Q) \to 0$.
    - **1190–1208**: the strictness problem (A.1.1); replace with C.5.
    - **1210–1216**: with C.5 this becomes exact at each fixed $\eta$, so "arbitrarily small changes of the positive exponent" can go.
    
    ### §8.3
    
    - **1235**: define $C^A(Q) := K^A(r, k)$ for $Q = 2^{-r}(k + [0,1)^n)$; the rank must be part of the index. In the notes' notation, the corner of $Q_r(x)$ is $x \upharpoonright r$.
    - **1237–1247**: replace the proof with C.6 (coding theorem, not Shannon–Fano).
    - **1249–1255**: replace with C.6, or cite the notes' Lemma 2.1.4 (Lutz–Stull A.1: $|K_r(x) - K(x \upharpoonright r)| \leq K(r) + c$). Since $C^Z(Q_r(x)) = K^Z(r, 2^r \cdot x \upharpoonright r)$, that lemma gives (18) immediately with error $2K(r) + O(1)$.
    - **1247 and 1404–1411**: state the sum/sup comparison as its own lemma, since it is the crux of the "sum/sup fork": $\boldsymbol{\kappa}^A(Q) \leq \mu_A(Q) \leq 2^{K(r) + c} \boldsymbol{\kappa}^A(Q)$ for $Q \in \mathcal{D}_r$ (C.6). Classically, $\Pi_a(Q)$ and $\mu_a(Q)$ are incomparable; the coding theorem is what collapses the fork for optimal semimeasures. The comparison itself is not new: it is the "LDS coding theorem" of Case–Lutz (*Mutual dimension*, ACM TOCT 7(3), 2015), which Lutz–Lutz use to prove that $\boldsymbol\kappa$ is locally optimal. Cite it rather than presenting it as part of the new work.
    
    ### §8.4
    
    - **1275–1287**: restate as Theorem E′ (C.7): (20) is optional, the $s = 0$ case is trivial, and $\mu$ may be taken absolutely continuous.
    - **1293–1299**: this becomes one sentence: "by C.5 there is a Kraft weight $b$ with $N \subseteq \operatorname{Tgt}_\eta(\mu_A, b)$."
    - **1305**: "$D$" is undefined. Using your §1.3 notation, write "$N \cap N_X(A, B, \eta/2) = \varnothing$." The constant works out because (21) together with C.6 gives $K^{A,B}_r(x) \leq K^A_r(x) - \eta r + K(r) + O(1)$ infinitely often, so preservation fails at rate $\eta/2$.
    - **1311**: delete the $s = 0$ sentences.
    - **1315–1345**: add the provenance note from line 968: (22) is Stull's (ST). Only the "$\leq s$" half of (20) is used; "$\geq s$" is automatic by the Billingsley lemma (C.7).
    - **1347**: no normalization is needed, since $\sum_Q 2^{-C^{A,B}(Q)} \leq 1$ by Kraft.
    
    ### §8.5
    
    - **1371–1393**: (25) simplifies to "$\exists \mu$ finite Borel with $\mathcal{N}^+_\mu \cap \mathcal{P}(X) \subseteq \mathcal{R}_s(X)$." The first line of the box becomes optional.
    - **1385**: true. Worth adding that $\mathcal{N}^+_\mu \cap \mathcal{P}(X)$ is an ideal, so the inclusion is stronger than it looks: finitely many null deletions are jointly harmless.
    - **1397**: Lebesgue measure isn't finite on $\mathbb{R}^n$. Use $\lambda|_{[0,1]^n}$ when $X \subseteq [0,1]^n$, or $e^{-|x|^2}\,dx$ in general (the local exponents are still $n$). Also "$n$dimensional" → "$n$dimensional".
    - **1398**: delete, or reduce it to the $s = 0$ triviality remark.
    - **1400**: this can be strengthened. By Theorem E′ the failure holds for *every* finite measure, not only those satisfying the local-exponent equality.
    
    ### §8.6–8.7
    
    - **1425**: see A.4; replace with a pointer to C.9.
    - **1431–1436**: add that the sufficiency proof is Stull's argument plus the tilt, and that the new ingredient on the necessity side is the pooling step (KC2).
    
    ### §9
    
    - **1464–1466**: the Proposition becomes a corollary of Theorem E with a classical proof (C.8, Proposition 3). Also fix "$\mu$null" → "$\mu$null" (1466, 1471) and "$\mathcal{H}^s$mass" → "$\mathcal{H}^s$mass" (1471).
    - **1497**: "it is still only sufficient as a criterion involving one ordinary null ideal" is accurate. Note that whether the *ambient* untilted version is also necessary is open (Part E.2).
    - **1509**: add that Frostman measures do give a witness for analytic sets (C.8, Proposition 4).
    - **1515**: the notes define "dimension function" in §1.1, Measures and Hausdorff Dimension (non-decreasing, right-continuous, $h(t) = 0 \iff t = 0$). Point there instead of to the dissertation's section number.
    - **1595**: the caveat is justified. In arXiv v2 (the current version), Stull's body proves only the $s$set case (Corollary 14), and his definition of a gauge imposes no regularity. C.9 gives an AC + CH counterexample for irregular gauges, so replace the caveat with C.9's statement.
    - **1605**: broken display.
    - **1609–1615**: replace with C.9's counterexample showing exactness is not necessary.
    
    ### §10
    
    - **1647**: "uses a densely supported atomic measure" is fine, but add that Lebesgue measure witnesses $B$ directly, and that by C.7 the witness can always be taken absolutely continuous.
    - **1657**: verified. Cite Stull's Theorem 41, and Corollary 42 and Theorem 43 for the two separations. Note that his Lemma 18 (the basic CH set in $\mathbb{R}$) prescribes only $\dim_H$; its packing dimension is 1.
    - **1675–1694** (§10.5): Crone–Fishman–Jackson also show, in the example following their AD corollary, that for a Bernstein set *neither* player wins the dimension game. That strengthens your point: the game is undetermined there.
    - **1675, 1793**: Logan Crone.
    
    ### §11
    
    - **1718–1722**: "the same proof" needs the packing analogue of Stull's Proposition 4 for the full-dimensional form. Stull states it as his Proposition 33, but his proof of the backward direction is copied from the Hausdorff case; C.10 gives the corrected argument.
    - **1724–1736**: correct as stated. I checked necessity and sufficiency using C.10's two lemmas. The null ideals correctly stay *Hausdorff-type* (Method II), since the bad sets are limsup sets.
    
    ### §12 to the end
    
    - **1740–1748**: I'd move "The strongest accurate conclusion is…" into the Final assessment, and trim §12 to two sentences or move it to an appendix, since it isn't connected to the proofs.
    - **1750–1776**: C.8 answers Next steps 5 and 6, as oracle-free reproofs of Stull's results. C.9 answers 9: regularity is needed, with an AC + CH counterexample still awaiting a line-by-line check. Step 7 should be reframed (A.4). Add Part E's questions.
    - **1810–1814**: delete the leftover Proposition.
    
    ---
    
    ## Part C. Paste-ready math
    
    ### C.4 The self-clause in (H) and (CH) is free
    
    **Lemma.** Suppose $\Pi \in \mathfrak{P}$ has the following property: for every $\Lambda \in \mathfrak{P}$ and every $\varepsilon > 0$, some $x \in X$ satisfies $\liminf_r L^\Lambda_r(x)/r \geq s - \varepsilon$ and $L^\Lambda_r(x) \geq L^\Pi_r(x) - \varepsilon r$ for all but finitely many $r$. Then $\Pi$ satisfies the full witness form (CH)–(CP).
    
    **Proof.** Given $\Lambda = \Pi_b$ and $\varepsilon$, apply the property to $\Lambda' := \Pi_h$ with $h = \tfrac12 \max\{a, b\}$ and tolerance $\varepsilon/2$. Since $\Lambda' \geq \tfrac12 \Pi$ and $\Lambda' \geq \tfrac12 \Lambda$, we have $L^{\Lambda'}_r \leq \min\{L^\Pi_r, L^\Lambda_r\} + 1$. So the witness $x$ has both lower rates at least $s - \varepsilon/2$. Moreover, eventually
    
    $$
    L^\Lambda_r(x) \geq L^{\Lambda'}_r(x) - 1 \geq L^\Pi_r(x) - (\varepsilon/2) r - 1 \geq L^\Pi_r(x) - \varepsilon r. \qquad \square
    $$
    
    The same argument, with $\varphi \vee \psi$ in place of $\tfrac12 \max\{\Pi, \Lambda\}$, shows that the first inequality in (H) is free.
    
    ### C.5 Kraft–Carathéodory duality, exact form (replaces the lemma and proofs in §8.2)
    
    Let $a : \mathcal{D} \to [0, \infty)$ be *any* function: a net premeasure, with no summability assumed. Fix $\eta \geq 0$ and define $\mathscr{T}_{a,\eta}$ by (PT). For a dyadic Kraft weight $b$, define the **$\eta$-targeted set**
    
    $$
    \operatorname{Tgt}_\eta(a, b) := \left\{ x : b(Q_r(x)) \geq 2^{\eta r} a(Q_r(x)) \text{ for infinitely many } r \right\}.
    $$
    
    **Lemma (KC).** For every $Y \subseteq \mathbb{R}^n$,
    
    $$
    \mathscr{T}_{a,\eta}(Y) = 0 \iff Y \subseteq \operatorname{Tgt}_\eta(a, b) \text{ for some dyadic Kraft weight } b.
    $$
    
    In the forward direction, $b$ can be taken strictly positive.
    
    **Proof of $\Leftarrow$.** For each $m$, the cubes $\left\{ Q : \operatorname{rk} Q \geq m,\ b(Q) \geq 2^{\eta \operatorname{rk} Q} a(Q) \right\}$ cover $\operatorname{Tgt}_\eta(a, b) \supseteq Y$. Their tilted cost is at most $\sum_{\operatorname{rk} Q \geq m} b(Q)$, which is the tail of a convergent series.
    
    **Proof of $\Rightarrow$.** For each $j \geq 0$, choose a cover $\mathcal{C}_j$ of $Y$ by cubes of rank $\geq j$ with $\sum_{Q \in \mathcal{C}_j} 2^{\eta \operatorname{rk} Q} a(Q) \leq 2^{-j-2}$. Enumerate $\mathcal{D} = \{ Q^{(0)}, Q^{(1)}, \ldots \}$ and put
    
    $$
    b(Q^{(i)}) := 2^{-i-2} + \sum_{\{ j : Q^{(i)} \in \mathcal{C}_j \}} 2^{\eta \operatorname{rk} Q^{(i)}} a(Q^{(i)}).
    $$
    
    Then $b > 0$ and $\sum b \leq \tfrac12 + \tfrac12 = 1$. Let $x \in Y$. Half-open cubes of a fixed rank partition $\mathbb{R}^n$, so for each $j$ the member of $\mathcal{C}_j$ containing $x$ is $Q_{r_j}(x)$ for some $r_j \geq j$, and $b(Q_{r_j}(x)) \geq 2^{\eta r_j} a(Q_{r_j}(x))$. Since $r_j \to \infty$, this happens at infinitely many ranks. $\square$
    
    **Consequences.**
    
    - Since $\operatorname{Bad}_\varepsilon(a, b) \subseteq \operatorname{Tgt}_\varepsilon(a, b)$, we get $\mathscr{T}_{a,\varepsilon}(\operatorname{Bad}_\varepsilon(a, b)) = 0$, with no slack in the exponent.
    - Write $\mathcal{N}_\eta(a)$ for the family of $\mathscr T_{a,\eta}$null sets. Then $\mathcal{N}_\eta(a)$ is *exactly* the family of subsets of $\eta$targeted sets. In the oracle translation, strict versus non-strict inequality costs one bit.
    - If $\eta \leq \eta'$, then $\mathcal{N}_{\eta'}(a) \subseteq \mathcal{N}_\eta(a)$.
    - **Comparability.** Suppose $2^{-g(r)} a(Q) \leq a'(Q) \leq 2^{g(r)} a(Q)$ on $\mathcal{D}_r$ with $g(r) = o(r)$. Then $\mathcal{N}_{\eta + \delta}(a) \subseteq \mathcal{N}_\eta(a') \subseteq \mathcal{N}_{\eta - \delta}(a)$ for every $0 < \delta < \eta$. In particular, $\mathcal{N}^+$ depends on $a$ only up to $2^{o(r)}$ factors.
    
    ### C.6 Cube/point and sum/sup comparisons (replaces the proofs of (17)–(18))
    
    Identify each $Q = 2^{-r}(k + [0,1)^n) \in \mathcal{D}_r$ with $(r, k) \in \mathbb{N} \times \mathbb{Z}^n$, and put $C^Z(Q) := K^Z(r, k)$. The corner of $Q_r(x)$ is $x \upharpoonright r$.
    
    **Lemma (cube/point).** There is $c = c_n$ such that for every oracle $Z$, point $x$, and $r$,
    
    $$
    K^Z_r(x) - c \leq C^Z(Q_r(x)) \leq K^Z_r(x) + K(r) + c.
    $$
    
    **Proof.** *Left inequality.* Let $c_n \geq 0$ be least with $2^{c_n} > \sqrt{n}/2$, so $c_n = 0$ for $n \leq 3$. Take a program for $(r, k)$ and append $n c_n$ bits naming the subcube $Q_{r + c_n}(x) \subseteq Q_r(x)$. This program outputs the subcube's center, which lies within $\tfrac{\sqrt n}{2} 2^{-r - c_n} < 2^{-r}$ of $x$.
    
    *Right inequality.* Let $q \in \mathbb{Q}^n$ with $|q - x| < 2^{-r}$. On each axis, $(q_i - 2^{-r}, q_i + 2^{-r})$ meets at most three half-open dyadic intervals of length $2^{-r}$. So $Q_r(x)$ is one of at most $3^n$ cubes computable from $(q, r)$. A self-delimiting program for $r$, one for $q$, and a $\lceil n \log_2 3 \rceil$-bit index give $C^Z(Q_r(x)) \leq K^Z(q) + K(r) + O(1)$. Minimize over $q$. $\square$
    
    **Lemma (sum/sup on a dyadic layer).** Let $\mu_A$ be as in (16) and $\boldsymbol\kappa^A = \Pi_{a_A}$. There is $c$ such that for every $A$ and every $Q \in \mathcal{D}_r$,
    
    $$
    2^{-C^A(Q) - c} \leq \boldsymbol{\kappa}^A(Q) \leq \mu_A(Q) \leq 2^{K(r) + c} \cdot 2^{-C^A(Q)}.
    $$
    
    **Proof.** *First inequality.* The corner $2^{-r}k \in Q$ is computable from $(r, k)$, so $K^A(2^{-r}k) \leq C^A(Q) + c$.
    
    *Second inequality.* A maximum is at most a sum.
    
    *Third inequality.* The function $\nu(r, k) := 2^{-K(r)} \mu_A(Q_{r,k})$ is lower semicomputable relative to $A$: enumerate $A$-programs whose outputs lie in the decidable set $Q_{r,k}$, and approximate $K(r)$ from above. Also $\sum_{r,k} \nu(r,k) \leq \sum_r 2^{-K(r)} \leq 1$. The relativized coding theorem gives $K^A(r, k) \leq -\log_2 \nu(r, k) + c$, that is, $C^A(Q) \leq -\log_2 \mu_A(Q) + K(r) + c$. All constants are uniform in $A$. $\square$
    
    **Corollary.** For all $A, x, r$,
    
    $$
    \bigl| L^{\mu_A}_r(x) - K^A_r(x) \bigr| \leq K(r) + c', \qquad \bigl| -\log_2 \boldsymbol\kappa^A(Q_r(x)) - K^A_r(x) \bigr| \leq K(r) + c'.
    $$
    
    In words: on each dyadic layer, the additive and maxitive prefix measures agree within a factor $2^{K(r) + O(1)}$. For an arbitrary $a$, the quantities $\Pi_a(Q)$ and $\mu_a(Q)$ are incomparable; the coding theorem is exactly what collapses the sum/sup fork for optimal semimeasures.
    
    **Provenance.** The third inequality is the Case–Lutz LDS coding theorem (A. Case and J. H. Lutz, *Mutual dimension*, ACM TOCT 7(3), 2015). Lutz–Lutz state it as $K(Q) \leq \log_2(1/\mathbf{m}(Q)) + K(r) + c$, where $K(Q)$ is the complexity of the set $Q$, and use it to prove that $\boldsymbol\kappa$ is locally optimal.
    
    ### C.7 Measure point-to-set principle, upward closure, and the simplified Theorem E
    
    **Lemma (dyadic Billingsley bound).** For every finite Borel measure $\mu$ and every $X \subseteq \mathbb{R}^n$,
    
    $$
    \sup_{x \in X} \operatorname{capdim}^{\mathcal{D}}_\mu(x) \geq \dim_H X.
    $$
    
    **Proof.** Let $t$ exceed the left side and fix $m$. Let $\mathcal{F}_m$ be the set of maximal cubes among $\left\{ Q : \operatorname{rk} Q \geq m,\ Q \cap X \neq \varnothing,\ \mu(Q) > 2^{-t \operatorname{rk} Q} \right\}$. Every $x \in X$ lies in such a cube, namely $Q_r(x)$ for some $r \geq m$, and hence in a maximal one. Maximal dyadic cubes are pairwise disjoint. So
    
    $$
    \mathcal{H}^t_{\sqrt{n}\,2^{-m}}(X) \leq \sum_{Q \in \mathcal{F}_m} (\operatorname{diam} Q)^t = n^{t/2} \sum_{Q \in \mathcal{F}_m} 2^{-t \operatorname{rk} Q} < n^{t/2} \sum_{Q \in \mathcal{F}_m} \mu(Q) \leq n^{t/2} \mu(\mathbb{R}^n).
    $$
    
    Hence $\mathcal{H}^t(X) < \infty$ and $\dim_H X \leq t$. $\square$
    
    **Lemma (dimension-minimizing measures exist).** For every $X$ there is a finite, purely atomic Borel measure $\mu_X$ with $\sup_{x \in X} \operatorname{capdim}^{\mathcal{D}}_{\mu_X}(x) \leq \dim_H X$. Together with the previous lemma, this gives a "measure point-to-set principle":
    
    $$
    \dim_H X = \min_{\mu} \sup_{x \in X} \operatorname{capdim}^{\mathcal{D}}_\mu(x),
    $$
    
    with the minimum over finite Borel measures.
    
    **Provenance.** This is Cutler's *weak duality principle* (C. D. Cutler, *Strong and weak duality principles for fractal dimension in Euclidean space*, Math. Proc. Cambridge Philos. Soc. 118 (1995), 393–410). Cutler states it with centered balls, an infimum, and probability measures on $\overline{X}$; the version here uses dyadic cubes and shows the minimum is attained. Lutz–Lutz (*Algorithmically optimal outer measures*, last section) already present the point-to-set principle as the effective counterpart of Cutler's principle. Their remark that the family $\{\boldsymbol\kappa^A\}$ does not depend on the set, whereas Cutler's measures live on $\overline{E}$, matches Theorem E exactly: the necessity witness $\mu_A$ is built from an oracle, while the classical witnesses (Frostman measures, Lebesgue measure) are built from $X$.
    
    **Proof.** The argument is the attainment half of C.2, carried out with dyadic cubes. Let $s := \dim_H X$ and $t_m := s + 1/m$. A set of diameter $d \in (2^{-r-1}, 2^{-r}]$ meets at most $2^n$ cubes of rank $r$, and each has $2^{-tr} < (2d)^t$. Since $\mathcal{H}^{t_m}(X) = 0$, we can therefore cover $X$ by cubes $Q_{m,j}$ of ranks $r_{m,j} \geq m^2$ with $\sum_j 2^{-t_m r_{m,j}} \leq 1$. Place an atom of mass $2^{-m} 2^{-t_m r_{m,j}}$ at a point of each $Q_{m,j}$. For $x \in X$ and each $m$, we have $x \in Q_{m,j} = Q_r(x)$ for some $j$, with $r = r_{m,j} \geq m^2$. So $L^{\mu_X}_r(x)/r \leq t_m + m/r \leq t_m + 1/m$. $\square$
    
    **Proposition (upward closure).** Suppose $\mu$ satisfies (PHE) on $X$, and $\mu'$ is a finite Borel measure with $\mu'(Q) \geq 2^{-o(\operatorname{rk} Q)} \mu(Q)$ for all $Q \in \mathcal{D}$ (for instance, $\mu' \geq \mu$). Then $\mu'$ satisfies (PHE) on $X$.
    
    **Proof.** By comparability (C.5), $\mathcal{N}_\eta(\mu') \subseteq \mathcal{N}_{\eta - \delta}(\mu)$ for each $0 < \delta < \eta$. So a $\mathscr T_{\mu',\eta}$-null $N \subseteq X$ is $\mathscr T_{\mu,\eta-\delta}$-null, and therefore harmless. $\square$
    
    Both conditions in Theorem E are *largeness* conditions on $\mu$. Bigger measures have fewer tilted-null sets, and the nontrivial half of (20), "$\leq s$," is also a lower bound on $\mu$. The only constraint in the other direction is finiteness.
    
    **Theorem E′.** Let $X \subseteq \mathbb{R}^n$ with $s = \dim_H X > 0$. The following are equivalent.
    
    **(i)** $X$ has an optimal Hausdorff oracle.
    
    **(ii)** There is a finite Borel measure $\mu$ such that, for every $\eta > 0$ and every $N \subseteq X$, $\mathscr{T}_{\mu,\eta}(N) = 0$ implies $\dim_H(X \setminus N) = s$.
    
    **(iii)** There is such a $\mu$ that also satisfies $\sup_{x \in X} \operatorname{capdim}^{\mathcal{D}}_\mu(x) = s$.
    
    **(iv)** There is such a $\mu$ as in (iii) that is absolutely continuous with respect to Lebesgue measure.
    
    **Proof.**
    
    (i) ⇒ (iii) is the draft's necessity proof, with C.5 and C.6 in place. (iii) ⇒ (i) is the draft's sufficiency proof. The implications (iv) ⇒ (iii) ⇒ (ii) are trivial.
    
    (ii) ⇒ (iii): replace $\mu$ by $\mu + \mu_X$. (PHE) survives by upward closure. The "$\leq s$" half of (20) holds because $\mu + \mu_X \geq \mu_X$, and the "$\geq s$" half is the Billingsley bound.
    
    (iii) ⇒ (iv): smear $\mu$ over cubes,
    
    $$
    \mu' := \sum_{Q \in \mathcal{D}} \pi_{\operatorname{rk} Q}\, \mu(Q)\, \lambda_Q, \qquad \lambda_Q := \frac{\lambda|_Q}{\lambda(Q)}.
    $$
    
    Then $\mu'(\mathbb{R}^n) \leq \mu(\mathbb{R}^n)$, $\mu' \ll \lambda$ with an $L^1$ density, and $\mu'(Q) \geq \pi_{\operatorname{rk} Q}\,\mu(Q)$. So (PHE) transfers by upward closure, and $\operatorname{capdim}^{\mathcal{D}}_{\mu'} \leq \operatorname{capdim}^{\mathcal{D}}_\mu$ pointwise. $\square$
    
    **Remark ($s = 0$).** Suppose $\dim_H X = 0$ and $x_0 \in X$. For any Hausdorff oracle $A_0$, the oracle $A := A_0 \oplus x_0$ is optimal. Indeed, $K^A_r(x_0) \leq K(r) + O(1)$, so eventually $K^{A,B}_r(x_0) \geq 0 \geq K^A_r(x_0) - \varepsilon r$, and the clause $\dim^{A,B}(x_0) \geq -\varepsilon$ is vacuous. On the measure side, $\delta_{x_0} + \mu_X$ works, since $\mathscr T_{\delta_{x_0},\eta}(\{x_0\}) = \infty$.
    
    **Remark (the same redundancy upstream).** Stull's [WITNESS] clause is redundant as an existence condition. If $A$ satisfies [FITNESS] and $A_0$ is a Hausdorff oracle, then $A \oplus A_0$ is optimal: apply [FITNESS] for $A$ to the competitor $A_0 \oplus B$, and use $K^{A}_r \geq K^{A, A_0}_r - O(1)$. Likewise, (M) is redundant in Theorems A–C (replace $\varphi$ by $\varphi \vee \varphi_0$), and attainment is redundant in Theorem D (replace $\Pi$ by $\tfrac12\max\{\Pi, \Pi_0\}$).
    
    ### C.8 Theorem E as a working GMT tool
    
    Throughout this section, $s = \dim_H X > 0$, and "$\mu$ witnesses $X$" means that $\mu$ satisfies (ii) of Theorem E′. Two facts are used repeatedly. First, each cover's tilted cost dominates its untilted cost, so
    
    $$
    \mathscr{T}_{\mu,\eta}(N) \geq \mu^*(N).
    $$
    
    Second, the mass distribution principle holds for outer measures: if $\nu(B(x, \rho)) \leq C \rho^t$ for all balls, then $\mathcal{H}^t(E) \geq C^{-1} \nu^*(E)$ for *every* $E$. (Replace each cover element by a closed ball of radius equal to its diameter.) The sharper pointwise form is part (i) of the Rogers–Taylor–Tricot density theorem, which Crone–Fishman–Jackson state for outer measures as their Theorem 1.
    
    **Proposition 1 (countable unions).** Let $X = \bigcup_{i \geq 1} X_i$. For each $i$ with $\dim_H X_i > 0$, suppose $\mu_i$ witnesses $X_i$ and $\mu_i(\mathbb{R}^n) \leq 1$. Then $\mu := \sum_i 2^{-i} \mu_i$ witnesses $X$.
    
    **Proof.** Let $N \subseteq X$ be $\mathscr T_{\mu,\eta}$-null. Since $\mu \geq 2^{-i} \mu_i$, the set $N \cap X_i$ is $\mathscr T_{\mu_i,\eta}$-null, so $\dim_H(X_i \setminus N) = \dim_H X_i$. Hence $\dim_H(X \setminus N) \geq \sup_i \dim_H X_i = s$. $\square$
    
    **Proposition 2 (full-dimensional subsets and supersets).** Let $Y \subseteq X$.
    
    - If $\dim_H Y = s$ and $\mu$ witnesses $Y$, then $\mu$ witnesses $X$.
    - If $\dim_H(X \setminus Y) < s$ and $\mu$ witnesses $X$, then $\mu$ witnesses $Y$.
    
    **Proof.** For the first claim, let $N \subseteq X$ be null. Then $N \cap Y$ is null, so $\dim_H(X \setminus N) \geq \dim_H(Y \setminus N) = s$. For the second, let $N \subseteq Y$ be null. Then $\dim_H(X \setminus N) = s$, and $X \setminus N = (Y \setminus N) \cup (X \setminus Y)$, where the second piece has dimension $< s$. $\square$
    
    Propositions 1 and 2 are classical counterparts of Stull's Proposition 7 (countable unions) and Observation 6 (full-dimensional supersets), which he proves with oracles.
    
    **Proposition 3 (Stull's measure criterion; §9.1 becomes a corollary).** Let $\mu$ be a metric outer measure with $0 < \mu(X) < \infty$ such that every $\mu$-null $N \subseteq X$ has $\dim_H(X \setminus N) = s$. Then $\nu(E) := \mu(E \cap X)$, for Borel $E$, witnesses $X$. In particular, each of Stull's two absolute-continuity hypotheses gives a witness, and so does an exact gauge satisfying (CMP).
    
    **Proof.** Borel sets are $\mu$-measurable, so $\nu$ is a finite Borel measure. Let $N \subseteq X$ be $\mathscr T_{\nu,\eta}$-null. Then $\nu^*(N) = 0$, so for every $\epsilon > 0$ there is a Borel $E \supseteq N$ with $\mu(N) \leq \mu(E \cap X) = \nu(E) < \epsilon$. Hence $\mu(N) = 0$, and $\dim_H(X \setminus N) = s$. $\square$
    
    **Proposition 4 (analytic sets).** Every analytic $X$ has a witness.
    
    **Proof.** Take $t_k \uparrow s$. The Besicovitch–Davies theorem (R. O. Davies, *Subsets of finite measure in analytic sets*, Indag. Math. 14 (1952), 488–489) gives compact sets $K_k \subseteq X$ with $0 < \mathcal{H}^{t_k}(K_k) < \infty$, and Frostman's lemma gives probability measures $\nu_k$ on $K_k$ with $\nu_k(B(x, \rho)) \leq C_k \rho^{t_k}$. Put $\mu := \sum_k 2^{-k} \nu_k$. Let $N \subseteq X$ be $\mathscr T_{\mu,\eta}$-null. Then $\nu_k^*(N) = 0$, so $\nu_k^*(K_k \setminus N) \geq \nu_k(K_k) - \nu_k^*(N) = 1$. The mass distribution principle gives $\mathcal{H}^{t_k}(K_k \setminus N) > 0$, so $\dim_H(X \setminus N) \geq t_k$ for every $k$. $\square$
    
    Propositions 3 and 4 use only $\mathscr T_{\mu,\eta} \geq \mu^*$, so they would still work with $\eta = 0$. The next result is where the tilt matters.
    
    **Lemma (tilted-null sets are small).** Let $\mu$ be a finite Borel measure, $\eta > 0$, $t \geq 0$, and $N \subseteq \mathbb{R}^n$ with
    
    $$
    \limsup_{r \to \infty} \frac{L^\mu_r(x)}{r} \leq t \qquad (x \in N).
    $$
    
    If $\mathscr{T}_{\mu,\eta}(N) = 0$, then $\dim_H N \leq t - \eta$. (In particular $N = \varnothing$ if $t < \eta$.)
    
    **Proof.** Fix $0 < \delta < \eta$ and let $N_j := \left\{ x \in N : \mu(Q_r(x)) \geq 2^{-(t+\delta) r} \text{ for all } r \geq j \right\}$, so that $N = \bigcup_j N_j$. Given $\epsilon > 0$ and $m \geq j$, take a cover of $N_j$ by cubes $Q_i$ of rank $r_i \geq m$ with tilted cost $< \epsilon$, and discard the cubes that miss $N_j$. Each remaining $Q_i$ equals $Q_{r_i}(x)$ for some $x \in N_j$, so $\mu(Q_i) \geq 2^{-(t+\delta) r_i}$ and
    
    $$
    \sum_i 2^{-(t + \delta - \eta) r_i} \leq \sum_i 2^{\eta r_i} \mu(Q_i) < \epsilon.
    $$
    
    So $\mathcal{H}^{t + \delta - \eta}(N_j) = 0$. If the exponent is negative, each term is $\geq 1$, so the cover must be empty. By countable stability, $\dim_H N \leq t + \delta - \eta$. Now let $\delta \to 0$. $\square$
    
    **Lemma (packing measure point-to-set principle).**
    
    **(a)** For every $X$ there is a finite Borel measure $\mu$ with $\limsup_r L^\mu_r(x)/r \leq \dim_P X$ for every $x \in X$.
    
    **(b)** For every finite Borel measure $\mu$, $\sup_{x \in X} \limsup_r L^\mu_r(x)/r \geq \dim_P X$.
    
    **Proof.** Let $S := \dim_P X$.
    
    (a) For each $k$, cover $X$ by bounded sets $X_{k,i}$ with $\overline{\dim}_B X_{k,i} < S + 1/k$. Then the number $N_r(X_{k,i})$ of rank-$r$ cubes meeting $X_{k,i}$ is at most $C_{k,i} 2^{(S + 1/k) r}$. Let $\nu_{k,i}$ place mass $\pi_r / N_r(X_{k,i})$ at a point of each rank-$r$ cube meeting $X_{k,i}$, for every $r$, and put $\mu := \sum_{k,i} 2^{-k-i-1} \nu_{k,i}$. For $x \in X_{k,i}$ and *every* $r$, we get $\mu(Q_r(x)) \geq 2^{-k-i-1} \pi_r C_{k,i}^{-1} 2^{-(S + 1/k) r}$.
    
    (b) Let $t$ exceed the left side and $\delta > 0$, and let $X_j$ be the set of $x \in X$ with $\mu(Q_r(x)) \geq 2^{-(t+\delta) r}$ for all $r \geq j$, so $X = \bigcup_j X_j$. For $r \geq j$, distinct rank-$r$ cubes meeting $X_j$ are disjoint, so there are at most $\mu(\mathbb{R}^n) 2^{(t + \delta) r}$ of them. Hence every bounded piece of $X_j$ has $\overline{\dim}_B \leq t + \delta$, and $S \leq t + \delta$. $\square$
    
    **Proposition 5 (weakly regular sets).** If $\dim_H X = \dim_P X = s$, then any $\mu$ from part (a) of the packing lemma witnesses $X$ and satisfies (20).
    
    **Proof.** Let $N \subseteq X$ be $\mathscr T_{\mu,\eta}$-null. The tilted-null lemma with $t = s$ gives $\dim_H N \leq s - \eta < s$, so $\dim_H(X \setminus N) = s$. Also $\liminf \leq \limsup \leq s$, which gives (20). $\square$
    
    So for a weakly regular set, every null deletion at tilt $\eta$ removes a set of dimension at most $s - \eta$. With $\eta = 0$, the argument would give nothing here. This is the classical shadow of Stull's Lemma 17, where a packing oracle $B$ gives $K^{A,B}_r(x) \leq (s + \varepsilon) r$ at *all* large $r$. That is exactly the bound on upper local dimension used in the tilted-null lemma.
    
    **Example (a full-dimensional Bernstein set $B \subseteq [0,1]$).** $\lambda|_{[0,1]}$ is a witness: $\mathscr T_{\lambda,\eta}$ is comparable to dyadic $\mathcal{H}^{1-\eta}$, so its null sets have dimension at most $1 - \eta$. Even the untilted version works, since $\lambda^*(B) = 1$.
    
    ### C.9 Exact gauges (for §9.3)
    
    **Lemma.** Let $K$ be compact and Ahlfors $t$-regular, and let $h$ be a dimension function with $\mathcal{H}^h(K) > 0$. Then $\liminf_{\rho \to 0} h(\rho)/\rho^t > 0$.
    
    **Proof.** $K$ is covered by $C \rho^{-t}$ balls of radius $\rho$, so $\mathcal{H}^h_{2\rho}(K) \leq C \rho^{-t} h(2\rho)$. If $h(\rho_i)/\rho_i^t \to 0$ along some sequence $\rho_i \to 0$, then $\mathcal{H}^h(K) = \lim_i \mathcal{H}^h_{2\rho_i}(K) = 0$. $\square$
    
    **Proposition (exact gauges are not necessary).** Let $s \in (0, 1]$, let $s_k \uparrow s$ with $s_k < s$, and let $K_k \subseteq [0,1]$ be an Ahlfors $s_k$-regular Cantor set. Put
    
    $$
    X := \{0\} \cup \bigcup_{k \geq 1} \left( 2^{-2k} + 2^{-2k-2} K_k \right).
    $$
    
    Then $X$ is compact, so it has optimal Hausdorff and packing oracles. But no dimension function $h$ has $0 < \mathcal{H}^h(X) < \infty$.
    
    **Proof.** Suppose $0 < \mathcal{H}^h(X) < \infty$. Since $\mathcal{H}^h(\{0\}) = 0$, some scaled copy of $K_k$ has positive $\mathcal{H}^h$-measure. By the lemma, $h(\rho) \geq c \rho^{s_k}$ for $\rho < \rho_0$, so $\mathcal{H}^h \geq c\, \mathcal{H}^{s_k}$. The copy of $K_{k+1}$ has dimension $s_{k+1} > s_k$, so its $\mathcal{H}^{s_k}$-measure is infinite, and therefore $\mathcal{H}^h(X) = \infty$, a contradiction. $\square$
    
    So the answer to "Does radial exactness characterize optimal oracles?" is no, since exactness isn't stable under countable unions of increasing dimension, while optimality is.
    
    **Proposition (irregular exact gauges are not sufficient; $\mathsf{AC} + \mathsf{CH}$).** Fix rationals $0 < u < s < w < v < 1$. There is a set $X \subseteq [0,1]$ with $\dim_H X = s$, and a continuous, strictly increasing, doubling dimension function $h$ with $0 < \mathcal{H}^h(X) < \infty$, such that $X$ has no optimal Hausdorff oracle. Here $\underline\alpha(h) = u < s$ and $\overline\alpha(h) = v$.
    
    **The gauge.** Choose block endpoints $M_0 < M_1 < \cdots$ with $M_{i+1}/M_i \to \infty$. Let $\sigma(j) = v$ for $j \in [M_{2i}, M_{2i+1})$ and $\sigma(j) = u$ for $j \in [M_{2i+1}, M_{2i+2})$, and put $g(0) = 0$, $g(j+1) = g(j) + \sigma(j)$. Let $h(2^{-j}) := 2^{-g(j)}$, interpolated log-linearly, with $h(0) = 0$. Then:
    
    - $h$ is continuous, strictly increasing, and doubling: $h(2t) \leq 2^v h(t)$;
    - $g(j)/j \to v$ along $j = M_{2i+1}$ and $g(j)/j \to u$ along $j = M_{2i+2}$.
    
    **Two digit-restricted sets.** For $S \subseteq \{1, 2, \ldots\}$, let $C(S)$ be the compact set of $x \in [0,1]$ with a binary expansion satisfying $x_j = 0$ for all $j \notin S$. Put
    
    - $Y := C(S_Y)$ with $|S_Y \cap [1, j]| = \lfloor g(j) \rfloor$, which is possible because $g$ increases by at most 1 per step;
    - $Z := C(S_Z)$ with $|S_Z \cap [1, j]| = \lfloor w j \rfloor$.
    
    These have the properties we need:
    
    - **$0 < \mathcal{H}^h(Y) < \infty$.** The $2^{\lfloor g(j) \rfloor}$ level-$j$ intervals cover $Y$, so $\mathcal{H}^h(Y) \leq 1$. The uniform measure $\nu_Y$ gives each level-$j$ interval mass $2^{-\lfloor g(j) \rfloor}$. A set $U$ with $\operatorname{diam} U \in (2^{-j-1}, 2^{-j}]$ meets at most two level-$j$ intervals, so $\nu_Y(U) \leq 4 h(2^{-j}) \leq 2^{v+2} h(\operatorname{diam} U)$, and the mass distribution principle gives $\mathcal{H}^h(Y) > 0$.
    - **$\dim_H Y = u$**, since $\dim_H Y = \liminf_j \lfloor g(j) \rfloor / j$.
    - **$Z$ is Ahlfors $w$regular and $\mathcal{H}^h(Z) = 0$.** Along $j = M_{2i+1}$, where $g(j) \approx vj$, we get $\mathcal{H}^h(Z) \leq \liminf_j 2^{\lfloor wj \rfloor - g(j)} = 0$.
    
    **Stull's construction inside $Z$.** Run the proof of Stull's Lemma 18 with two changes:
    
    - replace "a real random relative to the given countable oracle" by "a point of $Z$ whose free digits (those indexed by $S_Z$) are Martin-Löf random relative to that oracle";
    - choose the block sequences $a_n, b_n$ for the ratio $s' := s/w \in (0,1)$ in place of $s$.
    
    The block-copying step keeps every $y_\alpha$ in $Z$, because membership in $Z$ is a digit-by-digit condition. Every complexity estimate in Stull's proof scales by $w$. For $z \in Z$ with free-digit sequence $\zeta$, the notes' Lemma 2.1.4 gives
    
    $$
    K^C_r(z) = K^C(\zeta \upharpoonright |S_Z \cap [1, r]|) \pm O(\log r).
    $$
    
    The result is a set $N \subseteq Z$ with $\dim_H N = w s' = s$ and no optimal Hausdorff oracle. Against $A_\alpha$, the competitor $B = x_\alpha \oplus \{ y_\beta : \beta < \alpha \}$ saves about $w (1 - s') b_n$ bits at infinitely many scales $b_n$ on every $y_\beta$ with $\beta > \alpha$, and makes $\dim^{A_\alpha, B}(y_\beta) = 0$ for $\beta \leq \alpha$.
    
    One step in Stull's proof is implicit, and it carries over unchanged. To lower-bound $K^{A_\alpha}_{b_n, a_n}(y_\beta)$, one needs $x_\alpha$'s block to stay incompressible given the finitely many other $x_\gamma$ that appear in $y_\beta \upharpoonright a_n$. That follows from van Lambalgen's theorem, since each $x_\gamma$ was chosen random relative to all earlier ones.
    
    **Assembling.** Place $Y$ and $N$ in the two halves of $[0,1]$ by fixing the first binary digit, and let $X$ be their union. Then
    
    $$
    0 < \mathcal{H}^h(Y) \leq \mathcal{H}^h(X) \leq \mathcal{H}^h(Y) + \mathcal{H}^h(Z) = \mathcal{H}^h(Y) < \infty,
    $$
    
    so $h$ is an exact gauge for $X$, and $\dim_H X = \max\{u, s\} = s$.
    
    Suppose $A$ were an optimal Hausdorff oracle for $X$. By Stull's Proposition 4, every $N_X(A, B, \varepsilon)$ would have dimension $s$. Removing the copy of $Y$, which has dimension $u < s$, leaves the corresponding preservation set for $N$, still of dimension $s$. Since $A$ is also a Hausdorff oracle for $N$, Proposition 4 then makes $A$ optimal for $N$, a contradiction. $\square$
    
    So the implication announced in the abstract and introduction of Stull's arXiv v2, "exact gauge ⇒ optimal Hausdorff oracle", fails under $\mathsf{AC} + \mathsf{CH}$ for gauges with $\underline\alpha(h) < \dim_H X$. His Theorem 13 does give it when $\underline\alpha(h) = \dim_H X$, which is exactly (CMP) (combine (CMP) with (ORD)).
    
    ### C.10 Packing (for §11)
    
    **Lemma (packing analogue of Stull's Proposition 4).** Let $S := \dim_P X > 0$ and let $A$ be a packing oracle for $X$. Then $A$ is an optimal packing oracle iff $\dim_P N_X(A, B, \varepsilon) = S$ for every $B$ and every $\varepsilon > 0$.
    
    Stull states this as his Proposition 33. His proof of the backward direction is copied from the Hausdorff case (it uses $\dim_H$ and $\dim^{A,B}$), so here is the corrected argument.
    
    **Proof.** ($\Leftarrow$) Apply the packing point-to-set principle to $N_X(A, B, \varepsilon)$ relative to $A \oplus B$. This gives a point $x$ in it with $\operatorname{Dim}^{A,B}(x) \geq S - \varepsilon$.
    
    ($\Rightarrow$) Suppose $d := \dim_P G < S$ for $G := N_X(A, B, \varepsilon)$. Let $C$ be a packing oracle for $G$, choose $0 < \delta < \min\{\varepsilon, S - d\}$, and apply optimality against $B \oplus C$ with tolerance $\delta$. This gives $x$ with $\operatorname{Dim}^{A,B,C}(x) \geq S - \delta$ and $K^{A,B,C}_r(x) \geq K^A_r(x) - \delta r$ for all but finitely many $r$. If $x \in G$, then $\operatorname{Dim}^{A,B,C}(x) \leq \operatorname{Dim}^C(x) \leq d < S - \delta$. If $x \notin G$, then $K^{A,B,C}_r(x) \leq K^{A,B}_r(x) + O(1) < K^A_r(x) - \varepsilon r + O(1)$ for infinitely many $r$. Either way we have a contradiction. $\square$
    
    C.6 also gives $\limsup_r L^{\mu_A}_r(x)/r = \operatorname{Dim}^A(x)$. With that, this lemma, and the packing lemma from C.8, the Hausdorff proof of Theorem E carries over verbatim to the packing statement in §11. The simplifications in Theorem E′ also carry over.
    
    ### C.11 An oracle-free proof of Theorem C ⟺ Theorem E (new appendix)
    
    **Notation.** For a Kraft ball system $\mathcal{C}$, $M^{\mathcal{C}}_r(x)$ is as in §6.2. For a dyadic Kraft weight $b$, put $M^b_r(x) := \sup_{k \geq r} b(Q_k(x))$, which is (DT).
    
    Let $c = c_n$ be least with $2^c > \sqrt{n}$. Then every $Q \in \mathcal{D}_k$ lies in a rational closed ball $\widehat{B}_Q$, centered at the center of $Q$, with $\operatorname{diam} \widehat{B}_Q \leq 2^{c - k}$. Let $N_n := (2^c + 1)^n$. For a ball $B$ with $\operatorname{diam} B \leq 1$, put $k(B) := \max\{ k : \operatorname{diam} B \leq 2^{-k} \}$.
    
    **Lemma (transfers).**
    
    **(T1) Ball system to measure.** For every Kraft ball system $\mathcal{C}$ there is a Borel measure $\mu_{\mathcal{C}}$ with $\mu_{\mathcal{C}}(\mathbb{R}^n) \leq 1$ and $\mu_{\mathcal{C}}(Q_r(x)) \geq 2^{-n} M^{\mathcal{C}}_r(x)$.
    
    **(T2) Measure to ball system.** For every Borel measure $\mu$ with $\mu(\mathbb{R}^n) \leq 1$ there is a Kraft ball system $\mathcal{C}_\mu$ with $M^{\mathcal{C}_\mu}_r(x) \geq \tfrac12 \pi_{r+c}\, \mu(Q_{r+c}(x))$.
    
    **(T3) Competitor ball system to dyadic weight.** For every Kraft ball system $\mathcal{E}$ there is a dyadic Kraft weight $b_{\mathcal{E}}$ with $M^{\mathcal{E}}_r(x) \leq N_n M^{b_{\mathcal{E}}}_{r+c}(x)$.
    
    **(T4) Dyadic weight to competitor ball system.** For every dyadic Kraft weight $b$ there is a Kraft ball system $\mathcal{E}_b$ with $M^{\mathcal{E}_b}_r(x) \geq 2^{-nc-1} b(Q_r(x))$.
    
    **Proof.**
    
    (T1) A ball $B$ with diameter $\leq 2^{-k(B)}$ meets at most $2^n$ cubes of rank $k(B)$. Spread its weight $w$ equally over atoms placed in those cubes. If $x \in B$ and $\operatorname{diam} B \leq 2^{-r}$, then $k(B) \geq r$, and the cube $Q_{k(B)}(x) \subseteq Q_r(x)$ received mass at least $2^{-n} w$.
    
    (T2) Give $\widehat{B}_Q$ the length $\lceil -\log_2(\pi_{\operatorname{rk} Q}\, \mu(Q)) \rceil$. Kraft's inequality holds because $\sum_k \pi_k \leq 1$. Then $x \in Q_{r+c}(x) \subseteq \widehat{B}_{Q_{r+c}(x)}$, and this ball has diameter at most $2^{-r}$.
    
    (T3) Spread the weight $v$ of each $B \in \mathcal{E}$ equally over the at most $N_n$ cubes of rank $k(B) + c$ that meet $B$. If $x \in B$ with $\operatorname{diam} B \leq 2^{-r}$, then $k(B) + c \geq r + c$, and $Q_{k(B)+c}(x)$ received at least $v/N_n$.
    
    (T4) For each $Q \in \mathcal{D}_k$, give each of its $2^{nc}$ rank-$(k+c)$ subcubes $Q'$ the ball $\widehat{B}_{Q'}$, which has diameter at most $2^{-k}$, with weight at least $\tfrac12 2^{-nc} b(Q)$. For a given $x$, use $Q' = Q_{r+c}(x)$. $\square$
    
    **Lemma (the (DT) bad set is tilted-null).** Let $\mu$ be a finite Borel measure, $b$ a dyadic Kraft weight, and $0 < \eta < \varepsilon$. Then the set
    
    $$
    \left\{ x : M^b_t(x) > 2^{\varepsilon t} \mu(Q_t(x)) \text{ for infinitely many } t \right\}
    $$
    
    is $\mathscr{T}_{\mu,\eta}$-null.
    
    **Proof.** For each $m$, cover the set by the cubes $Q$ of rank $t \geq m$ that contain some dyadic $Q' \subseteq Q$ with $b(Q') > 2^{\varepsilon t} \mu(Q)$. The tilted cost of this cover is less than
    
    $$
    \sum_{t \geq m} 2^{-(\varepsilon - \eta) t} \sum_{Q \in \mathcal{D}_t} \sup_{Q' \subseteq Q} b(Q') \leq \sum_{t \geq m} 2^{-(\varepsilon - \eta) t}. \qquad \square
    $$
    
    Unlike in C.5, the condition $\eta < \varepsilon$ is genuinely needed here, because one cube $Q'$ can be charged at many ranks $t$.
    
    **Theorem.** Let $s = \dim_H X > 0$. The following are equivalent:
    
    - $X$ has a Kraft ball system $\mathcal{C}$ with $\dim_H G_X(\mathcal{C}, \mathcal{E}, \varepsilon) = s$ for every Kraft ball system $\mathcal{E}$ and every $\varepsilon > 0$ (the full-dimensional form of Theorem C, with or without (M));
    - some finite Borel measure satisfies (PHE) on $X$.
    
    **Proof (⇒).** Let $\mu := \mu_{\mathcal{C}}$ from (T1). Fix $\eta > 0$ and a $\mathscr{T}_{\mu,\eta}$-null $N \subseteq X$. By C.5 there is a strictly positive Kraft weight $b$ with $N \subseteq \operatorname{Tgt}_\eta(\mu, b)$. Using (T4) and then (T1), each $x \in N$ satisfies, for infinitely many $r$,
    
    $$
    M^{\mathcal{E}_b}_r(x) \geq 2^{-nc-1} b(Q_r(x)) \geq 2^{-nc-1} 2^{\eta r} \mu(Q_r(x)) \geq 2^{-nc-n-1} 2^{\eta r} M^{\mathcal{C}}_r(x).
    $$
    
    Also $M^{\mathcal{E}_b}_r(x) > 0$, because $b > 0$. So $x \notin G_X(\mathcal{C}, \mathcal{E}_b, \eta/2)$. Hence $G_X(\mathcal{C}, \mathcal{E}_b, \eta/2) \subseteq X \setminus N$, and $X \setminus N$ has dimension $s$.
    
    **Proof (⇐).** Normalize so that $\mu(\mathbb{R}^n) \leq 1$, and let $\mathcal{C} := \mathcal{C}_\mu$ from (T2). Fix $\mathcal{E}$ and $\varepsilon$, put $b := b_{\mathcal{E}}$ from (T3), and choose $0 < \eta < \varepsilon' < \varepsilon$. Let
    
    $$
    N := X \cap \left\{ x : M^b_t(x) > 2^{\varepsilon' t} \mu(Q_t(x)) \text{ for infinitely many } t \right\}.
    $$
    
    By the lemma, $N$ is $\mathscr T_{\mu,\eta}$-null, so $\dim_H(X \setminus N) = s$. For $x \in X \setminus N$ and all large $r$,
    
    $$
    M^{\mathcal{E}}_r(x) \leq N_n M^b_{r+c}(x) \leq N_n 2^{\varepsilon'(r+c)} \mu(Q_{r+c}(x)) \leq 2 N_n 2^{\varepsilon'(r+c)} \pi_{r+c}^{-1} M^{\mathcal{C}}_r(x) \leq 2^{\varepsilon r} M^{\mathcal{C}}_r(x).
    $$
    
    So $X \setminus N \subseteq G_X(\mathcal{C}, \mathcal{E}, \varepsilon)$. $\square$
    
    If $\mu$ satisfies (20), then (M) for $\mathcal{C}_\mu$ follows from (T2). Theorem C ⟺ Theorem B is exact by Kraft–McMillan. So this theorem, combined with Theorem A, leaves Theorem A as the only place oracles enter.
    
    **The design rule behind (T1)–(T4).** Classically there is no refinement inequality: $L^\Pi_{r+1}$ can exceed $L^\Pi_r$ by any amount. So a bounded scale shift is harmless only on the side that we are allowed to modify.
    
    - Competitors can be refined at bounded cost: (T3) pushes weight down $c$ ranks, and (T4) splits each cube into $2^{nc}$ subcubes.
    - The base cannot be refined. (T1) and (T2) are arranged so that the base never needs a shift in the unfavorable direction.
    - Monotonicity of the base measure, $\mu(Q_{r+1}(x)) \leq \mu(Q_r(x))$, which is a consequence of additivity, does the rest.
    
    The same rule gives a classical proof of Theorem D ⟺ Theorem C. The only new wrinkle is that a capacity atom serves at every radius, so turning a competitor capacity into a ball system costs a subexponential factor $\pi_r$. The scale shift of one or two between "$q \in B(x, 2^{-r})$" and "$x$ lies in a ball of diameter $\leq 2^{-r}$" is again absorbed by refining the competitor's balls by a bounded factor.
    
    ---
    
    ## Part D. Porting checklist for the MyST notes
    
    - **`set`.** In `myst.yml` it is a two-argument macro: `set{x \in X}{g(x) \geq t}`. Lines 775, 905, and 911 use one argument.
    - **Ambient dimension.** The notes use $\mathbb{R}^m$, with $n$ reserved for a second space; the draft uses $n$.
    - **Dyadic cubes.** The notes write $\mathcal{Q}^m_r$. The draft's $\mathcal{D}_r$ collides with the competitor system $\mathcal{D}$ in §6 and Theorem C, and with the macro `D` (= `mathcal{D}`).
    - **Tilted measures.** $\mathscr{T}_{\mu,\eta}$ is the Method-II net measure $\mathcal{H}^{\rho_{\mu,\eta}}$ of the net premeasure (PG), in the notes' §1.1 notation. The dissertation's Ch. 4 (Net Measures) defines "comparable premeasures" as exactly "having the same null sets." Using that language would tie §8 into the existing framework. Ch. 4 isn't in the online table of contents yet.
    - **Local dimensions.** The dissertation writes $\dim_{\operatorname{loc}}\mathbf{m}$ and $\dim_{\operatorname{loc}}\boldsymbol\kappa$. `Kappa` is already a macro for $\boldsymbol\kappa$, so $\Pi_{a_A}$ can be written `Kappa^A`.
    - **Citations into the notes.** (18) can cite the notes' Lemma 2.1.4 (`maxmin-truncation-for-r`), and refinement can cite Lemma 2.1.2 (Case–Lutz).
    - **Directives.** Convert `<aside>` blocks to `:::{prf:theorem}`, `:::{prf:definition}`, and `:::{prf:proof}` with `:label:`, and cite with `{cite:t}`.
    - **Constants.** The notes define $\leq^+$ and $=^+$ on the Notation page; several "$+ O(1)$" chains would read better with them.
    - **Dimension function.** The notes' definition (§1.1) is right-continuous with $h(t) = 0 \iff t = 0$. §9.3 should point there rather than to the dissertation's section number.
    
    ---
    
    ## Part E. Open questions I'd list in §13
    
    1. **The $\sigma$-ideal version.** Is having an optimal Hausdorff oracle equivalent to having a $\mu$ for which (PHE) holds for the $\sigma$-ideal generated by $\mathcal{N}^+_\mu$? Equivalently: can one always choose $A$ so that, for every $B$, the set $\{x : K^{A,B}_r(x) \geq K^A_r(x) - o(r)\}$ has full dimension? This replaces the claim at line 1114.
    2. **The untilted ambient version.** Is having an optimal Hausdorff oracle equivalent to having a finite Borel $\mu$ such that every $\mu^*$null $N \subseteq X$ is harmless? C.8 shows this holds for analytic sets, under Stull's measure criterion, and for Bernstein sets. Weakly regular sets are the test case, because there the proof uses the tilt.
    3. **Irregular exact gauges.** C.9 now gives an $\mathsf{AC} + \mathsf{CH}$ counterexample. What remains is a careful line-by-line write-up of the relativized construction, and checking whether the published STACS version of Stull's paper restricts the notion of gauge.
    4. **Coordinate-free and centered-ball versions.** The dyadic theorem holds for each of the $n+1$ shifted dyadic grids (rationally shifted, so the oracle proofs go through unchanged), so whether a witness exists doesn't depend on the grid. A ball version needs a centered Method II. The necessity direction is where this matters: a ball containing $x$ near its boundary need not dominate $Q_r(x)$.
    5. **Canonical witnesses.** Witnesses are upward closed and closed under countable positive combinations. Is there a natural description of the smallest possible null ideal, for example the intersection of $\mathcal{N}^+_\mu$ over all witnesses $\mu$?
    
    ---
    
    ### Corrections and new provenance
    
    - **Stull's Lemma 18** (the basic CH set in $\mathbb{R}$) prescribes only $\dim_H = s$; by the same estimates its packing dimension is 1. The prescribed-pair examples are Theorem 41.
    - **What Stull already proves.** Supersets (Observation 6), countable unions (Proposition 7), joins (Lemma 5), and the packing analogue of Proposition 4 (Proposition 33). C.8's Propositions 1–2 are classical reproofs of these, and C.10 corrects his proof of Proposition 33. There are also small slips in his packing section: Lemma 36 concludes "optimal Hausdorff oracle" where it means packing, and Proposition 33's backward direction uses Hausdorff quantities.
    - **Measure point-to-set principle (C.7).** This is Cutler's weak duality principle, *Math. Proc. Cambridge Philos. Soc.* 118 (1995), 393–410, and Lutz–Lutz make the comparison explicitly. Your references cite Cutler 1986; add the 1995 paper.
    - **Sum/sup lemma (C.6).** This is the Case–Lutz LDS coding theorem (*Mutual dimension*, ACM TOCT 7(3), 2015).
    - **Outer-measure mass distribution (C.8).** This is the Rogers–Taylor–Tricot density theorem, which is Crone–Fishman–Jackson's Theorem 1.
    - **Analytic sets (C.8, Proposition 4).** Use the Besicovitch–Davies theorem: R. O. Davies, *Subsets of finite measure in analytic sets*, Indag. Math. 14 (1952), 488–489. Crone–Fishman–Jackson note that the classical route goes through Rogers' increasing-sets lemma (Rogers, *Hausdorff Measures*, Theorems 47–48).
    - **More from Crone–Fishman–Jackson.** In the example following their AD corollary, they show that for a Bernstein set *neither* player wins the dimension game. Their Example 1, a union of compact $K_n$ with $\dim_H K_n \uparrow \delta$, is essentially the set in C.9's first proposition.
    
    ### Not resolved
    
    - **Olsen 1995.** It isn't on arXiv and I couldn't read it. Secondary sources describe $\mathcal{H}^{q,t}_\mu$ as a *centered* construction with an extra supremum over subsets, usually studied for $E \subseteq \operatorname{supp}\mu$. I found nothing treating null sets at $q = 1$, $t < 0$. So "(PT) is a dyadic, uncentered relative of Olsen's $\mathcal{H}^{1,-\eta}_\mu$" is the right phrasing, and the novelty claim stays "not found in the literature", not "verified new".
    - **The STACS 2022 version of Stull's paper.** I only read arXiv v2. Whether the published version changes the gauge definition or the exact-gauge claim is unchecked.
    
    ---
    
    ## Part G. The top summary and §§1–7.2
    
    The first half is in much better shape than the second. The proofs in §5 check out. Most of what follows is consistency, citations, and three places where a sentence claims more than its argument gives: line 400, line 546, and (DT) at line 833.
    
    ### G.1 Issues that cut across sections
    
    - **Two machines, not one.** Line 5 fixes $\mathbf{U}$ with outputs rational closed balls. Line 165 then fixes $\mathscr{U}$ (a different glyph), line 168 uses $K^A_{\mathbf{U}}(q)$ for rational *points*, and line 434 patches this with "we may as well assume $\mathbf{U}$ also fixes a universal oracle machine mapping programs to rational points." Miyabe's convention is cleaner: a ball machine $U$ and a point machine $V$ (his Definitions 5.3 and 5.6). Suggested replacement for the second sentence of line 5:
        
        > We fix two universal prefix-free oracle machines: $\mathbf{U}$, whose outputs are rational closed balls from $\mathcal{B}_{\mathbb{Q}}$, and $\mathbf{V}$, whose outputs are rational points. For an oracle $A$ and $q \in \mathbb{Q}^n$, put $K^A(q) := \min\{ |p| : \mathbf{V}^A(p) = q \}$.
        > 
        
        Then line 165 needs no new machine, and line 434 can be deleted.
        
    - **The $s = 0$ and minimizing clauses.** The A.2 simplifications apply here too. Theorem B's "if $s > 0$" can stay, but add the triviality remark (G.4). (M) is redundant for existence (C.7, last remark).
    
    ### G.6 §3 (lines 282–370)
    
    This is the Lutz–Lutz cover-encoding argument with the codebook taken out of the oracle, which supports your historical remark at line 302.
    
    - **Lines 358–370**: fine. You could add that $\operatorname{dom}(\varphi \vee \psi) = 0$ and $\operatorname{dom}\varphi \cup \operatorname{dom}\psi$ is prefix-free.
    
    ## Part H. The three follow-up directions: what I could prove
    
    I worked on the three directions from my assessment: products, projections, and set theory. Summary, roughly in order of confidence:
    
    - **Products (H.1).** Optimality is closed under products whenever $\dim_H(X \times Y) = \dim_H X + \dim_H Y$. There is a short oracle proof (H1), and a classical proof through Theorem E′ (H3) that rests on a new "tilted slicing" lemma (H2). A pushforward argument (H4) recovers the converse half of Stull's Lemma 21. The non-additive case stays open.
    - **Projections (H.2).** I did *not* find an oracle-free proof that (PHE) implies Marstrand's theorem. Instead I found a one-line lemma: the information an extra oracle gains about a point cannot grow under Lipschitz maps (H5). That gives closure under bi-Lipschitz maps and certain Lipschitz images (H6). Combined with the Lutz–Stull and Fiedler–Jing projection engines, it shows that **optimality survives almost every projection**, onto lines and onto $k$planes, with an exceptional set contained in a countable union of lower-dimensional sets (H7). There is also a sumset corollary (H8).
    - **Set theory (H.3).**
        - Under $\boldsymbol\Pi^1_1$determinacy, every $\boldsymbol\Sigma^1_2$ set has an optimal Hausdorff oracle (H9; solid).
        - Under $V = L$ there is a co-analytic set with none (H10; a detailed sketch built on Vidnyánszky's theorem).
        - So analytic sets are exactly where ZFC alone decides the question.
        - H11 explains why Stull's construction scheme needs CH.
    
    **Novelty check.** An arXiv metadata search finds only Stull and Fiedler–Jing on optimal oracles, and neither states these results; I also read both proofs. That doesn't rule out unpublished or folklore versions.
    
    ### H.1 Products
    
    Notation: for $Z \subseteq \mathbb{R}^n \times \mathbb{R}^m$ and $x \in \mathbb{R}^n$, write $Z_x := \{ y : (x, y) \in Z \}$. The rank-$r$ dyadic cubes of $\mathbb{R}^{n+m}$ are exactly the products $Q \times Q'$ of rank-$r$ cubes of $\mathbb{R}^n$ and $\mathbb{R}^m$.
    
    **Theorem H1 (products, additive case).** Let $X \subseteq \mathbb{R}^n$ and $Y \subseteq \mathbb{R}^m$ have optimal Hausdorff oracles, with $s_X := \dim_H X$ and $s_Y := \dim_H Y$. If $\dim_H(X \times Y) = s_X + s_Y$, then $X \times Y$ has an optimal Hausdorff oracle.
    
    **Proof.** Let $A_X$ and $A_Y$ be optimal for $X$ and $Y$, let $A_{XY}$ be a Hausdorff oracle for $X \times Y$, and put $C := A_X \oplus A_Y \oplus A_{XY}$. By Stull's Lemma 5, $C$ is optimal for $X$ and for $Y$, and it is a Hausdorff oracle for $X \times Y$. Fix an oracle $B$ and $\varepsilon > 0$.
    
    - Optimality of $C$ for $X$ against $B$ gives $x \in X$ with $\dim^{C,B}(x) \geq s_X - \varepsilon$ and $K^{C,B}_r(x) \geq K^C_r(x) - \varepsilon r$ for all large $r$.
    - Optimality of $C$ for $Y$ against $B \oplus x$ gives $y \in Y$ with $\dim^{C,B,x}(y) \geq s_Y - \varepsilon$ and $K^{C,B,x}_r(y) \geq K^C_r(y) - \varepsilon r$ for all large $r$.
    
    We use two standard facts, both of which relativize with constants independent of the oracle. The first is the chain rule $K_r(x, y) = K_r(x) + K_r(y \mid x) \pm O(\log r)$ (Lutz–Lutz). The second is $K^x_r(y) \leq K_r(y \mid x) + K(r) + O(1)$ (the notes' Lemma 2.1.7). Together with the subadditivity $K_r(x,y) \leq K_r(x) + K_r(y) + O(\log r)$, they give, for all large $r$,
    
    $$
    K^{C,B}_r(x, y) \geq K^{C,B}_r(x) + K^{C,B,x}_r(y) - O(\log r) \geq K^C_r(x) + K^C_r(y) - 2 \varepsilon r - O(\log r) \geq K^C_r(x, y) - 2 \varepsilon r - O(\log r).
    $$
    
    Dividing the first inequality by $r$ and taking $\liminf$ gives
    
    $$
    \dim^{C,B}(x, y) \geq \dim^{C,B}(x) + \dim^{C,B,x}(y) \geq s_X + s_Y - 2\varepsilon = \dim_H(X \times Y) - 2 \varepsilon. \qquad \square
    $$
    
    The additivity hypothesis holds whenever one factor is weakly regular, because $\dim_H X + \dim_H Y \leq \dim_H(X \times Y) \leq \dim_H X + \dim_P Y$ for arbitrary sets. So H1 contains the forward direction of Stull's Lemma 21.
    
    **Lemma H2 (slicing tilted-null sets).** Let $\mu$ and $\nu$ be finite Borel measures on $\mathbb{R}^n$ and $\mathbb{R}^m$, let $\eta_1, \eta_2 > 0$, and let $N \subseteq \mathbb{R}^{n+m}$ satisfy $\mathscr T_{\mu \otimes \nu, \eta_1 + \eta_2}(N) = 0$. Then for every $\eta_1' < \eta_1$ and $\eta_2' < \eta_2$ there is a $\mathscr T_{\mu, \eta_1'}$-null set $E \subseteq \mathbb{R}^n$ such that $N_x$ is $\mathscr T_{\nu, \eta_2'}$-null for every $x \notin E$.
    
    **Proof.** By C.5 there is a dyadic Kraft weight $b$ on the cubes of $\mathbb{R}^{n+m}$ with $N \subseteq \operatorname{Tgt}_{\eta_1 + \eta_2}(\mu \otimes \nu, b)$. Define its marginal $\beta(Q) := \sum_{Q'} b(Q \times Q')$, summing over cubes $Q'$ of the same rank as $Q$. This is again a dyadic Kraft weight.
    
    Let $E_0$ be the set of $x$ with $\mu(Q_r(x)) = 0$ for some $r$. It is a union of $\mu$-null cubes, hence $\mathscr T_{\mu,\eta}$-null for every $\eta$ (cover it by their subcubes). For $x \notin E_0$ and a cube $Q'$ of rank $r$, put
    
    $$
    c_x(Q') := 2^{-\eta_1 r} \frac{b(Q_r(x) \times Q')}{\mu(Q_r(x))}, \qquad \text{so that} \qquad \sum_{Q'} c_x(Q') = \sum_r 2^{-\eta_1 r} \frac{\beta(Q_r(x))}{\mu(Q_r(x))}.
    $$
    
    Let $E_\infty$ be the set of $x \notin E_0$ for which this sum diverges. For such $x$ the terms exceed $(r+1)^{-2}$ infinitely often, so $\beta(Q_r(x)) \geq (r+1)^{-2} 2^{\eta_1 r} \mu(Q_r(x))$ for infinitely many $r$. Hence $x \in \operatorname{Tgt}_{\eta_1'}(\mu, \beta)$, and $E_\infty$ is $\mathscr T_{\mu, \eta_1'}$-null by C.5.
    
    Put $E := E_0 \cup E_\infty$, and let $x \notin E$ and $y \in N_x$. Infinitely many $r$ satisfy $b(Q_r(x) \times Q_r(y)) \geq 2^{(\eta_1 + \eta_2) r} \mu(Q_r(x)) \nu(Q_r(y))$, which says exactly that $c_x(Q_r(y)) \geq 2^{\eta_2 r} \nu(Q_r(y))$. After dividing by the finite total $\sum_{Q'} c_x(Q')$, $c_x$ becomes a dyadic Kraft weight that targets $N_x$ at every exponent $\eta_2' < \eta_2$; the constant is absorbed by the exponent. By C.5, $N_x$ is $\mathscr T_{\nu, \eta_2'}$-null. $\square$
    
    **Theorem H3 (the classical form of H1).** Suppose $\mu$ witnesses $X$ and $\nu$ witnesses $Y$ in the sense of Theorem E′(ii), with $s_X, s_Y > 0$ and $\dim_H(X \times Y) = s_X + s_Y$. Then $\mu \otimes \nu$ witnesses $X \times Y$.
    
    **Proof.** Let $N \subseteq X \times Y$ be $\mathscr T_{\mu \otimes \nu, \eta}$-null. Apply H2 with $\eta_1 = \eta_2 = \eta/2$ and some $\eta' < \eta/2$. This gives a set $E$ with $\dim_H(X \setminus E) = s_X$ by (PHE) for $\mu$, and with $\dim_H(Y \setminus N_x) = s_Y$ for every $x \in X \setminus E$ by (PHE) for $\nu$.
    
    Put $Z := (X \times Y) \setminus N$. For $x \in X \setminus E$ we have $Z_x = Y \setminus N_x$. Eilenberg's inequality (Federer 2.10.25), applied to the projection $(x, y) \mapsto x$, gives
    
    $$
    \int^* \mathcal{H}^t(Z_x)\, d\mathcal{H}^u(x) \leq C\, \mathcal{H}^{u+t}(Z) \qquad (u, t \geq 0).
    $$
    
    For $u < s_X$ and $t < s_Y$, the integrand is $\infty$ on $X \setminus E$, and $\mathcal{H}^u(X \setminus E) = \infty$. So the upper integral is $\infty$, hence $\mathcal{H}^{u+t}(Z) = \infty$, and $\dim_H Z \geq s_X + s_Y = \dim_H(X \times Y)$. $\square$
    
    By Theorem E′, H3 is equivalent to H1. Its interest is that it uses no oracles, and that Lemma H2 is a new and reusable fact about tilted null ideals.
    
    **Proposition H4 (factors from products).** Suppose $\mu$ witnesses $X \times Y$, and let $\nu := (\pi_Y)_* \mu$. Then every $\mathscr T_{\nu,\eta}$-null $N \subseteq Y$ satisfies
    
    $$
    \dim_H(Y \setminus N) \geq \dim_H(X \times Y) - \dim_P X.
    $$
    
    In particular, if $X$ is weakly regular and $X \times Y$ has an optimal Hausdorff oracle, then so does $Y$ (the converse half of Stull's Lemma 21).
    
    **Proof.** If $N$ is covered by cubes $Q'_i$ of rank $r_i$, then the cubes $Q \times Q'_i$ cover $\mathbb{R}^n \times N$ at total cost $\sum_i 2^{\eta r_i} \sum_Q \mu(Q \times Q'_i) = \sum_i 2^{\eta r_i} \nu(Q'_i)$. So $X \times N$ is $\mathscr T_{\mu,\eta}$-null. By (PHE), $X \times (Y \setminus N)$ has dimension $\dim_H(X \times Y)$. The product inequality $\dim_H(X \times (Y \setminus N)) \leq \dim_P X + \dim_H(Y \setminus N)$ finishes the proof. $\square$
    
    **Still open: the non-additive case.** When $\dim_H(X \times Y) > \dim_H X + \dim_H Y$, both proofs stop at $s_X + s_Y$. In the oracle proof, optimality gives no control over the complexity profiles of the chosen $x$ and $y$, and the extra dimension of $X \times Y$ comes from points whose profiles interleave. In the classical proof, Eilenberg's inequality only sees base and fiber dimensions. I'd guess a counterexample exists under CH, but I haven't built one.
    
    ### H.2 Projections and Lipschitz images
    
    **Lemma H5 (information gain does not increase under Lipschitz maps).** Let $Z$ be an oracle and $f : \mathbb{R}^n \to \mathbb{R}^m$ a Lipschitz map computable relative to $Z$; that is, from $Z$ and a rational $q$ one can compute $f(q)$ to any precision. Then for every oracle $B$, point $z$, and precision $r$,
    
    $$
    K^Z_r(f(z)) - K^{Z,B}_r(f(z)) \leq K^Z_r(z) - K^{Z,B}_r(z) + O(\log r),
    $$
    
    with the constant depending only on $n$, $m$, and the Lipschitz constant of $f$.
    
    **Proof.** Let $W \in \{Z, Z \oplus B\}$. A precision-$(r + c)$ approximation of $z$ yields a precision-$r$ approximation of $f(z)$, so by the refinement estimate, $K^W_r(z, f(z)) = K^W_r(z) \pm O(\log r)$. The chain rule gives $K^W_r(z, f(z)) = K^W_r(f(z)) + K^W_r(z \mid f(z)) \pm O(\log r)$. Subtract the instance $W = Z \oplus B$ from the instance $W = Z$, and use $K^{Z,B}_r(z \mid f(z)) \leq K^Z_r(z \mid f(z)) + O(1)$. $\square$
    
    In words: if an extra oracle $B$ does not help describe $z$, it does not help describe any Lipschitz image of $z$. So the preservation inequality passes from points to their images.
    
    **Proposition H6 (Lipschitz images).** Let $E \subseteq \mathbb{R}^n$ have an optimal Hausdorff oracle, with $s := \dim_H E > 0$, and let $f : \mathbb{R}^n \to \mathbb{R}^m$ be Lipschitz. Suppose that $\dim_H f(G) = \dim_H f(E)$ for every $G \subseteq E$ with $\dim_H G = s$. Then $f(E)$ has an optimal Hausdorff oracle.
    
    In particular, **having an optimal Hausdorff oracle is invariant under bi-Lipschitz bijections between sets**: a bi-Lipschitz bijection $X \to X'$ extends coordinatewise (McShane) to a Lipschitz map $\mathbb{R}^n \to \mathbb{R}^m$, and the hypothesis holds trivially.
    
    **Proof.** Let $A$ be optimal for $E$, let $F$ encode $f$, let $H$ be a Hausdorff oracle for $f(E)$, and put $A' := A \oplus F \oplus H$. By Stull's Lemma 5, $A'$ is optimal for $E$, and it is a Hausdorff oracle for $f(E)$. Fix $B$ and $\varepsilon$.
    
    The preservation set $G := N_E(A', B, \varepsilon)$ has dimension $s$ by Stull's Proposition 4, so $\dim_H f(G) = \dim_H f(E)$. The point-to-set principle relative to $A' \oplus B$ gives $z \in G$ with $\dim^{A',B}(f(z)) \geq \dim_H f(E) - \varepsilon$. By H5, $f(z)$ inherits preservation from $z$. $\square$
    
    **Theorem H7 (optimality survives almost every projection).** Let $F \subseteq \mathbb{R}^n$ have an optimal Hausdorff oracle $A$, with $a := \dim_H F > 0$, and let $1 \leq k < n$. Then for every $V \in G(n,k)$ with $\dim^A(V) = k(n-k)$, the projection $p_V F$ has an optimal Hausdorff oracle, and $\dim_H p_V F = \min\{a, k\}$.
    
    Consequently, the set of $V$ for which $p_V F$ has no optimal Hausdorff oracle is contained in
    
    $$
    \bigcup_{j \geq 1} \left\{ V : \dim^A(V) \leq k(n-k) - 1/j \right\},
    $$
    
    a countable union of sets of Hausdorff dimension less than $k(n-k)$. In particular it has measure zero. This is strictly stronger than measure zero: a null set need not be a countable union of lower-dimensional sets.
    
    **Proof.** Fix such a $V$. Let $H$ be a Hausdorff oracle for $p_V F$, and put $A' := A \oplus V \oplus H$; it is a Hausdorff oracle for $p_V F$. Fix a competitor $B$ and $\varepsilon > 0$. Optimality of $A$ against $V \oplus H \oplus B$ gives $z \in F$ with
    
    $$
    \dim^{A,V,H,B}(z) \geq a - \varepsilon \qquad \text{and} \qquad K^{A,V,H,B}_r(z) \geq K^A_r(z) - \varepsilon r \quad (\forall^\infty r).
    $$
    
    *Dimension.* This $z$ is exactly the input of the proof of Fiedler–Jing's Theorem 1, with $b = k(n-k)$ and their competitor equal to $H \oplus B$. Its final chain of inequalities gives
    
    $$
    K^{A,V,H,B}_r(p_V z) \geq \left( \min\{a, k\} - O(\sqrt{\varepsilon}) \right) r
    $$
    
    for all large $r$, not just along a subsequence. (For $n = 2$, Stull's Theorem 23, the Lutz–Stull engine, gives the same for $\theta$ random relative to $A$.) So $\dim^{A',B}(p_V z) \geq \min\{a, k\} - O(\sqrt{\varepsilon})$. The upper bound $\dim_H p_V F \leq \min\{a, k\}$ is trivial, so $\dim_H p_V F = \min\{a, k\}$ and the dimension clause holds.
    
    *Preservation.* We have $K^{A'}_r(z) - K^{A',B}_r(z) \leq K^A_r(z) + O(1) - K^{A,V,H,B}_r(z) \leq \varepsilon r + O(1)$. Since $p_V$ is 1-Lipschitz and computable from $V$, H5 gives $K^{A'}_r(p_V z) - K^{A',B}_r(p_V z) \leq \varepsilon r + O(\log r)$.
    
    *Exceptional set.* By the point-to-set principle on $G(n,k)$, each set $\{ V : \dim^A(V) \leq c \}$ has Hausdorff dimension at most $c$. $\square$
    
    **Corollary H8 (sums).** Let $X, Y \subseteq \mathbb{R}$ have optimal Hausdorff oracles, with $\dim_H(X \times Y) = \dim_H X + \dim_H Y$ (for example, if one of them is weakly regular). Then for almost every $\lambda \in \mathbb{R}$, the set $X + \lambda Y$ has an optimal Hausdorff oracle and $\dim_H(X + \lambda Y) = \min\{\dim_H X + \dim_H Y, 1\}$.
    
    **Proof.** By H1, $X \times Y$ has an optimal Hausdorff oracle. Its projections satisfy $p_\theta(X \times Y) = \cos\theta \cdot (X + \tan\theta \cdot Y)$. Apply H7 and Stull's Marstrand theorem, use H6 to remove the scaling, and note that $\theta \mapsto \tan\theta$ preserves null sets. $\square$
    
    **What I did not get: a classical proof of Marstrand from (PHE).** The oracle proof needs a lower bound for $K_r(p_\theta z)$ at every scale, valid whenever the competitor makes no linear savings on $z$. A classical proof would need a discretized version of that engine for measures, in the spirit of Orponen's combinatorial proof for weakly regular sets. I think that remains the real test of whether Theorem E′ is a GMT tool.
    
    ### H.3 Set theory
    
    **Proposition H9 (determinacy gives the projective level).** Assume $\boldsymbol\Pi^1_1$-determinacy, which follows for instance from a measurable cardinal. Then every $\boldsymbol\Sigma^1_2$ subset of $\mathbb{R}^n$, in particular every co-analytic set, has an optimal Hausdorff oracle.
    
    **Proof.** Under $\boldsymbol\Pi^1_1$-determinacy, Crone–Fishman–Jackson show that every $\boldsymbol\Sigma^1_2$ set $X$ with $\dim_H X \geq \delta$ contains, for each $\delta' < \delta$, a compact set of dimension at least $\delta'$ (introduction of their paper). So $X$ contains compact sets $K_k$ with $\dim_H K_k \geq s - 1/k$. The union $Y := \bigcup_k K_k$ is $\sigma$-compact with $\dim_H Y = s$, so it has an optimal oracle by Stull's Lemma 15, and then so does $X$ by Stull's Observation 6. $\square$
    
    **Theorem H10 ($V = L$; a detailed sketch).** For every $n \geq 1$ and $s \in (0, n)$, there is a co-analytic set $E \subseteq \mathbb{R}^n$ with $\dim_H E = s$ and no optimal Hausdorff oracle.
    
    **Tool.** Vidnyánszky (*Transfinite inductions producing coanalytic sets*, Fund. Math. 2014; arXiv:1209.4267, Theorem 1.3) proves the following under $V = L$. Let $B$ be an uncountable Borel set, and let $F \subseteq M^{\leq \omega} \times B \times M$ be co-analytic, such that every section $F_{(A, p)}$ is cofinal in the Turing degrees. Then there is a co-analytic $X = \{ x_\alpha : \alpha < \omega_1 \}$ and an enumeration $B = \{ p_\alpha \}$ such that $x_\alpha \in F_{(A_\alpha, p_\alpha)}$, where $A_\alpha$ enumerates $\{ x_\beta : \beta < \alpha \}$ in order type at most $\omega$.
    
    **Encoding Stull's construction (Lemma 18) in that form.** Work in $2^\omega$, and fix $s \in (0,1)$ and Stull's blocks $(a_n, b_n]$, with $a_{n+1} = b_n^2$ and $b_n = \lfloor a_n / s \rfloor$. Reserve two very sparse sets of positions $S_1$ and $S_2$, with $O(\log\log r)$ positions below $r$. Call the positions outside the blocks and outside $S_1 \cup S_2$ *free*. For a point $y$, write $x(y)$ for its sequence of free digits. Inside each stretch $(b_n, a_{n+1}]$, fix a window $W_n$ of $b_n - a_n$ free positions; distinct $n$ give disjoint windows. Let $F_{(A, p)}$ be the set of $y$ such that:
    
    1. the digits of $y$ on $S_1$ spell out $p$;
    2. $x(y)$ is Martin-Löf random relative to $p \oplus \bigoplus_k A(k)$;
    3. on block $n$, $y$ copies the digits of $x(A(k(n)))$ in window $W_n$, where $k : \omega \to \omega$ hits every index infinitely often (cycling if $A$ is finite, and using zeros if $A$ is empty);
    4. the digits on $S_2$ are unconstrained.
    
    Checking Vidnyánszky's hypotheses:
    
    - **$F$ is Borel.** Relative ML-randomness is a Borel condition, and the other clauses are closed.
    - **Sections are cofinal in the Turing degrees.** Any $z$ can be written on $S_2$, so some $y$ in the section computes $z$.
    - **The sparse tracks are harmless.** They change every complexity in Stull's estimates by only $O(\log\log r)$.
    
    Vidnyánszky's theorem then gives a co-analytic $X = \{ y_\alpha \}$, where $p_\alpha$ runs through all oracles and $A_\alpha$ enumerates the earlier points.
    
    **Stull's three lemmas go through.**
    
    - **$\dim_H X \leq s$.** Every $y_\beta$ with $\beta > 0$ copies windows of $x(y_0)$ on infinitely many blocks, so relative to the oracle $x(y_0)$ its complexity at scale $b_n$ is at most $a_n + o(b_n)$.
    - **$\dim_H X \geq s$.** Every oracle is some $p_\alpha$, and $x(y_\alpha)$ is random relative to $p_\alpha$ together with everything $y_\alpha$ copies.
    - **No oracle $p_\alpha$ is optimal.** Use the competitor $B_\alpha := x(y_\alpha) \oplus (y_\beta)_{\beta \leq \alpha}$, a countable join since $\alpha < \omega_1$.
        - For $\beta \leq \alpha$, $\dim^{p_\alpha, B_\alpha}(y_\beta) = 0$.
        - For $\beta > \alpha$, $y_\beta$ copies windows of $x(y_\alpha)$ on infinitely many blocks. Those windows are incompressible relative to $p_\alpha$, because $p_\alpha$ is readable from $y_\alpha \in A_\beta$ through the track $S_1$, so condition 2 for $y_\beta$ makes $x(y_\beta)$ random relative to $p_\alpha \oplus x(y_\alpha)$. Van Lambalgen's theorem then handles the copied windows exactly as in Stull's proof. So $B_\alpha$ saves about $(1-s) b_n$ bits infinitely often.
    
    Finally, the binary-expansion map is injective on the points we use, and it carries co-analytic sets of such points to co-analytic subsets of $[0,1]$. Stull's Theorem 22 (products with $\{0\}$ or $[0,1]$) then gives every $s \in (0,n)$ in $\mathbb{R}^n$ while keeping co-analyticity. $\square$
    
    **Corollary.** "Every co-analytic set has an optimal Hausdorff oracle" fails in $L$ and holds under $\boldsymbol\Pi^1_1$-determinacy. It is therefore independent of ZFC, relative to the consistency of ZFC plus "every real has a sharp." For analytic sets the statement is a ZFC theorem (Stull). So among the projective classes, analytic sets are exactly where ZFC alone decides it. Stull's packing examples (Theorem 41) should become co-analytic in $L$ the same way, but I haven't checked that.
    
    **Remark H11 (why Stull's scheme needs CH).** In Stull's construction, oracle $A_\alpha$ is defeated because every later point copies $x_\alpha$ infinitely often, while the earlier points are absorbed into a countable competitor. Suppose instead that $\operatorname{cf}(2^{\aleph_0}) > \aleph_1$, for example $2^{\aleph_0} = \aleph_2$. Suppose also that each point copies only countably many earlier reals, and that for each $\alpha$ the points not copying $x_\alpha$ form a set $S_\alpha$ of size less than $2^{\aleph_0}$. (That is the most one could hope to absorb, even assuming every set of that size has dimension 0, as under $\operatorname{cov}(\mathcal{M}) = 2^{\aleph_0}$.) Then $\bigcup_{\alpha < \omega_1} S_\alpha$ has size less than $2^{\aleph_0}$. So some later point lies outside it, which means it copies $x_\alpha$ for every $\alpha < \omega_1$: uncountably many reals, a contradiction. So a ZFC construction, or a model of ZFC in which every set has an optimal oracle, needs a genuinely different mechanism. Theorem E′ casts the problem as diagonalizing against the $2^{\aleph_0}$ finite Borel measures, where each step must control all earlier points at once; that is the natural setting for cardinal-characteristic arguments. I haven't pushed further.
    
    ### H.4 Confidence, and what to check
    
    - **H1, H5, H6, H8, H9.** High confidence. Each is a few lines from cited facts.
    - **H2, H3, H4.** High confidence. They are elementary on top of C.5 and Eilenberg's inequality.
    - **H7.** High confidence that the argument is right. It rests on reading the *niform-in-$r$* lower bound out of the proofs of Stull's Theorem 23 and Fiedler–Jing's Theorem 1, both of which I read in the source. The theorem statements themselves only give the dimension conclusion.
    - **H10.** Medium confidence. Vidnyánszky's hypotheses are verified against his source. What still needs a careful line-by-line write-up is Stull's complexity estimates under the modified encoding: windows instead of position-matched blocks, plus the sparse tracks.
- Possible organization into AIT notes
    
    Several pieces have nothing specifically to do with optimal oracles and fit sections you already have:
    
    - **§2.1 Lifting:** the ball/point and cube/point comparisons (Miyabe's Proposition 5.7 and C.6), next to your Lemmas 2.1.2 and 2.1.4.
    - **§2.4 Point-to-set principles:** a subsection on classical forms of the principle:
        - Miyabe's ball-code theorem, with the direct proof from G.6;
        - Cutler's weak duality principle for measures;
        - the capacity version.
        
        These read well side by side, and Lutz–Lutz already draw the Cutler comparison.
        
    
    Then a new chapter after Ch. 2, "Optimal Oracles", with these sections:
    
    1. **Stull's theory, as a survey with exact citations.** The definition and Proposition 4; the remarks (the $s = 0$ case is trivial, [WITNESS] is free, no common good set); closure properties; sufficient conditions; AC+CH examples; Marstrand and Kaufman as applications.
    2. **Robust codes (Theorems A–C),** framed explicitly as a dictionary.
    3. **Tilted net measures and the Kraft–Carathéodory duality.**
    4. **The measure characterization:** Theorem E′ and upward closure.
    5. **Consequences:** the classical reproofs, why the tilt matters (weakly regular sets), Bernstein sets, exact gauges in both directions.
    6. **Packing analogues.**
    7. **Obstructions and open problems:** games, projections, set theory, the $\sigma$-ideal and untilted variants, products, general nets.
    
    An appendix would hold the capacity version (Theorem D) and the oracle-free transfer lemmas (C.11).
    
    **Practical points:**
    
    - **Order relative to Ch. 4.** Write the chapter on dyadic cubes $\mathcal{Q}^m_r$ so it doesn't depend on the unported net-measures chapter. Add the general-net version later as the payoff of Ch. 4.
    - **Mark what's new.** Since the notes mix dissertation material with unpublished results, label new results visibly, e.g. "(new)" in theorem titles plus a status banner on the chapter. That fits your provenance habit.
    - **Cut or move.** I'd move §12 (Fässler–Orponen), the gauge-refined-optimality speculation, and the long "Is this exact dimension?" discussion into open problems or a short terminology box.
    - **Preprint first.** If you might write this up as a paper (Theorem E′, the applications, and the gauge counterexample would make a reasonable short one), consider an arXiv preprint before it goes on the public notes site, and contact Stull and Miyabe first.


# Optimal oracles: classical cover, capacity, and tilted-measure characterizations

**2 November 2026**

For the entire document let’s fix a non-empty set $X \subseteq \mathbb{R}^n$ and denote $s := \dim_{\operatorname{H}}(X) \geq 0$ its Hausdorff dimension. We fix a universal prefix-free oracle Turing machine $\mathbf{U}$ which maps finite binary strings from $2^{<\omega}$ to closed Euclidean balls from $\mathcal{B}_{\mathbb{Q}}$ of positive rational radius and rational center.

## Top-level summary [slop]

In the pursuit of a classical characterization of “having optimal oracles”, we might seek to answer:

1. Can both the quantification over Turing oracles and Kolmogorov complexity be removed?
2. Can the result then be recognized as a familiar intrinsic condition from geometric measure theory?

It’s pretty easy to establish a classical characterization for having optimal oracles by combining Stull’s definition with ball-code framework of Miyabe:

**Proposed robust ball-code theorem.** Let $X \subseteq \mathbb{R}^n$ be nonempty and $s = \dim_H X$. Then $X$ has an optimal Hausdorff oracle if and only if there is a dimension-minimizing prefix-free code $\varphi$ of rational closed balls such that, for every other rational ball code $\psi$ and every $\varepsilon > 0$, some $x \in X$ satisfies

$$
\liminf_{r \to \infty} \frac{L^\psi_r(x)}{r} \geq s - \varepsilon \quad \text{and} \quad L^\psi_r(x) \geq L^\varphi_r(x) - \varepsilon r
$$

for all sufficiently large $r$; where $L^\varphi_r(x)$ is the length of the shortest $\varphi$-name for a ball of diameter at most $2^{-r}$ containing $x$.

For $s > 0$, the second clause has the cleaner equivalent form

$$
\dim_H \left\{ x \in X : (\forall^\infty r)\; L^\psi_r(x) \geq L^\varphi_r(x) - \varepsilon r \right\} = s. \tag{RB}
$$

for every $\psi$ and $\varepsilon>0$.

By Kraft–McMillan, we could use binary names for summability. That is, a ball code is equivalent to a countable family

$$
\mathcal{C} = \left\{ (B_i, \ell_i) : i \in I \right\}, \qquad \sum_i 2^{-\ell_i} \leq 1,
$$

of rational closed balls carrying a summable budget for assigning descriptions. Thus the theorem is equivalently a statement about **robust minimizing Kraft covers**. With weights $w_i=2^{-\ell_i}$, define

$$
M^{\mathcal{C}}_r(x) = \sup \left\{ w_i : x \in B_i,\ \operatorname{diam} B_i \leq 2^{-r} \right\}.
$$

Then (RB) says that one minimizing weighted ball family $\mathcal{C}$ satisfies, against every competing weighted family $\mathcal{D}$,

$$
M^{\mathcal{D}}_r(x) \leq 2^{\varepsilon r} \cdot M^{\mathcal{C}}_r(x) \quad (\forall^\infty r).
$$

on a subset of $X$ of full Hausdorff dimension. This is a geometric covering condition.

This doesn’t seem to appear in the literature. Indeed, Miyabe’s August 2026 paper explicitly leaves the classical characterization of Stull-optimal oracles open. The proof relies on a “stability-transfer lemma”: that an optimal code remains optimal after it is encoded into, and possibly strengthened by, a universal oracle code.

Next, a **summable rational possibility capacity** is a set function

$$
\Pi_a(E) = \sup \left\{ a(q) : q \in E \cap \mathbb{Q}^n \right\}, \qquad a(q) \geq 0, \qquad \sum_{q \in \mathbb{Q}^n} a(q) \leq 1.
$$

It is a *completely maxitive outer measure* and, because the positive superlevel sets of its density are finite, a *maxitive Choquet capacity*. After normalization, this density representation is the form called a *possibility measure*. Put (Billingsley-type dimension):

$$
\operatorname{capdim}_{\Pi_a}(x) = \liminf_{r \to \infty} \frac{-\log_2 \Pi_a(B(x, 2^{-r}))}{r}.
$$

The ball-code theorem can then be sharpened to the following.

**Maxitive-capacity theorem.** A nonempty $X \subseteq \mathbb{R}^n$, with $s = \dim_H X > 0$, has an optimal Hausdorff oracle if and only if there is a summable rational possibility capacity $\Pi$ such that

$$
\sup_{x \in X} \operatorname{capdim}_\Pi(x) = s
$$

and, for every other such capacity $\Lambda$ and every $\varepsilon>0$,

$$
\dim_H W_X(\Pi, \Lambda, \varepsilon) = s \tag{MC}
$$

where

$$
W_X(\Pi, \Lambda, \varepsilon) := \left\{ x \in X : (\forall^\infty r)\; \Lambda(B(x, 2^{-r})) \leq 2^{\varepsilon r} \cdot \Pi(B(x, 2^{-r})) \right\}.
$$

There is a witness version valid also when $s=0$. This is a genuine classical capacity characterization. Its condition says that one dimension-minimizing maxitive capacity **locally subpower-dominates** every competing summable maxitive capacity on a competitor-dependent full-dimensional part of $X$.

Pushing the covering argument one step further removes the competing capacity as well. Let $\mathcal{D}_r$ be the half-open dyadic cubes of side $2^{-r}$ and let $Q_r(x)$ be the unique member containing $x$. For a finite Borel measure $\mu$ put

$$
\operatorname{capdim}_\mu^{\mathcal{D}}(x) = \liminf_{r \to \infty} \frac{-\log_2 \mu(Q_r(x))}{r}.
$$

For $\eta > 0$, form the Method-II net outer measure

$$
\mathscr T_{\mu,\eta}(Y) = \lim_{m \to \infty} \inf \left\{ \sum_i 2^{\eta r_i} \mu(Q_i) : Y \subseteq \bigcup_i Q_i,\ Q_i \in \mathcal{D}_{r_i},\ r_i \geq m \right\}. \tag{T}
$$

This is a dyadic version of Olsen’s multifractal Hausdorff construction at $(q,t)=(1,-\eta)$. Let’s call it the **positive-tilt net outer measure**.

**Tilted-measure theorem.** Let $X \subseteq \mathbb{R}^n$ be nonempty and $s = \dim_H X > 0$. Then $X$ has an optimal Hausdorff oracle if and only if there is a finite nonzero Borel measure $\mu$ such that

$$
\sup_{x \in X} \operatorname{capdim}_\mu^{\mathcal{D}}(x) = s \tag{TM1}
$$

and deleting a null set for any positive tilt never lowers the Hausdorff dimension of $X$:

$$
N \subseteq X, \quad \mathscr T_{\mu,\eta}(N) = 0 \quad \Longrightarrow \quad \dim_H(X \setminus N) = s \quad (\forall \eta > 0). \tag{TM2}
$$

If $s = 0$, replace (TM2) by $\mathscr T_{\mu,\eta}(X) > 0$ for every $\eta > 0$.

Equivalently, for $s>0$, every $\mathscr T_{\mu,\eta}$-conull subset of $X$ has Hausdorff dimension $s$. Thus one finite measure is selected once, and the entire universal quantifier over competitors is replaced by a classical conull dimension-essentiality condition. The measure need not be carried by $X$; in the necessity proof it can be a finite atomic measure with countable dense support. This last point is what lets the theorem survive Bernstein sets and explains why ordinary Frostman formulations looked too restrictive.

The factor $2^{\eta r}$ is not decoration. It converts a linear $\eta r$ saving in description length into covering cost. A Kraft competitor that saves $\varepsilon r$ infinitely often produces a limsup set of zero $\mathscr T_{\mu,\eta}$-measure for each $0 < \eta < \varepsilon$. Conversely, if $\mathscr T_{\mu,\eta}(Y) = 0$, arbitrarily cheap fine covers of $Y$ can be pooled, with total Kraft mass at most one, into a single competitor saving essentially $\eta r$ at infinitely many scales at every point of $Y$. This two-way “Kraft–Carathéodory duality” is the new step that collapses (MC).

The final statement of this theorem contains only a finite Borel measure, dyadic local exponents, Method-II outer measures, and Hausdorff dimension. It may be described as a spatially adaptive, multifractal exactness condition. Ordinary exact gauges and Stull’s measure hypotheses remain important sufficient ways to produce optimality.

## 1. Fundamentals

### 1.0 Provenance of terms / symbols / concepts / constructions here

The report mixes established definitions with new names for proposed equivalences.

| Term or result | Status and source |
| --- | --- |
| Hausdorff/packing oracle; optimal Hausdorff/packing oracle; preservation set $N(A, B, \varepsilon)$ | By Stull (2021/2022). |
| Prefix-free ball code and its induced complexity; rational-ball reduction; encoding a rational code in an oracle; ball-versus-point comparison | By Miyabe (2026). |
| Discrete and continuous semimeasures, Method-II outer measures, net/mesh semimeasures, prefix outer measure $\kappa$, and local optimality of outer measures | Standard AIT/GMT vocabulary; and cites Lutz–Lutz papers. |
| Multifractal Hausdorff measures $\mathcal{H}_\mu^{q,t}$ | By Olsen. Formula (T) is the dyadic-net, $q=1,t=-\eta$ specialization. |
| Choquet capacity, maxitive measure, sup-measure, possibility measure, and cardinal density | Established capacity/maxitive-measure terminology; but conventions can vary in the literature. |
| **Hausdorff-robust ball code**, **rational Kraft ball system**, **dimension-essentially locally optimal capacity**, **Hausdorff-dimension-essential outer measure**, **positive-tilt net outer measure**, and **Kraft–Carathéodory duality** | New. |
| Theorems A–E, the $G_X$ notation, the “tagged join” notation, and “local subpower domination” as the description of the set-specific condition | New. But their prefixing and Method-II constructions, together with the subexponential-domination idea, are standard. |
| “Proposed” theorems in this report | New. |

### 1.1 Hausdorff and packing dimension

For $E \subseteq \mathbb{R}^n$, $s \geq 0$, and $\delta > 0$, the **$s$-dimensional Hausdorff content at scale $\delta$** is

$$
\mathcal{H}^s_\delta(E) = \inf \left\{ \sum_i (\operatorname{diam} U_i)^s : E \subseteq \bigcup_i U_i,\ \operatorname{diam} U_i \leq \delta \right\}.
$$

The **$s$-dimensional Hausdorff outer measure** is $\mathcal{H}^s(E) = \lim_{\delta \downarrow 0} \mathcal{H}^s_\delta(E)$, and **Hausdorff dimension** is

$$
\dim_H E = \inf \left\{ s : \mathcal{H}^s(E) = 0 \right\} = \sup \left\{ s : \mathcal{H}^s(E) = \infty \right\}.
$$

Packing dimension, denoted $\dim_P E$, may be defined via packing measures or as the countably stable modification of upper box dimension. One always has

$$
\dim_H E \leq \dim_P E.
$$

A set is called **weakly regular** when the two match: $\dim_H E=\dim_P E$.

I think there is also something to be said about having exact dimension, here.

### 1.2 Finite-precision complexity and effective dimensions

Fix a universal prefix-free oracle machine $\mathscr{U}$. For an oracle $A \subseteq \mathbb{N}$, a point $x \in \mathbb{R}^n$, and $r \in \mathbb{N}$, put

$$
K_r^A(x) = \min \left\{ K_{\mathbf{U}}^A(q) : q \in \mathbb{Q}^n,\ \lVert q - x \rVert < 2^{-r} \right\}.
$$

The **lower and upper information densities** relative to $A$ are

$$
\dim^A(x) = \liminf_{r \to \infty} \frac{K_r^A(x)}{r}, \qquad \operatorname{Dim}^A(x) = \limsup_{r \to \infty} \frac{K_r^A(x)}{r}.
$$

The lower quantity is **effective Hausdorff dimension**; the upper quantity is **effective packing dimension** (a.k.a., strong dimension).

The **point-to-set principle** of J. Lutz and N. Lutz states

$$
\dim_H X = \min_A \sup_{x \in X} \dim^A(x), \qquad \dim_P X = \min_A \sup_{x \in X} \operatorname{Dim}^A(x). \tag{P2S}
$$

An oracle attaining the first minimum is a **Hausdorff oracle** for $X$; one attaining the second is a **packing oracle**.

Being a Hausdorff oracle is a robust property under Turing joins: i.e., if $A$ is a Hausdorff oracle and $B$ is arbitrary, then $A\oplus B$ is also a Hausdorff oracle. Indeed, extra information cannot increase point complexity, while (P2S) supplies the opposite set-level inequality:

$$
s = \sup_{x \in X} \dim^A(x) \geq \sup_{x \in X} \dim^{A, B}(x) \geq s.
$$

Consequently, for every $\varepsilon>0$, some $x\in X$ has

$$
\dim^{A, B}(x) \geq s - \varepsilon \geq \dim^A(x) - \varepsilon.
$$

This only yields a complexity-preservation inequality at infinitely many ($\exists^\infty$) scales. It does not yield it eventually at every ($\forall^\infty$) scale.

### 1.3 Stull’s optimal oracles

In *Optimal Oracles for Point-to-Set Principles*, first posted in 2021 and published at STACS 2022, Don Stull defined $A$ to be **Hausdorff optimal for $X$** when it satisfies two conditions.

- **[WITNESS]** $A$ is a Hausdorff oracle for $X$.
- **[FITNESS]** For every oracle $B$ and every $\varepsilon>0$, there is an $x\in X$ such that
    
    $$
    \dim^{A, B}(x) \geq \dim_H X - \varepsilon
    $$
    
    and
    
    $$
    K_r^{A, B}(x) \geq K_r^A(x) - \varepsilon r \quad \text{for all sufficiently large } r. \tag{OO}
    $$
    

“For almost every $r \in \mathbb{N}$” is to be understood in the recursion-theoretic sense $\forall^\infty r$: all but finitely many $r$. We might isolate the points satisfying (OO) into their own set:

$$
N_X(A, B, \varepsilon) = \left\{ x \in X : (\forall^\infty r)\; K_r^{A, B}(x) \geq K_r^A(x) - \varepsilon r \right\}.
$$

Stull’s Proposition 4 gives the important reformulation when $s = \dim_H X > 0$:

$$
A \text{ is optimal} \iff A \text{ is Hausdorff and } (\forall B)(\forall \varepsilon)\; \dim_H N_X(A, B, \varepsilon) = s.
$$

Thus, for each fixed pair $(B, \varepsilon)$, any witness point $x$ can be strengthened to a full-dimensional family of witness points.

This does **not** mean that every point of $X$ works, nor that there is one fixed full-dimensional subset working simultaneously for all $B$. The witness set can depend on both $B$ and $\varepsilon$. For example, with $X=[0,1]$ and a trivial oracle $A = \varnothing$, a “competitor” oracle $B$ could encode one particular ML-random point $x$; even though $x$ fails (OO), still a full-dimensional set of other points survives.

[Note: The packing definition is identical except that $A$ must be a packing oracle and $\operatorname{Dim}^{A, B}(x)$ replaces $\dim^{A, B}(x)$.]

Let’s also fix the absolute-continuity condition he sets for metric outer measures: he needs something like “every $\mu$-conull subset of $X$ has full Hausdorff dimension”: i.e., $0 < \mu(X) < \infty$ while either

$$
\begin{cases} \mu \ll \mathcal{H}^{s - \delta} \quad (\forall \delta > 0), \text{ or}\\ \mathcal{H}^s \ll \mu \quad \wedge \quad \mathcal{H}^s(X) > 0. \end{cases}
$$

We might refer to this whole condition as **$\mu$ being Hausdorff-fit for $X$**.

We’ll say that $X$ **has an exact Hausdorff gauge** if there exists a gauge function $h$ for which $0 < \mathcal{H}^h(X) < \infty$.

## 2. Characterizing having optimal oracles

Call $\mathsf{HOHO}$ the condition of having optimal Hausdorff oracles, $\mathsf{HOPO}$ the same for packing, and $\mathsf{HOO}$ for both.

Stull already proved the following sufficient conditions.

- Every analytic set ($\mathbf{\Sigma}^1_1$), hence every Borel set ($\mathbf{\Delta}^1_1$) $\models \mathsf{HOO}$.
- Every weakly regular set (i.e., Hausdorff and packing dimensions agree) $\models \mathsf{HOO}$.
- If there is a metric outer measure which is Hausdorff-fit for $X$, then $X \models \mathsf{HOHO}$.
- Stull states that having an exact Hausdorff gauge (whose “lower order” agrees with $\dim_H X$) also implies $\models \mathsf{HOHO}$.
- Assuming the axiom of determinacy (AD), every $X \models \mathsf{HOHO}$.
    - This uses the theorem of Crone–Fishman–Jackson that every set has a Borel subset of equal Hausdorff dimension.
- Assuming the axiom of choice (AC) and the continuum hypothesis (CH), we can construct examples satisfying:
    - $\exists X : X \not\models \mathsf{HOHO} \quad \wedge \quad X \models \mathsf{HOPO}$
    - $\exists X : X \models \mathsf{HOHO} \quad \wedge \quad X \not\models \mathsf{HOPO}$
    - $\exists X : X \not\models \mathsf{HOHO} \quad \wedge \quad X \not\models \mathsf{HOPO}$

Stull’s proof for the Hausdorff-fit outer measures is especially revealing. From $\mu$, he assigns to a dyadic cube $Q_{r,i}$ a summable weight proportional to

$$
\text{weight}(Q_{r,i}) \propto \frac{\mu(X\cap Q_{r,i})}{r^2\mu(X)}.
$$

This is a discrete semimeasure. Levin-type coding dominance then shows that the set on which an additional oracle saves $\varepsilon r$ bits infinitely often has $\mu$-measure zero. The absolute-continuity hypotheses convert “$\mu$-null exceptional set” into “full Hausdorff dimension remains.”

### 2.1 Progress

The most directly relevant advance is Kenshi Miyabe’s *Ball codes: A coding characterization of Hausdorff and packing dimensions*, posted 30 August 2026. Miyabe proves a completely classical point-to-set-style formula in terms of arbitrary ball codebooks, with no machines or computability. He then recovers the algorithmic point-to-set principle by rationalizing a minimizing code and storing its countable codebook in an oracle.

Miyabe explicitly distinguishes “an oracle attaining the point-to-set minimum” from Stull’s stronger “optimal oracle” and writes that a classical characterization of the latter in the ball-code model is left open.

Later applications make the class more important but do not characterize it. Examples include Fiedler–Stull on universal projection sets and the 2026 Fiedler–Jing $k$-plane projection theorem, which proves Kaufman-type exceptional-set estimates for sets with optimal oracles.

Raymond Tana’s 2025 dissertation, *The Algorithmic Theory of Information and its Applications to Geometric Measure Theory*, develops precisely the surrounding infrastructure: semimeasures, point-to-set principles for Hausdorff measures, net spaces, net semimeasures, and local/global optimality of outer measures. In particular, its Chapters 4–5 compare incompressibility, semimeasure, outer-measure, and net-cover viewpoints. This strongly motivates looking for a summable-cover or capacity formulation rather than merely replacing one universal machine by another.

## 3. Miyabe’s classical ball codes

A **prefix-free ball code** was defined by Miyabe as a partial map $\varphi : \subset 2^{<\omega} \to \mathcal{B}$ defined on a prefix-free domain, where $\mathcal{B}$ is the family of positive-radius closed balls in $\mathbb{R}^n$. Define the **coding complexity function for $\varphi$:**

$$
L^\varphi_r(x) = \min \left\{ |p| : \varphi(p) \mathbin{\downarrow} \ni x \ \wedge \ \operatorname{diam} \varphi(p) \leq 2^{-r} \right\},
$$

with value $+\infty$ if there is no such name. Miyabe denotes this quantity $K_\varphi(x;r)$.

This is deliberately a very permissive object. Its domain is countable even though the codomain $\mathcal{B}$ is uncountable. There is no topological requirement that nearby or extension-related names denote nearby or nested balls.

Fix the **lower and upper coding complexity ratios for $\varphi$** as follows:

$$
\operatorname{bcdim}_\varphi(x) = \liminf_{r \to \infty} \frac{L^\varphi_r(x)}{r}, \qquad \operatorname{bcDim}_\varphi(x) = \limsup_{r \to \infty} \frac{L^\varphi_r(x)}{r}.
$$

Miyabe writes these as $\dim_\varphi$ and $\operatorname{Dim}_\varphi$. We avoid overloading those symbols even further!

What Miyabe’s ball codes contribute to the AIT-GMT story is recasting the point-to-set principle in terms of ball codes. This isn’t very surprising: this essentially isolates and classicalizes a geometric coding mechanism already latent in the Lutz–Lutz point-to-set proof.

<aside>

**Theorem**. Miyabe’s **ball code point-to-set principle**. 

$$
\begin{aligned} \dim_H X &= \min_\varphi \sup_{x \in X} \operatorname{bcdim}_\varphi(x), \\ \dim_P X &= \min_\varphi \sup_{x \in X} \operatorname{bcDim}_\varphi(x). \tag{BC} \end{aligned}
$$

where both minima are attained. And it suffices for the minimizing code to take values among **rational closed balls**

$$
\overline{B}(q, \delta), \qquad q \in \mathbb{Q}^n, \quad \delta \in \mathbb{Q}_{> 0}.

$$

</aside>

- simple argument for PTS?
    
    An AI wrote this and I don’t quite understand it.
    
    - For an arbitrary code $\varphi$, if $t$ exceeds the right-hand supremum, then every $x\in X$belongs at arbitrarily fine scales to a coded ball $\varphi(p)$ satisfying $|p|<tr$. Consequently,
        
        $$
        \operatorname{diam}(\varphi(p))^t
        \leq 2^{-tr}
        <2^{-|p|}.
        $$
        
        The sufficiently long such codewords cover $X$, while the corresponding $t$-cost is bounded by a tail of the Kraft sum. Those tails tend to zero, so $\mathcal H^t(X)=0$.
        
    - Conversely, take $t_k\downarrow\dim_H X$ and increasingly fine rational-ball covers whose $t_k$-costs are at most $2^{-k}$. Give each ball a prefix-free name of length approximately
        
        $$
        -\log_2!\left(\operatorname{diam}(B)^{t_k}\right).
        $$
        
        Kraft–Chaitin applies because the combined requested mass is at most $\sum_k2^{-k}$. Every $x\in X$ then receives descriptions at infinitely many precisions with asymptotic rate at most $t_k$, hence at most $\dim_H X$.
        
    
    So we cannot avoid the lower asymptotic rate itself—it is the pointwise quantity in the theorem—but we can avoid introducing $\operatorname{bcdim}$ as an additional layer of terminology.
    
    Your historical diagnosis is also basically right. The original Lutz–Lutz proof says that its minimizing oracle encodes increasingly refined Hausdorff covers, after which a point is
    described by specifying a sufficiently small cover element. That is precisely the ball-code construction with the codebook moved out of the oracle and made explicit.
    
    That gives Miyabe appropriate credit without making the result sound more conceptually surprising than it is. Miyabe himself observes that the rational-ball theorem can be recovered from the point-to-set principle, although that recovery does not reproduce his direct proof. His genuinely valuable additions are the clean classical formulation, rational-ball reduction, explicit attainment result, and especially the packing theorem, whose $\limsup$ direction requires modified upper box dimension rather than the easy sparse-scale Hausdorff argument. See Miyabe’s discussion and Remark 1.2.
    

Let $\mathfrak{B}_{\mathbb{Q}}$ denote the class of all prefix-free codes of rational closed balls. Then the minima in the theorem quantify over $\varphi \in \mathfrak{B}_{\mathbb{Q}}$.

Let’s refer to any $\varphi$ which witnesses $\dim_H X$ to be a **Hausdorff ball code for $X$**, and similar for $\dim_P X$ a **packing ball code for $X$**.

These rational closed balls serve as a countable geometric base for quantifying over $\varphi$.

For two codes $\varphi$ and $\psi$, let’s introduce a **tagged join** notation

$$
(\varphi \vee \psi)(0p) = \varphi(p), \qquad (\varphi \vee \psi)(1q) = \psi(q),
$$

so

$$
L^{\varphi \vee \psi}_r(x) = \min \left\{ L^\varphi_r(x), L^\psi_r(x) \right\} + 1.
$$

That is, searching for a short codeword over a tagged union decomposes into searching over either component code, with little overhead.

## 4. Equivalent characterization of $\mathsf{HOHO}$ via ball codes

### 4.1 Robust minimizing ball codes

Inspired by the definition of optimal oracles via Kolmogorov complexity, let’s define a corresponding property via classical ball codes and their corresponding coding complexity functions.

**Definition.** We say that $X$ **has optimal Hausdorff rational ball codes** ($\models \mathsf{HOHRBC}$) if there exists a ball code $\varphi \in \mathfrak{B}_{\mathbb{Q}}$ satisfying the following two conditions.

The code $\varphi$ is a Hausdorff ball code for $X$; i.e.,

$$
\sup_{x \in X} \operatorname{bcdim}_\varphi(x) = s. \tag{M}
$$

And, for every $\psi \in \mathfrak{B}_{\mathbb{Q}}$ and every $\varepsilon > 0$, there is an $x \in X$ such that

$$
\operatorname{bcdim}_\varphi(x) \geq s - \varepsilon, \qquad \operatorname{bcdim}_\psi(x) \geq s - \varepsilon. \tag{H}
$$

and

$$
L^\psi_r(x) \geq L^\varphi_r(x) - \varepsilon r \quad (\forall^\infty r). \tag{P}
$$

Note that if $\psi$ is a poor code that omits fine balls, its codelength complexities are large, trivially satisfying the preservation condition ($\text{P}$). This condition is harder to meet for alternate ball codes which describe many points more cheaply.

The first inequality in ($\text{H}$) is worth stating even though the reverse proof of Theorem A uses only the second. For Stull’s oracle witness it is automatic: adjoining $B$ cannot increase complexity, so high $\dim^{A, B}(x)$ forces high $\dim^A(x)$. For arbitrary static codebooks $\varphi$ and $\psi$ there is no such monotonicity, so it would *not* follow merely from (M), the second inequality in ($\text{H}$), and ($\text{P}$). In the forward proof we recover it by passing through the joined universal code $\mathbf{U}^{A \oplus B}$, which simulates both $\mathbf{U}^A$ and the encoded $\psi$. Including it therefore records the full oracle fact and does not change the equivalence.

The special case of $s > 0$ requires another analogous definition. For $\varphi, \psi \in \mathfrak{B}_{\mathbb{Q}}$ and $\varepsilon > 0$, isolate the points satisfying ($\text{P}$) into their own set:

$$
G_X(\varphi, \psi, \varepsilon) = \left\{ x \in X : (\forall^\infty r)\; L^\psi_r(x) \geq L^\varphi_r(x) - \varepsilon r \right\}.
$$

### 4.2 The equivalence

<aside>

**Theorem A.** $X \models \mathsf{HOHO} \iff X \models \mathsf{HOHRBC}$.

</aside>

For positive dimension there is an equivalent strengthening analogous to optimal oracles:

<aside>

**Theorem B.** If $s = \dim_H X > 0$, then a Hausdorff ball code $\varphi$ for $X$ is an optimal Hausdorff rational ball code for $X$ if and only if

$$
(\forall \psi \in \mathfrak{B}_{\mathbb{Q}})(\forall \varepsilon > 0)\; \dim_H G_X(\varphi, \psi, \varepsilon) = s. \tag{FD}
$$

</aside>

## 5. Proof of the robust ball-code theorem

Intuitively, from any optimal Hausdorff oracle we can build a PFBC on $\mathcal{B}_{\mathbb{Q}}$ by using the same universal prefix-free oracle machine $\mathbf{U}$ (whose outputs are rational closed balls) as Miyabe does and by defining $\varphi := \mathbf{U}^A$. In the reverse direction, from any optimal Hausdorff PFBC $\varphi$ we can encode it into an oracle $A$. Either construction yields an optimal Hausdorff object in the appropriate sense.

### 5.1 A uniform ball-code/point-complexity comparison

(We may as well assume that $\mathbf{U}$ also fixes a universal oracle machine mapping programs to rational points.)

The key relation to prove is the asymptotic equivalence between Kolmogorov complexity and ball code complexity under the universal oracle machine:

<aside>

**Proposition.** For every oracle $A \subseteq \mathbb{N}$, precision level $r \in \mathbb{N}$, and point $x \in \mathbb{R}^n$,

$$
L^{\mathbf{U}^A}_r(x) = K_r^A(x) \pm o(r)
$$

</aside>

Or, more sharply:

<aside>

**Uniform comparison lemma.** There is a constant $c$, depending only on the ambient dimension $n$ and the fixed optimal machine $\mathbf{U}$, such that for every $A, r, x$:

$$
K_r^A(x) - c \leq L^{\mathbf{U}^A}_r(x) \leq K_r^A(x) + 2K(r) + c. \tag{1}
$$

</aside>

Intuitively, $L^{\mathbf{U}^A}_r(x)$ captures the minimum length of a $\mathbf{U}^A$-program whose output is a rational closed ball containing $x$ and having diameter at most $2^{-r}$. The central claim here is that this quantity roughly matches $K^A_r(x)$: the minimum length $\mathbf{U}^A$-program required to describe a rational point within the open ball of radius $2^{-r}$ about $x$. This is a standard geometric argument.

**Note.** One could introduce alternate notation, say, $\Xi^A_r(x) := L^{\mathbf{U}^A}_r(x)$, for the complexity of naming a rational closed ball of diameter at most $2^{-r}$ that contains $x$ using $\mathbf{U}^A$-programs. Still, $\Xi^A_r(x) = K^A_r(x) \pm o(r)$.

We use Miyabe’s Proposition 5.7 to prove this lemma.

- **Proof of the uniform comparison lemma.**
    
    Miyabe proves (Proposition 5.7), with constants independent of $A, x, r$, that
    
    $$
    K_r^A(x) \leq L^{\mathbf{U}^A}_r(x) + O(1) \tag{2}
    $$
    
    while
    
    $$
    \begin{aligned} L^{\mathbf{U}^A}_r(x) &\leq K_{r + 1}^A(x) + K(r) + c_1 \tag{3}\\ &\leq K_r^A(x) + 2 \cdot K(r) + c_2 \end{aligned}
    $$
    
    $\square$
    

<aside>

**Corollary [Miyabe’s Corollary 5.8].** For every $A, x$,

$$
\begin{aligned} \liminf_r \frac{L^{\mathbf{U}^A}_r(x)}{r} &= \dim^A(x), \\ \limsup_r \frac{L^{\mathbf{U}^A}_r(x)}{r} &= \operatorname{Dim}^A(x). \tag{5} \end{aligned}
$$

</aside>

We might view this as yet another asymptotic agreement for effective dimension.

<aside>

**Corollary [eventual complexity achievement / preservation relation].**
For any oracles $A, B$ and complexity rate $\eta \geq 0$, if

$$
K_r^B(x) \geq K_r^A(x) - \eta r \quad (\forall^\infty r) \tag{6}
$$

then

$$
L^{\mathbf{U}^B}_r(x) \geq L^{\mathbf{U}^A}_r(x) - \eta r - 2K(r) - O(1) \quad (\forall^\infty r). \tag{7}
$$

</aside>

- **Proof of the eventual complexity-achievement corollary.**
    
    Apply the left-hand inequality of the uniform comparison lemma to oracle $B$ and the right-hand inequality to oracle $A$. $\square$
    

A similar proof gives the converse:

<aside>

**Corollary [eventual complexity achievement, converse].**
For any oracles $A, B$ and complexity rate $\eta \geq 0$, if

$$
L^{\mathbf{U}^B}_r(x) \geq L^{\mathbf{U}^A}_r(x) - \eta r \quad (\forall^\infty r). \tag{8}
$$

then

$$
K_r^B(x) \geq K_r^A(x) - \eta r - 2K(r) - O(1) \quad (\forall^\infty r). \tag{9}
$$

</aside>

Hence, for any $\delta > \eta$, (6) implies (8) with $\delta$ in place of $\eta$, and (8) implies (6) with the same enlargement.

<aside>

**Corollary [PTS].** For any $A \subseteq \mathbb{N}$ and $x \in X$,.

$$
\operatorname{bcdim}_{\mathbf{U}^A}(x) = \dim^A(x)
$$

Consequently, and since it suffices to minimize over rational ball covers,

$$
\dim_H X = \min_\varphi \sup_{x \in X} \operatorname{bcdim}_\varphi(x)
$$

Here the minimum ranges over prefix-free ball codes $\varphi$.

</aside>

### 5.2 Every rational code can be stored in an oracle

In his Lemma 5.4, Miyabe shows how to encode the domain and graph of any rational ball code into an oracle. Let $\varphi \in \mathfrak{B}_{\mathbb{Q}}$ be so encoded by the oracle $A$. Then $\mathbf{U}$ may simulate it with constant overhead:

$$
L^{\mathbf{U}^A}_r(x) \leq L^\varphi_r(x) + O_\varphi(1). \tag{ENC}
$$

And adjoining an arbitrary oracle $B$ does not prevent the universal machine from simulating $\varphi$:

$$
L^{\mathbf{U}^{A,B}}_r(x) \leq L^\varphi_r(x) + O_\varphi(1). \tag{ENCJ}
$$

Conversely, for each oracle $A$, the map $\pi \mapsto \mathbf{U}^A(\pi)$ is itself a prefix-free rational ball code.

### 5.3 Optimal oracle implies robust code

Assume $A$ is an optimal Hausdorff oracle for $X$. Let

$$
\varphi := \mathbf{U}^A
$$

be its universal rational ball code.

- **Witness condition.**
    
    By Miyabe’s **ball code point-to-set principle**, the **uniform comparison lemma**, and the witness condition that $A$ satisfies as a Hausdorff oracle for $X$:
    
    $$
    \begin{aligned} s \leq \sup_{x \in X} \operatorname{bcdim}_\varphi(x) &= \sup_{x \in X} \liminf_r \frac{L^\varphi_r(x)}{r}\\ &\leq \sup_{x \in X} \liminf_r \frac{K_r^A(x)}{r} = \sup_{x \in X} \dim^A(x) = s. \end{aligned}
    $$
    
    so $\varphi$ really is a Hausdorff ball code for $X$.
    
- **Fitness condition.**
    
    Fix a rational ball code $\psi$ and $\varepsilon > 0$. Let $B$ encode $\psi$, and consider the code
    
    $$
    \theta = \mathbf{U}^{A,B}.
    $$
    
    Let $\delta = \varepsilon/4$. Then, using the **uniform comparison lemma**, the fitness condition of $A$ as a Hausdorff oracle for $X$ gives a point $x \in X$ such that
    
    $$
    \begin{aligned} \operatorname{bcdim}_\theta(x) &= \liminf_r \frac{L^{\mathbf{U}^{A, B}}_r(x)}{r}\\ &\geq \liminf_r \frac{K^{A, B}_r(x)}{r}\\ &= \dim^{A, B}(x)\\ &\geq s - \delta. \end{aligned}
    $$
    
    (By (ENCJ), both $\operatorname{bcdim}_\varphi(x)$ and $\operatorname{bcdim}_\psi(x)$ are also at least $\operatorname{bcdim}_\theta(x) \geq s - \delta$.)
    
    Moreover, for all but finitely many $r \in \mathbb{N}$, the comparison corollary and (ENCJ) give
    
    $$
    \begin{aligned} L^{\psi}_r(x) &\geq L^\theta_r(x) - O(1)\\ &= L^{\mathbf{U}^{A, B}}_r(x) - O(1)\\ &\geq K^{A, B}_r(x) - O(1)\\ &\geq K^A_r(x) - \delta r - O(1)\\ &\geq L^\varphi_r(x) - \delta r - 2K(r) - O(1). \end{aligned}
    $$
    
    Since $2K(r) + O(1) = o(r)$, we have
    
    $$
    L^\psi_r(x) \geq L^\varphi_r(x) - \varepsilon r \quad (\forall^\infty r).
    $$
    
    Thus $\varphi$ is an optimal Hausdorff rational ball code for $X$.
    

### 5.4 Robust code implies optimal oracle

Assume now that $\varphi$ is an optimal Hausdorff rational ball code for $X$. Encode $\varphi$ into an oracle $A$, and let

$$
\Phi = \mathbf{U}^A.
$$

- **Witness condition.**
    
    Universality of $\mathbf{U}$ gives
    
    $$
    L^\Phi_r(x) \leq L^\varphi_r(x) + O(1) \tag{BASE}
    $$
    
    Combine this with the witness condition from $\varphi$ being a Hausdorff ball code for $X$ and Miyabe’s ball-code point-to-set principle:
    
    $$
    s \leq \sup_{x \in X} \operatorname{bcdim}_\Phi(x) \leq \sup_{x \in X} \operatorname{bcdim}_\varphi(x) = s.
    $$
    
    By the uniform comparison lemma, it follows that
    
    $$
    \sup_{x \in X} \dim^A(x) = \sup_{x \in X} \operatorname{bcdim}_\Phi(x) = s.
    $$
    
    Thus, $A$ is a Hausdorff oracle for $X$.
    
- **Fitness condition.**
    
    Fix any oracle $B$ and $\varepsilon > 0$. The code
    
    $$
    \theta = \mathbf{U}^{A,B}
    $$
    
    is a rational ball code, so the fitness condition of $\varphi$ as a Hausdorff ball code for $X$, applied with $\delta = \varepsilon/3$, gives an $x \in X$ such that
    
    $$
    \operatorname{bcdim}_\theta(x) \geq s - \delta
    $$
    
    and, using (BASE), for all but finitely many $r \in \mathbb{N}$,
    
    $$
    \begin{aligned} L^\theta_r(x) &\geq L^\varphi_r(x) - \delta r \\ &\geq L^\Phi_r(x) - \delta r - O(1). \tag{P2} \end{aligned}
    $$
    
    By the corollary **Eventual complexity achievement, converse**,
    
    $$
    K_r^{A, B}(x) \geq K_r^A(x) - \delta r - 2K(r) - O(1) \quad (\forall^\infty r).
    $$
    
    Absorbing these $o(r)$ terms into $\varepsilon r$, we have
    
    $$
    \begin{aligned} K_r^{A, B}(x) &\geq K_r^A(x) - \varepsilon r \quad (\forall^\infty r),\\ \dim^{A, B}(x) &= \operatorname{bcdim}_\theta(x) \geq s - \delta > s - \varepsilon. \end{aligned}
    $$
    
    Thus, $A$ is an optimal Hausdorff oracle for $X$.
    

### 5.5 Proof of the full-dimensional form

Assume $s > 0$.

Given $(\forall \psi \in \mathfrak{B}_{\mathbb{Q}})(\forall \varepsilon > 0)\; \dim_H G_X(\varphi, \psi, \varepsilon) = s$, let’s prove that $\varphi$ is an optimal Hausdorff rational ball code for $X$.

- **Witness condition.**
    
    We already have that $\varphi$ is a Hausdorff rational ball code for $X$.
    
- **Fitness condition.**
    
    Fix $\psi$ and $\varepsilon$, and put $G = G_X(\varphi, \psi, \varepsilon)$. By Miyabe’s point-to-set principle on $G$,
    
    $$
    s = \dim_H G \leq \sup_{x \in G} \operatorname{bcdim}_{\varphi \vee \psi}(x).
    $$
    
    Thus, there is some $x \in G$ satisfying $\operatorname{bcdim}_{\varphi \vee \psi}(x) \geq s - \varepsilon$. This trivially implies the same lower bound for $\operatorname{bcdim}_{\varphi}(x)$ and $\operatorname{bcdim}_{\psi}(x)$ since $L_{\varphi \vee \psi} = \min \{ L_\varphi, L_\psi \} + 1$.
    
    Conversely, suppose $\varphi$ is an optimal Hausdorff rational ball code for $X$, but for some $\psi, \varepsilon$ we have
    
    $$
    d := \dim_H G_X(\varphi, \psi, \varepsilon) < s.
    $$
    
    The fitness condition for $\varphi$ already implies $G_X(\varphi, \psi, \varepsilon) \neq \varnothing$.
    
    Then, by Miyabe’s PTS principle, we may pick a rational minimizing ball code $\gamma$ for it, and then form the tagged join
    
    $$
    \theta := \psi \vee \gamma.
    $$
    
    Take $\delta$ such that
    
    $$
    0 < 3\delta < \min \{ \varepsilon, s - d \}.
    $$
    
    Then, by the fitness condition of $\varphi$ against $\theta$ and $\delta$, there exists $x \in X$ with
    
    $$
    \operatorname{bcdim}_\theta(x) \geq s - \delta
    $$
    
    and
    
    $$
    L^\theta_r(x) \geq L^\varphi_r(x) - \delta r \quad (\forall^\infty r). \tag{10}
    $$
    
    If $x \in G_X(\varphi, \psi, \varepsilon)$, then
    
    $$
    s - \delta \leq \operatorname{bcdim}_\theta(x) \leq \operatorname{bcdim}_\gamma(x) \leq d < s - \delta,
    $$
    
    a contradiction. Otherwise, $x \notin G_X(\varphi, \psi, \varepsilon)$, in which case
    
    $$
    \begin{aligned} L^\theta_r(x) &\geq L^\varphi_r(x) - \delta r && (\forall^\infty r),\\ L^\theta_r(x) &\leq L^\psi_r(x) + 1 < L^\varphi_r(x) - \varepsilon r + 1 && (\exists^\infty r), \end{aligned}
    $$
    
    a contradiction for large $r$ because $\delta < \varepsilon$. This concludes the argument.
    

This proof is the ball-code analogue of Stull’s proof that one optimal witness entails a full-dimensional preservation set.

## 6. Removing codewords: robust Kraft covers

The robust ball-code theorem can be stated without finite strings.

### 6.1 Kraft ball systems

A **rational Kraft ball system** is a countable family

$$
\mathcal{C} = \left\{ (B_i, \ell_i) \in \mathcal{B}_{\mathbb{Q}} \times \mathbb{N} : i \in I \right\}, \qquad \sum_{i \in I} 2^{-\ell_i} \leq 1.
$$

We may associate to any rational Kraft ball system a corresponding complexity function over reals:

$$
L^{\mathcal{C}}_r(x) = \min \left\{ \ell_i : x \in B_i \ \wedge \ \operatorname{diam} B_i \leq 2^{-r} \right\}.
$$

Any prefix-free rational ball code $\varphi$ induces a rational Kraft ball system $\mathcal{C} = \set{(\varphi(\sigma), \lvert \sigma \rvert) : \sigma \in \operatorname{dom}(\varphi)}$. Under this association, the complexity functions agree: $L^\varphi_r(x) = L^{\mathcal{C}}_r(x)$. 

Conversely, the **countable Kraft–McMillan theorem** assigns pairwise prefix-incomparable binary strings of lengths $\ell_i$, giving a standard way to build from any Kraft ball system a prefix-free ball code with exactly the same coding complexity function $L^{\mathcal{C}}_r(x)$. 

> AI-generated: **Countable Kraft–McMillan.** Let $(\ell_i)_{i \in I}$ be a countable family of natural numbers with $\sum_i 2^{-\ell_i} \leq 1$. Each length occurs at most $2^\ell$ times, so $I$ can be listed as $i_0, i_1, \ldots$ with $\ell_{i_0} \leq \ell_{i_1} \leq \cdots$. Put $S_j := \sum_{k < j} 2^{-\ell_{i_k}}$ and let $\sigma_{i_j}$ be the first $\ell_{i_j}$ bits of the binary expansion of $S_j$. Because the lengths are nondecreasing, $S_j$ is a multiple of $2^{-\ell_{i_j}}$, so $\sigma_{i_j}$ names the dyadic interval $[S_j, S_j + 2^{-\ell_{i_j}})$. These intervals are disjoint, so the strings $\sigma_i$ are pairwise prefix-incomparable. Setting $\varphi(\sigma_i) := B_i$ gives a prefix-free rational ball code with $L^\varphi_r = L^{\mathcal{C}}_r$ exactly.
> 

Consequently, Theorems A and B remain true verbatim with rational ball codes replaced by rational Kraft ball systems.

<aside>

**Theorem C (rational Kraft ball systems).** A nonempty $X \subseteq \mathbb{R}^n$ has an optimal Hausdorff oracle iff there is a rational Kraft ball system $\mathcal{C}$ with 

$$
\sup_{x \in X} \liminf_r \frac{L^{\mathcal{C}}_r(x)}{r} = s
$$

such that, for every rational Kraft ball system $\mathcal{D}$ and every $\varepsilon > 0$, some $x \in X$ satisfies

$$
\liminf_{r \to \infty} \frac{L^{\mathcal{D}}_r(x)}{r} \geq s - \varepsilon \qquad \text{and} \qquad L^{\mathcal{D}}_r(x) \geq L^{\mathcal{C}}_r(x) - \varepsilon r \quad (\forall^\infty r).
$$

If $s > 0$, this is equivalent to $\dim_H G_X(\mathcal{C}, \mathcal{D}, \varepsilon) = s$ for all $\mathcal{D}$ and $\varepsilon$, with $G_X$ defined as in §4.1 using $L^{\mathcal{C}}$ and $L^{\mathcal{D}}$.

</aside>

### 6.2 Weighted-cover formulation

For a fixed rational Kraft ball system, write $w_i = 2^{-\ell_i}$ and define its **weighted-cover profile**:

$$
M^{\mathcal{C}}_r(x) = \sup \left\{ w_i : x \in B_i \ \wedge \ \operatorname{diam} B_i \leq 2^{-r} \right\}.
$$

clearly satisfying:

$$
L^{\mathcal{C}}_r(x) = -\log_2 M^{\mathcal{C}}_r(x).
$$

Then at a given point $x$, we say $\mathcal{C}$ satisfies the “preservation inequality” if for each $\mathcal{D}$ and $\varepsilon > 0$:

$$
M^{\mathcal{D}}_r(x) \leq 2^{\varepsilon r} \cdot M^{\mathcal{C}}_r(x) \quad (\forall^\infty r). \tag{11}
$$

**Note**: We might picture $M^{\mathcal{C}}_r(x)$ as a maximal function on ball scale-space: put an atom of mass $w_i$ at each ball $B_i$, and then take the supremal atom size among balls containing $x$ below scale $2^{-r}$.

### 6.3 Normalization to one dyadic tree [slop]

But the arbitrary-ball formulation is not essential. 

There is a dimensional constant $N =O_n(1)$ such that every ball $B$ can be covered by at most $N$ dyadic cubes whose circumscribed rational balls have diameter no larger than $\operatorname{diam} B$. Let $\mathcal{C}'$ be a new rational Kraft ball system with $B$ replaced by these at most $N$ balls, assigning each a weight of $w(B)/N$. The total Kraft budget cannot increase, while

$$
M^{\mathcal{C}'}_r(x) \geq \frac{1}{N} \cdot M^{\mathcal{C}}_r(x). \tag{DN}
$$

Similar can be done in the reverse direction.

It follows that Theorems A–C remain equivalent if both the minimizing system and all competitors are restricted to weighted members of one fixed dyadic tree. Indeed:

- normalizing an optimal base system makes its profile larger up to a fixed multiplicative constant, hence makes the required domination inequality easier and preserves its minimizing exponent;
- to test an arbitrary competitor, normalize it first. A point that has high lower rate for the stronger normalized competitor also has high lower rate for the original competitor, and domination of the normalized competitor transfers back with a constant loss.

If $Q_r(x) \in \mathcal{Q}^n_r$ is the unique half-open dyadic cube at precision $2^{-r}$ containing $x$, then its local profile is $M^w_r(x) := \sup\{ w(Q) : x \in \widehat{B}_Q,\ \operatorname{rk} Q \geq r + c_n \}$, which is literally a Kraft ball system.

## 7. Capacity characterization

### 7.1 Capacities

Inspired by Choquet’s classical theory of capacities, we’ll let a **capacity** be any set function $C : \mathcal{P}(\mathbb{R}^n) \to [0, +\infty]$ which satisfies:

- $C(\varnothing) = 0$;
- **Monotonicity**: $E \subseteq F \implies C(E) \leq C(F)$;
- **Continuity from below**: $E_i \uparrow E \Longrightarrow C(E_i) \uparrow C(E)$ for arbitrary increasing sets; and
- **Continuity from above**: $K_i \downarrow K \Longrightarrow C(K_i) \downarrow C(K)$ for decreasing compact sets.

That is, a capacity [a monotone set function with these continuity properties] is a premeasure on $X$ satisfying some extra montonicity and continuity properties. A capacity is not necessarily an outer measure, since we can’t guarantee subadditivity.

A capacity is described as:

- **Finitely maxitive** if:
    
    $$
    C(E \cup F) = \max \{ C(E), C(F) \}
    $$
    
- **$\sigma$-finitely maxitive** if:
    
    $$
    C\left(\bigcup_{i = 1}^\infty E_i \right) = \sup_i C(E_i)
    $$
    
- **Completely maxitive** if:
    
    $$
    C\left(\bigcup E_i \right) = \sup_i C(E_i)
    $$
    
     over arbitrary unions. 
    
- **Normalized** if $C(X) = 1$.

It may happen that a capacity has a point density function $g$, i.e.: 

$$
C(E) = \sup_{x \in E} g(x),
$$

In that case, the capacity must be completely maxitive and an outer measure. We may call such $C$ a **possibility measure** and $g$ its possibility distribution. 

### 7.2 From Discrete Semimeasures to Set Functions

A single discrete semimeasure $m : \mathbb{Q}^n \to [0, \infty)$ induces two natural set functions:

$$
\mu_m(E) = \sum_{q \in E \cap \mathbb{Q}^n} m(q) \quad\text{and}\quad \Pi_m(E) = \sup_{q \in E \cap \mathbb{Q}^n} m(q). \tag{SS}
$$

The first is the usual additive atomic measure. The second is actually a maxitive capacity, as we’ll discuss later. The two set functions for $m$ agree on singleton masses and always satisfy $\Pi_m(E) \leq \mu_m(E)$, but they can differ greatly on, say, a ball containing many atoms.

<aside>

**Claim**. $\Pi_m$ is a capacity function. 

</aside>

- **Proof**.
    - **Compact upper semicontinuity**:
        
        Given a density function $g$, let its **$t$-superlevel set** be: 
        
        $$
        \set{x \in X : g(x) \geq t}.
        $$
        
        Given $m$, which is summable, we may bound the size of the $t$-superlevel set of $g_m$:
        
        $$
        \lvert \set{q \in \mathbb{Q}^n : m(q) \geq t} \rvert \leq \frac{1}{t}, \quad (\forall t > 0).
        $$
        
        That is, each of its positive superlevel sets is finite and thus closed. 
        
        So, if $K_i \downarrow K$ are compact, then 
        
        $$
        \Pi_m(K_i) = \max_{x \in K_i} g_m(x) \downarrow \Pi_m(K).
        $$
        
    - **Lower semicontinuity**:
        
        Follows directly from complete maxitivity.
        
- Alternative statement
    
    <aside>
    
    **Lemma.** Let $C : \mathcal{P}(\mathbb{R}^n) \to [0, \infty]$ and put $g(x) := C(\{x\})$.
    
    1. $C$ is completely maxitive iff $C(E) = \sup_{x \in E} g(x)$ for every $E$.
    
    Any completely maxitive $C$ further satisfies:
    
    1. $C$ is a countably subadditive outer measure that is continuous from below along arbitrary increasing sequences.
    2. $C$ is continuous from above along decreasing sequences of compact sets iff $g$ is upper semicontinuous.
    3. If $m : \mathbb{Q}^n \to [0, 1]$ has $\sum_{q \in \mathbb{Q}^n} m(q) \leq 1$, let $g_m$ equal $m$ on $\mathbb{Q}^n$ and $0$ elsewhere. Then $g_m$ is upper semicontinuous, so $\Pi_m$ is a completely maxitive Choquet capacity.
    </aside>
    
    - **Proof**
        1. Write $E = \bigcup_{x \in E} \{x\}$. The converse follows from properties of suprema. 
        2. This follows from $\sup_{\bigcup_i E_i} g = \sup_i \sup_{E_i} g$.
        3. Suppose $g$ is upper semicontinuous, $K_i \downarrow K$ are compact, and $C(K) < t < \inf_i C(K_i)$. Each $K_i$ then contains a point with $g > t$. The superlevel set $\{g \geq t\}$ is closed by upper semicontinuity, so the sets $K_i \cap \{g \geq t\}$ are nonempty, compact, and decreasing. Their intersection $K \cap \{g \geq t\}$ is therefore nonempty, so $C(K) \geq t$, a contradiction. Conversely, continuity along $\overline{B}(x, 1/i) \downarrow \{x\}$ gives $\limsup_{y \to x} g(y) \leq \lim_i C(\overline{B}(x, 1/i)) = g(x)$.
        4. For $t > 0$, the set $\{g_a \geq t\}$ has at most $1/t$ elements and is therefore closed. For $t \leq 0$ it is all of $\mathbb{R}^n$. $\square$

Thus, $\Pi_m$ is a possibility measure with possibility distribution $g_m = m \circ \mathbf{1}_{\mathbb{Q}^n}$. Let’s call $\Pi_m$ a **summable rational possibility measure**. 

But it’s not additive, in general. If separated sets $E, F$ both have positive capacity under $\Pi_m$, then

$$
\Pi_m(E \cup F) = \max \{ \Pi_m(E), \Pi_m(F) \} \neq \Pi_m(E) + \Pi_m(F).
$$

It is therefore not a metric outer measure, in general.

Recall that we can define the lower local dimension of a locally finite outer measure $\mu$ as follows:

$$
\dim_{\mathrm{loc}}\mu(x) = \liminf_{r\to\infty}
\frac{-\log_2\mu(B_{2^{-r}}(x))}{r}.
$$

(This is the Billingsley-type formula I use in my dissertation in Chapter 4). It’s the same used by Lutz and Lutz for outer measures. They refer to it as the classical local fractal dimension of an outer measure. We can therefore consider this quantity for the outer measure $\Pi_m$:

$$
\begin{aligned}
\dim_{\mathrm{loc}}\Pi_m(x) &= \liminf_r \frac{-\log_2\Pi_m(B_{2^{-r}}(x))}{r} \\
&= \liminf_r \frac{-\log_2\sup_{y \in B_{2^{-r}}(x)} g_m(y)}{r}\\
&= \liminf_r \inf_{q \in B_{2^{-r}}(x) \cap \mathbb{Q}^n} \frac{-\log_2 m(q)}{r}
\end{aligned}
$$

In particular, recall by **Levin’s Coding Theorem** that the optimal discrete semimeasure relative to $A$ satisfies: $-\log_2 \mathbf{m}^A(\sigma) = K^A(\sigma) \pm O(1)$, so under the choice $m := \mathbf{m}^A$, we have

$$
\dim_{\operatorname{loc}} \Pi_{\mathbf{m}^A}(x) = \dim^A(x).
$$

Whereas the discrete semimeasure $m(q) := 2^{-K(q)}$ produces N. Lutz’s prefix outer measure: 

$$
\Pi_m(E) = \kappa(E) := 2^{-\min \{ K(q) : q \in E \cap \mathbb{Q}^n \}}.
$$

[Contrast this with $R(E) := \sum_{q \in E} 2^{-K(q)}$, which corresponds to the additive $\mu_m$ set function for the same $m$.]

Put another way: for an oracle $A$, put $a_A(q) := 2^{-K^A(q)}$. Kraft's inequality gives $\Pi_{a_A} \in \mathfrak{P}$. Writing $K^A(E) := \min \left\{ K^A(q) : q \in E \cap \mathbb{Q}^n \right\}$, we have

$$
\Pi_{a_A}(E) = 2^{-K^A(E)} = \boldsymbol{\kappa}^A(E),
$$

the relativized prefix outer measure. Since $K^A_r(x) = K^A(B(x, 2^{-r}))$ with $B$ open,

$$
L^{\Pi_{a_A}}_r(x) = K^A_r(x) \qquad \text{for all } A, x, r. \tag{KC}
$$

### 7.3 A possibility-capacity point-to-set principle

This part keeps the draft's notation, with two additions:

$$
L^\Pi_r(x) := -\log_2 \Pi(B(x, 2^{-r})), \qquad L^\mu_r(x) := -\log_2 \mu(Q_r(x)),
$$

where $B(x, \rho)$ is the *open* ball and $-\log_2 0 = +\infty$. These parallel $L^\varphi_r(x)$ and $L^{\mathcal{C}}_r(x)$. Competitor Kraft ball systems are called $\mathcal{E}$, to avoid the clash with the dyadic net $\mathcal{D}$.

Let $\mathfrak{P}$ be the class of set functions $\Pi_a$ with $a : \mathbb{Q}^n \to [0, 1]$ and $\sum_q a(q) \leq 1$.

**Theorem (P2SC).** For every $E \subseteq \mathbb{R}^n$,

$$
\dim_H E = \min_{\Pi \in \mathfrak{P}} \sup_{x \in E} \liminf_{r \to \infty} \frac{L^\Pi_r(x)}{r}.
$$

- Old statement
    
    For every $E \subseteq \mathbb{R}^n$,
    
    $$
    \dim_H E = \min_{\Pi_m} \sup_{x \in E} \dim_{\mathrm{loc}}\Pi_m(x). \tag{P2SC}
    $$
    

**Lower bound.** Fix $\Pi = \Pi_a \in \mathfrak{P}$, let $\alpha$ be the right-hand supremum for $\Pi$, and let $t > \alpha$. In particular $t > 0$. Let $S := \{ q : a(q) > 0 \}$, a countable set. For $x \in E \setminus S$ there are infinitely many $r$ with $L^\Pi_r(x) < tr$, that is, rationals $q_r$ with

$$
|x - q_r| < 2^{-r} < a(q_r)^{1/t}.
$$

Since $q_r \to x$ and $q_r \neq x$, and each set $\{q : a(q) \geq c\}$ with $c > 0$ is finite and does not contain $x$, we get $a(q_r) \to 0$. So for every $\delta > 0$,

$$
E \setminus S \subseteq \bigcup \left\{ B(q, a(q)^{1/t}) : q \in S,\ a(q) < \delta^t \right\},
$$

and therefore

$$
\mathcal{H}^t_{2\delta}(E \setminus S) \leq \sum_{a(q) < \delta^t} \bigl( 2 a(q)^{1/t} \bigr)^t = 2^t \sum_{a(q) < \delta^t} a(q) \xrightarrow[\delta \to 0]{} 0.
$$

The last sum is the tail of a convergent series, because only finitely many $q$ have $a(q) \geq \delta^t$. Thus $\mathcal{H}^t(E \setminus S) = 0$. Also $\mathcal{H}^t(S) = 0$, since $S$ is countable and $t > 0$. Hence $\dim_H E \leq t$.

Removing $S$ is necessary: if $x$ is itself an atom, the witnessing atom can be $x$ at every scale, and the balls do not shrink.

**Attainment.** Put $s := \dim_H E$, $t_m := s + 1/m$, and $R_m := m^2$. Since $\mathcal{H}^{t_m}(E) = 0$, we can cover $E$ by open balls $B_{m,j}$ with

$$
0 < d_{m,j} := \operatorname{diam} B_{m,j} \leq 2^{-R_m}, \qquad \sum_j d_{m,j}^{\,t_m} \leq 1
$$

Choose $q_{m,j} \in B_{m,j} \cap \mathbb{Q}^n$, and set

$$
a(q) := \sum_{\{(m,j) : q_{m,j} = q\}} 2^{-m} d_{m,j}^{\,t_m},
$$

so that $\sum_q a(q) \leq \sum_m 2^{-m} \leq 1$. Now fix $x \in E$ and $m$. Pick $j$ with $x \in B_{m,j}$, write $d := d_{m,j}$, and let $r := \lfloor \log_2(1/d) \rfloor \geq R_m$. Two points of an open ball of diameter $d$ lie at distance $< d \leq 2^{-r}$, so $q_{m,j} \in B(x, 2^{-r})$ and

$$
\frac{L^{\Pi_a}_r(x)}{r} \leq \frac{m + t_m \log_2(1/d)}{r} < \frac{m + t_m (r+1)}{r} \leq t_m + \frac{m + t_m}{m^2}.
$$

As $m \to \infty$, these scales satisfy $r \geq m^2 \to \infty$ and the bounds tend to $s$. Hence $\liminf_r L^{\Pi_a}_r(x)/r \leq s$. $\square$

### 7.4 Dimension-essential local domination

For two summable possibility capacities $\Pi, \Lambda$, define the **local subpower-domination set**:

$$
W_X(\Pi, \Lambda, \varepsilon) = \left\{ x \in X : (\forall^\infty r)\; \Lambda(B(x, 2^{-r})) \leq 2^{\varepsilon r} \cdot \Pi(B(x, 2^{-r})) \right\}. \tag{W}
$$

Let’s call $\Pi$ **dimension-essentially locally optimal for $X$** if it attains (P2SC) for $X$ and, for every $\Lambda$ and every $\varepsilon > 0$, the set in (W) has full Hausdorff dimension in $X$.

**Theorem D (maxitive-capacity characterization).** Let $X \subseteq \mathbb{R}^n$ be nonempty and $s = \dim_H X > 0$. Then $X$ has an optimal Hausdorff oracle if and only if it admits a dimension-essentially locally optimal summable rational possibility capacity.

For all $s \geq 0$, including zero, the equivalent witness formulation is: there is a minimizing $\Pi$ such that for every $\Lambda$ and every $\varepsilon > 0$, some $x \in X$ satisfies

$$
\dim_{\mathrm{loc}}\Pi_m(x) \geq s - \varepsilon, \qquad \dim_{\mathrm{loc}}\Lambda_m(x) \geq s - \varepsilon. \tag{CH}
$$

and

$$
\Lambda(B(x, 2^{-r})) \leq 2^{\varepsilon r} \cdot \Pi(B(x, 2^{-r})) \quad (\forall^\infty r). \tag{CP}
$$

### 7.5 Proof of Theorem D

Suppose first that $A$ is an optimal Hausdorff oracle for $X$, and let $\Pi := \Pi_{a_A}$. Equation (KC) says that $\Pi$ attains (P2SC).

Fix an arbitrary summable possibility capacity $\Lambda := \Pi_b$. Round its nonzero weights down to dyadic numbers. Kraft–McMillan gives a prefix code that names each rational $q$ at length $\lceil \log_2(1/b(q)) \rceil$. Store this code in an oracle $B$. Universality then gives, for a constant $c$,

$$
\Pi_{a_{A, B}}(E) \geq 2^{-c} \cdot \Lambda(E) \quad (E \subseteq \mathbb{R}^n). \tag{C1}
$$

The joined oracle can also simulate the base oracle, so for another constant $c'>0$,

$$
\Pi_{a_{A, B}}(E) \geq c' \cdot \Pi(E) \quad (E \subseteq \mathbb{R}^n). \tag{C1b}
$$

Apply optimality of $A$ with a smaller tolerance $\delta$. In capacity notation it supplies $x \in X$ with lower local capacity dimension at least $s - \delta$ for $\Pi_{a_{A, B}}$ and

$$
\Pi_{a_{A, B}}(B(x, 2^{-r})) \leq 2^{\delta r} \cdot \Pi(B(x, 2^{-r})) \quad (\forall^\infty r). \tag{C2}
$$

The high local dimension of $\Pi_{a_{A, B}}$, together with (C1) and (C1b), gives the two inequalities in (CH). Equations (C1)–(C2), with constants absorbed into $(\varepsilon - \delta)r$, give (CP) for $\Lambda$.

Conversely, suppose $\Pi := \Pi_a$ has the witness property. Kraft-code the weights $a(q)$ and store the code in an oracle $A$. For some $c > 0$, universality gives

$$
\Pi_{a_A}(E) \geq c \cdot \Pi(E) \quad (E \subseteq \mathbb{R}^n). \tag{C3}
$$

Thus $\operatorname{capdim}_{\Pi_{a_A}}(x) \leq \operatorname{capdim}_\Pi(x)$ pointwise. Since $\Pi$ minimizes (P2SC), the ordinary point-to-set lower bound forces

$$
\sup_{x \in X} \dim^A(x) = s,
$$

so $A$ is a Hausdorff oracle.

Now fix any oracle $B$ and use $\Lambda := \Pi_{a_{A, B}}$ in (CH)–(CP). Combining (CP) with (C3) gives

$$
\Pi_{a_{A, B}}(B(x, 2^{-r})) \leq c^{-1} \cdot 2^{\delta r} \cdot \Pi_{a_A}(B(x, 2^{-r})) \quad (\forall^\infty r).
$$

Taking negative logarithms and using (KC) yields

$$
K_r^{A, B}(x) \geq K_r^A(x) - \delta r - O(1),
$$

while (CH) is the required high-$\dim^{A, B}$ clause. Absorbing the constant proves that $A$ is optimal.

For $s > 0$, the passage from the witness formulation to full dimension is the same tagged-join argument as in Theorem B, now internal to maxitive capacities. If a good set in (W) were empty, the witness formulation against its defining competitor would immediately produce a point in it. Otherwise let $\Pi_c$ minimize (P2SC) for that good set. If $b$ and $c$ are the competitor and good-set weight functions, then

$$
h(q) = \tfrac{1}{2} \cdot \max \{ b(q), c(q) \}.
$$

is summable and $\Pi_h = \tfrac{1}{2} \cdot \max \{ \Pi_b, \Pi_c \}$. Choose $\delta$ smaller than both the gap in dimension and $\varepsilon$, then apply the witness property against $\Pi_h$. A witness inside the good set has $\Pi_h$-local dimension at most the smaller good-set dimension; a witness outside it violates preservation infinitely often through the $\Pi_b/2$ term. Thus neither location is possible.

Conversely, if (W) has full dimension, apply the lower-bound half of (P2SC) on $W_X(\Pi, \Lambda, \varepsilon)$ to the summable capacity $\tfrac{1}{2} \cdot \max \{ \Pi, \Lambda \}$. A point of local dimension at least $s - \varepsilon$ for this maximum has local dimension at least $s - \varepsilon$ for both $\Pi$ and $\Lambda$, hence satisfies (CH). This proves the full-dimensional form.

### 7.6 Implications of Theorem D

Theorem D identifies the nonadditive capacity suggested by the Kraft profile. The relevant operation is a supremum, not a sum: finite-precision complexity is the negative logarithm of the largest rational atom in a small ball. The preservation inequality is exactly **local subpower domination**,

$$
\Lambda(B(x, \rho)) \leq \rho^{-\varepsilon} \cdot \Pi(B(x, \rho))
$$

along all sufficiently small dyadic radii, on a full-dimensional set that may depend on $\Lambda$ and $\varepsilon$.

This is close to Lutz and Lutz’s established notion of local optimality for outer measures. Their locally optimal $\kappa$ subpower-dominates every lower-semicomputable strongly finite outer measure uniformly on all dyadic cubes. Theorem D removes computability, restricts competitors to summable maxitive capacities, and replaces uniform ambient domination by domination along centered balls on a full-dimensional, competitor-dependent portion of $X$. The resulting condition is set-specific and exactly matches Stull optimality.

## 8. Positive-tilt net outer measures

AI: “It turns out that competing outer measures can be absorbed into the null ideals of a one-parameter family of additive-cover outer measures. This makes the final witness a single finite Borel measure.”

I think Stull’s gauges and construction of Hausdorff outer measures is done over the half-open dyadic cubes. Doing fractal geometry over a restricted class of base sets is something I consider in my dissertation for meshes and nets. Here, we focus on the net $\mathcal{Q}^m$  of half-open dyadic cubes in Euclidean space. We already have notation for the unique cube $Q_r(x) \in \mathcal{Q}^m_r$ at layer $r$ containing $x$, and could reintroduce $\operatorname{rk}(Q)$ or $\operatorname{depth}(Q)$ as the layer $r$ in which $Q \in \mathcal{Q}^m_r$. This should serve as a layered-disjoint net in my parlance, and also be understandable as a layered disjoint system (LDS) in published speak. 

The following definition of what the agent called “lower dyadic local capacity dimension” of a finite Borel measure $\mu$ is probably recastable as a standard lower dimension of $\mu$ when restricted to this net $\mathcal{Q}^m$ (just a net-local version of the usual lower local dimension of a measure). 

$$
\liminf_{r \to \infty} \frac{-\log_2 \mu(Q_r(x))}{r}
$$

If $s, q > 0$, we might build a premeasure defined only over $\mathcal{Q}^m$ almost exactly as Olsen does (need a ref):

$$
\rho^\mu_{s, q}(Q) := \operatorname{diam}(Q)^s \cdot \mu(Q)^q = m^{-s/2} \cdot 2^{-s \cdot \operatorname{rk}(Q)} \cdot \mu(Q)^q.
$$

Then, let’s consider the Method II metric outer measure corresponding to $\rho^\mu_{s, q}$, which must use cover elements from $\operatorname{dom}(\rho^\mu_{s, q}) = \mathcal{Q}^m$:

$$
\begin{aligned}
\mathcal{H}^{\rho^\mu_{s,q}}(X) &:= \sup_{\delta > 0} \inf_{ (Q_i)_i \subset \mathcal{Q}^m} \left\{\sum_{i \in \omega} \rho^\mu_{s,q}(Q_i) :  \operatorname{diam}(Q_i) \leq \delta, \bigcup_{i \in \omega} Q_i \supseteq X \right\} \\
&= \lim_{r \to \infty} \inf_{(Q_i)_i \subset \mathcal{Q}^m} \left\{\sum_{i \in \omega} m^{-s /2} \cdot 2^{-s \cdot r_i} \cdot \mu(Q_i)^q : r_i \geq r, \bigcup_{i \in \omega} Q_i \supseteq X \right\}.
\end{aligned} 
$$

There’s a suggestion to call this as a **positive-tilt outer measure** for $\mu$, but not sure why.

Satisfies: 

- $\mathcal{H}^{\rho^\mu_{s',q}} \leq \mathcal{H}^{\rho^\mu_{s,q}}$ for all $s \leq s'$. So “null ideals”(?) grow with $s$. [what's the importance of this?]
- $\mathcal{H}^{\rho^\mu_{s,q}} \geq \mu^*$ (what’s the asterisk mean?), so the $\mathcal{H}^{\rho^\mu_{s,q}}$-null implies being $\mu$-null; i.e., $\mu \ll \mathcal{H}^{\rho^\mu_{s,q}}$ (I think). (How do you know?)

### 8.2 The Kraft–Carathéodory null-ideal lemma

The core argument is easiest before passing to a Borel measure. A **dyadic Kraft weight** is a function $a : \mathcal{D} \to [0,1]$ satisfying

$$
\sum_{Q \in \mathcal{D}} a(Q) \leq 1. \tag{DK}
$$

It is exactly a discrete semimeasure on the countable dyadic net. Define

$$
L^a_r(x) = -\log_2 a(Q_r(x))
$$

and, for two Kraft weights $a, b$ and $\varepsilon > 0$,

$$
\operatorname{Bad}_\varepsilon(a, b) = \left\{ x : b(Q_r(x)) > 2^{\varepsilon r} \cdot a(Q_r(x)) \text{ for infinitely many } r \right\}. \tag{BAD}
$$

Thus $\operatorname{Bad}_\varepsilon(a, b)$ is the set on which $b$ saves $\varepsilon r$ bits over $a$ infinitely often. Define $\mathscr T_{a,\eta}$ by (PT) with $a(Q)$ in place of $\mu(Q)$.

**Lemma (Kraft–Carathéodory null-ideal duality).** Let $a$ be a dyadic Kraft weight. The following two statements hold.
**(KC1)** If $b$ is another dyadic Kraft weight and $0 < \eta < \varepsilon$, then\mathscr T_{a,\eta}(\operatorname{Bad}_\varepsilon(a, b)) = 0. \tag{KC1}
**(KC2)** If $\mathscr T_{a,\eta}(Y) = 0$, then there is a dyadic Kraft weight $b$ such thatY \subseteq \operatorname{Bad}_\eta(a, b). \tag{KC2}

**Proof of (KC1).** At rank $r$, cover the bad event by those cubes satisfying $b(Q) > 2^{\varepsilon r} \cdot a(Q)$. For every $m$ their total tilted cost is at most

$$
\begin{split} \sum_{r \geq m} \sum_{\substack{Q \in \mathcal{D}_r \\ b(Q) > 2^{\varepsilon r} \cdot a(Q)}} 2^{\eta r} \cdot a(Q) &\leq \sum_{r \geq m} 2^{-(\varepsilon-\eta)r} \sum_{Q \in \mathcal{D}_r} b(Q) \\ &\leq \sum_{r \geq m} 2^{-(\varepsilon-\eta)r}. \end{split} \tag{14}
$$

The last expression tends to zero. This is the Hausdorff–Cantelli half of the duality.

**Proof of (KC2).** For each $j$, choose a cover $\mathcal{C}_j$ of $Y$ by cubes of ranks at least $j$ such that

$$
\sum_{Q \in \mathcal{C}_j} 2^{\eta \operatorname{rk}(Q)} \cdot a(Q) \leq 2^{-j-1}.
$$

Set

$$
b(Q) = \sum_{\{ j : Q \in \mathcal{C}_j \}} 2^{\eta \operatorname{rk}(Q)} \cdot a(Q). \tag{15}
$$

Then $\sum_Q b(Q) \leq 1$. If $x \in Y$, for every $j$ some $Q_j \in \mathcal{C}_j$ contains $x$, and

$$
b(Q_j) \geq 2^{\eta \operatorname{rk}(Q_j)} \cdot a(Q_j).
$$

Since $\operatorname{rk}(Q_j) \geq j$, these inequalities occur at unbounded ranks. After changing a non-strict inequality or a total mass equal to one by an immaterial constant factor, $x \in \operatorname{Bad}_\eta(a, b)$. This proves (KC2).

Consequently, after allowing arbitrarily small changes of the positive exponent,

$$
\bigcup_{\eta > 0} \{ Y : \mathscr T_{a,\eta}(Y) = 0 \}
$$

is exactly the ideal of sets that can be targeted at a fixed positive linear rate by one Kraft competitor. This is the promised elimination of the universal competitor: the adversarial quantifier is already encoded in the null sets of the tilted Carathéodory measures.

Two failed simplifications are now transparent.

- The untilted construction $\mathscr T_{a,0}$ cannot detect a linear saving.
- A single subexponential multiplier, such as $2^{\sqrt{r}}$, is also insufficient. A null cover for that cost yields only an $o(r)$ saving, whereas nonoptimality requires $\varepsilon r$ for one fixed $\varepsilon > 0$. The family of all positive exponential tilts is the exact scale.

### 8.3 Replacing a Kraft weight by one finite Borel measure

The preceding lemma is already classical covering theory, but its witness $a$ still looks like a semimeasure. It can be replaced, with only sublinear loss, by an ordinary finite Borel measure.

For an oracle $A$, let $K^A(q)$ denote prefix complexity of a rational point and put

$$
\mu_A = \sum_{q \in \mathbb{Q}^n} 2^{-K^A(q)} \cdot \delta_q. \tag{16}
$$

Selecting one shortest program for each rational and applying Kraft’s inequality shows that $\mu_A(\mathbb{R}^n) \leq 1$. Thus $\mu_A$ is a finite, purely atomic Borel measure with dense support. This is Tana’s additive prefix outer measure $R$, viewed as a Borel measure on its countable support, rather than the maxitive prefix measure $\kappa$.

Let $C^A(Q)$ be the length of a shortest $A$-program that outputs the index of the dyadic cube $Q$. There is a constant $c$, independent of $A, Q, r$, such that, for $Q \in \mathcal{D}_r$,

$$
2^{-C^A(Q) - c} \leq \mu_A(Q) \leq 2^{K(r) + c} \cdot 2^{-C^A(Q)}. \tag{17}
$$

For the first inequality, a cube description outputs a fixed rational point in that cube with constant overhead. For the second, the masses $\{ \mu_A(Q) : Q \in \mathcal{D}_r \}$ have sum at most one and are lower semicomputable relative to $A$. Shannon–Fano coding at rank $r$, with a self-delimiting description of $r$, gives

$$
C^A(Q) \leq -\log_2 \mu_A(Q) + K(r) + O(1),
$$

which is (17). This is the concrete sum/sup comparison underlying the locally optimal-outer-measure discussion in Lutz–Lutz and Tana: on a fixed dyadic layer, the sum of all rational prefix atoms in $Q$ and the largest effective cube weight differ by at most $2^{o(r)}$.

There is also a uniform cube/point comparison

$$
C^Z(Q_r(x)) = K_r^Z(x) + O(\log(r + 2)). \tag{18}
$$

for every oracle $Z$ and point $x$. In one direction, the center of $Q_r(x)$ is an approximation to $x$, with a constant shift in precision. In the other, an $r$-approximation to $x$ meets only $O_n(1)$ rank-$r$ dyadic cubes; after describing $r$, a constant-size index selects $Q_r(x)$. The constant precision shift is removed by the refinement estimate from Section 5.1. This is the cube-index version of the Case–Lutz dyadic-rational comparison quoted as Lemma 11 in Stull; the formulation here makes its uniform $O(\log r)$ content explicit. Combining (17) and (18) gives

$$
\operatorname{capdim}_{\mu_A}^{\mathcal{D}}(x) = \dim^A(x). \tag{19}
$$

It also shows why replacing the maxitive capacity by $\mu_A$ does not lose the all-large-scales information: the discrepancy is $O(\log r)$, not merely an equality of limiting dimensions.

More generally, multiplication of cube prices by $2^{o(r)}$ does not change the union of the positive-tilt null ideals. A small portion of the exponent absorbs the sub-linear factor. Thus (17) transfers the null-ideal lemma from the Kraft profile to the Borel measure $\mu_A$.

### 8.4 The tilted-measure characterization

Call a finite non-zero Borel measure $\mu$ **positively Hausdorff-essential on $X$** if, for every $\eta > 0$,

$$
N \subseteq X, \quad \mathscr T_{\mu,\eta}(N) = 0 \quad\Longrightarrow\quad \dim_H(X \setminus N) = \dim_H X. \tag{PHE}
$$

Equivalently, every subset of $X$ that is conull for $\mathscr T_{\mu,\eta}$ has full Hausdorff dimension. This is the tilted analogue of the dimension-essential outer-measure condition in Section 9.1.

**Theorem E (tilted-measure characterization).** Let $X \subseteq \mathbb{R}^n$ be nonempty and let $s = \dim_H X > 0$. The following are equivalent.

**(i)** The set $X$ has an optimal Hausdorff oracle.

**(ii)** There is a finite non-zero Borel measure $\mu$ such that

$$
\sup_{x \in X} \operatorname{capdim}_\mu^{\mathcal{D}}(x) = s \tag{20}
$$

and $\mu$ is positively Hausdorff-essential on $X$.

When $s = 0$, the corresponding witness form is obtained by replacing (PHE) by $\mathscr T_{\mu,\eta}(X) > 0$ for every $\eta > 0$.

#### Necessity

Let $A$ be an optimal Hausdorff oracle and take $\mu := \mu_A$ from (16). Equation (19) and the fact that $A$ is Hausdorff-minimizing give (20).

Fix $\eta > 0$ and suppose $N \subseteq X$ satisfies $\mathscr T_{\mu_A,\eta}(N) = 0$. Choose cheap covers as in the proof of (KC2), and assign to each selected cube the weight

$$
2^{\eta \operatorname{rk}(Q)} \cdot \mu_A(Q).
$$

Pooling the covers with summable outer coefficients gives one dyadic Kraft weight $b$. Round its nonzero values down to dyadic powers (losing a factor of at most two), apply Kraft–McMillan, and encode the resulting prefix code in an oracle $B$. At every $x \in N$ and at unbounded ranks $r$,

$$
\begin{split} C^{A, B}(Q_r(x)) &\leq -\log_2 b(Q_r(x)) + O(1) \\ &\leq -\log_2 \mu_A(Q_r(x)) - \eta r + O(1) \\ &\leq C^A(Q_r(x)) - \eta r + O(1), \end{split} \tag{21}
$$

where the last inequality uses the left side of (17). By (18), after reducing $\eta$ slightly, $N$ lies in Stull’s bad preservation set $D$ for $(A, B)$. If $s > 0$, Proposition 4 says that the good preservation set $X \setminus D$ has dimension $s$. Since $N \subseteq D$,

$$
X \setminus D \subseteq X \setminus N,
$$

so $\dim_H(X \setminus N) = s$, which is (PHE). Notice that this does **not** assert that $D$, or $N$, has dimension below $s$; disjoint subsets can both have full Hausdorff dimension. At $s = 0$, if $\mathscr T_{\mu_A,\eta}(X) = 0$, the same construction would defeat preservation at every point of $X$, contradicting the witness form of optimality. This proves necessity in both cases.

#### Sufficiency

Conversely, normalize $\mu(\mathbb{R}^n) \leq 1$ and let

$$
\pi_r = \frac{6}{\pi^2(r + 1)^2}.
$$

The cube weights

$$
a_\mu(Q) = \pi_{\operatorname{rk}(Q)} \cdot \mu(Q) \tag{22}
$$

satisfy

$$
\sum_{Q \in \mathcal{D}} a_\mu(Q) = \sum_r \pi_r \sum_{Q \in \mathcal{D}_r} \mu(Q) \leq 1.
$$

Round (22) down to dyadic powers and use an oracle $A$ to store the resulting Kraft code. The factor-two loss is constant. Universality gives

$$
C^A(Q) \leq -\log_2 \mu(Q) + O(\log(r + 2)) \qquad (Q \in \mathcal{D}_r). \tag{23}
$$

Equations (18), (20), and (23) imply

$$
\sup_{x \in X} \dim^A(x) \leq s.
$$

The point-to-set principle gives the reverse inequality for every oracle, so $A$ is a Hausdorff oracle for $X$.

Now fix an oracle $B$ and $\varepsilon > 0$. Let $w_{A, B}(Q) := 2^{-C^{A, B}(Q)}$; after an inessential constant normalization this is a dyadic Kraft weight. Consider the cube-version bad set on which

$$
C^{A, B}(Q_r(x)) < C^A(Q_r(x)) - \varepsilon r
$$

infinitely often. By (22)–(23), on a bad rank-$r$ cube,

$$
\mu(Q) \cdot 2^{\eta r} \leq C \cdot \pi_r^{-1} \cdot 2^{-(\varepsilon - \eta)r} \cdot w_{A, B}(Q) \tag{24}
$$

for any $0 < \eta < \varepsilon$. Summing (24) over bad cubes and then over $r \geq m$ gives a tail bounded by

$$
C \cdot \sum_{r \geq m} (r + 1)^2 \cdot 2^{-(\varepsilon - \eta)r},
$$

which tends to zero. The bad set is therefore $\mathscr T_{\mu,\eta}$-null.

If $s > 0$, (PHE) says directly that its complement in $X$ has full Hausdorff dimension. Applying the point-to-set lower bound to that complement relative to $A \oplus B$ supplies a point of $\dim^{A, B}$ arbitrarily close to $s$. Equation (18) transfers the eventual cube preservation inequality back to $K_r$. Formally, run the cube argument with a smaller tolerance, say one-third of the requested tolerance, and absorb the two $O(\log r)$ comparison errors. This proves optimality. If $s = 0$, positivity of $\mathscr T_{\mu,\eta}(X)$ says the bad set cannot be all of $X$, and any point in its complement supplies the required witness. This proves Theorem E.

### 8.5 The intrinsic null-ideal statement

Define the positive-tilt null ideal of $\mu$ by

$$
\mathcal{N}_\mu^+ = \bigcup_{\eta > 0} \{ Y \subseteq \mathbb{R}^n : \mathscr T_{\mu,\eta}(Y) = 0 \}.
$$

Each null family at a fixed $\eta$ is a $\sigma$-ideal. Their union over $\eta > 0$ is an ideal under subsets and finite unions, but need not be a $\sigma$-ideal: a countable sequence of witnessing exponents may decrease to zero.

Also define the family of dimension-harmless deletions from $X$ by

$$
\mathcal{R}_s(X) = \{ N \subseteq X : \dim_H(X \setminus N) = s \}.
$$

Unlike $\mathcal{N}_\mu^+$, the ambient family $\mathcal{R}_s(X)$ need not be an ideal: intersections of two full-dimensional sets can have smaller dimension. The content of the theorem is that the particular ideal of positive-tilt null sets lies inside this deletion-harmless family.

For $s > 0$, Theorem E can be compressed to the following classical statement:

$$
\boxed{ \begin{gathered} \exists \text{ a finite Borel measure } \mu \text{ with } \sup_{x \in X} \operatorname{capdim}_\mu^{\mathcal{D}}(x) = s, \\ \mathcal{N}_\mu^+ \cap \mathcal{P}(X) \subseteq \mathcal{R}_s(X). \end{gathered}} \tag{25}
$$

This is the promised necessary-and-sufficient condition with no oracle, program, finite string, prefix code, or competing capacity in its statement. It says that every positive-tilt-null deletion for one dimension-minimizing measure is harmless to the Hausdorff dimension of $X$.

Two sanity checks fix the direction of the tilt.

- If $X \subseteq \mathbb{R}^n$ has full ambient Hausdorff dimension $n$, take Lebesgue measure. Then $\mu(Q) = 2^{-nr}$ and $\mathscr T_{\mu,\eta}$ is, up to normalization, dyadic $\mathcal{H}^{n-\eta}$. A null set for this measure has dimension at most $n - \eta$, so removing it from an $n$dimensional $X$ leaves dimension $n$. Thus (20)–(PHE) hold. This includes a full-dimensional Bernstein set even though it carries no positive-dimensional Frostman measure.
- If $X = \{x\}$, take $\mu = \delta_x$. Its local exponent at $x$ is zero and the cost of the unique rank-$r$ cube containing $x$ is $2^{\eta r}$. Hence $\mathscr T_{\mu,\eta}(X) > 0$ (indeed it is infinite), matching the zero-dimensional witness clause.

It is important that (25) quantifies over all subsets of $X$, not merely Borel subsets. That is exactly where set theory enters. Under determinacy, every set has a full-dimensional Borel core and Stull obtains optimality. Under AC + CH, Stull’s nonoptimal examples imply the following completely classical failure: for every finite measure satisfying the local-exponent equality, some positive tilt has a null subset $N\subseteq X$ whose removal lowers the Hausdorff dimension of $X$.

### 8.6 Relation to semimeasures, exact gauges, and multifractal measures

The construction supplies the missing dictionary among the objects in the dissertation.

1. A dyadic Kraft weight $a$ is a **discrete net semimeasure**: mass is assigned to all net elements with one global summability constraint.
2. The maxitive profile $Q \mapsto a(Q)$, evaluated along $Q_r(x)$, turns largest local weight into shortest description. This is the role played by $\kappa$ and by the possibility capacity in Section 7.
3. The Borel measure $\mu_A = \sum_q 2^{-K^A(q)} \cdot \delta_q$ uses the same prefix atoms but aggregates by **sum**. This is Tana’s $R$ side of the sum/sup fork.
4. Method II aggregates the tilted cube prices by another sum over covers. The null-ideal lemma says precisely when these cover sums can be repackaged into one discrete competitor.

Thus the similarity between the dissertation’s semimeasure manipulations and the capacity argument is structural, not cosmetic. The maxitive object records local shortest descriptions; the additive object and Method II expose the covering null ideal hidden behind the universal competitor.

There is also a precise gauge interpretation. An ordinary Hausdorff gauge prices a cube only by its diameter, $h(2^{-r})$. The new price

$$
h_{\mu,\eta}(Q) = \mu(Q) \cdot (\operatorname{diam} Q)^{-\eta}
$$

depends on both location and scale. It is therefore a spatially adaptive or multifractal gauge. If, in a regular example, $\mu(Q)$ behaves like $h(\operatorname{diam} Q)$, then the positive tilt is the familiar neighboring gauge

$$
t \longmapsto h(t) \cdot t^{-\eta}.
$$

Theorem E says that optimality isn’t equivalent to exactness for one radial gauge. It is equivalent to Hausdorff-dimension-essentiality for every positive power tilt of one adaptive measure profile: every conull remainder of $X$ stays full-dimensional. This explains both why exact radial gauges are sufficient and why they looked too rigid to be necessary for arbitrary sets.

Finally, Theorem E does **not** assert that $\mu$ is exact-dimensional in the usual ergodic-theoretic sense. Exact-dimensionality asks that the lower and upper local dimensions coincide at a constant value for $\mu$-almost every point. Here the local exponent is inspected at every point of $X$, which may be $\mu$-null, and the decisive condition concerns the null ideals of the tilted Method-II measures. These are different notions.

### 8.7 What is established and what is new here

- Dyadic net measures and Method II are classical (Munroe/Rogers; the formulation used here follows Tana).
- Discrete semimeasures, the additive prefix measure $R$, the maxitive prefix outer measure $\kappa$, and their layerwise subexponential comparison are established in algorithmic dimension theory and are developed in the dissertation.
- Multifractal Hausdorff measures $\mathcal{H}_\mu^{q,t}$ are established; the closest standard provenance for (PT) is Olsen’s 1995 formalism.
- “Positive-tilt net outer measure,” “positively Hausdorff-essential,” the Kraft–Carathéodory null-ideal lemma, and Theorem E are new here. The proof is elementary once the right tilted premeasure is written down, but I found no published statement of the equivalence.

The remaining technical cleanup would be to make the presentation coordinate-free. We can use a general layered-disjoint net directly, as Tana’s framework suggests. A centered-ball version should use finitely many adjacent dyadic systems or a bounded-overlap decomposition; for a completely arbitrary non-doubling witness measure, this comparison should be written rather than assumed.

## 9. What ordinary additive measures already characterize

Theorem E uses an ordinary finite Borel measure, but not merely its ordinary null sets: it uses all of its positive-tilt Method-II null ideals, and the measure need not be carried by $X$. Stull’s earlier sufficient theorem asks when one ordinary metric outer measure carried by, or finite on, $X$ already does the job. That useful special case admits the following conceptual compression.

### 9.1 Dimension-essential measures

Let $s := \dim_H X$. Let’s call a metric outer measure $\mu$ **Hausdorff-dimension-essential on $X$** if it is finite and non-zero on $X$,

$$
0 < \mu(X) < \infty
$$

and every $\mu$-conull subset of $X$ has Hausdorff dimension $s$:

$$
\mu(N) = 0, \quad N \subseteq X \quad \Longrightarrow \quad \dim_H(X \setminus N) = s. \tag{12}
$$

When $\mu$ is a finite Borel or Radon measure carried by $X$, (12) says precisely that its upper Hausdorff dimension

$$
\overline{\dim}_H \mu = \inf \{ \dim_H E : \mu(\mathbb{R}^n \setminus E) = 0 \}
$$

is $s$. Thus this sufficient condition is a standard dimension-of-a-measure condition, even though the proof naturally allows metric outer measures on arbitrary subsets.

**Proposition (sufficient measure criterion).** If $X$ carries a Hausdorff-dimension-essential metric outer measure, then $X$ has an optimal Hausdorff oracle.

- **Reason.** Encode both a Hausdorff oracle and the dyadic masses of $\mu$. Stull’s semimeasure/Borel–Cantelli engine shows that, for every competitor $B$ and $\varepsilon > 0$, the set on which $B$ saves $\varepsilon r$ bits infinitely often is $\mu$null. Its complement is therefore full-dimensional by (12), and Stull’s full-dimensional criterion applies.

Stull’s two absolute-continuity hypotheses imply (12):

- If $\mu \ll \mathcal{H}^{s-\delta}$ for every $\delta > 0$, then a positive-$\mu$ set cannot have dimension below $s$.
- If $\mathcal{H}^s \ll \mu$ and $\mathcal{H}^s(X) > 0$, then removing a $\mu$null set removes no $\mathcal{H}^s$mass, so the remainder has dimension at least $s$.

#### Is this “exact dimension”?

No standard source I found gives Stull’s displayed disjunction a single special name, and **exact-dimensional** would be the wrong name. For a finite Borel measure, exact-dimensionality is the pointwise assertion that there is a constant $d$ such that

$$
\lim_{r \downarrow 0} \frac{\log \mu(B(x, r))}{\log r} = d \qquad \text{for $\mu$-almost every } x. \tag{ED}
$$

That terminology comes from the local-dimension tradition in fractal geometry and ergodic theory. It controls the asymptotic mass of individual small balls. Stull’s hypotheses instead compare **null ideals** of outer measures; neither hypothesis says that the local-dimension limit exists, is constant, or equals $s$. For example, the second hypothesis permits adding an atom to an $s$-dimensional measure, which immediately destroys exact-dimensionality while preserving $\mathcal{H}^s \ll \mu$.

There is, however, a standard dimension-of-a-measure translation. For a finite Borel measure carried by $X$, define

$$
\underline{\dim}_H \mu = \inf \{ \dim_H E : \mu(E) > 0 \}, \qquad \overline{\dim}_H \mu = \inf \{ \dim_H E : \mu(\mathbb{R}^n \setminus E) = 0 \}. \tag{DM}
$$

The notation and even the unadorned phrase “Hausdorff dimension of a measure” vary between authors, but these are commonly called the lower and upper Hausdorff dimensions of $\mu$. The first of Stull’s hypotheses forces $\underline{\dim}_H \mu = s$ (and hence also $\overline{\dim}_H \mu = s$ because $\mu$ is carried by $X$). The second forces $\overline{\dim}_H \mu = s$, but can leave $\underline{\dim}_H \mu < s$. Thus the standard name for the common consequence (12), in the carried Borel/Radon setting, is simply

**$\mu$ has upper Hausdorff dimension $s = \dim_H X$.**

For the more general metric-outer-measure formulation, “every $\mu$-conull subset of $X$ has full Hausdorff dimension” is the safest established-language description. **Hausdorff-dimension-essential on $X$** is shorthand introduced here, not terminology used by Stull or an established name I found. Historically, this is the exact property Stull’s Borel–Cantelli argument needs: the semimeasure calculation makes the infinite-savings exceptional set $\mu$-null, and one then needs deletion of that null set to leave Hausdorff dimension $s$. His two absolute-continuity assumptions are convenient sufficient tests for that survival property, approaching it from opposite directions.

This is also distinct from an **exact Hausdorff gauge** $h$, which means $0 < \mathcal{H}^h(X) < \infty$. There “exact” modifies the gauge/measure function and records the correct critical scale for $X$; it does not assert (ED) for $\mathcal{H}^h$, nor is it the conventional name for Stull’s two absolute-continuity alternatives.

This untilted “dimension-essential” formulation isolates the real GMT content of Stull’s measure theorem. It is still only sufficient as a criterion involving one ordinary null ideal; Theorem E becomes necessary and sufficient by retaining every positive power tilt.

### 9.2 Why Frostman measures are natural but insufficient

Frostman’s lemma says, in a standard capacitable setting, that $\dim_H E > t$ is witnessed by a non-zero finite Borel measure $\mu$ carried by $E$ with

$$
\mu(B(x, \rho)) \lesssim \rho^t.
$$

Such a measure turns geometric scale into logarithmic information and therefore fits the semimeasure proof perfectly. Reimann’s work makes this relationship effective.

But Frostman measures certify positive dimension through a compact or analytic core. Optimal oracles exist well beyond capacitable sets. Thus “there is a full-dimensional Frostman measure” cannot be a necessary condition for the class Stull defined.

### 9.3 Exact Hausdorff gauges and the information below dimension

#### Established terminology and provenance

A **gauge function** in Stull’s terminology—called a **dimension function** in Section 1.3.2 of the dissertation and in part of the GMT literature—is a non-decreasing function $h : [0, \infty) \to [0, \infty)$ with $h(0) = 0$ and suitable positivity/continuity away from zero. [Verified, STACS 2022 §2.1: "A function φ:[0,∞)→[0,∞) is a gauge function if φ is monotonically increasing, strictly increasing for t>0 and continuous." Stull's 𝓗^φ covers by balls, so it is the spherical measure. No order regularity is assumed. See `next_steps_for_optimal_oracles.md` §4.] It induces the Hausdorff outer measure

$$
\mathcal{H}^h(X) = \lim_{\delta \downarrow 0} \inf \left\{ \sum_i h(\operatorname{diam} U_i) : X \subseteq \bigcup_i U_i,\ \operatorname{diam} U_i \leq \delta \right\}. \tag{HG}
$$

The gauge is **exact for $X$** if

$$
0 < \mathcal{H}^h(X) < \infty. \tag{EX}
$$

This is the established notion of an **exact Hausdorff gauge** or **exact Hausdorff measure function**. It should not be confused with an **exact-dimensional measure**, which usually means a measure $\mu$ for which $\log \mu(B(x,r))/\log r$ has one constant limit at $\mu$-almost every $x$.

Stull defines (HG)–(EX) in Section 2.1 and states in the abstract and introduction that existence of an exact gauge is sufficient for an optimal Hausdorff oracle. The mechanism is his Theorem 13: use the metric outer measure $\mu := \mathcal{H}^h$ and show that its null sets cannot remove all of the Hausdorff dimension of $X$. Chapter 5.3 of the dissertation studies the closely related classical problem of extracting a subset of positive, finite Hausdorff/net measure for a **fixed** dimension function. These are the historical sources for the exact-measure viewpoint; this terminology isn’t new here.

#### What an exact gauge records beyond $\dim_H$

Hausdorff dimension retains only the critical power $t^s$. A gauge can retain the correction at that critical power. Put

$$
\gamma_h(r) = -\log_2 h(2^{-r}). \tag{GR}
$$

For a regular power-corrected gauge

$$
h(t) = t^s \cdot L(1/t), \qquad \frac{\log L(u)}{\log u} \longrightarrow 0,
$$

one has

$$
\gamma_h(r) = sr - \log_2 L(2^r) = sr + o(r). \tag{SO}
$$

The leading slope is the Hausdorff dimension; the sublinear term is the finer gauge information. For example, the planar Brownian-path gauge quoted by Stull,

$$
h(t) = t^2 \cdot \log(1/t) \cdot \log \log(1/t),
$$

has

$$
\gamma_h(r) = 2r - \log_2 r - \log_2 \log r + O(1).
$$

This explains precisely how an exact gauge can distinguish two sets that Hausdorff dimension alone cannot distinguish.

For a possibly irregular gauge, define its lower and upper power orders

$$
\underline{\alpha}(h) = \liminf_{t \downarrow 0} \frac{\log h(t)}{\log t}, \qquad \overline{\alpha}(h) = \limsup_{t \downarrow 0} \frac{\log h(t)}{\log t}.
$$

If (EX) holds and $s = \dim_H X$, the elementary comparison of Hausdorff sums gives

$$
\underline{\alpha}(h) \leq s \leq \overline{\alpha}(h). \tag{ORD}
$$

For example, if $u < \underline{\alpha}(h)$, then eventually $h(t) \leq t^u$ (the inequality reverses when multiplying by $\log t < 0$), so $0 < \mathcal{H}^h(X) \leq \mathcal{H}^u(X)$ and $u \leq s$. The other inequality is analogous. Equality of the two orders is an additional regularity statement, not part of the bare definition of a gauge.

#### The rigorous route from an exact gauge to optimality

Suppose $h$ is exact for $X$ and $s = \dim_H X$. A convenient sufficient regularity hypothesis is that, for every $\delta > 0$, there are $C_\delta, t_\delta > 0$ such that

$$
h(t) \leq C_\delta \cdot t^{s-\delta} \qquad (0 < t < t_\delta). \tag{CMP}
$$

Then

$$
\mathcal{H}^h \ll \mathcal{H}^{s-\delta} \qquad (\delta > 0).
$$

Indeed, every sufficiently fine cover has $h$-cost at most $C_\delta$ times its $(s - \delta)$-cost. Taking $\mu := \mathcal{H}^h$ in Stull’s Theorem 13 now proves that $X$ has an optimal Hausdorff oracle. All slowly varying corrections such as powers of $\log(1/t)$ or $\log\log(1/t)$ satisfy (CMP).

There is a small provenance caveat worth recording. Stull announces the blanket exact-gauge implication, but version 2 gives no separately numbered exact-gauge corollary after Theorem 13; the explicit corollary there is the power-gauge $s$-set case. The derivation above is immediate for regular-order gauges. Under Stull’s very minimal definition of “gauge,” a completely irregular $h$ does not visibly imply the null-set comparison in Theorem 13 merely from (EX) and $\dim_H X=s$. I have therefore stated the direct argument with (CMP) rather than silently assuming power regularity. This is a point to verify with Stull, not a claim here that the announced generality is false. [Verified against the STACS 2022 text: the body proves only Theorem 13 (the two absolute-continuity hypotheses), Corollary 14 (s-sets), and two examples with φ(t) = t^s log(1/t) and its reciprocal. The blanket exact-gauge claim appears only in the abstract and introduction.]

The semimeasure proof makes the connection to the preceding sections even more concrete. For $\mu = \mathcal{H}^h$, Stull’s weights become

$$
p_{h,X}(d_{r,i}) = \frac{\mathcal{H}^h(X \cap Q_{r,i})}{r^2 \cdot \mathcal{H}^h(X)}.
$$

Their code lengths are

- \log_2 p_{h,X}(d_{r,i}) = -\log_2 \mathcal{H}^h(X \cap Q_{r,i}) + 2\log_2 r + O(1).

Thus an exact gauge supplies an additive metric mass distribution; the $r^{-2}$ term pays for combining all precision levels; Levin dominance turns those masses into descriptions; and dimension-essentiality converts the resulting null exceptional set back into a full-dimensional preservation set. This is the exact bridge among gauges, discrete semimeasures, and optimal oracles.

#### Does radial exactness characterize optimal oracles?

At present, no converse is known for existence of one ordinary, diameter-only exact gauge. Theorem E does give a necessary-and-sufficient *adaptive* gauge statement, but the two notions operate at different resolutions.

- Optimal-oracle preservation allows an error $\varepsilon r$ for each fixed $\varepsilon>0$. Consequently it is insensitive to any fixed $o(r)$ correction in (SO), precisely where logarithmic exact gauges live.
- An exact gauge is a single additive, metric, diameter-based certificate. Theorem E instead yields cube prices $\mu(Q) \cdot (\operatorname{diam} Q)^{-\eta}$ that may vary spatially and requires the full family $\eta > 0$.
- Stull’s result therefore places ordinary radial exact gauges on the **sufficient-certificate** side of the picture. Theorem E explains the necessary replacement: multifractal, location-dependent gauges and their null ideals, not one function of diameter.

A plausible stronger research notion, introduced only as a suggestion here, is **gauge-refined optimality**: after fixing an exact $h$, compare the centered quantities

$$
K_r^A(x) - \gamma_h(r)
$$

or demand preservation with an error calibrated to the gauge correction $|\gamma_h(r) - sr| + O(\log r)$ rather than to $\varepsilon r$. For $s > 0$, merely dividing $K_r$ by $\gamma_h(r) = sr + o(r)$ recovers the same first-order dimension and therefore adds nothing; one must retain the centered second-order term. For $s = 0$, $\gamma_h(r)$ may itself be $o(r)$, so a gauge-normalized formulation could add real content where Stull’s high-dimension clause becomes vacuous. None of these refined conditions is proved equivalent to optimal oracles; they are concrete next questions suggested by the translation, not established results.

## 10. Obstructions and boundary cases

### 10.1 A Bernstein-set test case

Assuming choice, partition $[0,1]$ into two Bernstein sets $B_0, B_1$. Each Bernstein set meets every non-empty perfect subset of $[0,1]$, and so does its complement. Since

$$
1 = \dim_H [0, 1] = \max \{ \dim_H B_0, \dim_H B_1 \},
$$

at least one member $B$ of the partition has $\dim_H B = 1$. As $B \subseteq \mathbb{R}$, also $\dim_P B = 1$. Hence $B$ is weakly regular and Stull’s theorem gives optimal Hausdorff and packing oracles.

On the other hand, $B$ contains no uncountable closed set and therefore no positive-dimensional Borel subset. Indeed, every uncountable Borel set contains a nonempty perfect set.

It also carries no non-zero $t$-Frostman Radon measure for any $t > 0$. Such a measure is non-atomic. Inner regularity would produce an uncountable compact $K \subseteq B$ of positive measure, and $K$ would contain a perfect subset, contradicting the Bernstein property.

This single example rules out the following as necessary conditions:

- existence of a full-dimensional compact, Borel, or analytic core;
- existence of a positive-dimensional Frostman Radon measure carried by $X$;
- any characterization that first regularizes $X$ by taking an equal-dimensional Borel subset.

It does **not** rule out an ambient measure that is not carried by $B$. The necessity proof of Theorem E in fact uses a densely supported atomic measure and then forms nontrivial tilted Method-II outer measures from its cube masses. Thus the Bernstein test does not merely survive the new theorem; it explains why the witness must be allowed to live off the target set.

### 10.2 Dimension data alone cannot decide optimality

For every $0 \leq \alpha < \beta \leq 1$, the Borel set

$$
D_{\alpha, \beta} = \left\{ x : \dim(x) = \alpha,\ \operatorname{Dim}(x) = \beta \right\}
$$

has Hausdorff dimension $\alpha$, packing dimension $\beta$, and both kinds of optimal oracle. Under AC + CH, Stull constructs sets with the same kinds of prescribed unequal dimensions and no optimal oracles, as well as sets separating Hausdorff from packing optimality. Therefore no condition involving only $(\dim_H X, \dim_P X)$ can characterize the property.

### 10.3 Projection conclusions are necessary but likely too coarse

Stull’s original geometric consequence is that, if $X \subseteq \mathbb{R}^2$ has an optimal Hausdorff oracle, then for Lebesgue-almost every direction $e$,

$$
\dim_H(\pi_e X) = \min \{ \dim_H X, 1 \}.
$$

Recent work derives sharper exceptional-set estimates and higher-dimensional $k$-plane versions. But these projection conclusions record only the dimensions of images after taking a limit. Optimality records resistance to every auxiliary information source at essentially every sufficiently fine scale. It is therefore plausible—and consistent with all known examples—that ordinary projection behavior is strictly weaker than optimal-oracle behavior.

### 10.4 Set theory is not incidental

Under AD every set has an equal-dimensional Borel core and hence an optimal Hausdorff oracle. Under AC + CH, Stull’s transfinite constructions produce failures. A future intrinsic characterization must be flexible enough to see noncapacitable, choice-built sets.

### 10.5 Why the standard Hausdorff-dimension game is too strong

Crone, Fishman, and Jackson’s Hausdorff-dimension game is an illuminating comparison. Their Theorem 2 says that if the “large-set” player has a winning strategy in the $\delta$-dimension game with target $Y$, then the tree of plays generated by the strategy produces a compact set

$$
K \subseteq Y, \qquad \dim_H K \geq \delta.
$$

Consequently, if $B$ is the full-dimensional Bernstein set in Section 10.1, the large-set player cannot win the $\delta$-dimension game targeting $B$ for any $\delta > 0$, even though $B$ has optimal oracles. The same applies to every preservation set $W_B(\Pi, \Lambda, \varepsilon) \subseteq B$: no such set contains a positive-dimensional compact subset.

This rules out a broad natural proposal:

“$X$ has optimal oracles exactly when the defender has a winning Hausdorff-dimension strategy after the challenger chooses a competing cover or capacity.”

That proposal implies compact-core regularity and is therefore strictly stronger under choice. An interleaved game, in which the competitor adapts to the defender’s partial point, is stronger still and cannot be assumed equivalent to the static quantifier pattern.

There are two qualifications.

- For analytic targets, or under AD, determinacy converts dimension bounds into winning-strategy statements away from the critical exponent. This explains why Hausdorff games remain useful in the regular settings where Stull already proves optimality.
- A two-stage “game” in which the challenger first reveals the entire capacity and the defender then chooses a point is exactly (CH)–(CP), but it is merely the capacity criterion written as a game and adds no structure.

Thus the game route gives a useful obstruction rather than a new characterization for arbitrary sets. The maxitive-capacity route survives because its capacity is an ambient comparison device; it is not required to be carried by $X$ and does not manufacture a compact subset of $X$.

## 11. Packing optimality

Everything in Sections 3–8 has a packing analogue.

Call $\varphi$ **packing-robust for $X$** if

$$
\sup_{x \in X} \operatorname{bcDim}_\varphi(x) = \dim_P X
$$

and, for every rational ball code $\psi$ and $\varepsilon > 0$, some $x \in X$ has

$$
\operatorname{bcDim}_\varphi(x) \geq \dim_P X - \varepsilon, \qquad \operatorname{bcDim}_\psi(x) \geq \dim_P X - \varepsilon
$$

and

$$
L^\psi_r(x) \geq L^\varphi_r(x) - \varepsilon r \quad (\forall^\infty r).
$$

The same proof, using the packing half of Miyabe’s theorem, gives:

$X$ has an optimal packing oracle if and only if it has a packing-robust rational ball code, equivalently a packing-robust Kraft ball system.

Equivalently, replace $\operatorname{capdim}$ in Theorem D by $\operatorname{capDim}$ and require the good sets to have full packing dimension. When $\dim_P X > 0$, robustness is equivalent to the preservation sets having full packing dimension. The distinction between Hausdorff and packing optimality is now classical and transparent: it is the distinction between lower and upper asymptotic rates of the same maxitive-capacity profile. Stull’s AC + CH separation says these two robust-rate properties can genuinely differ.

Theorem E becomes: choose a finite Borel measure $\mu$ with

$$
\sup_{x \in X} \operatorname{capDim}_\mu^{\mathcal{D}}(x) = \sup_{x \in X} \limsup_{r \to \infty} \frac{-\log_2 \mu(Q_r(x))}{r} = \dim_P X,
$$

and require

$$
\mathscr T_{\mu,\eta}(N) = 0, \quad N \subseteq X \quad \Longrightarrow \quad \dim_P(X \setminus N) = \dim_P X
$$

for every $\eta > 0$ (with the analogous witness clause at packing dimension zero). The null-ideal lemma itself is unchanged; only the point-to-set extremum and the dimension required to survive a null deletion change. This also gives a classical formulation of Stull’s Hausdorff/packing separation under AC + CH.

## 12. Relation to the Fässler–Orponen conjecture

The Fässler–Orponen restricted-projection conjecture concerned non-degenerate one-parameter families of line and plane projections in $\mathbb{R}^3$. The original problem appears in Fässler–Orponen. The line case was proved in 2022 by Pramanik–Yang–Zahl and independently by Gan–Guth–Maldague; the plane case and higher-dimensional analogues were proved using Fourier decoupling and high–low methods. A current overview appears in the 2026 ICM restricted-projection survey.

This is relevant philosophically: a Marstrand-type theorem initially viewed through effective methods may later acquire a classical proof. But I found no published effective proof of the full Fässler–Orponen theorem, and its successful proofs use cinematic curvature, incidence geometry, Fourier decomposition, and decoupling. It therefore supplies motivation, not a direct technical route to the optimal-oracle characterization.

The robust Kraft-cover theorem suggests what an effective approach would need to control: not merely a minimizing cover of the source set, but uniform preservation of its point-scale weights after adjoining a code for the projection parameter and the analytic estimates used in the projection argument.

The strongest accurate conclusion is:

The oracle, code, and competitor quantifiers can apparently all be eliminated. Optimality is equivalent to the existence of one dimension-minimizing finite Borel measure for which every positive-tilt Method-II null deletion leaves the Hausdorff dimension of $X$ unchanged. This is a classical, additive-cover, necessary-and-sufficient condition. What remains open is whether the adaptive multifractal witness can be replaced by a more familiar radial gauge, energy capacity, or carried measure on restricted classes of sets.

## 13. Next steps

**1. Replace the named $\operatorname{bcdim}$ layer by a direct Hausdorff ball-code point-to-set theorem.** Define only $L_r^\varphi(x)$ and prove

$$
\dim_H X = \min_{\varphi \in \mathfrak{B}_{\mathbb{Q}}} \sup_{x \in X} \liminf_{r \to \infty} \frac{L_r^\varphi(x)}{r}
$$

directly. The lower-bound direction is a Kraft-tail Hausdorff-cover argument; the minimizing code is obtained by assigning prefix-free descriptions to a sequence of nearly critical rational-ball covers. This makes the geometric mechanism transparent and brings the proof closer to the original Lutz–Lutz construction, in which the minimizing oracle stores refined Hausdorff covers. Miyabe should still receive credit for isolating the ball-code theorem, proving the rational-ball reduction and attainment cleanly, and developing the packing analogue.

**2. Check Theorems A–E with Stull, Miyabe, the Lutzes, and experts in net measures.** Theorem E’s core is the short null-ideal Lemma (KC1)–(KC2), while the two translation points are the uniform cube/point comparison (18) and the additive/maxitive comparison (17). These are the places where a hidden convention or boundary issue would show up.

**3. Make Theorem E coordinate-free.** Prove it first on a general layered-disjoint net, then give a centered-ball version using finitely many adjacent dyadic systems or Besicovitch decompositions. Track arbitrary non-doubling measures explicitly.

**4. Compare (PT) systematically with Olsen’s multifractal formalism.** Determine whether “every $(1, -\eta)$-null deletion preserves full dimension” has an established name or a useful reformulation through a multifractal spectrum, upper dimension of a measure, or Billingsley dimension.

**5. Construct the measure $\mu$ directly in regular examples.** For analytic, weakly regular, and exact-gauge sets, produce a witness for Theorem E without passing through an oracle. This would turn the characterization into a practical GMT tool rather than only an exact translation.

**6. Prove closure directly with tilted ideals.** Mixtures of the witnessing measures should encode countable unions, while restriction of the ideal inclusion should handle full-dimensional supersets. Writing this carefully would test how naturally Theorem E reproduces Stull’s closure theorems.

**7. Separate common-good-set from competitor-dependent-good-set variants.** Requiring one full-dimensional $G \subseteq X$ that works for all competitors is much stronger. Even for one competitor, intersecting the full-dimensional good sets for $\varepsilon \downarrow 0$ can destroy dimension. Concrete counterexamples would locate the exact limit of scale selection.

**8. Extend to general net spaces.** The dissertation’s framework supplies the exact vocabulary: replace dyadic cubes by a layered-disjoint net and $2^{\eta r}$ by $\operatorname{diam}(N)^{-\eta}$. The proof survives whenever point complexity and net complexity agree up to $o(r)$.

**9. Audit exact gauges at irregular orders.** Determine whether Stull’s announced exact-gauge corollary follows for every gauge under his stated minimal definition, or whether one needs (CMP), an equivalent null-set comparison, or a standard regularity convention on dimension functions.

**10. Test gauge-refined optimality.** For regular exact gauges, compare the centered profile $K_r^A(x) - \gamma_h(r)$ rather than only $K_r^A(x)/r$. At dimension zero, investigate preservation at the natural scale $\gamma_h(r) = o(r)$.

## References and primary links

- Jack H. Lutz and Neil Lutz, *Algorithmic information, plane Kakeya sets, and conditional dimension*, the original Euclidean point-to-set principle.
- D. M. Stull, *Optimal Oracles for Point-to-Set Principles*, arXiv 2021; STACS 2022 published version.
- Jack H. Lutz and Neil Lutz, *Algorithmically Optimal Outer Measures*, arXiv 2020; ACM Transactions on Computation Theory, 2025.
- Gustave Choquet, *Theory of capacities*, 1954, for the classical continuity and capacitability framework.
- Lotfi A. Zadeh, *Fuzzy sets as a basis for a theory of possibility*, 1978, for possibility distributions and possibility measures.
- Paul Poncet, *A decomposition theorem for maxitive measures*, 2009/2011, for maxitive measures and cardinal densities.
- Ilya Molchanov and Kirstin Strokorb, *Max-stable random sup-measures with comonotonic tail dependence*, 2016, Section 2 for maxitive Choquet capacities and sup-measures.
- Kenshi Miyabe, *Ball codes: A coding characterization of Hausdorff and packing dimensions*, 2026.
- Raymond J. G. Tana, *The Algorithmic Theory of Information and its Applications to Geometric Measure Theory*, PhD dissertation, 2025.
- C. A. Rogers, *Hausdorff Measures*, Cambridge University Press, 1970, for Method-II and net-measure foundations.
- Colleen D. Cutler, *The Hausdorff Dimension Distribution of Finite Measures in Euclidean Space*, *Canadian Journal of Mathematics* 38 (1986), 1459–1484, for the dimension-of-a-measure tradition underlying lower/upper Hausdorff dimensions.
- Lars Olsen, *A Multifractal Formalism*, *Advances in Mathematics* 116 (1995), 82–196, for the measures $\mathcal{H}_\mu^{q,t}$; (PT) is their dyadic-net $q=1,t=-\eta$ relative.
- Jan Reimann, *Effectively closed sets of measures and randomness*, 2008.
- Logan Crone, Lior Fishman, and Stephen Jackson, *Hausdorff dimension regularity properties and games*, 2020.
- Jacob B. Fiedler and D. M. Stull, *Universal Sets for Projections*, 2024/2025.
- Jacob B. Fiedler and Zhifan Jing, *Projections of sets with optimal oracles onto $k$planes*, 2026.
- Katrin Fässler and Tuomas Orponen, *On restricted families of projections in $\mathbb{R}^3$*, 2013.

## Final assessment

For $s = \dim_H X > 0$, a set has an optimal Hausdorff oracle exactly when there is one finite Borel measure $\mu$ whose lower dyadic local capacity dimensions realize $s$ on $X$ and such that

$$
\mathscr T_{\mu,\eta}(N) = 0, \quad N \subseteq X \quad \Longrightarrow \quad \dim_H(X \setminus N) = s \qquad (\eta > 0).
$$

Equivalently, for each fixed $\eta > 0$, every subset of $X$ conull for the multifractal tilt has full Hausdorff dimension.

The decisive observation is the Kraft–Carathéodory duality. A competitor saving $\varepsilon r$ produces a summable limsup cover for every smaller positive tilt; conversely, zero tilted outer measure lets one pool cheap covers into a single Kraft competitor. The maxitive capacity was therefore an accurate intermediate object, but its universal comparison can be integrated out into an additive-cover null ideal. This is not an ordinary Frostman theorem. The witnessing measure may be atomic with dense support and need not be carried by $X$—exactly what the Bernstein example forces. Nor is it exactness for one radial gauge. It is a spatially adaptive multifractal exactness condition involving every positive power tilt. For regular sets, ordinary exact gauges remain natural sufficient certificates; for arbitrary sets, Theorem E identifies the more flexible object that replaces them.