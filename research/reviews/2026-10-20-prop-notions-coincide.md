---
verdict: pass
authors:
  - researcher, claude-opus-5-5, 2026-10-20
reviewer: reviewer, claude-opus-5-5, 2026-10-20
fingerprints:
  solutions/prop-notions-coincide.md: 36e0c1ff8b6c6a3f42d53b704eb38f8de8c3ea1577b9e3f4c5ab8f6a145f4cb2
  prop:notions-coincide: 0e3513d91d6f4b0208aa2bc1b2735d85c20cdabafb1647a118aea91a35400517
  def:critical-point: 2b3f99b415e32bcde26bf522b879305fe3edffd9318cf15b85f6d1b9699a06a5
---

Certify review of `solutions/prop-notions-coincide.md` against `prop:notions-coincide`,
with `def:sliced-wasserstein`, `def:barycentric-field` and `def:critical-point` (all in
`sec:setting`) and the audit tests of `research/program/brief.md`. Fresh context: I did
not write or direct the dossier and have not seen the conversation that produced it.

## Findings

**Statement agreement.** The manuscript claim, for $\mu,\rho \in \Ptwo{d}$ and $d \ge 1$:
(1) Lagrangian or Wasserstein critical ⇒ critical; (2) for absolutely continuous $\mu$ the
three notions coincide. The dossier theorem `thm:sol-nc-main` proves (a) item 1 for every
$\mu,\rho \in \Ptwo{d}$, every $d \ge 1$, with no hypothesis on $\rho$ or the supports, and
(b) for atomless $\mu$ the right derivative along every displacement interpolation of a
plan with first marginal $\mu$, which gives critical ⇒ Lagrangian and critical ⇒
Wasserstein. Absolute continuity implies no atom, so (a)+(b) give item 2 exactly as
quantified. The sharper form (atomless $\mu$) is proved. The definitions require a right
derivative to *exist and vanish*; (a) uses only that it exists and vanishes along one
curve, (b) proves existence. Agreement holds.

**Definition of $v_\mu$.** `def:barycentric-field` does not say how the versions
$\bar\gamma_\theta$ are chosen jointly in $\theta$. `lem:sol-nc-version` builds one Borel
$g(\theta,s)$ from the quantile functions (item 1: Borel measurability of $F$, $Q$ via
(F1) and Tonelli, checked), shows it is a version of $\bar\gamma_\theta$ for *every*
$\theta$ (item 3: the three-part split of $(0,1)$ — atom intervals, the countable set
$\{F(s^-)\}$, and the continuity points where $F(Q(u)) = u$ — checked), nondecreasing
on a set $A_\theta$ of full $\mu_\theta$-measure (item 2, checked including the boundary
cases $F = 0$, $F(c^-) = 1$), and that any other jointly Borel σ-a.e. version gives the
same field $\mu$-a.e. (item 5, Tonelli on $\{g \ne \tilde g\}$, checked). This is the
correct reading of the definition. $v_\mu \in L^2(\mu)$ with $\int\abs{w}^2\dd\mu \le
M_2(\rho)$ (item 4: Jensen on atom intervals, Cauchy–Schwarz with (F4)) — checked.

**Upper bound** (`lem:sol-nc-upper`). The lifted plan $\Lambda_\theta = \mu \otimes
k_\theta(\inner{x}{\theta},\cdot)$ has the right marginals; the expansion, the integrability
of the three terms, the identification $c_\theta = \int\inner{\xi}{\theta}(\inner{x}{\theta}
- g)\dd\mu$, the joint $L^1(\mu\otimes\sigma)$ bound and the Fubini/(F4) computation
$\int c_\theta\dd\sigma = \tfrac1d\inner{v_\mu}{\xi}$ are correct; valid for all $t \in \R$
and all $\mu$. Agrees with VKM Prop. 4.7(b) after renormalization (see below).

