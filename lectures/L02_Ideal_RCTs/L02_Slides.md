# L02 — Causal effects in ideal randomized trials

## Slide 1 — Title
- PHS564: Causal Inference Methods in Epidemiologic Research
- Lecture 02: Ideal randomized trials: identification and estimation
Speaker notes:
- Today we look at the 'Gold Standard' of causal inference: the randomized controlled trial (RCT). We will see why it works and how to analyze it correctly.

## Slide 2 — Course map
- L01: Potential Outcomes (Done)
- L02: Randomization identifies $E[Y^a]$
- Moving from theory to the first 'real' scenario.
Speaker notes:
- Figure title: Course Map Highlight; type: Draw (vector); file path: figures/L02/course_map.png; what it shows: timeline with Session 2 highlighted; alt-text: Course timeline highlighting session 2.

## Slide 3 — Target trial (preview)
- Every observational study should be viewed as an emulation of a target trial.
- Protocol components: Eligibility, Treatment, Assignment, Follow-up, Outcome.
Speaker notes:
- Figure title: Target Trial Checklist; type: Draw (vector); file path: figures/L02/target_trial_checklist.png; what it shows: checklist of protocol components; alt-text: A protocol checklist for a target trial.

## Slide 4 — Randomization mechanism
- Treatment $A$ is assigned by a coin flip or lottery.
- This ensures that treatment is NOT chosen by the patient or doctor.
Speaker notes:
- Figure title: Randomization; type: Draw (vector); file path: figures/L02/randomization_icon.png; what it shows: icon of a coin or lottery; alt-text: Icon representing the process of randomization.

## Slide 5 — Unconditional exchangeability
- $Y^a \perp A$: Potential outcomes are independent of the treatment assigned.
- The groups are comparable in every way (measured and unmeasured).
Speaker notes:
- This is the most powerful assumption in statistics. It only holds in ideal trials.

## Slide 6 — Identification result
- $E[Y^a] = E[Y|A=a]$
- Because groups are exchangeable, what we see in the treated group is what would have happened to everyone had they been treated.
Speaker notes:
- This is the fundamental link between the counterfactual world and the factual data.

## Slide 7 — Estimands in RCT
- Risk Difference (RD): $E[Y^1] - E[Y^0]$
- Risk Ratio (RR): $E[Y^1] / E[Y^0]$
- Intention-to-Treat (ITT) vs Per-Protocol (PP).
Speaker notes:
- Figure title: Estimand Tiles; type: Draw (vector); file path: figures/L02/estimand_tiles.png; what it shows: RD, RR, ITT, PP tiles; alt-text: Different types of causal estimands used in RCTs.

## Slide 8 — Estimator: difference in means
- Simple RD = $\bar{Y}_{treated} - \bar{Y}_{untreated}$
- This is an unbiased estimator of the ATE in an ideal trial.
Speaker notes:
- Minimal formula for the sample risk difference.

## Slide 9 — CI intuition
- Sampling variation: Every time we run the trial, we get a slightly different estimate.
- Confidence Interval (CI) tells us about the precision of our estimate.
Speaker notes:
- Figure title: Error Bars; type: Draw (vector); file path: figures/L02/error_bars.png; what it shows: point estimate with confidence interval; alt-text: Diagram showing a point estimate and its uncertainty.

## Slide 10 — (Pause/Activity) RCT abstract dissection
- Read the provided RCT abstract.
- Identify:
  1. The primary estimand.
  2. The estimator used.
  3. The target population.
Speaker notes:
- Timed anchor: 7 min. Use a recent NEJM or JAMA abstract.

## Slide 11 — ITT effect
- "Analyze as randomized."
- Measures the effect of the *assignment* to treatment, not necessarily the treatment itself.
Speaker notes:
- Figure title: ITT Pathway; type: Draw (vector); file path: figures/L02/itt_pathway.png; what it shows: path from assignment to outcome; alt-text: Diagram showing the Intention-to-Treat analysis path.

## Slide 12 — Per-protocol effect
- Measures the effect of the treatment among those who *actually followed* the protocol.
- Warning: This can introduce selection bias!
Speaker notes:
- Figure title: Adherence Pathway; type: Draw (vector); file path: figures/L02/pp_pathway.png; what it shows: path from assignment to adherence to outcome; alt-text: Diagram showing the Per-Protocol analysis path.

## Slide 13 — Noncompliance categories
- Always-takers: Take treatment regardless of assignment.
- Never-takers: Never take treatment.
- Compliers: Take treatment if assigned, don't if not.
Speaker notes:
- Figure title: Compliance Table; type: Draw (vector); file path: figures/L02/compliance_table.png; what it shows: 2x2 table of assignment vs adherence; alt-text: A table classifying subjects by their compliance behavior.

## Slide 14 — Why ITT preserves randomization
- Assignment is randomized. Even if people don't comply, the assignment remains exchangeable.
- ITT protects against confounding.
Speaker notes:
- Figure title: ITT Shield; type: Draw (vector); file path: figures/L02/itt_shield.png; what it shows: a shield icon over the treatment assignment; alt-text: Icon representing ITT as a protection against bias.

## Slide 15 — When PP needs adjustment
- Adherence is a choice. Those who adhere may be different from those who don't.
- PP analysis requires adjustment for "adherence confounding."
Speaker notes:
- Figure title: Adherence DAG; type: Draw (vector); file path: figures/L02/adherence_dag.png; what it shows: DAG with Z -> A -> Y and U affecting A and Y; alt-text: A DAG showing how non-compliance introduces confounding.

