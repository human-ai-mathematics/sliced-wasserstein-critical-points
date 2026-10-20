---
# No run, no candidate: a literature check. PDFs were read in the session scratch space,
# never committed. Line numbers are those of `pdftotext -layout` on the arXiv PDF of the
# version named; "PDF p." is the page index of the file, not the printed page number.
---

# Novelty check of the certified special cases before contacting A. Korba

## Question examined

Route `ap:certify-scouting`, lens `mine`, applied to the literature rather than to a proof.
For `thm:gaussian-target`, `thm:radial-d3`, `thm:radial-disc-d2` and `prop:notions-coincide`:
is the statement already in the literature, partly, or apparently new? And has anything
bearing on `conj:sw-critical` appeared after 17 October 2026? This checks **novelty only, not
correctness**. It extends the scouting searches of `verification/13-korba-sw/0-statut.md` §4
(author queries and "sliced Wasserstein" × critical/stationary/flow up to 17 October). New
here:
- full-text reading of the closest papers;
- the slice-matching / IDT line of work (Pitié et al.; Li–Moosmüller(–Wang); Thurin–Boyer–Nadjahi);
- Bonnotte's thesis;
- arXiv listings of 14–20 October 2026.

Sources read in full text (arXiv version given):
- VKM = Vauthier–Korba–Mérigot, arXiv:2502.06525v2 (ICML 2025);
- CS24 = Cozzi–Santambrogio, arXiv:2405.06313v1, the only arXiv version;
- CS26 = arXiv:2610.20972v1;
- DMM = Díaz Martín–Murphy, arXiv:2610.08734v1;
- TBN = Thurin–Boyer–Nadjahi, arXiv:2602.10691v2 (COLT 2026, PMLR 336:6156–6196);
- LMW = Li–Moosmüller–Wang, *Measure transfer via stochastic slicing and matching*, arXiv:2307.05705v3, 13 March 2026;
- LM = Li–Moosmüller, *Approximation properties of slice-matching operators*, arXiv:2310.10869v1;
- Kitagawa–Takatsu, arXiv:2311.15874;
- Park–Slepčev, arXiv:2311.05134;
- the survey arXiv:2508.12519v2;
- Han, *Rigidity and quantitative stability of the sliced Wasserstein deficit*, arXiv:2605.25453v2;
- Ito–Dong, *Sliced Wasserstein steering between Gaussian measures*, arXiv:2604.22807v1;
- Bonnotte's thesis (HAL tel-00946781, 170 pages).

## What we learned

1. *observed* (literature). **`thm:gaussian-target`: apparently new. It is partly known in
   three strictly smaller classes, and its mechanism (Sobolev regularity of the field +
   Stampacchia + trace against Σ) appears nowhere.**
   - *Isotropic target, finite entropy.* CS24 Thm 4.1 (l. 431–436) concerns the flow towards
     N(0, I_d) for ρ₀ of finite entropy. VKM §7 (v2 p. 9, l. 603–606) states the static
     consequence: "if ρ is a standard Gaussian and if µ has finite entropy, then µ = ρ". This
     is `thm:cs-isotropic`. CS24 says explicitly (l. 419–421) that the argument "does not
     generalize to other Gaussian distributions (whose covariance matrix is not a scalar
     multiple of the identity)".
   - *Density comparable to the target.* TBN Prop. 4 (§4.3, l. 482–495; proof in App. C.1,
     l. 1581–1604) takes a reference ν satisfying a Poincaré inequality and µ, σ with
     m ν ≤ µ, σ ≤ M ν. It gives F(σ) ≤ 2C_ν (M/m) ‖∇_{W₂}F(σ)‖_σ, hence "∇F(σ) = 0 iff σ = µ".
     Take ν = target = N(m₀, Σ), which satisfies Poincaré for any Σ ≻ 0. Then every critical σ
     with m ≤ dσ/dN(m₀,Σ) ≤ M is the target. The mechanism is different: flat convexity of
     SW₂², then Poincaré applied to the first variation Ψ. It needs full support and a
     two-sided density bound, which is exactly the class the brief excludes ("supp µ = supp ρ").
     TBN present it (l. 494–495) as Bonnotte's Lemma 5.7.2 without compactness.
   - *Gaussian sources.* TBN Prop. 8 (App. C.2, l. 1607–1611) gives a PL-type inequality
     F(σ)² ≤ ½W₂²(σ,µ)(1 + λ_max(Λ)/λ_min(Σ))‖∇F(σ)‖² for σ = N(0,Σ), µ = N(0,Λ), with Σ, Λ
     arbitrary. Used in App. E.1 (l. 2057–2068), it shows that a *centred Gaussian* critical
     point of an anisotropic centred Gaussian target is the target. Ito–Dong (arXiv:2604.22807)
     stays within Gaussian-to-Gaussian steering.
   - *What TBN still leave open.* TBN's conclusion (§6, l. 758–760) says that the explicit rate
     "requires an isotropic Gaussian target" and that extending it "to general Gaussian targets
     and non-elliptic distributions" remains open. That sentence is about rates, not the static
     question.
   - *Different notion: IDT fixed points.* Pitié–Kokaram–Dahyot (CVIU 2007), restated with
     repairs in Bonnotte's thesis (chapter "Isotropic IDT algorithm", theorem
     "(Pitié–Kokaram–Dahyot)", PDF p. 128), prove that IDT converges to a Gaussian target. The
     proof rests on the tensorisation ν = ⊗ e_i*#ν "for any basis", which holds only for
     isotropic Gaussians, and on finite relative entropy. IDT fixed points (every slice matched
     along a basis) are a stronger condition than v_µ = 0. LMW cites it (v3 l. 167–168:
     "convergence in KL when both σ and µ are Gaussians") and conjectures convergence under
     finite entropy (l. 719–721).
   - *Nothing else found.* DMM (§6, Thm 1 and Example 1, l. 397–430) studies Gaussian
     barycentres and the singular sphere, not uniqueness of a.c. critical points. Han
     (arXiv:2605.25453) studies the deficit d⁻¹W₂² − SW₂², not critical points; it uses an
     anisotropic Gaussian only as a counterexample to a sliced Poincaré–Korn inequality (§5.3).
     No source uses Stampacchia, W^{1,1} regularity of v_µ, or a Σ-weighted trace identity.

   Verdict: **new** as stated (any a.c. µ, holes and unbounded support allowed, no entropy,
   anisotropic Σ, non-centred). It strictly contains three known special cases, which the
   manuscript should cite:
   - isotropic Σ with finite entropy (CS24/VKM);
   - µ two-sided comparable to the Gaussian density (TBN Prop. 4);
   - µ a centred Gaussian (TBN Prop. 8 / App. E.1).

