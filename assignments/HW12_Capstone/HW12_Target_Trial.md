# Homework 12: Final Project Protocol

## The Goal
In this final assignment, you will apply the **Target Trial Emulation** framework to your semester project (MIMIC-IV or synthetic data).

## Part 1: Protocol Specification
Fill out the following 7 sections for your causal question:
1. **Eligibility Criteria:** Who is in your study? (e.g., adult patients in the ICU with sepsis).
2. **Treatment Strategies:** Define $A=1$ and $A=0$ clearly.
3. **Assignment Procedure:** State that you will emulate randomization by adjusting for a specific set of confounders $L$.
4. **Follow-up / Time Zero:** When does the clock start? How do you handle censoring?
5. **Outcome:** Define your primary endpoint.
6. **Causal Estimand:** Are you estimating a Risk Difference at a specific time? A Risk Ratio?
7. **Analysis Plan:** Which estimator will you use (G-formula, IPW, etc.)?

## Part 2: Survival Analysis (Coding)
Using the `l12_survival.csv` dataset:
1. Fit a pooled logistic hazard model.
2. Predict and plot the causal survival curves for $A=1$ and $A=0$.
3. Calculate the Risk Difference at $t=5$.

**Deliverable:** A protocol document (1-2 pages) and a Jupyter Notebook.

