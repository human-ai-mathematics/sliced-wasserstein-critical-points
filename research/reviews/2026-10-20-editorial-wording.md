---
verdict: editorial
amends:
  - research/reviews/2026-10-20-thm-gaussian-target.md
  - research/reviews/2026-10-20-thm-radial-disc-d2-rereview.md
  - research/reviews/2026-10-20-prop-notions-coincide-rereview2.md
  - research/reviews/2026-10-20-prop-critical-sphere-rereview.md
authors:
  - researcher, claude-opus-5-5, 2026-10-20
reviewer: reviewer, claude-opus-5-5, 2026-10-20
changes:
  solutions/thm-gaussian-target.md: {from: 377e0ab81f2fc2a2381070db22df30321aa83cf2cf5beaaeee69e6f1d1e33cb5, to: f7cb12d37309b40020d6a4ffb932997f32fedd9c225fb206a8da51303258b5c6}
  solutions/thm-radial-disc-d2.md: {from: dde77b5e56f01a7aeb8b1cd1f6e8fc51d1059bd93a245fef6d9c53d22867bcb4, to: 8cd85ab627d2b0d8c872334ac0c9df0e9dddf05d2485ffbd25b3b2ed97f89b9a}
  solutions/prop-notions-coincide.md: {from: 1f11bb8df5a2984e99b5a7ea0624edf13d40b4b7e1b1f6bb24792cb9129d767b, to: d5f67fe4c87e9d58c49d594ded9da2559ac8c1bed9a641ee2bd182cf9ecc2a41}
  solutions/prop-critical-sphere.md: {from: bd47ad6d544d33efd5ab2ff430724895f90b0ab462493ef038496db2c6a2e5e6, to: d71be6355e80f54b7428aa6b51b32bcc881a9c543720473a25df83a6500d127d}
---

# Editorial note on four 2026-10-20 reports (wording pass)

Fresh context; I wrote none of the dossiers or the amended reports. `check.py --diff` verified
each baseline against the recorded fingerprints (after `2026-10-20-editorial-citations.md` for
`thm-gaussian-target`), and `check.py --impact` names no changed manuscript statement; the
diffs below are its output. The ledger records `prop:critical-sphere` and
`prop:critical-segments` as `proved`, and `sec:open-directions` (modules/05-open-directions.md)
states the planar annulus case as open, so the new status wording and the new cross-reference
are accurate.

Of the five dossiers edited in this pass, `solutions/thm-radial-d3.md` is **not** carried over:
in `rem:r3-cantor-unbounded`, with $K \subset [1,2]$ arbitrary, "(0,1)" and "dense in $[1,2]$"
became "$(0,\min K)$" and "dense in $[\min K, \max K]$". This changes a formula and corrects a
claim (the old one was false when $\min K > 1$ or $\max K < 2$), so it takes a re-review.

## `solutions/thm-gaussian-target.md`

