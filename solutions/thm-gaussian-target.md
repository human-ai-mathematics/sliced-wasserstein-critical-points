---
title: "Gaussian targets"
ledger-node: thm:gaussian-target
numbering:
  enumerator: "2.%s"
---

% Proof dossier for thm:gaussian-target (researcher, prove lens). Uncertified draft until a
% proofs[] record in the ledger names it. Reproved from scratch; the scouting notes of
% 17 October 2026 (ensae-conjecture-scouting/verification/13-korba-sw/C-*.md) were read for
% the idea only and are not cited as authority.

**Overview.** We prove [](#thm:gaussian-target) as stated, for every $d \ge 1$, every
$m \in \R^d$ and every $\Sigma \succ 0$, for absolutely continuous $\mu \in \Ptwo{d}$, with no
entropy, density or support assumption on $\mu$. No flow is used: the argument is static. It
tests the criticality condition twice, once at order zero and once at order one.

1. *Domain* ([](#lem:gt-domain)). Let $C$ be the closed convex hull of $\operatorname{supp}\mu$
   and $U = \operatorname{int} C$. Since $\mu \ll \Leb$, $U \neq \emptyset$, $\mu(U) = 1$, and
   every projection $\mu_\theta$ puts mass on both sides of $\inner{x}{\theta}$ when $x \in U$.
2. *The monotone maps* ([](#lem:gt-monotone), [](#lem:gt-local-bounds)). Each
   $T_\theta = Q_{\rho_\theta} \circ F_{\mu_\theta}$ is finite, continuous and locally absolutely
   continuous on the open interval spanned by $\mu_\theta$, with $T_\theta' = f_\theta / g_\theta(T_\theta)$,
   and it is bounded uniformly in $\theta$ over each compact subset of $U$.
3. *A continuous representative* ([](#lem:gt-representative)). The barycentric field agrees
   $\mu$-a.e. with a field $V$ that is defined and continuous on all of $U$.
4. *Sobolev regularity* ([](#lem:gt-sobolev)). $V \in W^{1,1}_{\mathrm{loc}}(U;\R^d)$, with
   $DV(x) = I - d\int T_\theta'(\inner{x}{\theta})\,\theta\theta^\top \dd\sigma(\theta)$.
5. *From order zero to order one* ([](#lem:gt-stampacchia)). By Stampacchia's lemma, $DV = 0$
   Lebesgue-a.e. on a set $Z$ of full $\mu$-measure where $V = 0$; because $\mu \ll \Leb$, this
   holds $\mu$-a.e. This is the step that excludes the singular critical points.
6. *Two identities* ([](#lem:gt-identities)). Pairing $V = 0$ with $x - m$, and taking the trace
   of $DV = 0$ against $\Sigma$, gives two identities between one-dimensional quantities. Here
   the weight $\theta^\top \Sigma \theta$ is exactly the variance of $\rho_\theta$.
7. *A one-dimensional inequality* ([](#lem:gt-one-dim)). For each direction, the quantity
   combined by the two identities is bounded above by
   $-s_\theta^2\,\mathrm{KL}(\mu_\theta \mid \rho_\theta) - \tfrac12\int\abs{T_\theta - \Id}^2 \dd\mu_\theta$.
   Finiteness of the entropy of $\mu_\theta$ is *deduced* here, not assumed.
8. *Conclusion.* Integrating in $\theta$ forces $T_\theta = \Id$ $\mu_\theta$-a.e. for almost every
   $\theta$, so $\mu_\theta = \rho_\theta$; then $\mu = \rho$ by Cramér–Wold.

**Dependencies.**

- Manuscript nodes: [](#def:critical-point), hence [](#def:barycentric-field) and
  [](#def:sliced-wasserstein). From [](#def:barycentric-field) we use its stated fact that,
  when $\mu_\theta$ has no atom, $\bar\gamma_\theta = T_\theta$ $\mu_\theta$-a.e. This is the
  one-dimensional optimal transport theorem: Santambrogio, *Optimal Transport for Applied
  Mathematicians* (2015), Theorem 2.9 (with the monotone map of Theorem 2.5), restated as Theorem B.6 of
  {cite:t}`VauthierKorbaMerigot2025`. No other node is used. In particular,
  [](#prop:notions-coincide), [](#thm:cs-isotropic) and [](#prop:critical-sphere) are **not**
  used. [](#prop:critical-segments) and [](#prop:critical-sphere) appear only in the audit
  remarks, which are not part of the proof.
- Literature: Stampacchia's lemma, in the form of Gilbarg–Trudinger, *Elliptic Partial
  Differential Equations of Second Order* (2nd ed., 1983), Lemma 7.7: if $u$ is weakly
  differentiable on an open set $\Omega$ (that is, $u, Du \in L^1_{\mathrm{loc}}(\Omega)$), then
  $Du = 0$ a.e. on any set where $u$ is constant. The same result is Theorem 4.4(iv) of
  Evans–Gariepy, *Measure Theory and Fine Properties of Functions* (revised ed., 2015), stated
  there for $W^{1,p}(U)$ and applied here on each open $\Omega' \Subset \Omega$. We
  also use, without numbering, standard facts: Fubini–Tonelli, Lebesgue's density
  theorem, the fundamental theorem of calculus for absolutely continuous functions, Jensen's
  inequality, and Lévy's uniqueness theorem for characteristic functions.

**Notation.** $\sigma$ is the uniform probability on $\Sph{d-1}$, and
$\int \theta\theta^\top \dd\sigma(\theta) = I/d$. For $\theta \in \Sph{d-1}$, write
$m_\theta = \inner{m}{\theta}$ and $s_\theta = (\theta^\top\Sigma\theta)^{1/2}$, so that
$\rho_\theta = N(m_\theta, s_\theta^2)$, with density
$g_\theta(t) = (2\pi s_\theta^2)^{-1/2}\exp(-(t-m_\theta)^2/(2s_\theta^2))$ and quantile function
$Q_\theta(u) = m_\theta + s_\theta\Phi^{-1}(u)$ on $(0,1)$. Here $\Phi$ is the standard normal
distribution function and $\varphi = \Phi'$. The extreme eigenvalues of $\Sigma$ are
$0 < \lambda_{\min} \le \lambda_{\max}$, so $\lambda_{\min} \le s_\theta^2 \le \lambda_{\max}$. Further,
$F_\theta(y) = \mu(\{x : \inner{x}{\theta} \le y\})$ is the distribution function of $\mu_\theta$,
$S = \operatorname{supp}\mu$, $a_\theta = \inf_S \inner{\cdot}{\theta}$,
$b_\theta = \sup_S \inner{\cdot}{\theta}$ (possibly infinite), and $I_\theta = (a_\theta, b_\theta)$.
$\omega_k$ is the volume of the unit ball of $\R^k$ ($\omega_0 = 1$), and
$M_2(\nu) = \int \abs{y}^2 \dd\nu$.

## Statement

**Refined statement.** The theorem below is [](#thm:gaussian-target) verbatim, with $d \ge 1$.
The proof establishes more along the way: [](#lem:gt-stampacchia) and
[](#lem:gt-identities) hold for every target of the stated form, and [](#lem:gt-one-dim) holds
for every absolutely continuous one-dimensional law. We do not state a sharper theorem.

:::{prf:theorem} Gaussian targets
:label: thm:sol-gaussian-target
Let $d \ge 1$, $m \in \R^d$, $\Sigma$ a symmetric positive definite $d \times d$ matrix, and
$\rho = N(m, \Sigma)$. If $\mu \in \Ptwo{d}$ is absolutely continuous and is a critical point
of $\SW_2^2(\cdot,\rho)$, that is $v_\mu = 0$ $\mu$-almost everywhere, then $\mu = \rho$.
:::

Throughout [](#lem:gt-domain)–[](#lem:gt-identities), $\mu \in \Ptwo{d}$ is absolutely
continuous and $\rho = N(m,\Sigma)$ with $\Sigma \succ 0$. Criticality is assumed only in
[](#lem:gt-stampacchia) and [](#lem:gt-identities).

## The domain and the monotone maps

:::{prf:lemma} Domain
:label: lem:gt-domain
1. $\mu(H) = 0$ for every affine hyperplane $H$. Hence each $\mu_\theta$ is absolutely continuous
   on $\R$, and $(\theta, y) \mapsto F_\theta(y)$ is continuous on $\Sph{d-1} \times \R$.
2. $U \ne \emptyset$, $\Leb(\partial C) = 0$ and $\mu(U) = 1$.
3. $a_\theta = \inf_C \inner{\cdot}{\theta}$ and $b_\theta = \sup_C \inner{\cdot}{\theta}$. For
   $x \in U$ and every $\theta$, $\inner{x}{\theta} \in I_\theta$. For $y \in I_\theta$,
   $0 < F_\theta(y) < 1$. Finally, $\mu_\theta(I_\theta) = 1$.
:::

:::{prf:proof}
*(1)* An affine hyperplane is Lebesgue-null, so it is $\mu$-null. If $A \subset \R$ is
Lebesgue-null, then $P_\theta^{-1}(A)$ is Lebesgue-null in $\R^d$ by Fubini in an orthonormal
basis whose first vector is $\theta$. So $\mu_\theta(A) = 0$. For continuity, let
$(\theta_n, y_n) \to (\theta, y)$. For every $x$ off the hyperplane
$\{\inner{x}{\theta} = y\}$, $\one\{\inner{x}{\theta_n} \le y_n\} \to \one\{\inner{x}{\theta} \le y\}$.
That hyperplane is $\mu$-null, so $F_{\theta_n}(y_n) \to F_\theta(y)$ by dominated convergence.

*(2)* By (1), $\mu(S) = 1$ forces $S$ to lie in no affine hyperplane. So $S$ contains $d+1$
affinely independent points, and $C$ contains the simplex they span, which has nonempty
interior. For $\partial C$: fix $x_0$ and $r > 0$ with $B(x_0, 2r) \subset C$, and let
$x \in \partial C$, so that $\abs{x - x_0} \ge 2r$. Suppose a point $z = x + t(x - y)$ with $t > 0$ and $y \in B(x_0, r)$ lies
in $C$. Then $x = \frac{1}{1+t} z + \frac{t}{1+t} y$. Since $B(y, r) \subset B(x_0, 2r) \subset C$,
the convex set $C$ contains
$\frac{1}{1+t}z + \frac{t}{1+t}B(y, r) = B(x, \frac{t r}{1+t})$. This contradicts
$x \in \partial C$. Hence the open cone $\{x + t(x - y) : t > 0,\ y \in B(x_0, r)\}$ does not meet
$C$. Its vertex is $x$, and its half-aperture is $\arcsin(r/\abs{x - x_0})$. For
$x \in \partial C \cap B(0,R)$, this aperture is bounded below by a constant depending only on
$R$, $x_0$ and $r$. So the lower density of $\R^d \setminus C$ at $x$ is at least some
$c_R > 0$. Thus no point of $\partial C \cap B(0,R)$ is a Lebesgue density point of
$\partial C \subset C$. By Lebesgue's density theorem $\Leb(\partial C \cap B(0,R)) = 0$, for
every $R$. Finally $\mu(\R^d \setminus C) \le \mu(\R^d \setminus S) = 0$ and
$\mu(\partial C) = 0$ by absolute continuity, so $\mu(U) = 1$.

*(3)* A linear functional has the same supremum over a set and over its closed convex hull.
If $x \in U$, then $x \pm \eps\theta \in C$ for small $\eps > 0$, so
$a_\theta < \inner{x}{\theta} < b_\theta$. If $y \in I_\theta$, there is $s \in S$ with
$\inner{s}{\theta} < y$. The open half-space $\{\inner{\cdot}{\theta} < y\}$ is a neighbourhood
of a point of the support, so it has positive $\mu$-mass, and $F_\theta(y) > 0$. Symmetrically,
$F_\theta(y) < 1$. Finally, $\mu_\theta$ is carried by the closure of $I_\theta$ and has no atom,
so $\mu_\theta(I_\theta) = 1$.
:::

Set $O = \{(\theta, y) \in \Sph{d-1}\times\R : 0 < F_\theta(y) < 1\}$. It is open by
[](#lem:gt-domain) (1), and its $\theta$-section contains $I_\theta$. On $O$ put

$$
T(\theta, y) = T_\theta(y) = Q_\theta(F_\theta(y)) = m_\theta + s_\theta\,\Phi^{-1}(F_\theta(y)).
$$

:::{prf:lemma} The monotone maps
:label: lem:gt-monotone
1. $T$ is continuous on $O$, and each $T_\theta$ is nondecreasing on $I_\theta$.
2. $(T_\theta)_\#\mu_\theta = \rho_\theta$, so $\int T_\theta^2 \dd\mu_\theta = m_\theta^2 + s_\theta^2$
   and $\int (T_\theta - m_\theta)^2 \dd\mu_\theta = s_\theta^2$.
3. On every compact interval $J \subset I_\theta$, $T_\theta$ is absolutely continuous. Let
   $f_\theta$ be a density of $\mu_\theta$. For Lebesgue-a.e. $y \in I_\theta$,
   $T_\theta$ is differentiable at $y$ and

   $$
   T_\theta'(y) = \frac{f_\theta(y)}{g_\theta(T_\theta(y))} \ \ge 0 .
   $$ (eq-gt-ma)

4. There is a Borel function $D : \Sph{d-1}\times\R \to [0,\infty)$ such that, for every
   $\theta$, $D(\theta, \cdot) = T_\theta'$ Lebesgue-a.e. on $I_\theta$. We write $T_\theta'$ for
   $D(\theta,\cdot)$ from now on.
:::

:::{prf:proof}
:class: dropdown
*(1)* $F$ is continuous with values in $(0,1)$ on $O$, $\Phi^{-1}$ is continuous on $(0,1)$,
and $\theta \mapsto m_\theta, s_\theta$ are continuous. $F_\theta$ and $\Phi^{-1}$ are
nondecreasing.

*(2)* Since $F_\theta$ is continuous, $(F_\theta)_\#\mu_\theta$ is the uniform law on $(0,1)$. Indeed,
for $u \in (0,1)$, let $y_u = \max\{y : F_\theta(y) \le u\}$. Then $F_\theta(y_u) = u$ by
continuity, and $\mu_\theta(F_\theta \le u) = \mu_\theta((-\infty, y_u]) = u$. Also
$Q_\theta$ is the quantile function of $\rho_\theta$, so $(Q_\theta)_\#\mathrm{Unif}(0,1) = \rho_\theta$
($Q_\theta(u) \le t \iff u \le \Phi((t - m_\theta)/s_\theta)$). Since $\mu_\theta(I_\theta) = 1$,
$T_\theta$ is $\mu_\theta$-a.e. finite and $(T_\theta)_\#\mu_\theta = \rho_\theta$. The two moments
are those of $N(m_\theta, s_\theta^2)$.

*(3)* $F_\theta(y) = \int_{-\infty}^y f_\theta$ is absolutely continuous on $\R$ by
[](#lem:gt-domain) (1). On a compact $J \subset I_\theta$, the continuous function $F_\theta$ takes
values in a compact $[\eps, 1 - \eps] \subset (0,1)$ ([](#lem:gt-domain) (3)). There $\Phi^{-1}$
is $C^1$, hence Lipschitz. A Lipschitz function of an absolutely continuous function is
absolutely continuous. At each $y \in I_\theta$ where $F_\theta$ is differentiable with
$F_\theta'(y) = f_\theta(y)$, which holds for a.e. $y$ by Lebesgue's differentiation theorem, the
chain rule gives
$T_\theta'(y) = s_\theta f_\theta(y)/\varphi(\Phi^{-1}(F_\theta(y))) = f_\theta(y)/g_\theta(T_\theta(y))$.
This uses $g_\theta(T_\theta(y)) = s_\theta^{-1}\varphi((T_\theta(y)-m_\theta)/s_\theta)$ and
$(T_\theta(y) - m_\theta)/s_\theta = \Phi^{-1}(F_\theta(y))$. The right-hand side does not depend on
the choice of density, up to a null set.

*(4)* For $n \ge 1$, let $q_n(\theta, y) = n\,(T(\theta, y + 1/n) - T(\theta, y))$ when $(\theta, y)$
and $(\theta, y + 1/n)$ lie in $O$, and $q_n = 0$ otherwise. Each $q_n$ is Borel and $q_n \ge 0$
by monotonicity. Put $D = \limsup_n q_n$ where this is finite and $D = 0$ where it is
$+\infty$. $D$ is Borel. If $y \in I_\theta$ and $T_\theta$ is
differentiable at $y$, then $(\theta, y + 1/n) \in O$ for large $n$ ($O$ is open), so
$q_n(\theta, y) \to T_\theta'(y)$ and $D(\theta, y) = T_\theta'(y)$. By (3), this is the case for
a.e. $y \in I_\theta$.
:::

:::{prf:lemma} Local bounds
:label: lem:gt-local-bounds
Let $K \subset U$ be compact. For $\theta \in \Sph{d-1}$, let
$h^-_K(\theta) = \min_K \inner{\cdot}{\theta}$, $h^+_K(\theta) = \max_K \inner{\cdot}{\theta}$ and
$J^K_\theta = [h^-_K(\theta), h^+_K(\theta)]$. There is $m_K \in (0, \tfrac12]$ such that, for every
$\theta$, $J_\theta^K \subset I_\theta$ and $F_\theta(J^K_\theta) \subset [m_K, 1 - m_K]$. Consequently:

1. $\abs{T_\theta(y)} \le C_K := \abs{m} + \lambda_{\max}^{1/2}\,\Phi^{-1}(1 - m_K)$ for all
   $\theta$ and $y \in J_\theta^K$;
2. $T_\theta$ is absolutely continuous on $J^K_\theta$, and
   $\int_{J_\theta^K} T_\theta' \dd y = T_\theta(h_K^+(\theta)) - T_\theta(h_K^-(\theta)) \le 2 C_K$;
3. $\int_K T_\theta'(\inner{x}{\theta}) \dd x \le B_K := 2 C_K\,\omega_{d-1}(\operatorname{diam} K)^{d-1}$
   for every $\theta$ (for $d = 1$, read $B_K = 2C_K$).
:::

:::{prf:proof}
$J_\theta^K \subset I_\theta$ by [](#lem:gt-domain) (3), since $K \subset U$. The functions
$h^\pm_K$ are continuous (support functions of a compact set). The function
$m^+(\theta) = 1 - F_\theta(h_K^+(\theta))$ is therefore continuous by [](#lem:gt-domain) (1). It is
positive by [](#lem:gt-domain) (3), because $h_K^+(\theta) \in I_\theta$. Likewise
$m^-(\theta) = F_\theta(h_K^-(\theta))$ is continuous and positive. Let $m_K$ be the minimum over the
compact sphere of $\min(m^+, m^-, \tfrac12)$, so $m_K > 0$. Since $F_\theta$ is nondecreasing,
$F_\theta(J^K_\theta) \subset [m_K, 1 - m_K]$. Then (1) follows from
$\abs{T_\theta} \le \abs{m_\theta} + s_\theta\abs{\Phi^{-1}(F_\theta)}$ and the symmetry of
$\Phi^{-1}$. (2) is [](#lem:gt-monotone) (3) on the compact interval $J^K_\theta \subset I_\theta$,
together with (1).

For (3), let $\pi_\theta$ be the orthogonal projection onto $\theta^\perp$, and write
$x = y\theta + z$ with $z \in \theta^\perp$. Then $x \in K$ implies $y \in J^K_\theta$ and
$z \in \pi_\theta(K)$. The set $\pi_\theta(K)$ lies in a ball of $\theta^\perp$ of radius
$\operatorname{diam} K$ around the projection of any point of $K$. By Tonelli and (2),
$\int_K T_\theta'(\inner{x}{\theta}) \dd x \le \mathcal{H}^{d-1}(\pi_\theta(K)) \int_{J^K_\theta} T_\theta' \dd y \le B_K$.
:::

## The field and its derivative

On $U$ define

$$
W(x) = d\int_{\Sph{d-1}} T_\theta(\inner{x}{\theta})\,\theta \dd\sigma(\theta), \qquad V(x) = x - W(x).
$$

By [](#lem:gt-domain) (3), $(\theta, \inner{x}{\theta}) \in O$ for all $x \in U$ and all $\theta$.
By [](#lem:gt-local-bounds) (1) with $K = \{x\}$, the integrand is bounded, so $W$ is defined at
every point of $U$.

:::{prf:lemma} A continuous representative of the barycentric field
:label: lem:gt-representative
$V$ is continuous on $U$, and $v_\mu = V$ $\mu$-almost everywhere. In particular, $\mu$ is a
critical point of $\SW_2^2(\cdot,\rho)$ if and only if $V = 0$ $\mu$-a.e. on $U$.
:::

:::{prf:proof}
*Continuity.* Let $x_n \to x$ in $U$. Choose a compact neighbourhood $K \subset U$ of $x$. For
each $\theta$, $T_\theta(\inner{x_n}{\theta}) \to T_\theta(\inner{x}{\theta})$ by continuity of $T$
on $O$. The integrands are bounded by $C_K$ ([](#lem:gt-local-bounds)), so
$W(x_n) \to W(x)$ by dominated convergence.

*Agreement with $v_\mu$.* By [](#lem:gt-domain) (1), each $\mu_\theta$ has no atom. So, by
[](#def:barycentric-field), $\bar\gamma_\theta = T_\theta$ outside a $\mu_\theta$-null set $N_\theta$. The
integral defining $v_\mu$ in [](#def:barycentric-field) presupposes a choice of
$(x,\theta) \mapsto \bar\gamma_\theta(\inner{x}{\theta})$ that is $\mu\otimes\sigma$-measurable and
$\sigma$-integrable for $\mu$-a.e. $x$; we use any such choice. The map
$(x,\theta) \mapsto T_\theta(\inner{x}{\theta})$ is Borel on $U \times \Sph{d-1}$, since it is
continuous. So
$E = \{(x,\theta) \in U\times\Sph{d-1} : \bar\gamma_\theta(\inner{x}{\theta}) \ne T_\theta(\inner{x}{\theta})\}$
is $\mu\otimes\sigma$-measurable. For each $\theta$, its section
$\{x : \inner{x}{\theta} \in N_\theta\}$ is $\mu$-null. By Tonelli,
$(\mu\otimes\sigma)(E) = 0$, so for $\mu$-a.e. $x \in U$ the $\theta$-section of $E$ is
$\sigma$-null. For such $x$ the two integrands agree $\sigma$-a.e. and $v_\mu(x) = V(x)$. Since
$\mu(U) = 1$ ([](#lem:gt-domain) (2)), $v_\mu = V$ $\mu$-a.e.
:::

For $x \in U$ set

$$
a(x) = \int T_\theta'(\inner{x}{\theta}) \dd\sigma(\theta) \in [0, \infty], \qquad
A(x) = d\int T_\theta'(\inner{x}{\theta})\,\theta\theta^\top \dd\sigma(\theta) \quad \text{when } a(x) < \infty .
$$

Both are Borel on $U$ (Tonelli, [](#lem:gt-monotone) (4)).

:::{prf:lemma} Sobolev regularity
:label: lem:gt-sobolev
$a \in L^1_{\mathrm{loc}}(U)$, so $a < \infty$ Lebesgue-a.e. on $U$. Moreover
$V \in W^{1,1}_{\mathrm{loc}}(U;\R^d)$, and its weak derivative is $DV = I - A$ Lebesgue-a.e. on
$U$. That is, for all $i, j$ and every $\phi \in C^\infty_c(U)$,

$$
\int_U V_j\,\partial_i\phi \dd x = -\int_U (\delta_{ij} - A_{ij})\,\phi \dd x .
$$
:::

:::{prf:proof}
*Integrability.* For compact $K \subset U$, Tonelli and [](#lem:gt-local-bounds) (3) give
$\int_K a \dd x = \int \int_K T_\theta'(\inner{x}{\theta}) \dd x \dd\sigma(\theta) \le B_K$. Since
$\abs{A_{ij}} \le d\,a$, $A \in L^1_{\mathrm{loc}}(U)$. Also $V$ is continuous, hence locally
integrable.

*One direction, $\theta$ fixed.* Fix $\phi \in C^\infty_c(U)$ with support $K$. Let
$\delta = \min(1, \operatorname{dist}(K, \R^d \setminus U))$ ($\delta = 1$ if $U = \R^d$), and let
$K' = \{x : \operatorname{dist}(x, K) \le \delta/2\}$, a compact subset of $U$. Put
$u_\theta(x) = T_\theta(\inner{x}{\theta})$ for $x\in U$. We claim

$$
\int_U u_\theta\,\partial_i\phi \dd x = -\theta_i \int_U T_\theta'(\inner{x}{\theta})\,\phi(x) \dd x
\qquad (i = 1, \dots, d).
$$ (eq-gt-ibp)

Write $e_i = \theta_i\theta + \eta$ with $\eta = e_i - \theta_i\theta \perp \theta$, so
$\partial_i\phi = \theta_i\,\partial_\theta\phi + \partial_\eta\phi$. Use the coordinates
$x = y\theta + z$, $z \in \theta^\perp$. Both integrands vanish off $K$, where
$\abs{u_\theta} \le C_K$, so Fubini applies.

- *The $\eta$ part.* $\int u_\theta\,\partial_\eta\phi \dd x = \int_\R T_\theta(y) \big(\int_{\theta^\perp} \partial_\eta \phi(y\theta + z) \dd z\big) \dd y$.
  We restrict to the $y$ for which the inner integrand is not identically zero; these lie in
  $J^K_\theta \subset I_\theta$. The inner integral is the integral over $\theta^\perp$ of a
  derivative, in a direction of $\theta^\perp$, of a $C^1_c$ function, so it vanishes. (For
  $d = 1$, $\eta = 0$.)
- *The $\theta$ part.* For fixed $z$, $\psi_z(y) = \phi(y\theta + z)$ is $C^1$ with support in
  $J^K_\theta$, which lies in the interior of $J^{K'}_\theta$ because
  $h^\pm_{K'}(\theta) = h^\pm_K(\theta) \pm \delta/2$. On $J^{K'}_\theta$, $T_\theta$ is absolutely
  continuous ([](#lem:gt-local-bounds) (2) for $K'$). Integration by parts for a product of
  absolutely continuous functions on $J^{K'}_\theta$, whose boundary terms vanish because
  $\psi_z = 0$ at its endpoints, gives
  $\int T_\theta \psi_z' \dd y = -\int T_\theta' \psi_z \dd y$. Integrating in $z$ (Fubini, using
  $\abs{T_\theta \psi_z'} \le C_K \norm{\nabla\phi}_\infty \one_K$ and
  [](#lem:gt-local-bounds) (3)) gives
  $\int u_\theta\,\partial_\theta\phi \dd x = -\int T_\theta'(\inner{x}{\theta})\,\phi \dd x$.

Summing the two parts proves [](#eq-gt-ibp).

*Averaging over $\theta$.* $W_j(x) = d\int u_\theta(x)\,\theta_j \dd\sigma(\theta)$. On
$K \times \Sph{d-1}$ the integrand $u_\theta(x)\theta_j\partial_i\phi(x)$ is jointly Borel and
bounded by $C_K\norm{\nabla\phi}_\infty$. The integrand
$T_\theta'(\inner{x}{\theta})\abs{\phi(x)}$ has integral at most $\norm{\phi}_\infty B_K$ over
$K\times\Sph{d-1}$. So Fubini applies twice, and by [](#eq-gt-ibp)

$$
\int W_j\,\partial_i \phi \dd x
= d\int \theta_j \int u_\theta\,\partial_i\phi \dd x \dd\sigma
= -\int \phi(x)\, d\int T_\theta'(\inner{x}{\theta})\,\theta_i\theta_j \dd\sigma \dd x
= -\int A_{ij}\,\phi \dd x .
$$

Since $\int x_j\,\partial_i\phi = -\delta_{ij}\int\phi$, the claim follows.
:::

## Criticality at order one

:::{prf:lemma} Stampacchia transfer
:label: lem:gt-stampacchia
Assume moreover that $\mu$ is a critical point of $\SW_2^2(\cdot,\rho)$. Let
$Z = \{x \in U \cap S : V(x) = 0\}$. Then $Z$ is Borel and $\mu(Z) = 1$. For $\mu$-a.e. $x$,
$a(x) < \infty$ and $A(x) = I$.
:::

:::{prf:proof}
$Z$ is relatively closed in $U \cap S$ ($V$ is continuous), hence Borel. By
[](#lem:gt-representative), $V = 0$ $\mu$-a.e. on $U$. Since $\mu(U \cap S) = 1$, $\mu(Z) = 1$.
This is the only use of the criticality hypothesis in this lemma, and it involves only points
of $S$.

Fix $j$. By [](#lem:gt-sobolev), $V_j$ is weakly differentiable on $U$ with weak gradient
$(\delta_{ij} - A_{ij})_i$. Gilbarg–Trudinger, Lemma 7.7, applied to $V_j$ on $\Omega = U$,
gives $\nabla V_j = 0$ Lebesgue-a.e. on $\{V_j = 0\} \supset Z$. A weak gradient is determined up
to a Lebesgue-null set, so the statement holds for our representative $I - A$. So the set

$$
N = \{x \in Z : a(x) = \infty\} \cup \{x \in Z : a(x) < \infty,\ A(x) \ne I\}
$$

is Borel and Lebesgue-null (the first part by [](#lem:gt-sobolev)). **Because $\mu \ll \Leb$**,
$\mu(N) = 0$. Hence $a < \infty$ and $A = I$ on $Z \setminus N$, a set of full $\mu$-measure.
:::

:::{prf:lemma} Two identities
:label: lem:gt-identities
Assume that $\mu$ is a critical point of $\SW_2^2(\cdot,\rho)$. Then:

$$
\int s_\theta^2 \Big(\int T_\theta' \dd\mu_\theta\Big) \dd\sigma(\theta) = \int s_\theta^2 \dd\sigma(\theta) = \frac{\operatorname{tr}\Sigma}{d} ,
$$ (eq-gt-II)

$$
\int \Big(\int (y - m_\theta)(T_\theta(y) - y) \dd\mu_\theta(y)\Big) \dd\sigma(\theta) = 0 .
$$ (eq-gt-I)

All the inner integrals are measurable in $\theta$. The integrand of [](#eq-gt-I) is
$\sigma$-integrable. In particular $\int T_\theta' \dd\mu_\theta < \infty$ for $\sigma$-a.e. $\theta$.
:::

:::{prf:proof}
*[](#eq-gt-II): trace against $\Sigma$.* By [](#lem:gt-stampacchia), $\operatorname{tr}(\Sigma A(x)) = \operatorname{tr}\Sigma$
for $\mu$-a.e. $x$. Here
$\operatorname{tr}(\Sigma A(x)) = d\int T_\theta'(\inner{x}{\theta})\,\theta^\top\Sigma\theta \dd\sigma = d\int s_\theta^2\,T_\theta'(\inner{x}{\theta}) \dd\sigma$.
Integrate in $\mu$ and use Tonelli, which applies since the integrand is nonnegative and
jointly Borel. The image of $\mu$ under $P_\theta$ is $\mu_\theta$, so
$\operatorname{tr}\Sigma = d\int s_\theta^2 \int T_\theta' \dd\mu_\theta \dd\sigma$. Finally,
$\operatorname{tr}\Sigma = \operatorname{tr}(\Sigma \cdot d\int\theta\theta^\top\dd\sigma) = d\int s_\theta^2 \dd\sigma$.
Since $s_\theta^2 \ge \lambda_{\min} > 0$, the left-hand side of [](#eq-gt-II) being finite forces
$\int T_\theta'\dd\mu_\theta < \infty$ for $\sigma$-a.e. $\theta$.

*[](#eq-gt-I): pairing with $x - m$.* By [](#lem:gt-representative),
$\int_U \inner{x - m}{V(x)} \dd\mu(x) = 0$, provided the integrand is integrable; we check this
for each of its two terms. First, $\abs{\inner{x-m}{x}} \le \abs{x}^2 + \abs{m}\abs{x}$ is
$\mu$-integrable. Second,
$\inner{x - m}{W(x)} = d\int (\inner{x}{\theta} - m_\theta)\,T_\theta(\inner{x}{\theta}) \dd\sigma$.
By Tonelli, Cauchy–Schwarz and [](#lem:gt-monotone) (2),

$$
\iint \abs{y - m_\theta}\,\abs{T_\theta(y)} \dd\mu_\theta(y)\dd\sigma(\theta)
\le \int \big(2M_2(\mu_\theta) + 2m_\theta^2\big)^{1/2}\big(m_\theta^2 + s_\theta^2\big)^{1/2} \dd\sigma
< \infty ,
$$

because $M_2(\mu_\theta) \le M_2(\mu) < \infty$. So Fubini applies, and
$\int \inner{x-m}{W}\dd\mu = d\iint (y - m_\theta)T_\theta(y)\dd\mu_\theta\dd\sigma$. On the other
hand, $\inner{x-m}{x} = d\int(\inner{x}{\theta} - m_\theta)\inner{x}{\theta}\dd\sigma$, so
$\int \inner{x - m}{x}\dd\mu = d\iint (y - m_\theta)\,y \dd\mu_\theta\dd\sigma$, which is also
absolutely convergent. Subtracting gives [](#eq-gt-I) multiplied by $-d$. The inner integral of
[](#eq-gt-I) is bounded by
$(2M_2(\mu)+2\abs{m}^2)^{1/2}(\abs{m}^2+\lambda_{\max})^{1/2} + M_2(\mu) + \abs{m}M_2(\mu)^{1/2}$,
uniformly in $\theta$.
:::

## The one-dimensional inequality

:::{prf:lemma} One direction
:label: lem:gt-one-dim
Fix $\theta$ with $\int T_\theta'\dd\mu_\theta < \infty$, and drop the index $\theta$: $\nu = \mu_\theta$,
$f$ its density, $T = T_\theta$, $g = g_\theta$, $s = s_\theta$, $m_\theta$ the mean of $\rho_\theta$.
Put $E = \int \abs{T(y) - y}^2 \dd\nu(y)$. Then $\log f \in L^1(\nu)$, so
$\mathrm{KL}(\nu \mid \rho_\theta) = \int \log(f/g) \dd\nu$ is finite and nonnegative, and

$$
s^2 \int (1 - T') \dd\nu + \int (y - m_\theta)(T(y) - y) \dd\nu(y)
\;\le\; -\,s^2\,\mathrm{KL}(\nu \mid \rho_\theta) - \tfrac12 E \;\le\; -\tfrac12 E .
$$ (eq-gt-L)
:::

:::{prf:proof}
*Finiteness.* The set $\{f = 0\}$ is $\nu$-null, and [](#eq-gt-ma) holds Lebesgue-a.e. on
$I_\theta$, hence $\nu$-a.e. ($\nu \ll \Leb$, $\nu(I_\theta) = 1$). So $\nu$-a.e. we have
$T' > 0$, $T' < \infty$ (it is $\nu$-integrable), and

$$
\log T' = \log f - \log g(T), \qquad \log g(T) = -\log(\sqrt{2\pi}\,s) - \frac{(T - m_\theta)^2}{2s^2}.
$$

By [](#lem:gt-monotone) (2), $\log g(T) \in L^1(\nu)$ and
$\int \log g(T) \dd\nu = -\log(\sqrt{2\pi}\,s) - \tfrac12$. Since $\log t \le t - 1 < t$,
$(\log T')^+ \le T' \in L^1(\nu)$. Hence
$(\log f)^+ \le (\log T')^+ + \abs{\log g(T)} \in L^1(\nu)$. For the negative part, split $\R$.
Where $f \ge e^{-y^2}$, $f(\log f)^- \le y^2 f$. Where $f < e^{-y^2}$, $f < 1$ and
$f(\log f)^- = -f\log f \le \tfrac{2}{e}\sqrt f \le \tfrac2e e^{-y^2/2}$, using
$-t\log t \le \tfrac2e\sqrt t$ on $(0,1]$. Both bounds are Lebesgue-integrable because
$M_2(\nu) < \infty$. So $\int (\log f)^- \dd\nu = \int f(\log f)^-\dd y < \infty$, and
$\log f \in L^1(\nu)$. Therefore $\log T' \in L^1(\nu)$, and

$$
\int \log T' \dd\nu = \int \log f\dd\nu + \log(\sqrt{2\pi}\,s) + \tfrac12 .
$$

Also $\log(f/g) = \log f - \log g \in L^1(\nu)$, with
$\int \log g \dd\nu = -\log(\sqrt{2\pi}s) - \int (y-m_\theta)^2\dd\nu/(2s^2)$. By Jensen's
inequality for the concave $\log$, and since $g/f > 0$ $\nu$-a.e.,
$-\mathrm{KL}(\nu\mid\rho_\theta) = \int \log(g/f)\dd\nu \le \log\int_{\{f>0\}} g \dd y \le 0$.

*The inequality.* Since $1 - t \le -\log t$ for $t > 0$,

$$
s^2\int(1 - T')\dd\nu \le -s^2\int \log T'\dd\nu = -s^2\int\log f\dd\nu - s^2\log(\sqrt{2\pi}\,s) - \tfrac{s^2}2 .
$$

Expand $(T - m_\theta)^2 = (y - m_\theta)^2 + 2(y - m_\theta)(T - y) + (T - y)^2$; all terms are
$\nu$-integrable. Integrating, with $\int (T - m_\theta)^2\dd\nu = s^2$ ([](#lem:gt-monotone) (2)),

$$
\int (y - m_\theta)(T - y)\dd\nu = \tfrac{s^2}{2} - \tfrac12\int (y - m_\theta)^2\dd\nu - \tfrac12 E .
$$

Adding the two displays gives
$-s^2\big[\int \log f\dd\nu + \log(\sqrt{2\pi}\,s) + \int(y - m_\theta)^2\dd\nu/(2s^2)\big] - \tfrac12 E$.
The bracket is $\int\log(f/g)\dd\nu = \mathrm{KL}(\nu\mid\rho_\theta) \ge 0$. This is [](#eq-gt-L).
:::

## Proof of the theorem

:::{prf:proof} Proof of [](#thm:sol-gaussian-target)
Let $\mu$ be absolutely continuous, in $\Ptwo{d}$, and a critical point of
$\SW_2^2(\cdot, N(m,\Sigma))$. For each $\theta$ set

$$
L_\theta = s_\theta^2\Big(1 - \int T_\theta'\dd\mu_\theta\Big) + \int (y - m_\theta)(T_\theta(y) - y)\dd\mu_\theta(y).
$$

The function $\theta \mapsto s_\theta^2\int T_\theta'\dd\mu_\theta$ is nonnegative with finite
integral by [](#eq-gt-II). The functions $s_\theta^2$ and the second term of $L_\theta$ are
bounded ([](#lem:gt-identities)). Hence $L$ is $\sigma$-integrable, and by [](#eq-gt-II) and
[](#eq-gt-I),

$$
\int L_\theta \dd\sigma(\theta) = \frac{\operatorname{tr}\Sigma}{d} - \frac{\operatorname{tr}\Sigma}{d} + 0 = 0 .
$$

Let $G$ be the set of $\theta$ with $\int T_\theta'\dd\mu_\theta < \infty$, so $\sigma(G) = 1$
([](#lem:gt-identities)). For $\theta \in G$, [](#lem:gt-one-dim) gives $L_\theta \le -\tfrac12 E_\theta$,
with $E_\theta = \int \abs{T_\theta(y) - y}^2\dd\mu_\theta \ge 0$; $\theta\mapsto E_\theta$ is
measurable by Tonelli. So $0 = \int L\dd\sigma \le -\tfrac12\int E_\theta\dd\sigma \le 0$, and
$E_\theta = 0$ for $\sigma$-a.e. $\theta$. For such $\theta$, $T_\theta = \Id$ $\mu_\theta$-a.e., so
$\rho_\theta = (T_\theta)_\#\mu_\theta = \mu_\theta$ by [](#lem:gt-monotone) (2).

Let $G'$ be the set of $\theta$ with $\mu_\theta = \rho_\theta$. It has full $\sigma$-measure, so it
is dense in $\Sph{d-1}$, since $\sigma$ charges every nonempty open set. For $\xi = t\theta \ne 0$
choose $\theta_n \in G'$ with $\theta_n \to \theta$. Then
$\hat\mu(t\theta_n) = \hat\mu_{\theta_n}(t) = \hat\rho_{\theta_n}(t) = \hat\rho(t\theta_n)$, and by
continuity of characteristic functions $\hat\mu(\xi) = \hat\rho(\xi)$. So $\hat\mu = \hat\rho$, and
$\mu = \rho$ by Lévy's uniqueness theorem.
:::

## Remarks

:::{prf:remark} Where absolute continuity of $\mu$ is used
:label: rem:gt-where-ac
The hypothesis $\mu \ll \Leb$ is used at exactly three places.

- (a) [](#lem:gt-domain) (1): $\mu(H) = 0$ for hyperplanes. This makes the $\mu_\theta$
  absolutely continuous and $F$ jointly continuous.
- (b) [](#lem:gt-domain) (2): $U \ne \emptyset$ and $\mu(\partial C) = 0$, so $\mu(U) = 1$ and
  $\mu(Z) = 1$.
- (c) [](#lem:gt-stampacchia): the transfer of "$DV = 0$ Lebesgue-a.e. on $Z$" into
  "$DV = 0$ $\mu$-a.e.".

(a) alone is not enough: it holds for the sphere below. The decisive uses are (b) and (c). They
are what turns the order-zero condition $V = 0$ on $Z$ into the order-one condition $A = I$.
The order-one condition then yields [](#eq-gt-II).
:::

:::{prf:remark} Audit: the critical sphere
:label: rem:gt-sphere-audit
Let $\mu$ be the uniform probability on $r\Sph{d-1}$, $d \ge 2$, and $\rho = N(0, I_d)$, the
configuration of [](#prop:critical-sphere). Run the argument on it.

- (a) of [](#rem:gt-where-ac) holds: a hyperplane meets the sphere in a $\mu$-null set. So
  $F$ is jointly continuous and every $\mu_\theta$ is absolutely continuous.
- [](#lem:gt-monotone)–[](#lem:gt-sobolev) hold verbatim on $U = B(0,r)$. Their proofs use
  only (a) and $K \subset U$. So $V \in W^{1,1}_{\mathrm{loc}}(B(0,r))$.
- The argument **breaks at (b)**: $C = \bar B(0,r)$, and $\mu$ is carried by $\partial C$. So
  $\mu(U) = 0$ and $Z = U \cap S = \emptyset$. [](#lem:gt-stampacchia) yields nothing. The
  criticality information lives on $\partial U$, where no Sobolev structure is available, and
  $\partial U$ is Lebesgue-null, so (c) could not transfer anything even if it were.
- Identity [](#eq-gt-I) still holds for the sphere, written with $v_\mu$ in place of $V$:
  its proof pairs $v_\mu = 0$ $\mu$-a.e. with $x - m$ and uses only that the $\mu_\theta$ have
  no atom (so $\bar\gamma_\theta = T_\theta$) and the second moments. [](#lem:gt-one-dim) and the
  final step only involve the one-dimensional laws $\mu_\theta$, which are absolutely
  continuous; they apply to every $\theta$ with $\int T_\theta'\dd\mu_\theta < \infty$.
- Hence, if the sphere is critical as [](#prop:critical-sphere) asserts, [](#eq-gt-II) must
  fail for it: the step that the sphere defeats is precisely the passage through
  [](#lem:gt-stampacchia). For $d = 3$ this is visible directly. There
  $\mu_\theta = \mathrm{Unif}[-r, r]$ and $T_\theta$ maps $(-r, r)$ onto $\R$, so
  $\int T_\theta'\dd\mu_\theta = \frac{1}{2r}\lim_{y\uparrow r}\big(T_\theta(y) - T_\theta(-y)\big) = +\infty$
  for every $\theta$.

This bullet list is a consistency check, not part of the proof. [](#prop:critical-sphere) is
not certified here and nothing above rests on it.
:::

:::{prf:remark} Audit: the critical segments
:label: rem:gt-segments-audit
Let $\mu$ be the law of $(Z,0,\dots,0)$, $Z \sim N(0,\alpha_d^2)$, and $\rho = N(0, I_d)$,
$d \ge 2$. By [](#prop:critical-segments) (2), $\mu$ is a critical point for a Gaussian target.
The argument **breaks at (a) and (b)**.

- For $\theta \perp e_1$, $\mu_\theta = \delta_0$ has an atom. Then $T_\theta$ is not the
  barycentric projection, and $F$ is not jointly continuous.
- $C$ is the line $\R e_1$. So $U = \emptyset$, and the set where $v_\mu = 0$ is
  Lebesgue-null: (c) transfers nothing.

The disc segment of [](#prop:critical-segments) (1) fails in the same two places. Its target
is not Gaussian, so the theorem does not concern it anyway.

The same holds for any $\mu$ carried by a hyperplane, for any $\Sigma$: such a $\mu$ is exactly
where (b) fails, and the theorem says nothing about it.
:::

:::{prf:remark} What the Gaussian structure buys
:label: rem:gt-gaussian-role
The Gaussian form of $\rho$ is used in three places.

- (i) $Q_\theta$ is $C^1$ on $(0,1)$, with $Q_\theta' = 1/g_\theta(Q_\theta)$. So $T_\theta$ is
  continuous and locally absolutely continuous on $I_\theta$, $DV$ has no singular part, and
  Stampacchia's lemma applies in $W^{1,1}$. This needs every $\rho_\theta$ to have a positive
  density on $\R$, not more.
- (ii) In [](#lem:gt-one-dim), $\log g_\theta$ is a quadratic polynomial. So the pairing with
  $x - m$, which is linear in $x$, produces the potential part of
  $\mathrm{KL}(\cdot\mid\rho_\theta)$ in every direction at once.
- (iii) The trace is taken against the constant matrix $\Sigma$. The weight it produces,
  $\theta^\top\Sigma\theta$, is the variance of $\rho_\theta$, which is the weight the entropy term of
  [](#lem:gt-one-dim) needs.

For a non-Gaussian $\rho$, (ii)–(iii) would require the one-dimensional scores
$(\log g_\theta)'(\inner{x}{\theta})$ to combine linearly into a single field $M\nabla\log\rho(x)$ on
$\R^d$. We neither prove nor use that this characterizes Gaussians.
:::

:::{prf:remark} No entropy assumption
:label: rem:gt-no-entropy
For $\Sigma = I_d$, $m = 0$, this recovers the conclusion of [](#thm:cs-isotropic) without its
finite-entropy hypothesis. Finiteness of the entropy is deduced, and only for the projections
$\mu_\theta$ with $\theta \in G$, in [](#lem:gt-one-dim). Nothing is claimed about the entropy of
$\mu$ itself. No flow, and no well-posedness of any flow, enters the proof. The heuristic
behind it is the dissipation of $\mathrm{KL}(\cdot\mid\rho)$ along the preconditioned velocity
$\Sigma v_\mu$. That heuristic is replaced by [](#lem:gt-stampacchia), which avoids any
integration by parts against $\mu$.
:::

:::{prf:remark} Reading of the definition
:label: rem:gt-definition-reading
[](#lem:gt-representative) reads [](#def:barycentric-field) as requiring a
$\mu\otimes\sigma$-measurable version of $(x,\theta) \mapsto \bar\gamma_\theta(\inner{x}{\theta})$,
without which the integral defining $v_\mu$ has no meaning. Every such version gives the same
$v_\mu$ up to a $\mu$-null set. This is a reading of the definition, not an open step. It is
recorded so that a reviewer can check it against the manuscript.
:::

**Fences respected.** [](#thm:gaussian-target) has no `bounded_by`. The fences of the target,
[](#prop:critical-segments) (proved) and [](#prop:critical-sphere) (open), exhibit critical
points for $\rho = N(0, I_d)$ that are not absolutely continuous. The theorem assumes
$\mu \ll \Leb$ and so does not contradict them. [](#rem:gt-sphere-audit) and
[](#rem:gt-segments-audit) locate the step each of them defeats.
