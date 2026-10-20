% The manuscript's first module and the first page a reader sees. Every labelled claim
% directive in modules/ is a ledger node with the same id (SPECIFICATION.md, Formats →
% Ledger); its content is fixed, the prose around it is the writer's (Manuscript). The
% status next to each statement is displayed from the ledger: the prose never states one.

(sec:overview)=
# Orientation

+++ {"part": "abstract"}

The squared sliced Wasserstein distance to a target measure $\rho$ averages, over all
directions, the one-dimensional transport cost between the projections of a measure and of
$\rho$. It has critical points other than $\rho$, but every one known is singular. We ask
whether an absolutely continuous critical point must be the target itself, a question of
Vauthier, Korba and Mérigot. This document states the question precisely, proves it for
every Gaussian target and for several classes of radial measures, and says where the
general case resists.

+++

## The question

Let $\rho$ be a probability measure on $\R^d$, $d \ge 2$. For a direction $\theta$ on the unit
sphere, project a measure $\mu$ and the target $\rho$ on the line spanned by $\theta$, and
let $T_\theta$ be the monotone map carrying the first projection onto the second. A measure
$\mu$ is a *critical point* of $\SW_2^2(\cdot,\rho)$ when, at $\mu$-almost every point $x$, the
average of the one-dimensional displacements vanishes:

$$
x = d \int_{\Sph{d-1}} T_\theta(\inner{x}{\theta})\,\theta \dd\sigma(\theta),
$$

with $\sigma$ the uniform probability on the sphere ([](#def:critical-point)). The target is
a critical point, since then every $T_\theta$ is the identity. The question
([](#conj:sw-critical)) is whether it is the only absolutely continuous one.

## An example worked by hand

Critical points other than the target exist, and the simplest one shows what the question
is about. Take $d = 3$, the standard Gaussian target $\rho = N(0, I_3)$, and for $\mu$ the
uniform probability on the sphere of radius $r$.

Every projection of $\mu$ is the uniform law on $[-r, r]$: this is Archimedes' theorem on
the sphere and the circumscribed cylinder. Every projection of $\rho$ is $N(0,1)$. So all the
monotone maps are the same,

$$
T(u) = \Phi^{-1}\!\Big(\frac{1 + u/r}{2}\Big), \qquad -r \le u \le r,
$$

with $\Phi$ the standard normal distribution function. At a point $x = r e$ of the sphere,
the condition is invariant under the rotations fixing $e$, so only its component along $e$
matters. Under $\sigma$, $s = \inner{e}{\theta}$ is uniform on $[-1,1]$ (Archimedes again),
and $T$ is odd, so

$$
d \int_{\Sph{2}} T(\inner{re}{\theta})\inner{\theta}{e} \dd\sigma(\theta)
= 3 \int_0^1 T(rs)\, s \dd s
= 3 \int_0^1 \Phi^{-1}\!\Big(\frac{1+s}{2}\Big) s \dd s .
$$

The right-hand side does not depend on $r$. Substituting $s = 2\Phi(z) - 1$, with
$\varphi = \Phi'$,

$$
\int_0^1 \Phi^{-1}\!\Big(\frac{1+s}{2}\Big) s \dd s
= \int_0^\infty z\,\big(2\Phi(z) - 1\big)\, 2\varphi(z) \dd z
= \frac{1}{\sqrt\pi},
$$

using $\int_0^\infty z\varphi = \varphi(0)$ and, after an integration by parts,
$\int_0^\infty z\varphi\Phi = \tfrac12\varphi(0) + \int_0^\infty \varphi^2 = \tfrac{1}{2\sqrt{2\pi}} + \tfrac{1}{4\sqrt\pi}$.
The condition $r = 3/\sqrt\pi$ thus has exactly one solution: the uniform measure on the
sphere of radius $r_* = 3/\sqrt\pi \approx 1.6926$ is a critical point, and it is not the target
(compare [](#prop:critical-sphere), for every dimension).

Two features of this example frame the question. Its projections are absolutely continuous,
so criticality cannot be read on the projections alone. And the condition holds on the
sphere and nowhere else: off the support of $\mu$, nothing is asked. A measure with a
density spreads over a set with interior, and the conjecture is that this alone pins it to
the target. In dimension three, for radial measures, that is exactly what happens: the
sphere escapes only because its radial support is a single isolated point
([](#thm:radial-d3)).

## Main results

The general question ([](#conj:sw-critical)) is not settled here. What is proved:

- the usual notions of critical point coincide for every measure with no atom
  ([](#prop:notions-coincide)), so the question does not depend on which one is used;
- for the standard Gaussian target, the uniform sphere of radius $r_* = d\,A_d < \sqrt d$ is
  critical, and no other sphere centred at the origin is ([](#prop:critical-sphere), Example 1
  of {cite:t}`DiazMartinMurphy2026`, reproved here with the uniqueness and the bound);
- every Gaussian target, isotropic or not, is the only absolutely continuous critical point
  for itself, with no entropy hypothesis ([](#thm:gaussian-target));
- in dimension three, a rotation-invariant critical point whose radial law has no atom is the
  target ([](#thm:radial-d3));
- in the plane, a rotation-invariant critical point whose support is a full disc or the whole
  plane is the target ([](#thm:radial-disc-d2)).

Several proofs give somewhat more than the statement, as the text after each one says.
These proofs have been checked by independent reviews carried out by AI agents, not yet by
a human reader. Where we found earlier results covering part of a statement, the text after
it cites them; beyond those, we did not find these statements in the literature we searched,
which is not a claim that they are new.

## How this document is organized

[](#sec:setting) fixes the normalizations and shows that the usual notions of critical point
coincide for measures with no atom. [](#sec:target) states the question.
[](#sec:singular) collects the singular critical points, which show why absolute continuity is
needed. [](#sec:special-targets) treats the cases with full support, Gaussian targets and
radial measures. [](#sec:open-directions) describes where the general case resists.

## How results are checked

A statement counts as proved here only once a reviewer other than the author of its proof
has checked that proof in full against the precise statement, or once a named person has
read it and vouches for it; the status next to each statement says which, and links to the
proof. At present every proof given here was checked by such a review conducted by an AI
agent, which the status names with the model and the date; none has yet been read by a
human reviewer. Numerical computations are reported as evidence and never as proof.

To contribute — a counterexample, an idea, a correction — name the statement by the label
displayed next to it.
