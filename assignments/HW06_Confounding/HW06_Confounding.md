# Homework 06: Confounding

## Part 1: Conceptual
1. Draw a DAG where $L$ is a confounder.
2. Draw a DAG where $M$ is a mediator.
3. Why is "adjusting for everything" a bad strategy in causal inference?
4. What is the difference between a direct causal effect and a total causal effect?

## Part 2: Coding
Using the `l06_confounding.csv` dataset:
1. Calculate the naive ACE.
2. Calculate the Adjusted ACE by standardizing on `L1` and `L2`.
3. Calculate the ACE by standardizing on `L1`, `L2`, and `M`.
4. Which result (2 or 3) represents the total causal effect of $A$ on $Y$?

**Deliverable:** Jupyter Notebook or PDF.

