---
verdict: pass
authors:
  - researcher, claude-opus-5-5, 2026-10-20
  - orchestrator, claude-opus-5-5, 2026-10-20
reviewer: reviewer, claude-opus-5-5, 2026-10-20
fingerprints:
  solutions/prop-critical-sphere.md: d71be6355e80f54b7428aa6b51b32bcc881a9c543720473a25df83a6500d127d
  prop:critical-sphere: b5c9936d621e0f9ba0839fd69b9be0f19f4f7c59bf7621aec5d8d8e73855aafa
  def:critical-point: 2b3f99b415e32bcde26bf522b879305fe3edffd9318cf15b85f6d1b9699a06a5
  prop:notions-coincide: 75847c27e7b0052fc43c8abf198988644a0b57da282b0226d71e368cbd3caf2d
  solutions/thm-radial-d3.md: 6f0a737fa248491be1e86f068221b62a124df93afbd9090484cfa9b2a5e211e5
  thm:radial-d3: bc84d1ba4a883d56720f080fae800837e066093396646a495cff1333f7c6949f
  solutions/thm-radial-disc-d2.md: 8cd85ab627d2b0d8c872334ac0c9df0e9dddf05d2485ffbd25b3b2ed97f89b9a
  thm:radial-disc-d2: 74efe825ef7c471a39edabd72df536e4ff2d014ec0445d293bac56860d217080
---

# Grouped re-review: three sharpened manuscript statements

Fresh context; I wrote none of the dossiers, statements or earlier reports. Grouped
re-review (lens `certify`) of three statement-only changes.

## Findings

*Re-review of* `research/reviews/2026-10-20-prop-critical-sphere-rereview.md`,
`research/reviews/2026-10-20-thm-radial-d3-rereview2.md` and
`research/reviews/2026-10-20-thm-radial-disc-d2-rereview.md`.

**Versions compared.** Baseline: HEAD (`34459d6`), built in an isolated `git worktree`. There
the statements fingerprint as the reports record: `prop:critical-sphere` `f38d6569…`,
`thm:radial-d3` `61d070fb…`, `thm:radial-disc-d2` `1048aba0…`; `def:critical-point` and
`prop:notions-coincide` are unchanged. Dossiers: `git diff HEAD -- solutions/` is empty.
`solutions/thm-radial-d3.md` (`6f0a737f…`) equals its report's fingerprint directly;
`solutions/prop-critical-sphere.md` (`d71be635…`) and `solutions/thm-radial-disc-d2.md`
(`8cd85ab6…`) equal the `to` values of `research/reviews/2026-10-20-editorial-wording.md`,
whose `from` values are the reports' fingerprints. So the dossiers are the certified ones.
`check.py --impact` and `--diff` name only the three statements as changed. The only change in
the working tree is to `modules/03-singular-critical-points.md` and
`modules/04-special-targets.md`.

**Retained.** The earlier reports certified each dossier's proof of its refined theorem. The
proofs are unchanged, so those conclusions stand. Only statement agreement is examined here.

### prop:critical-sphere ← `thm:sol-cs-main` — agrees

New statement: for $d \ge 2$, $\rho = N(0,I_d)$, there is exactly one $r_* > 0$ with
$\mu_{r_*}$ a critical point; it is also Lagrangian and Wasserstein critical; $r_* < \sqrt d$;
$r_* = 3/\sqrt\pi$ for $d = 3$.

