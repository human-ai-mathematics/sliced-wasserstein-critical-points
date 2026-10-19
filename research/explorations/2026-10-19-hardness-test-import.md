---
artifacts:
  - research/runs/2026-10-19-solver-validation.jsonl
candidates:
  - id: cand:annulus-d2
    statement: >-
      Let ρ ∈ P₂(ℝ²) be radial and µ ∈ P₂(ℝ²) radial and absolutely continuous, with the law
      of |X|, X ∼ µ, supported on [c, R] for some 0 < c < R ≤ ∞. If µ is a critical point of
      SW₂²(·, ρ) (def:critical-point), then µ = ρ.
  - id: cand:odd-d-sign-changes
    statement: >-
      Let d ≥ 5 be odd, ρ ∈ P₂(ℝᵈ) radial and µ ∈ P₂(ℝᵈ) radial with the law of |X| atomless,
      and let T be the monotone map between their common projections. If µ is a critical
      point of SW₂²(·, ρ), then on every bounded component (a, b) of [0, sup supp|X|) minus
      supp|X|, the function T − Id changes sign at most (d − 3)/2 times.
  - id: cand:score-gluing-gaussian
    statement: >-
      Let ρ ∈ P₂(ℝᵈ), d ≥ 2, have a positive C² density, and let M : ℝᵈ → ℝ^{d×d} be a
      measurable field of symmetric positive definite matrices such that, for every θ, both
      θᵀM(x)θ and ⟨M(x)∇log ρ(x), θ⟩ depend on x only through ⟨x, θ⟩. Then M is constant and
      ρ is Gaussian.
  - id: cand:balayage-singular-layer
    statement: >-
      Let K ⊂ ℝ² be compact, the closure of its interior, and ν ≠ 0 a finite positive measure
      supported in a bounded component of ℝ² ∖ K. There is no finite signed measure λ on K,
      absolutely continuous, with λ(K) = −ν(ℝ²) and the potential |x| ∗ (ν + λ) constant on K.
      (First-order form of criticality for ρ = µ + ε(ν + λ), with mass ν in a hole of supp µ.)
---

# Founding checkpoint: the scouting hardness test of 17 October 2026

## Question examined

Whether `conj:sw-critical` resists one budgeted agent attempt, and what it leaves. This
checkpoint imports the result of the hardness test run on 17 October 2026, before this
repository existed, in `ensae-conjecture-scouting/verification/13-korba-sw/` (sibling
directory of this repository; the paths below are relative to it). Six agents: a status
check of the literature, an adversarial reading of two earlier claims, three routes
(radial in d = 2, a counterexample search in d = 2, anisotropic Gaussian targets), and an
adversarial reading of the Gaussian route. None of it was certified by a human, and none of
those readings is a review in this repository's sense.

## What we learned

- *established* — `prop:notions-coincide`, without compact support and for any ρ ∈ P₂
  (`1-relecture.md`, §2). The key step is that −v_µ is the direction of a Wasserstein
  geodesic, by cyclical monotonicity of x ↦ d∫γ̄_θ(⟨x,θ⟩)θ dσ.
- *established* — `thm:gaussian-target`, for any Σ ≻ 0 and any d, without entropy
  (`C-gaussiennes-anisotropes.md`, §4; adversarial reading `C-relecture-adverse.md`, verdict
  correct at 85 %). Reservations: the Fubini and measurability step of §4 is to be written
  out; the sketches of §§2(c)–(d), 5 and 6 are sketches; novelty is unchecked.
- *established* — `thm:radial-d3`, for µ_rad atomless and any radial ρ (`1-relecture.md`,
  §3, corrected proof). The earlier sketch it corrects was wrong: it excluded the sphere.
- *established* — `thm:radial-disc-d2` (`A-radial-d2.md`, §2, (P1)).
- *established* — in d = 2, criticality on an annulus does not force T = Id: for any
  Φ ∈ C_c^∞(0, c²), U = (1/π)A[Φ′] solves the Abel condition on the whole annulus
  (`A-radial-d2.md`, (P3)). What remains is the positivity of an inverse Abel transform in
  the hole: `cand:annulus-d2`.
- *established* — for radial measures, the condition is H_d(r) = ∫₀^r h(u) u (r² − u²)^m du = 0
  on the radial support, m = (d − 3)/2; locality survives in odd d (descent to H₃), convexity
  of T on holes survives only in d = 3 (`1-relecture.md`, §4). Hence `cand:odd-d-sign-changes`.
- *established* (sketch) — the Gaussian argument needs ⟨M∇log ρ(x), θ⟩ to depend only on
  ⟨x, θ⟩ with M constant, which forces ρ Gaussian (`C-gaussiennes-anisotropes.md`, §6): the
  constant case of `cand:score-gluing-gaussian`.
- *observed* — the 2D solver is validated: J ≤ 3·10⁻¹⁴ for µ = ρ, and the segments of
  `prop:critical-segments` give J ≈ 10⁻¹³ at L = 1024. Reproduced at smaller scale, with
  provenance, by `research/runs/2026-10-19-solver-validation.jsonl`, which also finds the
  three-dimensional critical radius of `prop:critical-sphere` equal to 3/√π to 10⁻¹¹.
- *observed, not reproduced here* — counterexample search (`B-contre-exemple.md`, on a cloud
  VM, results in `voie-b/resultats/`): with imposed support S ⊊ supp ρ, the minimizers of F
  on P(S) are never absolutely continuous (62–100 % of the mass in a boundary layer of
  width 0.03); residual floors from 3·10⁻⁴ to 0.6, stable under refinement; the linearized
  compensation on supp µ is not a measure (‖η‖_{L¹} ≈ h^{−0.5}). Inconclusive only for a
  target mass m_H ≤ 0.05 in a hole. Hence `cand:balayage-singular-layer` and
  `ap:small-mass-hole`.
- *observed* — literature status (`0-statut.md`): Díaz Martín–Murphy (arXiv:2610.08734),
  Oberwolfach Report 13/2026 and Cozzi–Santambrogio (arXiv:2610.20972) do not settle
  `conj:sw-critical`; the first supplies `prop:critical-sphere`.

## What resists

- In d = 2, the non-local positivity condition on an annulus, with no known linear
  certificate: `cand:annulus-d2`.
- Beyond Gaussian targets, the gluing of the projected scores: `cand:score-gluing-gaussian`.
- A counterexample: sweeping by the kernel |x| produces singular layers on ∂ supp µ, never a
  density (`cand:balayage-singular-layer`); every known spurious critical point is singular.

## Proposed next step

Certify the scouting arguments first (`ap:certify-scouting`), starting with
`thm:gaussian-target`: it is the strongest result and the one to show A. Korba. In parallel,
`ap:radial-annulus-d2` is the route most likely to give a new idea for supports with holes.
The other routes open with this checkpoint: `ap:radial-odd-d` (on `cand:odd-d-sign-changes`),
`ap:non-gaussian-targets` (on `cand:score-gluing-gaussian`) and `ap:small-mass-hole` (the
inconclusive regime of the counterexample search).
