# L12 — Capstone: marginal structural models, target trial emulation, and time-to-event outcomes

## Slide 1 — Title
- PHS564: Causal Inference Methods in Epidemiologic Research
- Lecture 12: Capstone: MSM, target trial emulation, and time-to-event outcomes
Speaker notes:
- Welcome to the final lecture. Today we bring everything together to solve the most complex problems in causal inference: time-varying confounding and target trial emulation.

## Slide 2 — Capstone roadmap
- 1. Marginal Structural Models (MSM) for time-varying treatment.
- 2. Target Trial Emulation: The blueprint for observational research.
- 3. Survival Analysis: Handling time-to-event outcomes.
Speaker notes:
- Figure title: 3-Module Bar; type: Draw (vector); file path: figures/L12/roadmap.png; what it shows: three horizontal segments representing the modules; alt-text: Roadmap for the final session.

## Slide 3 — Why time-varying confounding
- In many clinical scenarios, a variable (like illness severity) affects treatment decisions AND is affected by previous treatment.
- Standard regression fails here.
Speaker notes:
- Figure title: Timeline Severity; type: Draw (vector); file path: figures/L12/time_varying_confounding.png; what it shows: feedback loop between treatment and severity over time; alt-text: A diagram showing the feedback loop of time-varying confounding.

## Slide 4 — Longitudinal notation
- $L_t$: Covariates at time $t$.
- $A_t$: Treatment at time $t$.
- $C_t$: Censoring at time $t$.
- $Y$: Final outcome.
Speaker notes:
- Figure title: Legend; type: Draw (vector); file path: figures/L12/long_notation.png; what it shows: list of variables with time subscripts; alt-text: Notation for longitudinal data.

## Slide 5 — Time-varying DAG
- Structure: $A_{t-1} \rightarrow L_t \rightarrow A_t$, and both $L_t$ and $A_t$ affect $Y$.
- $L_t$ is a confounder for $A_t$, but also a mediator for $A_{t-1}$.
Speaker notes:
- Figure title: Longitudinal DAG; type: Draw (vector); file path: figures/L12/long_dag.png; what it shows: DAG with multiple time points and arrows; alt-text: A Directed Acyclic Graph for time-varying confounding.

## Slide 6 — Why naive regression fails
- If you adjust for $L_t$, you block the causal path from $A_{t-1}$ to $Y$.
- If you DON'T adjust for $L_t$, you have confounding for $A_t$.
- This is the "G-computation" or "MSM" motivation.
Speaker notes:
- Figure title: Bias Pathway; type: Draw (vector); file path: figures/L12/reg_bias.png; what it shows: highlighting the blocked and confounding paths; alt-text: Why standard regression cannot handle time-varying confounding.

## Slide 7 — MSM idea
- Use weights to create a pseudo-population where $A_t$ is independent of the past ($L_t, A_{t-1}$) at every time point.
Speaker notes:
- Figure title: Pseudo-population; type: Draw (vector); file path: figures/L12/msm_pseudo.png; what it shows: multiple time-slices being reweighted; alt-text: Conceptual diagram of a Marginal Structural Model.

## Slide 8 — Treatment weights (concept)
- $W_t = \prod_{k=0}^t \frac{1}{Pr(A_k | \bar{L}_k, \bar{A}_{k-1})}$
- The weight is the product of the inverse probabilities of treatment at each step.
Speaker notes:
- Minimal formula for time-varying IPTW.

## Slide 9 — Diagnostics: longitudinal weights
- Check the distribution of weights at each time point.
- Weights usually become more extreme as time progresses.
Speaker notes:
- Figure title: Weights Long; type: From notebook; file path: figures/L12/weights_long.png; what it shows: density plots of weights at t=1, t=2, t=3; alt-text: Weight distributions over time.

## Slide 10 — MSM estimation
- Fit a "pooled logistic regression" or "weighted regression" on the outcome $Y$ using the cumulative weights.
Speaker notes:
- Figure title: Model Box; type: Draw (vector); file path: figures/L12/msm_model.png; what it shows: weighted model formula; alt-text: Estimating an MSM.

## Slide 11 — Interpret MSM coefficient
- The coefficient represents the causal effect of a sustained treatment regime (e.g., "Always treat" vs "Never treat").
Speaker notes:
- Figure title: Interpretation Box; type: Draw (vector); file path: figures/L12/msm_interpret.png; what it shows: translation from beta to 'Always vs Never'; alt-text: How to interpret MSM results.

## Slide 12 — (Pause/Activity) Interpret MSM output
- Look at the provided output table.
- What is the estimated effect of 3 days of treatment vs 0 days?
Speaker notes:
- Timed anchor: 7 min. Practicing interpretation.

## Slide 13 — Target trial: protocol checklist
- 1. Eligibility
- 2. Treatment strategies
- 3. Assignment (Randomized vs Observational)
- 4. Time Zero (The start of follow-up)
- 5. Outcome & Follow-up
- 6. Analysis Plan
Speaker notes:
- Figure title: Checklist; type: Draw (vector); file path: figures/L12/trial_checklist.png; what it shows: components of a trial protocol; alt-text: The target trial emulation checklist.

## Slide 14 — Emulation mapping table
- Map each component of your "Ideal Trial" to your "Actual Observational Data."
Speaker notes:
- Figure title: 2-Column Table; type: Draw (vector); file path: figures/L12/mapping_table.png; what it shows: Target Trial vs Emulation; alt-text: Mapping an ideal trial to observational data.

## Slide 15 — Immortal time bias
- Occurs when we define treatment using information from the future.
- Example: "Ever treated" during the study. You must survive long enough to be treated!
Speaker notes:
- Figure title: Timeline Shaded; type: Draw (vector); file path: figures/L12/immortal_time.png; what it shows: a portion of the timeline shaded red; alt-text: Illustration of immortal time bias.

