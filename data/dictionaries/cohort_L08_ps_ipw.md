# Cohort Dictionary: L08 IPW/Propensity Score

**Cohort extract:** `cohort_L08_ps_ipw.parquet` (or `.csv`)

## Description

Baseline/early exposure cohort for IPW and propensity score analysis. Designed for point treatment with binary or continuous outcome.

## Variables

### Treatment
- **`A`** (int): Binary treatment indicator
  - `A = 1`: Treated (e.g., emergency admission or high HR)
  - `A = 0`: Control (e.g., non-emergency admission or low HR)

### Outcome
- **`Y`** (int or float): Outcome variable
  - Binary: in-hospital death (0/1)
  - Continuous: length of stay, etc.

### Confounders (baseline)
- **`age`** (float): Age in years
- **`sex_male`** (int): Sex indicator (1 = male, 0 = female)
- **`los`** (float): Length of stay (days)

### Identifiers
- **`stay_id`** (int): Unique ICU stay identifier
- **`hadm_id`** (int): Hospital admission identifier (if available)

## Cohort Definition

- **Time zero:** ICU admission
- **Exposure window:** First 6–24 hours of ICU stay
- **Follow-up:** In-hospital mortality or discharge
- **Eligibility:** [To be specified based on build script]

## Notes

- Derived from MIMIC-IV Demo
- Missing values: [To be documented]
- Units: [To be specified]
