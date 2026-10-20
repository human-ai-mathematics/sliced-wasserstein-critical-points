---
verdict: pass
authors:
  - researcher, claude-opus-5-5, 2026-10-20
reviewer: reviewer, claude-opus-5-5, 2026-10-20
fingerprints:
  solutions/thm-gaussian-target.md: 2d5de6b7b93a8154e876f869536672fa04c810a04ac40bbe977b1081a9638ad6
  thm:gaussian-target: 0d64aad49fc40805f5410fcbdfc0d011991305cf0fb627016390a08f47336dd6
  def:critical-point: 2b3f99b415e32bcde26bf522b879305fe3edffd9318cf15b85f6d1b9699a06a5
---

Certify review of `solutions/thm-gaussian-target.md` against `thm:gaussian-target`
(`modules/04-special-targets.md`), with `def:sliced-wasserstein`, `def:barycentric-field`,
`def:critical-point` (`modules/01-setting.md`) and the audit tests of
`research/program/brief.md`. Fresh context; I did not write or direct the dossier.

## Findings

**Statement agreement.** `thm:sol-gaussian-target` is the manuscript statement verbatim:
$d \ge 1$, $m \in \R^d$ arbitrary, $\Sigma$ symmetric positive definite, $\mu \in \Ptwo{d}$
absolutely continuous and critical in the sense of `def:critical-point` (1), conclusion
$\mu = \rho$. Same quantifiers, same hypotheses, no added assumption. The case $d = 1$
($\sigma$ uniform on $\{\pm1\}$, $\int\theta\theta^\top\dd\sigma = 1 = I/d$) goes through
every step; the dossier's conventions for it ($B_K = 2C_K$, $\eta = 0$) are right.

**Hypotheses used.** $\mu \ll \Leb$ (hyperplanes null, $\mu(\partial C) = 0$, the
Lebesgue-to-$\mu$ transfer); $\mu \in \Ptwo{d}$ (integrability in `lem:gt-identities`,
`lem:gt-one-dim`); $\Sigma \succ 0$ ($s_\theta^2 \ge \lambda_{\min} > 0$, $C^1$ quantile);
the Gaussian form of $\rho$ (smooth positive density of $\rho_\theta$, quadratic
$\log g_\theta$, variance $\theta^\top\Sigma\theta$). None unstated, none unused.

**Dependencies.** Only `def:critical-point` and, through it, `def:barycentric-field` and
`def:sliced-wasserstein` (all `defined`). The fact used from `def:barycentric-field` —
$\bar\gamma_\theta = T_\theta$ $\mu_\theta$-a.e. when $\mu_\theta$ has no atom — is stated in
that definition. `prop:critical-sphere` (open) and `prop:critical-segments` appear only in
remarks outside the proof. No open dependency.

**Fences.** `thm:gaussian-target` has no `bounded_by`. The target's fences exhibit
singular critical points; the theorem assumes $\mu \ll \Leb$, so there is no conflict.

**Steps, checked line by line.**

- `lem:gt-domain`. (1) Preimages of null sets under $P_\theta$ are null (Fubini); joint
  continuity of $F$ by dominated convergence off the $\mu$-null hyperplane. Correct.
  (2) $S$ spans $\R^d$ affinely since hyperplanes are $\mu$-null; the cone argument is
  correct (I rechecked $x = \frac1{1+t}z + \frac t{1+t}y$ and
  $\frac1{1+t}z + \frac t{1+t}B(y,r) = B(x, \frac{tr}{1+t})$, the half-aperture
  $\arcsin(r/\abs{x-x_0})$ bounded below on $B(0,R)$), and Lebesgue's density theorem gives
  $\Leb(\partial C) = 0$, hence $\mu(U) = 1$. (3) Correct; it only uses supp $\mu$.
- `lem:gt-monotone`. Push-forward $(F_\theta)_\#\mu_\theta = \mathrm{Unif}(0,1)$ via
  $y_u$ is correct; the chain rule $T_\theta' = s_\theta f_\theta/\varphi(\Phi^{-1}(F_\theta)) =
  f_\theta/g_\theta(T_\theta)$ checked. $T_\theta$ is locally absolutely continuous because
  $F_\theta$ is absolutely continuous and $\Phi^{-1}$ is locally Lipschitz: this is the point
  that leaves $DV$ with no singular part. The Borel version $D$ via $\limsup$ of difference
  quotients on the open set $O$ is correct.
- `lem:gt-local-bounds`. $m_K > 0$ by continuity and compactness; $\abs{T_\theta} \le C_K$;
  $\int_{J^K_\theta} T_\theta' \le 2C_K$ by the fundamental theorem for absolutely continuous
  functions; the slice bound $\mathcal H^{d-1}(\pi_\theta K) \le \omega_{d-1}(\operatorname{diam}K)^{d-1}$.
  Uniform in $\theta$, as needed.
