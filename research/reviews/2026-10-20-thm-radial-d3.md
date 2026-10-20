---
verdict: pass
authors:
  - researcher, claude-opus-5-5, 2026-10-20
reviewer: reviewer, claude-opus-5-5, 2026-10-20
fingerprints:
  solutions/thm-radial-d3.md: 7b79870e0b7281530e37751f468a87058a59da3f91f3fa02d5f96fa5d0b0f531
  thm:radial-d3: 61d070fb07106b54aa860ad86b8ffa4c03159f59249e5dfd5f25c2d458de4750
  def:critical-point: 2b3f99b415e32bcde26bf522b879305fe3edffd9318cf15b85f6d1b9699a06a5
---

Certify review of `solutions/thm-radial-d3.md` against `thm:radial-d3`
(`modules/04-special-targets.md`), with `def:sliced-wasserstein`, `def:barycentric-field`,
`def:critical-point` (`modules/01-setting.md`) and the audit tests of
`research/program/brief.md`. I worked in a fresh context. I did not write or direct the dossier.

## Findings

**Statement agreement.** The manuscript statement: $\rho, \mu \in \Ptwo{3}$ are
rotation-invariant, the law of $\abs{X}$ ($X \sim \mu$) has no atom, and $\mu$ is critical in the
sense of `def:critical-point` (1). The conclusion is $\mu = \rho$. There is no hypothesis of
absolute continuity on either measure. `thm:sol-radial-d3` keeps the same $\rho$ and $\mu$ and the
same notion of criticality, and replaces the atom hypothesis with (H): $\mu(\{0\}) = 0$ and
$K = \operatorname{supp}\mu_{\mathrm{rad}}$ has no isolated point. An atomless
$\mu_{\mathrm{rad}}$ gives $\mu(\{0\}) = \mu_{\mathrm{rad}}(\{0\}) = 0$. An isolated point $r$ of
$K$ would satisfy $\mu_{\mathrm{rad}}(\{r\}) = \mu_{\mathrm{rad}}(U) > 0$ for a small neighbourhood
$U$. So the manuscript hypothesis implies (H), and the dossier theorem implies `thm:radial-d3`
exactly as quantified. The sharpening is real: an atom of $\mu_{\mathrm{rad}}$ at a non-isolated
point of $K$ is allowed, and the proof handles it, because $\mu_1$ stays atomless and the
hole constant $c_b$ includes the atom.

**Hypotheses used.**
- $\mu(\{0\}) = 0$: $\mu_1$ atomless, so $\bar\gamma_\theta = T$ and $T(0) = 0$.
- No isolated point in $K$: $R > 0$, Step A, and $b < R$.
- Rotation invariance of both measures: everywhere.
- $\Ptwo{3}$: for `def:barycentric-field`.

None is unstated. $\mu \in \Ptwo{3}$ is otherwise unused (it is in the manuscript statement). The
absolute continuity of $\rho$ is not used.

**Dependencies and fences.** The dossier uses only `def:critical-point`, through
`def:barycentric-field` and `def:sliced-wasserstein` (all `defined`). From
`def:barycentric-field` it uses the stated fact that $\bar\gamma_\theta = Q_{\rho_\theta} \circ
F_{\mu_\theta}$ $\mu_\theta$-a.e. when $\mu_\theta$ is atomless. `prop:critical-sphere` (open) and
`prop:critical-segments` appear only in remarks. `thm:radial-d3` has no `bounded_by`. The target's
fences are consistent with the theorem: the sphere violates (H), and the segments are not
rotation-invariant.

**Steps checked, line by line.**

- `lem:r3-projections`.
  - (1) Constancy in $\theta$ by transitivity, then averaging and Fubini for bounded Borel
    $\varphi$, then Archimedes. Correct, including $x = 0$.
  - (2) Tonelli gives the density $f(u) = \int_{(\abs u,\infty)} \dd\mu_{\mathrm{rad}}/(2r)$.
    The bound, evenness and monotonicity are correct, and so is $f(u) > 0 \iff (\abs u,\infty)$
    meets $K \iff \abs u < R$.
  - (3) On a hole $(a,b)$, $f = c_b$, with $0 < c_b \le 1/(2b)$ when $0 < b < R$. Correct.