- Existence and uniqueness of $r_* > 0$, in the sense of [](#def:critical-point) item 1: item 1
  gives $0 < r_*$, and item 3 gives "$\mu_r$ is a critical point iff $r = r_*$" for every $r > 0$.
- Lagrangian and Wasserstein criticality of $\mu_{r_*}$: item 3.
- $r_* < \sqrt d$: item 1. $r_* = 3/\sqrt\pi$ for $d = 3$: item 4.

"Exactly one" refers to the first notion. That reading is also consistent with item 3, which
excludes every $r \ne r_*$ for all three notions. Same hypotheses ($d \ge 2$, standard Gaussian).
The theorem implies the statement exactly. Its dependency `prop:notions-coincide` is
unchanged.

### thm:radial-d3 ← `thm:sol-radial-d3` — agrees

New hypotheses: $\rho,\mu \in \Ptwo{3}$ rotation invariant; $\mu(\{0\}) = 0$; the support of
the law of $\abs X$ has no isolated point. Conclusion: critical $\Rightarrow \mu = \rho$. This is
hypothesis (H) of `thm:sol-radial-d3` word for word, with the same conclusion and the same
notion of criticality ($v_\mu = 0$ $\mu$-a.e.). The added clause "both hold when that law has
no atom" is proved in the dossier's *Refined statement* paragraph. Indeed
$\mu(\{0\}) = \mu_{\mathrm{rad}}(\{0\})$, and an isolated point of the support would carry an atom.
It is also restated in the theorem ("In particular this holds when $\mu_{\mathrm{rad}}$ has no
atom").

### thm:radial-disc-d2 ← `thm:sol-rd2-main` — agrees

New statement: $\rho \in \Ptwo{2}$ rotation invariant; $\mu \in \Ptwo{2}$ rotation invariant,
$\mu(\{0\}) = 0$, support a closed disc of positive radius centred at $0$ or $\R^2$; critical
$\Rightarrow \mu = \rho$. The dossier defines "radial" as $SO(2)$ invariance (line 62), and
its support is "$\overline B(0,R)$, $R \in (0,\infty)$, or $\R^2$". This is identical. The
absolute-continuity hypothesis that was removed is not used by the proof (the earlier report
and `thm:sol-rd2-main` already omit it).

### Cross-references in the dossiers that now read stale (non-blocking)

Each dossier still describes the *old* statement as weaker than its theorem. These sentences
say nothing false about the refined theorem or its proof, and the implication to the new
statement is immediate (shown above). They are wording defects only. See Corrections.

## Corrections

Non-blocking. To be made by the researcher and carried over by an editorial note.

1. `solutions/prop-critical-sphere.md:14`, `:63–65`, `:92–93`, `:347–348`. "sharper form",
   "sharpens … it gives uniqueness of the radius … value in dimension three … all three
   notions" and "which asks for some $r_* > 0$ such that $\mu_{r_*}$ is a Wasserstein critical
   point" describe the old statement. Line 347 derives the proposition from $r_* > 0$ and
   Wasserstein criticality alone. Restate it: the proposition is items 1, 3 and 4 (the theorem
   adds the closed-form field, the formula for $r_*$ and $\mu_{r_*} \ne \rho$). Line 36 ("which
   is what [](#prop:critical-sphere) states") should likewise no longer suggest that the
   proposition is the Wasserstein claim only.
2. `solutions/thm-radial-d3.md:14–16` ("slightly sharper form … instead of 'the law of
   $\abs X$ has no atom'"), `:81` ("contains"), `:446` ("This is the sharpening over
   [](#thm:radial-d3)"). The theorem now *is* the manuscript statement. Reword it as
   "proves [](#thm:radial-d3)"; the no-atom paragraph then justifies the statement's final
   clause.
3. `solutions/thm-radial-disc-d2.md:15–16` ("sharper form: absolute continuity of $\mu$ is
   replaced by $\mu(\{0\}) = 0$") and `:102–105` ("This implies … an absolutely continuous
   $\mu$ has $\mu(\{0\}) = 0$ …"). The statement no longer assumes absolute continuity.
   Remaining sharpenings over the statement: none on $\mu$; the local
   [](#prop:sol-rd2-local).

## Exclusions

- The proofs themselves: retained from the three earlier reports and not re-checked.
- Manuscript prose outside the `prf:` directives, which this certification does not cover.
  Three passages now read stale, for the orchestrator:
  - `modules/04-special-targets.md:113–116` repeats the new hypotheses as "the proof gives
    more".
  - `modules/04-special-targets.md:144–145` says "absolute continuity of $\mu$ is replaced by
    $\mu(\{0\}) = 0$", but the statement no longer assumes it.
  - `modules/03-singular-critical-points.md:37` says "It proves more" before reciting
    uniqueness and $r_* < \sqrt d$, which are now in the statement (the closed-form field is
    still extra).
- Other nodes and dossiers.

## Conclusion

- `solutions/prop-critical-sphere.md` proves the new `prop:critical-sphere`: **pass**.
- `solutions/thm-radial-d3.md` proves the new `thm:radial-d3`: **pass**.
- `solutions/thm-radial-disc-d2.md` proves the new `thm:radial-disc-d2`: **pass**.
