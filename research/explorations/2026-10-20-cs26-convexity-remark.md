---
candidates:
  - id: cand:no-positive-convexity-linf
    statement: >-
      Let d ≥ 2, let ν ∈ P₂(ℝᵈ) be absolutely continuous with a bounded density that is bounded
      below by a positive constant on some ball, and let M > ‖ν‖_∞. Then there is no λ > 0
      such that F_ν = ½ SW₂²(·, ν) is λ-geodesically convex on K_M = {ρ ∈ P₂(ℝᵈ) : ‖ρ‖_∞ ≤ M};
      by the quadratic-growth reduction of item 3 below, this follows from
      inf { SW₂²(µ, ν) / W₂²(µ, ν) : µ ∈ K_M, µ ≠ ν } = 0.
---

# The λ-convexity remark on Cozzi–Santambrogio (arXiv:2610.20972)

## Question examined

Route `ap:certify-scouting`, mining the citing paper `CozziSantambrogio2026` against
`conj:sw-critical`. The scouting file `verification/13-korba-sw/0-statut.md` (§3 and its list of
new results) contains an unchecked remark: "λ > 0 is excluded as soon as ν ∈ K, since at ρ = ν
the field v + id/d = id/d has Lipschitz constant 1/d, so L ≥ 1/d and λ = 1/d − L ≤ 0; hence
λ-convexity gives no 'critical ⇒ minimizer', only F(µ) ≤ (|λ|/2) W₂²(µ, ν) at a critical point
µ ∈ K." Question: what precisely is true, and does it deserve a node? Engaged:
`def:sliced-wasserstein`, `def:barycentric-field`, `def:critical-point`,
`prop:notions-coincide` (proved), `conj:sw-critical`.

Notation in CS26 (checked against the text): σ is the averaged surface measure (a probability,
as in `def:sliced-wasserstein`); F_ν(ρ) = ½ SW₂²(ρ, ν); v[ρ](x) = ⨍ (T_θ(x·θ) − x·θ) θ dσ(θ)
(eq. (1.2), no factor d); λ-convexity is (2.5), along a geodesic, with the W₂² term; Lemma 3.1:
Lip(v[ρ] + id/d) ≤ L on a geodesically convex K ⇒ λ = 1/d − L; Lemma 4.1 (L^p balls) and
Theorem 4.4 (L^∞ balls, λ = 1/d − c(d) κ^{-1/d} (1 − αd/(d−1))^{-1} M^{1/d}) supply L.

## What we learned

1. *established* — **The remark's computation is right, in CS26's normalization.** With
   ∫ θ⊗θ dσ = I/d, v[ρ] + id/d = ⨍ T_θ(x·θ) θ dσ. In the normalization of
   `def:barycentric-field`, v[ρ] = −v_ρ/d (relative to target ν), so v[ρ] + id/d =
   (Id − v_ρ)/d, and criticality (v_µ = 0 µ-a.e.) is v[µ] = 0 µ-a.e. At ρ = ν every T_θ is
   the identity, so v[ν] + id/d = id/d, of Lipschitz constant exactly 1/d. Hence any L valid
   for Lemma 3.1 on a K containing ν satisfies L ≥ 1/d, and CS26's λ = 1/d − L is ≤ 0. This
   is a statement about **the bound CS26's method produces** — option (b) of the mission —
   not about the convexity modulus of F_ν. It is consistent with CS26's own sentence that λ
   "is not expected to be positive" (l. 166).

2. *established* — **The naive upgrade (a) is false: F_ν can be (1/d)-convex on a
   geodesically convex set containing ν and other measures.** Let A = {(x ↦ sx + h)_#ν :
   s > 0, h ∈ ℝᵈ}. For ρ = (sx + h)_#ν, the map x ↦ sx + h is the gradient of a convex
   function, so W₂²(ρ, ν) = ∫ |(s−1)x + h|² dν; its projection on θ is the monotone map
   r ↦ sr + θ·h, so SW₂²(ρ, ν) = ∫∫ ((s−1)x·θ + h·θ)² dν dσ = (1/d) W₂²(ρ, ν). Between two
   elements of A the optimal map is again affine with positive scalar slope, A is geodesically
   convex, W₂² is a quadratic form in (Δs, Δh) along it (A is flat), and F_ν = W₂²(·, ν)/(2d)
   is exactly (1/d)-convex on A. So no statement "no λ > 0 on any geodesically convex set
   containing ν and another measure" holds.

3. *established* — **The true universal statement is λ ≤ 1/d, and it is elementary.** Let K be
   geodesically convex, ν ∈ K, and F_ν λ-convex on K. For µ ∈ K and the geodesic (ρ_t) from
   ρ₀ = ν to ρ₁ = µ, (2.5) and F_ν(ν) = 0 give 0 ≤ F_ν(ρ_t) ≤ t F_ν(µ) − (λ/2) t(1−t) W₂²(µ, ν);
   dividing by t and letting t → 0, **SW₂²(µ, ν) ≥ λ W₂²(µ, ν) for every µ ∈ K** (quadratic
   growth). With the trivial bound SW₂² ≤ W₂²/d (project an optimal plan: W₂²(µ_θ, ν_θ) ≤
   ∫ ((x−y)·θ)² dγ, then average using ∫ θ⊗θ dσ = I/d), λ ≤ 1/d as soon as K ∋ ν contains one
   µ ≠ ν; item 2 shows 1/d is attained. So λ > 0 on K ∋ ν is *equivalent in strength to* a
   linear comparison SW₂ ≥ √λ W₂ (relative to ν) on K — the point raised in the mission.

