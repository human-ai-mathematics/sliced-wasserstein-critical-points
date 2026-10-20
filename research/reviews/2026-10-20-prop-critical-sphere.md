---
verdict: revise
authors:
  - researcher, claude-opus-5-5, 2026-10-20
reviewer: reviewer, claude-opus-5-5, 2026-10-20
fingerprints:
  solutions/prop-critical-sphere.md: dec472991c2b19265cfc6aaee702e7f54af9cda4fcba0c2eb9e6a08e893dfb37
  prop:critical-sphere: f38d6569332b241f838753fa390b692cd910b90870629030d10b129996fa8dec
  def:critical-point: 2b3f99b415e32bcde26bf522b879305fe3edffd9318cf15b85f6d1b9699a06a5
  prop:notions-coincide: 75847c27e7b0052fc43c8abf198988644a0b57da282b0226d71e368cbd3caf2d
---

Certify review of `solutions/prop-critical-sphere.md` against `prop:critical-sphere`
(`sec:singular`), with `def:sliced-wasserstein`, `def:barycentric-field`,
`def:critical-point` and the current statement of `prop:notions-coincide` (item 2: "If µ
has no atom, the three notions … coincide"), and against the source
DiazMartinMurphy2026 (arXiv:2610.08734v1). Fresh context: I did not write or direct the
dossier and have not seen the conversation that produced it.

**Verdict: revise.** Every mathematical step is correct, and the theorem implies the
manuscript claim. The verdict is `revise` for one structural defect: the proof rests on two
statements internal to another dossier (`thm:sol-nc-main` part (b) and item 5 of
`lem:sol-nc-version`, in `solutions/prop-notions-coincide.md`), which are not ledger nodes,
are not covered by this certification's fingerprints, and belong to a dossier whose
certification has lapsed; and the dossier's remark `rem:sol-cs-refined` now makes a false
statement about the manuscript. Both are repaired by citing the current manuscript
statement of `prop:notions-coincide` and proving version independence inline (a few lines;
see Corrections). The repair touches no computation, so a re-review can be short.

## Findings

**Statement agreement.** Manuscript claim: for $d \ge 2$, $\rho = N(0,I_d)$, there is
$r_* > 0$ with $\mathrm{Unif}(r_*\Sph{d-1})$ a Wasserstein critical point
(`def:critical-point`, item 3). `thm:sol-cs-main` item 3 gives this with $r_* = dA_d > 0$
(item 1), plus uniqueness of the radius, the Lagrangian notion, $\mu_{r_*} \ne \rho$ and
$r_* = 3/\sqrt\pi$ for $d = 3$. Quantifiers ($\forall d \ge 2$, $\exists r_*$) and the
normalization (σ a probability, factor $d$ in $v_\mu$) match. A stronger theorem; allowed.

**Lemma `lem:sol-cs-projection` (law of Z).** Checked. $O(d)$-invariance gives one law
$\zeta_d$. No atom: each level set $\{\inner{e}{\theta} = t\}\cap\Sph{d-1}$ is empty, a point,
or a $(d-2)$-sphere (two points for $d=2$), of finite $\mathcal H^{d-2}$ measure, hence
$\mathcal H^{d-1}$-null. Symmetry from $-I_d$; $H(0) = 1/2$ uses the no-atom item.
$\E Z^2 = 1/d$ by coordinate permutations. $0 < H < 1$ on $(-1,1)$: the open caps
$\{\inner{e}{\theta} < t\}$, $\{> t\}$ are nonempty relatively open, so of positive σ-measure.
Projections of $\mu_r$ are the law of $rZ$ with CDF $H(\cdot/r)$; $\mu_r$ has no atom
($\sigma(\{e\}) \le \Prob(Z=1) = 0$). Correct.

**Lemma `lem:sol-cs-constant` ($0 < A_d < d^{-1/2}$).** Checked. $\tau = \Phi^{-1}\circ H$
is well defined and nondecreasing on $(-1,1)$; $\abs Z < 1$ a.s., $H$ continuous, so $H(Z)$
is uniform on $(0,1)$ and $\tau(Z) \sim N(0,1)$. $t\tau(t) \ge 0$ with $\tau(0) = 0$;
$\{Z = 0\}$ and $\{\tau(Z) = 0\}$ are null, so $Z\tau(Z) > 0$ a.s. and $A_d > 0$.
Cauchy–Schwarz gives $A_d \le d^{-1/2}$ (and finiteness); equality would force
$\tau(Z) = \lambda Z$ a.s., impossible since $\abs{\lambda Z} \le \lambda$ while a Gaussian is
unbounded. Hence $0 < r_* = dA_d < \sqrt d$. Correct.

**Lemma `lem:sol-cs-field` (the field).** Checked line by line.
- Monotone maps: $\rho_\theta = N(0,1)$, $Q_{\rho_\theta} = \Phi^{-1}$ on $(0,1)$,
  $F_{(\mu_r)_\theta}(s) = H(s/r) \in (0,1)$ for $\abs s < r$, a set of full
  $(\mu_r)_\theta$-measure; by `def:barycentric-field`, $\bar\gamma_\theta = \tau(\cdot/r)$
  $(\mu_r)_\theta$-a.e. Correct.
- Version $g(\theta,s) = \tau(s/r)\one_{\abs s<r}$: Borel on $\Sph{d-1}\times\R$, a version of
  $\bar\gamma_\theta$ for every θ. For $x = re$, $\abs{\inner{x}{\theta}} = r$ only at
  $\theta = \pm e$, σ-null, so the integrand is $\tau(\inner{e}{\theta})\theta$ σ-a.e.
  Correct. The independence of the field from the chosen jointly Borel version is
  imported from item 5 of `lem:sol-nc-version` (see *Defect* below). I checked that it
  holds: if $g, \tilde g$ are Borel versions, Tonelli gives
  $\int\!\!\int \abs{g - \tilde g}(\theta,\inner{x}{\theta})\dd\sigma\dd\mu(x)
  = \int\!\!\int \abs{g-\tilde g}(\theta,s)\dd\mu_\theta(s)\dd\sigma(\theta) = 0$, so for
  µ-a.e. $x$ the two integrands agree σ-a.e. (integrability of each integrand for µ-a.e.
  $x$ being part of the definition of $v_\mu$; here it is verified directly for every
  $x$ on the sphere).
- Integrability: $\int \tau(\inner{e}{\theta})^2\dd\sigma = \E\tau(Z)^2 = 1$; with
  $\abs\theta = 1$ and σ a probability the vector integral converges absolutely. Correct.
- Reflection: $S = I - 2uu^\top$, $u \perp e$, is symmetric orthogonal with $Se = e$,
  $Su = -u$; the integrand $f(\theta) = \tau(\inner{e}{\theta})\inner{u}{\theta}$ satisfies
  $f(S\theta) = -f(\theta)$ and σ is $S$-invariant, so $\inner{u}{I(e)} = 0$; $S$ preserves
  the null set $\{\pm e\}$ where τ is undefined. Correct.
- Radial component $\E[Z\tau(Z)] = A_d$, so $v_{\mu_r}(re) = (r - dA_d)e$ at every point
  of the sphere, hence $(1 - r_*/r)x$ $\mu_r$-a.e. Correct.

**Proof of `thm:sol-cs-main`.** Item 3: $(1 - r_*/r)x = 0$ with $\abs x = r > 0$ iff
$r = r_*$; so $\mu_r$ is a critical point (`def:critical-point`, item 1) iff $r = r_*$.
Passage to the Wasserstein notion: $\mu_{r_*}$ has no atom, so by the **current manuscript
statement** of `prop:notions-coincide`, item 2, the three notions coincide for it, and it is
a Lagrangian and a Wasserstein critical point. The dossier makes this passage instead through
`thm:sol-nc-main` (b) of the other dossier, which states the same implication; the
manuscript statement, fingerprinted above, supplies everything used. For $r \ne r_*$,
item 1 of `prop:notions-coincide`. $\mu_{r_*} \ne \rho$ since the sphere is Lebesgue-null.
Correct. (Correctness of `prop:notions-coincide` itself is outside this review; its
certification is being renewed separately, and this proof is only as good as that node —
`depends_on` records it.)

**Lemma `lem:sol-cs-d3` ($r_* = 3/\sqrt\pi$).** Checked. Archimedes:
$\sigma(\{a < \theta_3 \le b\}) = \frac{1}{4\pi}\cdot 2\pi\,[-\cos\phi]_{\arccos b}^{\arccos a}
= (b-a)/2$, so $H(t) = (1+t)/2$, and $\Phi(G) = H(Z)$ gives $Z = 2\Phi(G) - 1$ a.s. Then
$A_3 = 2\E[G\Phi(G)] = 2\int z\varphi\Phi$; with $z\varphi = -\varphi'$, integration by parts
gives $\int\varphi^2 = \frac{1}{2\pi}\sqrt\pi = \frac{1}{2\sqrt\pi}$ (boundary term vanishes).
$A_3 = 1/\sqrt\pi$, $r_* = 3/\sqrt\pi \approx 1.693 < \sqrt 3$, consistent with item 1 and
with the hand computation of `sec:overview`. Correct.

**Remarks.** `rem:sol-cs-formula`: the $d = 2$ quantile $Q_{\zeta_2}(u) = -\cos(\pi u)$
follows from $H(t) = 1 - \arccos(t)/\pi$; correct; not used by the proof.
`rem:sol-cs-density`: classical, explicitly not used.

**Hypotheses.** Used: $d \ge 2$ (no atom of ζ_d; for $d = 1$ the "sphere" is two atoms),
$\rho = N(0,I_d)$ (isotropy: one monotone map for all θ; Gaussian quantile). None unstated;
none stated and unused.

**Fences.** `prop:critical-sphere` has no `bounded_by`. It is itself a fence of
`conj:sw-critical`; consistent, since $\mu_{r_*}$ is singular. Sphere test of the brief: the
result is the sphere test's object, and it is consistent with `prop:notions-coincide`
(atomless, critical in all three senses).

**Imported result: comparison with the source.** I read arXiv:2610.08734v1, Example 1
(text l. 529–539: statement and proof sketch), the Standing Assumptions and Proposition 1
(l. 297–335), and the appendix "Details for Example 1" (l. 2788–2949).
- *Normalization.* The source takes $F = \tfrac12\SW_2^2(\cdot,N(0,I_d))$ with σ the
  uniform probability, and $\nabla_{W_2}F(\mu)(x) = \int (x\cdot\theta - T_\theta(x\cdot\theta))
  \theta\dd\sigma(\theta) = v_\mu(x)/d$ by $\int\inner{x}{\theta}\theta\dd\sigma = x/d$. Its
  radial component at $re_1$ is $r/d - A_d$ with
  $A_d = \int\Phi^{-1}(H(\theta_1))\theta_1\dd\sigma$, root $r_* = dA_d$: the same constant
  and the same $r_*$ as the dossier. Agreement confirmed.
- *Their notion.* "Wasserstein critical point" in the source means vanishing of the
  gradient of their Proposition 1, which identifies the derivative of
  $t \mapsto F((\Id + tv)_\#\mu)$ for $v \in C^1_c(\R^d;\R^d)$, under the standing assumption
  that σ-a.e. projection is atomless. This is a Lagrangian notion with smooth test fields,
  not the geodesic notion of `def:critical-point`, item 3. The dossier's
  `rem:sol-cs-source` says so correctly, and does not use Proposition 1. I did not check
  the proof of Proposition 1 (appendix, l. 1228 ff.); nothing here depends on it.
- *Their proof.* Correct in outline: projections $rZ$, monotone map $\Phi^{-1}(H(s/r))$,
  $O(d)$-equivariance making the field at $re_1$ parallel to $e_1$ and transporting the
  zero to the whole sphere. It asserts, without proof, that $A_d$ is finite and strictly
  positive; the dossier proves it (`lem:sol-cs-constant`). It gives no value of $r_*$.
  The dossier's comparison (`rem:sol-cs-source`) is accurate in every point; no
  discrepancy affecting the result.

**`references` on the node.** Appropriate to keep. The dossier is a complete, independent
proof (it does not use the source), so certification does not rest on the preprint; the
key records attribution, the source's proof agrees with the dossier as checked above, and
the display "Proved (from a preprint)" — a source's result checked here — is accurate.
Note that the source is a 6 October 2026 preprint and not *established*: without a
`proofs` record the node must stay `open`.

**Defect (reason for `revise`).**
1. *Dependence on unfingerprinted statements of another dossier.* Overview step 4
   (l. 33–37), *Dependencies* (l. 42–48), the proof of `lem:sol-cs-field` (l. 230–231) and
   the proof of item 3 (l. 316–321) rest on `thm:sol-nc-main` (b) and item 5 of
   `lem:sol-nc-version` of `solutions/prop-notions-coincide.md`. SPECIFICATION.md
   (*Proof records and dossiers*) allows a dossier to cite *certified nodes*; these two are
   not nodes, their text is not fingerprinted with this certification, and an edit of that
   dossier (whose certification is currently lapsed and being renewed) would silently
   change what this proof rests on. The node statement now suffices for the first, and the
   second is a few lines of Tonelli.
2. *False remark.* `rem:sol-cs-refined` (l. 334–349) states that the manuscript statement of
   `prop:notions-coincide` gives the passage only for absolutely continuous µ, and calls its
   dossier "certified" (also l. 43, l. 340). The current statement covers atomless µ, and
   that certification has lapsed. A certified text must not assert this.

## Corrections

None applied (the reviewer does not edit the dossier). Repairs required are in the
handoff's `next`.

## Exclusions

- `prop:notions-coincide` (its proof and dossier) is not checked here; its certification is
  being renewed separately. This proof uses only its manuscript statement as fingerprinted
  above (once repaired).
- Proposition 1 of DiazMartinMurphy2026 and its proof are not checked; the dossier does
  not use them.
- `rem:sol-cs-density` (the density of ζ_d and its Gaussian limit) and the claim in
  `rem:sol-cs-formula` that no closed form is addressed for $d \ne 3$ are not certified.
- The stability or instability of the critical sphere, and whether it is a local
  minimizer, are not addressed by the dossier and not certified.
