# Homework 13: Target trial emulation II: hands-on workshop (analysis pipeline)

**Team-based assignment** (2-person teams)

## Instructions

Complete the following tasks using the workshop notebook from L13:
1. Execute your protocol using the analysis pipeline
2. Submit repo PR with results

---

## Tasks

### 1. End-to-end pipeline

Execute your protocol:
- Load cohort extract (or build from Demo)
- Define cohort per protocol
- Run estimator using template functions
- Diagnostics (overlap, weights histogram, covariate balance or model fit)
- Export results to `results/`

### 2. Results bundle

Produce:
- 1 table (effect estimates)
- 1 figure (main diagnostic or result)
- 1 paragraph interpretation

---

## Deliverables

Submit a repo PR containing:
- `analysis.ipynb` (runs end-to-end)
- `results/` (1 figure + 1 table)
- `interpretation.md` (≤1 page: estimand, assumptions, result, limitation)

## Submission

Submit via GitHub PR as instructed.

## Grading Rubric

- Pipeline execution (50%): Runs without errors, all steps completed
- Results (30%): Clear table and figure
- Interpretation (20%): Honest, clear assessment