**Geodesic** (`lem:sol-nc-geodesic`). The full-measure Borel set $S$, the rearrangement
argument for $\sum h(u_i)(u_{i+1}-u_i) \le 0$ (ties handled since $h$ is a function),
the identity $\sum\inner{w(x_i)}{x_{i+1}-x_i} = d\int\sum g(\theta,u_i)(u_{i+1}-u_i)\dd\sigma$
and the passage to $c$-cyclical monotonicity are correct. The dossier proves
$\sum c(x_{i+1},y_i) \ge \sum c(x_i,y_i)$ for every finite family in $\Gamma$; Villani's
definition (Def. 5.1) uses $\sum c(x_i,y_{i+1})$, which follows by reversing the order of
the family — harmless, not stated. Optimality by Villani Thm 5.10(ii) (b)⇒(a): $c$ is
continuous, real-valued, $\ge 0$ (so $a = b = 0$), optimal cost finite; $\pi$ is
concentrated on the Borel c-CM set $\Gamma$. The constant-speed property from the
triangle inequality is correct (and trivially when $v_\mu = 0$). Part (a) then follows:
quotient $\le -\tfrac2d\norm{v_\mu}^2 + \tfrac td\norm{v_\mu}^2$.

**Bathtub and 1D first variation** (`lem:sol-nc-bathtub`, `lem:sol-nc-1d`). The bathtub
inequality $(Y-q)(Z - \one\{Y<q\}) \ge 0$, the choice of $\lambda$, and $\int_0^a Q =
qa + \E[(Y-q)\one\{Y<q\}]$ are correct. In 1D: the decomposition of the difference
quotient, $\norm{D_t} \le \norm{H}$, reduction of weak convergence to $\int_0^a$ (bounded
family + density of step functions), $\Prob(U<q) = a$ and $\Prob(U=q) = 0$ from
atomlessness, the two-sided squeeze, the identity $\E[UZ_t] - f(0) = \E[\abs{U-q}
\abs{Z_t - Z_0}] \le 2t\E\abs{H}$, the $\delta,K$ truncation, $\{S<a\} = \{U<q\}$ by (F1),
and the conclusion via $Q_0(S) = U$ a.s. (F3) and the conditional-expectation step — all
checked. (F3)'s arctan argument is correct.

**Integration over θ** (`lem:sol-nc-plan`). Hypotheses of the 1D lemma hold on
$(\R^d\times\R^d,\gamma)$ ($U, H \in L^2(\gamma)$ from $\mu \in \Ptwo{d}$ and $\int\abs{y}^2
\dd\gamma < \infty$). Uniform domination $\abs{W_\theta(t)^2 - W_\theta(0)^2}/t \le
L(2K+L)$ for $t \in (0,1]$ is correct, measurability in θ comes from item 1 applied to
$\mu_t \in \Ptwo{d}$, and dominated convergence along sequences gives the limit. The
$L^1(\gamma\otimes\sigma)$ bound and Fubini computation are correct. Main proof (b):
$\gamma = (\Id,\Id+\xi)_\#\mu$ for the Lagrangian notion; for geodesics, the single
optimal plan representing the whole geodesic (AGS Thm 7.2.2) — checked as below.

**Atoms lemma** (`lem:sol-nc-atoms`). The minimal-charged-affine-subspace argument is
correct: distinct minimal subspaces meet in uncharged sets, so finitely many have total
mass $\le 1$, hence countably many; an atom of $\mu_\theta$ forces θ into $\vec E^\perp$ for
some minimal $E$ of dimension $\ge 1$, a σ-null set. $d = 1$ handled. Converse trivial.

**Remarks.** The $\delta_0$ example is correct: with $\rho$ centred and $\rho \ne \delta_0$,
$g(\theta,0) = \int_0^1 Q_{\rho_\theta} = 0$, so $\delta_0$ is critical;
$\SW_2^2(\delta_{tc},\rho) = (M_2(\rho)+t^2\abs{c}^2)/d$, so it is Lagrangian critical;
along the geodesic $(t\Id)_\#\rho$, $\SW_2^2 = (1-t)^2M_2(\rho)/d$ with right derivative
$-2M_2(\rho)/d < 0$, so it is not Wasserstein critical. This shows the atomless hypothesis
cannot be dropped in (b) for the Wasserstein notion, and is consistent with (a). The
remark on the sphere and segments is accurate (both atomless; it uses only their
statements and certifies nothing about them).

