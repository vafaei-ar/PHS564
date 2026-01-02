# L07 — Selection bias (structure and adjustment)

## Slide 1 — Title
- PHS564: Causal Inference Methods in Epidemiologic Research
- Lecture 07: Selection bias (structure and adjustment)
Speaker notes:
- Today we tackle selection bias. We will see how it arises from the structure of our study design and how we can use Inverse Probability of Censoring Weights (IPCW) to fix it.

## Slide 2 — Selection as collider bias
- Selection bias occurs when we condition (restrict) our analysis to a "collider" or its descendant.
- $A \rightarrow S \leftarrow Y$ (Restriction to $S=1$ opens a non-causal path).
Speaker notes:
- Figure title: Selection Collider; type: Draw (vector); file path: figures/L07/selection_collider.png; what it shows: A -> S <- Y with a box around S; alt-text: A DAG showing selection as collider bias.

## Slide 3 — Examples
- Loss to follow-up: Only those who stay in the study are analyzed.
- Berkson's bias: Study conducted only among hospitalized patients.
- Complete-case analysis: Discarding anyone with missing data.
Speaker notes:
- Figure title: 3 Selection Tiles; type: Draw (vector); file path: figures/L07/selection_tiles.png; what it shows: three boxes with names of selection bias types; alt-text: Three common examples of selection bias.

## Slide 4 — DAG: dropout depends on L and Y
- If dropout ($S$) is affected by treatment ($A$) and a cause of the outcome ($L$), or the outcome itself ($Y$), bias is introduced.
Speaker notes:
- Figure title: Dropout DAG; type: Draw (vector); file path: figures/L07/dropout_dag.png; what it shows: DAG A -> S <- L -> Y; alt-text: A DAG showing how dropout can induce selection bias.

## Slide 5 — Censoring notation
- $C=1$ if censored (lost to follow-up).
- $C=0$ if observed.
- We only see $Y$ if $C=0$.
Speaker notes:
- Figure title: Censoring Legend; type: Draw (vector); file path: figures/L07/censoring_legend.png; what it shows: definitions of C and Y observed; alt-text: Notation for censoring in causal inference.

## Slide 6 — IPCW intuition
- "Weight the people who stayed to represent the people who left."
- If a certain type of person (e.g., older patients) is more likely to drop out, we give more weight to the older patients who stayed.
Speaker notes:
- Figure title: Reweighting; type: Draw (vector); file path: figures/L07/ipcw_reweighting.png; what it shows: original cohort vs weighted observed cohort; alt-text: An illustration of how IPCW reconstructs the original population.

## Slide 7 — IPCW steps
- 1. Fit a model for the probability of NOT being censored: $Pr(C=0 | A, L)$.
- 2. Calculate weights: $W_c = 1 / Pr(C=0 | A, L)$.
- 3. Run your analysis (e.g., mean of $Y$) using these weights.
Speaker notes:
- Figure title: IPCW Pipeline; type: Draw (vector); file path: figures/L07/ipcw_pipeline.png; what it shows: flow from model to weights to weighted mean; alt-text: The steps for implementing IPCW.

## Slide 8 — Weight diagnostics
- Check the distribution of your weights.
- Very large weights (e.g., > 100) can make your estimates unstable.
Speaker notes:
- Figure title: IPCW Weights; type: From notebook; file path: figures/L07/ipcw_weights.png; what it shows: histogram of censoring weights; alt-text: A histogram showing the distribution of IPCW weights.

## Slide 9 — Stabilized censoring weights
- Formula: $SW_c = \frac{Pr(C=0 | A)}{Pr(C=0 | A, L)}$
- This reduces the variance of your estimator while still removing bias.
Speaker notes:
- Figure title: SW Formula; type: Draw (vector); file path: figures/L07/sw_formula.png; what it shows: the formula for stabilized weights; alt-text: The mathematical formula for stabilized censoring weights.

## Slide 10 — (Pause/Activity) Identify S and its causes
- For your project: What is the primary mechanism of selection/censoring?
- What variables ($L$) might affect whether someone stays in your study?
Speaker notes:
- Timed anchor: 7 min. Identify potential sources of selection bias.

## Slide 11 — MCAR / MAR / MNAR (brief)
- MCAR: Missing completely at random (No bias).
- MAR: Missing at random (Fixed by IPCW/MI).
- MNAR: Missing NOT at random (Hard to fix!).
Speaker notes:
- Figure title: Missingness Tiles; type: Draw (vector); file path: figures/L07/missing_tiles.png; what it shows: three boxes for MCAR, MAR, MNAR; alt-text: The three types of missing data mechanisms.

## Slide 12 — Complete-case bias
- Warning: Discarding people with missing data is only safe if the data is MCAR.
- In most epidemiologic studies, this induces bias.
Speaker notes:
- Figure title: CC Warning; type: Draw (vector); file path: figures/L07/cc_warning.png; what it shows: 'Warning' sign next to 'Complete Case Analysis'; alt-text: A warning against the automatic use of complete-case analysis.

## Slide 13 — Sensitivity framing
- Since we can't observe why people are missing, we should ask: "How much bias would there be if the missing people were twice as likely to have the outcome?"
Speaker notes:
- Figure title: Sensitivity Dial; type: Draw (vector); file path: figures/L07/sensitivity_dial.png; what it shows: a dial representing the strength of unmeasured selection; alt-text: An illustration of sensitivity analysis for selection bias.

## Slide 14 — Summary
- Selection bias is a structural problem.
- IPCW is a powerful tool to address MAR selection.
- Always check your weights!
Speaker notes:
- Recap.

## Slide 15 — Homework: IPCW on toy data
- You will simulate censoring and use IPCW to recover the true treatment effect.
Speaker notes:
- Figure title: HW IPCW; type: From notebook placeholder; file path: figures/L07/hw_ipcw.png; what it shows: sample output from the homework; alt-text: Placeholder for the IPCW simulation homework.

## Slide 16 — Homework: DAG + assumption check
- Add a selection node ($S$) to your project DAG and discuss the plausibility of the MAR assumption for your study.
Speaker notes:
- Figure title: Rubric grid; type: Draw (vector); file path: figures/L07/hw_rubric.png; what it shows: grading rubric; alt-text: Rubric for the selection bias write-up.

## Slide 17 — Reading
- Read *What If* sections on Selection Bias.
Speaker notes:
- Assigned reading.

## Slide 18 — Exit ticket
- Give one example of selection bias in a study you have read or worked on.
Speaker notes:
- 2 min check.

## Slides 19-74 — [L07 Practice/backup modules as per plan]
- (Worked examples of loss to follow-up, Berkson's bias, and interpreting weight histograms).
Speaker notes:
- Pacing buffer slides.
