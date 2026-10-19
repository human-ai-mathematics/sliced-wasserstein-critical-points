% Special cases of the target: two from the literature, three whose arguments were written
% during the scouting of 17 October 2026 (ensae-conjecture-scouting/verification/13-korba-sw/)
% and are not yet checked here. Contents of the labelled directives are fixed (orchestrator).

(sec:special-targets)=
# Special cases

## Full support

:::{prf:theorem} Full support
:label: thm:bonnotte-full-support
Let $R > 0$, and let $\mu, \rho$ be absolutely continuous probability measures on the ball
$B(0,R)$ of $\R^d$, both with a density strictly positive on $B(0,R)$. Then $\mu$ is a
critical point of $\SW_2^2(\cdot,\rho)$ if and only if $\mu = \rho$.
:::

This is due to {cite:t}`Bonnotte2013` (Lemma 5.7.2), in the form of Proposition 4.6 of
{cite:t}`VauthierKorbaMerigot2025`. When $\mu$ charges every direction of the whole ball, the
condition holds on all of $B(0,R)$, and it determines every projection of $\mu$. The question
of [](#conj:sw-critical) is what happens when the support of $\mu$ has holes.

## Gaussian targets

:::{prf:theorem} Standard Gaussian target, finite entropy
:label: thm:cs-isotropic
Let $\rho = N(0, I_d)$, and let $\mu \in \Ptwo{d}$ be absolutely continuous with finite
entropy $\int \mu \log \mu \dd x < \infty$. If $\mu$ is a critical point of
$\SW_2^2(\cdot,\rho)$, then $\mu = \rho$.
:::

{cite:t}`CozziSantambrogio2025` (Theorem 4.1) show that along the sliced Wasserstein flow
towards the standard Gaussian, started from a measure of finite entropy and second moment,
$\SW_2^2(\mu_t,\rho) \le C/t$; a critical point is a stationary solution, so it must be the
target. {cite:t}`VauthierKorbaMerigot2025` draw this consequence in Section 7.
% The implication from the flow theorem to critical points is stated in VKM §7, not in CS.

:::{prf:theorem} Gaussian targets
:label: thm:gaussian-target
Let $d \ge 1$, $m \in \R^d$, $\Sigma$ a symmetric positive definite $d \times d$ matrix, and
$\rho = N(m, \Sigma)$. If $\mu \in \Ptwo{d}$ is absolutely continuous and is a critical point
of $\SW_2^2(\cdot,\rho)$, then $\mu = \rho$.
:::

No entropy assumption is made, and $\Sigma$ may be anisotropic.

**Idea of the proof.** At a critical point, not only $v_\mu$ but every field $M v_\mu$ vanishes
$\mu$-almost everywhere, so the entropy dissipation of Cozzi and Santambrogio may be
computed along a preconditioned velocity. With $M = \Sigma$ the dissipation splits again
direction by direction, each projection showing the slope of the relative entropy to
$N(0, \theta^\top\Sigma\theta)$, which is exactly $\rho_\theta$. To avoid integrating by parts
against an irregular $\mu$, the argument works with the derivative of $v_\mu$: on the interior
of the convex hull of the support of $\mu$, $v_\mu$ is a Sobolev function, and the gradient of a
Sobolev function vanishes almost everywhere on its zero set. Taking the trace of
$D v_\mu = 0$ against $\Sigma$ and integrating in $\mu$ forces every monotone map $T_\theta$ to be
the identity.

**Limits.** The splitting needs the scores of the projected targets,
$(\log \rho_\theta)'(\inner{x}{\theta})$, to fit together linearly into a field
$M \nabla \log \rho(x)$ on $\R^d$, with $M$ constant. That forces $\rho$ to be Gaussian.

## Radial measures

When $\mu$ and $\rho$ are invariant under rotations, all projections of $\mu$ are one law
$\mu_1$, all projections of $\rho$ are one law $\rho_1$, and the condition becomes a
one-dimensional equation on the odd monotone map $T$ from $\mu_1$ to $\rho_1$. In dimension three,
with $h = T - \Id$, it reads

$$
\int_0^r h(u)\,u \dd u = 0 \qquad \text{for every radius $r$ in the support of } \abs{X},\ X \sim \mu .
$$

:::{prf:theorem} Radial measures in dimension three
:label: thm:radial-d3
Let $\rho \in \Ptwo{3}$ and $\mu \in \Ptwo{3}$ be invariant under rotations, and assume that the
law of $\abs{X}$, for $X \sim \mu$, has no atom. If $\mu$ is a critical point of
$\SW_2^2(\cdot,\rho)$, then $\mu = \rho$.
:::

**Idea of the proof.** Two features are special to dimension three. The condition is
*local*: the left-hand side above is a primitive, and since the radial support has no
isolated point, its derivative $h(r)\,r$ vanishes on it, so $T$ is the identity there. And
the projection of a sphere is *uniform* (Archimedes), so $\mu_1$ is constant on each hole of
the radial support, which makes $T$ convex there. A convex function equal to the identity at
both ends of a hole lies below it, and the integral condition across the hole then forces
equality.

**Limits.** The uniform sphere of [](#prop:critical-sphere) has a single radius, an isolated
point of its radial support: it is exactly where the first step fails. In odd dimension
$d \ge 5$ the condition stays local but the projections of spheres are no longer uniform; in
even dimension the condition becomes non-local.

:::{prf:theorem} Radial measures on a full disc in the plane
:label: thm:radial-disc-d2
Let $\rho \in \Ptwo{2}$ be invariant under rotations, and let $\mu \in \Ptwo{2}$ be
absolutely continuous and invariant under rotations, with support a closed disc centred at
the origin or the whole plane. If $\mu$ is a critical point of $\SW_2^2(\cdot,\rho)$, then
$\mu = \rho$.
:::

**Idea of the proof.** In the plane the condition becomes an Abel equation: with
$U(\tau) = h(\sqrt\tau)$, it reads $\int_0^x U(\tau)(x - \tau)^{-1/2} \dd\tau = 0$ for $x$ in the
squared radial support. When that support is a whole interval $[0, R^2]$, injectivity of the
Abel transform gives $U = 0$, so $T$ is the identity and the projections of $\mu$ and $\rho$
agree.

**What remains.** On an annulus, the Abel equation on an interval away from the origin no
longer forces $U = 0$; [](#sec:open-directions) takes it up.
