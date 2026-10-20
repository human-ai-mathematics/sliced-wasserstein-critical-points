---
verdict: pass
authors:
  - researcher, claude-opus-5-5, 2026-10-20
reviewer: reviewer, claude-opus-5-5, 2026-10-20
fingerprints:
  solutions/thm-radial-disc-d2.md: 457f3a0e5e003c13850f964c303b18b3208b056161d8e2cf59849a13c2b42bc2
  thm:radial-disc-d2: 1048aba01cdddde1e4f9b2d1041342da625f5fe41912c599c6b38b2a653d1804
  def:critical-point: 2b3f99b415e32bcde26bf522b879305fe3edffd9318cf15b85f6d1b9699a06a5
---

Certify review of `solutions/thm-radial-disc-d2.md` against `thm:radial-disc-d2`
(`modules/04-special-targets.md`), with `def:sliced-wasserstein`, `def:barycentric-field`,
`def:critical-point` (`modules/01-setting.md`) and the audit tests of
`research/program/brief.md`. Fresh context; I did not write or direct the dossier. Every
step was checked by hand.

## Findings

**Statement agreement.** `thm:sol-rd2-main` assumes ρ ∈ P₂(ℝ²) radial (no density),
µ ∈ P₂(ℝ²) radial with µ({0}) = 0 and supp µ = closed disc of radius R ∈ (0,∞) or ℝ².
The manuscript statement assumes ρ radial in P₂, µ absolutely continuous, radial, with
support a closed disc centred at 0 or the plane. Absolute continuity gives µ({0}) = 0 and
excludes the degenerate disc {0} (its only measure is δ₀). "Invariant under rotations" in
the plane is SO(2)-invariance, the dossier's "radial". Conclusion µ = ρ is identical. The
dossier theorem is strictly stronger and implies the manuscript claim as quantified.

**Normalization.** σ is the uniform probability on S¹, factor d = 2 in v_µ, as in
`def:barycentric-field`. With σ = dφ/2π, v(re₁) = re₁ − (1/π)∫₀^{2π} T(r cos φ)(cos φ, sin φ) dφ;
(2/π)∫₀^π r cos²φ dφ = r; so v(re₁) = −(2/π)∫₀^π h(r cos φ) cos φ dφ · e₁. Folding at π/2
with h odd off E gives the factor 2, s = r cos φ gives (1/r)∫₀^r h(s) s (r²−s²)^{−1/2} ds,
and τ = s² gives ½A[U](r²): total −(2/(πr))A[U](r²). All constants verified; only the
non-vanishing of the prefactor matters.

**Steps checked.**

- (Q1), (Q2): correct, including right continuity and the identity F(Q(u)) = u for
  continuous F.
- `lem:sol-rd2-projection`: the Haar-averaging/Tonelli disintegration ν(B) = ∫λ_{|x|}(B)dν
  is correct; a line {x₁ = t} meets each circle of positive radius in ≤ 2 points, so
  ν₁ has an atom only at 0, of mass ν({0}). Fourier uniqueness via ν̂(tθ) = ν̂₁(t) is correct.
  Rotation invariance of the support is correct.
- `lem:sol-rd2-monotone`. Part 1: positivity of F, 1 − F on (−R,R) uses only R = sup|supp µ|
  and part 4; strict increase on (−a,a) uses B(0,a) ⊂ supp µ. Part 2: µ₁((−R,R)) = 1, with
  µ₁({±R}) = 0 from atomlessness — this correctly covers mass on the boundary circle.
  Part 3 (scrutinized): G(t) = 1 − G((−t)⁻) from symmetry of ρ₁; Q(1−u) = −sup{w : G(w⁻) ≤ u};
  the two inclusions identifying this supremum with Q⁺(u) are correct; Q⁺ is finite on (0,1);
  Q ≤ Q⁺ everywhere, and Q < Q⁺ forces G ≡ u on a nonempty open interval, these intervals are
  disjoint, so C is countable; F injective on (−a,a) makes E = F⁻¹(C) ∩ (−a,a) countable.
  Oddness T(−s) = −T(s) off E follows from F(−s) = 1 − F(s). Correct for arbitrary radial ρ,
  including atoms of ρ₁ (where Q, Q⁺ agree) and flat parts of G (the countable C).
