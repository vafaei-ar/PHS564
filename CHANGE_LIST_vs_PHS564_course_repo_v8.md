# Change list derived from `PHS564_course_repo/` (read-only) vs current main repo

This file records **what must change** in the main repository to match the updated plan and materials stored in:

- `PHS564_course_repo/plan/`
- `PHS564_course_repo/lectures/`
- `PHS564_course_repo/data/`

## Global / structural changes

- **Canonical repository layout**
  - Switch to: `plan/`, `lectures/`, `data/`, `requirements.txt`, `README.md` at repo root.
  - Lecture layout becomes: `lectures/Lxx_<slug>/{student/, instructor/}`.
  - Each lecture has **exactly**:
    - one student notebook `*_student.ipynb`
    - one instructor solution notebook `*_instructor_solution.ipynb`

- **Notebook conventions (“ipynb help”)**
  - Adopt the “**fill‑in‑the‑blank**” approach:
    - students edit **only** cells marked `TODO`
    - keep explicit step-by-step code (no “clever” one‑liners)
  - Notebooks must:
    - be runnable locally and in Colab (when the repo is cloned)
    - locate repo root robustly from `Path.cwd()` (walk up until `README.md`/`requirements.txt`)
    - use standard notation/columns (`A`, `Y`, `L`, etc.) and explicit variable lists like `L_list`
  - Statistical graphics required by the slide blueprint are saved under `figures/LXX/` and referenced as “From notebook” figures.

- **Data policy and data workflow**
  - Data directory structure must support:
    - `data/raw/` (optional; **do not commit**)
    - `data/processed/` (instructor-provided analysis-ready cohort extracts)
  - Add/align `data/download_data.py` (MIMIC-IV Demo downloader) and notebook error messages that instruct running it.
  - L08–L11 rely on **processed cohort extracts** (Parquet preferred, CSV fallback):
    - `cohort_L08_ps_ipw.(parquet|csv)`
    - `cohort_L09_gformula.(parquet|csv)`
    - `cohort_L10_survival.(parquet|csv)`
    - `cohort_L11_msm_longitudinal.(parquet|csv)`

- **Dependencies**
  - Replace the “course-as-a-Python-package” approach with lightweight notebook dependencies.
  - Align `requirements.txt` to the minimal set used in `PHS564_course_repo` (notably includes `pyarrow`).

- **Updated planning documents (source of truth)**
  - Replace/align to:
    - `plan/PHS564_course_build_plan_AI_ready_v8_MIMICdemo_polls_IV_optional.md`
    - `plan/PHS564_slides_master_plan_NotebookLM_v3_MIMICdemo_survival_MSM_capstone.md`
    - `plan/PHS564_in_class_exit_polls_bank_v1.md`
    - `plan/PHS564_Syllabus_Spring2026_filled_v7b_MIMICdemo_polls_survival_MSM.docx`

- **Exit polls (new deliverable)**
  - Add/maintain a bank of 3–5 end-of-class items per lecture (`plan/PHS564_in_class_exit_polls_bank_v1.md`).

## Lecture sequence / topical changes (high-level)

- **L01–L07**: remain conceptual foundations, but notebooks are rewritten to the fill‑in‑the‑blank + explicit pipeline style.
- **L08–L12 are substantially re-scoped around MIMIC-IV Demo**:
  - **L08** becomes: IPW + propensity score diagnostics (MIMIC-IV Demo processed cohort extract).
  - **L09** becomes: Standardization / parametric g-formula + “why model” (MIMIC-IV Demo extract; compare vs IPW).
  - **L10** becomes: causal survival analysis (discrete-time hazards + IPCW) (MIMIC-IV Demo extract).
  - **L11** becomes: MSMs for time-varying confounding (longitudinal person-period extract).
  - **L12** becomes: target trial emulation workshop + capstone/project alignment (protocol-heavy).
  - **IV** is now an **optional asynchronous mini-module**, not a core in-class lecture.

## Lecture folder naming changes (canonical slugs)

New canonical lecture directories (as in `PHS564_course_repo/lectures/`):

- `L01_counterfactuals_definition`
- `L02_ideal_rct`
- `L03_observational_assumptions`
- `L04_effect_modification`
- `L05_dags_dseparation`
- `L06_confounding`
- `L07_selection_bias`
- `L08_ipw_propensity`
- `L09_gformula_standardization`
- `L10_causal_survival`
- `L11_msm_time_varying`
- `L12_target_trial_workshop`

## Required updates to existing main repo artifacts

- **Replace existing lecture materials** (older lecture folder names, older notebooks, older slides) with the new canonical lecture directories + notebooks from the v8 plan.
- **Deprecate/remove** the previous `src/phs564_ci/`-package style from the student workflow (can be archived, but not the primary path).
- **Align README** to the “clone in Colab” workflow and the processed-extract policy.

