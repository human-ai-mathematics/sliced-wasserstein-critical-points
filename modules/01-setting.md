% The normalizations every statement rests on, and the equivalence of the notions of
% critical point. The content of each labelled directive is fixed (orchestrator); the
% prose is the writer's.

(sec:setting)=
# Setting and normalizations

Throughout, $d \ge 1$, $\Ptwo{d}$ is the set of Borel probability measures on $\R^d$ with
finite second moment, and $\Leb$ is the Lebesgue measure. A measure is *absolutely
continuous* when it is absolutely continuous with respect to $\Leb$.

:::{prf:definition} Sliced Wasserstein distance
:label: def:sliced-wasserstein
Let $\sigma$ be the uniform probability measure on the unit sphere $\Sph{d-1}$ of $\R^d$.
For $\theta \in \Sph{d-1}$, let $P_\theta(x) = \inner{x}{\theta}$ and, for a measure $\mu$
on $\R^d$, let $\mu_\theta = (P_\theta)_\#\mu$. For $\mu, \rho \in \Ptwo{d}$,

$$
\SW_2^2(\mu,\rho) = \int_{\Sph{d-1}} W_2^2(\mu_\theta, \rho_\theta) \dd\sigma(\theta),
$$

where $W_2$ is the quadratic Wasserstein distance on $\R$.
:::

With $\sigma$ a probability, $\int \inner{x}{\theta}\,\theta \dd\sigma(\theta) = x/d$ for every
$x \in \R^d$. This identity fixes the factor $d$ below.

:::{prf:definition} Barycentric field
:label: def:barycentric-field
Let $\mu, \rho \in \Ptwo{d}$. For $\theta \in \Sph{d-1}$, let $\gamma_\theta$ be the optimal
plan between $\mu_\theta$ and $\rho_\theta$ for the cost $\abs{s-t}^2$, which is unique,
and let $\bar\gamma_\theta(s) = \int t \dd\gamma_\theta(t \mid s)$ be its barycentric
projection, defined for $\mu_\theta$-almost every $s$. When $\mu_\theta$ has no atom,
$\bar\gamma_\theta = T_\theta := Q_{\rho_\theta} \circ F_{\mu_\theta}$ $\mu_\theta$-almost
everywhere, where $F_{\mu_\theta}$ is the distribution function of $\mu_\theta$ and
$Q_{\rho_\theta}$ the quantile function of $\rho_\theta$: $T_\theta$ is the monotone
transport map from $\mu_\theta$ to $\rho_\theta$. The *barycentric field* of $\mu$ relative
to $\rho$ is

$$
v_\mu(x) = x - d \int_{\Sph{d-1}} \bar\gamma_\theta(\inner{x}{\theta})\,\theta \dd\sigma(\theta),
$$

defined for $\mu$-almost every $x \in \R^d$.
:::

The factor $d$ is the one for which $v_\rho = 0$: when $\mu = \rho$, every $\bar\gamma_\theta$
is the identity. Equation (16) of {cite:t}`VauthierKorbaMerigot2025` prints the factor
$1/d$; their own computations (Appendix B.9) use $d$, which is the normalization adopted here.
Only the zero set of $v_\mu$ matters for what follows, and $-v_\mu/d$ is, up to that factor,
the velocity of the Wasserstein gradient flow of $\tfrac12\SW_2^2(\cdot,\rho)$.

:::{prf:definition} Critical points
:label: def:critical-point
Let $\mu, \rho \in \Ptwo{d}$.

1. $\mu$ is a *critical point* of $\SW_2^2(\cdot,\rho)$ when $v_\mu = 0$ $\mu$-almost
   everywhere, with $v_\mu$ the barycentric field of $\mu$ relative to $\rho$.