- `lem:r3-quantile`, which allows an atom of $\rho$ at $0$.
  - The case $S = 0$ is trivial.
  - For $S > 0$, $\rho_1$ charges every open interval in $(-S,S)$.
  - Right-continuity: a jump $Q(p) < Q(p+)$ would make $F \equiv p$ on
    $J = (Q(p), Q(p+))$. Since $-S \le Q(p)$ and $Q(p+) \le Q(\tfrac{1+p}{2}) \le S$, $J$ lies in
    $(-S,S)$, so $\rho_1(J) > 0$, a contradiction. Correct, and also for $S = \infty$.
  - Oddness: $F(t) = 1 - F((-t)-)$, then $\sup\{F(s-) \le p\} = \sup\{F(s) \le p\} = Q^+(p) =
    Q(p)$. The last equality uses the right-continuity just proved. Each inequality checked.
  - Convexity: $p_0 = F(0) = \tfrac{1+\rho_0}{2}$ and $M = \tfrac{1-\rho_0}{2} > 0$. $Q = 0$ on
    $[\tfrac12, p_0]$, which is the flat piece from the atom. $\Phi(t) = \int_0^t g$ is
    continuous, strictly increasing and concave on $[0,S)$, and tends to $M$ (no atom at $S \neq 0$).
    Its inverse $\psi : [0,M) \to [0,S)$ is convex and nondecreasing. The identity
    $\{t \ge 0 : \Phi(t) \ge y\} = [\psi(y), \infty)$ holds, including $t \ge S$. So
    $Q = \psi((p - p_0)^+)$ on $[\tfrac12, 1)$, which is convex. Correct.
- `lem:r3-monotone`.
  - $R > 0$ follows from (H).
  - $F_1$ is continuous and strictly increasing on $(-R,R)$, onto $(0,1)$, and $F_1(b) < 1$
    for $b < R$.
  - $T$ is finite, continuous and odd, and $T_\#\mu_1 = \rho_1$.
  - $\bar\gamma_\theta = T$ $\mu_1$-a.e. for every $\theta$.
  - Convexity on $[a,b]$ for a hole with $b < R$: $F_1$ is affine increasing with values in
    $[\tfrac12, 1)$, composed with a $Q$ that is convex there. Correct, including the hole $(0,b)$.
- `lem:r3-reduction`.
  - (1) $G$ is $C^1$ on $[0,R)$ with $G' = h(r)\,r$. Only $r < R$ is used.
  - (2) Rotation by $\pi$ about $e$ kills the transverse component. By Archimedes and oddness,
    the coefficient is $\int_0^1 T(rs)\,s \dd s$. The substitution $u = rs$ and
    $3\int_0^r u^2 \dd u = r^3$ give $V(re) = -\tfrac{3}{r^2} G(r)\,e$. Recomputed; correct with
    the factor $d = 3$.
  - (3) The dossier reads the definition as supplying a $\mu\otimes\sigma$-measurable version of
    $(x,\theta) \mapsto \bar\gamma_\theta(\inner{x}{\theta})$. Without such a version, the integral
    defining $v_\mu$ has no meaning, so this is the only coherent reading of
    `def:barycentric-field`, not an added hypothesis. Tonelli then gives
    $(\mu\otimes\sigma)(N) = \int \mu_1(N_\theta) \dd\sigma = 0$, so $v_\mu = V$ $\mu$-a.e. on
    $\{0 < \abs x < R\}$, independently of the version. Correct.
  - (4) $Z = \{G \neq 0\} \cap (0,R)$ is open. $\mu_{\mathrm{rad}}(Z) = 0$ follows from
    criticality, which is used only through $\mu$-null sets. So $Z \cap K = \emptyset$. Nothing is
    evaluated at $\abs x = R$. Correct.
- `lem:r3-support`.
  - $R \in K$ when $R < \infty$.
  - A component $(a,b)$ of $(0,R)\setminus K$ with $b = R$ would make $R$ isolated when
    $R < \infty$, and would contradict $\sup K = \infty$ when $R = \infty$. Hence $b < R$ and
    $b \in K$, and $a \in K$ when $a > 0$. Correct.