- `lem:gt-representative`. Continuity by dominated convergence. Agreement $v_\mu = V$
  $\mu$-a.e. by Tonelli on the set $E$, whose $\theta$-sections lie in
  $P_\theta^{-1}(N_\theta)$, $\mu$-null. **Reading of `def:barycentric-field`:** the definition
  defines $\bar\gamma_\theta$ only $\mu_\theta$-a.e. for each $\theta$, so the integral in
  $\theta$ at a fixed $x$ has meaning only through a jointly measurable version of
  $(x,\theta) \mapsto \bar\gamma_\theta(\inner x\theta)$; the dossier's reading
  (`rem:gt-definition-reading`) is the only coherent one, and the same Tonelli argument shows
  that all such versions give the same $v_\mu$ $\mu$-a.e. Accepted.
- `lem:gt-sobolev`. The integration by parts (`eq-gt-ibp`) is correct: the $\eta$-part
  vanishes as the integral over $\theta^\perp$ of a tangential derivative of a $C^1_c$
  function; the $\theta$-part is integration by parts of absolutely continuous functions on
  $J^{K'}_\theta$, with $h^\pm_{K'} = h^\pm_K \pm \delta/2$ so that $\psi_z$ vanishes at the
  endpoints. Both Fubini exchanges (in $z$, then in $\theta$) are justified by the bounds
  $C_K\norm{\nabla\phi}_\infty \one_K$ and $\norm\phi_\infty B_K$ on $K \times \Sph{d-1}$. Hence
  $V \in W^{1,1}_{\mathrm{loc}}(U)$ with $DV = I - A$, $a \in L^1_{\mathrm{loc}}(U)$.
- `lem:gt-stampacchia`. **Criticality is used only $\mu$-a.e.**: $Z = U \cap S \cap \{V = 0\}$,
  $\mu(Z) = 1$; nothing is asserted on $C \setminus S$. The Sobolev step gives $DV = 0$
  Lebesgue-a.e. on $Z$, a subset of $S$; the null set $N$ is Borel and Lebesgue-null, so
  $\mu(N) = 0$ by absolute continuity. The transfer is correct; it is meaningful because
  $\mu(Z) = 1$ and $\mu \ll \Leb$ force $\Leb(Z) > 0$.
- `lem:gt-identities`. (`eq-gt-II`) $\operatorname{tr}(\Sigma\theta\theta^\top) = s_\theta^2$,
  Tonelli for the nonnegative integrand, and $\operatorname{tr}\Sigma = d\int s_\theta^2\dd\sigma$.
  The $\mu_\theta$-integral of $T_\theta'$ does not depend on the version since
  $\mu_\theta \ll \Leb$ and $\mu_\theta(I_\theta) = 1$. (`eq-gt-I`) Pairing with $x - m$;
  $\inner{x-m}{x} = d\int(\inner x\theta - m_\theta)\inner x\theta\dd\sigma$; the
  Cauchy–Schwarz integrability bound and the uniform bound of the inner integral are correct.
- `lem:gt-one-dim`. **Finite entropy is deduced, not assumed:** from
  $\int T'\dd\nu < \infty$, $(\log T')^+ \le T'$ and $\log g(T) \in L^1(\nu)$ give
  $(\log f)^+ \in L^1(\nu)$; the negative part is controlled by splitting at $f = e^{-y^2}$,
  with $-t\log t \le \frac2e\sqrt t$ on $(0,1]$ (maximum of $se^{-s/2}$ is $2/e$) and
  $M_2(\nu) < \infty$. The inequality: $1 - t \le -\log t$, the expansion of
  $(T - m_\theta)^2$ with $\int (T-m_\theta)^2\dd\nu = s^2$, and the bracket equal to
  $\mathrm{KL}(\nu\mid\rho_\theta) \ge 0$ (Jensen). Every term is integrable. Checked.
- *Proof of the theorem.* $L$ is $\sigma$-integrable, $\int L\dd\sigma = 0$, $L_\theta \le
  -\frac12E_\theta$ on $G$ with $\sigma(G) = 1$, hence $E_\theta = 0$ a.e., $\mu_\theta =
  \rho_\theta$ on a dense set of directions, and $\hat\mu = \hat\rho$ by continuity of
  characteristic functions. Correct.

**Audit tests of the brief.**

- *Sphere* ($\mu$ uniform on $r_*\Sph{d-1}$, $\rho = N(0,I_d)$). $C = \bar B(0,r_*)$,
  $\mu(U) = 0$, $Z = \emptyset$: the proof breaks at `lem:gt-domain` (2) and
  `lem:gt-stampacchia`, exactly where absolute continuity of $\mu$ (not of $\mu_\theta$) is
  used. For $d = 3$, $\int T_\theta'\dd\mu_\theta = +\infty$ for every $\theta$, so
  `eq-gt-II` indeed fails. Passed.
- *Segments* (`prop:critical-segments` (2)). Atoms of $\mu_\theta$ for $\theta \perp e_1$,
  and $U = \emptyset$. Passed.