```diff
--- certified/solutions/thm-gaussian-target.md
+++ current/solutions/thm-gaussian-target.md
@@ -5,8 +5,8 @@
   enumerator: "2.%s"
 ---
 
-% Proof dossier for thm:gaussian-target (researcher, prove lens). Uncertified draft until a
-% proofs[] record in the ledger names it. Reproved from scratch; the scouting notes of
+% Proof dossier for thm:gaussian-target (researcher, prove lens); certified (see the proofs[]
+% record in the ledger). Reproved from scratch; the scouting notes of
 % 17 October 2026 (ensae-conjecture-scouting/verification/13-korba-sw/C-*.md) were read for
 % the idea only and are not cited as authority.
 
@@ -41,12 +41,12 @@
 
 **Dependencies.**
 
-- Manuscript nodes: [](#def:critical-point), hence [](#def:barycentric-field) and
+- Manuscript results: [](#def:critical-point), hence [](#def:barycentric-field) and
   [](#def:sliced-wasserstein). From [](#def:barycentric-field) we use its stated fact that,
   when $\mu_\theta$ has no atom, $\bar\gamma_\theta = T_\theta$ $\mu_\theta$-a.e. This is the
   one-dimensional optimal transport theorem: Santambrogio, *Optimal Transport for Applied
   Mathematicians* (2015), Theorem 2.9 (with the monotone map of Theorem 2.5), restated as Theorem B.6 of
-  {cite:t}`VauthierKorbaMerigot2025`. No other node is used. In particular,
+  {cite:t}`VauthierKorbaMerigot2025`. No other result of the manuscript is used. In particular,
   [](#prop:notions-coincide), [](#thm:cs-isotropic) and [](#prop:critical-sphere) are **not**
   used. [](#prop:critical-segments) and [](#prop:critical-sphere) appear only in the audit
   remarks, which are not part of the proof.
@@ -554,7 +554,7 @@
   no atom (so $\bar\gamma_\theta = T_\theta$) and the second moments. [](#lem:gt-one-dim) and the
   final step only involve the one-dimensional laws $\mu_\theta$, which are absolutely
   continuous; they apply to every $\theta$ with $\int T_\theta'\dd\mu_\theta < \infty$.
-- Hence, if the sphere is critical as [](#prop:critical-sphere) asserts, [](#eq-gt-II) must
+- Hence, since the sphere is critical ([](#prop:critical-sphere)), [](#eq-gt-II) must
   fail for it: the step that the sphere defeats is precisely the passage through
   [](#lem:gt-stampacchia). For $d = 3$ this is visible directly. There
   $\mu_\theta = \mathrm{Unif}[-r, r]$ and $T_\theta$ maps $(-r, r)$ onto $\R$, so
@@ -562,7 +562,7 @@
   for every $\theta$.
 
 This bullet list is a consistency check, not part of the proof. [](#prop:critical-sphere) is
-not certified here and nothing above rests on it.
+proved separately and nothing above rests on it.
 :::
 
 :::{prf:remark} Audit: the critical segments
@@ -623,8 +623,8 @@
 recorded so that a reviewer can check it against the manuscript.
 :::
 
-**Fences respected.** [](#thm:gaussian-target) has no `bounded_by`. The fences of the target,
-[](#prop:critical-segments) (proved) and [](#prop:critical-sphere) (open), exhibit critical
+**Consistency with the known critical points.** The known singular critical points,
+[](#prop:critical-segments) and [](#prop:critical-sphere) (both proved), exhibit critical
 points for $\rho = N(0, I_d)$ that are not absolutely continuous. The theorem assumes
 $\mu \ll \Leb$ and so does not contradict them. [](#rem:gt-sphere-audit) and
 [](#rem:gt-segments-audit) locate the step each of them defeats.
```

Why the mathematics is unchanged: the statement, formulas, hypotheses, quantifiers, constants
and steps read the same; only comments, the word "node" (→ "result"), the "Fences respected"
heading and status wording about `prop:critical-sphere` changed. In `rem:gt-sphere-audit`,
"if the sphere is critical as [prop] asserts" → "since the sphere is critical ([prop])"
discharges the remark's conditional by citing a result the ledger records as proved; the
remark's derivation is unchanged, and the remark still says it is not part of the proof and
that nothing in the proof rests on `prop:critical-sphere`.

## `solutions/thm-radial-disc-d2.md`

