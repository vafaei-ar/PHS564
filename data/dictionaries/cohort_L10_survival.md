# Cohort Dictionary: L10 Causal Survival Analysis

**Cohort extract:** `cohort_L10_survival.parquet` (or `.csv`)

## Description

Wide-format survival cohort for discrete-time survival analysis with time-to-event outcomes.

## Variables

### Treatment
- **`A`** (int): Binary treatment indicator (baseline/early exposure)

### Outcome (time-to-event)
- **`E`** (int): Event indicator (1 = event occurred, 0 = censored)
- **`T`** (int): Follow-up time (days or time periods)

### Confounders (baseline)
- **`age`** (float): Age in years
- **`sex_male`** (int): Sex indicator (1 = male, 0 = female)

### Identifiers
- **`hadm_id`** (int): Hospital admission identifier

## Cohort Definition

- **Time zero:** ICU admission
- **Exposure window:** First 6–24 hours
- **Follow-up:** Up to 28 days or discharge
- **Event:** Death or other time-to-event outcome

## Notes

- Convert to person-period format for analysis
- Censoring: administrative or informative (if applicable)
