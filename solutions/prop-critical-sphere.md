---
title: "A critical sphere"
ledger-node: prop:critical-sphere
numbering:
  enumerator: "5.%s"
---

% Dossier for prop:critical-sphere (route ap:certify-scouting, lens prove). A direct,
% self-contained proof of Example 1 of Diaz Martin & Murphy, arXiv:2610.08734v1 (its
% appendix, "Details for Example 1"), which is compared with this proof in
% rem:sol-cs-source and is not used as authority. Normalizations: those of
% def:sliced-wasserstein and def:barycentric-field (sigma a probability, factor d in v_mu).

**Overview.** We prove [](#prop:critical-sphere) as [](#thm:sol-cs-main), which also gives the radius by a
formula: for every $d \ge 2$ there is *exactly one* radius $r_* > 0$ for which the uniform probability
on $r_*\Sph{d-1}$ is critical for $\SW_2^2(\cdot, N(0,I_d))$, it is given by a formula,
$0 < r_* < \sqrt d$, and $r_* = 3/\sqrt\pi$ when $d = 3$. The barycentric field of a sphere of
radius $r$ is computed in closed form on the whole sphere: it is $(1 - r_*/r)\,x$. The steps
are:

1. *The projections of the uniform sphere* ([](#lem:sol-cs-projection)). All the
   one-dimensional projections $\inner{e}{\theta}$, $\theta \sim \sigma$, have one law
   $\zeta_d$, which has no atom, is symmetric, has second moment $1/d$, and has a
   distribution function $H$ with $0 < H < 1$ on $(-1,1)$.
2. *The constant $A_d$* ([](#lem:sol-cs-constant)). With $\tau = \Phi^{-1} \circ H$ and
   $Z \sim \zeta_d$, the variable $\tau(Z)$ is standard normal, $\tau$ is nondecreasing with
   $\tau(0) = 0$, and $A_d = \E[Z\,\tau(Z)]$ satisfies $0 < A_d < 1/\sqrt d$.
3. *The barycentric field of a sphere* ([](#lem:sol-cs-field)). For $\mu_r$ the uniform
   probability on $r\Sph{d-1}$, every monotone map $T_\theta$ is $s \mapsto \tau(s/r)$, the
   same for all $\theta$; at $x = re$, a reflection argument kills the component of the
   integral orthogonal to $e$, and the component along $e$ is $dA_d$. Hence
   $v_{\mu_r}(x) = (r - dA_d)\,e$ at every point $x = re$ of the sphere.
4. *Criticality* (proof of [](#thm:sol-cs-main)). Step 3 gives $v_{\mu_r} = 0$ on the sphere
   if and only if $r = r_* := dA_d$. The sphere has no atom, so item 2 of
   [](#prop:notions-coincide) turns the barycentric condition into the Wasserstein one, and
   the Lagrangian one, of [](#def:critical-point), as [](#prop:critical-sphere) states; item 1 of
   the same statement excludes every other radius, which is the uniqueness it asserts.
5. *Dimension three* ([](#lem:sol-cs-d3)). There $\zeta_3$ is uniform on $[-1,1]$
   (Archimedes), $\tau(Z)$ and $Z$ are linked by $Z = 2\Phi(\tau(Z)) - 1$, and a Gaussian
   integration by parts gives $A_3 = 1/\sqrt\pi$.

**Dependencies.** The definitions [](#def:sliced-wasserstein), [](#def:barycentric-field)
and [](#def:critical-point), and the statement [](#prop:notions-coincide): item 2 (for a
measure with no atom, the three notions of critical point coincide) for $r = r_*$, and
item 1 for $r \ne r_*$. Only the barycentric part of the theorem is proved here; the
passage to the other two notions is that statement. Classical facts used: the uniform probability $\sigma$ on $\Sph{d-1}$ is the
normalized $(d-1)$-dimensional Hausdorff measure of $\Sph{d-1}$, invariant under the
orthogonal group $O(d)$ and positive on nonempty relatively open subsets; the probability
integral transform (if a real random variable $Y$ has a continuous distribution function
$F$, then $F(Y)$ is uniform on $(0,1)$); Tonelli's theorem; the area element of $\Sph{2}$ in spherical
coordinates. The source, {cite:t}`DiazMartinMurphy2026`, is not used.

## Conventions

Throughout, $d \ge 2$, $\rho = N(0, I_d)$, $\Phi$ and $\varphi = \Phi'$ are the distribution
function and the density of $N(0,1)$, and $\Phi^{-1} : (0,1) \to \R$ is the inverse of $\Phi$.
For $r > 0$, $\mu_r$ is the uniform probability on the sphere $r\Sph{d-1}$, that is, the law
of $r\Theta$ with $\Theta \sim \sigma$. For a unit vector $e$, $\zeta^e$ denotes the law of
$\inner{e}{\Theta}$, $\Theta \sim \sigma$.

## Refined statement

The following proves [](#prop:critical-sphere) and adds to it a formula for the radius, the
closed-form barycentric field of every centred sphere, and the fact that the critical sphere
differs from the target.

:::{prf:theorem} The critical sphere of a standard Gaussian target
:label: thm:sol-cs-main
Let $d \ge 2$ and $\rho = N(0, I_d)$. Let $Z$ have the common law $\zeta_d$ of the
projections $\inner{e}{\Theta}$, $\Theta \sim \sigma$, $\abs{e} = 1$
([](#lem:sol-cs-projection)), let $H$ be its distribution function, and let

$$
A_d = \E\big[Z\,\Phi^{-1}(H(Z))\big]
= \int_{\Sph{d-1}} \inner{e}{\theta}\,\Phi^{-1}\big(H(\inner{e}{\theta})\big)\dd\sigma(\theta),
\qquad r_* = d\,A_d .
$$

Then:

1. $0 < r_* < \sqrt d$.
2. For every $r > 0$, the barycentric field of $\mu_r$ relative to $\rho$
   ([](#def:barycentric-field)) is, $\mu_r$-almost everywhere,
   $v_{\mu_r}(x) = \big(1 - \tfrac{r_*}{r}\big)\,x$.
3. $\mu_r$ is a critical point of $\SW_2^2(\cdot,\rho)$ if and only if $r = r_*$. The
   measure $\mu_{r_*}$ is a critical point, a Lagrangian critical point and a Wasserstein
   critical point of $\SW_2^2(\cdot,\rho)$ ([](#def:critical-point)), and $\mu_{r_*} \ne \rho$.
   For $r \ne r_*$, $\mu_r$ is none of the three.
4. For $d = 3$, $r_* = 3/\sqrt\pi$.
:::

Items 1, 3 and 4 together are [](#prop:critical-sphere), for the explicit radius $r_* > 0$
above: $\mu_{r_*}$ is critical in all three senses, and no other radius is.

## The projections of the uniform sphere

:::{prf:lemma} Projections of the uniform sphere
:label: lem:sol-cs-projection
Let $d \ge 2$. The law $\zeta^e$ does not depend on the unit vector $e$; call it $\zeta_d$
and let $Z \sim \zeta_d$, with distribution function $H$. Then:

1. $\zeta_d$ has no atom, and $\Prob(\abs{Z} < 1) = 1$;
2. $\zeta_d$ is symmetric ($-Z \sim Z$), so $H(0) = \tfrac12$;
3. $\E[Z^2] = 1/d$;
4. $0 < H(t) < 1$ for every $t \in (-1,1)$.

Moreover, for every $r > 0$ and every $\theta \in \Sph{d-1}$, the projection
$(\mu_r)_\theta$ is the law of $rZ$; its distribution function is $s \mapsto H(s/r)$ and it
has no atom. Finally, $\mu_r$ has no atom.
:::

:::{prf:proof}
:class: dropdown
*Independence of $e$.* For unit vectors $e, e'$ choose $Q \in O(d)$ with $Q^\top e = e'$.
Since $Q\Theta \sim \Theta$, $\inner{e}{Q\Theta} = \inner{Q^\top e}{\Theta} = \inner{e'}{\Theta}$
has the law of $\inner{e}{\Theta}$: $\zeta^{e'} = \zeta^e$.

*1.* Fix $e$ and $t \in \R$. The set $\{\theta \in \Sph{d-1} : \inner{e}{\theta} = t\}$ is
empty if $\abs t > 1$, the single point $\{te\}$ if $\abs t = 1$, and, if $\abs t < 1$, the
sphere of radius $\sqrt{1-t^2}$ centred at $te$ in the affine hyperplane
$\{\inner{e}{y} = t\}$, a compact $(d-2)$-dimensional submanifold (two points when $d = 2$).
In every case its $(d-1)$-dimensional Hausdorff measure vanishes, because it has finite
$(d-2)$-dimensional Hausdorff measure and $d - 2 < d - 1$. As $\sigma$ is the normalized
$(d-1)$-dimensional Hausdorff measure of $\Sph{d-1}$, $\Prob(Z = t) = 0$. Since $\abs{Z} \le 1$
and $\Prob(Z = \pm 1) = 0$, $\Prob(\abs Z < 1) = 1$.

*2.* $-\Theta \sim \Theta$ (since $-I_d \in O(d)$), so $-Z = \inner{e}{-\Theta} \sim Z$. Then
$\Prob(Z \le 0) = \Prob(Z \ge 0)$, and these two numbers add up to $1 + \Prob(Z = 0) = 1$, so
$H(0) = \tfrac12$.

*3.* Take $e = e_1$. The coordinate permutations belong to $O(d)$, so $\E[\Theta_i^2]$ does not
depend on $i$; since $\sum_i \Theta_i^2 = 1$, $\E[\Theta_1^2] = 1/d$, and $Z = \Theta_1$.

*4.* For $t \in (-1,1)$, the sets $\{\theta \in \Sph{d-1} : \inner{e}{\theta} < t\}$ and
$\{\theta \in \Sph{d-1}: \inner{e}{\theta} > t\}$ are relatively open and nonempty (they contain
$-e$ and $e$), so they have positive $\sigma$-measure: $H(t) \ge \Prob(Z < t) > 0$ and
$1 - H(t) = \Prob(Z > t) > 0$.

*Projections of $\mu_r$.* If $X = r\Theta \sim \mu_r$, then $\inner{X}{\theta} =
r\inner{\theta}{\Theta} \sim rZ$ by the first part, applied with $e = \theta$. Hence
$(\mu_r)_\theta$ is the law of $rZ$, with distribution function
$\Prob(rZ \le s) = H(s/r)$, and it has no atom by item 1.

*Atoms of $\mu_r$.* For $x \in \R^d$, $\mu_r(\{x\}) = 0$ if $\abs{x} \ne r$; if $\abs x = r$,
put $e = x/r$: $\mu_r(\{x\}) = \sigma(\{e\}) \le \sigma(\{\theta : \inner{e}{\theta} = 1\}) =
\Prob(Z = 1) = 0$.
:::

:::{prf:remark} The law $\zeta_d$, and what is not used
:label: rem:sol-cs-density
Classically, $\zeta_d$ has the density
$t \mapsto \frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)}\,(1 - t^2)^{(d-3)/2}$ on $(-1,1)$:
the arcsine law for $d = 2$, the uniform law for $d = 3$, and $\sqrt d\,Z$ converges in law to
$N(0,1)$ as $d \to \infty$. None of this is used: the proof of [](#thm:sol-cs-main) needs only
items 1–4 of [](#lem:sol-cs-projection), and the case $d = 3$ is checked directly in
[](#lem:sol-cs-d3).
:::

## The constant $A_d$

Let $\tau : (-1,1) \to \R$, $\tau(t) = \Phi^{-1}(H(t))$, which is well defined by item 4 of
[](#lem:sol-cs-projection).

:::{prf:lemma} The constant $A_d$
:label: lem:sol-cs-constant
Let $d \ge 2$ and $Z \sim \zeta_d$. Then $\tau$ is nondecreasing and Borel, $\tau(0) = 0$,
$\tau(Z)$ is a standard normal variable, and

$$
0 < A_d = \E[Z\,\tau(Z)] < \frac{1}{\sqrt d}.
$$
:::

:::{prf:proof}
:class: dropdown
$H$ is nondecreasing and $\Phi^{-1}$ is increasing, so $\tau$ is nondecreasing, hence Borel.
By item 2 of [](#lem:sol-cs-projection), $\tau(0) = \Phi^{-1}(\tfrac12) = 0$. By item 1, $H$ is
continuous, so $H(Z)$ is uniform on $(0,1)$ (probability integral transform), and
$\tau(Z) = \Phi^{-1}(H(Z))$ is standard normal; $\tau(Z)$ is defined almost surely since
$\abs Z < 1$ almost surely.

*Positivity.* Since $\tau$ is nondecreasing and $\tau(0) = 0$, $t\,\tau(t) \ge 0$ for every
$t \in (-1,1)$, with equality only if $t = 0$ or $\tau(t) = 0$. Both events $\{Z = 0\}$ and
$\{\tau(Z) = 0\}$ are null, the first by item 1 of [](#lem:sol-cs-projection), the second
because $\tau(Z)$ is Gaussian. So $Z\tau(Z) > 0$ almost surely, and $A_d > 0$.

*Upper bound.* By the Cauchy–Schwarz inequality and item 3,
$A_d \le \E[Z^2]^{1/2}\,\E[\tau(Z)^2]^{1/2} = d^{-1/2}$; in particular $A_d$ is finite.
Equality would force $\tau(Z) = \lambda Z$ almost surely for some $\lambda \ge 0$; this is
impossible, because $\abs{\lambda Z} \le \lambda$ while $\Prob(\abs{\tau(Z)} > \lambda) > 0$ for
a standard normal $\tau(Z)$. So $A_d < d^{-1/2}$.
:::

## The barycentric field of a sphere

:::{prf:lemma} The barycentric field of $\mu_r$
:label: lem:sol-cs-field
Let $d \ge 2$, $r > 0$ and $\rho = N(0,I_d)$. For every $\theta$, the monotone map from
$(\mu_r)_\theta$ to $\rho_\theta$ of [](#def:barycentric-field) is
$T_\theta(s) = \tau(s/r)$ for $\abs s < r$, a set of full $(\mu_r)_\theta$-measure. The
barycentric field of $\mu_r$ relative to $\rho$ satisfies, for $\mu_r$-almost every $x$,

$$
v_{\mu_r}(x) = x - d \int_{\Sph{d-1}} \tau\big(\inner{x/r}{\theta}\big)\,\theta \dd\sigma(\theta),
$$

the integral converging absolutely for every $x \in r\Sph{d-1}$, and for every
$x = re \in r\Sph{d-1}$,

$$
d \int_{\Sph{d-1}} \tau\big(\inner{e}{\theta}\big)\,\theta \dd\sigma(\theta) = d A_d\, e,
\qquad\text{so}\qquad v_{\mu_r}(re) = (r - dA_d)\,e .
$$
:::

:::{prf:proof}
*The monotone maps.* Since $\rho = N(0,I_d)$ and $\abs\theta = 1$, $\rho_\theta = N(0,1)$, whose
quantile function is $\Phi^{-1}$. By [](#lem:sol-cs-projection), $(\mu_r)_\theta$ is the law of
$rZ$, has no atom and has distribution function $s \mapsto H(s/r)$, which lies in $(0,1)$ for
$\abs s < r$ (item 4); and $\Prob(\abs{rZ} < r) = 1$ (item 1). So, by
[](#def:barycentric-field), $\bar\gamma_\theta = T_\theta = \Phi^{-1}\circ H(\cdot/r) =
\tau(\cdot/r)$, $(\mu_r)_\theta$-almost everywhere on $(-r,r)$.

*A version.* Let $g(\theta,s) = \tau(s/r)$ for $\abs s < r$ and $g(\theta,s) = 0$ otherwise.
It is Borel on $\Sph{d-1}\times\R$ (it does not depend on $\theta$, and $\tau$ is Borel), and
by the previous paragraph $g(\theta,\cdot)$ is a version of $\bar\gamma_\theta$ for every
$\theta$.

*Independence of the version.* [](#def:barycentric-field) fixes $\bar\gamma_\theta$ only
$(\mu_r)_\theta$-almost everywhere, so we check that the field does not depend on the version.
Let $\tilde g$ be any Borel function on $\Sph{d-1}\times\R$ such that, for $\sigma$-almost
every $\theta$, $\tilde g(\theta,\cdot)$ is a version of $\bar\gamma_\theta$, that is,
$\tilde g(\theta,\cdot) = g(\theta,\cdot)$ $(\mu_r)_\theta$-almost everywhere. The function
$(x,\theta) \mapsto \abs{g - \tilde g}(\theta,\inner{x}{\theta})$ is Borel and nonnegative
on $\R^d\times\Sph{d-1}$, and $(\mu_r)_\theta$ is the image of $\mu_r$ under
$x \mapsto \inner{x}{\theta}$, so Tonelli's theorem gives

$$
\int_{\R^d}\int_{\Sph{d-1}} \abs{g - \tilde g}(\theta,\inner{x}{\theta})\dd\sigma(\theta)
\dd\mu_r(x)
= \int_{\Sph{d-1}}\int_\R \abs{g - \tilde g}(\theta,s)\dd(\mu_r)_\theta(s)\dd\sigma(\theta)
= 0 .
$$

Hence, for $\mu_r$-almost every $x$, $\tilde g(\theta,\inner{x}{\theta}) =
g(\theta,\inner{x}{\theta})$ for $\sigma$-almost every $\theta$, and the two integrals
$d\int \tilde g(\theta,\inner{x}{\theta})\,\theta\dd\sigma$ and
$d\int g(\theta,\inner{x}{\theta})\,\theta\dd\sigma$ coincide (the second converges
absolutely, see *Integrability* below). So $v_{\mu_r}$ may be computed with $g$, up to a
$\mu_r$-null set. For $x = re$ with $\abs e = 1$ and every $\theta$,
$\abs{\inner{x}{\theta}} \le r$ with equality only for $\theta = \pm e$, a $\sigma$-null set
([](#lem:sol-cs-projection), item 1); so $g(\theta,\inner{x}{\theta}) =
\tau(\inner{e}{\theta})$ for $\sigma$-almost every $\theta$, which gives the displayed formula
for $v_{\mu_r}$.

*Integrability.* For $x = re$,
$\int \tau(\inner{e}{\theta})^2 \dd\sigma(\theta) = \E[\tau(Z)^2] = 1$, because
$\inner{e}{\Theta} \sim Z$ and $\tau(Z)$ is standard normal ([](#lem:sol-cs-constant)). As
$\abs\theta = 1$ and $\sigma$ is a probability, the vector integral
$I(e) = \int \tau(\inner{e}{\theta})\,\theta\dd\sigma(\theta)$ converges absolutely.

*The component orthogonal to $e$.* Let $u$ be a unit vector orthogonal to $e$ and
$S = I_d - 2uu^\top \in O(d)$ the reflection across $u^\perp$. Then $Se = e$, $Su = -u$,
$S$ is symmetric, and $S\Theta \sim \Theta$. Hence
$\inner{e}{S\theta} = \inner{Se}{\theta} = \inner{e}{\theta}$ and
$\inner{u}{S\theta} = \inner{Su}{\theta} = -\inner{u}{\theta}$, and the change of variables
$\theta \mapsto S\theta$ gives

$$
\inner{u}{I(e)} = \int \tau(\inner{e}{\theta})\inner{u}{\theta}\dd\sigma(\theta)
= \int \tau(\inner{e}{S\theta})\inner{u}{S\theta}\dd\sigma(\theta)
= -\inner{u}{I(e)} ,
$$

so $\inner{u}{I(e)} = 0$. As $u \perp e$ is arbitrary, $I(e)$ is parallel to $e$.

*The component along $e$.*
$\inner{e}{I(e)} = \int \tau(\inner{e}{\theta})\inner{e}{\theta}\dd\sigma(\theta) =
\E[Z\tau(Z)] = A_d$, since $\inner{e}{\Theta} \sim Z$ for every unit $e$
([](#lem:sol-cs-projection)). So $I(e) = A_d\,e$ and
$v_{\mu_r}(re) = re - dA_d\,e = (r - dA_d)\,e$.
:::

## Dimension three

:::{prf:lemma} The radius in dimension three
:label: lem:sol-cs-d3
For $d = 3$, $\zeta_3$ is the uniform law on $[-1,1]$ and $A_3 = 1/\sqrt\pi$; hence
$r_* = 3/\sqrt\pi$.
:::

:::{prf:proof}
:class: dropdown
*Archimedes.* In spherical coordinates $\theta = (\sin\phi\cos\psi, \sin\phi\sin\psi,
\cos\phi)$, $\phi \in (0,\pi)$, $\psi \in (0,2\pi)$, the area element of $\Sph{2}$ is
$\sin\phi\dd\phi\dd\psi$, of total mass $4\pi$. With $e = e_3$, for $-1 \le a < b \le 1$,

$$
\sigma(\{a < \theta_3 \le b\}) = \frac{1}{4\pi}\int_0^{2\pi}\!\!\int_{\arccos b}^{\arccos a}
\sin\phi\dd\phi\dd\psi = \frac{b - a}{2} ,
$$

so $\zeta_3$ is uniform on $[-1,1]$ and $H(t) = (1+t)/2$ for $t \in [-1,1]$.

*The constant.* Let $G = \tau(Z)$, standard normal by [](#lem:sol-cs-constant). As $H$ is
increasing on $[-1,1]$, $Z = H^{-1}(\Phi(G)) = 2\Phi(G) - 1$ almost surely, so, using
$\E[G] = 0$,

$$
A_3 = \E[Z\,G] = \E\big[G\,(2\Phi(G) - 1)\big] = 2\,\E[G\,\Phi(G)]
= 2\int_\R z\varphi(z)\Phi(z)\dd z .
$$

Since $z\varphi(z) = -\varphi'(z)$, an integration by parts on $[-R,R]$ gives
$\int_{-R}^R z\varphi\Phi = [-\varphi\Phi]_{-R}^{R} + \int_{-R}^R \varphi^2$, and the bracket
tends to $0$ as $R \to \infty$ ($0 \le \Phi \le 1$, $\varphi(\pm R) \to 0$). Moreover
$\int_\R \varphi^2 = \frac{1}{2\pi}\int_\R e^{-z^2}\dd z = \frac{\sqrt\pi}{2\pi} =
\frac{1}{2\sqrt\pi}$. Hence $A_3 = 2\cdot\frac{1}{2\sqrt\pi} = \frac{1}{\sqrt\pi}$ and
$r_* = 3A_3 = 3/\sqrt\pi$.
:::

## Proof of the theorem

:::{prf:proof} Proof of [](#thm:sol-cs-main)
*1.* $r_* = dA_d$ and $0 < A_d < d^{-1/2}$ by [](#lem:sol-cs-constant), so $0 < r_* < \sqrt d$.

*2.* By [](#lem:sol-cs-field), for $\mu_r$-almost every $x$, writing $x = re$,
$v_{\mu_r}(x) = (r - r_*)\,e = (1 - r_*/r)\,x$.

*3.* By item 2, $v_{\mu_r}(x) = (1 - r_*/r)x$ for $\mu_r$-almost every $x$, and
$\abs x = r > 0$ $\mu_r$-almost everywhere. So $v_{\mu_r} = 0$ $\mu_r$-almost everywhere if
and only if $r = r_*$: by [](#def:critical-point), item 1, $\mu_r$ is a critical point if and
only if $r = r_*$.

The measure $\mu_r$ has no atom ([](#lem:sol-cs-projection)). By item 2 of
[](#prop:notions-coincide), the three notions of critical point coincide for $\mu_{r_*}$;
since it is a critical point, it is also a Lagrangian critical point and a Wasserstein
critical point of $\SW_2^2(\cdot,\rho)$. For $r \ne r_*$, $\mu_r$ is not a critical point, so
by item 1 of [](#prop:notions-coincide) it is neither a Lagrangian nor a Wasserstein
critical point.

Finally, $\mu_{r_*}(r_*\Sph{d-1}) = 1$, while $\rho(r_*\Sph{d-1}) = 0$ because $\rho$ has a
density and the sphere is Lebesgue-null; so $\mu_{r_*} \ne \rho$.

*4.* This is [](#lem:sol-cs-d3).

Since $r_* > 0$, $\mu_{r_*}$ is a critical, a Lagrangian and a Wasserstein critical point, no
other radius is any of the three, and item 4 holds, items 1, 3 and 4 give
[](#prop:critical-sphere).
:::

## Remarks

:::{prf:remark} The radius in other dimensions
:label: rem:sol-cs-formula
Let $U = H(Z)$, uniform on $(0,1)$, and let $Q_{\zeta_d}(u) = \inf\{t : H(t) \ge u\}$ be the
quantile function of $\zeta_d$. Then $Z = Q_{\zeta_d}(U)$ almost surely: by right continuity of
$H$, $Q_{\zeta_d}(u) \le t$ if and only if $u \le H(t)$, so $Q_{\zeta_d}(H(Z)) \le Z$; and
$Q_{\zeta_d}(U)$ has law $\zeta_d$, because $\Prob(Q_{\zeta_d}(U) \le t) = \Prob(U \le H(t)) =
H(t)$; so the nonnegative bounded variable $Z - Q_{\zeta_d}(U)$ has mean zero and vanishes
almost surely. Also $\tau(Z) = \Phi^{-1}(U)$. So the pair $(Z, \tau(Z))$ is the
comonotone coupling of $\zeta_d$ and $N(0,1)$, and

$$
r_* = d\int_0^1 Q_{\zeta_d}(u)\,\Phi^{-1}(u)\dd u ,
$$

$d$ times the covariance of $\zeta_d$ and $N(0,1)$ under their monotone coupling. For
$d = 2$, $\zeta_2$ is the law of $\cos\Psi$ with $\Psi$ uniform on $(0,2\pi)$, $Q_{\zeta_2}(u)
= -\cos(\pi u)$ and $r_* = -2\,\E[G\cos(\pi\Phi(G))]$ with $G \sim N(0,1)$. This proof gives
a closed form only for $d = 3$; whether other dimensions admit one is not addressed. The
bound $r_* < \sqrt d$ says that the critical sphere has a smaller second moment, $r_*^2$,
than the target, whose second moment is $d$.
:::

:::{prf:remark} Comparison with the source
:label: rem:sol-cs-source
The statement is Example 1 of {cite:t}`DiazMartinMurphy2026` (arXiv:2610.08734v1), proved in
its appendix ("Details for Example 1"). Their argument and this one agree in substance: the
projections of $\mu_r$ all have the law of $rZ$, the monotone map is
$\Phi^{-1}(H(\cdot/r))$ in every direction, equivariance under the orthogonal maps fixing $e$
makes the field at $re$ parallel to $e$, and the radial component is affine in $r$, with
root $r_* = dA_d$ for the same constant $A_d = \int \Phi^{-1}(H(\theta_1))\theta_1
\dd\sigma(\theta)$. The differences are the following.

- *Normalization.* They study $F = \tfrac12\SW_2^2(\cdot, N(0,I_d))$ and write its
  Wasserstein gradient as $\int(\inner{x}{\theta} - T_\theta(\inner{x}{\theta}))\,\theta
  \dd\sigma(\theta)$, with $\sigma$ a probability. By [](#def:sliced-wasserstein) and the
  identity $\int\inner{x}{\theta}\theta\dd\sigma = x/d$, this is $v_\mu(x)/d$: consistent with
  the first variation $\tfrac2d\inner{v_\mu}{\xi}_{L^2(\mu)}$ of $\SW_2^2$ along
  $(\Id + t\xi)_\#\mu$ for atomless $\mu$ in this normalization, halved.
  The zero set, and hence $r_*$, are the same.
- *The notion of criticality.* Their "Wasserstein critical point" is the vanishing of the
  Wasserstein gradient of their Proposition 1, which they obtain as the derivative along
  $(\Id + tv)_\#\mu$ for $v \in C^1_c(\R^d;\R^d)$, assuming atomless projections. This is a
  Lagrangian-type notion with smooth test fields, not the geodesic notion of
  [](#def:critical-point), item 3. Here the passage from $v_\mu = 0$ to the notions of
  [](#def:critical-point) goes through [](#prop:notions-coincide) instead of their Proposition 1,
  which is not used.
- *Positivity and finiteness of $A_d$.* They assert that $A_d$ is finite and strictly positive;
  [](#lem:sol-cs-constant) proves it, with the bound $A_d < d^{-1/2}$.
- *Uniqueness and the value.* Their argument shows, without saying so, that $r_*$ is the only
  critical radius, since the equation is affine in $r$; item 3 of [](#thm:sol-cs-main) states
  it. They give no value of $r_*$; the value $3/\sqrt\pi$ for $d = 3$
  ([](#lem:sol-cs-d3)) agrees with the hand computation of [](#sec:overview).
- *Symmetry.* They use every orthogonal map fixing $e$, and also equivariance to transport the
  conclusion from $re_1$ to the whole sphere; here one reflection per orthogonal direction
  suffices, and the computation is done directly at every point $re$.

No discrepancy affecting the result was found.
:::

**Consistency.** The sphere is a test case for [](#conj:sw-critical); [](#thm:sol-cs-main) is
consistent with that conjecture,
since $\mu_{r_*}$ is not absolutely continuous (it is concentrated on a Lebesgue-null sphere),
and with [](#prop:notions-coincide), since $\mu_{r_*}$ has no atom and is critical in all three
senses at once.
