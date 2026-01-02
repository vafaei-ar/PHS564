# L03 — Causal effects in observational studies (identifiability and assumptions)

## Slide 1 — Title
- PHS564: Causal Inference Methods in Epidemiologic Research
- Lecture 03: Observational studies: assumptions & identification
Speaker notes:
- Welcome back. Today we transition from the "ideal" world of RCTs to the "real" world of observational studies, where we must replace randomization with strong assumptions.

## Slide 2 — Course map
- L01: Potential Outcomes
- L02: Randomized Trials
- L03: Observational Studies (Moving to non-experimental data)
Speaker notes:
- Figure title: Course map highlight; type: Draw (vector); file path: figures/L03/course_map.png; what it shows: map with L03 highlighted; alt-text: Course timeline highlighting session 3.

## Slide 3 — Why observational?
- Ethics: Can't randomize smoking or pollution.
- Cost: RCTs are expensive and take years.
- Rare exposures: Hard to find enough people for an RCT.
Speaker notes:
- Figure title: Why Obs Icons; type: Draw (vector); file path: figures/L03/why_obs.png; what it shows: icons for ethics, cost, and rarity; alt-text: Three icons justifying the use of observational studies.

## Slide 4 — Running example: early antibiotics
- Question: Does early antibiotics (within 1hr) reduce mortality in sepsis?
- Problem: Doctors give antibiotics earlier to *sicker* patients.
- Severity is a confounder.
Speaker notes:
- Figure title: Severity Confounding; type: Draw (vector); file path: figures/L03/severity_confounding.png; what it shows: timeline with severity influencing both treatment timing and outcome; alt-text: A clinical timeline showing how patient severity affects both treatment and survival.

## Slide 5 — Identification roadmap
- 1. Define Causal Estimand: $E[Y^a]$
- 2. State Assumptions: Exchangeability, Positivity, Consistency.
- 3. Select Identification Method: G-formula, IPW, etc.
Speaker notes:
- Figure title: Identification Pipeline; type: Draw (vector); file path: figures/L03/id_pipeline.png; what it shows: flow from estimand to method; alt-text: A pipeline showing the steps of causal identification.

## Slide 6 — Conditional exchangeability
- Assumption: $Y^a \perp A | L$
- Within levels of $L$, treatment is "as-if" randomized.
- No unmeasured confounding.
Speaker notes:
- Figure title: Assumption callout; type: Draw (vector); file path: figures/L03/exch_callout.png; what it shows: the math formula with a 'No Unmeasured Confounding' label; alt-text: Formula for conditional exchangeability.

## Slide 7 — Positivity
- Assumption: $Pr(A=a|L=l) > 0$ for all $l$ where $Pr(L=l) > 0$.
- Every type of person must have a non-zero chance of receiving every treatment.
Speaker notes:
- Figure title: Overlap Sketch; type: Draw (vector); file path: figures/L03/overlap_sketch.png; what it shows: two overlapping distributions; alt-text: A diagram showing the overlap required for the positivity assumption.

## Slide 8 — Consistency
- Assumption: If $A=a$, then $Y = Y^a$.
- Requires well-defined interventions.
- "Obesity" is not an intervention; "Bariatric surgery" is.
Speaker notes:
- Figure title: Consistency Callout; type: Draw (vector); file path: figures/L03/consistency_callout.png; what it shows: Y=Y^a formula; alt-text: The consistency equation.

## Slide 9 — What must be in L?
- All pre-treatment common causes of $A$ and $Y$.
- Domain knowledge is essential!
Speaker notes:
- Figure title: Confounder Checklist; type: Draw (vector); file path: figures/L03/conf_checklist.png; what it shows: checklist for identifying confounders; alt-text: A checklist for variables that must be included in the adjustment set.

## Slide 10 — (Pause/Activity) Which assumption is fragile here?
- Scenario: A study on the effect of a new, very expensive drug on cancer survival.
- Which assumption (Exchangeability, Positivity, Consistency) is most likely to be violated? Why?
Speaker notes:
- Timed anchor: 6–7 min. Ask teams to justify their choice.

## Slide 11 — Identification by standardization
- Formula: $E[Y^a] = \sum_l E[Y|A=a, L=l] Pr(L=l)$
- This is the "parametric G-formula" (in its simplest form).
Speaker notes:
- Figure title: Standardization Equation; type: Draw (vector); file path: figures/L03/std_eq.png; what it shows: labeled standardization formula; alt-text: The mathematical formula for standardization.

## Slide 12 — Standardization intuition
- 1. Calculate the risk in each stratum of $L$.
- 2. Average those risks, weighting by the size of the stratum in the *whole* population.
Speaker notes:
- Figure title: Strata Weights; type: Draw (vector); file path: figures/L03/strata_weights.png; what it shows: visual grouping by L then re-averaging; alt-text: A diagram illustrating the process of standardization.

## Slide 13 — Identification by IPW (preview)
- $E[Y^a] = E \left[ \frac{I(A=a) Y}{Pr(A=a|L)} \right]$
- Create a "pseudo-population" by re-weighting people.
Speaker notes:
- Figure title: Weighting Schematic; type: Draw (vector); file path: figures/L03/ipw_schematic.png; what it shows: original population vs weighted pseudo-population; alt-text: A diagram showing how IPW expands certain observations to create a balanced population.

