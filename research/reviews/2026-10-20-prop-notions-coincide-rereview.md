---
verdict: pass
authors:
  - researcher, claude-opus-5-5, 2026-10-20
reviewer: reviewer, claude-opus-5-5, 2026-10-20
fingerprints:
  solutions/prop-notions-coincide.md: 36e0c1ff8b6c6a3f42d53b704eb38f8de8c3ea1577b9e3f4c5ab8f6a145f4cb2
  prop:notions-coincide: 75847c27e7b0052fc43c8abf198988644a0b57da282b0226d71e368cbd3caf2d
  def:critical-point: 2b3f99b415e32bcde26bf522b879305fe3edffd9318cf15b85f6d1b9699a06a5
---

Certify re-review of `solutions/prop-notions-coincide.md` against the changed statement
`prop:notions-coincide`. Fresh context: I did not write or direct the dossier and did not
write the earlier review.

## Findings

*Re-review of `research/reviews/2026-10-20-prop-notions-coincide.md`.*

**Versions compared.** The baseline is the committed `modules/01-setting.md` (HEAD
`106a70f`) together with the current, untracked dossier. In an isolated `git worktree` of
HEAD, `check.py --fingerprint solutions/prop-notions-coincide.md` gives exactly the three
fingerprints recorded by the earlier report (dossier `36e0c1ff…`, `prop:notions-coincide`
`0e3513d9…`, `def:critical-point` `2b3f99b4…`). The baseline is verified. In the current tree
the dossier and `def:critical-point` are unchanged; only `prop:notions-coincide` changed
(`0e3513d9…` → `75847c27…`).

**The change.** `git diff -- modules/01-setting.md` has one hunk, in item 2 of
`prop:notions-coincide`: "If $\mu$ is absolutely continuous, the three notions … coincide"
became "If $\mu$ has no atom, the three notions … coincide". Item 1, the preamble
"Let $\mu,\rho \in \Ptwo{d}$" and the definitions are unchanged.

**Statement agreement for the new item 2.** Quantifiers: for all $\mu,\rho \in \Ptwo{d}$
(and every $d \ge 1$) with $\mu$ atomless, critical ⇔ Lagrangian critical ⇔ Wasserstein
critical, as defined in `def:critical-point`. `thm:sol-nc-main` has the same preamble
($d \ge 1$, $\mu,\rho \in \Ptwo{d}$, no hypothesis on $\rho$ or the supports), and:

- Lagrangian ⇒ critical and Wasserstein ⇒ critical: part (a), for every $\mu$, so in
  particular for atomless $\mu$.
- critical ⇒ Lagrangian: part (b) with $\gamma = (\Id,\Id+\xi)_\#\mu$, for every
  $\xi \in L^2(\mu;\R^d)$; the right derivative exists and equals
  $\tfrac2d\inner{v_\mu}{\xi} = 0$. Existence and vanishing, as the definition requires.
- critical ⇒ Wasserstein: part (b) along every constant-speed geodesic issued from $\mu$,
  represented by an optimal plan $\gamma$ with first marginal $\mu$ and
  $\int\abs{y}^2\dd\gamma = M_2(\mu_1) < \infty$.

The theorem's last sentence states the conclusion verbatim: "for a measure $\mu$ with no
atom … the three notions of critical point of `def:critical-point` coincide". The only
hypothesis of (b) is "$\mu$ has no atom", the manuscript's new hypothesis, read in the
same sense (no $x$ with $\mu(\{x\}) > 0$; `lem:sol-nc-atoms`, first line of its proof).
The dossier therefore proves the new item 2 exactly as quantified, not only a weaker or
stronger form of it; item 1 is unchanged and still follows from (a).

**No reliance on absolute continuity.** I traced every use of the hypothesis in (b): the
proof of the theorem, part (b), uses only "$\mu$ has no atom" to apply `lem:sol-nc-atoms`
(atomless $\mu$ ⇒ $\mu_\theta$ atomless for σ-a.e. θ), which feeds `lem:sol-nc-plan`, whose
hypothesis is exactly that, and through it `lem:sol-nc-1d` (atomless law of $U$) and
`lem:sol-nc-version`, item 3 ($g(\theta,\cdot) = T_\theta$ when $\mu_\theta$ is atomless).
The geodesic representation (AGS Thm 7.2.2, statement verified in the earlier report via
Villani's displacement-interpolation corollary) holds for every $\mu \in \Ptwo{d}$; no
Brenier map or density is invoked. A search of the dossier for "absolute"/"density" finds
absolute continuity only in the overview, in `rem:sol-nc-singular`, and in the two
sentences that derive the old item 2 from (b) (lines 146–147 and 586–587, "an absolutely
continuous measure has no atom"). That sentence is now a redundant extra step, not a gap:
the new item 2 is the theorem's own conclusion.

**Conclusions retained.** The dossier is byte-for-byte the version certified (same
fingerprint), and `def:critical-point` is unchanged, so every step-level conclusion of the
earlier report stands unaffected: `lem:sol-nc-version`, `lem:sol-nc-upper`,
`lem:sol-nc-geodesic`, `lem:sol-nc-bathtub`, `lem:sol-nc-1d`, `lem:sol-nc-plan`,
`lem:sol-nc-atoms`, the main proof, the remarks, the citations (with the same caveat that
the printed AGS was unavailable and the theorem numbers 5.3.1 and 7.2.2 are confirmed only
indirectly), dependencies (`depends_on: [def:critical-point]`; no `bounded_by` on this
node), and the audit tests of the brief. The earlier report already recorded that the proof
uses only atomlessness for (b); the change brings the manuscript to that sharper form and
does not alter any step's input. The argument's structure does not change, so a full review
is not needed.

**Hypotheses.** Used: $\mu,\rho \in \Ptwo{d}$; for item 2, $\mu$ atomless. None used and
unstated; none stated and unused for the new statement.

**Build.** `uv run scripts/check.py --fast` reports no FAIL for the dossier.

## Corrections

Non-blocking, editorial; a fix would go through an editorial note.

1. `solutions/prop-notions-coincide.md:146-147` and `:586-587`: the derivation of the
   manuscript's second item via "an absolutely continuous measure has no atom" refers to
   the superseded statement; it may now read that (b) with (a) gives the second item
   directly. (Lines 109 and 142, "replaces absolute continuity" and "in particular for an
   absolutely continuous one", are still accurate.)
2. The two corrections of the earlier report (Definition 2.3 in §2.1 of Santambrogio;
   reversing the family for Villani's form of c-cyclical monotonicity) still apply.

## Exclusions

Not certified here: the manuscript prose around the proposition, in particular the
"Idea of the proof" of `sec:setting` (`modules/01-setting.md:98-99`), which still says
"when $\mu$ is absolutely continuous, every geodesic issued from $\mu$ is of that form, by
Brenier's theorem" and no longer matches the atomless statement — a `sync`-lens matter for
the orchestrator; the changes to `research/program/brief.md` and `ledger.yaml` in the
working tree; and everything the earlier report excluded (`prop:critical-sphere`,
`prop:critical-segments`, critical points with atoms in general, existence of the right
derivatives for measures with atoms).
