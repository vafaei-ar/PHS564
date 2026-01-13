# Homework 09: Standardization + (parametric) g-formula

**Team-based assignment** (2-person teams)

## Instructions

Complete the following tasks using the MIMIC-IV Demo cohort extract:
1. Run the g-formula pipeline from L09 notebook
2. Submit notebook outputs and short answers

---

## Tasks

### 1. Derivation

Write the standardization formula and state conditional exchangeability + positivity.

### 2. Coding

G-formula estimate + bootstrap CI:
- Specify E[Y|A,L] model (formula; include nonlinear terms if justified)
- Produce standardized estimates for E[Y^1] and E[Y^0] + effect measure
- Run bootstrap (≥200 replicates) and plot bootstrap distribution

### 3. Comparison

Contrast with IPW results from L08 (one paragraph).

---

## Deliverables

- **Notebook**: `HW09_gformula_standardization.ipynb` (runs end-to-end)
- **Summary**: `HW09_summary.md` (≤1 page)

## Submission

Submit via GitHub (PR or release tag) or Canvas as instructed.

## Grading Rubric

- Derivation (25%): Correct formula and assumptions
- Coding (50%): Correct implementation, bootstrap CI
- Comparison (25%): Thoughtful comparison with IPW
