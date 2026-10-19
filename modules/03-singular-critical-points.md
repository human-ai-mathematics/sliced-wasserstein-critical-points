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
Let $d \ge 2$ and $\rho = N(0, I_d)$. There exists $r_* > 0$ such that the uniform probability
measure on the sphere $r_*\Sph{d-1}$ is a Wasserstein critical point of $\SW_2^2(\cdot,\rho)$.
:::

This is Example 1 of {cite:t}`DiazMartinMurphy2026`. By the first part of
[](#prop:notions-coincide), such a sphere is also a critical point. The overview computes
$r_* = 3/\sqrt\pi$ by hand in dimension three ([](#sec:overview)).

The sphere is the more instructive example: its projections are absolutely continuous, and
its support has codimension one, yet it is critical. Absolute continuity of the
projections is therefore not enough; a proof of [](#conj:sw-critical) must use that $\mu$
itself has a density.
