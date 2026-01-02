# PHS564 — Causal Inference (Course Repo)

This repository contains **student** and **instructor** Jupyter notebooks for all 12 lectures.

Design principle: **fill‑in‑the‑blank**.
- Students edit *only* model specifications and a few short analysis lines.
- The rest of the pipeline is explicit, procedural, and readable.

---

## Quickstart (local)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Open notebooks with JupyterLab / VSCode.

---

## Quickstart (Google Colab)

Recommended workflow:
1) Clone the repo inside Colab:
```bash
!git clone <YOUR_GITHUB_REPO_URL>
%cd <REPO_FOLDER_NAME>
!pip -q install -r requirements.txt
```
2) Open a notebook under `lectures/Lxx_*/student/` and run top‑to‑bottom.

> If you open a notebook directly from GitHub (without cloning), relative paths will break.

---

## Lecture notebooks

Each lecture has:
- `student/` — student notebook
- `instructor/` — instructor solution notebook

Lectures:
- L01 Counterfactuals and causal effects
- L02 Ideal randomized trials
- L03 Observational studies: identification assumptions
- L04 Effect modification
- L05 DAGs and collider bias
- L06 Confounding and adjustment strategies
- L07 Selection bias and censoring weights
- L08 IPW pipeline (MIMIC-IV Demo extract)
- L09 Standardization / g-formula (MIMIC-IV Demo extract)
- L10 Causal survival analysis (MIMIC-IV Demo extract)
- L11 MSMs for time‑varying confounding (MIMIC-IV Demo extract)
- L12 Target trial emulation workshop (capstone)

---

## Data policy

### Raw MIMIC-IV Demo
You may download MIMIC-IV Demo (if the instructor asks you to) into `data/raw/`:
```bash
python data/download_data.py
```
**Do not commit any raw data** under `data/raw/` to GitHub.

### Processed cohort extracts (required for L08–L11)
For teaching and homework equity, L08–L11 expect **instructor‑provided processed extracts** under `data/processed/`:

- `cohort_L08_ps_ipw.parquet` (or `.csv`)
- `cohort_L09_gformula.parquet` (or `.csv`)
- `cohort_L10_survival.parquet` (or `.csv`)
- `cohort_L11_msm_longitudinal.parquet` (or `.csv`)
- (optional) `cohort_L12_capstone.parquet` (or `.csv`)

If these are missing, the notebooks will raise a `FileNotFoundError` with instructions.

---

## Repository structure (high level)

```
data/
  raw/            # optional, do not commit
  processed/      # instructor-provided cohort extracts (do not commit unless allowed)
lectures/
  L01_.../
    student/
    instructor/
  ...
```