2. *observed* (literature). **`thm:radial-d3`: apparently new.** No source treats radial
   critical points of SW₂² in d = 3. The closest radial material is all singular or
   constructive:
   - the critical sphere (DMM Example 1, l. 418–430 and its appendix proof; recorded here as
     `prop:critical-sphere`);
   - CS24 Example 2 (l. 619–626), a segment with any radial target, which is invariant under
     the flow;
   - VKM Prop. 5.1 (segments; l. 440–450);
   - CS26 Rem. 4.3 (l. 621–630): the unique measures with constant projections are the
     uniform measure on S² for d = 3 and (1 − |x|²)^{-1/2} for d = 2.

   The Archimedes and Abel structure of projections of radial measures is classical
   Radon-transform material, but it is used nowhere for SW critical points. "Abel" occurs in
   none of the sliced-OT texts read except as a substring.

3. *observed* (literature). **`thm:radial-disc-d2`: partially known.** The overlap is
   Bonnotte's thesis, Lemma 5.7.2 (section "Open questions" of the SW-flow chapter, PDF p.
   151). It assumes µ ∈ P(B(0,r)) a.c. with a strictly positive density on the ball, and a
   target ν supported in the same ball. Then ∫ψ'_θ(⟨θ,x⟩)θ dθ = 0 µ-a.e. iff µ = ν. The proof
   is a duality argument: Ψ is Lipschitz with ∇Ψ = 0 a.e., so Ψ is constant on the ball, and
   the c-inequality is integrated against ν.
   - Restricted to radial µ, this covers the case of `thm:radial-disc-d2` where the density of
     µ is positive a.e. on the disc and supp ρ ⊂ disc, in any d.
   - The same idea appears as DMM Cor. 3–4 (l. 529–585): compact convex K, supp µ = K, uniform
     Lipschitz 1-D maps.
   - TBN Prop. 4 handles full support on ℝᵈ, with a density comparable to a reference measure
     that satisfies Poincaré.
   - VKM Prop. 4.6 restates Bonnotte (l. 409–411), as TBN Lemma 2 does (App. B.1, l. 1338–1340).

   Not covered by any of them, hence new:
   - ρ an *arbitrary* radial measure, possibly with support larger than the disc, atoms,
     singular parts, or unbounded support (all of Bonnotte, DMM and TBN need supp ρ ⊂ supp µ in
     some form);
   - µ whose support is the disc but whose density vanishes on a set of positive measure;
   - µ not absolutely continuous (only µ({0}) = 0);
   - R = ∞ with no comparability.

   The method, injectivity of the Abel transform in d = 2, does not appear in the literature
   read.

