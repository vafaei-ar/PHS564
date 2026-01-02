# L06 — Confounding: definition, confounders, and adjustment strategies

## Slide 1 — Title
- PHS564: Causal Inference Methods in Epidemiologic Research
- Lecture 06: Confounding: definition, confounders, and adjustment strategies
Speaker notes:
- Today we deep-dive into confounding. We will define it formally and explore the different strategies we have to adjust for it.

## Slide 2 — Confounding (counterfactual definition)
- $E[Y^a | A=1] \neq E[Y^a | A=0]$
- Treatment groups are not exchangeable.
- The treated would have had different outcomes than the untreated, even if they had received the same treatment.
Speaker notes:
- Figure title: Confounding Equation; type: Draw (vector); file path: figures/L06/conf_eq.png; what it shows: the counterfactual inequality; alt-text: Mathematical definition of confounding using potential outcomes.

## Slide 3 — Role taxonomy
- Confounder: Common cause of $A$ and $Y$.
- Mediator: On the causal path from $A$ to $Y$.
- Collider: Common effect of $A$ and $Y$ (or their causes).
- Instrument: Causes $A$ but only affects $Y$ through $A$.
- Proxy: Measured variable that is a marker for an unmeasured confounder.
Speaker notes:
- Figure title: Role Table; type: Draw (vector); file path: figures/L06/role_table.png; what it shows: 2x2 table with names and DAG structures; alt-text: A table classifying variables by their role in the DAG.

## Slide 4 — Selecting variables: DAG-first
- Don't just pick "significant" variables.
- Use the DAG to find the **minimal sufficient adjustment set**.
Speaker notes:
- Figure title: DAG to Set; type: Draw (vector); file path: figures/L06/dag_to_set.png; what it shows: DAG arrows leading to a circle around adjustment variables; alt-text: Diagram showing how a DAG identifies the correct adjustment set.

## Slide 5 — Adjustment methods map
- 1. Stratification / Standardization (G-formula)
- 2. Regression Adjustment (Outcome Modeling)
- 3. Matching (Direct comparison of similar units)
- 4. Inverse Probability Weighting (Exposure Modeling)
Speaker notes:
- Figure title: Methods Grid; type: Draw (vector); file path: figures/L06/methods_grid.png; what it shows: 2x2 grid of the four methods; alt-text: A map of the different methods for confounding adjustment.

## Slide 6 — Stratification (toy)
- Divide data into bins of $L$.
- Calculate effect in each bin.
Speaker notes:
- Figure title: Stratification Table; type: Draw (vector); file path: figures/L06/strat_table.png; what it shows: data table split into two smaller tables by L; alt-text: Visualization of data stratification.

## Slide 7 — Standardization recap
- Take a weighted average of the stratum-specific effects.
- Weights come from the distribution of $L$ in the whole population.
Speaker notes:
- Figure title: Standardization Weights; type: Draw (vector); file path: figures/L06/std_weights.png; what it shows: strata combined with weights to get a single number; alt-text: Diagram showing the weighted averaging in standardization.

## Slide 8 — Regression adjustment
- Model the outcome: $Y = \beta_0 + \beta_1 A + \beta_2 L$.
- Use the model to predict what would happen under $A=1$ and $A=0$ for everyone.
Speaker notes:
- Figure title: Model Predict; type: Draw (vector); file path: figures/L06/model_predict.png; what it shows: a regression line splitting into two counterfactual predictions; alt-text: Diagram showing regression-based adjustment and prediction.

## Slide 9 — Matching
- For every treated person, find an untreated person with the same $L$.
- Discard people without matches (Caution: this changes the population!)
Speaker notes:
- Figure title: Matching Schematic; type: Draw (vector); file path: figures/L06/matching.png; what it shows: people in two groups being paired up; alt-text: Illustration of the matching process.

## Slide 10 — Propensity score (preview)
- $e(L) = Pr(A=1 | L)$
- The probability of being treated given your covariates.
- A single number that summarizes all confounding.
Speaker notes:
- Figure title: PS Formula; type: Draw (vector); file path: figures/L06/ps_formula.png; what it shows: the definition of the propensity score; alt-text: The mathematical definition of the propensity score.