```diff
--- certified/solutions/thm-radial-disc-d2.md
+++ current/solutions/thm-radial-disc-d2.md
@@ -5,8 +5,8 @@
   enumerator: "4.%s"
 ---
 
-% Proof dossier for thm:radial-disc-d2 (route ap:certify-scouting, lens prove). Uncertified
-% draft until a proofs[] record in the ledger names it. Reproved from scratch; the scouting
+% Proof dossier for thm:radial-disc-d2 (route ap:certify-scouting, lens prove). Certified
+% (see the proofs[] record in the ledger). Reproved from scratch; the scouting
 % notes ensae-conjecture-scouting/verification/13-korba-sw/A-radial-d2.md (§1, §2 (P1), (P3))
 % and 1-relecture.md (§4) were read for the idea only and are not cited as authority.
 % Normalizations: def:sliced-wasserstein (sigma a probability) and def:barycentric-field
@@ -48,8 +48,8 @@
 **Dependencies.** The definitions [](#def:sliced-wasserstein), [](#def:barycentric-field) and
 [](#def:critical-point), including the identification $\bar\gamma_\theta = T_\theta$
 $\mu_\theta$-a.e. when $\mu_\theta$ has no atom, which is part of
-[](#def:barycentric-field). No other node of the manuscript is used in the proof:
-[](#thm:bonnotte-full-support), [](#prop:critical-sphere) and the other nodes named below
+[](#def:barycentric-field). No other result of the manuscript is used in the proof:
+[](#thm:bonnotte-full-support), [](#prop:critical-sphere) and the other results named below
 appear only in remarks. Literature results used, all classical: Fubini–Tonelli; Lebesgue's
 differentiation theorem (a locally integrable function whose integral over every interval
 vanishes is zero a.e.); uniqueness of a finite Borel measure on $\R^2$ given its Fourier
@@ -427,13 +427,13 @@
 would give $Q_{\rho_1} = Q_{\mu_1}$ off the band of levels $(F_{\mu_1}(0^-), F_{\mu_1}(0))$, and
 monotonicity would squeeze $Q_{\rho_1}$ to $0$ on that band. Writing this out requires the
 barycentric projection of the monotone plan at the non-atomic points of a measure with one
-atom; it is not done in this dossier, and [](#thm:sol-rd2-main) does not claim it.
+atom; it is not done here, and [](#thm:sol-rd2-main) does not claim it.
 :::
 
 :::{prf:remark} Why the argument does not extend to an annulus
 :label: rem:sol-rd2-annulus
-Let $\mu$ be radial with radial support $[c, R]$, $0 < c < R \le \infty$ (the setting of the
-open candidate `cand:annulus-d2`). Steps 1 to 4 still run with the open annulus
+Let $\mu$ be radial with radial support $[c, R]$, $0 < c < R \le \infty$ (the annulus case,
+which remains open: [](#sec:open-directions)). Steps 1 to 4 still run with the open annulus
 $\{c < \abs x < R\}$ in place of $B(0,a) \setminus \{0\}$ — the continuity argument of
 [](#lem:sol-rd2-continuous), part 3, does not use the origin, and the computation of
 [](#lem:sol-rd2-reduction) holds for every $r \in (0,R)$ once $T$ is odd — and give
@@ -462,7 +462,7 @@
 bounded derivative: $h'(s) = 2sU'(s^2)$, with $U'$ continuous on $[0,\infty)$ and of order
 $x^{-5/2}$ at infinity) and that $T_\#\mu_1$ be the projection $\rho_1$ of a *positive* radial
 measure $\rho$, which in the plane is a sign condition on an inverse Abel transform inside the
-hole. That non-local sign condition is exactly what `cand:annulus-d2` asks about; nothing here
+hole. That non-local sign condition is exactly the open question of the annulus case; nothing here
 decides it. (The claims of this paragraph on $T$ are checked only in outline and are not used
 anywhere.)
 
@@ -514,8 +514,7 @@
 turns on; [](#rem:sol-rd2-annulus) shows why.
 :::
 
-**Fences respected.** [](#thm:radial-disc-d2) has no `bounded_by` node. The fences of the
-target are checked anyway. [](#prop:critical-sphere) ($d = 2$): the critical circle has
+**Consistency with the known critical points.** [](#prop:critical-sphere) ($d = 2$): the critical circle has
 support a circle, not a disc, so it is outside the hypotheses of [](#thm:sol-rd2-main),
 although it satisfies $\mu(\{0\}) = 0$ ([](#rem:sol-rd2-circle)). [](#prop:critical-segments):
 a measure carried by a segment is not radial, and its support is not a disc. $\delta_0$, critical
```

Why the mathematics is unchanged: the statement, formulas, hypotheses, quantifiers, constants
and steps read the same; only a comment, "node"/"dossier" → "result"/"here", the "Fences
respected" heading, and the harness name `cand:annulus-d2` (replaced by a pointer to the same
open annulus question in `sec:open-directions`) changed, in remarks the proof does not use.

## `solutions/prop-notions-coincide.md`

