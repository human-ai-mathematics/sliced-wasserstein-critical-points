---
verdict: pass
authors:
  - researcher, claude-opus-5-5, 2026-10-20
reviewer: reviewer, claude-opus-5-5, 2026-10-20
fingerprints:
  solutions/prop-notions-coincide.md: 6a9015d76f5f1f3022d26fd52ebba743a32a723e87b9829a85434b5b361e26d3
  prop:notions-coincide: 75847c27e7b0052fc43c8abf198988644a0b57da282b0226d71e368cbd3caf2d
  def:critical-point: 2b3f99b415e32bcde26bf522b879305fe3edffd9318cf15b85f6d1b9699a06a5
---

# Re-review of `solutions/prop-notions-coincide.md` (stale wording)

Fresh context. I wrote neither the dossier nor any of its reviews. Lens `certify`, re-review.

## Findings

*Re-review of `research/reviews/2026-10-20-prop-notions-coincide-rereview2.md`*, as carried
over by `research/reviews/2026-10-20-editorial-wording.md` (dossier `1f11bb8d…` → `d5f67fe4…`).

**Versions compared.** Baseline: HEAD (`4b57130`), in an isolated `git worktree`: the dossier
fingerprints as `d5f67fe4…`, `prop:notions-coincide` as `75847c27…`, `def:critical-point` as
`2b3f99b4…`, the certified values; `check.py --diff` also reports the baseline verified. Current:
the working-tree dossier (`6a9015d7…`); both statements unchanged (`check.py --impact`).

**The changes** (`check.py --diff`). Five hunks: the Overview (l. 14–17), the sentence after
the step list (l. 47), the *Refined statement* preamble (l. 108–110), the paragraph after the
theorem (l. 146–148), the paragraph *The manuscript statement* closing the proof of
`thm:sol-nc-main` (l. 587–588), and the bullet *The sphere and the segments* of
`rem:sol-nc-singular`. They address the non-blocking Correction 1 of the two earlier
re-reviews (item 2 was derived through "an absolutely continuous measure has no atom").

**Check against the current statement** (modules/01-setting.md:74–81): for $\mu,\rho \in
\Ptwo{d}$, (1) Lagrangian or Wasserstein critical ⇒ critical; (2) if $\mu$ has no atom, the
three notions coincide.

- *Closing proof paragraph* (the changed step). "Its first item is (a)": part (a) of
  `thm:sol-nc-main` concludes, for every $\mu,\rho \in \Ptwo{d}$, that a Lagrangian or
  Wasserstein critical point has $v_\mu = 0$ $\mu$-a.e. — item 1 verbatim. "Its second, for
  $\mu$ with no atom, is (a) with (b)": under exactly that hypothesis, (b) gives critical ⇒
  Lagrangian and Wasserstein, and (a) the converses, so the three coincide — item 2, same
  hypothesis, no detour through absolute continuity. Correct and complete.
- *Paragraph after the theorem, Overview, preamble.* Same derivation in prose; "beyond the
  statement, the theorem gives the derivative formulas" is true ((b) and the `limsup` of (a)).
  "Nothing is assumed on $\mu$ beyond the absence of atoms" is true of the theorem (part (a)
  assumes nothing). No claim added.
- *Remark bullet.* "the sphere of `prop:critical-sphere` is critical in all three senses, as
  stated there" matches the current modules/03-singular-critical-points.md:29–33. It is a
  remark outside the proof.

**Conclusions retained.** The theorem `thm:sol-nc-main`, every lemma and every step of the
proofs of (a) and (b) are identical to the certified version; the earlier reports' conclusions
(statement agreement, `lem:sol-nc-version`, `-upper`, `-geodesic`, `-bathtub`, `-1d`, `-plan`,
`-atoms`, the proofs of (a) and (b), hypotheses, dependencies, citations) stand, since none
depends on the reworded sentences. The structure is unchanged; a full review is not needed.

**Build.** `uv run scripts/check.py --fast` reports no error for the dossier.

## Corrections

None.

## Exclusions

Those of the earlier reports: `prop:critical-sphere` and `prop:critical-segments` (only their
statements are used, in a remark), critical points with atoms in general, the manuscript prose
of `sec:setting`. Citations were not re-checked.

## Conclusion

`solutions/prop-notions-coincide.md` (`6a9015d7…`) proves the current `prop:notions-coincide`:
**pass**.
