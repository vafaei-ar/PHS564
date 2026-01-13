# Homework 11: Time-varying treatment and confounding: marginal structural models (MSMs)

**Team-based assignment** (2-person teams)

## Instructions

Complete the following tasks using the MIMIC-IV Demo cohort extract:
1. Run the MSM pipeline from L11 notebook
2. Submit notebook outputs and short answers

---

## Tasks

### 1. Time-varying DAG

Draw a time-varying DAG for your cohort; explain why L_t is problematic.

### 2. Coding

Construct weights and fit an MSM:
- Specify numerator/denominator models (formulas)
- Compute stabilized weights (treatment weights; censoring weights if applicable)
- Diagnose weights (distribution over time, truncation)
- Fit weighted MSM and interpret

### 3. Interpretation

1 paragraph on assumptions + one key limitation.

---

## Deliverables

- **Notebook**: `HW11_msm_time_varying.ipynb` (runs end-to-end)
- **Summary**: `HW11_summary.md` (≤1 page)
- **Figure**: Weight diagnostics plot

## Submission

Submit via GitHub (PR or release tag) or Canvas as instructed.

## Grading Rubric

- DAG (25%): Correct structure, clear explanation
- Coding (55%): Correct weight construction and MSM fitting
- Interpretation (20%): Clear assumptions and limitations
