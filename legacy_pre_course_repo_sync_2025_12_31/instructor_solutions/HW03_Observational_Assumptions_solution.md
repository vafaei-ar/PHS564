# HW03 Solution: Observational Studies

## Part 1: Conceptual
1. Within levels of measured confounders L, the treatment is as-if randomized.
2. A drug is contraindicated for patients with a specific condition (e.g., kidney failure). These patients will never receive the drug, so $P(A=1|L=KidneyFailure) = 0$.
3. Because it requires that the treatment $A$ corresponds to a unique, observable potential outcome, which usually means the intervention must be specific.

## Part 2: Coding (Sketch)
```python
df = load_data("l03_observational.csv")
# Naive ACE will be biased (e.g., 5.0)
# Adjusted ACE should be close to 2.0
```