## Slide 14 — Positivity failure demo
- If some groups never get the treatment, we can't estimate the effect for them.
- Standard errors explode.
Speaker notes:
- Figure title: Bad Overlap; type: From notebook; file path: figures/L03/overlap_bad.png; what it shows: density plots of propensity scores with no overlap; alt-text: A plot showing a violation of the positivity assumption.

## Slide 15 — Extreme weights intuition
- When $Pr(A|L)$ is very small (near 0), the weight $1/Pr(A|L)$ becomes huge.
- One person can dominate the entire analysis.
Speaker notes:
- Figure title: Denominator Shrink; type: Draw (vector); file path: figures/L03/weight_blowup.png; what it shows: fraction 1/x as x goes to zero; alt-text: An illustration of how small probabilities lead to extreme weights.

## Slide 16 — Unmeasured confounding
- If $U$ affects both $A$ and $Y$ and is not in $L$, exchangeability is gone.
- Results will be biased.
Speaker notes:
- Figure title: U-DAG; type: Draw (vector); file path: figures/L03/u_dag.png; what it shows: A <- U -> Y; alt-text: A DAG showing unmeasured confounding.

## Slide 17 — Measurement error in L
- Even if you measure $L$, measuring it poorly (noise) leaves "residual confounding."
Speaker notes:
- Figure title: Noisy L; type: Draw (vector); file path: figures/L03/noisy_l.png; what it shows: DAG with L* as a noisy version of L; alt-text: A DAG showing measurement error in a confounder.

## Slide 18 — Practical: define time zero
- Follow-up MUST start at the moment eligibility and treatment assignment are determined.
- Failure to do so leads to "immortal time bias."
Speaker notes:
- Figure title: T0 Highlight; type: Draw (vector); file path: figures/L03/t0_obs.png; what it shows: timeline with a red 'Start' mark at treatment; alt-text: A timeline emphasizing the correct definition of time zero.

## Slide 19 — (Pause/Activity) List L for your project
- Revisit your causal question.
- List at least 5 covariates you would need to measure to satisfy conditional exchangeability.
Speaker notes:
- Timed anchor: 7–8 min. Remind students to only include pre-treatment variables.

## Slide 20 — Selection bias teaser
- Bias can occur even without a common cause if we condition on a "collider."
- We will cover this in depth in L07.
Speaker notes:
- Figure title: Collider Intro; type: Draw (vector); file path: figures/L03/collider_intro.png; what it shows: A -> S <- Y; alt-text: A DAG for selection bias.

## Slide 21 — Transportability teaser
- Can we "transport" results from our study population to a different target population?
Speaker notes:
- Figure title: Two Circles; type: Draw (vector); file path: figures/L03/transport.png; what it shows: two overlapping circles representing populations; alt-text: A diagram illustrating the concept of transportability.

## Slide 22 — Summary: assumptions
- Exchangeability (No unmeasured confounding)
- Positivity (Overlap)
- Consistency (Well-defined intervention)
Speaker notes:
- Figure title: Assumption Legend; type: Draw (vector); file path: figures/L03/assumption_legend.png; what it shows: the three big assumptions; alt-text: A summary of the three core identifiability assumptions.

## Slide 23 — Summary: two method families
- Outcome Modeling (G-formula/Standardization)
- Exposure Modeling (IPW/Propensity Scores)
Speaker notes:
- Figure title: Method Fork; type: Draw (vector); file path: figures/L03/method_fork.png; what it shows: a fork in the road labeled outcome vs exposure; alt-text: A diagram contrasting outcome-based and exposure-based causal methods.

## Slide 24 — Homework: overlap diagnostics
- You will check the distribution of covariates across treatment groups.
Speaker notes:
- Figure title: HW Overlap; type: From notebook placeholder; file path: figures/L03/hw_overlap.png; what it shows: sample overlap plot; alt-text: A placeholder for the homework overlap diagnostic plot.

## Slide 25 — Homework: assumptions memo
- Write a 1-page memo justifying why your chosen question's assumptions might hold (or fail).
Speaker notes:
- Figure title: Rubric Grid; type: Draw (vector); file path: figures/L03/hw_rubric.png; what it shows: a small grading rubric; alt-text: A grading rubric for the assumptions memo.

## Slide 26 — Reading
- Read Chapter 3 of *What If*.
Speaker notes:
- Essential reading for this session.

## Slide 27 — Exit ticket
- Name one assumption we discussed.
- Give one example of how to check or fix it in a study design.
Speaker notes:
- 2 min feedback.

## Slide 28 — Backup: notation legend
- Math definitions of assumptions.
Speaker notes:
- Figure title: Notation Backup; type: Draw (vector); file path: figures/L03/notation_backup.png; what it shows: formal math notation; alt-text: A backup slide with formal mathematical definitions.

## Slide 29 — Backup: g-formula schematic
- Step-by-step logic of standardization.
Speaker notes:
- Figure title: G-formula Step; type: Draw (vector); file path: figures/L03/gform_step.png; what it shows: algorithm flowchart; alt-text: A flowchart for the standardization algorithm.

## Slide 30 — Backup: IPW schematic
- Step-by-step logic of weighting.
Speaker notes:
- Figure title: IPW Step; type: Draw (vector); file path: figures/L03/ipw_step.png; what it shows: weighting flowchart; alt-text: A flowchart for the IPW algorithm.

## Slides 31-75 — [L03 Practice/backup modules as per plan]
- (These slides contain further iterations and additional practice problems following the themes above).
Speaker notes:
- Pacing buffer slides.
