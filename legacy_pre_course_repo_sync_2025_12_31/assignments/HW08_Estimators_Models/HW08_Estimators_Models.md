# Homework 08: Estimators and Models

## Part 1: Conceptual
1. Define **Estimand**, **Estimator**, and **Estimate**.
2. Explain the "Curse of Dimensionality" in your own words. Why does it make simple stratification impossible?
3. What is the difference between **Model Bias** and **Sampling Variance**?

## Part 2: Coding
Using the `l08_l09_parametric.csv` dataset:
1. Fit a simple linear model: `Y ~ A`. What is the coefficient for $A$? Is this a causal effect?
2. Fit a model adjusting for all confounders: `Y ~ A + L1 + L2 + L3 + L4`. Compare this coefficient for $A$ to the previous one.
3. If you added interaction terms (e.g., `A * L1`), how would that change the complexity of your model?

**Deliverable:** Jupyter Notebook or PDF.

