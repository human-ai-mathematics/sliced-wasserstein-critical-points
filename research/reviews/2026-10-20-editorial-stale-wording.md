---
verdict: editorial
amends:
  - research/reviews/2026-10-20-sharpened-statements-rereview.md
authors:
  - researcher, claude-opus-5-5, 2026-10-20
reviewer: reviewer, claude-opus-5-5, 2026-10-20
changes:
  solutions/thm-radial-disc-d2.md: {from: 9e183e25d27e9de3854c5e4d03d56ea37d491382f902a429c080d5dcd42cae7c, to: 03d89f57f74ecacd945ce09decf57f4c1ac2483fa7cb37ed62a516e04978ae10}
---

# Editorial note on `research/reviews/2026-10-20-sharpened-statements-rereview.md`

Fresh context; I wrote neither the dossier nor the amended report. `check.py --diff` verified
the baseline (`4aa38f124d02`) against the certified fingerprint, which is the `to` of
`2026-10-20-editorial-sharpened-wording.md`; an isolated `git worktree` of HEAD fingerprints the
dossier as `9e183e25…`. `check.py --impact` names no changed manuscript statement
(`thm:radial-disc-d2` is `74efe825…` as recorded). The diff below is its output.

Of the three dossiers edited in this pass, only this one is carried over here. The edits to
`solutions/prop-notions-coincide.md` (the last paragraph of the proof of `thm:sol-nc-main`
now derives item 2 of `prop:notions-coincide` without absolute continuity) and to
`solutions/prop-critical-sphere.md` (the closing proof sentence gains the premise
$r_* < \sqrt d$; the uniqueness is re-attributed in the overview) change steps of proof, and
are re-reviewed in `2026-10-20-prop-notions-coincide-rereview3.md` and
`2026-10-20-prop-critical-sphere-rereview3.md`.

## `solutions/thm-radial-disc-d2.md`

```diff
@@ -397,7 +397,7 @@
 :::{prf:remark} Audit: the critical circle
 :label: rem:sol-rd2-circle
 Let $\mu$ be the uniform probability on $r_*\Sph{1}$ and $\rho = N(0,I_2)$, critical by
-[](#prop:critical-sphere) with $d = 2$ and the first part of [](#prop:notions-coincide). It
+[](#prop:critical-sphere) with $d = 2$. It
 is radial with $\mu(\{0\}) = 0$, and $\mu_1$ (the arcsine law on $[-r_*,r_*]$) has no atom: all
 steps up to [](#lem:sol-rd2-reduction) apply, with $R = r_*$. What fails is the support
 hypothesis: there is no $a > 0$ with $B(0,a) \subset \operatorname{supp}\mu$, so
```

Why the mathematics is unchanged: the statement, formulas, hypotheses, quantifiers,
constants and steps read the same; only a stale cross-reference in an audit remark did. The
current `prop:critical-sphere` (modules/03-singular-critical-points.md:29–33) states directly
that the sphere is a critical point (`def:critical-point`, item 1), so the remark's claim
"critical" no longer needs `prop:notions-coincide`; the remark is not a step of the proof of
`thm:sol-rd2-main`.
