---
verdict: pass
authors:
  - researcher, claude-opus-5-5, 2026-10-20
reviewer: reviewer, claude-opus-5-5, 2026-10-20
fingerprints:
  solutions/prop-critical-sphere.md: e2f237554d7b944111ef73f29664984e6c96d6a353592c4c5170f355d9d9fade
  prop:critical-sphere: b5c9936d621e0f9ba0839fd69b9be0f19f4f7c59bf7621aec5d8d8e73855aafa
  def:critical-point: 2b3f99b415e32bcde26bf522b879305fe3edffd9318cf15b85f6d1b9699a06a5
  prop:notions-coincide: 75847c27e7b0052fc43c8abf198988644a0b57da282b0226d71e368cbd3caf2d
---

# Re-review of `solutions/prop-critical-sphere.md` (stale wording, closing sentence)

Fresh context. I wrote neither the dossier nor any of its reviews. Lens `certify`, re-review.

## Findings

*Re-review of `research/reviews/2026-10-20-prop-critical-sphere-rereview2.md`.*

**Versions compared.** Baseline: HEAD (`4b57130`; the dossier last changed in `4aa38f1`), in an
isolated `git worktree`: the dossier fingerprints as `733dac6c…`, and `prop:critical-sphere`,
`def:critical-point`, `prop:notions-coincide` as `b5c9936d…`, `2b3f99b4…`, `75847c27…` — the
values the report records (no later editorial note amends it). `check.py --diff` also reports
the baseline verified. Current: the working-tree dossier (`e2f23755…`); the three statements
unchanged (`check.py --impact`).

**The changes** (`check.py --diff`). Four hunks, applying the report's Corrections 1 and 2.

1. Overview, first sentence: a duplicated "it is given by a formula" removed.
2. Overview, step 4: the uniqueness is now attributed to the "if and only if" of step 3, and
   item 1 of `prop:notions-coincide` is said to exclude the other radii for the Lagrangian and
   Wasserstein notions. Both true: step 3 / item 3 gives $v_{\mu_r} = 0$ iff $r = r_*$, which is
   the uniqueness for a critical point (`def:critical-point`, item 1); item 1 of
   `prop:notions-coincide` in contrapositive excludes the other two notions for $r \ne r_*$.
3. After the theorem, "together are" → "together give": the items imply the proposition.
4. Closing sentence of the proof of `thm:sol-cs-main` (l. 348): "Since $r_* > 0$" → "Since
   $0 < r_* < \sqrt d$". A step of proof, hence this re-review.

**Check of change 4** against the current `prop:critical-sphere`
(modules/03-singular-critical-points.md:29–33; $d \ge 2$, $\rho = N(0,I_d)$, as in the theorem):
"exactly one $r_* > 0$" with $\mu_{r_*}$ critical — item 1 ($r_* > 0$) and item 3 (critical iff
$r = r_*$, over all $r > 0$); "also a Lagrangian and a Wasserstein critical point" — item 3;
"$r_* < \sqrt d$" — item 1, now named in the premise; "$r_* = 3/\sqrt\pi$ when $d = 3$" —
item 4. Every premise is a proved item, every clause of the statement is supplied; the
inference is correct and closes the gap noted (as harmless) in the previous report.

**Conclusions retained.** The theorem, `lem:sol-cs-projection`, `lem:sol-cs-constant`,
`lem:sol-cs-field`, `lem:sol-cs-d3`, the proofs of items 1–4, the dependencies and the remarks
are identical to the certified version and do not depend on the changed sentences; the earlier
certifications' conclusions stand. The structure is unchanged; a full review is not needed.

**Build.** `uv run scripts/check.py --fast` reports no error for the dossier.

## Corrections

None.

## Exclusions

As in the earlier reports: unchanged proof steps were retained, not re-derived; manuscript
prose outside the `prf:` directives is not covered.

## Conclusion

`solutions/prop-critical-sphere.md` (`e2f23755…`) proves the current `prop:critical-sphere`:
**pass**.
