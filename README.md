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

**Option 1: Open directly in Colab (recommended)**
- Click the "Open In Colab" badge next to any lecture below
- The notebook will open in Colab (from GitHub)
- **Run the first “Colab bootstrap” cell** in the notebook (it clones the repo + installs requirements)

**Option 2: Clone manually (rarely needed)**
1) Clone the repo inside Colab:
```bash
!git clone https://github.com/vafaei-ar/PHS564.git
%cd PHS564
!pip -q install -r requirements.txt
```
2) Open a notebook under `lectures/Lxx_*/student/` and run top‑to‑bottom.

---

## Lecture notebooks (with Colab links)

Each lecture has:
- `student/` — student notebook
 
> Instructor solution notebooks are **not** published in this public repository.

| Lecture | Topic | Student Notebook (Colab) |
| :--- | :--- | :--- |
| L01 | Counterfactuals and causal effects | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vafaei-ar/PHS564/blob/main/lectures/L01_counterfactuals_definition/student/L01_counterfactuals_definition_student.ipynb) |
| L02 | Ideal randomized trials | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vafaei-ar/PHS564/blob/main/lectures/L02_ideal_rct/student/L02_ideal_rct_student.ipynb) |
| L03 | Observational studies: identification assumptions | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vafaei-ar/PHS564/blob/main/lectures/L03_observational_assumptions/student/L03_observational_assumptions_student.ipynb) |
| L04 | Effect modification | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vafaei-ar/PHS564/blob/main/lectures/L04_effect_modification/student/L04_effect_modification_student.ipynb) |
| L05 | DAGs and collider bias | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vafaei-ar/PHS564/blob/main/lectures/L05_dags_dseparation/student/L05_dags_dseparation_student.ipynb) |
| L06 | Confounding and adjustment strategies | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vafaei-ar/PHS564/blob/main/lectures/L06_confounding/student/L06_confounding_student.ipynb) |
| L07 | Selection bias and censoring weights | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vafaei-ar/PHS564/blob/main/lectures/L07_selection_bias/student/L07_selection_bias_student.ipynb) |
| L08 | IPW pipeline (MIMIC-IV Demo extract) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vafaei-ar/PHS564/blob/main/lectures/L08_ipw_propensity/student/L08_ipw_propensity_student.ipynb) |
| L09 | Standardization / g-formula (MIMIC-IV Demo extract) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vafaei-ar/PHS564/blob/main/lectures/L09_gformula_standardization/student/L09_gformula_standardization_student.ipynb) |
| L10 | Causal survival analysis (MIMIC-IV Demo extract) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vafaei-ar/PHS564/blob/main/lectures/L10_causal_survival/student/L10_causal_survival_student.ipynb) |
| L11 | MSMs for time‑varying confounding (MIMIC-IV Demo extract) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vafaei-ar/PHS564/blob/main/lectures/L11_msm_time_varying/student/L11_msm_time_varying_student.ipynb) |
| L12 | Target trial emulation workshop (capstone) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vafaei-ar/PHS564/blob/main/lectures/L12_target_trial_workshop/student/L12_target_trial_workshop_student.ipynb) |

---

## Data policy

### Raw MIMIC-IV Demo
You may download MIMIC-IV Demo (if the instructor asks you to) into `data/raw/`.

**In Google Colab (recommended):**
Add this cell at the top of your notebook:
```python
# Download MIMIC-IV Demo data (Colab-friendly)
import sys
from pathlib import Path

# Add repo root to path
repo_root = Path.cwd()
if (repo_root / "data" / "download_data.py").exists():
    sys.path.insert(0, str(repo_root))
else:
    # If running from a subdirectory, find repo root
    for _ in range(4):
        repo_root = repo_root.parent
        if (repo_root / "data" / "download_data.py").exists():
            sys.path.insert(0, str(repo_root))
            break

from data.download_data import download_mimic_demo

# Download MIMIC-IV Demo (uses pure Python, no wget needed)
download_mimic_demo()  # Downloads to data/raw/
```

**Local installation:**
```bash
python data/download_data.py
```

**Do not commit any raw data** under `data/raw/` to GitHub.

### Processed cohort extracts (required for L08–L11)
Lectures L08–L11 expect **analysis-ready cohort extracts** under `data/processed/`:

- `cohort_L08_ps_ipw.parquet` (or `.csv`)
- `cohort_L09_gformula.parquet` (or `.csv`)
- `cohort_L10_survival.parquet` (or `.csv`)
- `cohort_L11_msm_longitudinal.parquet` (or `.csv`)
- (optional) `cohort_L12_capstone.parquet` (or `.csv`)

If these are missing, build them from raw MIMIC-IV Demo:

```bash
python data/build_processed_extracts_demo.py --exposure-mode admission_type
# optional alternative exposure definition:
# python data/build_processed_extracts_demo.py --exposure-mode vitals --hr-threshold 100
```

In Colab, the applied lecture notebooks include a “Build the processed cohort extract” cell you can run once.

---

## Repository structure (high level)

```
data/
  raw/            # optional, do not commit
  processed/      # derived cohort extracts (do not commit)
lectures/
  L01_.../
    student/
    instructor/
  ...
```
