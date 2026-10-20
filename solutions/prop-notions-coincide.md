---
title: "The notions of critical point coincide"
ledger-node: prop:notions-coincide
numbering:
  enumerator: "1.%s"
---

% Dossier for prop:notions-coincide (route ap:certify-scouting, lens prove). Written from
% scratch; the scouting file ensae-conjecture-scouting/verification/13-korba-sw/1-relecture.md
% §2 suggested the key step (the direction -v_mu is a geodesic direction) and is not cited as
% authority. Normalizations: those of def:sliced-wasserstein and def:barycentric-field
% (sigma a probability, factor d in v_mu).

**Overview.** We prove [](#prop:notions-coincide) in a sharper form,
[](#thm:sol-nc-main): the first part holds for every $\mu,\rho \in \Ptwo{d}$, and the second
holds as soon as $\mu$ has no atom, which absolute continuity implies. The steps are:

1. *A jointly measurable version of the barycentric projections*
   ([](#lem:sol-nc-version)). From the quantile functions we build one Borel function
   $g(\theta,s)$ which, for every $\theta$, is a version of $\bar\gamma_\theta$, is
   nondecreasing on a set of full $\mu_\theta$-measure, and equals $T_\theta$ when $\mu_\theta$
   has no atom. This makes $v_\mu$ a well-defined element of $L^2(\mu;\R^d)$, with
   $\norm{\Id - v_\mu}_{L^2(\mu)}^2 \le \int \abs{y}^2 \dd\rho$.
2. *An upper bound valid for every $\mu$* ([](#lem:sol-nc-upper)). Coupling the perturbed
   projection with $\rho_\theta$ through the optimal plan $\gamma_\theta$ gives
   $\SW_2^2((\Id+t\xi)_\#\mu,\rho) \le \SW_2^2(\mu,\rho) + \tfrac{2t}{d}\inner{v_\mu}{\xi}
   + \tfrac{t^2}{d}\norm{\xi}^2$ for all $t \in \R$.
3. *The direction $-v_\mu$ is a geodesic direction, for every $\mu$*
   ([](#lem:sol-nc-geodesic)). The field $\Id - v_\mu$ has a cyclically monotone graph
   because each $g(\theta,\cdot)$ is nondecreasing; hence it is an optimal transport map and
   $t \mapsto (\Id - t v_\mu)_\#\mu$, $t\in[0,1]$, is a constant-speed geodesic. Steps 2 and 3
   prove the first part: along this one curve the right difference quotient is at most
   $-\tfrac2d\norm{v_\mu}^2 + O(t)$.
4. *A one-dimensional first-variation formula* ([](#lem:sol-nc-1d)), proved by the bathtub
   principle, for an atomless source and an arbitrary target in $\mathcal P_2(\R)$.
5. *The first variation along an arbitrary coupling, for atomless $\mu$*
   ([](#lem:sol-nc-plan)), by integrating step 4 over $\theta$ under a uniform domination.
   Together with the representation of Wasserstein geodesics by optimal plans, it proves the
   converse: if $v_\mu = 0$ $\mu$-a.e., every directional derivative vanishes.
6. *Atoms of the projections* ([](#lem:sol-nc-atoms)): $\mu$ has no atom if and only if
   $\mu_\theta$ has no atom for $\sigma$-almost every $\theta$. This identifies the hypothesis
   of step 5 with "µ has no atom".

[](#rem:sol-nc-singular) explains how the equivalence behaves for the singular critical
points (sphere, segments) and gives the example of $\delta_0$, which shows that the converse
fails for measures with atoms. Absolute continuity is used nowhere beyond the absence of
atoms.

**Dependencies.** The definitions [](#def:sliced-wasserstein), [](#def:barycentric-field)
and [](#def:critical-point). No other node of the manuscript is used; in particular
[](#prop:critical-sphere) and [](#prop:critical-segments) are only discussed in a remark,
never used. Literature results used, all classical:

1. One-dimensional optimal transport: for $\alpha, \beta \in \mathcal P_2(\R)$, the monotone
   plan $(Q_\alpha, Q_\beta)_\#\Leb|_{(0,1)}$ is the unique optimal plan for the cost
   $\abs{s-t}^2$, so that $W_2^2(\alpha,\beta) = \int_0^1 \abs{Q_\alpha - Q_\beta}^2$
   ({cite:t}`Santambrogio2015`, Theorem 2.9 with the definition of $\gamma_{\mathrm{mon}}$ in
   Definition 2.3 (§2.1), and Proposition 2.17).
2. Disintegration of a probability measure on a product of Polish spaces
   ({cite:t}`AmbrosioGigliSavare2008`, Theorem 5.3.1).
3. Optimality of $c$-cyclically monotone plans: {cite:t}`Villani2009`, Theorem 5.10(ii),
   equivalence (a)⇔(b), for a real-valued continuous cost bounded below by $0$ and finite
   optimal cost.
4. Constant-speed geodesics of $(\Ptwo{d},W_2)$ are displacement interpolations of optimal
   plans ({cite:t}`AmbrosioGigliSavare2008`, Theorem 7.2.2).

Brenier's theorem is not needed; neither are compact supports, a density of $\rho$, or any
semi-concavity.

## Conventions

For $\nu \in \mathcal P(\R^d)$ write $M_2(\nu) = \int \abs{x}^2 \dd\nu(x)$. For a Borel
probability $\alpha$ on $\R$, $F_\alpha(s) = \alpha((-\infty,s])$, $F_\alpha(s^-) =
\alpha((-\infty,s))$, and $Q_\alpha(u) = \inf\{s \in \R : F_\alpha(s) \ge u\}$ for
$u \in (0,1)$. The following elementary facts are used throughout.

- **(F1)** For $u \in (0,1)$ and $s \in \R$: $Q_\alpha(u) \le s \iff u \le F_\alpha(s)$
  (right continuity of $F_\alpha$). Hence $Q_\alpha$ is nondecreasing and left continuous,
  $F_\alpha(Q_\alpha(u)^-) \le u \le F_\alpha(Q_\alpha(u))$, and, for $V$ uniform on $(0,1)$,
  $Q_\alpha(V)$ has law $\alpha$ (since $\Prob(Q_\alpha(V) \le s) = \Prob(V \le F_\alpha(s))$).
- **(F2)** The literature result 1 above.
- **(F3)** If $\alpha$ has no atom, $F_\alpha$ is continuous, so $F_\alpha(Q_\alpha(u)) = u$
  for $u \in (0,1)$ by (F1). If moreover $U$ has law $\alpha$, then $F_\alpha(U)$ is uniform on
  $(0,1)$: by (F1), $\Prob(F_\alpha(U) \ge u) = \Prob(U \ge Q_\alpha(u)) = 1 -
  F_\alpha(Q_\alpha(u)) = 1-u$. And $Q_\alpha(F_\alpha(U)) = U$ almost surely: (F1) gives
  $Q_\alpha(F_\alpha(U)) \le U$ (on the full-probability event $F_\alpha(U) \in (0,1)$), and
  both sides have law $\alpha$, so $\E[\arctan U - \arctan Q_\alpha(F_\alpha(U))] = 0$ with a
  nonnegative integrand.
- **(F4)** $\int_{\Sph{d-1}} \theta\theta^{\top} \dd\sigma(\theta) = \tfrac1d I_d$ (it commutes
  with rotations and has trace $1$). Hence $\int \inner{x}{\theta}\theta \dd\sigma = x/d$ and
  $\int \inner{x}{\theta}^2\dd\sigma = \abs{x}^2/d$; in particular
  $\int M_2(\nu_\theta)\dd\sigma(\theta) = M_2(\nu)/d$.

The *barycentric projection* of a plan $\gamma \in \mathcal P(\R\times\R)$ with first
marginal $\alpha$ and $\int \abs{t}\dd\gamma < \infty$ is the $\alpha$-a.e. unique
$b \in L^1(\alpha)$ such that $\int \varphi(s) b(s)\dd\alpha(s) = \int \varphi(s)\, t
\dd\gamma(s,t)$ for every bounded Borel $\varphi$; if $\gamma(\dd s,\dd t) = \alpha(\dd s)
k(s,\dd t)$ is a disintegration, $b(s) = \int t\, k(s,\dd t)$ for $\alpha$-a.e. $s$. This is
the $\bar\gamma_\theta$ of [](#def:barycentric-field), with $\gamma_\theta$ the unique optimal
plan, which by (F2) is $(Q_{\mu_\theta}, Q_{\rho_\theta})_\#\Leb|_{(0,1)}$.

A curve $(\mu_t)_{t\in[0,1]}$ in $\Ptwo{d}$ is a *constant-speed geodesic* when
$W_2(\mu_s,\mu_t) = \abs{t-s}\,W_2(\mu_0,\mu_1)$ for all $s,t \in [0,1]$. For
$\gamma \in \mathcal P(\R^d\times\R^d)$ write $\pi^1, \pi^2$ for the coordinate projections.

## Refined statement

The following sharpens [](#prop:notions-coincide): part (a) is its first item, with a single
test curve; part (b) replaces absolute continuity by the absence of atoms and gives the
derivative.

:::{prf:theorem} The notions of critical point coincide for atomless measures
:label: thm:sol-nc-main
Let $d \ge 1$ and $\mu, \rho \in \Ptwo{d}$, and let $v_\mu$ be the barycentric field of $\mu$
relative to $\rho$ ([](#def:barycentric-field)). Then $v_\mu \in L^2(\mu;\R^d)$, and:

(a) The curve $\mu_t = (\Id - t v_\mu)_\#\mu$, $t \in [0,1]$, is a constant-speed geodesic of
$(\Ptwo{d},W_2)$ with $\mu_0 = \mu$, of the form $(\Id + t\xi)_\#\mu$ with
$\xi = -v_\mu \in L^2(\mu;\R^d)$, and

$$
\limsup_{t \downarrow 0} \frac{\SW_2^2(\mu_t,\rho) - \SW_2^2(\mu,\rho)}{t}
\;\le\; -\frac2d \norm{v_\mu}_{L^2(\mu)}^2 .
$$

Consequently, if $\mu$ is a Lagrangian critical point or a Wasserstein critical point of
$\SW_2^2(\cdot,\rho)$ ([](#def:critical-point)), then $v_\mu = 0$ $\mu$-almost everywhere: $\mu$
is a critical point of $\SW_2^2(\cdot,\rho)$.

(b) Assume that $\mu$ has no atom. Let $\gamma \in \mathcal P(\R^d \times \R^d)$ have first
marginal $\mu$ and $\int \abs{y}^2 \dd\gamma(x,y) < \infty$, and let
$\mu_t = ((1-t)\pi^1 + t\pi^2)_\#\gamma$. Then $t \mapsto \SW_2^2(\mu_t,\rho)$, $t \in [0,1]$,
has a right derivative at $t = 0$, equal to

$$
\frac2d \int \inner{v_\mu(x)}{y - x} \dd\gamma(x,y).
$$

In particular, for every $\xi \in L^2(\mu;\R^d)$ the right derivative of
$t \mapsto \SW_2^2((\Id+t\xi)_\#\mu,\rho)$ at $0$ is $\tfrac2d \inner{v_\mu}{\xi}_{L^2(\mu)}$,
and if $v_\mu = 0$ $\mu$-a.e. then $\mu$ is both a Lagrangian and a Wasserstein critical point.
Hence, for a measure $\mu$ with no atom — in particular for an absolutely continuous one —
the three notions of critical point of [](#def:critical-point) coincide.
:::

Part (a) is the first item of [](#prop:notions-coincide). An absolutely continuous measure
has no atom, so part (b) together with part (a) gives its second item. No assumption is
made on $\rho$ beyond $\rho \in \Ptwo{d}$, and none on the supports.

## A measurable version of the barycentric projections

For $\theta \in \Sph{d-1}$ and $s \in \R$ put $a(\theta,s) = F_{\mu_\theta}(s^-)$,
$b(\theta,s) = F_{\mu_\theta}(s)$, and $R(\theta,u) = Q_{\rho_\theta}(u)$ for $u \in (0,1)$.
Define

$$
g(\theta,s) =
\begin{cases}
\dfrac{1}{b-a}\displaystyle\int_a^b R(\theta,u)\dd u & \text{if } a < b
\quad (\text{an atom of } \mu_\theta \text{ at } s),\\[2mm]
R(\theta, b) & \text{if } 0 < a = b < 1,\\[1mm]
0 & \text{otherwise},
\end{cases}
\qquad a = a(\theta,s),\ b = b(\theta,s),
$$

and let $A_\theta = \{s \in \R : a(\theta,s) < b(\theta,s)\} \cup
\{s : 0 < a(\theta,s) = b(\theta,s) < 1\}$.

:::{prf:lemma} The version $g$
:label: lem:sol-nc-version
Let $\mu, \rho \in \Ptwo{d}$.

1. The functions $a, b$ are Borel on $\Sph{d-1}\times\R$, $R$ is Borel on
   $\Sph{d-1}\times(0,1)$ with $\int_0^1 R(\theta,u)^2\dd u = M_2(\rho_\theta) \le M_2(\rho)$
   for every $\theta$, and $g$ is a finite Borel function on $\Sph{d-1}\times\R$. The same
   holds for the quantile function $(\theta,u) \mapsto Q_{\nu_\theta}(u)$ of any
   $\nu \in \Ptwo{d}$, and $\theta \mapsto W_2^2(\nu_\theta, \rho_\theta)$ is Borel.
2. For every $\theta$, $\mu_\theta(\R \setminus A_\theta) = 0$ and $g(\theta,\cdot)$ is
   nondecreasing on $A_\theta$.
3. For every $\theta$, $g(\theta,\cdot)$ is a version of $\bar\gamma_\theta$, and
   $\int g(\theta,s)^2 \dd\mu_\theta(s) \le M_2(\rho_\theta)$. If $\mu_\theta$ has no atom,
   $g(\theta,s) = T_\theta(s) = Q_{\rho_\theta}(F_{\mu_\theta}(s))$ for every $s$ with
   $F_{\mu_\theta}(s) \in (0,1)$, hence $\mu_\theta$-a.e.
4. Let $S_0 = \{x \in \R^d : \int g(\theta,\inner{x}{\theta})^2 \dd\sigma(\theta) < \infty\}$.
   Then $S_0$ is Borel, $\mu(S_0) = 1$, the map
   $w(x) = d\int g(\theta,\inner{x}{\theta})\,\theta\dd\sigma(\theta)$ is Borel on $S_0$, and
   $\int \abs{w}^2 \dd\mu \le M_2(\rho)$. Thus $v_\mu = \Id - w$ (set $w = 0$ off $S_0$)
   belongs to $L^2(\mu;\R^d)$.
5. If $\tilde g$ is another Borel function on $\Sph{d-1}\times\R$ such that $\tilde
   g(\theta,\cdot)$ is a version of $\bar\gamma_\theta$ for $\sigma$-a.e. $\theta$, the field
   built from $\tilde g$ agrees with $v_\mu$ $\mu$-a.e. So $v_\mu$ does not depend on the
   version chosen in [](#def:barycentric-field).
:::

:::{prf:proof}
:class: dropdown
*1.* The function $(x,\theta,s) \mapsto \one\{\inner{x}{\theta} \le s\}$ is Borel on
$\R^d\times\Sph{d-1}\times\R$, so $b(\theta,s) = \int \one\{\inner{x}{\theta}\le s\}
\dd\mu(x)$ is Borel by Tonelli's theorem; likewise $a$, with a strict inequality. By (F1),
$\{(\theta,u) : Q_{\nu_\theta}(u) \le s\} = \{(\theta,u) : u \le F_{\nu_\theta}(s)\}$, which is
Borel for each $s$; hence $(\theta,u) \mapsto Q_{\nu_\theta}(u)$ is Borel, and $R$ is the case
$\nu = \rho$. By (F1), $R(\theta,V)$ has law $\rho_\theta$ for $V$ uniform, so $\int_0^1 R^2 =
M_2(\rho_\theta) = \int \inner{y}{\theta}^2\dd\rho \le M_2(\rho)$. By (F2),
$W_2^2(\nu_\theta,\rho_\theta) = \int_0^1 \abs{Q_{\nu_\theta}(u) - R(\theta,u)}^2\dd u$, Borel in
$\theta$ by Tonelli.

For $g$: on the Borel set $\{a < b\}$, $g(\theta,s) = (b-a)^{-1}\int_0^1 \one\{a(\theta,s) < u
< b(\theta,s)\} R(\theta,u)\dd u$. The integrand is Borel in $(\theta,s,u)$ and integrable in
$u$ for each $(\theta,s)$ (as $R(\theta,\cdot) \in L^2(0,1)$), so Tonelli's theorem applied to
its positive and negative parts shows that this is a finite Borel function. On
$\{0 < a = b < 1\}$, $g = R(\theta, b(\theta,s))$ is a composition of Borel maps with values in
$\R$. Hence $g$ is finite and Borel.

*2.* Fix $\theta$ and write $F = F_{\mu_\theta}$. The complement of $A_\theta$ is
$\{s : F(s^-) = F(s) = 0\} \cup \{s : F(s^-) = F(s) = 1\}$. The first set is contained in
$\{F = 0\}$, an interval of the form $(-\infty, c)$ or $(-\infty,c]$ on which $F$ vanishes,
so it is $\mu_\theta$-null. The second set is contained in $\{s : F(s^-) = 1\}$. If
$\{F=1\}$ is empty, so is this set; otherwise let $c = \inf\{F = 1\}$. Then $\{F(s^-) = 1\}$
is contained in $(c,\infty) \cup \{c\}$, where $\mu_\theta((c,\infty)) = 1 - F(c) = 0$, and $c$
belongs to it only if $F(c^-) = 1 = F(c)$, that is, only if $\mu_\theta(\{c\}) = 0$. So
$\mu_\theta(\R\setminus A_\theta) = 0$.

For $s \in A_\theta$ let $I(s) = (a(\theta,s), b(\theta,s))$ if $s$ is an atom and
$I(s) = \{b(\theta,s)\}$ otherwise; in both cases $I(s) \subset (0,1)$ and $g(\theta,s)$ is the
average of $R(\theta,\cdot)$ over $I(s)$ (for the uniform probability on the interval, or the
value at the point). If $s < s'$ are in $A_\theta$, then $b(\theta,s) = F(s) \le F(s'^-) =
a(\theta,s')$, so every point of $I(s)$ is $\le$ every point of $I(s')$. Since $R(\theta,\cdot)$
is nondecreasing on $(0,1)$, $R(\theta,u) \le R(\theta,u')$ for $u \in I(s)$, $u' \in I(s')$,
and averaging gives $g(\theta,s) \le g(\theta,s')$.

*3.* Fix $\theta$, write $Q = Q_{\mu_\theta}$, $F = F_{\mu_\theta}$, $R = R(\theta,\cdot)$, and
let $\varphi$ be bounded Borel. By (F2), $\int \varphi(s)\,t\dd\gamma_\theta(s,t) =
\int_0^1 \varphi(Q(u))R(u)\dd u$, and by (F1) $\int \varphi(s) g(\theta,s)\dd\mu_\theta(s) =
\int_0^1 \varphi(Q(u))\, g(\theta,Q(u))\dd u$. Split $(0,1)$ into three Borel parts.
(i) For an atom $s$ of $\mu_\theta$ and $u \in (F(s^-), F(s)]$, (F1) gives $Q(u) = s$
(indeed $F(s) \ge u$, while $F(t) \le F(s^-) < u$ for $t < s$). On this interval
$\varphi(Q(u))g(\theta,Q(u)) = \varphi(s)g(\theta,s)$, whose integral is
$\varphi(s)\int_{F(s^-)}^{F(s)} R$, the integral of $\varphi(Q)R$ over the interval. There are
countably many atoms. (ii) The set of $u$ with $Q(u)$ an atom and
$u \notin (F(Q(u)^-),F(Q(u))]$ is contained in $\{F(s^-) : s \text{ atom}\}$, which is
countable. (iii) For every other $u \in (0,1)$, $s = Q(u)$ is not an atom, so $F(s^-) = F(s)$,
and $F(s^-) \le u \le F(s)$ by (F1) gives $F(s) = u \in (0,1)$; thus $g(\theta,Q(u)) =
R(F(Q(u))) = R(u)$. Summing, the two integrals agree, so $g(\theta,\cdot)$ is a version of
$\bar\gamma_\theta$. The same decomposition and Jensen's inequality on each atom interval give
$\int g(\theta,\cdot)^2\dd\mu_\theta = \int_0^1 g(\theta,Q(u))^2\dd u \le \int_0^1 R^2 =
M_2(\rho_\theta)$. If $\mu_\theta$ has no atom, the first case of the definition of $g$ never
occurs, and $g(\theta,s) = R(\theta,F(s)) = T_\theta(s)$ whenever $F(s) \in (0,1)$; the other
$s$ form a $\mu_\theta$-null set by item 2.

*4.* By Tonelli, $x \mapsto \int g(\theta,\inner{x}{\theta})^2\dd\sigma$ is Borel, so $S_0$ is
Borel, and by item 3 and (F4),

$$
\int\!\!\int g(\theta,\inner{x}{\theta})^2 \dd\sigma(\theta)\dd\mu(x)
= \int\!\!\int g(\theta,s)^2\dd\mu_\theta(s)\dd\sigma(\theta)
\le \int M_2(\rho_\theta)\dd\sigma(\theta) = \frac{M_2(\rho)}{d} < \infty,
$$

so $\mu(S_0) = 1$. For $x \in S_0$, $\theta \mapsto g(\theta,\inner{x}{\theta})$ lies in
$L^2(\sigma) \subset L^1(\sigma)$, so $w(x)$ is defined, and Borel on $S_0$ by Fubini's
theorem applied to each coordinate. For a unit vector $e$, Cauchy–Schwarz and (F4) give
$\inner{w(x)}{e}^2 = d^2(\int g(\theta,\inner{x}{\theta})\inner{\theta}{e}\dd\sigma)^2 \le
d^2 \int g(\theta,\inner{x}{\theta})^2\dd\sigma \cdot \tfrac1d$. Taking $e = w(x)/\abs{w(x)}$,
$\abs{w(x)}^2 \le d\int g(\theta,\inner{x}{\theta})^2\dd\sigma$, and integrating in $\mu$,
$\int \abs{w}^2\dd\mu \le M_2(\rho)$. Since $\Id \in L^2(\mu)$, $v_\mu = \Id - w \in
L^2(\mu;\R^d)$.

*5.* The set $\{(\theta,s) : g \ne \tilde g\}$ is Borel and, by Tonelli,
$\int \sigma(\{\theta : g(\theta,\inner{x}{\theta}) \ne \tilde g(\theta,\inner{x}{\theta})\})
\dd\mu(x) = \int \mu_\theta(\{g(\theta,\cdot) \ne \tilde g(\theta,\cdot)\})\dd\sigma(\theta) = 0$.
So for $\mu$-a.e. $x$ the two integrands agree $\sigma$-a.e., and the two fields agree at $x$
(when $\tilde g(\cdot,\inner{x}{\theta}) \in L^1(\sigma)$, which then holds as it equals
$g(\cdot,\inner{x}{\theta})$ $\sigma$-a.e.).
:::

From now on $\bar\gamma_\theta(s) = g(\theta,s)$, and $v_\mu = \Id - w$ with $w$ as in item 4.

## The upper bound

:::{prf:lemma} Upper bound along a perturbation, for every µ
:label: lem:sol-nc-upper
Let $\mu, \rho \in \Ptwo{d}$ and $\xi \in L^2(\mu;\R^d)$. For every $t \in \R$,

$$
\SW_2^2((\Id+t\xi)_\#\mu,\rho) \le \SW_2^2(\mu,\rho) + \frac{2t}{d}\inner{v_\mu}{\xi}_{L^2(\mu)}
+ \frac{t^2}{d}\norm{\xi}_{L^2(\mu)}^2 .
$$
:::

:::{prf:proof}
Fix a Borel representative of $\xi$, $t \in \R$, and $\theta \in \Sph{d-1}$; write
$\mu^t = (\Id+t\xi)_\#\mu \in \Ptwo{d}$. Disintegrate $\gamma_\theta(\dd s,\dd y) =
\mu_\theta(\dd s)\,k_\theta(s,\dd y)$ ({cite:t}`AmbrosioGigliSavare2008`, Theorem 5.3.1), and
let $\Lambda_\theta(\dd x,\dd y) = \mu(\dd x)\,k_\theta(\inner{x}{\theta},\dd y)$, a probability
on $\R^d\times\R$. For Borel $A, B \subset \R$, $\Lambda_\theta(\{\inner{x}{\theta} \in A\}
\times B) = \int \one_A(\inner{x}{\theta})k_\theta(\inner{x}{\theta},B)\dd\mu(x) = \int \one_A(s)
k_\theta(s,B)\dd\mu_\theta(s) = \gamma_\theta(A\times B)$. So the image of $\Lambda_\theta$ under
$(x,y) \mapsto (\inner{x}{\theta}, y)$ is $\gamma_\theta$, its second marginal is $\rho_\theta$,
and its first marginal is $\mu$. The image of $\Lambda_\theta$ under
$(x,y) \mapsto (\inner{x + t\xi(x)}{\theta}, y)$ is therefore a coupling of $\mu^t_\theta$ and
$\rho_\theta$, and

$$
W_2^2(\mu^t_\theta,\rho_\theta) \le \int \big(\inner{x}{\theta} - y + t\inner{\xi(x)}{\theta}\big)^2
\dd\Lambda_\theta
= W_2^2(\mu_\theta,\rho_\theta) + 2t\,c_\theta + t^2\!\int \inner{\xi}{\theta}^2\dd\mu,
$$

where $c_\theta = \int \inner{\xi(x)}{\theta}(\inner{x}{\theta} - y)\dd\Lambda_\theta(x,y)$. All
three terms are finite: $\int(\inner{x}{\theta} - y)^2\dd\Lambda_\theta = \int (s-y)^2
\dd\gamma_\theta = W_2^2(\mu_\theta,\rho_\theta)$, and $\int \abs{\inner{\xi(x)}{\theta}}\abs{y}
\dd\Lambda_\theta \le \norm{\xi}_{L^2(\mu)} M_2(\rho_\theta)^{1/2}$ by Cauchy–Schwarz. Integrating
first in $y$,

$$
c_\theta = \int \inner{\xi(x)}{\theta}\Big(\inner{x}{\theta} - \int y\,k_\theta(\inner{x}{\theta},\dd y)\Big)\dd\mu(x)
= \int \inner{\xi(x)}{\theta}\big(\inner{x}{\theta} - g(\theta,\inner{x}{\theta})\big)\dd\mu(x),
$$

because $\int y\,k_\theta(s,\dd y) = \bar\gamma_\theta(s) = g(\theta,s)$ for $\mu_\theta$-a.e.
$s$ ([](#lem:sol-nc-version), item 3), hence for $\mu$-a.e. $x$ with $s = \inner{x}{\theta}$.

The last expression is defined for every $\theta$, and the integrand
$(x,\theta) \mapsto \inner{\xi(x)}{\theta}(\inner{x}{\theta} - g(\theta,\inner{x}{\theta}))$ is
Borel and lies in $L^1(\mu\otimes\sigma)$: by Cauchy–Schwarz its integral is at most
$\norm{\xi}_{L^2(\mu)}\,(2M_2(\mu) + 2M_2(\rho))^{1/2}$, using
$\int\!\!\int\inner{\xi}{\theta}^2 \le \norm{\xi}^2$ and [](#lem:sol-nc-version), item 4.
So $\theta \mapsto c_\theta$ is Borel and, by Fubini and (F4),

$$
\int c_\theta\dd\sigma(\theta) = \int \Big\langle \xi(x), \int\big(\inner{x}{\theta} -
g(\theta,\inner{x}{\theta})\big)\theta\dd\sigma(\theta)\Big\rangle\dd\mu(x)
= \int \Big\langle \xi(x), \frac{x}{d} - \frac{w(x)}{d}\Big\rangle\dd\mu(x)
= \frac1d\inner{v_\mu}{\xi}_{L^2(\mu)},
$$

the inner integral being computed for $x \in S_0$. Also $\int\!\!\int\inner{\xi(x)}{\theta}^2
\dd\mu\dd\sigma = \norm{\xi}^2/d$ by (F4). Both sides of the pointwise inequality are Borel in
$\theta$ ([](#lem:sol-nc-version), item 1); integrating over $\sigma$ gives the claim.
:::

## The direction −v_µ is a geodesic direction

:::{prf:lemma} A geodesic issued from every µ
:label: lem:sol-nc-geodesic
Let $\mu,\rho \in \Ptwo{d}$, $w = \Id - v_\mu$. The plan $(\Id, w)_\#\mu$ is optimal between
$\mu$ and $w_\#\mu$, so $W_2(\mu, w_\#\mu) = \norm{v_\mu}_{L^2(\mu)}$, and
$\mu_t = (\Id - t v_\mu)_\#\mu = ((1-t)\Id + t w)_\#\mu$, $t \in [0,1]$, is a constant-speed
geodesic with $\mu_0 = \mu$.
:::

:::{prf:proof}
*A full-measure set.* The set $\{(\theta,s) : s \notin A_\theta\}$ is Borel (it is defined by
$a$ and $b$), and by Tonelli and [](#lem:sol-nc-version), item 2,
$\int \sigma(\{\theta : \inner{x}{\theta} \notin A_\theta\})\dd\mu(x) = \int \mu_\theta(\R
\setminus A_\theta)\dd\sigma(\theta) = 0$. Let $S$ be the Borel set of $x \in S_0$ such that
$\inner{x}{\theta} \in A_\theta$ for $\sigma$-a.e. $\theta$; then $\mu(S) = 1$.

*Cyclical monotonicity.* We first recall the one-dimensional fact: if $h$ is nondecreasing on
a set $A \subset \R$ and $u_1,\dots,u_n \in A$, $u_{n+1} = u_1$, then $\sum_i h(u_i)(u_{i+1} -
u_i) \le 0$. Indeed this sum is $\sum_i h(u_i)u_{\tau(i)} - \sum_i h(u_i)u_i$ for the cyclic
permutation $\tau(i) = i+1$, and since the finite sequences $(u_i)$ and $(h(u_i))$ are
similarly ordered ($u_i < u_j \Rightarrow h(u_i) \le h(u_j)$), the rearrangement inequality
says that $\sum_i h(u_i)u_{\tau(i)} \le \sum_i h(u_i) u_i$ for every permutation $\tau$.

Let $x_1,\dots,x_n \in S$ and $x_{n+1} = x_1$. For $\sigma$-a.e. $\theta$, all the numbers
$u_i = \inner{x_i}{\theta}$ lie in $A_\theta$ (a finite union of null sets is null), where
$g(\theta,\cdot)$ is nondecreasing, so

$$
\sum_{i=1}^n \inner{w(x_i)}{x_{i+1} - x_i}
= d\int \sum_{i=1}^n g(\theta,u_i)\,(u_{i+1} - u_i)\dd\sigma(\theta) \le 0 ,
$$

where the integrals defining $w(x_i)$ converge since $x_i \in S_0$. With $y_i = w(x_i)$, this
reads $\sum_i \abs{x_{i+1} - y_i}^2 - \sum_i \abs{x_i - y_i}^2 = \sum_i(\abs{x_{i+1}}^2 -
\abs{x_i}^2) - 2\sum_i \inner{y_i}{x_{i+1} - x_i} \ge 0$: the set
$\Gamma = \{(x, w(x)) : x \in S\}$, Borel as the graph of a Borel map on a Borel set, is
$c$-cyclically monotone for $c(x,y) = \abs{x-y}^2$ (in the orientation of Villani's
Definition 5.1, $\sum_i c(x_i,y_i) \le \sum_i c(x_i,y_{i+1})$, by reversing the order of the points).

*Optimality.* The plan $\pi = (\Id,w)_\#\mu$ satisfies $\pi(\Gamma) = \mu(S) = 1$. The cost $c$
is continuous, real-valued and nonnegative, and the optimal cost between $\mu$ and $w_\#\mu$
is at most $\int\abs{x - w(x)}^2\dd\mu = \norm{v_\mu}^2 < \infty$ (both measures are in
$\Ptwo{d}$ since $w \in L^2(\mu)$). By {cite:t}`Villani2009`, Theorem 5.10(ii), (b)⇒(a), the
$c$-cyclically monotone plan $\pi$ is optimal, so $W_2^2(\mu,w_\#\mu) = \norm{v_\mu}^2$.

*Geodesic.* For $s,t \in [0,1]$, the coupling $((\Id - s v_\mu), (\Id - tv_\mu))_\#\mu$ gives
$W_2(\mu_s,\mu_t) \le \abs{t-s}\norm{v_\mu}$. For $s \le t$, the triangle inequality gives
$\norm{v_\mu} = W_2(\mu_0,\mu_1) \le W_2(\mu_0,\mu_s) + W_2(\mu_s,\mu_t) + W_2(\mu_t,\mu_1) \le
(s + (t-s) + (1-t))\norm{v_\mu}$, so every inequality is an equality, and
$W_2(\mu_s,\mu_t) = (t-s)W_2(\mu_0,\mu_1)$.
:::

## The one-dimensional first variation

:::{prf:lemma} Bathtub principle
:label: lem:sol-nc-bathtub
Let $Y$ be an integrable random variable on a probability space $(\Omega,\Prob)$, with law
$\alpha$, and $a \in (0,1)$. Then

$$
\int_0^a Q_\alpha(u)\dd u = \min\{\E[YZ] : Z \colon \Omega \to [0,1] \text{ measurable},\ \E Z = a\},
$$

and the minimum is attained.
:::

:::{prf:proof}
:class: dropdown
Let $q = Q_\alpha(a)$. By (F1), $\Prob(Y < q) = F_\alpha(q^-) \le a \le F_\alpha(q) =
\Prob(Y \le q)$. For admissible $Z$, $(Y - q)(Z - \one\{Y<q\}) \ge 0$ pointwise (on
$\{Y < q\}$ both factors are $\le 0$, elsewhere both are $\ge 0$), so
$\E[YZ] = qa + \E[(Y-q)Z] \ge qa + \E[(Y-q)\one\{Y<q\}]$. Equality holds for
$Z^* = \one\{Y<q\} + \lambda\one\{Y = q\}$, with $\lambda \in [0,1]$ chosen so that
$\E Z^* = a$ (any $\lambda$ if $\Prob(Y = q) = 0$, in which case $\Prob(Y<q) = a$). Finally,
by (F1), $Q_\alpha(u) \le q$ for $u \le a$ and $Q_\alpha(u) \ge q$ for $u > a$, so
$\int_0^a (Q_\alpha - q) = \int_0^1 (Q_\alpha - q)\one\{Q_\alpha < q\} = \E[(Y-q)\one\{Y<q\}]$,
the last equality because $Q_\alpha(V)$ has law $\alpha$ for $V$ uniform. Hence the minimum
equals $qa + \E[(Y-q)\one\{Y<q\}] = \int_0^a Q_\alpha$.
:::

:::{prf:lemma} One-dimensional first variation
:label: lem:sol-nc-1d
Let $U, H \in L^2(\Omega,\Prob)$, let the law $\alpha$ of $U$ have no atom, let $\beta \in
\mathcal P_2(\R)$, and let $T = Q_\beta \circ F_\alpha$, defined on $\{F_\alpha \in (0,1)\}$,
which carries the law of $U$. Writing $\alpha_t$ for the law of $U + tH$,

$$
\lim_{t \downarrow 0} \frac{W_2^2(\alpha_t,\beta) - W_2^2(\alpha,\beta)}{t} = 2\,\E\big[H\,(U - T(U))\big].
$$
:::

:::{prf:proof}
Write $Q_t = Q_{\alpha_t}$ and $R = Q_\beta$, all in $L^2(0,1)$ by (F1). By (F2),

$$
W_2^2(\alpha_t,\beta) - W_2^2(\alpha,\beta) = \norm{Q_t - Q_0}^2 + 2\inner{Q_t - Q_0}{Q_0 - R}
$$

in $L^2(0,1)$, and $\norm{Q_t - Q_0} = W_2(\alpha_t,\alpha) \le \norm{(U+tH) - U}_{L^2(\Prob)}
= t\norm{H}$. So $D_t = (Q_t - Q_0)/t$ satisfies $\norm{D_t} \le \norm{H}$, and the difference
quotient equals $t\norm{D_t}^2 + 2\inner{D_t}{Q_0 - R}$, whose first term tends to $0$. It
remains to show $\inner{D_t}{Q_0 - R} \to \E[H(U - T(U))]$.

Let $S = F_\alpha(U)$, uniform on $(0,1)$ by (F3), and let $m$ be a Borel function on $(0,1)$
with $m(S) = \E[H \mid S]$ almost surely (Doob–Dynkin); $\int_0^1 m^2 = \E[m(S)^2] \le \E H^2$.

*Claim: $D_t \rightharpoonup m$ weakly in $L^2(0,1)$ as $t \downarrow 0$.* Since
$\norm{D_t} \le \norm{H}$, $\norm{m} \le \norm{H}$ and step functions are dense in $L^2(0,1)$,
it suffices to prove $\int_0^a D_t \to \int_0^a m$ for each $a \in (0,1)$. Fix $a$, let
$q = Q_0(a)$, and $f(t) = \int_0^a Q_t$. By [](#lem:sol-nc-bathtub) applied to
$Y = U + tH$, $f(t) = \min_Z \E[(U+tH)Z]$ over measurable $Z\colon\Omega\to[0,1]$ with
$\E Z = a$. Since $\alpha$ has no atom, $\Prob(U = q) = 0$ and, by (F3),
$\Prob(U < q) = F_\alpha(q) = a$; so $Z_0 = \one\{U<q\}$ is admissible, and by the proof of
[](#lem:sol-nc-bathtub) it is a minimizer at $t = 0$: $f(0) = \E[UZ_0]$.

- Upper bound: $f(t) \le \E[(U+tH)Z_0] = f(0) + t\E[HZ_0]$.
- Lower bound: let $Z_t$ be a minimizer at $t$. Since $Z_t$ is admissible at $0$,
  $f(t) = \E[UZ_t] + t\E[HZ_t] \ge f(0) + t\E[HZ_t]$.
- Since $\E Z_t = \E Z_0$, $\E[UZ_t] - f(0) = \E[(U-q)(Z_t - Z_0)] = \E[\abs{U-q}\,\abs{Z_t -
  Z_0}]$ (on $\{U<q\}$, $Z_0 = 1 \ge Z_t$; on $\{U > q\}$, $Z_0 = 0 \le Z_t$). By the two bounds,
  this is $f(t) - t\E[HZ_t] - f(0) \le t(\E[HZ_0] - \E[HZ_t]) \le 2t\E\abs{H}$.
- For $\delta > 0$ and $K > 0$,
  $\E[\abs{H}\abs{Z_t - Z_0}] \le \E[\abs{H}\one\{\abs{U-q}\le\delta\}] + \E[\abs{H}\one\{\abs{H}
  > K\}] + \tfrac{K}{\delta}\E[\abs{U-q}\abs{Z_t - Z_0}]$, and the last term is at most
  $2tK\E\abs{H}/\delta$. Letting $t \downarrow 0$, then $K \to \infty$ and $\delta \to 0$, by
  dominated convergence and $\Prob(U = q) = 0$: $\E[HZ_t] \to \E[HZ_0]$.

Hence $\int_0^a D_t = (f(t) - f(0))/t$, squeezed between $\E[HZ_t]$ and $\E[HZ_0]$, tends to
$\E[H\one\{U<q\}]$. By (F1), $\{S < a\} = \{F_\alpha(U) < a\} = \{U < Q_0(a)\} = \{U<q\}$, so
$\E[H\one\{U<q\}] = \E[\E[H\mid S]\one\{S<a\}] = \E[m(S)\one\{S<a\}] = \int_0^a m$, proving the
claim.

*Conclusion.* By the claim, $\inner{D_t}{Q_0 - R} \to \inner{m}{Q_0 - R} = \E[m(S)(Q_0(S) -
R(S))]$, using that $S$ is uniform. By (F3), $Q_0(S) = U$ a.s., and $R(S) = Q_\beta(F_\alpha(U))
= T(U)$. Since $Q_0(S) - R(S)$ is $\sigma(S)$-measurable and square integrable,
$\E[m(S)(Q_0(S) - R(S))] = \E[H(Q_0(S) - R(S))] = \E[H(U - T(U))]$.
:::

## The first variation along a coupling, for atomless µ

:::{prf:lemma} Atoms of the projections
:label: lem:sol-nc-atoms
Let $\mu \in \mathcal P(\R^d)$. Then $\mu$ has no atom if and only if $\mu_\theta$ has no atom
for $\sigma$-almost every $\theta$.
:::

:::{prf:proof}
:class: dropdown
If $\mu(\{x_0\}) > 0$, every $\mu_\theta$ has an atom at $\inner{x_0}{\theta}$. Conversely let
$\mu$ have no atom. If $d = 1$, $\mu_{\pm1}$ is $\mu$ or its reflection, without atom. Let
$d \ge 2$. Call an affine subspace $E$ *charged* if $\mu(E) > 0$, and *minimal* if moreover no
affine subspace properly contained in $E$ is charged. Every charged affine subspace contains a
minimal one (take a charged affine subspace of least dimension inside it), of dimension $\ge 1$
since $\mu$ has no atom. If $E \ne E'$ are minimal, $E \cap E'$ is empty or an affine subspace
properly contained in $E$ (if $E \subset E'$, minimality of $E'$ would be contradicted), hence
uncharged. So finitely many distinct minimal subspaces $E_1,\dots,E_k$ satisfy
$\sum_i \mu(E_i) = \mu(\cup_i E_i) \le 1$; for each $n$ at most $n$ of them have mass
$> 1/n$, and there are countably many minimal subspaces. If $\mu_\theta$ has an atom at $s$, the
hyperplane $\{\inner{x}{\theta} = s\}$ is charged and contains a minimal $E$, whose direction
$\vec E \ne \{0\}$ is orthogonal to $\theta$. Hence the set of such $\theta$ is contained in the
countable union of the sets $\vec E^{\perp} \cap \Sph{d-1}$. Each is $\sigma$-null:
$\sigma$ is the law of $G/\abs{G}$ for a standard Gaussian vector $G$, and $\Prob(G \in
\vec E^\perp) = 0$ for a proper linear subspace $\vec E^\perp$.
:::

:::{prf:lemma} First variation along a coupling
:label: lem:sol-nc-plan
Let $\mu, \rho \in \Ptwo{d}$ with $\mu_\theta$ atomless for $\sigma$-a.e. $\theta$. Let
$\gamma \in \mathcal P(\R^d \times \R^d)$ have first marginal $\mu$ and
$\int\abs{y}^2\dd\gamma < \infty$, and $\mu_t = ((1-t)\pi^1 + t\pi^2)_\#\gamma$. Then

$$
\lim_{t\downarrow 0}\frac{\SW_2^2(\mu_t,\rho) - \SW_2^2(\mu,\rho)}{t}
= \frac2d\int\inner{v_\mu(x)}{y-x}\dd\gamma(x,y).
$$
:::

:::{prf:proof}
Let $L^2 = \int\abs{y-x}^2\dd\gamma < \infty$. Fix $\theta$ with $\mu_\theta$ atomless and
apply [](#lem:sol-nc-1d) on the probability space $(\R^d\times\R^d,\gamma)$ with
$U = \inner{x}{\theta}$, of law $\mu_\theta$, $H = \inner{y-x}{\theta}$, and $\beta = \rho_\theta$:
the law of $U + tH = \inner{(1-t)x + ty}{\theta}$ is $(\mu_t)_\theta$, and
$T_\theta(U) = g(\theta,U)$ $\gamma$-a.s. by [](#lem:sol-nc-version), item 3. Hence, writing
$W_\theta(t) = W_2((\mu_t)_\theta,\rho_\theta)$,

$$
\frac{W_\theta(t)^2 - W_\theta(0)^2}{t} \longrightarrow
2\int\inner{y-x}{\theta}\big(\inner{x}{\theta} - g(\theta,\inner{x}{\theta})\big)\dd\gamma(x,y)
=: 2 e_\theta .
$$

*Domination.* By the triangle inequality and the coupling $(U+tH, U)$,
$\abs{W_\theta(t) - W_\theta(0)} \le W_2((\mu_t)_\theta,\mu_\theta) \le t\norm{H}_{L^2(\gamma)} \le
tL$, and $W_\theta(0) \le M_2(\mu_\theta)^{1/2} + M_2(\rho_\theta)^{1/2} \le M_2(\mu)^{1/2} +
M_2(\rho)^{1/2} =: K$ (compare both with $\delta_0$). So for $t \in (0,1]$,
$\abs{W_\theta(t)^2 - W_\theta(0)^2}/t \le L(2K + L)$, a constant. The functions of $\theta$
involved are Borel ([](#lem:sol-nc-version), item 1, applied to $\mu_t$ and $\mu$), and the
limit holds for $\sigma$-a.e. $\theta$; by dominated convergence along every sequence
$t_n \downarrow 0$, the difference quotient of $\SW_2^2(\mu_t,\rho)$ tends to
$2\int e_\theta\dd\sigma(\theta)$.

*Computation.* The integrand $(x,y,\theta) \mapsto \inner{y-x}{\theta}(\inner{x}{\theta} -
g(\theta,\inner{x}{\theta}))$ is Borel and in $L^1(\gamma\otimes\sigma)$: by Cauchy–Schwarz,
its integral is at most $L\,(2M_2(\mu)+2M_2(\rho))^{1/2}$, using (F4) and
[](#lem:sol-nc-version), item 4, the first marginal of $\gamma$ being $\mu$. By Fubini and
(F4), for $\gamma$-a.e. $(x,y)$ (namely $x \in S_0$),
$\int\inner{y-x}{\theta}(\inner{x}{\theta} - g(\theta,\inner{x}{\theta}))\dd\sigma(\theta) =
\inner{y - x}{(x - w(x))/d} = \tfrac1d\inner{y-x}{v_\mu(x)}$. Hence $\int e_\theta\dd\sigma =
\tfrac1d\int\inner{v_\mu(x)}{y-x}\dd\gamma$.
:::

## Proof of the theorem

:::{prf:proof}
That $v_\mu \in L^2(\mu;\R^d)$ is [](#lem:sol-nc-version), item 4.

*(a).* By [](#lem:sol-nc-geodesic), $\mu_t = (\Id - tv_\mu)_\#\mu$, $t\in[0,1]$, is a
constant-speed geodesic with $\mu_0 = \mu$, and it equals $(\Id + t\xi)_\#\mu$ with
$\xi = -v_\mu \in L^2(\mu;\R^d)$. By [](#lem:sol-nc-upper) with this $\xi$, for $t \in (0,1]$,

$$
\frac{\SW_2^2(\mu_t,\rho) - \SW_2^2(\mu,\rho)}{t} \le -\frac2d\norm{v_\mu}^2 + \frac td\norm{v_\mu}^2,
$$

which gives the bound on the $\limsup$. If $\mu$ is a Lagrangian critical point, the right
derivative along $(\Id + t\xi)_\#\mu$ exists and vanishes for this $\xi$; if $\mu$ is a
Wasserstein critical point, it exists and vanishes along the geodesic $(\mu_t)$. In both cases
the $\limsup$ is $0$, so $0 \le -\tfrac2d\norm{v_\mu}^2$ and $v_\mu = 0$ in $L^2(\mu)$, that is
$\mu$-a.e.

*(b).* Let $\mu$ have no atom. By [](#lem:sol-nc-atoms), $\mu_\theta$ is atomless for
$\sigma$-a.e. $\theta$, and [](#lem:sol-nc-plan) gives the right derivative along
$((1-t)\pi^1 + t\pi^2)_\#\gamma$. For $\xi \in L^2(\mu;\R^d)$ take $\gamma = (\Id,\Id+\xi)_\#\mu$:
then $((1-t)\pi^1 + t\pi^2)_\#\gamma = (\Id+t\xi)_\#\mu$, and the derivative is
$\tfrac2d\inner{v_\mu}{\xi}_{L^2(\mu)}$. If $(\mu_t)_{t\in[0,1]}$ is a constant-speed geodesic
of $(\Ptwo{d},W_2)$ with $\mu_0 = \mu$, there is an optimal plan $\gamma$ between $\mu$ and
$\mu_1$ with $\mu_t = ((1-t)\pi^1 + t\pi^2)_\#\gamma$ for every $t \in [0,1]$
({cite:t}`AmbrosioGigliSavare2008`, Theorem 7.2.2); $\gamma$ has first marginal $\mu$ and
$\int\abs{y}^2\dd\gamma = M_2(\mu_1) < \infty$, and the right derivative along $(\mu_t)$ is
$\tfrac2d\int\inner{v_\mu(x)}{y-x}\dd\gamma$. If $v_\mu = 0$ $\mu$-a.e., all these derivatives
vanish, so $\mu$ is a Lagrangian and a Wasserstein critical point. With (a), the three notions
coincide for $\mu$.

*The manuscript statement.* Its first item is (a). For its second, an absolutely continuous
$\mu$ has no atom, so (a) and (b) apply.
:::

## Remarks

:::{prf:remark} Which implication uses which hypothesis; the singular critical points
:label: rem:sol-nc-singular
- *Part (a) uses no hypothesis on $\mu$.* Lagrangian ⇒ critical and Wasserstein ⇒ critical
  hold for every $\mu \in \Ptwo{d}$, including measures with atoms. Only the existence of the
  geodesic of [](#lem:sol-nc-geodesic) is used, and that lemma rests on monotonicity alone.
- *Part (b) uses only that $\mu$ has no atom*, through [](#lem:sol-nc-1d): the minimizer
  $Z_0 = \one\{U<q\}$ of the bathtub problem must be unique up to null sets
  ($\Prob(U = q) = 0$), and $F_\alpha(Q_\alpha(a)) = a$. Absolute continuity of $\mu$ is never
  used beyond this, and neither is Brenier's theorem: geodesics are handled through their
  optimal plans, whether or not they are induced by maps.
- *The sphere and the segments.* The uniform measure on $r\Sph{d-1}$ ($d \ge 2$) and the
  measures of [](#prop:critical-segments) have no atom. By [](#thm:sol-nc-main), for them the
  three notions coincide as well: the sphere of [](#prop:critical-sphere), stated there as a
  Wasserstein critical point, is a critical point and a Lagrangian critical point, and the
  segments, stated as critical points, are also Lagrangian and Wasserstein critical points.
  (This uses only the statements of those two results, which this dossier does not prove.)
  Consequently, the equivalence of notions cannot be where a proof of [](#conj:sw-critical)
  uses absolute continuity of $\mu$: it passes the sphere test and the segment test of the
  problem without distinguishing them from absolutely continuous measures. A proof of the
  target must use the density of $\mu$ elsewhere.
- *Atoms: the converse fails for the Wasserstein notion.* Let $\mu = \delta_0$ and let
  $\rho \in \Ptwo{d}$ be centred, $\rho \ne \delta_0$. Every $\mu_\theta = \delta_0$ has an atom
  with $a = 0$, $b = 1$, so $g(\theta,0) = \int_0^1 Q_{\rho_\theta} = \int\inner{y}{\theta}
  \dd\rho = 0$, and $v_\mu(0) = 0$: $\mu$ is critical. It is a Lagrangian critical point:
  $(\Id+t\xi)_\#\delta_0 = \delta_{tc}$ with $c = \xi(0)$, and by (F4)
  $\SW_2^2(\delta_{tc},\rho) = \int\!\!\int(\inner{y}{\theta} - t\inner{c}{\theta})^2\dd\rho
  \dd\sigma = (M_2(\rho) + t^2\abs{c}^2)/d$, whose right derivative at $0$ vanishes. It is not
  a Wasserstein critical point: the only coupling of $\delta_0$ and $\rho$ is $\delta_0 \otimes
  \rho$, so $\mu_t = (t\,\Id)_\#\rho$ is a constant-speed geodesic (the argument of
  [](#lem:sol-nc-geodesic), *Geodesic*, applies verbatim), and since the quantile function
  of the law of $tZ$ is $tQ_Z$ for $t > 0$, (F2) and (F4) give $\SW_2^2(\mu_t,\rho) =
  (1-t)^2M_2(\rho)/d$, with right derivative $-2M_2(\rho)/d < 0$. So in part (b) the absence
  of atoms cannot be dropped for the Wasserstein notion, and [](#lem:sol-nc-plan) fails for
  this $\mu$ (its right-hand side vanishes).
:::

:::{prf:remark} What is not addressed
:label: rem:sol-nc-open
- Whether a critical point *with atoms* is always a Lagrangian critical point is not
  addressed: it is not needed for [](#prop:notions-coincide), and [](#lem:sol-nc-1d) uses the
  absence of atoms. ({cite:t}`VauthierKorbaMerigot2025`, Proposition 4.4, treat finitely
  supported $\mu$ when $\rho$ has a density.)
- [](#def:critical-point) asks that the right derivatives *vanish*, which presupposes that they
  exist. Part (a) uses only that the upper right Dini derivative along the single curve of
  [](#lem:sol-nc-geodesic) is $\ge 0$; part (b) proves the existence of the derivatives for
  atomless $\mu$. Their existence for general $\mu$, which
  {cite:t}`VauthierKorbaMerigot2025`, Proposition 4.7(a), derive from convexity, is not used.
- Every step above is written out; the dossier rests on the four literature results listed
  under *Dependencies*, whose theorem numbers a reviewer should check against the editions in
  the bibliography.
:::

:::{prf:remark} Normalization, and comparison with Vauthier–Korba–Mérigot
:label: rem:sol-nc-normalization
With $\sigma$ a probability and the factor $d$ of [](#def:barycentric-field), the derivative in
[](#lem:sol-nc-plan) is $\tfrac2d\inner{v_\mu}{\xi}$. {cite:t}`VauthierKorbaMerigot2025`,
equation (16), print the factor $1/d$ in $v_\mu$, and their Proposition 4.7(c) prints
$\varphi'(0) = 2\inner{v_\mu}{\xi}$; with the normalization used here the correct constant is
$2/d$, and their Proposition 4.7(b) correspondingly reads, after renormalization, as
[](#lem:sol-nc-upper). None of this affects a zero set. Compared with their
Corollary 4.8, part (a) adds the Wasserstein notion, and part (b) removes the assumptions of
compact supports and atomless $\rho$, keeping only that $\mu$ has no atom.
:::

**Fences respected.** [](#prop:notions-coincide) has no `bounded_by` node. The fences of the
target, [](#prop:critical-segments) and [](#prop:critical-sphere), concern
[](#conj:sw-critical), not this statement; [](#rem:sol-nc-singular) checks that the refined
statement is consistent with both (they are atomless, and the equivalence holds for them),
and uses neither.
