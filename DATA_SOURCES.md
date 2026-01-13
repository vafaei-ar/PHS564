# Data Sources (PHS564)

This course uses publicly available data for teaching causal inference methods.

## Primary Teaching Dataset: MIMIC-IV Demo

**MIMIC-IV Demo** is a publicly available subset of MIMIC-IV (Medical Information Mart for Intensive Care) that does not require credentialing.

- **Source**: https://physionet.org/content/mimiciv-demo/2.2/
- **License**: PhysioNet Credentialed Health Data License 1.5.0
- **Size**: ~100 MB (much smaller than full MIMIC-IV)
- **Access**: No credentialing required; direct download

### What is MIMIC-IV Demo?

MIMIC-IV Demo contains a de-identified subset of the full MIMIC-IV database, designed for:
- Teaching and learning
- Method development
- Reproducible research demonstrations

### Data Structure

The Demo includes the same schema as full MIMIC-IV:
- `patients` - patient demographics
- `admissions` - hospital admission records
- `icustays` - ICU stay records
- `chartevents` - charted events (vitals, lab results)
- `labevents` - laboratory measurements
- And other tables (see MIMIC-IV documentation)

### Course Usage

This course uses **analysis-ready cohort extracts** derived from MIMIC-IV Demo:
- Built using `data/build_processed_extracts_demo.py`
- Stored in `data/processed/` (not committed to Git)
- Used in lectures L08-L11 (and optionally L12-L13)

See `data/README.md` for details on downloading and building extracts.

## Optional: Full MIMIC-IV for Final Projects

Teams may choose to use **full MIMIC-IV** for their capstone projects (requires PhysioNet credentialing).

- **Source**: https://physionet.org/content/mimiciv/2.2/
- **License**: PhysioNet Credentialed Health Data License 1.5.0
- **Access**: Requires completion of CITI training and PhysioNet credentialing
- **Deadline**: Teams must complete credentialing by Week 4 if using full MIMIC-IV

**Important**: Never commit or upload row-level full MIMIC-IV data to GitHub/Colab/Canvas. Share code, SQL queries, and aggregate outputs only.

## Data Policy

1. **MIMIC-IV Demo**: Publicly available; can be downloaded and used freely
2. **Full MIMIC-IV**: Requires credentialing; never commit patient-level data
3. **Processed extracts**: Small enough to be shared; built from Demo schema
4. **Raw data**: Never commit to Git (use `.gitignore`)

## References

- Johnson, A., Bulgarelli, L., Pollard, T., Horng, S., Celi, L. A., & Mark, R. (2023). MIMIC-IV (version 2.2). PhysioNet. https://doi.org/10.13026/6mm1-ek67
- MIMIC-IV Demo: https://physionet.org/content/mimiciv-demo/2.2/