- *Atoms, unbounded supports, fat Cantor supports, irregular densities.* No atom is
  possible; $I_\theta$ and $U$ may be unbounded and all bounds are local on compacts of $U$;
  Stampacchia's lemma applies on an arbitrary measurable set, so dense holes of positive
  measure are harmless (nothing is done hole by hole); no integration by parts against $\mu$
  — only against Lebesgue measure on slices, with the absolutely continuous $T_\theta$.

**Citations.**

- Santambrogio, *Optimal Transport for Applied Mathematicians* (Birkhäuser 2015), checked
  in the book: Theorem 2.5 is the existence and uniqueness of the nondecreasing map
  $T_{\mathrm{mon}} = F_\nu^{[-1]} \circ F_\mu$ for atomless $\mu$; the optimality statement
  the dossier means — for $h$ strictly convex and finite (KP), $\gamma_{\mathrm{mon}}$ is the
  unique optimal plan, induced by $T_{\mathrm{mon}}$ when $\mu$ is atomless — is
  **Theorem 2.9**. The number is wrong (see Corrections); the fact itself holds, with
  $h(z) = z^2$ and (KP) finite on $\Ptwo{1}$.
- Vauthier–Korba–Mérigot, arXiv:2502.06525v2, Theorem B.6, checked in the preprint: the
  monotone plan $(F_\mu^{-1}, F_\nu^{-1})_\#\Leb|_{[0,1]}$ is the unique optimal plan for
  strictly convex $h(x-y)$. For atomless $\mu_\theta$ this plan is $(\Id, T_\theta)_\#\mu_\theta$,
  so $\bar\gamma_\theta = T_\theta$. Correct. In any case the fact is part of
  `def:barycentric-field`.
- Evans–Gariepy, *Measure Theory and Fine Properties of Functions*, revised ed. (2015),
  Theorem 4.4(iv), checked in the book: "$Df = 0$ $\Leb^n$-a.e. on $\{f = 0\}$" for
  $f \in W^{1,p}(U)$, $1 \le p < \infty$. It applies to $V_j \in W^{1,1}_{\mathrm{loc}}(U)$
  after restriction to each open $U' \Subset U$ (where $V_j$ is bounded and $DV_j \in L^1$)
  and a countable exhaustion of $U$. This suffices for `lem:gt-stampacchia`.
- Gilbarg–Trudinger, 2nd ed., Lemma 7.7: the local copy is a DjVu file I could not extract,
  and web sources did not show the text. **Not verified by me.** The step does not depend
  on it, since Evans–Gariepy Theorem 4.4(iv) was verified and covers it.
- Fubini–Tonelli, Lebesgue density and differentiation, absolutely continuous calculus,
  Jensen, Lévy uniqueness: standard, used within their hypotheses.

**Build.** `uv run scripts/check.py` exits 0 with no MyST error for the dossier.

**Verdict.** Every step of the proof was checked and holds. The dossier proves
`thm:gaussian-target` exactly as quantified in the manuscript. Pass.

## Corrections

Editorial only; none affects a step. Each lapses this certification when applied, and an
editorial note (*Review* in `SPECIFICATION.md`) can carry it over.

1. `solutions/thm-gaussian-target.md`, line 48: "Theorem 2.5" should read "Theorem 2.9
   (with $T_{\mathrm{mon}}$ as in Theorem 2.5)". Theorem 2.5 of Santambrogio (2015) does not
   state optimality.
2. `solutions/thm-gaussian-target.md`, lines 56–57: Evans–Gariepy Theorem 4.4(iv) is stated
   for $W^{1,p}(U)$, not for weakly differentiable functions in general. It is "the same
   result" only after localization to $U' \Subset U$. A clause saying so would make the
   citation exact.

## Exclusions

- `rem:gt-where-ac`, `rem:gt-sphere-audit`, `rem:gt-segments-audit`, `rem:gt-gaussian-role`,
  `rem:gt-no-entropy` and `rem:gt-definition-reading` are commentary. I checked them for
  consistency only. In particular, nothing here certifies `prop:critical-sphere` or the
  claim that the critical sphere fails `eq-gt-II` in dimensions other than 3.
- The heuristic in `rem:gt-gaussian-role` that score gluing forces a Gaussian
  (`cand:score-gluing-gaussian`) is neither proved nor certified.
- Not certified: `prop:notions-coincide`, the manuscript's "Idea of the proof" and
  "Limits" prose for `thm:gaussian-target`, and any extension to non-Gaussian targets or to
  singular $\mu$.
- The claim of `rem:gt-no-entropy` that this result supersedes `thm:cs-isotropic` is
  mathematically correct: take $m = 0$, $\Sigma = I_d$. Recording it in the ledger is the
  orchestrator's call.
- Gilbarg–Trudinger Lemma 7.7 is not verified (see Findings).
