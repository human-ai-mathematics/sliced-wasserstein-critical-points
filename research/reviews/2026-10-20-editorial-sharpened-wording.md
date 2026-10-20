---
verdict: editorial
amends:
  - research/reviews/2026-10-20-sharpened-statements-rereview.md
authors:
  - researcher, claude-opus-5-5, 2026-10-20
reviewer: reviewer, claude-opus-5-5, 2026-10-20
changes:
  solutions/thm-radial-d3.md: {from: 6f0a737fa248491be1e86f068221b62a124df93afbd9090484cfa9b2a5e211e5, to: d25b47f0c7e477a992f80f580cd9cb7b6fec23e48086a6e3dfb173f028a5610b}
  solutions/thm-radial-disc-d2.md: {from: 8cd85ab627d2b0d8c872334ac0c9df0e9dddf05d2485ffbd25b3b2ed97f89b9a, to: 9e183e25d27e9de3854c5e4d03d56ea37d491382f902a429c080d5dcd42cae7c}
---

# Editorial note on `research/reviews/2026-10-20-sharpened-statements-rereview.md`

Fresh context; I wrote none of the dossiers or the amended report. `check.py --diff` verified
the baseline (`34459d636c45`) against the report's fingerprints; `check.py --impact` names no
changed manuscript statement (`thm:radial-d3`, `thm:radial-disc-d2` and `def:critical-point`
fingerprint as the report records). The diffs below are its output. The edits apply the
report's Corrections 2 and 3.

Of the three dossiers edited in this pass, `solutions/prop-critical-sphere.md` is **not**
carried over. The closing sentence of the proof of `thm:sol-cs-main` (l. 347–349) is a step of
proof, and its inference changed: it used to conclude the proposition from "$r_* > 0$ and
$\mu_{r_*}$ is a Wasserstein critical point". It now concludes from items 1, 3 and 4, with new
premises (all three notions, uniqueness over every radius, the $d = 3$ value). This is a
changed step, not a reworded sentence, so it takes a re-review.

## `solutions/thm-radial-d3.md`

```diff
@@ -11,9 +11,9 @@
 % (see the proofs[] record in the ledger). Normalizations: those of
 % def:sliced-wasserstein and def:barycentric-field (sigma a probability, factor d = 3).
 
-**Overview.** We prove [](#thm:radial-d3) in a slightly sharper form,
-[](#thm:sol-radial-d3): instead of "the law of $\abs{X}$ has no atom" it suffices that this law
-has no atom at $0$ and that its support has no isolated point. The target $\rho$ is any
+**Overview.** We prove [](#thm:radial-d3) as [](#thm:sol-radial-d3), under its hypotheses:
+the law of $\abs{X}$ has no atom at $0$ and its support has no isolated point; "the law of
+$\abs{X}$ has no atom" is the special case named in its final clause. The target $\rho$ is any
 rotation-invariant measure of $\Ptwo{3}$: atoms (necessarily at $0$), singular parts and
 unbounded supports are allowed, and $\mu$ need not be absolutely continuous nor compactly
 supported. The steps are:
@@ -78,7 +78,7 @@
 
 ## Statement
 
-**Refined statement.** [](#thm:sol-radial-d3) below contains [](#thm:radial-d3): if the law
+**Refined statement.** [](#thm:sol-radial-d3) below is [](#thm:radial-d3), and its final clause holds: if the law
 $\mu_{\mathrm{rad}}$ of $\abs{X}$ has no atom, then $\mu_{\mathrm{rad}}(\{0\}) = 0$ and its support
 has no isolated point (an isolated point $r$ of the support has a neighbourhood $U$ with
 $\mu_{\mathrm{rad}}(U) = \mu_{\mathrm{rad}}(\{r\}) > 0$). The hypotheses on $\rho$ are those of
@@ -443,7 +443,7 @@
 - Atoms of $\mu_{\mathrm{rad}}$ at points of $(0,\infty)$ that are not isolated in $K$ are
   allowed: for instance $\mu_{\mathrm{rad}} = \tfrac12\delta_1 + \tfrac12\mathrm{U}[1,2]$, a
   measure that is not absolutely continuous, is covered. Their projections are still
-  atomless. This is the sharpening over [](#thm:radial-d3).
+  atomless. This is why [](#thm:radial-d3) does not require the radial law to be atomless.
```

Why the mathematics is unchanged: the theorem `thm:sol-radial-d3`, its hypotheses, the
argument that an atomless radial law satisfies them (l. 81–84, untouched) and every proof
step read the same. Only the description of how the theorem relates to the sharpened
manuscript statement changed: "sharper form"/"contains"/"sharpening" became "is". The report
checked that identity (hypothesis (H) word for word).

## `solutions/thm-radial-disc-d2.md`

```diff
@@ -12,8 +12,8 @@
 % Normalizations: def:sliced-wasserstein (sigma a probability) and def:barycentric-field
 % (factor d = 2 in v_mu).
 
-**Overview.** We prove [](#thm:radial-disc-d2) in a sharper form, [](#thm:sol-rd2-main):
-absolute continuity of $\mu$ is replaced by $\mu(\{0\}) = 0$; $\rho$ is an arbitrary radial
+**Overview.** We prove [](#thm:radial-disc-d2) as [](#thm:sol-rd2-main):
+absolute continuity of $\mu$ is not assumed, only $\mu(\{0\}) = 0$; $\rho$ is an arbitrary radial
 measure of $\Ptwo{2}$ (no density, atoms allowed, unbounded support allowed); the disc may
 have any radius $R \in (0,\infty)$, or be the whole plane ($R = \infty$). A local version,
 [](#prop:sol-rd2-local), shows that the monotone map is the identity on $(-a,a)$ as soon as
@@ -99,9 +99,9 @@
 critical point of $\SW_2^2(\cdot,\rho)$ ([](#def:critical-point)), then $\mu = \rho$.
 :::
 
-This implies [](#thm:radial-disc-d2): an absolutely continuous $\mu$ has $\mu(\{0\}) = 0$, and
-its support, a closed disc centred at $0$ or the plane, is not $\{0\}$, so the disc has a
-radius $R > 0$. No hypothesis on $\rho$ beyond radial symmetry and a finite second moment is
+This is [](#thm:radial-disc-d2): its hypothesis $\mu(\{0\}) = 0$ is the manuscript's, and its
+support is a closed disc centred at $0$ of radius $R > 0$, hence not $\{0\}$, or the plane;
+absolute continuity of $\mu$ is not assumed. No hypothesis on $\rho$ beyond radial symmetry and a finite second moment is
 used; no density of $\mu$ is used either.
```

Why the mathematics is unchanged: `thm:sol-rd2-main`, its hypotheses and every proof step
read the same. Only the prose linking it to the manuscript changed: the bridge from absolute
continuity to $\mu(\{0\}) = 0$, which the old statement needed, is dropped. The statement no
longer assumes absolute continuity, and the report checked that the theorem matches it
exactly.
