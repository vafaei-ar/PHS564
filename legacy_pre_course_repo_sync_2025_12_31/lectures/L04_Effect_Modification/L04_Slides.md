# L04 — Effect modification and effect-measure modification

## Slide 1 — Title
- PHS564: Causal Inference Methods in Epidemiologic Research
- Lecture 04: Effect modification and effect-measure modification
Speaker notes:
- Today we move beyond the "average" effect to look at how treatment effects might differ across subgroups of the population.

## Slide 2 — Why heterogeneity matters
- Targeting: Which patients benefit most from a drug?
- Equity: Does an intervention work equally well for all demographic groups?
- Mechanisms: Does the effect vary by a biological marker?
Speaker notes:
- Figure title: Heterogeneity Icons; type: Draw (vector); file path: figures/L04/hetero_icons.png; what it shows: icons for target, scales of equity, and biology; alt-text: Three icons representing why effect modification is important.

## Slide 3 — Definitions
- Effect Modification: The causal effect of $A$ on $Y$ varies across levels of $V$.
- Interaction: The joint effect of two interventions ($A$ and $B$) is different from the sum of their individual effects.
- Effect-Measure Modification (EMM): Heterogeneity depends on the scale (RD vs RR).
Speaker notes:
- Figure title: Definitions Panel; type: Draw (vector); file path: figures/L04/definitions_panel.png; what it shows: three boxes with definitions; alt-text: Definitions of effect modification, interaction, and EMM.

## Slide 4 — Scale dependence
- A treatment can show effect modification on the Risk Difference (RD) scale but NOT on the Risk Ratio (RR) scale, and vice versa.
- Public health often cares about RD (absolute burden).
- Biology often cares about RR (relative change).
Speaker notes:
- Figure title: RD/RR Panel; type: Draw (vector); file path: figures/L04/scale_panel.png; what it shows: RD and RR formulas side-by-side; alt-text: Contrast between absolute and relative scales.

## Slide 5 — Numeric example setup
- Stratum $V=0$ (Men):
  - Risk if Treated: 0.20
  - Risk if Untreated: 0.10
- Stratum $V=1$ (Women):
  - Risk if Treated: 0.60
  - Risk if Untreated: 0.30
Speaker notes:
- Figure title: 2x2 Tables; type: Draw (vector); file path: figures/L04/strata_tables.png; what it shows: two tables with risks for each stratum; alt-text: Risks of outcome by treatment in two different strata.

## Slide 6 — Compute RD by stratum
- Men ($V=0$): $RD = 0.20 - 0.10 = 0.10$
- Women ($V=1$): $RD = 0.60 - 0.30 = 0.30$
- Conclusion: Effect modification on the RD scale (0.30 vs 0.10).
Speaker notes:
- Figure title: RD Arithmetic; type: Draw (vector); file path: figures/L04/rd_arithmetic.png; what it shows: step-by-step subtraction; alt-text: Calculation of risk differences in two strata.

## Slide 7 — Compute RR by stratum
- Men ($V=0$): $RR = 0.20 / 0.10 = 2.0$
- Women ($V=1$): $RR = 0.60 / 0.30 = 2.0$
- Conclusion: NO effect modification on the RR scale (both are 2.0).
Speaker notes:
- Figure title: RR Arithmetic; type: Draw (vector); file path: figures/L04/rr_arithmetic.png; what it shows: step-by-step division; alt-text: Calculation of risk ratios in two strata.

## Slide 8 — Visualize risks by stratum
- Bar plot showing how treatment effect (the gap between bars) changes by group.
Speaker notes:
- Figure title: Risk by Group; type: From notebook; file path: figures/L04/risk_by_group.png; what it shows: grouped bar chart of risks; alt-text: A bar chart visualizing risk heterogeneity.

## Slide 9 — Interpretation guidance
- Which scale to use?
- If the goal is policy/resource allocation $\rightarrow$ RD.
- If the goal is biological mechanism $\rightarrow$ RR.
Speaker notes:
- Figure title: Interpretation Checklist; type: Draw (vector); file path: figures/L04/interpret_checklist.png; what it shows: checklist for scale choice; alt-text: Guidance on choosing between RD and RR scales.

## Slide 10 — Interaction in regression
- Model: $E[Y | A, V] = \beta_0 + \beta_1 A + \beta_2 V + \beta_3 (A \times V)$
- $\beta_3$ is the "interaction term."
- If $\beta_3 \neq 0$, there is effect modification on the model's scale.
Speaker notes:
- Minimal formula for a linear or logistic model with interaction.