4. *sketch, not written out* — **On CS26's sets, positive λ fails for a different reason than
   the remark gives** (`cand:no-positive-convexity-linf`). By item 3 it suffices that
   SW₂²/W₂² → 0 along some µₙ ∈ K_M. Take ν ≥ c > 0 on B(x₀, 2r), η a smooth bump on B(x₀, r)
   even in x₁ − x₀·e₁, and µₙ = ν + δ η sin(n(x₁ − x₀·e₁)) with δ small (density in K_M since
   M > ‖ν‖_∞, mass preserved, density ≥ c/2 on B(x₀, 2r)). Then (i) W₂(µₙ, ν) ≥ M^{-1/2}
   ‖µₙ − ν‖_{Ḣ^{-1}} ≳ δ/n (Loeper/Peyre); (ii) for each θ, F_{µₙ,θ} − F_{ν,θ} is supported in
   an interval where both projected densities are ≥ c' > 0, so W₂(µₙ,θ, ν_θ) ≲ ‖F_{µₙ,θ} −
   F_{ν,θ}‖_{L²}; (iii) by the Fourier slice theorem, averaging (ii) over θ gives SW₂² ≲
   δ² ‖η sin(n·)‖²_{Ḣ^{-(d+1)/2}} ≲ δ² n^{-(d+1)} (the low frequencies are harmless: the
   perturbation has zero mass and first moment O(n^{-k})). Ratio ≲ n^{-(d−1)} → 0 for d ≥ 2.
   Steps (i)–(iii) are standard but have not been written out with constants here.

5. *established* — **Item (c), the consequence at a critical point, is correct.** Let K be
   geodesically convex with ν ∈ K, F_ν λ-convex on K with λ ≤ 0, and µ ∈ K absolutely
   continuous (automatic on CS26's L^p and L^∞ balls) and critical in the sense of
   `def:critical-point` (1). By `prop:notions-coincide` (2), µ is a Wasserstein critical
   point: along the geodesic (µ_t) from µ to ν the right derivative of F_ν(µ_t) at 0 vanishes.
   (2.5) gives (F_ν(µ_t) − F_ν(µ))/t ≤ −F_ν(µ) + (|λ|/2)(1−t) W₂²(µ, ν); letting t → 0,
   **F_ν(µ) ≤ (|λ|/2) W₂²(µ, ν)**, i.e. SW₂²(µ, ν) ≤ (L − 1/d) W₂²(µ, ν) with CS26's λ = 1/d − L.
   (For λ > 0 the same line gives µ = ν, which is the "critical ⇒ minimizer" that item 1 rules
   out for CS26's bounds.) Uniqueness of the geodesic from an absolutely continuous µ makes the
   "there exists a geodesic" in (2.5) harmless.

6. *established* — **(c) is no better than trivial unless λ > −1/d.** The trivial bound of
   item 3 is F_ν(µ) ≤ W₂²(µ, ν)/(2d) for every µ. So (c) says something only when |λ| < 1/d,
   i.e. L < 2/d. CS26 give no explicit c(d) in Theorem 4.4 and their L in Lemma 4.1 is a
   Riesz-potential bound that grows with M; nothing in the paper shows L < 2/d is ever reached
   with ν ∈ K. Even when it is, the conclusion is a strict deficit in SW₂² ≤ W₂²/d at a
   critical point, not µ = ν: it does not bear on `conj:sw-critical`.

## What resists

Nothing here moves `conj:sw-critical`. Global λ-convexity is the wrong tool: by item 3, λ > 0
on a class containing ν is a linear SW/W comparison on that class, which fails on the density-
bounded classes where CS26 work (`cand:no-positive-convexity-linf`, sketched). A convexity
route would need convexity only along geodesics from critical points to ν — which is the
conjecture in disguise (it holds for λ > 0 iff those critical points equal ν).

## Proposed next step

Recommendation: **no node, no dossier.** The scouting remark is a comment on CS26's method
(option (b)); its strengthening (a) is false as stated (item 2), true only in the elementary
form λ ≤ 1/d (item 3) or in the sketched L^∞-ball form (item 4), neither of which bears on
`conj:sw-critical`; (c) is correct but non-trivial only if λ > −1/d (item 6). Correct the
scouting file's line "la voie λ > 0 ⇒ (Q) est fermée" to "fermée pour les bornes de CS26 (L ≥ 1/d
dès que ν ∈ K); pour la convexité elle-même, fermée sur les boules L^∞ (esquisse) mais pas sur
toute classe". If a later route needs the SW/W non-comparison on bounded densities, promote
`cand:no-positive-convexity-linf` by writing items 3–4 out with constants.
