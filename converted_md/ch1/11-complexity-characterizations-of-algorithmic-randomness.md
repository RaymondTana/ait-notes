---
title: "Complexity Characterizations of Algorithmic Randomness"
label: section:Complexity_Characterizations_of_Algorithmic_Randomness
---

## Algorithmic Discrepancies

We fix some notation for the quantitative discrepancy between a finitary object's algorithmic entropy and its mass according to some premeasure.

:::{prf:definition}
Let $\rho$ be a premeasure on $2^\omega$. Define for any $\sigma \in 2^{<\omega}$ its:

- **A priori discrepancy**: $\operatorname{\Delta M}_\rho(\sigma) := \operatorname{KM}(\sigma) + \log \rho([\sigma]) = \log \frac{\rho([\sigma])}{\mathbf{M}(\sigma)}$,
- **Prefix discrepancy**: $\operatorname{\Delta P}_\rho(\sigma) := K(\sigma) + \log \rho([\sigma]) =^* \log \frac{\rho([\sigma])}{\mathbf{m}(\sigma)}$.
:::

When $\rho = \rho_s$, simply write $\operatorname{\Delta M}_s$ and $\operatorname{\Delta P}_s$.

## Complexity Characterizations of Algorithmic Randomness

It turns out that these algorithmic discrepancies characterize the various $s$-dimensional randomness notions defined above.

:::{prf:theorem}
:label: theorem:complexity_characterizations_of_randomness
Let $s \geq 0$ be left-c.e. and $x \in 2^\omega$. Then $x$ is:

- ML-$s$-random $\iff$ $x$ is weak Chaitin-$s$-random: $\operatorname{\Delta P}_s(\restrict{x}{r}) \geq O(1)$, {cite:p}`Tad02`;
- Solovay-$s$-random $\iff$ $x$ is strong Chaitin-$s$-random: $\operatorname{\Delta P}_s(\restrict{x}{r}) \to \infty$, {cite:p}`Tad02; CST06`;
- Strong ML-$s$-random $\iff$ $\operatorname{\Delta M}_s(\restrict{x}{r}) \geq O(1)$, {cite:p}`CST06`;
- Vehement ML-$s$-random $\iff$ $x$ is strong ML-$s$-random;
- Strong Solovay-$s$-random $\iff$ $\operatorname{\Delta M}_s(\restrict{x}{r}) \to \infty$, {cite:p}`MR09`.
:::

In light of these characterizations, one may argue on the level of discrete or continuous semimeasures rather than covers in order to effectivize results on Hausdorff dimension.
