% Special cases of the target: two from the literature, three proved here (dossiers in
% solutions/, certified by agent reviews of 20 October 2026; no human review yet, novelty
% against the literature not checked). Contents of the labelled directives are fixed
% (orchestrator).

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

This result is contained in the next one, which removes the entropy hypothesis and allows
any Gaussian target; it is kept because it is the published case from which the next proof
starts.

:::{prf:theorem} Gaussian targets
:label: thm:gaussian-target
Let $d \ge 1$, $m \in \R^d$, $\Sigma$ a symmetric positive definite $d \times d$ matrix, and
$\rho = N(m, \Sigma)$. If $\mu \in \Ptwo{d}$ is absolutely continuous and is a critical point
of $\SW_2^2(\cdot,\rho)$, then $\mu = \rho$.
:::

No entropy assumption is made, no assumption on the support or the regularity of the density
of $\mu$, and $\Sigma$ may be anisotropic; the case $\rho = N(0, I_d)$ recovers
[](#thm:cs-isotropic) without its entropy hypothesis.

**What was known.** We found three strictly smaller cases in the literature. The isotropic
target with $\mu$ of finite entropy is [](#thm:cs-isotropic) above
({cite:t}`CozziSantambrogio2025`, Theorem 4.1, with the consequence drawn by
{cite:t}`VauthierKorbaMerigot2025`, Section 7). {cite:t}`ThurinBoyerNadjahi2026`
(Proposition 4), applied with the Gaussian target as reference measure, cover a $\mu$ whose
density is bounded above and below by multiples of the Gaussian density, hence with full
support; their Proposition 8, used in their Appendix E.1, covers a centred Gaussian $\mu$ and a
centred Gaussian target. We did not find the statement above, nor its method, in the
literature; that search has limits, and we make no stronger claim.

**Idea of the proof.** The heuristic is the dissipation of the relative entropy to $\rho$
along the preconditioned velocity $\Sigma v_\mu$, which, at a critical point, vanishes as
$v_\mu$ does. The proof replaces this flow computation by a static one, testing the condition
at order zero and at order one. On the interior $U$ of the convex hull of the support of
$\mu$, which carries all of $\mu$ because $\mu$ has a density, the field $v_\mu$ has a continuous
version in the Sobolev space $W^{1,1}_{\mathrm{loc}}(U)$, with
$Dv_\mu(x) = I - d\int T_\theta'(\inner{x}{\theta})\,\theta\theta^\top\dd\sigma(\theta)$. The gradient
of a Sobolev function vanishes almost everywhere on its zero set (Stampacchia), and since
$\mu$ has a density, $Dv_\mu = 0$ holds $\mu$-almost everywhere: this is the step the
singular critical points defeat. Pairing $v_\mu = 0$ with $x - m$, and taking the trace of
$Dv_\mu = 0$ against $\Sigma$, gives two identities between one-dimensional quantities, in
which the weight $\theta^\top\Sigma\theta$ is exactly the variance of $\rho_\theta$. In each
direction, because $\log\rho_\theta$ is a quadratic polynomial, the combination is at most
$-(\theta^\top\Sigma\theta)\,\mathrm{KL}(\mu_\theta\mid\rho_\theta) - \tfrac12\int\abs{T_\theta - \Id}^2\dd\mu_\theta$;
finiteness of the entropy of $\mu_\theta$ is deduced, not assumed. The identities make the
average over directions vanish, so $T_\theta = \Id$ for almost every $\theta$, and $\mu = \rho$
by the Cramér–Wold theorem.

For the uniform sphere of [](#prop:critical-sphere), the support of $\mu$ is the boundary of
its convex hull, which $\mu$ charges entirely: there is no interior on which to differentiate.
In dimension three the failure is visible: the monotone map sends $(-r,r)$ onto $\R$, so
$\int T_\theta'\dd\mu_\theta = \infty$ and the second identity breaks down.

**Limits.** The proof uses the Gaussian form of $\rho$ twice: $\log\rho_\theta$ is quadratic, so the
pairing with the linear field $x - m$ produces the potential part of every
$\mathrm{KL}(\cdot\mid\rho_\theta)$ at once; and the trace against a constant matrix produces the
variances of the $\rho_\theta$, the weights the entropy terms need. For another target, this
would require the one-dimensional scores $(\log\rho_\theta)'(\inner{x}{\theta})$ to combine
linearly into a single field $M\nabla\log\rho(x)$ on $\R^d$ with $M$ constant, which we expect,
but have not shown, to single out Gaussians.

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
Let $\rho \in \Ptwo{3}$ and $\mu \in \Ptwo{3}$ be invariant under rotations. Assume that
$\mu(\{0\}) = 0$ and that the support of the law of $\abs{X}$, for $X \sim \mu$, has no
isolated point; both hold when that law has no atom. If $\mu$ is a critical point of
$\SW_2^2(\cdot,\rho)$, then $\mu = \rho$.
:::

The hypotheses on $\mu$ bear only on its mass at the origin and on the shape of its radial
support: $\mu$ need be neither absolutely continuous nor compactly supported. The target may
be any rotation-invariant measure with a finite second moment, with an atom at the origin, a
singular part or an unbounded support.

**Idea of the proof.** Two features are special to dimension three. The condition is
*local*: the left-hand side above is a primitive, and since the radial support has no
isolated point, its derivative $h(r)\,r$ vanishes on it, so $T$ is the identity there. And
the projection of a sphere is *uniform* (Archimedes), so the density of $\mu_1$ is constant on
each hole of the radial support; since the density of $\rho_1$ is nonincreasing away from the
origin, its quantile function is convex there, and $T$ is convex on each hole. A convex
function equal to the identity at both ends of a hole lies below it, and the integral
condition across the hole then forces equality. The holes are treated one at a time, so a
radial support with infinitely many holes, such as a Cantor set of positive measure, needs
nothing more. We did not find this statement in the literature; the radial critical points treated
there are singular, such as the sphere of [](#prop:critical-sphere).

**Limits.** The uniform sphere of [](#prop:critical-sphere) has a single radius, an isolated
point of its radial support: it is exactly where the first step fails. In odd dimension
$d \ge 5$ the condition stays local but the projections of spheres are no longer uniform; in
even dimension the condition becomes non-local.

:::{prf:theorem} Radial measures on a full disc in the plane
:label: thm:radial-disc-d2
Let $\rho \in \Ptwo{2}$ be invariant under rotations, and let $\mu \in \Ptwo{2}$ be
invariant under rotations, with $\mu(\{0\}) = 0$ and with support a closed disc of positive
radius centred at the origin or the whole plane. If $\mu$ is a critical point of
$\SW_2^2(\cdot,\rho)$, then $\mu = \rho$.
:::

Here too $\mu$ need not be absolutely continuous, and $\rho$ may be any rotation-invariant
measure with a finite second moment. The proof gives a local form as well: if the open disc $B(0,a)$ lies in the support of $\mu$, the
monotone map is the identity on $(-a,a)$.

**Idea of the proof.** In the plane the condition becomes an Abel equation: with
$U(\tau) = h(\sqrt\tau)$, it reads $\int_0^x U(\tau)(x - \tau)^{-1/2} \dd\tau = 0$ for $x$ in the
squared radial support. When that support is a whole interval $[0, R^2]$, injectivity of the
Abel transform gives $U = 0$, so $T$ is the identity and the projections of $\mu$ and $\rho$
agree. To have the equation at every point of the disc and not only $\mu$-almost everywhere,
the proof uses that the field is continuous off the origin, not that the density of $\mu$ is
positive: a density vanishing on a set of radii of positive measure but empty interior is
covered.

The mechanism is that of [](#thm:bonnotte-full-support): the support of $\mu$ has no hole, so
the condition holds on a whole disc and determines the projections. Part of the statement is
known. When $\mu$ has a positive density on the disc and the support of $\rho$ lies in the
disc, the conclusion follows, in any dimension, from Lemma 5.7.2 of {cite:t}`Bonnotte2013`,
from Corollaries 3 and 4 of {cite:t}`DiazMartinMurphy2026`, and, for a density comparable to a
reference measure satisfying a Poincaré inequality, from Proposition 4 of
{cite:t}`ThurinBoyerNadjahi2026`. Each of these needs the support of $\rho$ inside that of
$\mu$ in some form; we did not find in the literature the cases where $\rho$ is an arbitrary
radial measure, nor those where the density of $\mu$ vanishes on a set of positive measure or
$\mu$ is not absolutely continuous. Neither [](#thm:bonnotte-full-support) nor the statement
above contains the other. Radial symmetry makes the inversion explicit, which removes every
hypothesis on $\rho$ and every positivity hypothesis on the density of $\mu$; the full-support
theorem needs no symmetry. Neither says anything about supports with holes.

**What remains.** On an annulus, the Abel equation on an interval away from the origin no
longer forces $U = 0$; [](#sec:open-directions) takes it up.
