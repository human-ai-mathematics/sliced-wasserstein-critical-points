---
verdict: pass
authors:
  - researcher, claude-opus-5-5, 2026-10-20
reviewer: reviewer, claude-opus-5-5, 2026-10-20
fingerprints:
  solutions/prop-critical-sphere.md: bd47ad6d544d33efd5ab2ff430724895f90b0ab462493ef038496db2c6a2e5e6
  prop:critical-sphere: f38d6569332b241f838753fa390b692cd910b90870629030d10b129996fa8dec
  def:critical-point: 2b3f99b415e32bcde26bf522b879305fe3edffd9318cf15b85f6d1b9699a06a5
  prop:notions-coincide: 75847c27e7b0052fc43c8abf198988644a0b57da282b0226d71e368cbd3caf2d
---

Certify review of the repaired `solutions/prop-critical-sphere.md` against
`prop:critical-sphere` (`sec:singular`), with `def:sliced-wasserstein`,
`def:barycentric-field`, `def:critical-point` and the current manuscript statement of
`prop:notions-coincide` (proved; certified by
`research/reviews/2026-10-20-prop-notions-coincide-rereview.md`), and against the source
DiazMartinMurphy2026 (arXiv:2610.08734v1). Fresh context: I did not write or direct the
dossier and have not seen the conversation that produced it.

**Verdict: pass.**

## Findings

*Re-review of `research/reviews/2026-10-20-prop-critical-sphere.md`* (verdict `revise`,
dossier fingerprint `dec47299…`). That report found every computation correct and asked
for two repairs: (1) cite the manuscript statement of `prop:notions-coincide` instead of
`thm:sol-nc-main` (b) and item 5 of `lem:sol-nc-version` of another dossier, and prove
version independence inline; (2) remove the false remark `rem:sol-cs-refined`.

**Versions compared.** The pre-repair dossier is not in git, so no baseline matching
`dec47299…` can be verified. I therefore reviewed the current dossier
(`bd47ad6d…`) **in full**, using the earlier report only as a guide. The statement
fingerprints of `prop:critical-sphere`, `def:critical-point` and `prop:notions-coincide`
are identical to those the earlier report recorded; I read the current texts of these and
of `def:sliced-wasserstein` and `def:barycentric-field`.

**Repairs.**
- No reference to `solutions/prop-notions-coincide.md` or to any `sol-nc` label remains
  (searched); `rem:sol-cs-refined` and the word "certified" are gone.
- Overview step 4, *Dependencies* and the proof of item 3 now cite
  `prop:notions-coincide` item 2 ("If µ has no atom, the three notions … coincide") for
  $r = r_*$ and item 1 for $r \ne r_*$. Both items, as stated in the manuscript, supply
  exactly what is used: $\mu_{r_*}, \rho \in \Ptwo{d}$ (compact support; Gaussian),
  $\mu_{r_*}$ atomless (`lem:sol-cs-projection`), critical by item 3's first paragraph,
  hence Lagrangian and Wasserstein critical; for $r \ne r_*$, not critical, hence by
  item 1 (contrapositive) neither of the other two. The dossier does not state
  $\mu_r \in \Ptwo{d}$ explicitly; it is immediate (support in $r\Sph{d-1}$) and is not a
  gap.
- *Independence of the version* in `lem:sol-cs-field` (l. 229–254): checked. For jointly
  Borel $g, \tilde g$ agreeing $(\mu_r)_\theta$-a.e. for σ-a.e. θ, the map
  $(x,\theta) \mapsto \abs{g - \tilde g}(\theta,\inner{x}{\theta})$ is Borel and nonnegative;
  Tonelli and $(\mu_r)_\theta = (P_\theta)_\#\mu_r$ give a zero double integral, so for
  $\mu_r$-a.e. $x$ the integrands agree σ-a.e. and the two field integrals coincide (the
  $g$-integral being absolutely convergent at every point of the sphere). This reads
  `def:barycentric-field` as computed with a jointly measurable version of
  $(\theta,s) \mapsto \bar\gamma_\theta(s)$, which the σ-integral requires; with that
  reading the step is complete. On the sphere, $\abs{\inner{re}{\theta}} = r$ only for
  $\theta = \pm e$, σ-null, so $g(\theta,\inner{re}{\theta}) = \tau(\inner{e}{\theta})$
  σ-a.e. Correct.