- Final proof.
  - Step A: $r \in K \cap (0,R)$ is an interior point of the domain of the $C^1$ function $G$,
    so $G'(r)$ exists. It equals the limit of the difference quotients along $r_n \in K \cap
    (0,R)\setminus\{r\}$, where $G = 0$, so $h(r)\,r = 0$ and $T(r) = r$. Differentiability is
    claimed only at points of $(0,R)$, where it holds.
  - Step B: $h$ is convex on $[a,b]$, with $h(a) = h(b) = 0$ (Step A, or $T(0) = 0$ when
    $a = 0$), so $h \le 0$. Since $G(b) - G(a) = 0$ and $h(u)\,u \le 0$ is continuous,
    $h = 0$ on $(a,b]$. Correct.
  - Step C: the partition of $[0,R)$ and oddness.
  - Step D: $\rho_1 = T_\#\mu_1 = \mu_1$, then Cramér–Wold through characteristic functions.
    Correct.

**Audit tests (brief).**
- *Sphere* $r_*\Sph{2}$, $\rho = N(0,I_3)$: $K = \{r_*\}$ is an isolated point. The argument
  breaks exactly at the hypothesis "K has no isolated point": the only component is $(0,R)$, with
  $b = R$, and Step A has nothing to act on. All criticality information sits on $\abs x = R$,
  which the proof never uses. I re-derived the remark's condition:
  $\int_0^1 \Phi^{-1}(\tfrac{1+s}{2})\,s \dd s = 4\int_0^\infty \varphi^2 = 1/\sqrt\pi = r/3$, so
  $r = 3/\sqrt\pi$, consistent with `sec:overview`.
  - The hypothesis that bites is implied by absolute continuity of $\mu$, as the brief requires.
  - The brief's "first scouting sketch" error, $T(b) = b$ at $b = R$, is not repeated.
- *Atom at 0*: $\delta_0$ is excluded by $\mu(\{0\}) = 0$. An atom of $\rho$ at $0$ is handled
  in `lem:r3-quantile` (3).
- *Segments*: these measures are not rotation-invariant in $\R^3$, so they are out of scope.
- *Unbounded supports*: $R = \infty$ and $S = \infty$ are handled. $G$ is finite on $[0,R)$. No
  component is unbounded.
- *Fat Cantor supports*: Step A is pointwise and Step B treats each component independently,
  with no ordering or induction.
- *Irregular densities*: no integration by parts against $\mu$ is used.

**Citations.** The step that uses Santambrogio (2015) rests on the fact stated in
`def:barycentric-field`, so the citation is not load-bearing. I did not re-check the book. The
earlier certified review `2026-10-20-thm-gaussian-target.md` records that the optimality
statement is Theorem 2.9, not Theorem 2.5 (Correction 1). Archimedes, Cramér–Wold, Tonelli and
the elementary properties of $Q$ are standard and are used within their hypotheses.

**Build.** `uv run scripts/check.py` exits 0 with no MyST error for the dossier.

**Verdict.** I checked every step of the proof and each one holds. The dossier proves
`thm:sol-radial-d3`, which implies `thm:radial-d3` exactly as quantified. Pass.

## Corrections

These are editorial only and none affects a step. Applying any of them lapses this
certification; an editorial note can carry it over.

1. `solutions/thm-radial-d3.md`, line 55: "Theorem 2.5" should read "Theorem 2.9 (with the
   monotone map of Theorem 2.5)". This follows the earlier review's reading of Santambrogio (2015).
2. `solutions/thm-radial-d3.md`, lines 506–509 (`rem:r3-cantor-unbounded`): the normalized
   Lebesgue measure on a closed set $K$ need not have support $K$. Require every relatively open
   subset of $K$ to have positive Lebesgue measure (true for the Smith–Volterra–Cantor set), or
   write "its support". This is a remark, not part of the proof.

## Exclusions

- The remarks `rem:r3-hypotheses`, `rem:r3-sphere-audit`, `rem:r3-atom-origin`,
  `rem:r3-cantor-unbounded` and `rem:r3-dimension` are commentary. I checked them only for
  consistency. Nothing here certifies `prop:critical-sphere`, the value $r_* = 3/\sqrt\pi$, or
  any claim for $d \neq 3$.
- Not certified: whether mixtures $p\,\delta_0 + (1-p)\nu$ can be critical (the dossier leaves
  this open). Also not certified: the manuscript's "Idea of the proof" and "Limits" prose for
  `thm:radial-d3`, and `thm:radial-disc-d2`.
- The certified result covers any rotation-invariant $\rho \in \Ptwo{3}$, without a density. That
  is a sharpening of the manuscript statement. Recording it is the orchestrator's call.