## Slide 16 — Design fixes
- Align $T_0$ with eligibility.
- Use "New User" designs.
- Define treatment status at $T_0$ (or use MSMs for time-varying).
Speaker notes:
- Figure title: Corrected Timeline; type: Draw (vector); file path: figures/L12/t0_fix.png; what it shows: timeline with T0, eligibility, and treatment perfectly aligned; alt-text: How to correctly align time zero.

## Slide 17 — (Pause/Activity) Protocol v2 workshop
- Revisit your project protocol.
- Refine your definition of Time Zero and Eligibility to avoid immortal time bias.
Speaker notes:
- Timed anchor: 10–12 min. Improving student projects.

## Slide 18 — Survival outcomes: why special
- We don't just care IF someone died, but WHEN.
- Censoring: Some people leave before the event happens.
Speaker notes:
- Figure title: Timeline; type: Draw (vector); file path: figures/L12/survival_intro.png; what it shows: patients followed for different lengths of time; alt-text: Basics of survival data.

## Slide 19 — Discrete-time hazard
- $h(t) = Pr(T=t | T \geq t)$
- The probability of the event occurring at time $t$, given you haven't had it yet.
Speaker notes:
- Figure title: Hazard Formula; type: Draw (vector); file path: figures/L12/hazard_formula.png; what it shows: definition of discrete-time hazard; alt-text: The discrete-time hazard function.

## Slide 20 — Person-period dataset
- Transform data so each patient has one row for every time point they are at risk.
Speaker notes:
- Figure title: Dataset Schematic; type: Draw (vector); file path: figures/L12/person_period.png; what it shows: one row per person-time; alt-text: Visual of a person-period (long) dataset.

## Slide 21 — Pooled logistic for hazards
- Fit a logistic model on the person-period data: `logit h(t) = intercept_t + beta * A + covariates`.
Speaker notes:
- Minimal formula for hazard modeling.

## Slide 22 — Hazard → survival curve
- Calculate the survival probability $S(t)$ as the product of $(1 - hazard)$ at every previous step.
Speaker notes:
- Figure title: Product Schematic; type: Draw (vector); file path: figures/L12/hazard_to_survival.png; what it shows: multiplying probabilities to get a curve; alt-text: Transforming hazards into a survival curve.

## Slide 23 — Plot survival curves (toy)
- Compare the probability of surviving over time for treated vs. untreated groups.
Speaker notes:
- Figure title: Survival Curves; type: From notebook; file path: figures/L12/survival_curves.png; what it shows: two step-functions (Kaplan-Meier style); alt-text: Predicted survival curves.

## Slide 24 — Weighted pooled logistic (link to MSM)
- Combine Module A and Module C: use IPTW weights in your pooled logistic model to handle time-varying confounding.
Speaker notes:
- Figure title: Weights + Model; type: Draw (vector); file path: figures/L12/weighted_survival.png; what it shows: weights feeding into a pooled logistic model; alt-text: Combining MSMs with survival analysis.

## Slide 25 — (Pause/Activity) Notebook walk-through
- Run the survival code in the notebook.
- Interpret the final survival curves.
Speaker notes:
- Timed anchor: 12–15 min. Final coding exercise.

## Slide 26 — Integrate deliverables
- Your protocol $\rightarrow$ Analysis Plan $\rightarrow$ Code $\rightarrow$ Results.
Speaker notes:
- Figure title: Pipeline; type: Draw (vector); file path: figures/L12/final_pipeline.png; what it shows: course components merging into a final project; alt-text: Integration of course deliverables.

## Slide 27 — Capstone homework recap
- 1. Final Protocol (v2).
- 2. Survival Analysis Lab results.
- 3. Reflection on causal assumptions.
Speaker notes:
- Figure title: Checklist; type: Draw (vector); file path: figures/L12/final_checklist.png; what it shows: list of items due; alt-text: Final deliverables checklist.

## Slide 28 — Final project rubric (mini)
- Reproducibility: Can someone else run your code?
- Validity: Did you identify bias correctly?
- Clarity: Are your results interpreted in plain English?
Speaker notes:
- Figure title: Rubric Grid; type: Draw (vector); file path: figures/L12/final_rubric.png; what it shows: grading criteria; alt-text: Final project grading rubric.

## Slide 29 — Common capstone pitfalls
- Immortal time bias (T0 alignment).
- Extreme weights (Positivity/Weight Truncation).
- Adjusting for post-treatment variables incorrectly.
Speaker notes:
- Figure title: Warning List; type: Draw (vector); file path: figures/L12/final_warnings.png; what it shows: warning icons next to pitfalls; alt-text: Common mistakes in advanced causal analysis.

## Slide 30 — Course summary
- You can now: Define causal questions, Draw DAGs, use G-formula, IPTW, IV, and emulate trials.
Speaker notes:
- Figure title: Summary Checklist; type: Draw (vector); file path: figures/L12/course_summary.png; what it shows: a checklist of all skills learned; alt-text: Summary of course achievements.

## Slide 31 — Next steps
- Advanced topics: G-estimation, Machine Learning (Double ML), Mediation analysis.
Speaker notes:
- Figure title: Path Forward; type: Draw (vector); file path: figures/L12/next_steps.png; what it shows: arrow pointing to future topics; alt-text: Suggestions for further study.

## Slide 32 — Closing Q&A
Speaker notes:
- Final discussion.

## Slide 33 — Thank you slide
Speaker notes:
- Congratulations on completing the course!

## Slides 34-86 — [L12 Practice/backup modules as per plan]
- (Worked examples for stabilized weights, identifying time-varying confounders, and finding immortal time in vignettes).
Speaker notes:
- Pacing buffer slides.
