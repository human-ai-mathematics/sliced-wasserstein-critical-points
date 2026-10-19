"""Unit tests of the 2D solver: the field vanishes at the target, and on the critical
segments of prop:critical-segments; it does not vanish on a non-critical disc."""
import unittest

import numpy as np
from scipy.special import ndtri

from swcrit.sw2d import Grid, disk, normalize, second_moment, v_grid, v_points


def j_points(X, w, rhoQ, L, m2):
    v = v_points(X, w, rhoQ, L)
    return float((w * (v ** 2).sum(1)).sum() / m2)


class TestSolver(unittest.TestCase):
    def test_field_vanishes_at_target(self):
        G = Grid(2.0, 80)
        mu = normalize(disk(G, (0, 0), 1.5))
        idx, v = v_grid(G, mu, mu, 32)
        J = float((mu[idx] * (v ** 2).sum(1)).sum() / second_moment(G, mu))
        self.assertLess(J, 1e-10)

    def test_sliced_uniform_segment_is_critical(self):
        # mu uniform on [-4/pi, 4/pi] x {0}; rho sliced-uniform, Q_theta(u) = 2u - 1.
        N = 4000
        s = (np.arange(N) + 0.5) / N
        w = np.full(N, 1 / N)
        crit = np.c_[(8 / np.pi) * (s - 0.5), 0 * s]
        self.assertLess(j_points(crit, w, lambda l: lambda u: 2 * u - 1, 256, 0.5), 1e-6)
        wide = 1.2 * crit
        self.assertGreater(j_points(wide, w, lambda l: lambda u: 2 * u - 1, 256, 0.5), 1e-3)

    def test_gaussian_segment_is_critical(self):
        # mu = N(0, alpha_2^2) on the first axis, alpha_2 = 4/pi; rho = N(0, I_2).
        N = 4000
        s = (np.arange(N) + 0.5) / N
        w = np.full(N, 1 / N)
        X = np.c_[(4 / np.pi) * ndtri(s), 0 * s]
        self.assertLess(j_points(X, w, lambda l: ndtri, 256, 2.0), 1e-5)

    def test_smaller_disc_is_not_critical(self):
        G = Grid(2.0, 80)
        mu = normalize(disk(G, (0, 0), 0.8))
        rho = normalize(disk(G, (0, 0), 1.5))
        idx, v = v_grid(G, mu, rho, 32)
        J = float((mu[idx] * (v ** 2).sum(1)).sum() / second_moment(G, rho))
        self.assertGreater(J, 1e-2)


if __name__ == "__main__":
    unittest.main()