## Slide 16 — Loss to follow-up
- Selection bias in trials.
- If dropout is related to treatment and outcome, the remaining sample is no longer exchangeable.
Speaker notes:
- Figure title: Dropout Timeline; type: Draw (vector); file path: figures/L02/dropout_timeline.png; what it shows: subjects leaving the trial over time; alt-text: Timeline showing subject attrition in a clinical trial.

## Slide 17 — CONSORT flow
- Standard for reporting RCTs.
- Shows how many people were screened, randomized, and analyzed.
Speaker notes:
- Figure title: CONSORT Diagram; type: Draw (vector); file path: figures/L02/consort_flow.png; what it shows: CONSORT flow chart; alt-text: The standard CONSORT flow diagram for reporting randomized trials.

## Slide 18 — Blinding & measurement bias
- Blinding prevents knowledge of treatment from affecting outcome measurement or behavior.
- Single, Double, Triple blinding.
Speaker notes:
- Figure title: Bias Channels; type: Draw (vector); file path: figures/L02/blinding_bias.png; what it shows: paths from knowledge to bias; alt-text: Diagram showing how lack of blinding can introduce measurement bias.

## Slide 19 — (Pause/Activity) design a mini RCT
- In your teams:
- Define Time Zero, Treatment $A$, Outcome $Y$, and Follow-up for your causal question.
Speaker notes:
- Timed anchor: 8–10 min.

## Slide 20 — Covariate adjustment in RCT
- We adjust not to remove bias (randomization did that), but to increase **precision**.
- Smaller variance, narrower CIs.
Speaker notes:
- Figure title: Bias vs Variance; type: Draw (vector); file path: figures/L02/precision_slider.png; what it shows: slider showing gain in precision; alt-text: A diagram illustrating how covariate adjustment improves precision.

## Slide 21 — Stratified estimator (toy)
- Compute RD in each stratum of $L$, then take a weighted average.
Speaker notes:
- Figure title: Table Arithmetic; type: Draw (vector); file path: figures/L02/stratified_arithmetic.png; what it shows: step-by-step arithmetic for stratified RD; alt-text: Visual breakdown of calculating a stratified risk difference.

## Slide 22 — Regression adjustment (toy)
- Fit a model: $Y = \beta_0 + \beta_1 A + \beta_2 L$.
- Use the model to predict risks.
Speaker notes:
- Figure title: Model to Predict; type: Draw (vector); file path: figures/L02/regression_adjustment.png; what it shows: model fitting leading to prediction; alt-text: Diagram showing regression-based adjustment.

## Slide 23 — Simulation: RCT vs observational
- See how randomization removes the "backdoor" path from $L$.
Speaker notes:
- Figure title: RCT vs Obs Simulation; type: From notebook; file path: figures/L02/sim_rct_vs_obs.png; what it shows: distribution of covariates in RCT vs observational; alt-text: A plot showing that RCTs balance covariates while observational studies do not.

## Slide 24 — Subgroup analyses cautions
- Multiplicity: The more groups you check, the more likely you find a "significant" result by chance.
- Pre-specify your subgroups!
Speaker notes:
- Figure title: Caution Box; type: Draw (vector); file path: figures/L02/subgroup_caution.png; what it shows: warning icons for subgroup analysis; alt-text: Warning icon for multiple testing in subgroup analysis.

## Slide 25 — Harms reporting
- Relative risks can be misleading for rare events.
- Always report absolute risks (RD) for safety outcomes.
Speaker notes:
- Figure title: RD Emphasis; type: Draw (vector); file path: figures/L02/rd_harms.png; what it shows: comparison of small RR vs large RD; alt-text: Diagram emphasizing the importance of absolute risk for harms.

## Slide 26 — Summary
- Randomization creates exchangeability.
- ITT is the primary causal estimand.
- Precision is the goal of adjustment.
Speaker notes:
- Wrap up the core messages of the lecture.

## Slide 27 — Homework: simulate RCT
- You will generate a trial and estimate the RD with CIs.
Speaker notes:
- Figure title: HW Simulation; type: From notebook placeholder; file path: figures/L02/hw_sim.png; what it shows: example plot from the homework; alt-text: A placeholder for the homework simulation output.

## Slide 28 — Homework: critique paper
- Read an RCT paper and evaluate its adherence to the CONSORT standards.
Speaker notes:
- Figure title: Paper Checklist; type: Draw (vector); file path: figures/L02/paper_critique.png; what it shows: checklist for evaluating a clinical trial; alt-text: A rubric for critiquing a randomized controlled trial.

## Slide 29 — Reading
- Read Chapter 2 of *What If*.
Speaker notes:
- Remind students of the reading assignment.

## Slide 30 — Exit ticket
- What is one thing you learned today?
- What is one question you still have?
Speaker notes:
- Quick feedback for the instructor.

## Slide 31 — Backup: notation legend
- $Y^a$, ITT, PP.
Speaker notes:
- Figure title: Legend; type: Draw (vector); file path: figures/L02/legend_backup.png; what it shows: notation definitions; alt-text: A backup slide with the notation legend.

## Slide 32 — Backup: course map
- Reviewing our progress.
Speaker notes:
- Figure title: Course Map; type: Draw (vector); file path: figures/L02/course_map_backup.png; what it shows: full course map; alt-text: A backup slide with the full course map.

## Slides 33-72 — [L02 Practice/backup modules as per plan]
- (These slides contain further iterations and additional practice problems following the themes above).
Speaker notes:
- Buffer slides for pacing.
