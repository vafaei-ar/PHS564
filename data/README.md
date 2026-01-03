# Data directory (PHS564)

This course uses **MIMIC-IV Demo** (public). Lectures L08–L11 use **processed cohort extracts** that are built from the raw Demo tables.

## Folder structure

```text
data/
  raw/        # optional downloads (DO NOT COMMIT)
  processed/  # derived cohort extracts (DO NOT COMMIT)
```

## Raw MIMIC-IV Demo (optional)

If/when instructed, you may download MIMIC-IV Demo into `data/raw/`:

```bash
python data/download_data.py
```

**Do not commit** anything under `data/raw/` to GitHub.

## Processed cohort extracts (required for L08–L11)

Lectures **L08–L11** expect analysis-ready cohort extracts under `data/processed/`.

Preferred format is **Parquet** (fast; requires `pyarrow`), with **CSV** as fallback.

Expected files:

- `cohort_L08_ps_ipw.parquet` (or `cohort_L08_ps_ipw.csv`)
- `cohort_L09_gformula.parquet` (or `cohort_L09_gformula.csv`)
- `cohort_L10_survival.parquet` (or `cohort_L10_survival.csv`)
- `cohort_L11_msm_longitudinal.parquet` (or `cohort_L11_msm_longitudinal.csv`)
- (optional) `cohort_L12_capstone.parquet` (or `.csv`) if the instructor provides one

If these are missing, the notebooks will raise a `FileNotFoundError` with instructions.

To build them from raw MIMIC-IV Demo:

```bash
# 1) Download raw Demo tables
python data/download_data.py --method python --out data/raw --version 2.2

# 2) Build teaching cohort extracts into data/processed/
python data/build_processed_extracts_demo.py --exposure-mode admission_type
```
