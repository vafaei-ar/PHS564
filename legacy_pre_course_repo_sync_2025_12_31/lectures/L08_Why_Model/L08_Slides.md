# L08 — Why model? (estimators, models, bias-variance tradeoff)

## Slide 1 — Title
- PHS564: Causal Inference Methods in Epidemiologic Research
- Lecture 08: Why model? (estimators, models, bias–variance tradeoff)
Speaker notes:
- Today we move from the "theory" of identification to the "practice" of estimation. We will discuss why we need models and the tradeoffs we make when we use them.

## Slide 2 — Estimator vs model vs estimand
- Estimand: The theoretical quantity we want to measure (e.g., $E[Y^1] - E[Y^0]$).
- Model: A set of assumptions about the functional form of the data (e.g., $Y = \beta A + \gamma L$).
- Estimator: The algorithm/formula used to compute an estimate from data (e.g., OLS).
Speaker notes:
- Figure title: Three Boxes; type: Draw (vector); file path: figures/L08/three_boxes.png; what it shows: boxes for Estimand, Model, Estimator; alt-text: Three boxes defining estimand, model, and estimator.

## Slide 3 — Plug-in estimators
- In causal inference, we often fit a model, then "plug in" different values of $A$ to get counterfactual predictions.
Speaker notes:
- Figure title: Pipeline; type: Draw (vector); file path: figures/L08/plugin_pipeline.png; what it shows: flow from model to prediction to effect; alt-text: A pipeline showing the plug-in estimation process.

## Slide 4 — Bias–variance tradeoff
- Underfitting: Model is too simple to capture the true relationship (High Bias).
- Overfitting: Model captures noise in the specific sample (High Variance).
Speaker notes:
- Figure title: Bias-Variance; type: From notebook; file path: figures/L08/bias_variance.png; what it shows: classic underfit/overfit/just-right curves; alt-text: Plots illustrating the bias-variance tradeoff.

## Slide 5 — Misspecification demo
- If the true relationship is non-linear (e.g., $Y \sim L^2$) but we model it as linear ($Y \sim L$), our causal effect estimate will be biased.
Speaker notes:
- Figure title: Misspecification Demo; type: From notebook; file path: figures/L08/misspecification_demo.png; what it shows: linear model failing to fit a quadratic curve; alt-text: A plot showing how model misspecification induces bias.

## Slide 6 — Parametric vs flexible models
- Parametric (e.g., OLS): High assumptions, high precision, easy to interpret.
- Flexible (e.g., Splines, Random Forest): Low assumptions, low precision, harder to interpret.
Speaker notes:
- Figure title: Slider; type: Draw (vector); file path: figures/L08/model_slider.png; what it shows: a slider between parametric and flexible; alt-text: A scale showing the tradeoff between model flexibility and assumptions.

## Slide 7 — Bootstrap for uncertainty
- Since causal estimators (like IPW or G-formula) involve multiple steps, simple standard errors often fail.
- We use the Bootstrap: Resample with replacement many times.
Speaker notes:
- Figure title: Bootstrap Loop; type: Draw (vector); file path: figures/L08/bootstrap_loop.png; what it shows: original data -> multiple samples -> multiple estimates -> distribution; alt-text: A flowchart of the bootstrap procedure.

## Slide 8 — Robust SE (concept)
- "Sandwich" estimators.
- Useful when we use weights (like IPW), as the variance calculation must account for the fact that the weights are themselves estimated.
Speaker notes:
- Figure title: Sandwich Icon; type: Draw (vector); file path: figures/L08/sandwich_icon.png; what it shows: a literal sandwich labeled 'Robust SE'; alt-text: Icon for robust standard errors.

## Slide 9 — (Pause/Activity) Propose a model + checks
- For your project: What type of model (Linear, Logistic, etc.) would you use?
- What diagnostic checks (e.g., residuals, calibration) will you perform?
Speaker notes:
- Timed anchor: 8 min. Discussion on model selection and validation.

## Slide 10 — Model checks you must do
- Calibration: Do the predicted risks match the observed risks?
- Residuals: Are there patterns left over?
- Extrapolation: Are we making predictions for people who don't exist in our data?
Speaker notes:
- Figure title: Checklist; type: Draw (vector); file path: figures/L08/model_checks.png; what it shows: a checklist of essential model diagnostics; alt-text: A checklist for model validation.

## Slide 11 — When modeling fails
- Positivity violations: If $Pr(A=1|L)=0$, the model will still give you a prediction by "extrapolating" from other values of $L$.
- This prediction is based purely on the model's functional form, NOT on data.
Speaker notes:
- Figure title: Warning; type: Draw (vector); file path: figures/L08/extrapolation_warning.png; what it shows: a dotted line extending beyond data points; alt-text: A diagram illustrating the danger of extrapolation under positivity violations.

## Slide 12 — Summary
- Models are tools to handle high-dimensional confounding.
- But they are just "guesses" about the truth.
- Always check your assumptions and functional forms.
Speaker notes:
- Recap.

## Slide 13 — Homework: simulate misspecification impact
- You will analyze a dataset with a quadratic relationship using a linear model and see how the effect estimate changes.
Speaker notes:
- Figure title: HW Mis; type: From notebook placeholder; file path: figures/L08/hw_mis.png; what it shows: sample output plot; alt-text: Placeholder for the model misspecification homework.

## Slide 14 — Homework: write model-check plan
- Draft a 1-page plan for how you will validate the models used in your final project.
Speaker notes:
- Figure title: Template; type: Draw (vector); file path: figures/L08/hw_template.png; what it shows: a layout for the validation plan; alt-text: Template for the model validation homework.

## Slide 15 — Reading
- Read *What If* sections on Modeling and Estimators.
Speaker notes:
- Assigned reading.

## Slides 16-66 — [L08 Practice/backup modules as per plan]
- (Worked examples of logistic vs linear models, interpreting calibration plots, and identifying overfitting).
Speaker notes:
- Pacing buffer slides.
