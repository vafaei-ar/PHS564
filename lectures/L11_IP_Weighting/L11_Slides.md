# L11 — IP weighting for confounding (propensity scores) and diagnostics

## Slide 1 — Title
- PHS564: Causal Inference Methods in Epidemiologic Research
- Lecture 11: IP weighting for confounding (propensity scores) and diagnostics
Speaker notes:
- Welcome to Lecture 11. Today we focus on Inverse Probability of Treatment Weighting (IPTW), a powerful way to use propensity scores to identify causal effects.

## Slide 2 — Goal of IPTW
- Create a "pseudo-population" where treatment $A$ is independent of measured confounders $L$.
- In this pseudo-population, exchangeability holds without conditioning on $L$.
Speaker notes:
- Figure title: Reweighting Sketch; type: Draw (vector); file path: figures/L11/reweighting_sketch.png; what it shows: original population vs balanced pseudo-population; alt-text: Diagram showing how weighting balances groups.

## Slide 3 — Propensity score definition
- $e(L) = Pr(A=1 | L)$
- The probability of being assigned to the treated group given your baseline characteristics.
Speaker notes:
- Figure title: PS Formula Tile; type: Draw (vector); file path: figures/L11/ps_formula_tile.png; what it shows: the definition of the propensity score; alt-text: Mathematical definition of the propensity score.

## Slide 4 — IPTW weights
- For treated ($A=1$): $W = 1 / e(L)$
- For untreated ($A=0$): $W = 1 / (1 - e(L))$
Speaker notes:
- Figure title: Weight Formula; type: Draw (vector); file path: figures/L11/weight_formula.png; what it shows: the formula for IPTW weights; alt-text: The mathematical formula for IP treatment weights.

## Slide 5 — Stabilized weights
- $SW = \frac{Pr(A)}{Pr(A | L)}$
- Stabilized weights have a mean of 1 and lower variance, leading to more stable estimates.
Speaker notes:
- Figure title: SW Formula Tile; type: Draw (vector); file path: figures/L11/sw_formula_tile.png; what it shows: the formula for stabilized weights; alt-text: The mathematical formula for stabilized IPTW weights.

## Slide 6 — Pipeline
- 1. Fit Propensity Score Model (e.g., Logistic).
- 2. Compute Weights.
- 3. Diagnose (Overlap, SMDs).
- 4. Estimate Effect (Weighted Regression).
Speaker notes:
- Figure title: IPTW Pipeline; type: Draw (vector); file path: figures/L11/iptw_pipeline.png; what it shows: flow from PS model to final estimate; alt-text: A pipeline showing the steps of IPTW.

## Slide 7 — Overlap plot
- Visualize the distribution of propensity scores by treatment group.
- Check for "positivity violations" (no overlap).
Speaker notes:
- Figure title: Overlap Plot; type: From notebook; file path: figures/L11/overlap.png; what it shows: density plots of PS for treated and untreated; alt-text: A plot showing the overlap of propensity scores.

## Slide 8 — Weight histogram
- Look for extreme weights.
- If some weights are very large (e.g., > 100), your estimate might be dominated by a few individuals.
Speaker notes:
- Figure title: Weight Histogram; type: From notebook; file path: figures/L11/weights_hist.png; what it shows: histogram of IPTW weights; alt-text: A histogram showing the distribution of weights.

## Slide 9 — Balance (love plot)
- Compare Standardized Mean Differences (SMDs) before and after weighting.
- Goal: SMDs < 0.1 for all confounders.
Speaker notes:
- Figure title: Love Plot; type: From notebook; file path: figures/L11/love_plot.png; what it shows: dot plot of SMDs before and after weighting; alt-text: A Love plot for checking covariate balance.

## Slide 10 — Truncation / trimming
- Truncation: Capping extreme weights (e.g., at the 1st and 99th percentiles).
- Trimming: Removing people with extreme PS.
- Tradeoff: Reduces variance but can introduce bias.
Speaker notes:
- Figure title: Bias-Variance Slider; type: Draw (vector); file path: figures/L11/trunc_slider.png; what it shows: a slider for truncation strength; alt-text: Diagram showing the tradeoff in weight truncation.

## Slide 11 — Weighted effect estimation
- Estimate the ATE using a weighted mean or a weighted regression:
- `smf.wls("Y ~ A", data=df, weights=df['W']).fit()`
Speaker notes:
- Figure title: Estimator Box; type: Draw (vector); file path: figures/L11/estimator_box.png; what it shows: code snippet for weighted regression; alt-text: A box showing how to estimate effects with weights.

## Slide 12 — Robust SE
- Since we use weights, we must use "robust" or "sandwich" standard errors to get correct confidence intervals.
Speaker notes:
- Figure title: Sandwich Icon; type: Draw (vector); file path: figures/L11/sandwich_icon.png; what it shows: sandwich icon; alt-text: Icon for robust standard errors in weighted analysis.

## Slide 13 — (Pause/Activity) Compute weights & balance
- Follow the notebook to fit a PS model, compute weights, and check balance for a sample dataset.
Speaker notes:
- Timed anchor: 15–18 min. Hands-on coding of IPTW.

## Slide 14 — PS model specification tips
- Include all confounders.
- Don't include instruments (Z) or mediators (M).
- Check for non-linearities in the PS model.
Speaker notes:
- Figure title: Specification Checklist; type: Draw (vector); file path: figures/L11/ps_checklist.png; what it shows: checklist for PS model building; alt-text: A checklist for correctly specifying a propensity score model.

## Slide 15 — Common failures
- Extreme Weights: Check if positivity holds.
- Poor Overlap: You may need to restrict your target population.
- Wrong Covariates: Use your DAG!
Speaker notes:
- Figure title: Warning List; type: Draw (vector); file path: figures/L11/iptw_warnings.png; what it shows: list of common IPTW failure modes; alt-text: A list of things to watch out for in IPTW.

## Slide 16 — Reporting template
- Report the PS model formula, the distribution of weights, and the Love plot alongside your final ATE.
Speaker notes:
- Figure title: Reporting Template; type: Draw (vector); file path: figures/L11/iptw_report.png; what it shows: layout for reporting IPTW results; alt-text: A template for reporting IP weighting results.

## Slide 17 — Summary
- IPTW creates a balanced pseudo-population.
- Propensity scores are a tool for reweighting, not for prediction.
- Diagnostics (Love plots) are non-negotiable!
Speaker notes:
- Recap.

## Slide 18 — Homework: IPTW analysis
- You will perform a complete IPTW analysis on the NHEFS dataset and deliver the overlap plot, Love plot, and effect estimate.
Speaker notes:
- Figure title: HW Results; type: From notebook placeholder; file path: figures/L11/hw_results.png; what it shows: sample output plots; alt-text: Placeholder for the IPTW homework results.

## Slide 19 — Homework: methods paragraph draft
- Write the "Methods" section for an IPTW analysis of your chosen project.
Speaker notes:
- Figure title: Methods Template; type: Draw (vector); file path: figures/L11/iptw_methods_template.png; what it shows: a sample methods paragraph; alt-text: Template for the IPTW methods write-up.

## Slide 20 — Reading
- Read *What If* sections on Propensity Scores and IP Weighting.
Speaker notes:
- Assigned reading.

## Slide 21 — Exit ticket
- What was the most important variable to balance in your Activity 1 Love plot? Did weighting fix it?
Speaker notes:
- 2 min check.

## Slides 22-82 — [L11 Practice/backup modules as per plan]
- (Worked examples of weight calculation, interpreting Love plots, and identifying the impact of instrument inclusion).
Speaker notes:
- Pacing buffer slides.

