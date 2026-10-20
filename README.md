# Critical points of the sliced Wasserstein distance

Let $\rho$ be an absolutely continuous probability measure on $\mathbb R^d$, $d \ge 2$. Is every
absolutely continuous critical point of $\mu \mapsto \tfrac12 \mathrm{SW}_2^2(\mu, \rho)$ equal to
$\rho$? This is the open question of Vauthier, Korba and Mérigot
([arXiv:2502.06525](https://arxiv.org/abs/2502.06525), ICML 2025, §7), stated here as
`conj:sw-critical`. Singular critical points other than $\rho$ exist (segments, spheres). The
statement is established in the literature when $\mu$ and $\rho$ have positive densities on a
common ball, and for the standard Gaussian target under finite entropy. This repository
proves it for every Gaussian target (no entropy hypothesis), for radial measures in dimension
three and for radial measures whose support is a full disc or the whole plane in dimension
two, and proves that the usual notions of critical point coincide for atomless measures and that the critical sphere
of a standard Gaussian target has a unique radius. These five proofs are certified by **agent
reviews** (20 October 2026), not yet by a human. A literature search (arXiv and the closest
papers in full text) found earlier results covering part of four of them, cited in the
manuscript, and is not a claim of novelty. The general question stays open. The ledger
[`research/program/ledger.yaml`](research/program/ledger.yaml), not this file, is the source
of truth for what is proved.

This repository is a MyST Markdown manuscript together with the record of a **sustained
conjecture search** on that question. It was instantiated from
[conjecture-search-template v0.6.0](https://github.com/human-ai-mathematics/conjecture-search-template/releases/tag/v0.6.0);
the scouting that led to it is in `../ensae-conjecture-scouting/verification/13-korba-sw/`.
Why the template exists is in [`PURPOSE.md`](PURPOSE.md). The rules are in
[`SPECIFICATION.md`](SPECIFICATION.md). Start every session that edits the repository by
reading it.

## Layout

| path | holds |
|---|---|
| [`modules/`](modules/) | the manuscript, the text a reader reads: every claim as a labelled `prf:` directive, in prose written for a mathematician |
| [`research/program/`](research/program/) | the ledger; the brief once a search runs, the portfolio of routes from the first route |
| [`research/explorations/`](research/explorations/) | dated checkpoints and candidate statements |
| [`research/reviews/`](research/reviews/) | independent proof reviews |
| [`research/runs/`](research/runs/) | computation scripts and their output |
| [`research/lib/`](research/lib/) | shared computation code (`swcrit`: the 2D solver of the barycentric field), its lock and unit tests |
| [`solutions/`](solutions/) | standalone proof and refutation dossiers |
| [`.claude/agents/`](.claude/agents/), [`.codex/agents/`](.codex/agents/) | the three roles: `researcher`, `reviewer` and `writer`, for Claude Code and for Codex |
| [`templates/`](templates/) | an empty copy of each file genre |
| [`example/`](example/README.md) | one complete worked search, a fixture to copy from |

## Setup and verify

Needs [uv](https://docs.astral.sh/uv/), which provisions Python and PyYAML from
`pyproject.toml`, and Node.js 18+ for MyST (pinned in `package.json`):

```bash
npm ci
./scripts/check.sh               # the checker, the worked example, the unit tests
uv run scripts/check.py         # full check; 0 errors required before any status change
uv run scripts/check.py --fast  # research state only, no MyST build
uv run scripts/check.py --impact # compact scope for grouped re-reviews; same validation
uv run scripts/check.py --diff   # the same, with each change's diff for an editorial note
uv run scripts/check.py --statements   # before and after a writer's pass: must not change
uv run scripts/check.py --drafts       # the draft dossiers, never published
npx myst start                   # read the manuscript and the proofs in a browser
uv run --project research/lib python -m unittest discover -s research/lib/tests  # the solver
```

Agents run the checker and MyST many times per session. Approve those commands once and
for good (`uv run scripts/check.py` and `node_modules/.bin/myst`): in Claude Code, as
`allow` rules in `.claude/settings.json`; in Codex, by accepting the prefix rule offered
on the first escalation. Each approval asked again costs a turn, and in Codex a call to
its reviewing model. See *Running agents* below for practical guidance; the independence
requirement is in *Review* in `SPECIFICATION.md`.

The first check in a fresh clone downloads MyST's site theme into `_build/`. A green check
establishes structure only. Each statement shows its status, read from the ledger by
[`scripts/status.mjs`](scripts/status.mjs). The `pages` workflow publishes the manuscript
and the certified dossiers to GitHub Pages when dispatched by hand, after a person has
read them.

## Running agents

Prefer the client's agent tools so assignments, results and progress remain visible.
Load the corresponding instructions from `.claude/agents/` or `.codex/agents/` for each
role. In Claude Code, use the Agent tool's role selection when available. In Codex,
use `spawn_agent` with `fork_turns: "none"` for an independent reviewer and ensure its
assignment loads the reviewer instructions; use the role-selection mechanism your client
actually exposes rather than assuming an `agent_type` argument exists.

A reviewer must not inherit the conversation that authored or directed the proof. Check
that the chosen launch mechanism supplies that fresh context. Other agents can receive
context useful to their tasks. Prefer these managed tools over background shell sessions.

Use completion notifications or blocking waits (such as `wait_agent`) rather than repeated
status polling. Choose a timeout within the client's limits that still allows progress
updates and responses to the user; no fixed wait duration is part of the repository
contract. Start a new session when it helps keep context focused, not automatically after
each task. The recommended scientific workflow is in *Workflow* in `SPECIFICATION.md`.

## Licence

The text (manuscript, proofs and research records) is under
[CC BY 4.0](LICENSE-CC-BY-4.0.txt), the code under MIT; [`LICENSE`](LICENSE) says which is which.
