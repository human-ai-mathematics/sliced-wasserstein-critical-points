"""Two-dimensional solver for the barycentric field v_mu of F = 1/2 SW_2^2(., rho).

Normalization of def:barycentric-field, with sigma the uniform probability on S^1:

    v_mu(x) = x - 2 * mean_theta [ T_theta(<x,theta>) theta ],  T_theta = Q_{rho_theta} o F_{mu_theta}.

Directions: midpoint rule on the half circle, phi_l = pi (l + 1/2) / L, which is exact for
mean <x,th> th = x/2 as soon as L >= 2.

Two representations of mu:
- a density on a grid: one mass per square cell of side h. The projection of a cell is a
  trapezoidal law (the sum of two uniforms of widths h|cos|, h|sin|); the masses are
  deposited on a fine 1D grid (step h/SUB, linear deposit), then convolved with that kernel;
- weighted particles: F_mu at particle i is the mass strictly before it plus w_i / 2.

Imported from the scouting folder ensae-conjecture-scouting/verification/13-korba-sw/voie-b/
(sw2d.py, 17 October 2026), with the comments translated. Nothing it computes certifies
anything.
"""
import numpy as np

SUB = 4


class Grid:
    def __init__(self, R, n):
        self.R, self.n = R, n
        self.h = 2 * R / n
        c = -R + self.h * (np.arange(n) + 0.5)
        self.X, self.Y = np.meshgrid(c, c, indexing="ij")
        self.P = np.c_[self.X.ravel(), self.Y.ravel()]
        self.dt = self.h / SUB
        Tm = R * np.sqrt(2) + 2 * self.h
        self.K = int(np.ceil(2 * Tm / self.dt)) + 1
        self.t = -Tm + self.dt * np.arange(self.K)        # centres of the 1D bins
        self.edges = np.r_[self.t - self.dt / 2, self.t[-1] + self.dt / 2]


def directions(L):
    phi = np.pi * (np.arange(L) + 0.5) / L
    return phi, np.c_[np.cos(phi), np.sin(phi)]


def _trap_kernel(a, b, dt):
    """Masses of the trapezoidal kernel (widths a, b) on bins of step dt centred at k dt."""
    a, b = max(a, 1e-9 * dt), max(b, 1e-9 * dt)
    m = int(np.ceil((a + b) / 2 / dt)) + 1
    k = np.arange(-m, m + 1)
    e = np.r_[k - 0.5, m + 0.5] * dt
    y = (np.arange(64) + 0.5) / 64 * b - b / 2      # quadrature over the second uniform
    cdf = np.clip((e[:, None] - y[None, :] + a / 2) / a, 0, 1).mean(1)
    return np.diff(cdf)


def proj_cdf_grid(G, mass, theta):
    """CDF of the projection of a grid density, at the edges of the 1D bins (length K+1)."""
    s = G.P @ theta
    u = (s - G.t[0]) / G.dt
    i0 = np.floor(u).astype(int); f = u - i0
    p = np.bincount(i0, mass * (1 - f), G.K) + np.bincount(i0 + 1, mass * f, G.K + 1)[:G.K]
    ker = _trap_kernel(G.h * abs(theta[0]), G.h * abs(theta[1]), G.dt)
    p = np.convolve(p, ker, mode="same")
    return np.r_[0.0, np.cumsum(p)]


def quantile_fn(edges, F):
    Fs = F + 1e-15 * np.arange(len(F))               # strictly increasing (holes in the support)
    return lambda u: np.interp(u, Fs, edges)


def v_grid(G, mu, rho, L, idx=None, rho_q=None):
    """v_mu at the centres of the cells idx (default: supp mu). mu, rho: masses (n*n,)."""
    if idx is None:
        idx = np.flatnonzero(mu > 0)
    phi, D = directions(L)
    X = G.P[idx]
    acc = np.zeros_like(X)
    for l in range(L):
        th = D[l]
        Fm = proj_cdf_grid(G, mu, th)
        u = np.interp(X @ th, G.edges, Fm)
        Q = rho_q(l) if rho_q is not None else quantile_fn(G.edges, proj_cdf_grid(G, rho, th))
        acc += Q(u)[:, None] * th[None, :]
    return idx, X - 2 * acc / L


def v_points(X, w, rhoQ, L):
    """Particles (X, weights w); rhoQ(l) -> the quantile function of rho_theta_l."""
    phi, D = directions(L)
    acc = np.zeros_like(X)
    for l in range(L):
        s = X @ D[l]
        o = np.argsort(s, kind="stable")
        cw = np.cumsum(w[o]); u = np.empty_like(s); u[o] = cw - w[o] / 2
        acc += rhoQ(l)(u)[:, None] * D[l][None, :]
    return X - 2 * acc / L


def rho_quantiles_grid(G, rho, L):
    phi, D = directions(L)
    Qs = [quantile_fn(G.edges, proj_cdf_grid(G, rho, D[l])) for l in range(L)]
    return lambda l: Qs[l]


def sw2_grid(G, mu, rho, L, nu=2000):
    phi, D = directions(L)
    u = (np.arange(nu) + 0.5) / nu
    tot = 0.0
    for l in range(L):
        qm = quantile_fn(G.edges, proj_cdf_grid(G, mu, D[l]))(u)
        qr = quantile_fn(G.edges, proj_cdf_grid(G, rho, D[l]))(u)
        tot += np.mean((qm - qr) ** 2)
    return tot / L


# ---------- test densities ----------
def disk(G, c, r):
    return ((G.P[:, 0] - c[0]) ** 2 + (G.P[:, 1] - c[1]) ** 2 < r * r).astype(float)


def normalize(m):
    return m / m.sum()


def second_moment(G, m):
    c = (m[:, None] * G.P).sum(0)
    return float((m * ((G.P - c) ** 2).sum(1)).sum())
