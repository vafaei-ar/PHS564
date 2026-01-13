# Homework 02: Causal effects in ideal randomized trials

**Team-based assignment** (2-person teams)

## Instructions

Complete the following tasks and submit:
1. One Jupyter notebook with your code and outputs
2. A short summary (≤1 page PDF/markdown) with your answers

---

## Tasks

### 1. Conceptual question

In an ideal RCT, under what condition can Pr(Y=1|A=1) be interpreted causally? Explain in 3–5 sentences.

### 2. Conditional randomization

Show (with algebra) why standardization recovers the marginal causal risk when treatment is conditionally randomized.

### 3. Coding

Generate trial data with stratified randomization:
- Create a dataset with a binary confounder L and treatment A assigned conditionally on L
- Estimate RD/RR with and without standardization
- Report both estimates and explain why they differ (or don't)

### 4. Positivity violation

Give a concrete example of a positivity violation in a trial. Explain why it's a problem.

---

## Deliverables

- **Notebook**: `HW02_ideal_rct.ipynb`
- **Summary**: `HW02_summary.md` (≤1 page)

## Submission

Submit via GitHub (PR or release tag) or Canvas as instructed.

## Grading Rubric

- Conceptual question (25%): Clear explanation
- Algebra derivation (25%): Correct mathematical reasoning
- Coding (35%): Correct implementation, clear comparison
- Positivity example (15%): Relevant, well-explained example
