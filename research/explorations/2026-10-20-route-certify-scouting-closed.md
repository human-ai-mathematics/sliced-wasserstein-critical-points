---
# No run, no candidate: the certification of the scouting arguments, and the route closed.
---

# The scouting arguments certified; route ap:certify-scouting closed

## Question examined

Route `ap:certify-scouting`: turn the arguments of the 17 October 2026 scouting into
dossiers and certify each by a fresh reviewer, so that later routes can cite them. Also
settle the two side remarks of the scouting status file (the critical sphere of Díaz
Martín–Murphy, the λ-convexity remark on Cozzi–Santambrogio) and check novelty before a
mathematician is contacted.

## What we learned

- *certified* (agent reviews, 20 October 2026; no human acceptance yet) —
  `prop:notions-coincide`, `thm:gaussian-target`, `thm:radial-d3`, `thm:radial-disc-d2`,
  `prop:critical-sphere`. Each dossier proves a form at least as strong as the manuscript
  statement; the review reports are under `research/reviews/2026-10-20-*`. Item 2 of
  `prop:notions-coincide` was sharpened to "µ has no atom", the form its dossier proves, so
  that `prop:critical-sphere` (a singular, atomless measure) can rest on it; a re-review
  restored its certification.
- *observed* — the certification cycle worked as intended: one `revise` (the sphere dossier
  cited statements inside another dossier rather than a certified node), repaired and passed
  by a full re-review; reviewers' citation corrections were carried by an editorial note or
  short re-reviews against the committed baseline.
- *established* — the scouting remark "λ > 0 is excluded" constrains only the bound of
  Cozzi–Santambrogio's method, not the convexity of ½SW₂²(·, ν); no node
  (`2026-10-20-cs26-convexity-remark.md`, which also records `cand:no-positive-convexity-linf`).
- *observed* (literature) — `thm:gaussian-target` and `thm:radial-d3` were not found in the
  literature; `thm:radial-disc-d2` and `prop:notions-coincide` extend known results; nothing
  after 17 October bears on `conj:sw-critical` (`2026-10-20-novelty-check.md`).

## What resists

Nothing on this route. The certifications are agent reviews; human acceptance, and a Google
Scholar / MathSciNet pass on novelty, are outside what agents can supply. `conj:sw-critical`
is untouched: the remaining obstacles are those of the other routes (`cand:annulus-d2`,
`cand:odd-d-sign-changes`, `cand:score-gluing-gaussian`, `cand:balayage-singular-layer`).

## Proposed next step

Route closed: its objective is accomplished. A named human (first the Gaussian dossier) may
accept a dossier through `accepted_by`. The search continues on `ap:radial-annulus-d2`, the
smallest configuration outside every proved case.
