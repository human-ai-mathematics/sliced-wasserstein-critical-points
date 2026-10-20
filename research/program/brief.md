---
target: conj:sw-critical
---

# Problem brief

The harness remembers, validates and certifies; it does not supply mathematical pressure.
This file does: it knows how the target usually fails, what would count as finishing, and
which disguises a dead route wears. It owns none of the mathematics — the statement lives in
`modules/`, its status in the ledger.

## The target

`conj:sw-critical`, stated at `:label: conj:sw-critical` in `sec:target` — read it there;
this file never copies it. It is the question of Vauthier–Korba–Mérigot (arXiv:2502.06525v2,
§7), with the normalizations of `def:sliced-wasserstein`, `def:barycentric-field` and
`def:critical-point`. By `prop:notions-coincide`, the barycentric notion used in the statement
agrees with the Lagrangian and Wasserstein notions for an atomless µ, in particular an absolutely continuous one; a proof
may work with any of them once that node is certified, and must say which it uses.

Where the statement is vulnerable:

- **The condition holds only µ-almost everywhere.** Nothing is asked off supp µ. Every
  difficulty lives in the holes of supp µ relative to supp ρ; a proof that uses the condition
  on all of supp ρ, or on the convex hull of supp µ, assumes what it must prove.
- **Absolute continuity of µ is essential, not technical.** `prop:critical-sphere` is a
  critical point with absolutely continuous projections; `prop:critical-segments` are critical
  points of dimension one. Absolute continuity of the projections µ_θ is *not* enough.
- **Absolute continuity of ρ** is the article's hypothesis and is kept in the target. The
  statement makes sense for every ρ ∈ P₂ (see Neighbourhood).
- **Normalization.** σ is the uniform *probability* on S^{d−1}; the factor in v_µ is d, so
  that v_ρ = 0. VKM's equation (16) prints 1/d, and its Proposition 4.7(c) writes
  φ'(0) = 2⟨v_µ, ξ⟩ where (2/d)⟨v_µ, ξ⟩ is correct. Neither affects a zero set, but a
  quoted constant from the article must be renormalized before use.

## The exact negation

There exist d ≥ 2, an absolutely continuous ρ ∈ P₂(ℝᵈ) and an absolutely continuous
µ ∈ P₂(ℝᵈ) with µ ≠ ρ and v_µ = 0 µ-almost everywhere.

**One witness suffices**, since the statement is universal with no uniform constant. But the
witness must be exact: a numerical near-critical point, however small its residual, refutes
nothing, and the near-critical points found so far all degenerate towards singular measures
as the resolution grows. A refutation needs an analytic µ and ρ and a hand-checked
verification of v_µ = 0 on supp µ.

## What counts as complete

**A complete proof** establishes `conj:sw-critical` for every d ≥ 2 and every absolutely
continuous ρ ∈ P₂. None of the following counts: radial measures; Gaussian or log-concave
targets; compactly supported µ or ρ; µ of finite entropy, or with a smooth or bounded
density; supp µ = supp ρ, or supp µ with no holes; a single dimension; a result conditional
on an open statement.

**A complete refutation** negates the exact quantified statement through a certified
dossier, with `refuted_by` naming a proved refuter: one explicit pair (µ, ρ) as in the
negation.

## Edge cases and audit tests

A reviewer checks every proof against these:

- **The sphere test.** Apply the argument to the uniform measure on r_*S^{d−1} with
  ρ = N(0, I_d) (`prop:critical-sphere`; r_* = 3/√π for d = 3, see `sec:overview`). It is
  critical, so a correct proof must break exactly where it uses absolute continuity of µ.
  The first scouting sketch of the radial case in d = 3 failed this test: it "proved" that the
  sphere is not critical.
- **The segment test.** The same with `prop:critical-segments`.
- **Atoms.** δ₀ is critical for every radial ρ (v(0) = 0 trivially); an argument on radial
  measures must exclude an atom at 0 of µ, and may allow one for ρ.
- **Unbounded supports.** µ and ρ need not be compactly supported: monotone maps T_θ may be
  unbounded, and quantities like G(r) = ∫₀^r (T − Id) u du are finite only for r < sup supp.
- **Fat Cantor supports.** supp µ may have countably many dense holes, with positive
  Lebesgue measure; any argument hole by hole must hold for them.
- **Irregular densities.** µ ≪ Leb gives no regularity of its density: no integration by
  parts against µ (the Gaussian argument uses Sobolev regularity of v_µ instead).
- **Directions where µ_θ has atoms.** Impossible for µ ≪ Leb, but an argument that passes to
  limits of measures may meet them; then γ̄_θ, not T_θ, is the right object.

## Traps and circular reductions

- **Entropy and flow arguments.** Cozzi–Santambrogio's dissipation identity needs finite
  entropy (`thm:cs-isotropic`); an argument through the flow must not assume the flow from µ
  is well posed or stays absolutely continuous without proving it.
- **Reducing to the projections.** "Every µ_θ is determined" is the conclusion, not a step:
  for the sphere all µ_θ are absolutely continuous and differ from ρ_θ.
- **Even dimension.** For radial measures, H_d' = 2m r H_{d−2} lets one descend from d to d − 2
  but, in even dimension, only down to the Abel condition of d = 2, never to the local
  condition of d = 3.
- **Numerical floors.** The 2D solver (`research/lib`) maps near-critical points well; it does
  not decide a singular limit, and a residual floor that is stable under refinement is
  evidence of no critical point nearby, not a proof.
- **Linearization.** Around µ = ρ the linearized problem is rigid on every mesh tested; a
  linear result says nothing about large perturbations.

## Neighbourhood

- `thm:gaussian-target`, `thm:radial-d3`, `thm:radial-disc-d2`, `prop:notions-coincide` —
  special cases and the equivalence of notions, with scouting arguments to certify first.
- `cand:annulus-d2` — the smallest configuration outside every proved case.
- `cand:odd-d-sign-changes` — the radial case in odd d ≥ 5.
- `cand:score-gluing-gaussian` — why the Gaussian argument stops at Gaussians.
- `cand:balayage-singular-layer` — the mechanism suggested by the numerical search for a
  counterexample.
- The version for an arbitrary ρ ∈ P₂ (no density) — a strengthening worth a candidate
  once a route needs it: the radial d = 3 argument already allows any radial ρ.

## Budget policy

The honest outcome — unresolved, with certified special cases and the exact remaining
obstacles — is permitted. Stop when no route is left worth running, not on a clock. Heavy
computation (a cloud VM) is decided by the orchestrator per mission, with the run committed
before it is launched.
