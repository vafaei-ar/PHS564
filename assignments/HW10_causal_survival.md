# Homework 10: Causal survival analysis: time-to-event outcomes, censoring, discrete-time hazards

**Team-based assignment** (2-person teams)

## Instructions

Complete the following tasks using the MIMIC-IV Demo cohort extract:
1. Run the survival analysis pipeline from L10 notebook
2. Submit notebook outputs and short answers

---

## Tasks

### 1. Target trial for time-to-event

Define your target trial for a time-to-event outcome and specify censoring rules.

### 2. Coding

Produce unweighted and IPCW-weighted survival curves:
- Convert to person-period format
- Fit hazard model (pooled logistic)
- Compute survival curves under A=1 and A=0
- If informative censoring: fit censoring model and compute IPCW; re-estimate curves
- Interpret differences

### 3. Short answer

Why "hazard ratio" is not automatically a causal effect measure without assumptions.

---

## Deliverables

- **Notebook**: `HW10_causal_survival.ipynb` (runs end-to-end)
- **Summary**: `HW10_summary.md` (≤1 page)
- **Figure**: Survival curves plot

## Submission

Submit via GitHub (PR or release tag) or Canvas as instructed.

## Grading Rubric

- Target trial (20%): Complete protocol with censoring rules
- Coding (60%): Correct implementation, both weighted and unweighted
- Interpretation (20%): Clear explanation of assumptions
