% The target statement. Its content is fixed (orchestrator); the prose is the writer's.
% Source of the formulation: ensae-conjecture-scouting/verification/13-korba-sw/1-relecture.md, §1.

(sec:target)=
# The question

{cite:t}`VauthierKorbaMerigot2025` close their study of the critical points of the sliced
Wasserstein distance with an open question (Section 7): *is it possible to prove that any
Wasserstein or Lagrangian critical point $\mu$ of $\tfrac12\SW_2^2(\cdot,\rho)$ which is
absolutely continuous must be equal to $\rho$?* With the normalizations of [](#sec:setting),
and since the notions of critical point coincide for an absolutely continuous measure
([](#prop:notions-coincide)), the question reads as follows.

:::{prf:conjecture} Absolutely continuous critical points are the target
:label: conj:sw-critical
Let $d \ge 2$, and let $\rho \in \Ptwo{d}$ be absolutely continuous. If $\mu \in \Ptwo{d}$ is
absolutely continuous and is a critical point of $\SW_2^2(\cdot,\rho)$, then $\mu = \rho$.
:::

In words: the condition

$$
d \int_{\Sph{d-1}} T_\theta(\inner{x}{\theta})\,\theta \dd\sigma(\theta) = x
\qquad \text{for $\mu$-almost every } x,
$$

with $T_\theta$ the monotone map from $\mu_\theta$ to $\rho_\theta$, forces every $T_\theta$ to
be the identity. The condition says nothing outside the support of $\mu$, and that is the
whole difficulty: a measure whose support leaves holes in the support of $\rho$ is
constrained only where it lives.

The conjecture is stated in the direction expected. Its negation asks for a single
dimension $d$, target $\rho$ and absolutely continuous critical point $\mu \ne \rho$.

**Why it matters.** The squared sliced Wasserstein distance is a common training loss for
generative models and the objective of particle methods that move a cloud of points
towards a target. It is not geodesically convex, and it has critical points other than
the target, all known ones singular ([](#sec:singular)). An affirmative answer would say
that, among measures with a density, the target is the only place a gradient method can
stop; it is the missing step between the stationary-point analysis and convergence results for the flow.

**Evidence.** The statement holds when $\mu$ and $\rho$ have positive densities on a common
ball ([](#thm:bonnotte-full-support)), and for the standard Gaussian target under finite
entropy ([](#thm:cs-isotropic)). [](#sec:special-targets) proves it for every Gaussian target
with no entropy hypothesis ([](#thm:gaussian-target)), for radial measures in dimension three
([](#thm:radial-d3)), and for radial measures in the plane whose support is a full disc
([](#thm:radial-disc-d2)). None of these touches the general case, where neither $\rho$ is
Gaussian nor the pair radial. Numerical
searches in the plane for an absolutely continuous critical point other than the target
have found none; this is evidence, not proof. [](#sec:open-directions) says where the general case resists.

**Where to start.** The cases of [](#sec:special-targets) fail beyond themselves for named
reasons: the Gaussian proof needs the scores of the projected targets to fit together
linearly, the radial proof in dimension three needs the projection of a sphere to be
uniform, and the planar proof needs the support of $\mu$ to have no hole. The annulus in the plane is the smallest configuration where neither applies.
