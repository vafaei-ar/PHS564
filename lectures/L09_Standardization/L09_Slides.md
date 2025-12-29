# L09 — Standardization and the (parametric) g-formula

## Slide 1 — Title
- PHS564: Causal Inference Methods in Epidemiologic Research
- Lecture 09: Standardization and the (parametric) g-formula
Speaker notes:
- Today we learn how to implement the G-formula using parametric models. This is a general and flexible method for causal inference.

## Slide 2 — Goal
- Our goal is to estimate the potential outcome mean $E[Y^a]$ for different values of $a$.
- We do this by fitting an outcome model and averaging its predictions over the population.
Speaker notes:
- Figure title: Target Box; type: Draw (vector); file path: figures/L09/target_box.png; what it shows: box with E[Y^a] as the target; alt-text: The target of standardization is the potential outcome mean.

## Slide 3 — g-formula identification
- $E[Y^a] = \sum_l E[Y | A=a, L=l] Pr(L=l)$
- This requires: Exchangeability, Positivity, and Consistency.
- "We use the observed data to simulate the counterfactual world."
Speaker notes:
- Figure title: g-formula Equation; type: Draw (vector); file path: figures/L09/gformula_eq.png; what it shows: the g-formula equation with assumption labels; alt-text: The g-formula for causal identification.

## Slide 4 — Algorithm overview
- 1. Fit outcome model $E[Y | A, L]$.
- 2. Copy the dataset and set everyone to $A=a$.
- 3. Predict $Y$ using the model.
- 4. Average the predictions.
- 5. Bootstrap for confidence intervals.
Speaker notes:
- Figure title: Pipeline; type: Draw (vector); file path: figures/L09/gformula_pipeline.png; what it shows: flow from fit to average to bootstrap; alt-text: A pipeline showing the steps of the parametric g-formula.

## Slide 5 — Toy dataset
- Example with one confounder $L$ (Age), treatment $A$ (Statins), and outcome $Y$ (Heart Disease).
Speaker notes:
- Figure title: Mini Table; type: Draw (vector); file path: figures/L09/toy_data.png; what it shows: a 5-row table of L, A, Y; alt-text: A toy dataset for demonstration.

## Slide 6 — Step 1: fit E[Y|A,L]
- Choose a model based on $Y$:
  - $Y$ is continuous $\rightarrow$ OLS.
  - $Y$ is binary $\rightarrow$ Logistic or Linear Probability Model.
Speaker notes:
- Figure title: Model Box; type: Draw (vector); file path: figures/L09/model_box.png; what it shows: a box representing the outcome model; alt-text: Choosing an appropriate outcome model.

## Slide 7 — Step 2: create A=1 dataset
- Take your original dataset and change EVERYONE'S treatment to $A=1$.
- Keep $L$ exactly as it is.
Speaker notes:
- Figure title: Data Copy; type: Draw (vector); file path: figures/L09/data_copy.png; what it shows: two tables side-by-side, one with observed A, one with all A=1; alt-text: Creating the counterfactual dataset for A=1.

## Slide 8 — Step 3: predict Y under A=1
- Use your model from Step 1 to predict the probability of $Y$ for each row in your "all treated" dataset.
- These are your $\hat{Y}^1$ values.
Speaker notes:
- Figure title: Prediction Arrow; type: Draw (vector); file path: figures/L09/predict_arrow.png; what it shows: model applying to the A=1 dataset; alt-text: Predicting counterfactual outcomes.

## Slide 9 — Step 4: average Ŷ^1
- The mean of your predictions $\hat{Y}^1$ is your estimate for $E[Y^1]$.
Speaker notes:
- Figure title: Averaging; type: Draw (vector); file path: figures/L09/averaging_risks.png; what it shows: column of predictions being averaged; alt-text: Averaging the predicted risks.

## Slide 10 — Repeat for A=0
- Do the same thing: set $A=0$ for everyone, predict, and average to get $E[Y^0]$.
Speaker notes:
- Figure title: Repeat; type: Draw (vector); file path: figures/L09/repeat_a0.png; what it shows: process repeating for A=0; alt-text: Repeating the process for the untreated counterfactual.

## Slide 11 — Compute ATE
- $ATE = E[Y^1] - E[Y^0]$.
Speaker notes:
- Figure title: Formula Tile; type: Draw (vector); file path: figures/L09/ate_tile.png; what it shows: final subtraction to get the ATE; alt-text: Calculation of the Average Treatment Effect.

## Slide 12 — (Pause/Activity) Implement g-formula (toy)
- Using the code provided in your notebook, walk through the steps for a small dataset.
Speaker notes:
- Timed anchor: 15 min. Guided coding exercise.

## Slide 13 — Plot: predicted risks
- Visualize the distribution of predicted risks for both treated and untreated counterfactual worlds.
Speaker notes:
- Figure title: g-formula Risk; type: From notebook; file path: figures/L09/gformula_risk.png; what it shows: histogram or density of predictions; alt-text: Plot of counterfactual predicted risks.

## Slide 14 — Diagnostics: calibration
- Check if your model's predictions align with reality.
Speaker notes:
- Figure title: Calibration Check; type: From notebook; file path: figures/L09/model_check_calibration.png; what it shows: calibration plot (observed vs predicted); alt-text: Model calibration diagnostic plot.

## Slide 15 — Uncertainty: bootstrap CI
- Since our estimate involves multiple steps, we must resample our entire dataset (with replacement) and repeat the g-formula 500-1000 times to get the 95% CI.
Speaker notes:
- Figure title: Bootstrap Loop; type: Draw (vector); file path: figures/L09/bootstrap_loop.png; what it shows: repeating the pipeline many times; alt-text: The bootstrap procedure for uncertainty.

## Slide 16 — Extrapolation warning
- If there are no treated people at certain levels of $L$, the model is just guessing.
- Be careful with wide confidence intervals.
Speaker notes:
- Figure title: Warning; type: Draw (vector); file path: figures/L09/extrapol_warning.png; what it shows: warning icon; alt-text: Warning about model extrapolation under positivity violations.

## Slide 17 — Communication: report assumptions
- When publishing, clearly state:
  - The model used (e.g., Logistic).
  - The variables in $L$.
  - How you checked for non-linearity.
Speaker notes:
- Figure title: Reporting Template; type: Draw (vector); file path: figures/L09/reporting_template.png; what it shows: layout for a methods section; alt-text: A template for reporting g-formula results.

## Slide 18 — Summary
- g-formula is a "predict and average" approach.
- It is highly flexible (can handle non-linearities and interactions).
- Bootstrap is essential for correct inference.
Speaker notes:
- Recap.

## Slide 19 — Homework: g-formula on provided dataset
- You will use the `phs564_ci.estimators.standardization` helper to analyze a dataset and produce a risk difference with a bootstrap CI.
Speaker notes:
- Figure title: HW Output; type: From notebook placeholder; file path: figures/L09/hw_output.png; what it shows: sample output table; alt-text: Placeholder for the g-formula homework results.

## Slide 20 — Homework: methods paragraph draft
- Write a formal "Methods" paragraph describing your g-formula analysis for your final project.
Speaker notes:
- Figure title: Template; type: Draw (vector); file path: figures/L09/hw_methods_template.png; what it shows: a sample methods paragraph; alt-text: Template for the methods write-up.

## Slide 21 — Reading
- Read *What If* sections on the G-formula.
Speaker notes:
- Assigned reading.

## Slides 22-78 — [L09 Practice/backup modules as per plan]
- (Worked examples of choosing functional forms and avoiding common pitfalls like including post-treatment covariates).
Speaker notes:
- Pacing buffer slides.