## Slide 11 — (Pause/Activity) Choose adjustment set
- Look at this DAG.
- Which variables must you adjust for? Which must you NOT adjust for?
Speaker notes:
- Timed anchor: 7 min. Discussion on avoiding colliders while blocking backdoor paths.

## Slide 12 — When adjustment harms
- 1. Conditioning on a collider (Induces bias).
- 2. Conditioning on a mediator (Blocks causal effect).
- 3. Conditioning on an instrument (Amplifies bias).
Speaker notes:
- Figure title: Warning List; type: Draw (vector); file path: figures/L06/adj_harm.png; what it shows: 'Warning' icons next to collider, mediator, instrument; alt-text: A list of scenarios where adjustment can be harmful.

## Slide 13 — Overadjustment example
- If $A \rightarrow M \rightarrow Y$ and you adjust for $M$, you remove the effect of $A$.
Speaker notes:
- Figure title: Mediator Bias; type: Draw (vector); file path: figures/L06/mediator_bias.png; what it shows: DAG A -> M -> Y with M crossed out; alt-text: A DAG illustrating overadjustment bias from a mediator.

## Slide 14 — Instrument adjustment caution
- If $Z \rightarrow A$ and there is unmeasured confounding $A \leftarrow U \rightarrow Y$, adjusting for $Z$ can make the bias from $U$ even worse.
Speaker notes:
- Figure title: IV Bias DAG; type: Draw (vector); file path: figures/L06/iv_bias_dag.png; what it shows: DAG Z -> A <- U -> Y; alt-text: A DAG showing why adjusting for an instrument can be harmful.

## Slide 15 — Practical timeline check
- Pre-exposure: Confounders.
- Post-exposure: Mediators or Colliders.
- Put your variables into bins based on when they occurred relative to $A$.
Speaker notes:
- Figure title: Timeline Bins; type: Draw (vector); file path: figures/L06/timeline_bins.png; what it shows: three bins (Pre, During, Post) on a timeline; alt-text: A temporal guide for variable classification.

## Slide 16 — Balance is the goal
- After adjustment (matching or weighting), the treated and untreated groups should look the same on $L$.
Speaker notes:
- Figure title: Balance Scale; type: Draw (vector); file path: figures/L06/balance_scale.png; what it shows: a balanced scale with A=1 and A=0; alt-text: A metaphor for covariate balance.

## Slide 17 — Summary
- Confounding is about non-exchangeability.
- Use DAGs to choose your adjustment set.
- Outcome models (regression) and exposure models (PS/IPW) are the two main paths.
Speaker notes:
- Recap.

## Slide 18 — Homework: compare methods
- You will analyze the same dataset using standardization, regression, and matching.
Speaker notes:
- Figure title: HW Compare; type: From notebook placeholder; file path: figures/L06/hw_compare.png; what it shows: comparison table from the homework; alt-text: Placeholder for the method comparison homework results.

## Slide 19 — Homework: DAG justification memo
- Briefly explain why your chosen $L$ set blocks all backdoor paths and avoids overadjustment.
Speaker notes:
- Figure title: Rubric grid; type: Draw (vector); file path: figures/L06/hw_rubric.png; what it shows: grading rubric; alt-text: Rubric for the DAG justification memo.

## Slide 20 — Reading
- Read *What If* Confounding chapters.
Speaker notes:
- Assigned reading.

## Slide 21 — Exit ticket
- Give an example of a variable that is a confounder for your question.
- Give an example of a variable that would be a mediator.
Speaker notes:
- 2 min check.

## Slide 22 — Backup: checklist
- Checklist for reporting an adjusted analysis (e.g., variables included, method used, balance check).
Speaker notes:
- Figure title: Reporting Checklist; type: Draw (vector); file path: figures/L06/report_checklist.png; what it shows: list of items to include in a paper; alt-text: A checklist for reporting confounding adjustment.

## Slides 23-78 — [L06 Practice/backup modules as per plan]
- (Worked examples for standardization vs regression vs matching and role classification drills).
Speaker notes:
- Pacing buffer slides.