## Slide 11 — Marginal vs conditional effects
- Conditional Effect: Effect within a specific level of $V$.
- Marginal Effect: The average effect in the entire population (standardized).
Speaker notes:
- Figure title: Contrast; type: Draw (vector); file path: figures/L04/marginal_vs_cond.png; what it shows: zooming from whole population to subgroups; alt-text: Diagram contrasting population-level and subgroup-level effects.

## Slide 12 — (Pause/Activity) Choose scale for 2 questions
- Question 1: How many lives will we save if we vaccinate everyone in Region A vs Region B?
- Question 2: Does this drug inhibit the same pathway in smokers vs non-smokers?
- Which scale (RD or RR) is more appropriate for each?
Speaker notes:
- Timed anchor: 7 min. Discussion on why scale matters for the answer.

## Slide 13 — Reporting template
- 1. Table: Stratum-specific risks and effects (RD & RR).
- 2. Figure: Forest plot or grouped bar chart.
- 3. Narrative: "The treatment was more effective in group X on the absolute scale..."
Speaker notes:
- Figure title: Reporting Template; type: Draw (vector); file path: figures/L04/report_template.png; what it shows: layout for reporting results; alt-text: A template for reporting effect modification.

## Slide 14 — Pitfalls
- Multiple Testing: Checking 50 subgroups guarantees a "significant" result by chance.
- Sparse Strata: Small sample size in subgroups leads to unstable estimates.
Speaker notes:
- Figure title: Warning List; type: Draw (vector); file path: figures/L04/pitfall_list.png; what it shows: list with warning icons; alt-text: Common pitfalls in subgroup analysis.

## Slide 15 — Transportability teaser
- If the effect modification is strong, the Average Treatment Effect (ATE) will change if the distribution of $V$ changes.
- Study in US (50% $V=1$) vs study in UK (10% $V=1$).
Speaker notes:
- Figure title: Two Circles Transport; type: Draw (vector); file path: figures/L04/transport_hetero.png; what it shows: two population circles with different compositions; alt-text: Diagram showing how population composition affects transportability.

## Slide 16 — Summary
- Heterogeneity is common and important.
- Scale matters: Always report RD if you care about public health impact.
- Avoid data-dredging: Pre-specify subgroups.
Speaker notes:
- Wrap up main points.

## Slide 17 — Homework: scale dependence simulation
- You will create a dataset where the effect is modified on one scale but not the other.
Speaker notes:
- Figure title: HW Scale; type: From notebook placeholder; file path: figures/L04/hw_scale.png; what it shows: example output plot; alt-text: Placeholder for homework simulation plot.

## Slide 18 — Homework: interpretation write-up
- Interpret an interaction coefficient from a regression model.
Speaker notes:
- Figure title: Rubric grid; type: Draw (vector); file path: figures/L04/hw_rubric.png; what it shows: rubric for interpretation; alt-text: Grading rubric for the homework write-up.

## Slide 19 — Reading
- Read *What If* sections on Effect Modification.
Speaker notes:
- Link to textbook.

## Slide 20 — Exit ticket
- In one sentence, explain how a treatment can have "no effect modification" on the RR scale but "significant effect modification" on the RD scale.
Speaker notes:
- 2 min check.

## Slide 21 — Backup: forest plot layout
- Example of a well-formatted forest plot showing heterogeneity.
Speaker notes:
- Figure title: Forest Plot; type: Draw (vector); file path: figures/L04/forest_plot.png; what it shows: classic forest plot; alt-text: A forest plot visualizing effect heterogeneity.

## Slide 22 — Backup: interaction examples
- Linear: $\beta_3$ is the change in RD.
- Logistic: $exp(\beta_3)$ is the change in OR (Ratio of Odds Ratios).
Speaker notes:
- Figure title: Model Formulas; type: Draw (vector); file path: figures/L04/model_formulas.png; what it shows: linear vs logistic interaction terms; alt-text: Math for interactions in different model types.

## Slide 23 — Backup: glossary
- Recap of terms.
Speaker notes:
- Figure title: Glossary; type: Draw (vector); file path: figures/L04/glossary.png; what it shows: terms and brief definitions; alt-text: A glossary of effect modification terms.

## Slides 24-68 — [L04 Practice/backup modules as per plan]
- (Additional practice problems for RD/RR, interpreting coefficients, and avoiding pitfalls).
Speaker notes:
- Pacing buffer slides.
