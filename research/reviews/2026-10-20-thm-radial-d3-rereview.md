---
verdict: pass
authors:
  - researcher, claude-opus-5-5, 2026-10-20
reviewer: reviewer, claude-opus-5-5, 2026-10-20
fingerprints:
  solutions/thm-radial-d3.md: 78187ff1b753db99c6ec3edce135209d08619a1c5edd893818ac4aba163b7d6d
  thm:radial-d3: 61d070fb07106b54aa860ad86b8ffa4c03159f59249e5dfd5f25c2d458de4750
  def:critical-point: 2b3f99b415e32bcde26bf522b879305fe3edffd9318cf15b85f6d1b9699a06a5
---

Certify re-review of `solutions/thm-radial-d3.md` against `thm:radial-d3`. Fresh context; I
did not write or direct the dossier and did not write the earlier review.

## Findings

*Re-review of `research/reviews/2026-10-20-thm-radial-d3.md`.*

**Versions compared.** Baseline: commit `34adda0`. In an isolated `git worktree` of it,
`check.py --fingerprint solutions/thm-radial-d3.md` gives exactly the recorded fingerprints
(dossier `7b79870e…`, `thm:radial-d3` `61d070fb…`, `def:critical-point` `2b3f99b4…`). Baseline
verified. Current: the working-tree dossier (`78187ff1…`); both statements unchanged
(`check.py --impact`).

**The changes.** Two hunks, applying the earlier report's Corrections 1 and 2.

1. Line 55, dependencies paragraph: Santambrogio (2015) "Theorem 2.5" → "Theorem 2.9" for the
   one-dimensional optimal transport fact. The fact is the one stated in
   `def:barycentric-field` and used from there; the earlier report found the citation not
   load-bearing. Mathematics unchanged.
2. `rem:r3-cantor-unbounded`, fat Cantor bullet (lines 506–509): a hypothesis is added on $K$,
   "every relatively open subset of which has positive Lebesgue measure (a Smith–Volterra–Cantor
   set, for instance)". This changes the remark's hypotheses, hence this re-review.

**Check of change 2.** With the added hypothesis, $\operatorname{supp}(\Leb|_K) = K$: it is
contained in $K$ because $K$ is closed, and every $x \in K$ is in it because each neighbourhood
of $x$ meets $K$ in a relatively open set of positive measure. So $\operatorname{supp}
\mu_{\mathrm{rad}} = K$, which the remark's description of $(0,R) \setminus K$ (holes dense in
$[1,2]$, since $K$ has no interior) and its appeal to `lem:r3-support` (3) require; without it
the support could be a proper subset of $K$, which is the defect the earlier report named. A
Smith–Volterra–Cantor set (rescaled to $[1,2]$) has the property: its intersection with an open
interval meeting it contains a scaled copy of a positive-measure construction stage. The density
$\propto \one_K(\abs{x})\abs{x}^{-2}$ is unchanged and correct in $\R^3$. The remark is
commentary, used by no step of the proof; restricting its example weakens, never strengthens,
what it asserts, so no proof step and no other remark is affected.

**Conclusions retained.** Every other line is identical to the certified version, so the
earlier report's conclusions stand: statement agreement (the dossier theorem implies
`thm:radial-d3` as quantified, with $\rho$ any rotation-invariant measure in $\Ptwo{3}$), all
lemmas and Steps A and B, hypotheses, the audit tests, dependencies and fences. The argument's
structure is unchanged; a full review is not needed.

**Build.** `uv run scripts/check.py --fast` reports no MyST error for the dossier.

## Corrections

None blocking. One non-blocking observation on the remark (present in the baseline, not
introduced by this edit): "$(0,R) \setminus K$ consists of $(0,1)$ and countably many holes"
presumes $1 \in K$ (and $R = \max K$); for a general $K \subset [1,2]$ the first component is
$(0, \min K)$. True for the Smith–Volterra–Cantor example; "$(0,\min K)$" would be exact.

## Exclusions

As in the earlier report: the remarks (`rem:r3-hypotheses`, `rem:r3-sphere-audit`,
`rem:r3-atom-origin`, `rem:r3-cantor-unbounded`, `rem:r3-dimension`) are commentary and are
not certified beyond the consistency check above; nothing certifies `prop:critical-sphere`,
$r_* = 3/\sqrt\pi$, claims for $d \ne 3$, mixtures $p\,\delta_0 + (1-p)\nu$, or the manuscript
prose. Santambrogio (2015) was not re-checked here; the earlier report's reading is retained.