2. $\mu$ is a *Lagrangian critical point* of $\SW_2^2(\cdot,\rho)$ when, for every
   $\xi \in L^2(\mu;\R^d)$, the right derivative of
   $t \mapsto \SW_2^2((\Id + t\xi)_\#\mu, \rho)$ at $t = 0$ vanishes.
3. $\mu$ is a *Wasserstein critical point* of $\SW_2^2(\cdot,\rho)$ when, along every
   constant-speed geodesic $(\mu_t)_{t \in [0,1]}$ of $(\Ptwo{d}, W_2)$ with $\mu_0 = \mu$,
   the right derivative of $t \mapsto \SW_2^2(\mu_t, \rho)$ at $t = 0$ vanishes.
:::

The first notion is the barycentric Lagrangian critical point of
{cite:t}`VauthierKorbaMerigot2025` (Definition 4.2), the second is their Definition 4.1.
For an absolutely continuous $\mu$, the first is also the stationarity condition of the
Wasserstein gradient flow written by {cite:t}`Bonnotte2013` (Section 5.7.1). The three
notions agree on the measures the main question is about:

:::{prf:proposition} The notions of critical point coincide
:label: prop:notions-coincide
Let $\mu, \rho \in \Ptwo{d}$.

1. If $\mu$ is a Lagrangian critical point, or a Wasserstein critical point, of
   $\SW_2^2(\cdot,\rho)$, then it is a critical point of $\SW_2^2(\cdot,\rho)$.
2. If $\mu$ has no atom, the three notions of critical point of
   $\SW_2^2(\cdot,\rho)$ coincide.
:::

No compact support and no density of $\rho$ are assumed. Part of this is known.
{cite:t}`VauthierKorbaMerigot2025` (Corollary 4.8) prove that a Lagrangian critical point is a
critical point, for every $\mu$ and $\rho$, and the converse when $\mu$ and $\rho$ are both
compactly supported and have no atom. The statement above adds the Wasserstein notion, which
we did not find related to the other two for $\SW_2^2$ in the literature, and for the converse
keeps only the hypothesis that $\mu$ has no atom.

**Idea of the proof.** Testing a perturbation $(\Id + t\xi)_\#\mu$ against a coupling built
direction by direction gives the upper bound

$$
\SW_2^2((\Id + t\xi)_\#\mu, \rho) \le \SW_2^2(\mu,\rho)
+ \tfrac{2t}{d}\inner{v_\mu}{\xi}_{L^2(\mu)} + \tfrac{t^2}{d}\norm{\xi}_{L^2(\mu)}^2 .
$$

The field $w = \Id - v_\mu$ has a cyclically monotone graph, because each $\bar\gamma_\theta$
is nondecreasing; so $t \mapsto (\Id - t v_\mu)_\#\mu$, $t \in [0,1]$, is a Wasserstein
geodesic issued from $\mu$. (A close analogue: for an absolutely continuous measure,
{cite:t}`LiMoosmullerWang2023` show that the map matching the slices along an orthonormal
basis, and its convex combinations with the identity, are optimal transport maps.) Along it, either notion of criticality and the upper bound give
$0 \le -\tfrac2d\norm{v_\mu}^2$, hence $v_\mu = 0$. This part uses no hypothesis on $\mu$.

For the converse, a measure with no atom has atomless projections in almost every
direction. For an atomless source on the line, a one-dimensional bathtub argument gives the
first variation of $W_2^2$ exactly; integrated over directions, it gives the right derivative
of $\SW_2^2$ along the displacement interpolation of *any* coupling $\gamma$ of $\mu$ with
another measure: $\tfrac2d\int\inner{v_\mu(x)}{y-x}\dd\gamma(x,y)$. Since every Wasserstein
geodesic is the displacement interpolation of an optimal coupling, whether or not that
coupling is induced by a map, no appeal to Brenier's theorem is needed, and absolute
continuity enters only through the absence of atoms. The hypothesis cannot be dropped for the
Wasserstein notion: $\delta_0$ is a critical point for every centred target $\rho \ne \delta_0$,
and $\SW_2^2$ decreases strictly along the geodesic from $\delta_0$ to $\rho$.

% Source: ensae-conjecture-scouting/verification/13-korba-sw/1-relecture.md, §2 (Prop. A).
