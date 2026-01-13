# Target Trial Protocol Template

**Team:** [Team name]  
**Date:** [Date]  
**Protocol version:** v1

---

## 1. Causal Question (Informal)

- **Population:**  
- **Intervention / strategy A=1:**  
- **Comparator / strategy A=0:**  
- **Outcome:**  
- **Time zero (index):**  
- **Estimand:** (ATE? ATT? risk difference at 28 days? etc.)

---

## 2. Target Trial Specification

| Component | Your choice (precise, implementable) |
|---|---|
| Eligibility criteria | |
| Treatment strategies | |
| Assignment procedure | (observational analogue; how you emulate randomization) |
| Follow-up (start/end) | |
| Outcome definition | |
| Causal contrast | (intention-to-treat vs per-protocol analogue) |
| Analysis plan | (estimator: g-formula / IPW / MSM / doubly robust; diagnostics) |

---

## 3. DAG + Confounder Set

- Draw a DAG for your question (baseline + time-varying, if needed).
- List the minimal adjustment set(s) you will use and justify clinically.

---

## 4. Data Mapping (MIMIC Variables)

- Map each trial component to MIMIC variables / tables.
- Define code lists / thresholds (ICD, labs, vitals) where needed.

---

## 5. Threat Model (Bias Audit)

- **Exchangeability:** what's missing / unmeasured?
- **Positivity:** where do treatment strategies become unrealistic?
- **Consistency:** multiple versions of treatment?
- **Measurement error:** outcome/treatment misclassification?
- **Selection bias:** censoring / discharge / loss to follow-up?
- **Time zero errors:** immortal time bias / mis-specified start of follow-up?

---

## 6. Deliverables Checklist

- [ ] Target trial table (filled)
- [ ] 1-page methods memo (PDF)
- [ ] Reproducible notebook(s) that run on Demo data
- [ ] Figures: DAG, weight diagnostics (if IPW/MSM), effect estimates with CI