- *Quantile argument* in `rem:sol-cs-formula`: checked. For $u \in (0,1)$ the Galois
  relation $Q(u) \le t \iff u \le H(t)$ holds by right continuity; it gives
  $Q(H(Z)) \le Z$ and $\Prob(Q(U) \le t) = H(t)$ with $U = H(Z)$ uniform; $Q(U) \in [-1,1]$,
  so $Z - Q(U) \ge 0$ is bounded with mean $0$ and vanishes a.s. Then
  $r_* = d\int_0^1 Q\,\Phi^{-1}$, a covariance since both means vanish. For $d = 2$,
  $H(t) = 1 - \arccos(t)/\pi$, $Q(u) = -\cos(\pi u)$ and
  $r_* = -2\E[G\cos(\pi\Phi(G))]$. Correct; the remark is not used by the proof.

**Statement agreement.** `prop:critical-sphere`: for $d \ge 2$, $\rho = N(0,I_d)$, some
$r_* > 0$ makes $\mathrm{Unif}(r_*\Sph{d-1})$ a Wasserstein critical point
(`def:critical-point`, item 3). `thm:sol-cs-main` items 1 and 3 give it, with uniqueness of
the radius, all three notions, $\mu_{r_*} \ne \rho$ and $r_* = 3/\sqrt\pi$ for $d = 3$.
Quantifiers and normalization (σ a probability, factor $d$ in $v_\mu$) match. Stronger;
allowed.

**`lem:sol-cs-projection` (law of Z).** Checked: $O(d)$-invariance gives one law; level
sets of $\inner{e}{\cdot}$ on $\Sph{d-1}$ are empty, a point, or a $(d-2)$-sphere (two
points if $d = 2$), $\mathcal H^{d-1}$-null, so no atom and $\abs Z < 1$ a.s.; symmetry via
$-I_d$, and $H(0) = \tfrac12$ using no atom; $\E Z^2 = 1/d$ by coordinate permutations;
$0 < H < 1$ on $(-1,1)$ from nonempty relatively open caps; projections of $\mu_r$ are
the law of $rZ$ with distribution function $H(\cdot/r)$; $\mu_r$ has no atom. Correct.

**`lem:sol-cs-constant` ($0 < A_d < d^{-1/2}$).** Checked: τ nondecreasing, Borel,
$\tau(0) = 0$; $H$ continuous so $H(Z) \sim U(0,1)$, valued in $(0,1)$ a.s., and
$\tau(Z) \sim N(0,1)$; $t\tau(t) \ge 0$ with $\{Z = 0\}$, $\{\tau(Z) = 0\}$ null, so
$Z\tau(Z) > 0$ a.s. and $A_d > 0$; Cauchy–Schwarz gives $A_d \le d^{-1/2}$, equality would
force $\tau(Z) = \lambda Z$, $\lambda \ge 0$, bounded by λ, impossible for a Gaussian.
Hence $0 < r_* < \sqrt d$. Correct.

**`lem:sol-cs-field`, remaining steps.** Monotone map: $\rho_\theta = N(0,1)$,
$Q_{\rho_\theta} = \Phi^{-1}$, $F_{(\mu_r)_\theta} = H(\cdot/r) \in (0,1)$ on $(-r,r)$, of full
measure, so $\bar\gamma_\theta = T_\theta = \tau(\cdot/r)$ a.e. by `def:barycentric-field`.
Integrability: $\int\tau(\inner{e}{\theta})^2\dd\sigma = 1$. Reflection: $S = I - 2uu^\top$,
$u \perp e$, symmetric orthogonal, $Se = e$, $Su = -u$, $S_\#\sigma = \sigma$; the integrand
$\tau(\inner{e}{\theta})\inner{u}{\theta}$ is odd under $S$, so $\inner{u}{I(e)} = 0$.
Radial part $\E[Z\tau(Z)] = A_d$. So $v_{\mu_r}(re) = (r - dA_d)e$ on the whole sphere.
Correct.

