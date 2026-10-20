---
verdict: pass
authors:
  - researcher, claude-opus-5-5, 2026-10-20
reviewer: reviewer, claude-opus-5-5, 2026-10-20
fingerprints:
  solutions/prop-critical-sphere.md: 733dac6c02cd54471a1e3e86dd5486f9dccde7731189079ae8891871122faace
  prop:critical-sphere: b5c9936d621e0f9ba0839fd69b9be0f19f4f7c59bf7621aec5d8d8e73855aafa
  def:critical-point: 2b3f99b415e32bcde26bf522b879305fe3edffd9318cf15b85f6d1b9699a06a5
  prop:notions-coincide: 75847c27e7b0052fc43c8abf198988644a0b57da282b0226d71e368cbd3caf2d
---

# Re-review of `solutions/prop-critical-sphere.md` (wording and closing derivation)

Fresh context. I wrote neither the dossier nor any of its reviews. Lens `certify`, re-review.

## Findings

*Re-review of* `research/reviews/2026-10-20-sharpened-statements-rereview.md`.

**Baseline.** For this dossier, that report certifies `d71be635…`. The
`to` value of `research/reviews/2026-10-20-editorial-wording.md` is the same, and that note
amends the earlier `2026-10-20-prop-critical-sphere-rereview.md`. The untracked
`2026-10-20-editorial-sharpened-wording.md` does not touch this dossier. HEAD (`e953a1d`),
checked out in an isolated `git worktree`, fingerprints as `d71be635…` for the dossier, and as
`b5c9936d…`, `2b3f99b4…` and `75847c27…` for `prop:critical-sphere`, `def:critical-point` and
`prop:notions-coincide`. All four equal the report's values. Those three statements are
unchanged in the current tree. The baseline is verified.

**Changes** (`git diff HEAD -- solutions/prop-critical-sphere.md`). There are four hunks and
nothing else. No statement, formula, lemma or proof step other than the closing sentence
changed.

1. Overview, first sentence. "in a sharper form" became "as thm:sol-cs-main, which also gives
   the radius by a formula". This is true: `r_* = d A_d` with `A_d` an explicit integral.
2. Overview, step 4. The barycentric condition is now said to become "the Wasserstein one, and
   the Lagrangian one", and item 1 of `prop:notions-coincide` "excludes every other radius,
   which is the uniqueness it asserts". The first half is true (item 2 of
   `prop:notions-coincide`, atomless sphere). The second half misattributes the uniqueness
   (Correction 1). The proposition asserts uniqueness for a *critical point*
   (`def:critical-point` item 1). That uniqueness comes from the "if and only if" of step 3.
   Item 1 of `prop:notions-coincide` excludes other radii only for the Lagrangian and
   Wasserstein notions. This is a roadmap sentence. The proof (l. 327–330) attributes the
   uniqueness correctly, so the defect is not mathematical.
3. *Refined statement* preamble. The theorem adds a formula for the radius, the closed-form
   field of every centred sphere (item 2) and $\mu_{r_*} \ne \rho$ (item 3). All three are true.
   The post-theorem sentence says items 1, 3 and 4 "together are" the proposition. They imply
   it, and they say slightly more (they also give $\mu_{r_*} \ne \rho$ and the exclusion of the
   other two notions for $r \ne r_*$). "$\mu_{r_*}$ is critical in all three senses, and no other
   radius is" is item 3.
4. Closing sentence of the proof of `thm:sol-cs-main` (l. 347–349). It is checked against the
   current `prop:critical-sphere` (modules/03-singular-critical-points.md:29–33):
   - "exactly one $r_* > 0$ with $\mu_{r_*}$ a critical point": item 1 gives $r_* > 0$, and item 3
     gives "critical point iff $r = r_*$" over all $r > 0$, which are all the radii $\mu_r$ is
     defined for;
   - "also a Lagrangian and a Wasserstein critical point": item 3;
   - "$r_* < \sqrt d$": item 1;
   - "$r_* = 3/\sqrt\pi$ when $d = 3$": item 4.

   Hypotheses are the same ($d \ge 2$, $\rho = N(0,I_d)$). The derivation is correct and
   complete. Its "since" clause does not list $r_* < \sqrt d$, but the conclusion invokes item 1,
   which supplies it.

**Retained.** The earlier reports' certification covers the lemmas
(`lem:sol-cs-projection`, `lem:sol-cs-constant`, `lem:sol-cs-field`, `lem:sol-cs-d3`), the
proofs of items 1–4, the dependencies and the remarks. None of these changed, and none depends
on the reworded sentences, so those conclusions stand. The statement agreement established in
the earlier report is the one re-confirmed in item 4 above.

## Corrections

These are non-blocking: wording only, to be made by the researcher and carried over by an
editorial note.

1. `solutions/prop-critical-sphere.md:36–37`. Replace "item 1 of the same statement excludes
   every other radius, which is the uniqueness it asserts" with something like "the uniqueness
   it asserts is the 'if and only if' above, and item 1 of the same statement excludes every
   other radius for the other two notions as well".
2. Optional: `:92`, "together are" → "together give". `:347`, add "$r_* < \sqrt d$" to the
   "since" clause.

## Exclusions

- The unchanged proof steps are retained from the earlier certifications and were not
  re-derived.
- Manuscript prose outside the `prf:` directives is not covered.
- The other dossiers modified in the working tree (`solutions/thm-radial-d3.md`,
  `solutions/thm-radial-disc-d2.md`) and the untracked editorial note are not covered.

## Conclusion

`solutions/prop-critical-sphere.md` (`733dac6c…`) proves the current `prop:critical-sphere`:
**pass**.
