# Exit Poll: Lecture 09 — Standardization + g-formula (MIMIC-IV Demo)

1) **MCQ:** In the g-formula algorithm for a binary outcome, we:  
- A. regress A on Y  
- B. model \(E[Y|A,L]\), predict under A=1 and A=0, then average  
- C. match on outcome  
- D. compute weights from \(Pr(Y|A,L)\) directly  
**Key:** B

2) **MCQ:** Compared to IPW, g-formula is more sensitive to:  
- A. weight truncation choice  
- B. outcome model misspecification  
- C. overlap in propensity score  
- D. censoring mechanisms  
**Key:** B

3) **MCQ:** Bootstrapping a g-formula estimate means:  
- A. resampling predicted outcomes without refitting the model  
- B. resampling individuals and repeating the full procedure (including refitting)  
- C. adding random noise to the outcome  
- D. using asymptotic normality only  
**Key:** B

4) **Short answer:** Why can “excellent prediction” still produce biased causal estimates?

---