```diff
--- certified/solutions/prop-notions-coincide.md
+++ current/solutions/prop-notions-coincide.md
@@ -47,7 +47,7 @@
 atoms.
 
 **Dependencies.** The definitions [](#def:sliced-wasserstein), [](#def:barycentric-field)
-and [](#def:critical-point). No other node of the manuscript is used; in particular
+and [](#def:critical-point). No other result of the manuscript is used; in particular
 [](#prop:critical-sphere) and [](#prop:critical-segments) are only discussed in a remark,
 never used. Literature results used, all classical:
 
@@ -605,7 +605,7 @@
   three notions coincide as well: the sphere of [](#prop:critical-sphere), stated there as a
   Wasserstein critical point, is a critical point and a Lagrangian critical point, and the
   segments, stated as critical points, are also Lagrangian and Wasserstein critical points.
-  (This uses only the statements of those two results, which this dossier does not prove.)
+  (This uses only the statements of those two results, which are proved separately.)
   Consequently, the equivalence of notions cannot be where a proof of [](#conj:sw-critical)
   uses absolute continuity of $\mu$: it passes the sphere test and the segment test of the
   problem without distinguishing them from absolutely continuous measures. A proof of the
@@ -637,7 +637,7 @@
   [](#lem:sol-nc-geodesic) is $\ge 0$; part (b) proves the existence of the derivatives for
   atomless $\mu$. Their existence for general $\mu$, which
   {cite:t}`VauthierKorbaMerigot2025`, Proposition 4.7(a), derive from convexity, is not used.
-- Every step above is written out; the dossier rests on the four literature results listed
+- Every step above is written out; the proof rests on the four literature results listed
   under *Dependencies*, whose theorem numbers a reviewer should check against the editions in
   the bibliography.
 :::
@@ -654,8 +654,8 @@
 compact supports and atomless $\rho$, keeping only that $\mu$ has no atom.
 :::
 
-**Fences respected.** [](#prop:notions-coincide) has no `bounded_by` node. The fences of the
-target, [](#prop:critical-segments) and [](#prop:critical-sphere), concern
+**Consistency with the known critical points.** The known singular critical points,
+[](#prop:critical-segments) and [](#prop:critical-sphere), concern
 [](#conj:sw-critical), not this statement; [](#rem:sol-nc-singular) checks that the refined
 statement is consistent with both (they are atomless, and the equivalence holds for them),
 and uses neither.
```

Why the mathematics is unchanged: the statement, formulas, hypotheses, quantifiers, constants
and steps read the same; only "node"/"dossier" → "result"/"proof", the "Fences respected"
heading, and "which this dossier does not prove" → "which are proved separately" (accurate
status, in a remark that uses only those statements and is not part of the proof) changed.

## `solutions/prop-critical-sphere.md`

```diff
--- certified/solutions/prop-critical-sphere.md
+++ current/solutions/prop-critical-sphere.md
@@ -366,7 +366,7 @@
 
 $d$ times the covariance of $\zeta_d$ and $N(0,1)$ under their monotone coupling. For
 $d = 2$, $\zeta_2$ is the law of $\cos\Psi$ with $\Psi$ uniform on $(0,2\pi)$, $Q_{\zeta_2}(u)
-= -\cos(\pi u)$ and $r_* = -2\,\E[G\cos(\pi\Phi(G))]$ with $G \sim N(0,1)$. This dossier gives
+= -\cos(\pi u)$ and $r_* = -2\,\E[G\cos(\pi\Phi(G))]$ with $G \sim N(0,1)$. This proof gives
 a closed form only for $d = 3$; whether other dimensions admit one is not addressed. The
 bound $r_* < \sqrt d$ says that the critical sphere has a smaller second moment, $r_*^2$,
 than the target, whose second moment is $d$.
@@ -409,8 +409,8 @@
 No discrepancy affecting the result was found.
 :::
 
-**Fences respected.** [](#prop:critical-sphere) has no `bounded_by` node. The sphere is a
-fence of [](#conj:sw-critical); [](#thm:sol-cs-main) is consistent with that conjecture,
+**Consistency.** The sphere is a test case for [](#conj:sw-critical); [](#thm:sol-cs-main) is
+consistent with that conjecture,
 since $\mu_{r_*}$ is not absolutely continuous (it is concentrated on a Lebesgue-null sphere),
 and with [](#prop:notions-coincide), since $\mu_{r_*}$ has no atom and is critical in all three
 senses at once.
```

Why the mathematics is unchanged: the statement, formulas, hypotheses, quantifiers, constants
and steps read the same; only "dossier" → "proof" and the "Fences respected" heading ("fence"
→ "test case", dropping the harness remark on `bounded_by`) changed, in a closing consistency
paragraph.
