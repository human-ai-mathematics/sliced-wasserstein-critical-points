---
verdict: pass
authors:
  - researcher, claude-opus-5-5, 2026-10-20
reviewer: reviewer, claude-opus-5-5, 2026-10-20
fingerprints:
  solutions/thm-radial-d3.md: 6f0a737fa248491be1e86f068221b62a124df93afbd9090484cfa9b2a5e211e5
  thm:radial-d3: 61d070fb07106b54aa860ad86b8ffa4c03159f59249e5dfd5f25c2d458de4750
  def:critical-point: 2b3f99b415e32bcde26bf522b879305fe3edffd9318cf15b85f6d1b9699a06a5
---

Certify re-review of `solutions/thm-radial-d3.md` against `thm:radial-d3`. Fresh context; I
did not write or direct the dossier and wrote none of its earlier reviews.

## Findings

*Re-review of `research/reviews/2026-10-20-thm-radial-d3-rereview.md`.*

**Versions compared.** Baseline: commit `6e6b42f`. In an isolated `git worktree` of it,
`check.py --fingerprint solutions/thm-radial-d3.md` gives exactly the fingerprints recorded in
that report (dossier `78187ff1…`, `thm:radial-d3` `61d070fb…`, `def:critical-point`
`2b3f99b4…`). Baseline verified. Current: the working-tree dossier (`6f0a737f…`); both
statements are unchanged (same fingerprints), and `thm:radial-d3` still has no `bounded_by` and
depends only on `def:critical-point` in the ledger.

**The changes** (`git diff 6e6b42f -- solutions/thm-radial-d3.md`), five hunks.

1. Header `%` comment: "Uncertified draft until a proofs[] record … names it" → "Certified (see
   the proofs[] record in the ledger)". A comment line, outside the fingerprint and the
   mathematics.
2. Dependencies paragraph: "Manuscript nodes" → "Manuscript results"; "No other node is used" →
   "No other result of the manuscript is used". Same list, same exclusion; the list still names
   `def:critical-point`, `def:barycentric-field`, `def:sliced-wasserstein` and the same one-
   dimensional fact. No step changes.
3. `rem:r3-sphere-audit`, last sentence: `prop:critical-sphere` "which is not certified here" →
   "which is proved separately". Agrees with the ledger (`status: proved`, with a proof record).
   The sentence's point, that nothing in the proof rests on it, is unchanged and true: the
   proof does not cite it.
4. Final paragraph: heading "Fences respected" → "Consistency with the known critical points",
   the sentence "[thm:radial-d3] has no `bounded_by`. The fences of the target:" removed, and
   `prop:critical-sphere` "(open)" → "(proved)". The comparison that follows (the sphere's
   radial law is an atom at an isolated support point, excluded by (H); `prop:critical-segments`
   is not rotation-invariant) is unchanged. The removed sentence was an assertion about the
   ledger, still true; no fence exists to respect. No step changes.
5. `rem:r3-cantor-unbounded`, fat Cantor bullet: "$(0,R)\setminus K$ consists of $(0,1)$ and
   countably many holes, dense in $[1,2]$" → "… of $(0,\min K)$ and countably many holes, dense
   in $[\min K,\max K]$". This is the earlier report's non-blocking observation, applied.

**Check of change 5.** Here $K \subset [1,2]$ is closed, without interior, and every relatively
open subset has positive measure, so (as the earlier report showed) $K =
\operatorname{supp}\mu_{\mathrm{rad}}$ and $R = \sup K = \max K$. Then $(0,R)\setminus K =
(0,\min K) \cup ([\min K,\max K]\setminus K)$, a disjoint union. Since $\min K \ge 1 > 0$,
$(0,\min K)$ is a non-empty component with endpoints $0$ and $\min K \in K$, and $\min K < R$
because $K$ has positive measure, so is not a point. The second set is open, hence a countable
union of open intervals with endpoints in $K$; it is dense in $[\min K,\max K]$ because $K$ has
no interior. This matches `lem:r3-support` (3) (each component is $(a,b)$ with $b<R$, $b\in K$,
$a\in K$ or $a=0$), on which the remark relies. The new formula is exact for every such $K$;
the old one held only when $1 = \min K$ and $2 = \max K$. The remark is commentary, used by no
step of the proof, so nothing downstream is affected.

**Conclusions retained.** Every other line is identical to the version certified by the earlier
report, and the edits above alter no step of proof, no hypothesis, no lemma and the dossier
theorem not at all. The conclusions of `research/reviews/2026-10-20-thm-radial-d3-rereview.md`
(and, through it, of `research/reviews/2026-10-20-thm-radial-d3.md`) stand: statement
agreement with `thm:radial-d3`, the lemmas, Steps A and B, hypotheses, dependencies, citations
and the absence of fences. The argument's structure is unchanged; a full review is not needed.

**Build.** `uv run scripts/check.py --fast` reports no MyST error for the dossier.

## Corrections

None.

## Exclusions

As in the earlier reports: the remarks (`rem:r3-hypotheses`, `rem:r3-sphere-audit`,
`rem:r3-atom-origin`, `rem:r3-cantor-unbounded`, `rem:r3-dimension`) and the final consistency
paragraph are commentary, checked only for consistency. Nothing here certifies
`prop:critical-sphere` (its "proved" is read from the ledger; whether its own certification is
current is outside this review), $r_* = 3/\sqrt\pi$, claims for $d \ne 3$, mixtures
$p\,\delta_0 + (1-p)\nu$, the header comment's status claim, or the manuscript prose.
Santambrogio (2015) was not re-checked; the earlier reading is retained.
