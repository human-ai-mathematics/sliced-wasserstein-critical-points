---
title: "Radial measures in dimension three"
ledger-node: thm:radial-d3
numbering:
  enumerator: "3.%s"
---

% Dossier for thm:radial-d3 (route ap:certify-scouting, lens prove). Written from scratch;
% the scouting file ensae-conjecture-scouting/verification/13-korba-sw/1-relecture.md, §3
% ("Théorème B") and §4, suggested the structure and is not cited as authority. Certified
% (see the proofs[] record in the ledger). Normalizations: those of
% def:sliced-wasserstein and def:barycentric-field (sigma a probability, factor d = 3).

**Overview.** We prove [](#thm:radial-d3) in a slightly sharper form,
[](#thm:sol-radial-d3): instead of "the law of $\abs{X}$ has no atom" it suffices that this law
has no atom at $0$ and that its support has no isolated point. The target $\rho$ is any
rotation-invariant measure of $\Ptwo{3}$: atoms (necessarily at $0$), singular parts and
unbounded supports are allowed, and $\mu$ need not be absolutely continuous nor compactly
supported. The steps are:

1. *Projections* ([](#lem:r3-projections)). All projections of $\mu$ are one even law $\mu_1$,
   and all projections of $\rho$ are one law $\rho_1$. Off the origin, $\mu_1$ has a density
   $f$ that is nonincreasing in $\abs{u}$, positive exactly for $\abs{u} < R$, and *constant on
   every hole* of the radial support (Archimedes).
2. *The quantile function of $\rho_1$* ([](#lem:r3-quantile)) is continuous, odd about
   $\tfrac12$, and convex on $[\tfrac12, 1)$, because the density of $\rho_1$ is nonincreasing
   on $(0,\infty)$; an atom of $\rho$ at $0$ only adds a flat piece.
3. *The monotone map* ([](#lem:r3-monotone)). $T = Q_{\rho_1}\circ F_{\mu_1}$ is defined,
   finite, continuous and odd on the whole interval $(-R,R)$, holes included, and convex on the
   closure of every hole that stays away from $R$.
4. *Radial reduction* ([](#lem:r3-reduction)). For $0 < r < R$ and a unit vector $e$, the
   barycentric field is $v_\mu(re) = -\tfrac{3}{r^2}\,G(r)\,e$ with
   $G(r) = \int_0^r (T(u) - u)\,u \dd u$, a $C^1$ function on $[0,R)$; criticality gives
   $G = 0$ on $K \cap (0,R)$, where $K$ is the radial support.
5. *Structure of the radial support* ([](#lem:r3-support)). $K$ is perfect, and each connected
   component of $(0,R) \setminus K$ is an interval $(a,b)$ with $b < R$, $b \in K$, and
   $a \in K$ or $a = 0$.
6. *Conclusion* (proof of [](#thm:sol-radial-d3)). On $K \cap (0,R)$, $G$ vanishes on a set
   with no isolated point, so $G' = (T - \Id)\,u$ vanishes there and $T = \Id$. On each hole
   $[a,b]$, $T$ is convex with $T(a) = a$, $T(b) = b$, so $h = T - \Id \le 0$; the integral
   condition $G(b) - G(a) = 0$ then forces $h = 0$. Hence $T = \Id$ on $(-R,R)$, $\rho_1 = \mu_1$,
   and $\mu = \rho$ by Cramér–Wold.

The holes are treated one at a time and independently, with no ordering or induction, so
countably many dense holes (a fat Cantor radial support) need nothing more. The audit
remarks locate exactly where the critical sphere of [](#prop:critical-sphere) and the
critical point $\delta_0$ escape the argument.

**Dependencies.**

- Manuscript results: [](#def:critical-point), hence [](#def:barycentric-field) and
  [](#def:sliced-wasserstein). From [](#def:barycentric-field) we use its stated fact that, when
  $\mu_\theta$ has no atom, $\bar\gamma_\theta = T_\theta = Q_{\rho_\theta}\circ F_{\mu_\theta}$
  $\mu_\theta$-a.e.: the one-dimensional optimal transport theorem, {cite:t}`Santambrogio2015`,
  Theorem 2.9 (with Proposition 2.2 for $(Q_\nu)_\#\mathrm{Unif}(0,1) = \nu$ and
  $(F_\nu)_\#\nu = \mathrm{Unif}(0,1)$ for an atomless $\nu$). No other result of the manuscript is used. In
  particular [](#prop:notions-coincide), [](#thm:gaussian-target) and
  [](#prop:critical-sphere) are **not** used; [](#prop:critical-sphere) and
  [](#prop:critical-segments) appear only in audit remarks, which are not part of the proof.
- Classical facts used without proof: Archimedes' theorem (if $\omega$ is uniform on $\Sph{2}$
  and $e$ is a unit vector, $\inner{\omega}{e}$ is uniform on $[-1,1]$: the zone
  $\{a \le \inner{\omega}{e} \le b\}$ of the unit sphere has area $2\pi(b-a)$); transitivity
  of the action of $SO(3)$ on $\Sph{2}$; Fubini–Tonelli; the fundamental theorem of calculus
  for continuous integrands; the structure of open subsets of $\R$ (countable disjoint unions of
  open intervals); the Cramér–Wold theorem (a probability measure on $\R^d$ is determined by
  its one-dimensional projections, via characteristic functions).

**Notation.** "Rotation" means an element of $SO(3)$; invariance under $O(3)$ implies it. For
$\nu$ a measure on $\R^3$, $\nu_{\mathrm{rad}} = \abs{\cdot}_\#\nu$ is its *radial law*. We fix
rotation-invariant $\mu, \rho \in \Ptwo{3}$ and put

- $K = \operatorname{supp}\mu_{\mathrm{rad}} \subset [0,\infty)$, $R = \sup K \in [0,\infty]$;
- $S = \sup \operatorname{supp}\rho_{\mathrm{rad}} \in [0,\infty]$, $\rho_0 = \rho(\{0\})$;
- for a probability $\nu$ on $\R$: $F_\nu(t) = \nu((-\infty,t])$ and
  $Q_\nu(p) = \inf\{t : F_\nu(t) \ge p\}$ for $p \in (0,1)$, which is finite, nondecreasing and
  satisfies $Q_\nu(p) \le t \iff p \le F_\nu(t)$;
- $\mathrm{U}[-r,r]$ the uniform probability on $[-r,r]$ for $r > 0$, and $\mathrm{U}[0,0] = \delta_0$.

## Statement

**Refined statement.** [](#thm:sol-radial-d3) below contains [](#thm:radial-d3): if the law
$\mu_{\mathrm{rad}}$ of $\abs{X}$ has no atom, then $\mu_{\mathrm{rad}}(\{0\}) = 0$ and its support
has no isolated point (an isolated point $r$ of the support has a neighbourhood $U$ with
$\mu_{\mathrm{rad}}(U) = \mu_{\mathrm{rad}}(\{r\}) > 0$). The hypotheses on $\rho$ are those of
[](#thm:radial-d3): rotation invariance and finite second moment.

:::{prf:theorem} Radial measures in dimension three, refined
:label: thm:sol-radial-d3
Let $\rho \in \Ptwo{3}$ and $\mu \in \Ptwo{3}$ be invariant under rotations. Assume that

(H) $\mu(\{0\}) = 0$, and the support $K$ of the law $\mu_{\mathrm{rad}}$ of $\abs{X}$, $X \sim \mu$,
has no isolated point.

If $\mu$ is a critical point of $\SW_2^2(\cdot,\rho)$, that is $v_\mu = 0$ $\mu$-almost
everywhere, then $\mu = \rho$. In particular this holds when $\mu_{\mathrm{rad}}$ has no atom, for
instance when $\mu$ is absolutely continuous, and neither $\mu$ nor $\rho$ need be compactly
supported or absolutely continuous.
:::

Throughout [](#lem:r3-projections)–[](#lem:r3-support), $\mu, \rho \in \Ptwo{3}$ are
rotation-invariant. Hypothesis (H) is assumed from [](#lem:r3-monotone) on, and criticality
only in the last part of [](#lem:r3-reduction) and in the final proof.

## Projections of radial measures

:::{prf:lemma} Projections
:label: lem:r3-projections
1. For every $\theta \in \Sph{2}$, $\mu_\theta = \mu_1$ and $\rho_\theta = \rho_1$, where

   $$
   \mu_1 = \int_{[0,\infty)} \mathrm{U}[-r,r] \dd\mu_{\mathrm{rad}}(r), \qquad
   \rho_1 = \int_{[0,\infty)} \mathrm{U}[-r,r] \dd\rho_{\mathrm{rad}}(r).
   $$
2. $\mu_1 = \mu(\{0\})\,\delta_0 + f(u)\dd u$ and $\rho_1 = \rho_0\,\delta_0 + g(u)\dd u$, with,
   for $u \ne 0$,

   $$
   f(u) = \int_{(\abs{u},\infty)} \frac{\dd\mu_{\mathrm{rad}}(r)}{2r}, \qquad
   g(u) = \int_{(\abs{u},\infty)} \frac{\dd\rho_{\mathrm{rad}}(r)}{2r}.
   $$
   Both are even, finite ($f(u) \le 1/(2\abs{u})$), nonincreasing in $\abs{u}$; $f(u) > 0$ iff
   $0 < \abs{u} < R$, and $g(u) > 0$ iff $0 < \abs{u} < S$. Both $\mu_1$ and $\rho_1$ are
   symmetric.
3. (*Holes.*) If $0 \le a < b$ and $\mu_{\mathrm{rad}}((a,b)) = 0$, then $f$ is constant on
   $(a,b)$, equal to $c_b = \int_{[b,\infty)} \dd\mu_{\mathrm{rad}}(r)/(2r)$, and
   $0 < c_b < \infty$ whenever $0 < b < R$.
:::

:::{prf:proof}
:class: dropdown
*(1)* Let $\varphi : \R \to \R$ be bounded Borel. For a rotation $O$,
$\int \varphi(\inner{x}{O\theta})\dd\mu(x) = \int \varphi(\inner{O^\top x}{\theta})\dd\mu(x) =
\int \varphi(\inner{x}{\theta})\dd\mu(x)$, because $(O^\top)_\#\mu = \mu$. Since $SO(3)$ acts
transitively on $\Sph{2}$, $\theta \mapsto \int \varphi(\inner{x}{\theta})\dd\mu(x)$ is constant.
Averaging it over $\sigma$ and using Fubini ($\varphi$ is bounded),

$$
\int \varphi \dd\mu_\theta = \int_{\R^3} \Big(\int_{\Sph{2}} \varphi(\inner{x}{\theta'})
\dd\sigma(\theta')\Big) \dd\mu(x).
$$

For $x = re$ with $r > 0$ and $\abs{e} = 1$, Archimedes' theorem gives
$\int_{\Sph{2}} \varphi(r\inner{e}{\theta'})\dd\sigma(\theta') = \tfrac12\int_{-1}^1 \varphi(rs)\dd s =
\int \varphi \dd\mathrm{U}[-r,r]$; for $x = 0$ the inner integral is $\varphi(0)$. The inner
integral depends on $x$ only through $\abs{x}$, so
$\int\varphi\dd\mu_\theta = \int_{[0,\infty)} \big(\int\varphi\dd\mathrm{U}[-r,r]\big)\dd\mu_{\mathrm{rad}}(r)$.
The same holds for $\rho$.

*(2)* Split off $r = 0$ and apply Tonelli to $\varphi \ge 0$:
$\int_{(0,\infty)} \frac{1}{2r}\int_{\R} \one_{\abs{u} < r}\varphi(u)\dd u\dd\mu_{\mathrm{rad}}(r)
= \int_{\R} \varphi(u) \Big(\int_{(0,\infty)} \frac{\one_{r > \abs{u}}}{2r}\dd\mu_{\mathrm{rad}}(r)\Big)\dd u$,
and the inner integral is $f(u)$ for $u \ne 0$. Evenness and monotonicity in $\abs{u}$ are read
on the formula (the domain $(\abs{u},\infty)$ shrinks as $\abs{u}$ grows), and
$f(u) \le \mu_{\mathrm{rad}}((\abs{u},\infty))/(2\abs{u})$. The integrand $1/(2r)$ is positive,
so $f(u) > 0$ iff $\mu_{\mathrm{rad}}((\abs{u},\infty)) > 0$, iff the open set $(\abs{u},\infty)$
meets $K$, iff $\abs{u} < R$. Likewise for $g$ with $S$. Symmetry of $\mu_1$, $\rho_1$ follows
from (1), since each $\mathrm{U}[-r,r]$ is symmetric.

*(3)* For $u \in (a,b)$, $(u,\infty) = (u,b) \cup [b,\infty)$ and
$\mu_{\mathrm{rad}}((u,b)) = 0$, so $f(u) = c_b$. If $0 < b$, $c_b \le 1/(2b) < \infty$. If
$b < R$, the open set $(b,\infty)$ meets $K$, so $\mu_{\mathrm{rad}}([b,\infty)) > 0$ and $c_b > 0$.
:::

## The quantile function of the projected target

Write $F = F_{\rho_1}$ and $Q = Q_{\rho_1}$ in this section.

:::{prf:lemma} Quantile function of $\rho_1$
:label: lem:r3-quantile
1. $Q$ is finite, nondecreasing and continuous on $(0,1)$, and $Q_\#\mathrm{Unif}(0,1) = \rho_1$.
2. $Q(1-p) = -Q(p)$ for every $p \in (0,1)$, and $Q(\tfrac12) = 0$.
3. $Q$ is convex on $[\tfrac12, 1)$.
:::

:::{prf:proof}
:class: dropdown
If $S = 0$, then $\rho = \delta_0$, $\rho_1 = \delta_0$ and $Q \equiv 0$: all claims hold. Assume
$S > 0$; then $\rho_0 < 1$ and, by [](#lem:r3-projections) (2), $\rho_1(J) \ge \int_J g > 0$ for
every nonempty open interval $J \subset (-S,S)$. Also $\rho_1(\{t\}) = 0$ for $t \neq 0$.

*(1)* Finiteness, monotonicity, left-continuity and $Q_\#\mathrm{Unif}(0,1) = \rho_1$ are standard
consequences of $Q(p) \le t \iff p \le F(t)$. Right-continuity: fix $p \in (0,1)$ and let
$Q(p+) = \lim_{p' \downarrow p} Q(p')$. Suppose $Q(p) < Q(p+)$ and let $t \in (Q(p), Q(p+))$.
Then $F(t) \ge p$ because $t > Q(p)$, and $F(t) < p'$ for every $p' > p$ because
$t < Q(p+) \le Q(p')$. So $F(t) = p$ on the open interval $J = (Q(p),Q(p+))$, i.e.
$\rho_1(J) = 0$. But $F(t) = 0$ for $t < -S$ and $F(S) = 1$ if $S < \infty$, so
$-S \le Q(p)$ and $Q(p+) \le Q(\tfrac{1+p}{2}) \le S$: $J$ is a nonempty open interval in
$(-S,S)$, which $\rho_1$ charges. Contradiction.

*(2)* By symmetry, $F(t) = \rho_1((-\infty,t]) = \rho_1([-t,\infty)) = 1 - F((-t)-)$. Hence
$F(t) \ge 1-p \iff F((-t)-) \le p$, and

$$
Q(1-p) = \inf\{t : F((-t)-) \le p\} = -\sup\{s : F(s-) \le p\}.
$$

The last supremum equals $Q^+(p) := \sup\{s : F(s) \le p\}$: $F(s-) \le F(s)$ gives "$\ge$",
and if $F(s-) \le p$ then $F(s') \le p$ for all $s' < s$, giving "$\le$". Finally
$Q^+(p) = Q(p)$: if $t < Q(p)$ then $F(t) < p$, so $Q^+(p) \ge Q(p)$; if $F(s) \le p < p'$ then
$s \le Q(p')$ (otherwise $F(s) \ge F(Q(p')) \ge p'$), so $Q^+(p) \le Q(p') \to Q(p)$ as
$p' \downarrow p$, by (1). Thus $Q(1-p) = -Q(p)$, and $Q(\tfrac12) = 0$.

*(3)* Put $p_0 = F(0) = \tfrac{1+\rho_0}{2}$ and $M = \tfrac{1-\rho_0}{2} > 0$. For $t < 0$,
$F(t) \le \rho_1((-\infty,0)) = M \le \tfrac12$.

- For $p \in (\tfrac12, p_0]$: $F(0) = p_0 \ge p$ gives $Q(p) \le 0$, and $F(t) \le \tfrac12 < p$
  for $t < 0$ gives $Q(p) \ge 0$. With (2), $Q = 0$ on $[\tfrac12, p_0]$.
- For $t \ge 0$, $F(t) = p_0 + \Phi(t)$ with $\Phi(t) = \int_0^t g$. On $[0,S)$, $\Phi$ is
  continuous, strictly increasing ($g > 0$ on $(0,S)$), concave ($g$ nonincreasing), with
  $\Phi(0) = 0$ and $\Phi(t) \uparrow \rho_1((0,\infty)) = M$ as $t \uparrow S$; and $\Phi = M$ on
  $[S,\infty)$. Let $\psi : [0,M) \to [0,S)$ be the inverse bijection. It is nondecreasing and
  convex: for $y_i = \Phi(t_i)$ and $\lambda \in [0,1]$, concavity gives
  $\Phi(\lambda t_1 + (1-\lambda)t_2) \ge \lambda y_1 + (1-\lambda) y_2$, and applying $\psi$,
  $\lambda\psi(y_1) + (1-\lambda)\psi(y_2) \ge \psi(\lambda y_1 + (1-\lambda) y_2)$.
- For $p \in (p_0, 1)$: $F(t) \le M < p$ for $t < 0$, so
  $Q(p) = \inf\{t \ge 0 : \Phi(t) \ge p - p_0\} = \psi(p - p_0)$, since
  $\{t \ge 0 : \Phi(t) \ge y\} = [\psi(y),\infty)$ for $y \in [0,M)$.

Hence $Q(p) = \psi((p - p_0)^+)$ on $[\tfrac12, 1)$ (note $\psi(0) = 0$): a nondecreasing convex
function of a convex function, so convex.
:::

## The monotone map

From here on (H) holds. Then $K$, being nonempty with no isolated point, is infinite, so
$R > 0$.

:::{prf:lemma} The monotone map
:label: lem:r3-monotone
Let $F_1 = F_{\mu_1}$ and $T = Q \circ F_1$ on $(-R,R)$.

1. $\mu_1$ has no atom; $F_1$ is continuous on $\R$, strictly increasing on $(-R,R)$, maps
   $(-R,R)$ onto $(0,1)$, and $\mu_1((-R,R)) = 1$. Moreover $F_1(0) = \tfrac12$ and
   $F_1(-u) = 1 - F_1(u)$.
2. $T$ is finite, nondecreasing, continuous and odd on $(-R,R)$, with $T(0) = 0$ and
   $T_\#\mu_1 = \rho_1$. For every $\theta$, $\bar\gamma_\theta = T$ $\mu_1$-a.e.
3. If $0 \le a < b < R$ and $\mu_{\mathrm{rad}}((a,b)) = 0$, then $T$ is convex on $[a,b]$.
:::

:::{prf:proof}
:class: dropdown
*(1)* By [](#lem:r3-projections) (2) and $\mu(\{0\}) = 0$, $\mu_1 = f(u)\dd u$, so $F_1$ is
continuous. For $-R < u < u' < R$, $\mu_1((u,u']) = \int_u^{u'} f > 0$ since $f > 0$ on
$(u,u') \setminus \{0\}$. If $R < \infty$, $\mu_1$ is carried by $[-R,R]$ (as $K \subset [0,R]$)
and has no atom, so $\mu_1((-R,R)) = 1$, $F_1(u) \to 0$ as $u \downarrow -R$ and $F_1(u) \to 1$ as
$u \uparrow R$; the same limits hold at $\mp\infty$ if $R = \infty$. By continuity and strict
monotonicity, $F_1$ maps $(-R,R)$ onto $(0,1)$. Symmetry and continuity give
$F_1(-u) = \mu_1([u,\infty)) = 1 - F_1(u)$, and $F_1(0) = \tfrac12$.

*(2)* $T$ is the composition of $F_1 : (-R,R) \to (0,1)$, continuous nondecreasing, with $Q$,
finite continuous nondecreasing on $(0,1)$ ([](#lem:r3-quantile) (1)). Oddness:
$T(-u) = Q(1 - F_1(u)) = -Q(F_1(u)) = -T(u)$ by [](#lem:r3-quantile) (2), so $T(0) = 0$. Since
$\mu_1$ is atomless, $(F_1)_\#\mu_1 = \mathrm{Unif}(0,1)$, hence $T_\#\mu_1 = Q_\#\mathrm{Unif}(0,1) = \rho_1$.
For every $\theta$, $\mu_\theta = \mu_1$ has no atom and $\rho_\theta = \rho_1$
([](#lem:r3-projections) (1)), so [](#def:barycentric-field) gives
$\bar\gamma_\theta = Q_{\rho_1}\circ F_{\mu_1} = T$ $\mu_1$-a.e.

*(3)* By [](#lem:r3-projections) (3), $f = c_b$ on $(a,b)$ with $0 < c_b < \infty$ ($b > 0$ as
$b > a \ge 0$). Hence $F_1(u) = F_1(a) + c_b(u - a)$ for $u \in [a,b]$: an increasing affine
function. Its values lie in $[F_1(0), F_1(b)] \subset [\tfrac12, 1)$, since $a \ge 0$ and
$F_1(b) < 1$ by (1). By [](#lem:r3-quantile) (3), $Q$ is convex on $[\tfrac12,1)$, and a convex
function of an increasing affine function is convex.
:::

## The radial reduction

:::{prf:lemma} Radial reduction of the barycentric field
:label: lem:r3-reduction
Assume (H). Let $h = T - \Id$ on $(-R,R)$ and

$$
G(r) = \int_0^r h(u)\,u \dd u, \qquad 0 \le r < R .
$$

1. $G$ is finite and $C^1$ on $[0,R)$, with $G(0) = 0$ and $G'(r) = h(r)\,r$.
2. For $x \in \R^3$ with $0 < \abs{x} < R$, the field
   $V(x) = x - 3\int_{\Sph{2}} T(\inner{x}{\theta})\,\theta\dd\sigma(\theta)$ is well defined, and,
   writing $x = re$ with $r = \abs{x}$,

   $$
   V(re) = \Big(r - 3\int_0^1 T(rs)\,s \dd s\Big)\, e = -\frac{3}{r^2}\,G(r)\, e .
   $$ (eq-r3-reduction)
3. $v_\mu = V$ $\mu$-a.e. on $\{x : 0 < \abs{x} < R\}$.
4. If $\mu$ is a critical point of $\SW_2^2(\cdot,\rho)$, then $G = 0$ on $K \cap [0,R)$.
:::

:::{prf:proof}
*(1)* $T$ is continuous on $(-R,R)$ ([](#lem:r3-monotone) (2)), so $u \mapsto h(u)u$ is
continuous on $[0,R)$; the fundamental theorem of calculus applies on every $[0,r]$, $r < R$.
No integrability at $R$ is needed or claimed.

*(2)* Fix $x = re$, $0 < r < R$. For $\theta \in \Sph{2}$, $\abs{r\inner{e}{\theta}} \le r$, and
$T$ is continuous, hence bounded, on $[-r,r]$: the integrand is bounded and continuous in
$\theta$. Write $\theta = s e + \theta_\perp$ with $s = \inner{e}{\theta}$ and
$\theta_\perp \perp e$. The rotation $O_e$ of angle $\pi$ about the axis $e$ maps
$\theta \mapsto s e - \theta_\perp$ and preserves $\sigma$; applying it,

$$
\int T(rs)\,\theta_\perp \dd\sigma(\theta) = -\int T(rs)\,\theta_\perp \dd\sigma(\theta) = 0 .
$$

By Archimedes, $s$ is uniform on $[-1,1]$ under $\sigma$, so
$\int T(r\inner{e}{\theta})\,\theta \dd\sigma(\theta) = \tfrac12 \int_{-1}^1 T(rs)\,s\dd s \; e =
\int_0^1 T(rs)\,s \dd s \; e$, because $s \mapsto T(rs)\,s$ is even ($T$ is odd). Substituting
$u = rs$ and using $3\int_0^r u^2 \dd u = r^3$,

$$
r - 3\int_0^1 T(rs)\,s\dd s = r - \frac{3}{r^2}\int_0^r T(u)\,u\dd u
= -\frac{3}{r^2}\int_0^r (T(u) - u)\,u \dd u = -\frac{3}{r^2}\,G(r).
$$


*(3)* By [](#lem:r3-monotone) (2), for every $\theta$ the set
$N_\theta = \{s : \bar\gamma_\theta(s) \ne \tilde T(s)\}$ satisfies $\mu_1(N_\theta) = 0$, where
$\tilde T$ is $T$ on $(-R,R)$, extended by $0$ elsewhere (a $\mu_1$-null set by
[](#lem:r3-monotone) (1)). As in every use of [](#def:barycentric-field), we read the definition
as providing a $\mu\otimes\sigma$-measurable version of
$(x,\theta) \mapsto \bar\gamma_\theta(\inner{x}{\theta})$, without which the integral defining
$v_\mu$ has no meaning. Then
$N = \{(x,\theta) : \bar\gamma_\theta(\inner{x}{\theta}) \ne \tilde T(\inner{x}{\theta})\}$ is
$\mu\otimes\sigma$-measurable, and by Tonelli

$$
(\mu\otimes\sigma)(N) = \int_{\Sph{2}} \mu\big(\{x : \inner{x}{\theta} \in N_\theta\}\big)\dd\sigma(\theta)
= \int_{\Sph{2}} \mu_\theta(N_\theta) \dd\sigma(\theta) = 0 .
$$

So for $\mu$-a.e. $x$, $\bar\gamma_\theta(\inner{x}{\theta}) = \tilde T(\inner{x}{\theta})$ for
$\sigma$-a.e. $\theta$. For such an $x$ with $0 < \abs{x} < R$, $\abs{\inner{x}{\theta}} < R$ for
every $\theta$, so $\tilde T(\inner{x}{\theta}) = T(\inner{x}{\theta})$ and $v_\mu(x) = V(x)$. The
same argument shows that $v_\mu$ does not depend, up to a $\mu$-null set, on the version chosen.

*(4)* Let $Z = \{r \in (0,R) : G(r) \ne 0\}$, an open set by (1). By [](#eq-r3-reduction),
for $0 < \abs{x} < R$, $V(x) = 0$ iff $G(\abs{x}) = 0$. Hence, by (3) and criticality,

$$
\mu_{\mathrm{rad}}(Z) = \mu\big(\{x : 0 < \abs{x} < R,\ V(x) \ne 0\}\big)
= \mu\big(\{x : 0 < \abs{x} < R,\ v_\mu(x) \ne 0\}\big) = 0 .
$$

An open set of $\mu_{\mathrm{rad}}$-measure zero does not meet $K = \operatorname{supp}\mu_{\mathrm{rad}}$.
So $G = 0$ on $K \cap (0,R)$, and $G(0) = 0$.

Nothing is evaluated at $\abs{x} = R$: if $R < \infty$ and $\mu_{\mathrm{rad}}$ has an atom at $R$,
the condition on that sphere is simply not used.
:::

## The radial support

:::{prf:lemma} Structure of the radial support
:label: lem:r3-support
Assume (H).

1. $0 < R \le \infty$, and $R \in K$ if $R < \infty$.
2. Every $r \in K \cap (0,R)$ is the limit of a sequence $(r_n)$ of points of
   $K \cap (0,R) \setminus \{r\}$.
3. The open set $(0,R) \setminus K$ is the disjoint union of at most countably many open
   intervals $(a,b)$, its connected components, and each of them satisfies
   $0 \le a < b < R$, $b \in K$, $\mu_{\mathrm{rad}}((a,b)) = 0$, and $a \in K$ if $a > 0$.
:::

:::{prf:proof}
:class: dropdown
*(1)* $R > 0$ was noted before [](#lem:r3-monotone); $K$ is closed, so it contains its finite
supremum.

*(2)* $r$ is not isolated in $K$, so there are $r_n \in K \setminus \{r\}$ with $r_n \to r$; since
$(0,R)$ is an open neighbourhood of $r$, $r_n \in (0,R)$ for $n$ large.

*(3)* $(0,R) \setminus K$ is open in $\R$, hence a disjoint union of open intervals, its
components, each containing a rational, so at most countably many. Let $(a,b)$ be one, with
$0 \le a < b \le R$. Suppose $b = R$. If $R = \infty$, $K \cap (a,\infty) = \emptyset$
contradicts $\sup K = \infty$. If $R < \infty$, then $K \cap (a, \infty) = \{R\}$ (as
$K \subset [0,R]$), so $R$ is an isolated point of $K$, contradicting (H). Hence $b < R$. By
maximality of the component, $b \notin (0,R) \setminus K$, and $b \in (0,R)$, so $b \in K$;
likewise $a \in K$ if $a > 0$. Finally $(a,b)$ is open and disjoint from $K$, so
$\mu_{\mathrm{rad}}((a,b)) = 0$.
:::

## Proof of the theorem

:::{prf:proof}
Assume (H) and that $\mu$ is a critical point. Let $T$, $h = T - \Id$ and $G$ be as in
[](#lem:r3-monotone) and [](#lem:r3-reduction). By [](#lem:r3-reduction) (4),

$$
G = 0 \quad \text{on } K \cap [0,R).
$$ (eq-r3-star)

*Step A: $T = \Id$ on $K \cap (0,R)$.* Let $r \in K \cap (0,R)$, and let $r_n \to r$ be as in
[](#lem:r3-support) (2). By [](#eq-r3-star), $G(r_n) = G(r) = 0$. Since $G$ is differentiable at $r$
([](#lem:r3-reduction) (1)),

$$
h(r)\,r = G'(r) = \lim_{n\to\infty} \frac{G(r_n) - G(r)}{r_n - r} = 0 ,
$$

and $r > 0$, so $T(r) = r$. This is the only place where the absence of isolated points of $K$
enters, together with $b < R$ in [](#lem:r3-support) (3).

*Step B: $T = \Id$ on every hole.* Let $(a,b)$ be a component of $(0,R) \setminus K$, as in
[](#lem:r3-support) (3): $0 \le a < b < R$ and $\mu_{\mathrm{rad}}((a,b)) = 0$.

- By [](#lem:r3-monotone) (3), $T$, hence $h$, is convex on $[a,b]$.
- $h(b) = 0$ by Step A, since $b \in K \cap (0,R)$. $h(a) = 0$: by Step A if $a > 0$ (then
  $a \in K \cap (0,R)$), and by $T(0) = 0$ ([](#lem:r3-monotone) (2)) if $a = 0$.
- A convex function lies below its chord: for $u \in [a,b]$,
  $h(u) \le \frac{b-u}{b-a}h(a) + \frac{u-a}{b-a}h(b) = 0$.
- $G(a) = 0$ (by [](#eq-r3-star) if $a > 0$, and $G(0) = 0$) and $G(b) = 0$ by [](#eq-r3-star). Hence

  $$
  \int_a^b h(u)\,u \dd u = G(b) - G(a) = 0 .
  $$

  The integrand $h(u)\,u$ is continuous and $\le 0$ on $[a,b]$, so it vanishes identically
  there; since $u > 0$ on $(a,b]$, $h = 0$ on $(a,b]$, and $h(a) = 0$ was shown.

The convexity alone gives only $h \le 0$; it is the integral condition across the hole that
gives $h = 0$.

*Step C: $T = \Id$ on $(-R,R)$.* Every point of $[0,R)$ is $0$, or lies in $K \cap (0,R)$, or in
a component of $(0,R) \setminus K$. Steps A and B and $T(0) = 0$ give $T = \Id$ on $[0,R)$, and
oddness ([](#lem:r3-monotone) (2)) gives $T = \Id$ on $(-R,R)$. The components are handled
independently of one another, whatever their number and their arrangement.

*Step D: conclusion.* By [](#lem:r3-monotone) (1)–(2), $\mu_1((-R,R)) = 1$ and
$\rho_1 = T_\#\mu_1 = \mu_1$. By [](#lem:r3-projections) (1), $\mu_\theta = \mu_1 = \rho_1 = \rho_\theta$
for every $\theta \in \Sph{2}$. Then for every $t \in \R$ and $\theta \in \Sph{2}$ the
characteristic functions satisfy $\hat\mu(t\theta) = \hat\mu_\theta(t) = \hat\rho_\theta(t) = \hat\rho(t\theta)$,
so $\hat\mu = \hat\rho$ and $\mu = \rho$ (Cramér–Wold).
:::

## Remarks

:::{prf:remark} Where the hypotheses are used
:label: rem:r3-hypotheses
- $\mu(\{0\}) = 0$ is used in [](#lem:r3-monotone) (1): with it, $\mu_1$ has no atom, so
  $\bar\gamma_\theta = T$ (the definition's one-dimensional fact) and $F_1(0) = \tfrac12$, whence
  $T(0) = 0$, which Step B uses for the hole adjacent to $0$.
- "$K$ has no isolated point" is used in Step A (through [](#lem:r3-support) (2)) and in
  [](#lem:r3-support) (3) ($b < R$: no hole reaches the end of the radial support, so every hole
  is closed by a point where Step A applies and $T$ is finite). It also gives $R > 0$.
- Atoms of $\mu_{\mathrm{rad}}$ at points of $(0,\infty)$ that are not isolated in $K$ are
  allowed: for instance $\mu_{\mathrm{rad}} = \tfrac12\delta_1 + \tfrac12\mathrm{U}[1,2]$, a
  measure that is not absolutely continuous, is covered. Their projections are still
  atomless. This is the sharpening over [](#thm:radial-d3).
- On $\rho$: only rotation invariance and $\rho \in \Ptwo{3}$ (for [](#def:barycentric-field)
  to apply) are used. An atom $\rho_0 > 0$ at the origin only adds the flat piece
  $Q = 0$ on $[\tfrac12, \tfrac{1+\rho_0}{2}]$ in [](#lem:r3-quantile) (3), which keeps $Q$ convex
  on $[\tfrac12,1)$. Absolute continuity of $\rho$ is not used.
- Absolute continuity of $\mu$ is used nowhere directly; it implies (H), since each sphere is
  Lebesgue-null, so $\mu_{\mathrm{rad}}$ has no atom.
:::

:::{prf:remark} Audit: the critical sphere
:label: rem:r3-sphere-audit
Let $\mu$ be the uniform probability on $r\Sph{2}$ and $\rho = N(0, I_3)$, the configuration of
[](#prop:critical-sphere), worked by hand in [](#sec:overview) (critical for $r = 3/\sqrt\pi$).
Here $\mu_{\mathrm{rad}} = \delta_r$, $K = \{r\}$, $R = r$. Run the argument on it.

- $\mu(\{0\}) = 0$ holds, and [](#lem:r3-projections), [](#lem:r3-quantile) and
  [](#lem:r3-monotone) (1)–(2) hold, their proofs using of (H) only $\mu(\{0\}) = 0$ and $R > 0$: $\mu_1 = \mathrm{U}[-r,r]$ is atomless — the sphere
  has absolutely continuous projections — and $T(u) = \Phi^{-1}\big(\tfrac{1 + u/r}{2}\big)$ on
  $(-r,r)$, with $\Phi$ the standard normal distribution function. [](#lem:r3-monotone) (3)
  holds on $[0,b]$ for every $b < r$: $T$ is convex there.
- [](#lem:r3-reduction) (1)–(3) hold but concern only the set $\{0 < \abs{x} < R\}$, which is
  $\mu$-null, and (4)
  yields nothing, since $K \cap [0,R) = \emptyset$. The criticality condition lives entirely on
  $\abs{x} = R$, which the proof never uses (see the end of the proof of [](#lem:r3-reduction)).
  There it reads $\int_0^1 \Phi^{-1}\big(\tfrac{1+s}{2}\big)\,s\dd s = r/3$, an improper integral,
  which [](#sec:overview) solves.
- The argument **breaks exactly at the hypothesis "$K$ has no isolated point"**: $r$ is
  isolated, so [](#lem:r3-support) (3) fails — the only component of $(0,R) \setminus K$ is
  $(0,R)$ itself, with $b = R$ — and Step A has no point to act on. Step B on $(0,R)$ would need
  $h(R) = 0$, whereas $T(u) \to +\infty$ as $u \uparrow r$.
- Atomlessness of the projections $\mu_\theta$ is therefore not what excludes the sphere; the
  hypothesis that bites is on the radial support, which absolute continuity of $\mu$ (or
  atomlessness of $\mu_{\mathrm{rad}}$) guarantees.

*The earlier error.* A sketch of this theorem asserted $T = \Id$ at both ends of every hole on
the ground that $G(a) = G(b) = 0$, and then concluded from convexity alone. Applied to the
sphere, it asserts $T(r) = r$ at the end of the hole $(0,r)$, and so "proves" that the sphere
is not critical, which is false. Here the endpoint values come only from Step A, which needs the
endpoint to be a non-isolated point of $K$ inside $(0,R)$, and the passage from $h \le 0$ to
$h = 0$ uses the integral condition $G(b) - G(a) = 0$. Nothing in the proof rests on
[](#prop:critical-sphere), which is proved separately: this remark is a consistency check.
:::

:::{prf:remark} Audit: an atom at the origin
:label: rem:r3-atom-origin
$\delta_0$ is a critical point for every rotation-invariant $\rho \in \Ptwo{3}$: its projections are
$\delta_0$, the only plan is $\delta_0\otimes\rho_1$, so $\bar\gamma_\theta(0) = \int t\dd\rho_1(t) = 0$
by symmetry, and $v_{\delta_0}(0) = 0$. It differs from $\rho$ unless $\rho = \delta_0$. (H) excludes
it twice: $\mu(\{0\}) = 1$, and $K = \{0\}$ is a single isolated point.

For $\mu = p\,\delta_0 + (1-p)\nu$ with $0 < p < 1$ and $\nu$ radial, $\mu_1$ has an atom at $0$, so
[](#lem:r3-monotone) (1) fails, $\bar\gamma_\theta$ is not $T$ at $0$, and the map relevant on
$u \ne 0$ has right limit $Q_{\rho_1}(\tfrac{1+p}{2}) \ge 0$ at $0$, possibly positive. Step B for
the hole adjacent to $0$ then loses the sign of the chord. We neither prove nor exclude that
such mixtures can be critical: they are outside (H) and outside [](#thm:radial-d3), and nothing is
claimed about them here.
:::

:::{prf:remark} Fat Cantor and singular radial supports; unbounded supports
:label: rem:r3-cantor-unbounded
- *Fat Cantor supports.* Let $K \subset [1,2]$ be a closed set with no interior and positive
  Lebesgue measure, every relatively open subset of which has positive Lebesgue measure (a
  Smith–Volterra–Cantor set, for instance), and $\mu_{\mathrm{rad}}$ the normalized Lebesgue measure on $K$. Then $\mu$ is
  absolutely continuous, with density proportional to $\one_K(\abs{x})\,\abs{x}^{-2}$, and
  $(0,R) \setminus K$ consists of $(0,\min K)$ and countably many holes, dense in $[\min K, \max K]$. The proof
  applies unchanged: Step A is pointwise on $K \cap (0,R)$, and Step B treats each component
  separately, using only its two endpoints, which lie in $K \cap (0,R)$ or equal $0$
  ([](#lem:r3-support) (3)). No ordering of the holes, induction, or interior point of $K$ is
  used. The same holds when $\mu_{\mathrm{rad}}$ is a singular continuous measure on a
  Lebesgue-null Cantor set: $\mu$ is then singular, and still covered.
- *Unbounded supports.* $R = \infty$ and $S = \infty$ are allowed. Then $T$ is finite and
  continuous on all of $\R$ (it may be unbounded), $G$ is finite on $[0,\infty)$, and no component
  of $(0,R)\setminus K$ is unbounded ([](#lem:r3-support) (3)). When $R < \infty$, $G$ is
  evaluated only at points $r < R$, where $T$ is bounded on $[0,r]$; no integrability of $h$
  near $R$ is used, and $T$ may blow up at $R$ (as for a Gaussian $\rho$).
:::

:::{prf:remark} What is special to dimension three; the segment test
:label: rem:r3-dimension
Archimedes' theorem is used twice, and both uses are specific to $d = 3$. In
[](#lem:r3-reduction) (2), $\inner{e}{\theta}$ is uniform under $\sigma$, so the condition is the
vanishing of a primitive $G$ — a *local* condition, which Step A differentiates. In
[](#lem:r3-projections) (3), the projection of a sphere is uniform, so $f$ is constant on the
holes and $T$ is convex there, which Step B uses. In dimension $d$ the weight of
$\inner{e}{\theta}$ is proportional to $(1-s^2)^{(d-3)/2}$ and the projection of a sphere has
density proportional to $(r^2 - u^2)^{(d-3)/2}$; neither step survives as written, and nothing
is claimed for $d \ne 3$.

The critical points of [](#prop:critical-segments) are not invariant under rotations of $\R^3$
(they are carried by a line, or live in $\R^2$), so they are outside the theorem's scope and do
not test it.
:::

**Consistency with the known critical points.** [](#prop:critical-sphere) (proved) exhibits a rotation-invariant critical point for
$\rho = N(0, I_3)$ whose radial law is an atom at an isolated point of its support; (H) excludes
it, and [](#rem:r3-sphere-audit) locates the steps it defeats. [](#prop:critical-segments)
(proved) concerns measures carried by a line, not rotation-invariant in $\R^3$, so it is outside
the hypotheses ([](#rem:r3-dimension)).