**Proof of `thm:sol-cs-main`.** Item 2 from the lemma; item 3: $(1 - r_*/r)x = 0$ with
$\abs x = r > 0$ iff $r = r_*$; passage to the other notions as under *Repairs*;
$\mu_{r_*} \ne \rho$ since the sphere is Lebesgue-null. Item 4 is `lem:sol-cs-d3`. Correct.

**`lem:sol-cs-d3` ($r_* = 3/\sqrt\pi$).** Checked: $\theta_3 = \cos\phi \in (a,b]$ iff
$\phi \in [\arccos b, \arccos a)$, $\frac{2\pi}{4\pi}(b - a) = (b-a)/2$, so $H(t) = (1+t)/2$
and $Z = 2\Phi(G) - 1$ a.s.; $A_3 = 2\E[G\Phi(G)]$; with $z\varphi = -\varphi'$ the boundary
term vanishes and $\int\varphi^2 = \frac{\sqrt\pi}{2\pi} = \frac{1}{2\sqrt\pi}$; $A_3 =
1/\sqrt\pi$, $r_* = 3/\sqrt\pi \approx 1.693 < \sqrt3$. It agrees with the independent hand
computation of `sec:overview` ($\int_0^\infty \varphi^2 = \tfrac{1}{4\sqrt\pi}$ there gives
the same $1/\sqrt\pi$). Correct.

**Hypotheses.** Used: $d \ge 2$ (atomless ζ_d), $\rho = N(0,I_d)$ (one monotone map for
all θ; Gaussian quantile). None unstated; none stated and unused.

**Dependencies and fences.** `depends_on` = [def:critical-point, prop:notions-coincide],
both `defined`/`proved` (the latter certified by the pass report named above, whose
fingerprint of `prop:notions-coincide` matches the current one). No `bounded_by` on the
node. Sphere test of the brief: the result is that test's object; it is consistent with
`conj:sw-critical` ($\mu_{r_*}$ singular) and with `prop:notions-coincide`.

**Imported results: agreement with the source.** I read arXiv:2610.08734v1
(`../ensae-conjecture-scouting/verification/citing-papers/2610.08734.txt`): Standing
Assumptions and Proposition 1 (≈ l. 297–335), Example 1 and its sketch (l. 530–539), and
the appendix "Details for Example 1" (l. 2788–2949). The source takes
$F = \tfrac12\SW_2^2(\cdot, N(0,I_d))$, σ the uniform probability, gradient
$\int(x\cdot\theta - T_r(x\cdot\theta))\theta\dd\sigma = v_\mu(x)/d$ (by
$\int\inner{x}{\theta}\theta\dd\sigma = x/d$), monotone map $\Phi^{-1}(H(s/r))$ in every
direction, $O(d)$-equivariance making the field at $re_1$ parallel to $e_1$, radial
component $r/d - A_d$ with $A_d = \int\Phi^{-1}(H(\theta_1))\theta_1\dd\sigma$, root
$r_* = dA_d$ — the same constant and radius as the dossier. The source asserts without
proof that $A_d$ is finite and positive (the dossier proves it), gives no value of $r_*$,
and its "Wasserstein critical point" is the vanishing of the gradient of its
Proposition 1 (derivative along $(\Id + tv)_\#\mu$, $v \in C^1_c$, atomless projections),
not the geodesic notion of `def:critical-point` item 3. `rem:sol-cs-source` states all of
this accurately, including the normalization ("$\tfrac2d\inner{v_\mu}{\xi}$, halved").
The dossier's proof does not use the source; certification does not rest on the
preprint, which is a 6 October 2026 preprint and not *established*.

**Build.** `uv run scripts/check.py` reports no MyST error and no error for the dossier
(only "draft … no proof record names it").

## Corrections

None.

## Exclusions

- The proof of `prop:notions-coincide` is not re-checked here; this proof uses its
  manuscript statement, fingerprinted above, certified separately.
- Proposition 1 of DiazMartinMurphy2026 and its proof are not checked; unused.
- `rem:sol-cs-density` (density of ζ_d, Gaussian limit) is not certified; the proof does
  not use it. `rem:sol-cs-formula` is checked as stated, but the absence of closed forms
  for $d \ne 3$ is not addressed and not certified.
- Stability of the critical sphere, and whether it is a local minimizer, are not addressed
  and not certified.
