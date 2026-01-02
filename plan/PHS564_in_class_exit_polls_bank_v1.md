# PHS564 — In-class exit polls (12 sessions)

**Purpose:** 5-minute end-of-class “exit poll” that (i) forces retrieval practice, (ii) gives you fast feedback on misconceptions, and (iii) creates a lightweight participation grade.

**Format:** 3–5 items per lecture (mostly multiple choice) + 1 optional free-text “muddiest point”.  
**Grading suggestion:** completion-based with 1–2 auto-graded knowledge checks (to discourage random clicking).  
**Delivery options:** Canvas “New Quiz”, PollEverywhere, iClicker Cloud, or a short Google Form.

**Instructor note:** For Lecture 1, the poll also collects background information for team formation (clinical + programming mix).

---

## L01 — Counterfactuals and definition of causal effects (team formation + concept check)

1) **Your programming comfort (Python)**  
- A. Never used  
- B. Beginner (can run notebooks, basic pandas)  
- C. Intermediate (write functions, debug)  
- D. Advanced (package-level work)

2) **Languages you can realistically use this semester (select all)**  
- A. Python  
- B. R  
- C. SAS  
- D. SQL  
- E. None / need support

3) **Your clinical/biomedical domain comfort (self-report)**  
- A. Minimal (non-clinical background)  
- B. Some (took clinical/epi courses)  
- C. Moderate (worked with clinical data / workflows)  
- D. High (clinical training or deep ICU/EHR experience)

4) **Team preference**  
- A. Prefer partner with stronger coding  
- B. Prefer partner with stronger clinical context  
- C. No preference  
- D. Prefer to work solo (**only if you allow**)

5) **Concept check (MCQ):** Which statement is closest to the meaning of a causal effect?  
- A. Difference in observed outcomes between treated and untreated  
- B. Difference between the outcome if treated vs if untreated **for the same person/population**  
- C. Correlation between treatment and outcome  
- D. Regression coefficient of treatment  
**Key:** B

Free text (optional): “What part of today’s material is still unclear?”

---

## L02 — Causal effects in ideal randomized trials

1) **MCQ:** In an ideal randomized trial, exchangeability holds mainly because:  
- A. Large sample size  
- B. Randomization breaks common causes of treatment and outcome  
- C. Blinding guarantees no confounding  
- D. Regression adjustment is used  
**Key:** B

2) **MCQ:** “Consistency” is violated when:  
- A. Treatment assignment is not random  
- B. The treatment is ill-defined (different versions)  
- C. There is loss to follow-up  
- D. Outcomes are rare  
**Key:** B

3) **MCQ:** Positivity means:  
- A. Everyone has outcome probability >0  
- B. Everyone has treatment probability >0 and <1 within covariate strata  
- C. The causal effect is beneficial  
- D. No measurement error  
**Key:** B

4) **Short answer (1–2 sentences):** What is the estimand in a two-arm RCT with binary outcome? (risk difference / risk ratio / etc.)

Free text: muddiest point.

---

## L03 — Causal effects in observational studies (identifiability and assumptions)

1) **MCQ:** In observational studies, to identify \(E[Y^1]\) using observed data, we typically need:  
- A. Only consistency  
- B. Consistency + positivity + conditional exchangeability  
- C. Randomization  
- D. No missing data  
**Key:** B

2) **MCQ:** Conditional exchangeability given \(L\) means:  
- A. \(A \perp Y\)  
- B. \(A \perp Y^a \mid L\)  
- C. \(Y^1 = Y^0\)  
- D. \(L \perp Y\)  
**Key:** B

3) **MCQ:** The main reason crude treated vs untreated comparison is biased is usually:  
- A. small sample size  
- B. confounding  
- C. measurement error in outcome  
- D. positivity violation  
**Key:** B

4) **Short answer:** Give one example of a pre-treatment confounder in an ICU antibiotic question.

---

## L04 — Effect modification and effect-measure modification

1) **MCQ:** Effect modification is a property of:  
- A. the estimator only  
- B. the causal effect in the population and the chosen effect measure  
- C. sampling variability only  
- D. randomization only  
**Key:** B

2) **MCQ:** If risk difference is constant across strata but risk ratio varies, then:  
- A. there is no effect modification  
- B. effect modification depends on the chosen effect measure  
- C. both measures must show the same pattern  
- D. this cannot happen  
**Key:** B

3) **MCQ:** The most defensible way to report effect modification is:  
- A. report subgroup p-values only  
- B. report stratum-specific causal effects + uncertainty + a clear estimand  
- C. pick the most significant subgroup  
- D. only report interaction coefficient without interpretation  
**Key:** B

4) **Short answer:** What is the difference between interaction in a regression model and causal effect modification?

---

## L05 — DAGs, d-separation, and collider bias

1) **MCQ:** A collider is a variable that:  
- A. causes both A and Y  
- B. is caused by both A and Y  
- C. lies on the causal pathway A→Y  
- D. is independent of A and Y  
**Key:** B

2) **MCQ:** Conditioning on a collider typically:  
- A. reduces confounding  
- B. opens a non-causal path and can induce bias  
- C. guarantees exchangeability  
- D. has no effect  
**Key:** B

3) **MCQ:** A minimal sufficient adjustment set aims to:  
- A. include as many variables as possible  
- B. block all backdoor paths without conditioning on colliders  
- C. block the causal path A→Y  
- D. maximize prediction accuracy  
**Key:** B

4) **Short answer:** In one sentence, why “adjust for everything” is bad advice?