**Normalization against VKM** (arXiv:2502.06525v2, source fetched outside the repository).
Eq. (16) is $v^{\mathrm{VKM}}_\mu = \tfrac1d x - \int\bar\gamma_\theta(\inner{x}{\theta})\theta
\dd\theta = v_\mu/d$; Prop. 4.7(b) reads $\SW_2^2((\Id+\xi)_\#\mu,\rho) \le \SW_2^2 +
2\inner{v^{\mathrm{VKM}}_\mu}{\xi} + \tfrac1d\norm{\xi}^2$, i.e. `lem:sol-nc-upper` at $t=1$;
Prop. 4.7(c) $\varphi'(0) = 2\inner{v^{\mathrm{VKM}}_\mu}{\xi} = \tfrac2d\inner{v_\mu}{\xi}$.
So the dossier's remark is accurate as a renormalization; note that VKM's 4.7(b)–(c) are
consistent with their own eq. (16) as printed. Cor. 4.8 assumes compact supports and
atomless µ, ρ; Prop. 4.4 treats $\mu_X$ with distinct points and ρ a density;
Prop. 4.7(a) gives existence of the derivatives by convexity — all as the dossier says.

**Citations.**
- Santambrogio 2015, Thm 2.9 (unique optimal plan $\gamma_{\mathrm{mon}}$ for strictly
  convex $h(y-x)$ with finite cost) and Prop. 2.17 ($T_c = \int_0^1 h(F_\nu^{[-1]} -
  F_\mu^{[-1]})$): checked against the author's version of the book (OTAM-cvgmt.pdf);
  statements and numbers match. $\gamma_{\mathrm{mon}}$ is Definition 2.3, in §2.1, not
  §2.2 as the dossier says (Correction 1).
- Villani 2009, Thm 5.10(ii) (a)⇔(b), and Def. 5.1: content checked against the 2006
  Saint-Flour draft, where the theorem is numbered 5.9 with identical hypotheses and
  part (ii); the published number 5.10 is the standard citation. Statement used follows.
- AGS 2008, Thm 5.3.1 (disintegration): the printed book was unavailable to me; the number
  and statement are confirmed by VKM's Theorem A.2, which quotes it; any disintegration
  of a probability on $\R\times\R$ suffices here.
- AGS 2008, Thm 7.2.2 (every constant-speed geodesic of $\Ptwo{d}$ is $((1-t)\pi^1+t\pi^2)_\#
  \gamma$ for one optimal $\gamma$): the printed book was unavailable; the statement used is
  verified independently from Villani's Corollary "displacement interpolation as
  geodesics" (draft Cor. 7.20; complete separable locally compact length space, $p > 1$),
  which in $\R^d$, where minimizing constant-speed geodesics are segments, gives exactly
  this representation with $(e_0,e_1)_\#\Pi$ optimal. The step therefore stands; only the
  AGS theorem number itself is unconfirmed from the primary source.

**Hypotheses.** Used: $\mu,\rho \in \Ptwo{d}$; for (b), $\mu$ atomless. None used and
unstated. Stated but unused relative to the manuscript: absolute continuity of $\mu$
(weakened to atomless, as the dossier proves).

**Dependencies and fences.** Only the three definitions; `depends_on: [def:critical-point]`
is accurate (the other two definitions are reached through it). No `bounded_by` on this
node. `prop:critical-sphere` (open) and `prop:critical-segments` appear only in a remark,
never as a step.

**Audit tests of the brief.** Sphere and segment tests: the proof never uses absolute
continuity, and its conclusion is consistent with both examples (they are atomless, so all
three notions coincide for them; nothing contradicts their criticality). Atoms: $\delta_0$
treated correctly. Unbounded supports: only second moments are used. Directions where
$\mu_\theta$ has atoms: handled by $g$ via $\bar\gamma_\theta$, not $T_\theta$. Fat Cantor
supports and irregular densities: no regularity of µ used.

**Build.** `uv run scripts/check.py` reports no FAIL; the dossier builds.

## Corrections

Non-blocking, editorial; a fix would go through an editorial note.

1. `solutions/prop-notions-coincide.md:57-58`: "the definition of $\gamma_{\mathrm{mon}}$ in
   §2.2" should read "Definition 2.3 (§2.1)".
2. `solutions/prop-notions-coincide.md:377-380`: optionally add that Villani's form
   $\sum c(x_i,y_i) \le \sum c(x_i,y_{i+1})$ follows by applying the inequality to the family
   in reverse order.

## Exclusions

Not certified here: `prop:critical-sphere` and `prop:critical-segments`, discussed in
`rem:sol-nc-singular`; whether a critical point with atoms is Lagrangian critical in
general (`rem:sol-nc-open`); existence of the right derivatives for measures with atoms;
the manuscript prose of `sec:setting` (including its claim about VKM Appendix B.9), which
is the `sync` lens's.
