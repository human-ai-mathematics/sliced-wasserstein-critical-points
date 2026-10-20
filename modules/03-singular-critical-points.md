% Singular critical points: why absolute continuity is in the statement. Contents of the
% labelled directives are fixed (orchestrator); prose is the writer's.

(sec:singular)=
# Singular critical points

Without absolute continuity the statement of [](#conj:sw-critical) is false, and the
counterexamples show what any proof must use.

:::{prf:proposition} Critical segments
:label: prop:critical-segments
1. Let $d = 2$ and let $\rho$ be the probability measure on the open unit disc with density
   $x \mapsto \frac{1}{2\pi}(1 - \abs{x}^2)^{-1/2}$, each of whose projections $\rho_\theta$ is
   the uniform probability on $[-1,1]$. The measure $\mu = \frac{\pi}{8}\,\mathcal{H}^1$
   restricted to the segment $[-\frac4\pi, \frac4\pi] \times \{0\}$ is a critical point of
   $\SW_2^2(\cdot,\rho)$.
2. Let $d \ge 2$, $\rho = N(0, I_d)$, and $\alpha_d = d \int_{\Sph{d-1}} \abs{\inner{\theta}{e_1}}
   \dd\sigma(\theta)$. The law $\mu$ of $(Z, 0, \dots, 0)$, with $Z \sim N(0, \alpha_d^2)$, is a
   critical point of $\SW_2^2(\cdot,\rho)$.
:::

This is Proposition 5.1 of {cite:t}`VauthierKorbaMerigot2025`. In the first case each
projection of $\mu$ is uniform, $\mu_\theta = U[-\tfrac4\pi\abs{\cos\varphi}, \tfrac4\pi\abs{\cos\varphi}]$
for $\theta = (\cos\varphi, \sin\varphi)$, the monotone maps are linear, and the condition on
the segment reduces to $\int_{\Sph{1}} \abs{\cos\varphi} \dd\sigma = 2/\pi$. The same authors
show that such segments are unstable for a suitable perturbation.

:::{prf:proposition} A critical sphere
:label: prop:critical-sphere
Let $d \ge 2$ and $\rho = N(0, I_d)$. There is exactly one $r_* > 0$ such that the uniform
probability measure on the sphere $r_*\Sph{d-1}$ is a critical point of $\SW_2^2(\cdot,\rho)$.
It is also a Lagrangian and a Wasserstein critical point, $r_* < \sqrt d$, and
$r_* = 3/\sqrt\pi$ when $d = 3$.
:::

This is Example 1 of {cite:t}`DiazMartinMurphy2026`; the proof given here is direct and
does not rely on theirs.

**Idea of the proof.** All projections of the uniform probability
$\mu_r$ on $r\Sph{d-1}$ have one law, that of $r Z$ with $Z = \inner{e}{\Theta}$, $\Theta \sim \sigma$,
so every monotone map is the same function $s \mapsto \Phi^{-1}(H(s/r))$, with $H$ the
distribution function of $Z$. At a point $x = re$, reflections fixing $e$ kill the part of the
field orthogonal to $e$, and the barycentric field is

$$
v_{\mu_r}(x) = \Big(1 - \frac{r_*}{r}\Big)x, \qquad r_* = d\,A_d, \quad
A_d = \E\big[Z\,\Phi^{-1}(H(Z))\big] .
$$

This gives the uniqueness of the radius and the bound $0 < r_* < \sqrt d$: the critical sphere has a
smaller second moment than the target. In dimension three $Z$ is uniform on $[-1,1]$
(Archimedes) and $r_* = 3/\sqrt\pi$, the value computed by hand in [](#sec:overview); no
closed form is given here in other dimensions. The sphere has no atom, so by
[](#prop:notions-coincide) it is critical in all three senses of [](#def:critical-point) at
once, and a sphere of any other radius in none.

The sphere is the more instructive example: its projections are absolutely continuous, and
its support has codimension one, yet it is critical. Absolute continuity of the
projections is therefore not enough; a proof of [](#conj:sw-critical) must use that $\mu$
itself has a density. Nor can the equivalence of the notions of critical point be where the
density enters: the sphere and the segments have no atom, so for them, too, the three notions
coincide. Each proof in [](#sec:special-targets) says where the sphere escapes it.