---

## L06 — Confounding: definition, confounders, and adjustment strategies

1) **MCQ:** A confounder is (best definition):  
- A. any variable associated with exposure  
- B. any variable associated with outcome  
- C. a pre-exposure common cause of exposure and outcome (or proxy) that opens a backdoor path  
- D. any post-exposure mediator  
**Key:** C

2) **MCQ:** Adjusting for a mediator will typically:  
- A. estimate the total effect  
- B. block part of the causal effect (estimating controlled direct effect or worse)  
- C. never changes the estimate  
- D. always reduces variance  
**Key:** B

3) **MCQ:** Regression adjustment targets a causal estimand only if:  
- A. the model predicts well  
- B. exchangeability/positivity/consistency hold and the model is correctly specified for the identification functional  
- C. the p-value is <0.05  
- D. residuals are normal  
**Key:** B

4) **Short answer:** Name one adjustment strategy besides regression (e.g., matching, weighting, stratification, standardization).

---

## L07 — Selection bias (structure and adjustment)

1) **MCQ:** Selection bias often arises when we condition on:  
- A. a confounder  
- B. a collider related to selection into the study  
- C. randomization indicator  
- D. an instrument  
**Key:** B

2) **MCQ:** Inverse probability of censoring weighting (IPCW) requires that:  
- A. censoring is completely random  
- B. censoring is independent of the outcome given measured history (conditional exchangeability for censoring)  
- C. no confounding exists  
- D. hazards are proportional  
**Key:** B

3) **MCQ:** A key warning sign for selection adjustment is:  
- A. narrow CI  
- B. extreme censoring weights / lack of overlap  
- C. large sample size  
- D. balanced covariates  
**Key:** B

4) **Short answer:** Give one real-world source of selection/censoring in EHR studies.

---

## L08 — IPW for confounding + diagnostics (MIMIC-IV Demo)

1) **MCQ:** Stabilized weight for treated is roughly:  
- A. \(Pr(A=1|L)\)  
- B. \(Pr(A=1)/Pr(A=1|L)\)  
- C. \(Pr(A=0)/Pr(A=1|L)\)  
- D. \(1/Pr(A=0|L)\)  
**Key:** B

2) **MCQ:** If propensity score overlap is poor, the main problem is:  
- A. bias is guaranteed to be zero  
- B. positivity is violated or near-violated, causing unstable estimates  
- C. you should always add more covariates  
- D. p-values become smaller  
**Key:** B

3) **MCQ:** After weighting, we primarily check balance using:  
- A. R²  
- B. standardized mean differences (SMD) / love plot  
- C. AIC  
- D. residual normality  
**Key:** B

4) **Short answer:** In one sentence, what pseudo-population does IPW create?

Free text: muddiest point.

---

## L09 — Standardization + g-formula (MIMIC-IV Demo)

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

## L10 — Causal survival analysis (MIMIC-IV Demo)

1) **MCQ:** The survival function \(S(t)\) is:  
- A. \(Pr(T \le t)\)  
- B. \(Pr(T > t)\)  
- C. the hazard at time t  
- D. the risk difference  
**Key:** B

2) **MCQ:** Discrete-time hazard modeling typically uses:  
- A. linear regression on T  
- B. pooled logistic regression on person-period data  
- C. naive Kaplan–Meier only  
- D. OLS on censoring indicator  
**Key:** B

3) **MCQ:** IPCW for censoring is valid if censoring is:  
- A. always independent of outcome without conditioning  
- B. conditionally independent of potential outcomes given measured history  
- C. deterministic  
- D. absent  
**Key:** B

4) **Short answer:** Why is “time zero” definition critical for avoiding immortal time bias?

---

## L11 — MSMs for time-varying treatments (MIMIC-IV Demo)

1) **MCQ:** Time-varying confounding “affected by prior treatment” breaks standard adjustment because:  
- A. it makes data too large  
- B. it creates a mediator-confounder that cannot be conditioned on without bias  
- C. it guarantees positivity  
- D. it removes selection bias  
**Key:** B

2) **MCQ:** Stabilized MSM weight at time t combines:  
- A. only treatment model numerator  
- B. treatment weights and censoring weights over time  
- C. only outcome model  
- D. only baseline covariates  
**Key:** B

3) **MCQ:** A practical symptom of a broken MSM analysis is:  
- A. weights close to 1 for everyone  
- B. extreme weights that dominate the estimate  
- C. outcome model converges  
- D. many covariates  
**Key:** B

4) **Short answer:** In one sentence, what does an MSM estimate (interpretation)?

---

## L12 — Capstone target trial emulation workshop

1) **MCQ:** In a target trial protocol, “treatment strategies” refer to:  
- A. the statistical estimator  
- B. the interventions being compared (including timing and duration)  
- C. the outcome model  
- D. the confounder set only  
**Key:** B

2) **MCQ:** The single most common preventable bias in EHR “treatment timing” studies is:  
- A. random error  
- B. immortal time bias from incorrect time zero / exposure window  
- C. publication bias  
- D. multicollinearity  
**Key:** B

3) **MCQ:** A minimal credible reporting sentence includes:  
- A. only a p-value  
- B. “Under assumptions X/Y/Z, we estimate …” + estimand + main limitation  
- C. only an odds ratio  
- D. only model coefficients  
**Key:** B

4) **Short answer:** What is your team’s (one) biggest remaining risk for bias, and what is your mitigation?

Free text: muddiest point.

