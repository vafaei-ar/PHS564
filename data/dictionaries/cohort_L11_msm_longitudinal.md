# Cohort Dictionary: L11 MSM (Time-Varying)

**Cohort extract:** `cohort_L11_msm_longitudinal.parquet` (or `.csv`)

## Description

Long-format person-period dataset for marginal structural models (MSMs) with time-varying treatment and confounding.

## Variables

### Identifiers
- **`stay_id`** (int): Unique ICU stay identifier
- **`t_day`** (int): Day of follow-up (1, 2, 3, ...)

### Treatment (time-varying)
- **`A_t`** (int): Treatment indicator at time t
  - Derived from vitals (e.g., mean HR > threshold on day t)

### Time-varying Confounders
- **`hr_mean`** (float): Mean heart rate on day t

### Baseline Confounders
- **`age`** (float): Age in years
- **`sex_male`** (int): Sex indicator (1 = male, 0 = female)

### Outcome
- **`Y`** (int): Final outcome (binary, measured at end of follow-up)

## Cohort Definition

- **Time zero:** ICU admission
- **Follow-up:** Up to 7 days (or t_max as specified)
- **Treatment:** Time-varying (measured daily)
- **Format:** One row per person-period

## Notes

- Long format: multiple rows per person (one per time period)
- Treatment and time-varying confounders measured at each time point
- Outcome measured at end of follow-up
