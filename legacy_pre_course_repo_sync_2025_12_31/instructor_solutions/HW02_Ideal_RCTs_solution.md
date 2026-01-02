# HW02 Solution: Ideal Randomized Trials

## Part 1: Conceptual
1. Randomization ensures that treatment assignment is independent of potential outcomes. This makes the treated and untreated groups comparable (exchangeable).
2. Randomization guarantees exchangeability *in expectation*. In small samples, there can be "chance imbalances" in covariates, so exchangeability might not hold perfectly.

## Part 2: Coding (Sketch)
```python
df = load_data("l02_ideal_rct.csv")
# RR = 0.3 / 0.2 approx 1.5
# Stratified RR should be similar
# Standardized RR should be similar
```

