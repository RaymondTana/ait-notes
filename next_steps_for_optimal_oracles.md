I've read the scratch file's review notes (Parts A–H) and its older report sections §1–2 and §9, plus your Ch. 1–2 pages. Here's my take, starting with your direct questions and ending with a proposed plan.

## 1. Is s = 0 trivial for packing too?

Yes, by the same argument. Suppose dim_P X = 0, let x₀ ∈ X, and let A₀ be any packing oracle. Then A := A₀ ⊕ x₀ is an optimal packing oracle:
- Joins preserve being a packing oracle.
- K^A_r(x₀) ≤ K(r) + O(1), so K^{A,B}_r(x₀) ≥ 0 ≥ K^A_r(x₀) − εr for all large r.
- Dim^{A,B}(x₀) ≥ 0 − ε holds automatically.

The argument never uses which dimension is involved. It works because the tolerance is linear (εr) and the dimension clause is empty at 0.

It's also worth saying *why* s = 0 needs separate handling. Stull's Prop. 4 says "dim N_X(A,B,ε) = s". At s = 0 this can't tell an empty preservation set from a nonempty one, since dim ∅ = 0. So the exception is about how the condition is phrased, not about the mathematics.

**Recommendation:** state at the start of the chapter that the relevant dimension is positive, and handle s = 0 in one remark covering both Hausdorff and packing. Note that the assumption depends on the notion: a set with dim_H = 0 < dim_P is trivial on the Hausdorff side but not on the packing side.

## 2. Does [Witness] follow from [Fitness]?

**For a single oracle, no.** Let C be a computable s-dimensional Cantor set (with ∅ optimal for C), let z be an ML-random point of [0,1], and set X = C ∪ {z}. Then:
- dim_H X = s.
- ∅ satisfies [Fitness], because points of C serve as the witnesses.
- ∅ is not a Hausdorff oracle for X, because dim(z) = 1 > s.

**For existence, yes.** If A is fit and A₀ is a Hausdorff oracle, then A ⊕ A₀ is optimal: apply A's fitness to the competitor A₀ ⊕ B. So X has an optimal oracle iff some oracle is fit.

Better still, **Stull's Prop. 4 needs only [Fitness]**. Neither direction of its proof uses that A is a Hausdorff oracle (I checked both). So for s > 0:

> X has optimal Hausdorff oracles ⟺ ∃A ∀B ∀ε: dim_H N_X(A,B,ε) = s.

**It holds for every characterization in the scratch, for the same reason.** Each one has the same three ingredients:

| Objects | Join | [Witness] is nonempty by | [Fitness] is upward-closed by |
|---|---|---|---|
| oracles | A ⊕ A₀ | Lutz–Lutz point-to-set principle | relativization |
| ball codes (Thm A–C) | φ ∨ φ₀ | Miyabe's ball-code theorem (your §2.4) | merging costs 1 bit |
| capacities (Thm D) | ½max{Π, Π₀} | capacity point-to-set principle | same |
| measures (Thm E) | μ + μ_X | Cutler's weak duality | comparability (C.5) |

So you have one meta-lemma: if both properties are upward-closed under the join and [Witness] is always inhabited, then the two together are inhabited iff [Fitness] is. The packing versions work the same way.

**Recommendation:** define *optimal oracle* exactly as Stull does, since that is the published term and applications cite it. Then prove "[Witness] is free" right away, name the other half (e.g. **fit oracle**), and argue only with fitness after that. For the later classical characterizations, state only the [Fitness] form, with the meta-lemma as a remark.

## 3. What Stull's two absolute-continuity conditions have in common

You've identified the right property: for 0 < μ(X) < ∞, **every μ-conull subset of X has dimension s.** Both conditions imply it:
- **μ ≪ 𝓗^{s−δ} for every δ.** A conull Y has μ(Y) = μ(X) > 0, so 𝓗^{s−δ}(Y) > 0 and dim Y ≥ s − δ.
- **𝓗^s ≪ μ and 𝓗^s(X) > 0.** If μ(X∖Y) = 0, then 𝓗^s(X∖Y) = 0, so 𝓗^s(Y) = 𝓗^s(X) > 0.

The scratch's Prop. 3 (C.8) shows this property alone is sufficient. Two points to make when you introduce it:
- **When s > 0, positivity comes for free:** if μ(X) = 0, then X is itself null and its empty complement would need dimension s.
- **Finiteness carries all the content.** 𝓗^t with t < s satisfies the conull property for *every* X, which contradicts the CH examples. Say so explicitly.

This also gives you the symmetry you want. By Prop. 4, fitness says the same thing for a different null family: deleting any set on which some B saves εr bits infinitely often leaves full dimension. **Every condition then has one shape: some source has a null family whose deletion never lowers dim_H X.**

| Condition | Null family | Status |
|---|---|---|
| Stull's measure criterion | μ-null sets | sufficient |
| Theorem E′ | 𝒯_{μ,η}-null sets (tilted) | characterization |
| Fitness | saving sets of A | definition |

Whether the untilted measure version is also *necessary* is open (Part E.2), which fits the "mystery" angle well.

For a measure carried by X, the property is the standard statement "upper Hausdorff dimension of μ equals s". Use that phrase in the text and keep a coined name ("dimension-essential") as shorthand.

## 4. "Gauge" in your notes versus Stull

