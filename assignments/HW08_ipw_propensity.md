# Homework 08: IP weighting for confounding (propensity scores) + diagnostics

**Team-based assignment** (2-person teams)

## Instructions

Complete the following tasks using the MIMIC-IV Demo cohort extract:
1. Run the IPW pipeline from L08 notebook
2. Submit notebook outputs and a 1–2 page memo

---

## Tasks

### 1. Target trial block (mandatory)

Write 1–2 paragraphs answering:
- Eligibility criteria
- Time zero
- Exposure window
- Outcome window
- Estimand

### 2. Coding

Run the IPW pipeline:
- Specify propensity model formula (justify covariates as pre-treatment)
- Compute stabilized weights
- Run diagnostics (overlap, weights, balance)
- Estimate marginal causal effect

### 3. Diagnostics panel (required figures)

Save to `figures/L08/`:
- `ps_overlap.png`
- `weights_hist.png`
- `love_plot.png`

### 4. Interpretation

5–8 sentences: "Under assumptions … we estimate …"; mention one limitation.

---

## Deliverables

- **Notebook**: `HW08_ipw_propensity.ipynb` (runs end-to-end)
- **Memo**: `HW08_memo.md` (1–2 pages)
- **Figures**: Saved to `figures/L08/`

## Submission

Submit via GitHub (PR or release tag) or Canvas as instructed.

## Grading Rubric

- Target trial (25%): Complete, implementable protocol
- Coding (35%): Correct pipeline, all steps completed
- Diagnostics (25%): All required figures, clear interpretation
- Interpretation (15%): Clear, honest assessment
