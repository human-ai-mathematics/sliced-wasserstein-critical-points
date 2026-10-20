---
title: "Radial measures on a full disc in the plane"
ledger-node: thm:radial-disc-d2
numbering:
  enumerator: "4.%s"
---

% Proof dossier for thm:radial-disc-d2 (route ap:certify-scouting, lens prove). Uncertified
% draft until a proofs[] record in the ledger names it. Reproved from scratch; the scouting
% notes ensae-conjecture-scouting/verification/13-korba-sw/A-radial-d2.md (§1, §2 (P1), (P3))
% and 1-relecture.md (§4) were read for the idea only and are not cited as authority.
% Normalizations: def:sliced-wasserstein (sigma a probability) and def:barycentric-field
% (factor d = 2 in v_mu).

**Overview.** We prove [](#thm:radial-disc-d2) in a sharper form, [](#thm:sol-rd2-main):
absolute continuity of $\mu$ is replaced by $\mu(\{0\}) = 0$; $\rho$ is an arbitrary radial
measure of $\Ptwo{2}$ (no density, atoms allowed, unbounded support allowed); the disc may
have any radius $R \in (0,\infty)$, or be the whole plane ($R = \infty$). A local version,
[](#prop:sol-rd2-local), shows that the monotone map is the identity on $(-a,a)$ as soon as
the open disc $B(0,a)$ lies in the support of $\mu$. The steps are:

1. *Projections of radial measures* ([](#lem:sol-rd2-projection)). All projections of a
   radial $\mu$ are one symmetric law $\mu_1$, which has no atom if and only if
   $\mu(\{0\}) = 0$, and $\mu_1$ determines $\mu$.
2. *The monotone map* ([](#lem:sol-rd2-monotone)). $T = Q_{\rho_1} \circ F_{\mu_1}$ is finite
   and nondecreasing on $(-R,R)$, pushes $\mu_1$ to $\rho_1$, and is odd on $(-a,a)$ outside a
   countable set.
3. *A continuous version of the field* ([](#lem:sol-rd2-continuous)). The barycentric field
   agrees $\mu$-a.e. on $B(0,R)$ with a field $v$ continuous on $B(0,R) \setminus \{0\}$; at a
   critical point, $v = 0$ on all of $B(0,a) \setminus \{0\}$, not only $\mu$-a.e. This is
   where the support hypothesis enters first.
4. *Radial reduction* ([](#lem:sol-rd2-reduction)). With $h = T - \Id$ and
   $U(\tau) = h(\sqrt\tau)$, $v(r e_1) = -\frac{2}{\pi r}\, A[U](r^2)\, e_1$ for $0 < r < a$,
   where $A[U](x) = \int_0^x U(\tau)(x-\tau)^{-1/2} \dd\tau$ is the Abel transform.
5. *Injectivity of the Abel transform* ([](#lem:sol-rd2-abel)), proved in full in
   $L^1_{\mathrm{loc}}([0,X))$: if $A[U] = 0$ a.e. on $(0,X)$, then $U = 0$ a.e. on $(0,X)$.
   It is applied with $X = a^2$ and $U \in L^\infty_{\mathrm{loc}}([0,a^2))$. This is where the
   support hypothesis enters a second time: the equation must hold on an interval
   *starting at $0$*.
6. *Conclusion.* $T = \Id$ on $(-a,a)$; with $a = R$, $\rho_1 = T_\#\mu_1 = \mu_1$, and
   $\rho = \mu$ by step 1.

The remarks run the audit tests of the brief: the critical circle
([](#rem:sol-rd2-circle)), an atom at $0$ ([](#rem:sol-rd2-atom)), the annulus
([](#rem:sol-rd2-annulus)), irregular and unbounded data ([](#rem:sol-rd2-irregular)); and
compare the result with [](#thm:bonnotte-full-support) ([](#rem:sol-rd2-bonnotte)).

**Dependencies.** The definitions [](#def:sliced-wasserstein), [](#def:barycentric-field) and
[](#def:critical-point), including the identification $\bar\gamma_\theta = T_\theta$
$\mu_\theta$-a.e. when $\mu_\theta$ has no atom, which is part of
[](#def:barycentric-field). No other node of the manuscript is used in the proof:
[](#thm:bonnotte-full-support), [](#prop:critical-sphere) and the other nodes named below
appear only in remarks. Literature results used, all classical: Fubini–Tonelli; Lebesgue's
differentiation theorem (a locally integrable function whose integral over every interval
vanishes is zero a.e.); uniqueness of a finite Borel measure on $\R^2$ given its Fourier
transform; Euler's Beta integral $\int_0^1 u^{-1/2}(1-u)^{-1/2} \dd u = \pi$. The injectivity
of the Abel transform is classical (it is the uniqueness half of Abel's inversion of the
half-integral); it is proved in full below rather than cited.

## Conventions

A measure $\nu$ on $\R^2$ is *radial* when $R_\#\nu = \nu$ for every rotation $R \in SO(2)$.
We write $e_1 = (1,0)$, $B(0,a) = \{\abs{x} < a\}$ (with $B(0,\infty) = \R^2$), and
$\overline B(0,R)$ for the closed disc. For a Borel probability $\alpha$ on $\R$,
$F_\alpha(s) = \alpha((-\infty,s])$, $F_\alpha(s^-) = \alpha((-\infty,s))$, and
$Q_\alpha(u) = \inf\{s \in \R : F_\alpha(s) \ge u\}$ for $u \in (0,1)$, a finite number. In
[](#def:barycentric-field) the quantile function is not pinned down; we use this
left-continuous version, which is the one for which the facts below are written; any other
version differs from it at countably many $u$ only, which changes $T_\theta$ on a
$\mu_\theta$-null set when $\mu_\theta$ has no atom, and so does not change $v_\mu$
$\mu$-a.e. (see the proof of [](#lem:sol-rd2-continuous)).

- **(Q1)** For $u \in (0,1)$ and $s \in \R$: $Q_\alpha(u) \le s \iff u \le F_\alpha(s)$. Hence
  $F_\alpha(Q_\alpha(u)^-) \le u \le F_\alpha(Q_\alpha(u))$, and if $V$ is uniform on $(0,1)$,
  $Q_\alpha(V)$ has law $\alpha$.
- **(Q2)** If $\alpha$ has no atom and $S$ has law $\alpha$, then $F_\alpha(S)$ is uniform on
  $(0,1)$.

:::{prf:proof}
:class: dropdown
(Q1) If $u \le F_\alpha(s)$, then $s$ belongs to the set whose infimum is $Q_\alpha(u)$, so
$Q_\alpha(u) \le s$. Conversely, if $Q_\alpha(u) \le s$, then for every $t > s$ there is
$t' < t$ with $F_\alpha(t') \ge u$, so $F_\alpha(t) \ge u$; right continuity of $F_\alpha$ gives
$F_\alpha(s) \ge u$. Taking $s = Q_\alpha(u)$ gives $u \le F_\alpha(Q_\alpha(u))$; for
$t < Q_\alpha(u)$ the equivalence gives $F_\alpha(t) < u$, hence $F_\alpha(Q_\alpha(u)^-) \le u$.
Finally $\Prob(Q_\alpha(V) \le s) = \Prob(V \le F_\alpha(s)) = F_\alpha(s)$.

(Q2) $F_\alpha$ is continuous, so by (Q1) $F_\alpha(Q_\alpha(u)) = u$ for $u \in (0,1)$. By
(Q1) again, for $u \in (0,1)$, $\Prob(F_\alpha(S) \ge u) = \Prob(S \ge Q_\alpha(u)) =
1 - F_\alpha(Q_\alpha(u)^-) = 1 - F_\alpha(Q_\alpha(u)) = 1 - u$.
:::

## Refined statement

:::{prf:theorem} Radial measures on a full disc, refined
:label: thm:sol-rd2-main
Let $\rho \in \Ptwo{2}$ be radial. Let $\mu \in \Ptwo{2}$ be radial, with $\mu(\{0\}) = 0$, and
with support either $\overline B(0,R)$ for some $R \in (0,\infty)$, or $\R^2$. If $\mu$ is a
critical point of $\SW_2^2(\cdot,\rho)$ ([](#def:critical-point)), then $\mu = \rho$.
:::

This implies [](#thm:radial-disc-d2): an absolutely continuous $\mu$ has $\mu(\{0\}) = 0$, and
its support, a closed disc centred at $0$ or the plane, is not $\{0\}$, so the disc has a
radius $R > 0$. No hypothesis on $\rho$ beyond radial symmetry and a finite second moment is
used; no density of $\mu$ is used either.

:::{prf:proposition} The local statement
:label: prop:sol-rd2-local
Let $\rho, \mu \in \Ptwo{2}$ be radial with $\mu(\{0\}) = 0$ and $\mu \ne \delta_0$, let
$R = \sup\{\abs{x} : x \in \operatorname{supp}\mu\} \in (0,\infty]$, and let
$T = Q_{\rho_1} \circ F_{\mu_1}$ as in [](#lem:sol-rd2-monotone). Assume that
$B(0,a) \subset \operatorname{supp}\mu$ for some $a \in (0,R]$. If $\mu$ is a critical point
of $\SW_2^2(\cdot,\rho)$, then $T(s) = s$ for every $s \in (-a,a)$.
:::

(The hypothesis $\mu \ne \delta_0$ is implied by $\mu(\{0\}) = 0$; it is written to make
$R > 0$ visible.)

## Lemmas

:::{prf:lemma} Projections of radial measures
:label: lem:sol-rd2-projection
Let $\nu$ be a radial Borel probability on $\R^2$ and $\nu_1 = (P_{e_1})_\#\nu$.

1. $\nu_\theta = \nu_1$ for every $\theta \in \Sph{1}$, and $\nu_1$ is symmetric:
   $\nu_1(-B) = \nu_1(B)$ for every Borel $B \subset \R$.
2. For every $t \in \R$, $\nu_1(\{t\}) = \nu(\{0\})\,\one_{t = 0}$. In particular $\nu_1$ has no
   atom if and only if $\nu(\{0\}) = 0$.
3. If $\nu'$ is another radial Borel probability on $\R^2$ with $\nu'_1 = \nu_1$, then
   $\nu' = \nu$.
4. $\operatorname{supp}\nu$ is invariant under rotations.
:::

:::{prf:proof}
1. For $\theta \in \Sph{1}$ let $R_\theta \in SO(2)$ with $R_\theta e_1 = \theta$. Then
   $P_\theta(x) = \inner{x}{R_\theta e_1} = P_{e_1}(R_\theta^{-1} x)$, so
   $\nu_\theta = (P_{e_1})_\#(R_\theta^{-1})_\#\nu = (P_{e_1})_\#\nu = \nu_1$. The rotation by
   $\pi$ is $-\Id$, so $(-\Id)_\#\nu = \nu$ and $\nu_1 = (-1)_\#\nu_1$.
2. Let $\lambda_r$ be the uniform probability on the circle $\{\abs{x} = r\}$ for $r > 0$, and
   $\lambda_0 = \delta_0$. Let $m$ be the Haar probability of $SO(2)$. Since $\nu$ is radial,
   for every Borel $B \subset \R^2$,
   $\nu(B) = \int_{SO(2)} \nu(R^{-1}B) \dd m(R) = \int_{\R^2} \int_{SO(2)} \one_B(Rx) \dd m(R)
   \dd\nu(x) = \int_{\R^2} \lambda_{\abs{x}}(B) \dd\nu(x)$ (Tonelli, and the image of $m$ under
   $R \mapsto Rx$ is $\lambda_{\abs{x}}$). Take $B = \{x : x_1 = t\}$. For $\abs{x} > 0$, $B$
   meets the circle of radius $\abs{x}$ in at most two points, so $\lambda_{\abs{x}}(B) = 0$;
   and $\lambda_0(B) = \one_{t=0}$. Hence $\nu_1(\{t\}) = \nu(B) = \nu(\{0\})\one_{t=0}$.
3. For $\xi = t\theta$ with $t \in \R$ and $\theta \in \Sph{1}$,
   $\hat\nu(\xi) = \int e^{i t \inner{x}{\theta}} \dd\nu(x) = \int e^{its} \dd\nu_\theta(s)
   = \hat\nu_1(t)$, by part 1. So $\hat\nu' = \hat\nu$ on $\R^2$, and $\nu' = \nu$ by uniqueness
   of the Fourier transform of finite Borel measures.
4. $x \notin \operatorname{supp}\nu$ iff some open ball $B'$ around $x$ has $\nu(B') = 0$; then
   $RB'$ is an open ball around $Rx$ with $\nu(RB') = \nu(B') = 0$.
:::

From now on, $\rho, \mu \in \Ptwo{2}$ are radial, $\mu(\{0\}) = 0$, $\mu \ne \delta_0$,
$R = \sup\{\abs{x} : x \in \operatorname{supp}\mu\} \in (0,\infty]$, and $a \in (0,R]$ with
$B(0,a) \subset \operatorname{supp}\mu$, as in [](#prop:sol-rd2-local). We write
$\mu_1, \rho_1$ for the common projections, $F = F_{\mu_1}$, $Q = Q_{\rho_1}$.

:::{prf:lemma} The monotone map
:label: lem:sol-rd2-monotone
1. $F$ is continuous on $\R$, $0 < F(s) < 1$ for $s \in (-R,R)$, and $F$ is strictly
   increasing on $(-a,a)$.
2. The map $T = Q \circ F : (-R,R) \to \R$ is finite and nondecreasing; for every $r < R$ it is
   bounded on $[-r,r]$; its set $D$ of discontinuity points is countable; and
   $T_\#\mu_1 = \rho_1$ (note $\mu_1((-R,R)) = 1$).
3. There is a countable set $E \subset (-a,a)$ such that $T(-s) = -T(s)$ for every
   $s \in (-a,a) \setminus E$.
4. For every $\theta \in \Sph{1}$, $T_\theta = T$ on $(-R,R)$, where $T_\theta =
   Q_{\rho_\theta} \circ F_{\mu_\theta}$ is the map of [](#def:barycentric-field).
:::

:::{prf:proof}
1. Continuity: $\mu_1$ has no atom ([](#lem:sol-rd2-projection), part 2). Let
   $s \in (-R,R)$. There is $x \in \operatorname{supp}\mu$ with $\abs{x} > \abs{s}$; by
   [](#lem:sol-rd2-projection), part 4, the points $(\pm\abs{x}, 0)$ lie in
   $\operatorname{supp}\mu$. The open half-planes $\{x_1 > s\}$ and $\{x_1 < s\}$ contain
   respectively $(\abs{x},0)$ and $(-\abs{x},0)$, so they have positive $\mu$-measure: an open
   set meeting the support has positive measure. Hence $1 - F(s) = \mu_1((s,\infty)) > 0$ and
   $F(s) \ge \mu_1((-\infty,s)) > 0$. If $-a < s < s' < a$, the open strip
   $\{s < x_1 < s'\}$ contains $((s+s')/2, 0) \in B(0,a) \subset \operatorname{supp}\mu$, so
   $F(s') - F(s) = \mu_1((s,s']) > 0$.
2. By part 1, $F(s) \in (0,1)$ on $(-R,R)$, where $Q$ is finite; $Q$ and $F$ are
   nondecreasing, hence so is $T$, and a nondecreasing real function on an interval has
   countably many discontinuities and is bounded on each compact subinterval $[-r,r]$
   (by $\max(\abs{T(-r)},\abs{T(r)})$). If $R < \infty$, $\mu_1$ is carried by $[-R,R]$
   (as $\mu$ is carried by $\overline B(0,R)$) and $\mu_1(\{\pm R\}) = 0$; so
   $\mu_1((-R,R)) = 1$ in all cases. Let $S$ have law $\mu_1$. By (Q2), $F(S)$ is uniform on
   $(0,1)$; by (Q1), $T(S) = Q(F(S))$ has law $\rho_1$.
3. *Symmetry of $F$.* For every $s$, $F(-s) = \mu_1((-\infty,-s]) = \mu_1([s,\infty)) =
   1 - F(s^-) = 1 - F(s)$, by symmetry of $\mu_1$ and continuity of $F$.

   *Symmetry of $Q$.* Write $G = F_{\rho_1}$ and $Q^+(u) = \sup\{t : G(t) \le u\}$ for
   $u \in (0,1)$, a finite number. By symmetry of $\rho_1$,
   $G(t) = \rho_1([-t,\infty)) = 1 - G((-t)^-)$. Hence $G(t) \ge 1-u \iff G((-t)^-) \le u$, and
   $Q(1-u) = \inf\{t : G((-t)^-) \le u\} = -\sup\{w : G(w^-) \le u\}$. The last supremum is
   $Q^+(u)$: if $G(w) \le u$ then $G(w^-) \le u$; if $G(w^-) \le u$ then $G(w') \le u$ for
   every $w' < w$, so $Q^+(u) \ge w$. Thus $Q(1-u) = -Q^+(u)$ for all $u \in (0,1)$.

   *$Q = Q^+$ off a countable set.* $Q(u) \le Q^+(u)$: if $Q^+(u) < t < Q(u)$, then
   $G(t) < u$ by (Q1) and $G(t) > u$ by definition of $Q^+$, a contradiction. If
   $Q(u) < Q^+(u)$, then for $t \in (Q(u), Q^+(u))$ we have $G(t) \ge u$ by (Q1) and
   $G(t) \le u$ (there is $t' > t$ with $G(t') \le u$); so $G = u$ on the nonempty open
   interval $(Q(u),Q^+(u))$. These intervals are pairwise disjoint for distinct $u$, so the
   set $C = \{u : Q(u) \ne Q^+(u)\}$ is countable.

   *Conclusion.* For $s \in (-a,a)$, $T(-s) = Q(1 - F(s)) = -Q^+(F(s))$, which equals
   $-Q(F(s)) = -T(s)$ unless $F(s) \in C$. Since $F$ is injective on $(-a,a)$ (part 1),
   $E = \{s \in (-a,a) : F(s) \in C\}$ is countable.
4. $\mu_\theta = \mu_1$ and $\rho_\theta = \rho_1$ by [](#lem:sol-rd2-projection), part 1.
:::

:::{prf:lemma} A continuous version of the field
:label: lem:sol-rd2-continuous
For $x \in B(0,R)$ put

$$
v(x) = x - 2 \int_{\Sph{1}} T(\inner{x}{\theta})\,\theta \dd\sigma(\theta).
$$

1. The integral converges absolutely for every $x \in B(0,R)$, and $v$ is continuous on
   $B(0,R) \setminus \{0\}$.
2. $v = v_\mu$ $\mu$-almost everywhere on $B(0,R)$, where $v_\mu$ is the barycentric field of
   $\mu$ relative to $\rho$ ([](#def:barycentric-field)), computed with any version of
   $(\theta,s) \mapsto \bar\gamma_\theta(s)$ that is jointly Borel.
3. If $\mu$ is a critical point of $\SW_2^2(\cdot,\rho)$, then $v(x) = 0$ for every
   $x \in B(0,a) \setminus \{0\}$.
:::

:::{prf:proof}
1. If $\abs{x} \le r < R$, then $\inner{x}{\theta} \in [-r,r]$, where $\abs{T} \le M_r$ by
   [](#lem:sol-rd2-monotone), part 2: the integrand is bounded by $M_r$. Let
   $x \in B(0,R) \setminus \{0\}$ and $x_n \to x$; choose $r$ with $\abs{x} < r < R$, so that
   $\abs{x_n} \le r$ for $n$ large. For each $t \in \R$ the equation $\inner{x}{\theta} = t$ has
   at most two solutions $\theta \in \Sph{1}$, because $x \ne 0$; as $D$ is countable, the set
   $\{\theta : \inner{x}{\theta} \in D\}$ is countable, hence $\sigma$-null. For every other
   $\theta$, $T(\inner{x_n}{\theta}) \to T(\inner{x}{\theta})$. Dominated convergence (bound
   $M_r$) gives $v(x_n) \to v(x)$.
2. By [](#def:barycentric-field) and [](#lem:sol-rd2-monotone), parts 1 and 4: $\mu_\theta = \mu_1$
   has no atom, so $\bar\gamma_\theta = T_\theta = T$ $\mu_1$-a.e., for every $\theta$. Let
   $g(\theta,s)$ be a jointly Borel version, that is, $g(\theta,\cdot) = \bar\gamma_\theta$
   $\mu_\theta$-a.e. for every $\theta$. The set
   $N = \{(x,\theta) : \abs{x} < R,\ g(\theta,\inner{x}{\theta}) \ne T(\inner{x}{\theta})\}$ is
   Borel, and for each $\theta$ its section has $\mu$-measure at most
   $\mu_1(\{s \in (-R,R) : g(\theta,s) \ne T(s)\}) = 0$. By Tonelli, $(\mu \otimes \sigma)(N) = 0$,
   so for $\mu$-a.e. $x \in B(0,R)$ the two integrands agree for $\sigma$-a.e. $\theta$, the
   integral defining $v_\mu(x)$ converges absolutely (by part 1), and $v_\mu(x) = v(x)$.
   (Changing $Q$ at countably many points changes $T$ on the set where $F$ takes countably many
   values, which is $\mu_1$-null since $F_\#\mu_1$ is uniform; the same argument applies.)
3. Let $O = B(0,a) \setminus \{0\}$, an open set contained in $\operatorname{supp}\mu$, and
   $N' = \{x \in O : v(x) \ne 0\}$. By part 1, $N'$ is open; by part 2 and criticality,
   $\mu(N') = 0$. An open set of $\mu$-measure zero does not meet $\operatorname{supp}\mu$;
   since $N' \subset \operatorname{supp}\mu$, $N' = \emptyset$.
:::

:::{prf:lemma} Radial reduction: the Abel condition
:label: lem:sol-rd2-reduction
Let $h(s) = T(s) - s$ for $s \in (-R,R)$, and $U(\tau) = h(\sqrt\tau)$ for $\tau \in [0,R^2)$.
Then $U$ is Borel and bounded on $[0,y]$ for every $y < R^2$, and for every $r \in (0,a)$,

$$
v(r e_1) = -\frac{4}{\pi r} \left( \int_0^r h(s)\, s\, (r^2 - s^2)^{-1/2} \dd s \right) e_1
= -\frac{2}{\pi r}\, A[U](r^2)\, e_1,
\qquad
A[U](x) = \int_0^x \frac{U(\tau)}{\sqrt{x - \tau}} \dd\tau ,
$$

all integrals converging absolutely.
:::

:::{prf:proof}
$U$ is Borel ($T$ is monotone, $\sqrt\cdot$ continuous) and bounded on $[0,y]$ by
[](#lem:sol-rd2-monotone), part 2, applied with $r = \sqrt y$.

Parametrize $\theta = (\cos\varphi, \sin\varphi)$, so that $\sigma$ is $\dd\varphi/(2\pi)$ on
$[0,2\pi)$. Then $v(re_1) = re_1 - \frac1\pi \int_0^{2\pi} T(r\cos\varphi)(\cos\varphi,
\sin\varphi) \dd\varphi$, with a bounded integrand. Under $\varphi \mapsto 2\pi - \varphi$ the
cosine is unchanged and the sine changes sign, so the second component vanishes and the first
is $\frac2\pi \int_0^\pi T(r\cos\varphi)\cos\varphi \dd\varphi$. Since
$\frac2\pi\int_0^\pi r\cos^2\varphi \dd\varphi = r$,

$$
v(re_1) = -\frac2\pi \left(\int_0^\pi h(r\cos\varphi) \cos\varphi \dd\varphi\right) e_1 .
$$

Split at $\pi/2$ and substitute $\varphi \mapsto \pi - \varphi$ on $(\pi/2,\pi)$: that half
becomes $\int_0^{\pi/2} -h(-r\cos\varphi)\cos\varphi \dd\varphi$. Since $r < a$,
$r\cos\varphi \in [0,r] \subset (-a,a)$, and $h(-s) = -T(s) + s = -h(s)$ for
$s \in (-a,a) \setminus E$ ([](#lem:sol-rd2-monotone), part 3). The set of $\varphi$ with
$r\cos\varphi \in E$ is countable, so $\int_0^\pi h(r\cos\varphi)\cos\varphi \dd\varphi =
2\int_0^{\pi/2} h(r\cos\varphi)\cos\varphi \dd\varphi$. Substitute $s = r\cos\varphi$,
$\varphi \in (0,\pi/2)$, so $\cos\varphi = s/r$ and $\dd\varphi = -\dd s/\sqrt{r^2-s^2}$:

$$
\int_0^{\pi/2} h(r\cos\varphi)\cos\varphi \dd\varphi = \frac1r \int_0^r h(s)\,s\,(r^2-s^2)^{-1/2}
\dd s .
$$

This gives the first expression; the integral converges absolutely because $h$ is bounded on
$[0,r]$ and $\int_0^r s(r^2-s^2)^{-1/2} \dd s = r$. Finally substitute $\tau = s^2$,
$s \dd s = \dd\tau/2$: $\int_0^r h(s)\,s\,(r^2-s^2)^{-1/2} \dd s = \frac12 A[U](r^2)$.
:::

:::{prf:lemma} Injectivity of the Abel transform
:label: lem:sol-rd2-abel
Let $X \in (0,\infty]$ and let $U$ be a Borel function on $[0,X)$ with
$\int_0^y \abs{U} < \infty$ for every $y < X$. Then $A[U](x)$ converges absolutely for almost
every $x \in (0,X)$, and $A[U] \in L^1_{\mathrm{loc}}([0,X))$. If $A[U](x) = 0$ for almost every
$x \in (0,X)$, then $U = 0$ almost everywhere on $(0,X)$.
:::

:::{prf:proof}
Fix $y \in (0,X)$. By Tonelli,

$$
\int_0^y \int_0^x \frac{\abs{U(\tau)}}{\sqrt{x-\tau}} \dd\tau \dd x
= \int_0^y \abs{U(\tau)} \cdot 2\sqrt{y - \tau} \dd\tau \le 2\sqrt y \int_0^y \abs U < \infty,
$$

which gives the first two claims. Next, for $0 \le \tau < y$, the substitution
$x = \tau + (y-\tau)u$ gives

$$
\int_\tau^y \frac{\dd x}{\sqrt{(y-x)(x-\tau)}} = \int_0^1 \frac{\dd u}{\sqrt{u(1-u)}} = \pi .
$$

Hence, by Tonelli, $\int_0^y \int_0^x \abs{U(\tau)}\,(y-x)^{-1/2}(x-\tau)^{-1/2} \dd\tau \dd x =
\pi \int_0^y \abs U < \infty$, and Fubini applies:

$$
\int_0^y \frac{A[U](x)}{\sqrt{y-x}} \dd x
= \int_0^y U(\tau) \int_\tau^y \frac{\dd x}{\sqrt{(y-x)(x-\tau)}} \dd\tau
= \pi \int_0^y U(\tau) \dd\tau .
$$

If $A[U] = 0$ a.e. on $(0,X)$, the left side vanishes, so $\int_0^y U = 0$ for every
$y \in (0,X)$, hence $\int_I U = 0$ for every interval $I \subset (0,X)$. By Lebesgue's
differentiation theorem, $U(y) = \frac{\dd}{\dd y}\int_0^y U = 0$ for almost every
$y \in (0,X)$.
:::

The function space matters: the lemma is applied below to $U \in L^\infty_{\mathrm{loc}}([0,a^2))
\subset L^1_{\mathrm{loc}}([0,a^2))$, with no integrability near $a^2$ (nor at infinity when
$a = \infty$) and no continuity of $U$ (which may jump at the countably many discontinuities of
$T$). It is the Volterra structure that makes it local: $A[U]$ on $(0,y)$ depends only on $U$
on $(0,y)$, so the lemma on $(0,X)$ needs the hypothesis on $(0,X)$ only.

## Proofs of the statements

:::{prf:proof} of [](#prop:sol-rd2-local)
By [](#lem:sol-rd2-continuous), part 3, $v(re_1) = 0$ for every $r \in (0,a)$. By
[](#lem:sol-rd2-reduction), $A[U](x) = 0$ for every $x \in (0,a^2)$, with $U$ Borel and bounded
on each $[0,y]$, $y < a^2$. By [](#lem:sol-rd2-abel) with $X = a^2$, $U = 0$ a.e. on $(0,a^2)$.
Then $h = 0$ a.e. on $(0,a)$: indeed
$\Leb(\{s \in (0,a) : h(s) \ne 0\}) = \int_0^a \one_{U(s^2) \ne 0} \dd s
= \int_0^{a^2} \one_{U(\tau) \ne 0} \frac{\dd\tau}{2\sqrt\tau} = 0$.

So $T(s) = s$ on a dense subset of $(0,a)$. For $s \in (0,a)$ choose $s_n \uparrow s$ and
$s'_n \downarrow s$ in this subset; monotonicity gives $s_n = T(s_n) \le T(s) \le T(s'_n) = s'_n$,
so $T(s) = s$. For $s \in (-a,0) \setminus E$, [](#lem:sol-rd2-monotone), part 3, gives
$T(s) = -T(-s) = -(-s) = s$, since $-s \in (0,a)$. As $E$ is countable, this holds on a dense
subset of $(-a,0)$, and the same squeeze gives $T = \Id$ on $(-a,0)$.
Finally $-\varepsilon = T(-\varepsilon) \le T(0) \le T(\varepsilon) = \varepsilon$ for every
$\varepsilon \in (0,a)$, so $T(0) = 0$.
:::

:::{prf:proof} of [](#thm:sol-rd2-main)
Let $R \in (0,\infty]$ be the radius of the support ($R = \infty$ for the plane). Then
$R = \sup\{\abs{x} : x \in \operatorname{supp}\mu\}$ and $B(0,R) \subset \operatorname{supp}\mu$,
so [](#prop:sol-rd2-local) applies with $a = R$: $T = \Id$ on $(-R,R)$. By
[](#lem:sol-rd2-monotone), part 2, $\mu_1((-R,R)) = 1$ and $\rho_1 = T_\#\mu_1 = \mu_1$. By
[](#lem:sol-rd2-projection), part 3, $\rho = \mu$.
:::

## Remarks and audit tests

:::{prf:remark} Where each hypothesis is used
:label: rem:sol-rd2-hypotheses
- $\mu(\{0\}) = 0$: only through "$\mu_1$ has no atom"
  ([](#lem:sol-rd2-projection), part 2), which makes $F$ continuous, $\bar\gamma_\theta = T$,
  and $T_\#\mu_1 = \rho_1$ by (Q2).
- The support of $\mu$ is a full disc: twice. In [](#lem:sol-rd2-continuous), part 3, to pass
  from "$v = 0$ $\mu$-a.e." to "$v = 0$ at every point of $B(0,R) \setminus \{0\}$"; and in the
  application of [](#lem:sol-rd2-abel), which needs the Abel equation on an interval
  $(0,X)$ whose left end is $0$. It is also used in [](#lem:sol-rd2-monotone), part 1, for the
  strict monotonicity of $F$ (hence the countability of $E$).
- Absolute continuity of $\mu$, and any property of a density of $\mu$: not used.
- On $\rho$: radial symmetry only (for $\rho_\theta = \rho_1$, for the oddness of $T$, and in
  the final Fourier step); the finite second moment is needed only for the definitions.
  $\rho$ may be singular, have an atom at $0$, and be unbounded or supported outside the disc.
- $R = \infty$, and $T$ unbounded: only the boundedness of $T$ on each $[-r,r]$, $r < R$, is
  used; quantities at the edge $\abs{x} = R$ never enter. If $R < \infty$, $\mu$ may even
  charge the boundary circle $\{\abs{x} = R\}$ (for instance a mixture of the uniform
  measure on the disc and the uniform measure on its boundary): the theorem covers it.
:::

:::{prf:remark} Audit: the critical circle
:label: rem:sol-rd2-circle
Let $\mu$ be the uniform probability on $r_*\Sph{1}$ and $\rho = N(0,I_2)$, critical by
[](#prop:critical-sphere) with $d = 2$ and the first part of [](#prop:notions-coincide). It
is radial with $\mu(\{0\}) = 0$, and $\mu_1$ (the arcsine law on $[-r_*,r_*]$) has no atom: all
steps up to [](#lem:sol-rd2-reduction) apply, with $R = r_*$. What fails is the support
hypothesis: there is no $a > 0$ with $B(0,a) \subset \operatorname{supp}\mu$, so
[](#lem:sol-rd2-continuous), part 3, gives nothing: criticality says nothing at any point
of the open disc $B(0,r_*)$, which is $\mu$-null. The circle itself lies on the edge
$\abs x = R$, outside the domain where $v$ was built; and even if the radial reduction is
carried out there, it yields the single equation $A[U](r_*^2) = 0$ (one value of the Abel
transform), which does not determine $U$. The proof therefore
breaks exactly where it uses that the support is a disc, not where absolute continuity
could have entered — consistent with the circle being critical. The same holds for the
uniform measure on any circle and any radial $\rho$: one equation, no injectivity.
:::

:::{prf:remark} Audit: an atom at the origin
:label: rem:sol-rd2-atom
The measure $\delta_0$ is critical for every radial $\rho$: $v(0) = -2\bar\gamma(0)\int\theta
\dd\sigma = 0$. It is excluded twice: $\delta_0(\{0\}) = 1$, and its support $\{0\}$ is not a
disc of positive radius. With $\mu(\{0\}) > 0$, $\mu_1$ has an atom at $0$
([](#lem:sol-rd2-projection), part 2), $F$ jumps there, and [](#def:barycentric-field) no longer
identifies $\bar\gamma_\theta$ with $T_\theta$ at $s = 0$; this is the only place where the hypothesis
$\mu(\{0\}) = 0$ enters.

*Not closed here.* For $\mu = (1-\lambda)\delta_0 + \lambda\mu'$ with $\lambda \in (0,1)$ and
$\mu'$ radial with support $\overline B(0,R)$, $R > 0$, we expect the conclusion $\mu = \rho$ to
persist: for $x \ne 0$, $\inner{x}{\theta} = 0$ only for two values of $\theta$, the barycentric
projection at points $s \ne 0$ should still be $Q_{\rho_1}(F_{\mu_1}(s))$, the Abel argument
would give $Q_{\rho_1} = Q_{\mu_1}$ off the band of levels $(F_{\mu_1}(0^-), F_{\mu_1}(0))$, and
monotonicity would squeeze $Q_{\rho_1}$ to $0$ on that band. Writing this out requires the
barycentric projection of the monotone plan at the non-atomic points of a measure with one
atom; it is not done in this dossier, and [](#thm:sol-rd2-main) does not claim it.
:::

:::{prf:remark} Why the argument does not extend to an annulus
:label: rem:sol-rd2-annulus
Let $\mu$ be radial with radial support $[c, R]$, $0 < c < R \le \infty$ (the setting of the
open candidate `cand:annulus-d2`). Steps 1 to 4 still run with the open annulus
$\{c < \abs x < R\}$ in place of $B(0,a) \setminus \{0\}$ — the continuity argument of
[](#lem:sol-rd2-continuous), part 3, does not use the origin, and the computation of
[](#lem:sol-rd2-reduction) holds for every $r \in (0,R)$ once $T$ is odd — and give
$A[U](x) = 0$ for $x \in (c^2, R^2)$ only. This does not force $U = 0$, by the following
family.

Let $\Phi \in C_c^\infty((0,c^2))$ and $U = \frac1\pi A[\Phi']$ on $[0,\infty)$. By the
computation in the proof of [](#lem:sol-rd2-abel) (applied to the bounded function $\Phi'$),
$A[U](x) = \int_0^x \Phi' = \Phi(x)$ for every $x \ge 0$, so $A[U] = 0$ on $[c^2,\infty)$. For
$x \ge c^2$ the integrand of $A[\Phi'](x)$ is smooth on the support of $\Phi$, and an
integration by parts gives

$$
U(x) = -\frac{1}{2\pi} \int_0^{c^2} \Phi(\sigma)\,(x-\sigma)^{-3/2} \dd\sigma ,
$$

which is $< 0$ for every $x \ge c^2$ when $\Phi \ge 0$, $\Phi \not\equiv 0$. The odd function
$h$ with $h(s) = U(s^2)$ for $s \ge 0$ therefore satisfies the Abel condition of
[](#lem:sol-rd2-reduction) at every radius $r \ge c$, while $h(s) \ne 0$ at every $s \ge c$.
Any $T = \Id + \varepsilon h$ thus makes the formula of [](#lem:sol-rd2-reduction) vanish on the
whole annulus. What the disc case had and the annulus lacks is the equation on $(0,c^2)$: the
values of $A[U]$ in the hole are free, and the inversion of [](#lem:sol-rd2-abel) needs them.

What this family does *not* give is a counterexample. For a critical pair one needs, in
addition, that $T$ be nondecreasing (true for $\varepsilon$ small, since $h$ is odd with
bounded derivative: $h'(s) = 2sU'(s^2)$, with $U'$ continuous on $[0,\infty)$ and of order
$x^{-5/2}$ at infinity) and that $T_\#\mu_1$ be the projection $\rho_1$ of a *positive* radial
measure $\rho$, which in the plane is a sign condition on an inverse Abel transform inside the
hole. That non-local sign condition is exactly what `cand:annulus-d2` asks about; nothing here
decides it. (The claims of this paragraph on $T$ are checked only in outline and are not used
anywhere.)

When the radial support is $[0,a] \cup [c,R]$ with $0 < a < c$, [](#prop:sol-rd2-local) still
gives $T = \Id$ on $(-a,a)$; on the outer annulus the same family, now with
$\Phi \in C_c^\infty((a^2,c^2))$, shows that the Abel condition alone again leaves $T$ free.
:::

:::{prf:remark} Irregular densities, fat Cantor supports, unbounded supports
:label: rem:sol-rd2-irregular
The support hypothesis concerns the closed support only. A radial $\mu$ whose density vanishes
on a set of radii of positive measure with empty interior (a fat Cantor set of radii) still has
support $\overline B(0,R)$ and is covered: [](#lem:sol-rd2-continuous) transfers the condition
from $\mu$-almost every point to every point of the punctured disc by continuity of $v$, not by
positivity of a density. No integration by parts against $\mu$ is made. For unbounded data
($R = \infty$, or $\rho$ with unbounded support), $T$ may be unbounded near $\pm R$; only its
boundedness on compact subintervals of $(-R,R)$ is used, and no quantity at $\abs x = R$
appears.
:::

:::{prf:remark} Comparison with the full-support theorem
:label: rem:sol-rd2-bonnotte
[](#thm:bonnotte-full-support) assumes $\mu$ and $\rho$ absolutely continuous probabilities on
one bounded ball $B(0,R)$, both with a density strictly positive on it, but no symmetry.
[](#thm:sol-rd2-main) assumes radial symmetry of both, but nothing else on $\rho$. Neither
contains the other. Among radial pairs:

- *Already covered by [](#thm:bonnotte-full-support).* $R < \infty$, $\operatorname{supp}\rho
  \subset \overline B(0,R)$ with $\rho$ absolutely continuous and its density strictly positive
  on $B(0,R)$, and $\mu$ absolutely continuous with a density strictly positive on $B(0,R)$.
  Here the present result gives nothing new; it is an explicit proof (by Abel inversion) of a
  radial instance.
- *Not covered, $\operatorname{supp}\rho \not\subset \overline B(0,R)$.* For example $\mu$ uniform
  on the unit disc and $\rho$ uniform on a disc of radius $2$, or any radial $\rho$ charging
  $\{\abs x > R\}$: the theorem shows that $\mu$ is not critical. A Gaussian $\rho = N(0,sI_2)$
  is already covered by [](#thm:gaussian-target), for every absolutely continuous $\mu$.
- *Not covered, $\operatorname{supp}\rho \subset \overline B(0,R)$ but $\rho$ without a density
  positive on $B(0,R)$.* $\rho$ singular (a circle, an atom at $0$, a mixture), or absolutely
  continuous with a density vanishing on a subset of positive measure of $B(0,R)$.
- *Not covered, on the side of $\mu$.* $R = \infty$ ($\mu$ with full support in the plane,
  $\rho$ non-Gaussian); $\mu$ with support $\overline B(0,R)$ whose density vanishes on a set of
  positive measure; $\mu$ not absolutely continuous (singular parts with $\mu(\{0\}) = 0$).

The novelty is therefore modest and should be stated as such: the mechanism is the one of
the full-support theorem — the support of $\mu$ has no hole, so the condition holds on a
whole disc and determines the projections — and radial symmetry makes the inversion explicit
(Abel), which removes every hypothesis on $\rho$ and every positivity hypothesis on the
density of $\mu$. It says nothing about supports with holes, the case [](#conj:sw-critical)
turns on; [](#rem:sol-rd2-annulus) shows why.
:::

**Fences respected.** [](#thm:radial-disc-d2) has no `bounded_by` node. The fences of the
target are checked anyway. [](#prop:critical-sphere) ($d = 2$): the critical circle has
support a circle, not a disc, so it is outside the hypotheses of [](#thm:sol-rd2-main),
although it satisfies $\mu(\{0\}) = 0$ ([](#rem:sol-rd2-circle)). [](#prop:critical-segments):
a measure carried by a segment is not radial, and its support is not a disc. $\delta_0$, critical
for every radial $\rho$, has an atom at $0$ ([](#rem:sol-rd2-atom)).