4. *observed* (literature). **`prop:notions-coincide`: partially known.**
   - *Known part.* "Lagrangian critical ⇒ barycentric critical" for every µ, ρ is VKM Cor. 4.8,
     first sentence (l. 372–375; proof App. B.7, l. 1825–1831), which itself comes from VKM
     Prop. 4.7(b).
   - *Known converse, with stronger hypotheses.* VKM Cor. 4.8, second sentence, needs µ and ρ
     *both compactly supported and without atoms*. Its proof goes through Prop. 4.7(c)
     (l. 366–367; App. B.6, l. 1752ff.), which extends Bonnotte's Prop. 5.1.7 (µ, ρ a.c.,
     compact).
   - *Known equivalence for a.c. µ.* VKM (l. 389–404) note, citing Bonnotte §5.7.1, that for a.c.
     µ (and a.c. ρ) the stationarity condition of the flow is v_µ = 0.
   - *Wasserstein critical points.* VKM define them only in the introduction (l. 70–74) and
     discuss them only for W₂², not for SW₂² (l. 82–91). No result links Wasserstein critical
     points of SW₂² to the other notions.
   - *Near-precedent for step 3 of the dossier.* The dossier's step 3 shows that Id − v_µ is
     cyclically monotone, hence that −v_µ is a geodesic direction. LMW v3 (l. 497–499) prove
     the analogue for a.c. σ: the slice-matching map along an orthonormal basis, and its convex
     combinations with Id, are Brenier maps, hence optimal from σ_k to σ_{k+1}.

   Verdict: part 1 is new for the Wasserstein notion and known (VKM) for the Lagrangian
   notion. Part 2 is a genuine extension of VKM Cor. 4.8: only "µ has no atom" is assumed, with
   no compact support, no condition on ρ, and the Wasserstein notion included.

5. *observed* (literature). **Nothing new on `conj:sw-critical` after 17 October 2026.**
   - arXiv API, abstract searches "sliced" ∧ "Wasserstein" / "optimal transport", submissions
     14–20 October: four papers, of which only CS26 is relevant, and it is already known.
   - arXiv `/list/<cat>/pastweek` for math.OC, math.AP, math.PR, math.FA, math.NA, math.MG,
     math.CA, stat.ML, cs.LG and cs.CV, announcements of 14–20 October: the only
     sliced-Wasserstein titles are CS26, *Vertical Sliced Wasserstein Distances for
     Meta-Measures* (2610.20743) and *Sliced Wasserstein Sketches with Error Certificates*
     (2610.20788). Both abstracts are unrelated.
   - Earlier, previously unlisted papers that touch the question: TBN Prop. 4 and 8 (item 1)
     and LMW Rem. 11 (l. 743–746), which reduces their assumption (A1-ii) to Bonnotte's lemma.
     These are the only additions to the §4 list of the scouting file.
   - The four open-question statements found (VKM §7, CS24 l. 133–136, LMW l. 719–721, TBN §6
     l. 758–760) all still describe the a.c. case as open.

## What resists

- **Paywalled or inaccessible.**
  - Pitié–Kokaram–Dahyot, CVIU 107 (2007): not read; Bonnotte's restatement was used instead.
  - G. Cozzi's Padova master's thesis (thesis.unipd.it, handle 20.500.12608/56021): the
    download returned an HTML page.
  - The Oberwolfach report OWR 2026-13 was not re-read; it was already covered by the
    scouting file.
- **Not queried.** Google Scholar, MathSciNet and zbMATH. This leaves papers that are in no
  arXiv category and conference papers without an arXiv version as residual risk, for example
  NeurIPS/ICML work on slice-matching or SW flows.
- **Indexing lag.** The arXiv API full-text index stopped at submissions of 14 October. The
  listings cover announcements up to 20 October. A paper submitted on 19–20 October and
  announced later is not covered.
- **Bonnotte's thesis.** Its fonts lose all digits under pdftotext. Lemma 5.7.2 is identified
  by the citations of VKM and TBN together with its content on PDF p. 151; the printed page
  number was not read.
- **TBN Prop. 4 not checked for correctness.** It is applied to an unbounded reference ν, while
  their first-variation formula (Prop. 6) is stated under compact support (see their Rem. 8).
  This affects only how strongly we can cite it as prior art.

## Proposed next step

1. The orchestrator adds the bibliography entries listed in the handoff (`deltas`). It asks the
   `writer` to cite, next to `thm:gaussian-target`, the three known subclasses (CS24/VKM, TBN
   Prop. 4, TBN Prop. 8). It also asks for Bonnotte Lemma 5.7.2 and TBN Prop. 4 to be cited
   next to `thm:radial-disc-d2`, and VKM Cor. 4.8 and LMW to be placed precisely next to
   `prop:notions-coincide`. This decides how novelty is presented to A. Korba: the Gaussian
   and radial-d3 results as new, the other two as extensions.
2. Before the contact, a human runs one Google Scholar pass: "cited by" on VKM, CS24 and TBN.
   This is the only uncovered channel, and it would detect a non-arXiv paper on the static
   Gaussian question.