- `lem:sol-rd2-continuous` (scrutinized). Part 1: local boundedness of T plus countability
  of {θ : ⟨x,θ⟩ ∈ D} for x ≠ 0 and dominated convergence give continuity on B(0,R)∖{0}.
  Part 2: for a jointly Borel version g, the set N is Borel; each θ-section has µ-measure
  ≤ µ₁({s ∈ (−R,R) : g(θ,s) ≠ T(s)}) = 0 (the dossier writes "=" for the first relation; the
  set {|x| < R} is smaller than {|⟨x,θ⟩| < R}, so it is "≤", which is all that is needed);
  Tonelli gives v = v_µ µ-a.e. on B(0,R). The remark on other quantile versions is correct
  (F_#µ₁ uniform). Part 3: criticality is used only as "v_µ = 0 µ-a.e."; the set
  {x ∈ B(0,a)∖{0} : v(x) ≠ 0} is open (part 1), µ-null, and contained in supp µ, hence empty.
  This is exactly the passage through supp µ the brief requires; no use of the condition off
  supp µ, and µ-mass on the circle |x| = R is never needed.
- `lem:sol-rd2-reduction`: computation verified above; U Borel and locally bounded on [0,R²).
- `lem:sol-rd2-abel` (scrutinized). Tonelli bound ∫₀^y|U|·2√(y−τ) dτ < ∞ gives A[U] ∈
  L¹_loc([0,X)) and a.e. absolute convergence; substitution x = τ + (y−τ)u gives the Beta
  integral π; absolute integrability π∫₀^y|U| < ∞ licenses Fubini; ∫₀^y A[U](x)(y−x)^{−1/2}dx
  = π∫₀^y U; vanishing for all y < X and Lebesgue differentiation give U = 0 a.e. Only
  U ∈ L¹_loc([0,X)) is used; X = ∞ is allowed.
- Proof of `prop:sol-rd2-local`: A[U](x) = 0 for every x ∈ (0,a²) since the prefactor
  −2/(πr) ≠ 0; U = 0 a.e. ⇒ h = 0 a.e. on (0,a) (change of variables correct); density of a
  co-null set plus monotonicity squeeze gives T = Id on (0,a); on (−a,0)∖E oddness gives
  T(s) = −T(−s) = s, then the squeeze again; T(0) = 0 by squeeze. Correct.
- Proof of `thm:sol-rd2-main`: a = R, T = Id on (−R,R) which carries µ₁, so ρ₁ = T_#µ₁ = µ₁ and
  ρ = µ by the projection lemma. Correct.

**Hypotheses.** Used: radial ρ ∈ P₂ (projections equal and symmetric; Fourier step);
radial µ with µ({0}) = 0 (atomless µ₁: continuity of F, γ̄_θ = T, (Q2)); B(0,R) ⊂ supp µ and
R = sup|supp µ| (positivity/strict monotonicity of F, the open-set argument, the Abel equation
on an interval starting at 0). Stated but unused in the manuscript statement: absolute
continuity of µ (only µ({0}) = 0 is needed) and any condition on ρ beyond radial ∈ P₂ — the
dossier already records this sharpening. No unstated hypothesis found.

**Unbounded R, boundary mass.** R = ∞ handled (X = ∞, T only locally bounded). Mass on the
circle |x| = R is allowed and harmless: it does not affect µ₁((−R,R)) = 1, and the proof never
evaluates v on that circle.

**Audit tests of the brief.**

- *Sphere test (circle r_*S¹, ρ = N(0,I₂)).* µ({0}) = 0 and µ₁ is atomless; the proof breaks
  at `lem:sol-rd2-continuous` part 3 / `prop:sol-rd2-local`, which need some a > 0 with
  B(0,a) ⊂ supp µ — i.e. at the support hypothesis. It does not "prove" the circle
  non-critical. Passes.
- *Segment test.* A measure carried by a segment is radial only if it is δ₀; outside the
  hypotheses. Passes.
- *Atom at 0.* δ₀ excluded by µ({0}) = 0 (and by the support). An atom of ρ (at 0 or
  elsewhere, through ρ₁) is allowed and correctly handled by the Q/Q⁺ argument. Passes.
- *Annulus.* Not claimed; the remark's reason (Abel equation only on (c², R²)) is correct, and
  the family U = (1/π)A[Φ′], A[U] = Φ, U(x) = −(1/2π)∫Φ(σ)(x−σ)^{−3/2}dσ for x ≥ c², was checked.
- *Unbounded supports, fat Cantor supports, irregular densities.* Only closed-support
  information and local boundedness of T are used; no integration by parts against µ.
- *Atoms of µ_θ.* Excluded by µ({0}) = 0 for every θ.

**Remarks.** `rem:sol-rd2-bonnotte` states the overlap with `thm:bonnotte-full-support`
correctly: that theorem needs µ and ρ absolutely continuous on one bounded ball with densities
positive on it; radial pairs of that kind are covered by both; the dossier's theorem
additionally covers R = ∞, ρ singular or charging outside the disc, densities of µ vanishing on
positive-measure sets, and non-absolutely-continuous µ with µ({0}) = 0; Bonnotte covers
non-radial pairs. "Neither contains the other" is correct, and the Gaussian aside agrees with
`thm:gaussian-target` (d = 2, any a.c. µ). The sketches are clearly marked as not claimed:
the atom-at-0 extension ("Not closed here … does not claim it") and the annulus monotonicity
paragraph ("checked only in outline and are not used anywhere").

**Dependencies.** The proof uses only the three definitions and classical results
(Tonelli/Fubini, Fourier uniqueness, Beta integral, Lebesgue differentiation), all used
within their standard hypotheses. No open node is used: `prop:critical-sphere`,
`prop:notions-coincide`, `thm:bonnotte-full-support`, `thm:gaussian-target` appear in remarks
only. The ledger lists `depends_on: [def:critical-point]`, which reaches
`def:barycentric-field` and `def:sliced-wasserstein` transitively; the fingerprints therefore
cover only `def:critical-point` directly, as the checker prints them. Fences: the node has no
`bounded_by`; the target's fences (`prop:critical-sphere`, `prop:critical-segments`) are
respected, as above.

**Build.** `uv run scripts/check.py` reports no FAIL and no MyST error for the dossier.

**Non-blocking observations** (for a later editorial pass; none affects the proof).

1. Line 243–245: "its section has µ-measure µ₁(…) = 0" should read "≤ µ₁(…) = 0".
2. `rem:sol-rd2-circle` (line 399–400) says the circle is critical "by
   [](#prop:critical-sphere)"; that node is `open` in the ledger (a preprint not yet checked
   here). The remark is an audit, not used in the proof, and its conclusion (where the proof
   breaks) does not depend on the circle being critical; but the sentence should say the
   criticality is the preprint's claim, not established here.

## Corrections

None.

## Exclusions

Not certified here: the extension to µ with an atom at 0 sketched in `rem:sol-rd2-atom`; every
claim of `rem:sol-rd2-annulus` beyond the Abel identity (monotonicity of Id + εh, positivity of
the inverse transform, `cand:annulus-d2`); the criticality of the circle (`prop:critical-sphere`);
the comparison claims of `rem:sol-rd2-bonnotte` beyond the logical overlap of the statements;
and `conj:sw-critical` itself, of which this is a special case excluded by the brief's
completion criteria (radial, d = 2, no holes).
