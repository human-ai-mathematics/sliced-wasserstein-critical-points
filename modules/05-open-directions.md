% Open directions, in prose only: the precise tentative statements live in the research
% record (research/explorations/), not here. No labelled claim directive in this module
% until a statement is promoted.

(sec:open-directions)=
# Where the general case resists

What is proved covers Gaussian targets, radial measures in dimension three, and radial
measures in the plane whose support is a full disc. Four configurations are the natural
next steps. None is settled here.

**The annulus in the plane.** Let $\mu$ and $\rho$ be radial in $\R^2$, with $\mu$ supported on
an annulus $\{c \le \abs{x} \le R\}$, $c > 0$. The condition of [](#thm:radial-disc-d2) becomes
an Abel equation on $[c^2, R^2]$ only, and it no longer forces the monotone map to be the
identity: for any smooth $\Phi$ compactly supported in $(0, c^2)$, the function
$U = \tfrac1\pi A[\Phi']$, with $A$ the Abel transform, solves it exactly on the whole annulus.
What survives is a sign condition: the map must push the projection of $\mu$ to the
projection of a *positive* radial measure, and in the plane that is the nonnegativity of an
inverse Abel transform inside the hole. Whether that sign condition, which is non-local,
forces the identity is the question. When the support is a disc and an annulus,
$\{\abs{x} \le a\} \cup \{c \le \abs{x} \le R\}$ with $0 < a < c$, the local form of
[](#thm:radial-disc-d2) still makes the map the identity on $(-a,a)$, and the same family
leaves it free on the outer annulus.

**Radial measures in odd dimension $d \ge 5$.** The condition stays local, so the monotone
map is the identity on the radial support, as in dimension three. On each hole $(a,b)$ one
still has $h(a) = h(b) = 0$ and $\int_a^b h(u)\,u^{2j+1} \dd u = 0$ for $j = 0, \dots, (d-3)/2$,
but the projected density is no longer constant there, and convexity is lost. It would
suffice that $h$ change sign at most $(d-3)/2$ times on each hole.

**Targets beyond Gaussians.** The proof of [](#thm:gaussian-target) pairs the condition with
a linear field and takes a trace against a constant matrix; both steps use that every
projected target has a quadratic logarithm. With a constant matrix we expect this to
single out Gaussian targets, though we have not proved it. A matrix field $M(x)$ varying
with $x$, or a log-concave target, is the first thing to try; the constraint that
$\theta^\top M(x)\theta$ depend only on $\inner{x}{\theta}$ is very rigid.

**A small mass in a hole.** A counterexample, if one exists, must have a support with
holes. Numerical searches in the plane, with $\mu$ fixed and $\rho$ optimized, leave the field
bounded away from zero in every configuration where refinement is conclusive. At first
order, criticality asks that the potential of the kernel $\abs{x}$ be constant on the
support of $\mu$, and sweeping a mass onto that support by this kernel produces singular
layers on its boundary, never a density. The one regime where the computations are not
conclusive is a small target mass, at most five per cent, placed in a hole of the support
of $\mu$. These are observations, not proofs.
