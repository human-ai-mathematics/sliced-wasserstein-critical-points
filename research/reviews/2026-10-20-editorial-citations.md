---
verdict: editorial
amends:
  - research/reviews/2026-10-20-thm-gaussian-target.md
authors:
  - researcher, claude-opus-5-5, 2026-10-20
reviewer: reviewer, claude-opus-5-5, 2026-10-20
changes:
  solutions/thm-gaussian-target.md: {from: 2d5de6b7b93a8154e876f869536672fa04c810a04ac40bbe977b1081a9638ad6, to: 377e0ab81f2fc2a2381070db22df30321aa83cf2cf5beaaeee69e6f1d1e33cb5}
---

# Editorial note on `research/reviews/2026-10-20-thm-gaussian-target.md`

Fresh context; I wrote neither the dossier nor the amended report. The baseline (commit
`34adda0`, isolated `git worktree`) reproduces the fingerprints the report records;
`thm:gaussian-target` and `def:critical-point` are unchanged (`check.py --impact` names no
changed statement). The edit applies the report's Corrections 1 and 2.

Of the four dossiers edited in the same pass, only this one is carried over here. The edits to
`solutions/thm-radial-d3.md` (a hypothesis added in `rem:r3-cantor-unbounded`),
`solutions/thm-radial-disc-d2.md` ("has µ-measure" → "has µ-measure at most", a changed step)
and `solutions/prop-notions-coincide.md` (an added claim on Villani's orientation of cyclical
monotonicity) each change a hypothesis, a step or a claim, and are re-reviewed separately.

## `solutions/thm-gaussian-target.md`

```diff
@@ -45,7 +45,7 @@
   [](#def:sliced-wasserstein). From [](#def:barycentric-field) we use its stated fact that,
   when $\mu_\theta$ has no atom, $\bar\gamma_\theta = T_\theta$ $\mu_\theta$-a.e. This is the
   one-dimensional optimal transport theorem: Santambrogio, *Optimal Transport for Applied
-  Mathematicians* (2015), Theorem 2.5, restated as Theorem B.6 of
+  Mathematicians* (2015), Theorem 2.9 (with the monotone map of Theorem 2.5), restated as Theorem B.6 of
   {cite:t}`VauthierKorbaMerigot2025`. No other node is used. In particular,
@@ -54,7 +54,8 @@
   Differential Equations of Second Order* (2nd ed., 1983), Lemma 7.7: if $u$ is weakly
   differentiable on an open set $\Omega$ (that is, $u, Du \in L^1_{\mathrm{loc}}(\Omega)$), then
   $Du = 0$ a.e. on any set where $u$ is constant. The same result is Theorem 4.4(iv) of
-  Evans–Gariepy, *Measure Theory and Fine Properties of Functions* (revised ed., 2015). We
+  Evans–Gariepy, *Measure Theory and Fine Properties of Functions* (revised ed., 2015), stated
+  there for $W^{1,p}(U)$ and applied here on each open $\Omega' \Subset \Omega$. We
   also use, without numbering, standard facts: Fubini–Tonelli, Lebesgue's density
```

Why the mathematics is unchanged: the statement, formulas, hypotheses, quantifiers, constants
and steps read the same; only the theorem number of the Santambrogio citation (for the same
fact, taken from `def:barycentric-field`) and a clause on how the secondary Evans–Gariepy
reference applies (by localization, to the same fact already cited from Gilbarg–Trudinger
Lemma 7.7) changed. Neither adds a claim used by the proof.
