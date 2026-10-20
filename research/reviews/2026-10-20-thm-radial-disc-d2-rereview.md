---
verdict: pass
authors:
  - researcher, claude-opus-5-5, 2026-10-20
reviewer: reviewer, claude-opus-5-5, 2026-10-20
fingerprints:
  solutions/thm-radial-disc-d2.md: dde77b5e56f01a7aeb8b1cd1f6e8fc51d1059bd93a245fef6d9c53d22867bcb4
  thm:radial-disc-d2: 1048aba01cdddde1e4f9b2d1041342da625f5fe41912c599c6b38b2a653d1804
  def:critical-point: 2b3f99b415e32bcde26bf522b879305fe3edffd9318cf15b85f6d1b9699a06a5
---

Certify re-review of `solutions/thm-radial-disc-d2.md` against `thm:radial-disc-d2`. Fresh
context; I did not write or direct the dossier and did not write the earlier review.

## Findings

*Re-review of `research/reviews/2026-10-20-thm-radial-disc-d2.md`.*

**Versions compared.** Baseline: commit `34adda0` (the commit that added the earlier report).
In an isolated `git worktree` of it, `check.py --fingerprint solutions/thm-radial-disc-d2.md`
gives exactly the recorded fingerprints (dossier `457f3a0e…`, `thm:radial-disc-d2` `1048aba0…`,
`def:critical-point` `2b3f99b4…`). Baseline verified. Current: the working-tree dossier
(`dde77b5e…`); both statements unchanged (`check.py --impact` names no changed statement).

**The change.** One hunk, `lem:sol-rd2-continuous`, proof part 2 (line 244): "for each $\theta$
its section has $\mu$-measure $\mu_1(\{s \in (-R,R) : g(\theta,s) \ne T(s)\}) = 0$" became "has
$\mu$-measure at most $\mu_1(\ldots) = 0$". This is the earlier report's non-blocking
observation 1.

**Check.** Write $A_\theta = \{s \in (-R,R) : g(\theta,s) \ne T(s)\}$. The θ-section of $N$ is
$\{x : \abs{x} < R,\ \inner{x}{\theta} \in A'_\theta\}$ with $A'_\theta = \{s : g(\theta,s) \ne
T(s)\}$; since $\abs{x} < R$ forces $\abs{\inner{x}{\theta}} < R$, it is contained in
$\{x : \inner{x}{\theta} \in A_\theta\}$, whose $\mu$-measure is $\mu_\theta(A_\theta) =
\mu_1(A_\theta)$ (radial symmetry, `lem:sol-rd2-projection`). So "at most" is correct, whereas
the former equality can fail when $\mu$ charges the circle $\abs{x} = R$ (allowed). The bound is
$0$ since $g(\theta,\cdot) = T$ $\mu_1$-a.e.; the following Tonelli step uses only that each
section is null, so it, the conclusion $v_\mu = v$ $\mu$-a.e. on $B(0,R)$, and part 3 are
unaffected. The edit replaces a false intermediate equality by the true inequality the step
needs.

**Conclusions retained.** Every other line of the dossier is identical to the certified
version and no other step uses the changed relation, so the earlier report's conclusions stand:
statement agreement (the dossier theorem is strictly stronger than `thm:radial-disc-d2`),
normalization constants, `lem:sol-rd2-projection`, `lem:sol-rd2-monotone`, parts 1 and 3 of
`lem:sol-rd2-continuous`, `lem:sol-rd2-reduction`, `lem:sol-rd2-abel`, `prop:sol-rd2-local`,
the main proof, hypotheses, audit tests, dependencies and fences. The argument's structure is
unchanged; a full review is not needed.

**Build.** `uv run scripts/check.py --fast` reports no MyST error for the dossier.

## Corrections

None. The earlier report's non-blocking observation 2 (`rem:sol-rd2-circle` citing the open
`prop:critical-sphere` as established) is not addressed by this edit and still applies; it is
outside the proof.

## Exclusions

Everything the earlier report excluded: `rem:sol-rd2-atom`, the claims of
`rem:sol-rd2-annulus` beyond the Abel identity (`cand:annulus-d2`), the criticality of the
circle (`prop:critical-sphere`), the comparison claims of `rem:sol-rd2-bonnotte` beyond the
logical overlap, and `conj:sw-critical`.
