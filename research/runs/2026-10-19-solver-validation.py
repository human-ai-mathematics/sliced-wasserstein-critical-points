# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy>=2", "scipy>=1.13", "swcrit"]
#
# [tool.uv.sources]
# swcrit = { path = "../lib" }
# ///
"""Validate the 2D solver of research/lib (swcrit.sw2d) against known critical points, and
evaluate the critical radius of the sphere of prop:critical-sphere in dimension three.

    uv run research/runs/2026-10-19-solver-validation.py

Reproduces, at a smaller scale, the validation of the scouting folder
(ensae-conjecture-scouting/verification/13-korba-sw/voie-b/01-validation.py, 17 October 2026):
(a) the field vanishes when mu = rho; (b) it vanishes on the segments of
prop:critical-segments, and not on a dilated segment; (c) it does not vanish on a smaller
disc, at every resolution. Then (d) the radial condition of the three-dimensional sphere for
rho = N(0, I_3), whose root the overview computes by hand as 3/sqrt(pi).
J is int |v_mu|^2 dmu divided by the second moment of rho. Nothing it prints certifies anything.
"""
import json
import platform
import random
import subprocess
from importlib.metadata import version
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import ndtri

from swcrit.sw2d import Grid, disk, normalize, second_moment, v_grid, v_points

SEED = 0                    # every computation below is deterministic
PACKAGES: list[str] = ["numpy", "scipy", "swcrit"]
OUT = Path(__file__).with_suffix(".jsonl")
GRID_N = [80, 160]
DIRECTIONS = [64, 256, 1024]
PARTICLES = 10000


def provenance(**params) -> dict:
    """The seed, the parameters, the commit (dirty if uncommitted) and the versions."""
    def git(*args: str) -> str:
        return subprocess.run(["git", *args], capture_output=True, text=True,
                              cwd=OUT.parent).stdout.strip()
    return {"provenance": {"seed": SEED, **params,
                           "git_commit": git("rev-parse", "HEAD") or None,
                           "dirty": bool(git("status", "--porcelain")),
                           "python": platform.python_version(),
                           "versions": {name: version(name) for name in PACKAGES}}}


def j_grid(G, mu, rho, L):
    idx, v = v_grid(G, mu, rho, L)
    return float((mu[idx] * (v ** 2).sum(1)).sum() / second_moment(G, rho))


def j_points(X, w, rhoQ, L, m2):
    v = v_points(X, w, rhoQ, L)
    return float((w * (v ** 2).sum(1)).sum() / m2)


def run(rng: random.Random) -> list[dict]:
    records = []
    for n in GRID_N:
        G = Grid(2.0, n)
        cases = {
            "disc": normalize(disk(G, (0, 0), 1.5)),
            "two-discs": normalize(disk(G, (-1, 0), .7) + disk(G, (1, .3), .6)),
            "square-frame": normalize(((np.abs(G.P).max(1) < 1.6)
                                       & (np.abs(G.P).max(1) > .8)).astype(float)),
        }
        for name, m in cases.items():
            records.append({"check": "a: mu = rho", "case": name, "n": n, "L": 64,
                            "J": j_grid(G, m, m, 64)})
        mu, rho = normalize(disk(G, (0, 0), .8)), normalize(disk(G, (0, 0), 1.5))
        records.append({"check": "c: smaller disc", "n": n, "L": 128,
                        "J": j_grid(G, mu, rho, 128)})

    s = (np.arange(PARTICLES) + .5) / PARTICLES
    w = np.full(PARTICLES, 1 / PARTICLES)
    for L in DIRECTIONS:
        for factor in [1.0, 1.2]:
            X = np.c_[factor * (8 / np.pi) * (s - .5), 0 * s]
            records.append({"check": "b: sliced-uniform segment", "bears_on": "prop:critical-segments",
                            "dilation": factor, "L": L, "N": PARTICLES,
                            "J": j_points(X, w, lambda l: (lambda u: 2 * u - 1), L, 0.5)})
        X = np.c_[(4 / np.pi) * ndtri(s), 0 * s]
        records.append({"check": "b: Gaussian segment", "bears_on": "prop:critical-segments",
                        "L": L, "N": PARTICLES, "J": j_points(X, w, lambda l: ndtri, L, 2.0)})

    # d = 3, mu uniform on r S^2: mu_theta = U[-r, r], T(u) = Phi^{-1}((1 + u/r)/2), and
    # v_mu = 0 on the sphere iff int_0^r (T(u) - u) u du = 0.
    def G3(r):
        return quad(lambda u: (ndtri((1 + u / r) / 2) - u) * u, 0, r, limit=200)[0]
    r_star = brentq(G3, 0.5, 3.0, xtol=1e-14)
    records.append({"check": "d: critical sphere, d = 3", "bears_on": "prop:critical-sphere",
                    "r_star": r_star, "three_over_sqrt_pi": 3 / np.sqrt(np.pi),
                    "difference": r_star - 3 / np.sqrt(np.pi)})
    return records


if __name__ == "__main__":
    records = [provenance(grid_n=GRID_N, directions=DIRECTIONS, particles=PARTICLES),
               *run(random.Random(SEED))]
    OUT.write_text("".join(json.dumps(record) + "\n" for record in records))
    print(OUT.read_text(), end="")
