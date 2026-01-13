# Homework 01: Counterfactuals and definition of causal effects

**Team-based assignment** (2-person teams)

## Instructions

Complete the following tasks and submit:
1. One Jupyter notebook with your code and outputs
2. A short summary (≤1 page PDF/markdown) with your answers

---

## Tasks

### 1. Definitions (written)

Write the estimand for:
- Causal mean difference
- Causal risk difference
- Causal risk ratio
- Causal odds ratio

### 2. Well-defined intervention

Pick one vague exposure (e.g., "diet quality") and define 2 realistic interventions. Discuss:
- What are the "versions" of each intervention?
- How does this relate to the consistency assumption?

### 3. Simulation (Python/R/SAS)

Simulate potential outcomes and generate observed data under:
- (i) Randomized assignment
- (ii) Confounded assignment

Compare causal effect vs observed association; include 1 figure.

**Requirements:**
- Set a random seed for reproducibility
- Generate potential outcomes Y(a=0) and Y(a=1)
- Show both scenarios (RCT vs confounded)
- Visualize the difference between association and causation

### 4. Reflection

In 5–7 sentences: why "association is not causation" in your simulation?

---

## Deliverables

- **Notebook**: `HW01_counterfactuals_definition.ipynb`
- **Summary**: `HW01_summary.md` (≤1 page)
- **Figure**: Save as `HW01_figure.png`

## Submission

Submit via GitHub (PR or release tag) or Canvas as instructed.

## Grading Rubric

- Definitions (20%): Correct estimand formulas
- Well-defined intervention (20%): Clear, implementable interventions
- Simulation (40%): Correct implementation, clear visualization
- Reflection (20%): Thoughtful connection to course concepts
