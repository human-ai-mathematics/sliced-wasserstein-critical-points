---
verdict: pass
authors:
  - researcher, claude-opus-5-5, 2026-10-20
reviewer: reviewer, claude-opus-5-5, 2026-10-20
fingerprints:
  solutions/prop-notions-coincide.md: 1f11bb8df5a2984e99b5a7ea0624edf13d40b4b7e1b1f6bb24792cb9129d767b
  prop:notions-coincide: 75847c27e7b0052fc43c8abf198988644a0b57da282b0226d71e368cbd3caf2d
  def:critical-point: 2b3f99b415e32bcde26bf522b879305fe3edffd9318cf15b85f6d1b9699a06a5
---

Certify re-review of `solutions/prop-notions-coincide.md` against `prop:notions-coincide`.
Fresh context; I did not write or direct the dossier and did not write either earlier review.

## Findings

*Re-review of `research/reviews/2026-10-20-prop-notions-coincide-rereview.md`.*

**Versions compared.** Baseline: commit `34adda0`. In an isolated `git worktree` of it,
`check.py --fingerprint solutions/prop-notions-coincide.md` gives exactly the fingerprints
recorded by the earlier re-review (dossier `36e0c1ff…`, `prop:notions-coincide` `75847c27…`,
`def:critical-point` `2b3f99b4…`). Baseline verified. Current: the working-tree dossier
(`1f11bb8d…`); both statements unchanged (`check.py --impact`).

**The changes.** Two hunks, applying Corrections 1 and 2 of
`2026-10-20-prop-notions-coincide.md` (repeated by the earlier re-review).

1. Line 58, citation list: "the definition of $\gamma_{\mathrm{mon}}$ in §2.2" → "Definition 2.3
   (§2.1)", the location the first report checked against the author's version of
   Santambrogio (2015). Mathematics unchanged.
2. Proof of the geodesic lemma, *Cyclical monotonicity* (lines 380–381): a parenthesis is added,
   "(in the orientation of Villani's Definition 5.1, $\sum_i c(x_i,y_i) \le \sum_i
   c(x_i,y_{i+1})$, by reversing the order of the points)". This adds a claim to a step, hence
   this re-review.

**Check of change 2.** The proof establishes, for every finite family $x_1,\dots,x_n \in S$
with $y_i = w(x_i)$ and cyclic indices, $\sum_i c(x_{i+1},y_i) \ge \sum_i c(x_i,y_i)$. Apply it
to the reversed family $x'_i = x_{n+1-i}$, $y'_i = y_{n+1-i}$, also in $\Gamma$: with
$j = n - i$ (cyclically), $c(x'_{i+1},y'_i) = c(x_j,y_{j+1})$ and $c(x'_i,y'_i) = c(x_{j+1},
y_{j+1})$, so $\sum_j c(x_j,y_{j+1}) \ge \sum_j c(x_j,y_j)$ — Villani's Definition 5.1, as the
first report (which checked Def. 5.1 against the Saint-Flour draft) said. The added sentence is
true and closes the orientation gap the first report noted as harmless; the subsequent
*Optimality* step (Villani Thm 5.10(ii), (b)⇒(a)) now receives exactly its hypothesis. Nothing
else uses the sentence.

**Conclusions retained.** Every other line is identical to the version certified by the
earlier re-review, whose conclusions (and, through it, the first report's step-level
conclusions) stand: statement agreement with the atomless item 2 and item 1,
`lem:sol-nc-version`, `lem:sol-nc-upper`, `lem:sol-nc-geodesic` apart from the line examined
above, `lem:sol-nc-bathtub`, `lem:sol-nc-1d`, `lem:sol-nc-plan`, `lem:sol-nc-atoms`, the main
proof, hypotheses, dependencies and audit tests. The argument's structure is unchanged; a full
review is not needed.

**Build.** `uv run scripts/check.py --fast` reports no MyST error for the dossier.

## Corrections

None blocking. The earlier re-review's non-blocking Correction 1 (lines 146–147 and 586–587
still derive item 2 via "an absolutely continuous measure has no atom") is not addressed by
this edit and still applies.

## Exclusions

Everything the earlier reports excluded: `prop:critical-sphere`, `prop:critical-segments`,
critical points with atoms in general, existence of the right derivatives for measures with
atoms, and the manuscript prose of `sec:setting`. The AGS theorem numbers remain confirmed only
indirectly, as recorded before; Santambrogio and Villani were not re-checked here.