- **Your notes never use the word "gauge".** Ch. 1 defines a **dimension function** (non-negative, non-decreasing, right-continuous, h(t) = 0 ⟺ t = 0) and the **Hausdorff premeasure** ρ_h = h ∘ diam, with 𝓗^{ρ_h} built by Method II over arbitrary covers.
- **Stull's definition (verified in the STACS 2022 version, §2.1, verbatim):** "A function φ : [0,∞) → [0,∞) is a gauge function if φ is monotonically increasing, strictly increasing for t > 0 and continuous." His 𝓗^φ(E) = lim_r h^φ_r(E), with h^φ_r(E) = inf{Σ_i φ(d(Q_i)) : ⋃_i Q_i covers E, d(Q_i) ≤ 2^{−r}}, "where d(Q) is the diameter of ball Q". "When 0 < 𝓗^φ(E) < ∞, we say that φ is an exact gauge for E." His absolute continuity matches ours: "μ ≪ ν if μ(A) = 0 for every set A for which ν(A) = 0."
- **Comparison.**

  | | Notes | Stull |
  |---|---|---|
  | Monotonicity | non-decreasing | strictly increasing on (0,∞) |
  | Continuity | right-continuous | continuous |
  | Value at 0 | h(t) = 0 ⟺ t = 0 | φ(0) = 0 not stated (implicit: if φ(0) > 0, every infinite set has infinite 𝓗^φ-measure) |
  | Covers | arbitrary sets | balls (so 𝓗^φ is the *spherical* measure; comparable to ours when φ is doubling, not in general) |
  | Order regularity | none | none |

  So Stull's gauges (with φ(0) = 0) are a subclass of the notes' dimension functions. When citing him, say his gauges are continuous and strictly increasing and that he covers by balls.
- **What Stull actually proves about exact gauges.** The abstract and introduction say, with no extra hypotheses, that "the existence of exact gauge functions for a set E is sufficient for the existence of optimal Hausdorff oracles". The body proves:
  - Theorem 13: a metric outer measure μ with 0 < μ(E) < ∞ and either μ ≪ 𝓗^{s−δ} for every δ > 0, or 𝓗^s ≪ μ and 𝓗^s(E) > 0, gives an optimal Hausdorff oracle;
  - Corollary 14: the s-set case, 0 < 𝓗^s(E) < ∞;
  - two examples with φ(t) = t^s log(1/t) and its reciprocal, both via Theorem 13.

  So the blanket claim isn't proved for arbitrary gauges. That confirms the scratch's caveat.
- **The difference that matters is order regularity, not continuity.** Neither definition requires h(t) ≈ t^s up to sub-power factors. That regularity, i.e. (CMP), or equivalently liminf_{t→0⁺} log h(t)/log t = dim_H X, is exactly what "exact gauge ⇒ optimal oracle" needs via Theorem 13. C.9 claims a counterexample without it; that construction is only medium-confidence.

**For the fundamentals (PR 1):**
- Add "gauge" as a synonym of dimension function, in the glossary too.
- Define exact gauges and prove liminf_{t→0⁺} log h(t)/log t ≤ dim_H X ≤ limsup_{t→0⁺} log h(t)/log t for an exact gauge h. Avoid the names "lower/upper order" (not verified as standard for gauges).

Your premeasure framework also already covers the tilted measures later on: 𝒯_{μ,η} is just 𝓗^ρ with ρ(Q) = 2^{η·rk Q} μ(Q) on dyadic cubes.

## 5. Proposed plan

Your sequencing is right: fundamentals, then optimal oracles as a case study, then the classical characterizations.

**PR 1: Fundamentals (GMT side, in Ch. 1's Measures and Hausdorff Dimension page)**
- Gauges and exact gauges, with the liminf/limsup bound on dim_H.
- Absolute continuity of outer measures.
- Classical packing dimension, which is currently missing (only the effective version is defined). Move the covering number N(X, δ) there from 04-algorithmic-randomness.
- Weakly regular sets. This term is attested: Fiedler–Stull, *Universal Sets for Projections* (arXiv 2411.16001, §1.3), say "We say that a set is weakly regular if its Hausdorff and packing dimension are equal." Stull's optimal-oracles paper says "regular" once, informally (§3.3.1).
- Lower and upper Hausdorff dimension of an outer measure, with Stull's two absolute-continuity conditions proved there as a pure GMT proposition.
- Packing oracles (one sentence in §2.4).
- The notation Q_r(x) on the Notation page (𝒬^m_r is already there).
- Dropped: the mass distribution principle and Frostman's lemma (only needed for the later oracle-free reproofs).

**PR 2: A bridge at the end of §2.4**
Hausdorff and packing oracles are closed under joins. That closure only gives preservation at infinitely many scales, not at all large ones. That gap is the motivating question for the next chapter.

**PR 3: New chapter, "Optimal Oracles" (published material plus easy structural remarks)**
1. Motivation, and Stull's definition (Hausdorff and packing).
2. Structure: the join lemma, Prop. 4 for fitness alone, [Witness] is free, and the s = 0 remark.
3. Closure properties: supersets, countable unions, and removing lower-dimensional parts.
4. Sufficient conditions: analytic sets, weakly regular sets, the shared measure property, and exact gauges with order regularity.
5. Limits: the AC + CH separations, AD via Crone–Fishman–Jackson, and Bernstein sets.
6. Applications: projection theorems (Stull, Fiedler–Stull, Fiedler–Jing).
7. The mystery: Miyabe leaves the classical characterization open, and exact gauges are not necessary (the easy compact example in C.9).

**PR 4 and later: Classical characterizations**
Ball codes, then capacities, then tilted measures, each stated in [Fitness]-only form with the meta-lemma. After that, the oracle-free reproofs, and an appendix with Theorem D and C.11.

Keep the new results (C.8 reproofs, the second C.9 example, H.1–H.3) visibly labeled "(new)". Consider whether to post a preprint or contact Stull and Miyabe before they go on the public site.

If this looks right, I can start PR 1 or draft the chapter outline as a stub page.