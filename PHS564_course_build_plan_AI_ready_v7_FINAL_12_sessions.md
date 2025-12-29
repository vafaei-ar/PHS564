# PHS564 — Causal Inference Methods in Epidemiologic Research (Draft course build plan)

**Format:** 12 sessions (up to 120 min each) + optional recitations/labs
**Student work mode:** 2-person teams for coding + mini-projects; individual for short concept checks (optional).  
**Peer evaluation:** short confidential peer check-ins (mid-course and end) to support fair team grading; may adjust team scores by ±10% when there is strong evidence of unequal contribution.
**Primary computing track:** Python (Colab). R/SAS allowed for deliverables, but templates/examples will be in Python.  
**Prerequisites (assumed):** graduate-level epidemiology/biostatistics; comfort with regression (linear/logistic); basic probability; ability to read scientific papers. Coding can be beginner–intermediate, but students must be able to run and modify notebooks.
**Pre-course setup (recommended):** complete the short “Python + Jupyter warm-up” notebook (provided) and ensure access to GitHub + Google Colab.
**Primary dataset for teaching:** NHEFS smoking cessation example (fast onboarding, no IRB/DUA delays).  
**Primary dataset for team projects:** MIMIC-IV (credentialed access via PhysioNet).  
**Core textbook:** Hernán MA, Robins JM. *Causal Inference: What If* (free online + code/data). https://miguelhernan.org/whatifbook

---

## 0) Course learning objectives (what students should be able to do by the end)

1. **Define a causal question** precisely using counterfactuals; distinguish estimand / estimator / estimate.
2. **State and critique assumptions** (consistency, exchangeability, positivity; plus selection assumptions).
3. **Use DAGs** to reason about bias (confounding, collider/selection bias) and choose adjustment sets.
4. **Estimate causal effects** for point treatments using:
   - outcome regression (g-formula / standardization)
   - inverse probability weighting (IPW) and marginal structural models (MSMs)
5. **Diagnose model/identification problems** (positivity issues, weight instability, misspecification).
6. **Communicate results** as a “target trial emulation”: eligibility, treatment strategies, follow-up, outcome, estimand, analysis plan, limitations.

---

## 1) Course structure and assessment (suggested)

### A. Weekly rhythm (simple and high-yield)
- **Before class (30–60 min):** guided reading + 3–5 “concept check” questions (ungraded or low-stakes).
- **In class:** 20–30 min core theory + 30–40 min worked example + 10–20 min active exercise.
- **After class:** one small coding task (team) + short interpretation write-up (≤ 1 page).

### B. Suggested grading (adjust to your program norms)
- Participation / concept checks: 10–15%
- Homeworks (coding + short answers): 40–50%
- Team project (MIMIC): 35–45%
- Reproducibility & code quality rubric: built into HW + project

### C. Team policy (2-person teams)
- Stable teams for most of semester (reduces coordination overhead).
- Each submission lists: (i) division of work, (ii) what was learned, (iii) one open question.
- Encourage “pair programming” at least once per homework.

---

## 2) Computing stack (Python-first, reproducible)

### A. Recommended Python packages
- Core: `numpy`, `pandas`, `scipy`, `statsmodels`, `scikit-learn`
- Graphics: `matplotlib`, `seaborn` (optional), `plotly` (nice for interactive)
- Causal graphs: `networkx`, `graphviz` (or `pydot`)
- Balance diagnostics: `causalml` (optional), or custom standardized mean differences (SMD)
- Robust SE: `statsmodels` robust covariance; bootstrap utilities
- Optional causal libraries (only if you want): `dowhy` (for DAG + estimand), `econml` (advanced—optional)

### B. Colab + GitHub workflow
- One **course GitHub repo** with:
  - `/notebooks/` (Colab notebooks; each lecture has a starter + solution)
  - `/data/` (NOT for patient-level data; store synthetic/NHEFS only)
  - `/src/` (shared helper functions: IP weights, standardization, bootstrap, plots)
  - `/assignments/` (prompts + rubric)
  - `/project/` (templates: proposal, analysis plan, report)
- Students **fork** (or GitHub Classroom) and submit PRs or release tags.

### C. Reproducibility rules (important for MIMIC)
- Never upload **row-level MIMIC data** to GitHub (even de-identified).
- Share: code, SQL queries, cohort definitions, aggregate tables, figures, and logs.
- Use “configuration files” for local paths / credentials.

---



### D. AI-assisted course material generation workflow (Cursor + NotebookLM) — recommended

This file is written to be **machine-actionable**: you can give it to (i) a coding agent (Cursor) to generate a clean teaching repository with runnable Colab notebooks, and (ii) a reading/presentation agent (NotebookLM) to generate slide decks + speaker notes that match the lectures.

**Division of labor (suggested)**
- **Cursor (coding + repo):** create the GitHub repository, Python package utilities, all lecture notebooks (student + instructor solution), assignment prompts, and solution keys.
- **NotebookLM (slides + narration):** generate lecture slide decks (outline + speaker notes), in-class activities, and short “reading guides”.

**Source-of-truth rule (prevents hallucinations)**
- Use *this plan* + *What If* chapters + your existing slides as the primary sources.
- Keep notation consistent (potential outcomes, exchangeability, positivity, consistency; DAG terminology).
- Do **not** introduce new methods unless explicitly requested (e.g., mediation, TMLE, causal discovery).

**Required artifacts per lecture (minimum)**
1. `slides/LXX_<topic>.md` (slide-by-slide outline + speaker notes; convertible to PPTX/Google Slides)
2. `notebooks/LXX_<topic>_student.ipynb` (exercise-driven)
3. `instructor_solutions/LXX_<topic>_solution.ipynb` (full working solution; not released to students until after due date)
4. `assignments/HWXX_<topic>.md` (prompt + rubric + submission instructions)
5. `instructor_solutions/HWXX_<topic>_solution.md` (answer key + code pointers)
6. Optional: `quizzes/QXX_concept_check.md` (5–8 quick questions)

**Quality gates (run before releasing to students)**
- Every notebook runs top-to-bottom in Colab **without manual edits**.
- Plots are readable and labeled; random seeds set for reproducibility.
- No row-level MIMIC data committed; only synthetic/NHEFS in repo.
- Solution notebooks stored in a private location (private repo/branch or instructor-only folder ignored by git).

---
## 3) MIMIC-IV access plan (so projects are feasible)

### A. Access steps (students start early)
1. Create a PhysioNet account.
2. Complete required human-data training (CITI “Data or Specimens Only Research” is commonly required on PhysioNet).  
   - See PhysioNet “CITI Course Instructions”: https://physionet.org/about/citi-course/  
   - See “Required training for MIMIC-IV”: https://physionet.org/content/mimiciv/view-required-training/3.1/
3. Sign the data use agreement and request access to MIMIC-IV on PhysioNet.
4. Use the official hosting options (often via Google Cloud).  
   - MIMIC-IV landing page: https://physionet.org/content/mimiciv/


**Contingency plan (important):** MIMIC credentialing can take time. All homework and teaching notebooks will run on course-provided synthetic/de-identified datasets. If a team does not have MIMIC access by **Week 6**, they may (i) continue on the provided datasets for the final project, or (ii) switch to an alternative public dataset approved by the instructor.

### B. A safe “early start” option: MIMIC-IV demo
If you want students to practice cohort extraction before full credentialing, consider using the **MIMIC-IV demo** dataset (same schema, limited content) for workshops and early assignments:
- PhysioNet demo page: https://physionet.org/content/mimic-iv-demo/
- AWS Open Data Registry entry: https://registry.opendata.aws/mimic-iv-demo/

### C. Reproducible cohort building (recommended)
Use the community **MIMIC Code Repository** for vetted concept definitions (e.g., ventilation, sepsis, comorbidities) and SQL patterns:
- MIT-LCP/mimic-code (main repo): https://github.com/MIT-LCP/mimic-code
- MIMIC-IV concepts folder: https://github.com/MIT-LCP/mimic-code/tree/main/mimic-iv

### D. Practical teaching suggestion
- **Do not wait for MIMIC** to start causal methods. Use NHEFS or synthetic data first.
- Make **MIMIC** the focus of the final project once access is granted.

---

## 4) A “target trial” template (use in every homework + project)
Each team must write (1–2 paragraphs) answering:
1. Eligibility criteria
2. Treatment strategies (A=1 vs A=0; define versions; time zero)
3. Assignment procedure (real-world; what “as-if randomized” assumption means)
4. Follow-up window
5. Outcome definition
6. Causal estimand (risk difference / risk ratio / mean difference)
7. Identification assumptions (exchangeability, positivity, consistency; and for selection)
8. Estimation plan (standardization, IPW/MSM, etc.)
9. Diagnostics + sensitivity discussion

This keeps students **focused** and prevents adding unrelated complexity.

---

# Lecture-by-lecture plan (with materials + coding + homework)

> Notes:
> - “Required reading” is intentionally short.
> - “Suggested/optional” items are for motivated students, or for you to enrich slides.
> - Each lecture includes a **Python/Colab activity** and **homework** with both conceptual and applied parts.

---

## Lecture 1 — Counterfactuals and definition of causal effects
### Assets to generate (slides + notebook + homework)
- Slides: `slides/L01_counterfactuals_definition.md` (outline + speaker notes) → (optional) export to PPTX/Google Slides
- Notebook (student): `notebooks/L01_counterfactuals_definition_student.ipynb`
- Notebook (solution, instructor): `instructor_solutions/L01_counterfactuals_definition_solution.ipynb`
- Homework prompt: `assignments/HW01_counterfactuals_definition.md`
- Homework solutions: `instructor_solutions/HW01_counterfactuals_definition_solution.md`
- Optional concept check: `quizzes/Q01_counterfactuals_definition_concept_check.md`


### Why this lecture
Students must internalize “causal questions live in a counterfactual world” and why association ≠ causation.

### Learning goals
- Define individual vs average causal effects; causal estimands on different scales.
- Explain consistency and why “multiple versions of treatment” and interference matter.
- Distinguish association measures vs causal effect measures.

### Required reading
- Hernán & Robins, *What If*, Chapter 1. https://miguelhernan.org/whatifbook

### Suggested/optional
- Short primer on potential outcomes (any epidemiology-friendly note you like).
- If you want to connect DAGs early: 1–2 slides previewing “common causes” vs “colliders”.

### In-class active learning (10–15 min)
- Give 3 informal questions (e.g., “effect of obesity on mortality”) and ask students to rewrite as interventions with clear versions.
- Small group: “What is the treatment here? What is time zero? What is the outcome?”

### Colab notebook idea
**Notebook 01:** “Potential outcomes in code”
- Simulate a population with potential outcomes Y(a=0), Y(a=1).
- Show: average causal effect vs associational difference under confounding.
- Add an interactive slider for confounding strength (optional with `ipywidgets`).

### Homework (team coding + short answers)
1. **Definitions:** Write the estimand for:
   - causal mean difference, causal risk difference, causal risk ratio, causal odds ratio.
2. **Well-defined intervention:** Pick one vague exposure (e.g., “diet quality”) and define 2 realistic interventions + discuss versions.
3. **Simulation (Python/R/SAS):**
   - Simulate potential outcomes and generate observed data under (i) randomized assignment and (ii) confounded assignment.
   - Compare causal effect vs observed association; include 1 figure.
4. **Reflection:** In 5–7 sentences: why “association is not causation” in your simulation?

Deliverable: one notebook + ≤1 page PDF/markdown summary.

#### Instructor solution sketch (for generating the solution notebook/key)

1. **Estimands**
   - Mean difference: \(E[Y^{1}] - E[Y^{0}]\)
   - Risk difference (binary Y): \(Pr(Y^{1}=1) - Pr(Y^{0}=1)\)
   - Risk ratio: \(Pr(Y^{1}=1)/Pr(Y^{0}=1)\)
   - Odds ratio: \(\{Pr(Y^{1}=1)/Pr(Y^{1}=0)\}/\{Pr(Y^{0}=1)/Pr(Y^{0}=0)\}\)
2. **Well-defined intervention examples**
   - Show 2–3 “vague exposure → concrete intervention” rewrites (e.g., “obesity” → bariatric surgery vs calorie restriction; “SES” → cash transfer; “exercise” → prescribed minutes/week).
   - Explicitly connect to “multiple versions of treatment” and consistency.
3. **Simulation**
   - Data-generating mechanism with confounder \(L\):  
     - Generate \(L\sim Bernoulli(p)\)  
     - Define potential outcomes \(Y^{a}\) via logistic (or linear probability) model depending on \(a\) and \(L\).  
     - Scenario A (RCT): \(A\perp L\). Scenario B (confounded): \(Pr(A=1|L)\) depends on \(L\).
   - Compute:
     - True causal effect from \(\bar Y^{1}, \bar Y^{0}\) (generated from potential outcomes).
     - Observed association from \(Pr(Y=1|A=1) - Pr(Y=1|A=0)\) (or RR).
   - Visualization: show association vs causal effect under both scenarios; optional slider for strength of confounding (via \(Pr(A=1|L)\) or effect of \(L\) on Y).
4. **Reflection key points**
   - Association ≠ causation when \(A\) is not exchangeable (common causes).
   - Individual causal effects are not identified because only one potential outcome is observed per person.


---

## Lecture 2 — Causal effects in ideal randomized trials
### Assets to generate (slides + notebook + homework)
- Slides: `slides/L02_ideal_rct.md` (outline + speaker notes) → (optional) export to PPTX/Google Slides
- Notebook (student): `notebooks/L02_ideal_rct_student.ipynb`
- Notebook (solution, instructor): `instructor_solutions/L02_ideal_rct_solution.ipynb`
- Homework prompt: `assignments/HW02_ideal_rct.md`
- Homework solutions: `instructor_solutions/HW02_ideal_rct_solution.md`
- Optional concept check: `quizzes/Q02_ideal_rct_concept_check.md`


### Learning goals
- Explain how randomization gives exchangeability; contrast unconditional vs conditional randomization.
- Compute causal effects under randomization using observed outcomes.
- Understand positivity and why it is automatic in well-designed trials.

### Required reading
- Hernán & Robins, Chapter 2. https://miguelhernan.org/whatifbook

### In-class: worked example
- Reproduce the tree-based “conditionally randomized experiment” calculation (standardization idea).

### Colab notebook idea
**Notebook 02:** “From RCT tables to causal effects”
- Compute RD/RR from 2×2 table.
- Show stratified randomization example: compute standardized risk.
- Optional: bootstrap CI for RD.

### Homework
1. In an ideal RCT, under what condition can Pr(Y=1|A=1) be interpreted causally? Explain in 3–5 sentences.
2. Conditional randomization: show (with algebra) why standardization recovers the marginal causal risk.
3. Coding:
   - Generate trial data with stratified randomization.
   - Estimate RD/RR with and without standardization; report both.
4. Short question: give a concrete example of positivity violation in a trial.

#### Instructor solution sketch (for generating the solution notebook/key)

1. **Estimands**
   - Mean difference: \(E[Y^{1}] - E[Y^{0}]\)
   - Risk difference (binary Y): \(Pr(Y^{1}=1) - Pr(Y^{0}=1)\)
   - Risk ratio: \(Pr(Y^{1}=1)/Pr(Y^{0}=1)\)
   - Odds ratio: \(\{Pr(Y^{1}=1)/Pr(Y^{1}=0)\}/\{Pr(Y^{0}=1)/Pr(Y^{0}=0)\}\)
2. **Well-defined intervention examples**
   - Show 2–3 “vague exposure → concrete intervention” rewrites (e.g., “obesity” → bariatric surgery vs calorie restriction; “SES” → cash transfer; “exercise” → prescribed minutes/week).
   - Explicitly connect to “multiple versions of treatment” and consistency.
3. **Simulation**
   - Data-generating mechanism with confounder \(L\):  
     - Generate \(L\sim Bernoulli(p)\)  
     - Define potential outcomes \(Y^{a}\) via logistic (or linear probability) model depending on \(a\) and \(L\).  
     - Scenario A (RCT): \(A\perp L\). Scenario B (confounded): \(Pr(A=1|L)\) depends on \(L\).
   - Compute:
     - True causal effect from \(\bar Y^{1}, \bar Y^{0}\) (generated from potential outcomes).
     - Observed association from \(Pr(Y=1|A=1) - Pr(Y=1|A=0)\) (or RR).
   - Visualization: show association vs causal effect under both scenarios; optional slider for strength of confounding (via \(Pr(A=1|L)\) or effect of \(L\) on Y).
4. **Reflection key points**
   - Association ≠ causation when \(A\) is not exchangeable (common causes).
   - Individual causal effects are not identified because only one potential outcome is observed per person.

---

## Lecture 3 — Causal effects in observational studies (identifiability and assumptions)
### Assets to generate (slides + notebook + homework)
- Slides: `slides/L03_observational_assumptions.md` (outline + speaker notes) → (optional) export to PPTX/Google Slides
- Notebook (student): `notebooks/L03_observational_assumptions_student.ipynb`
- Notebook (solution, instructor): `instructor_solutions/L03_observational_assumptions_solution.ipynb`
- Homework prompt: `assignments/HW03_observational_assumptions.md`
- Homework solutions: `instructor_solutions/HW03_observational_assumptions_solution.md`
- Optional concept check: `quizzes/Q03_observational_assumptions_concept_check.md`


### Learning goals
- Conceptualize observational studies as “imperfect randomized experiments”.
- State the 3 key identifiability conditions: exchangeability, positivity, well-defined interventions.
- Recognize why conditional exchangeability cannot be tested from observed data alone.

### Required reading
- Hernán & Robins, Chapter 3. https://miguelhernan.org/whatifbook

### Suggested/optional (high-yield classic)
- Hernán & Taubman (well-defined interventions; obesity example).
- Greenland & Robins (identifiability/exchangeability/confounding).

### In-class activity
- Students write a target trial for a common observational question (e.g., statins and mortality).

### Colab notebook idea
**Notebook 03:** “Standardization and IPW in a toy observational study”
- Simulate a confounded dataset with 1–2 covariates.
- Show both estimators recover the same estimand if assumptions hold.

### Homework
1. Define conditional exchangeability in words and in notation.
2. Describe one real-world threat to:
   - exchangeability
   - positivity
   - consistency
3. Coding:
   - Use a simulated observational dataset with L, A, Y.
   - Estimate the marginal causal effect using:
     (i) standardization with stratification (few strata), and
     (ii) IPW.
   - Compare with the true effect from the data-generating mechanism.
4. Write a “limitations” paragraph: which assumption is most fragile and why?

#### Instructor solution sketch (for generating the solution notebook/key)

1. **Target trial answer**
   - Include eligibility, time zero, treatment strategies, follow-up, outcome, estimand, analysis plan (1 short paragraph each).
2. **Threats to assumptions**
   - Exchangeability: unmeasured severity/confounding by indication.
   - Positivity: treatment never used in some subgroup (e.g., contraindication).
   - Consistency: “treatment” has multiple versions (dose/timing/adherence).
3. **Coding solution**
   - Simulate observational data:
     - L affects both A and Y; define true \(E[Y^{1}] - E[Y^{0}]\).
   - Implement:
     - (i) stratified g-computation/standardization (few L strata)
     - (ii) IPW with true/estimated propensity score.
   - Compare estimates to truth; show bias if omitting L.
4. **Limitations paragraph key**
   - Conditional exchangeability is untestable; plausibility depends on measured covariates and subject-matter knowledge.

---

## Lecture 4 — Effect modification and effect-measure modification
### Assets to generate (slides + notebook + homework)
- Slides: `slides/L04_effect_modification.md` (outline + speaker notes) → (optional) export to PPTX/Google Slides
- Notebook (student): `notebooks/L04_effect_modification_student.ipynb`
- Notebook (solution, instructor): `instructor_solutions/L04_effect_modification_solution.ipynb`
- Homework prompt: `assignments/HW04_effect_modification.md`
- Homework solutions: `instructor_solutions/HW04_effect_modification_solution.md`
- Optional concept check: `quizzes/Q04_effect_modification_concept_check.md`


### Learning goals
- Define effect modification (causal effect differs across strata) vs effect-measure modification (depends on scale).
- Compute stratum-specific causal effects and interpret them.
- Discuss pooling vs not pooling; link to transportability.

### Required reading
- Hernán & Robins, Chapter 4. https://miguelhernan.org/whatifbook

### In-class activity
- Provide a 2×2×2 table (A, Y, M). Students compute RD and RR in strata and decide if modification exists on each scale.

### Colab notebook idea
**Notebook 04:** “Scale matters”
- Simulate data where RR differs but RD doesn’t (or vice versa).
- Visualize stratum-specific risks and effect measures.

### Homework
1. Provide an example where there is effect-measure modification on RR but not RD (or the opposite).
2. When is pooling appropriate? Give a principle-based answer (not only p-values).
3. Coding:
   - Simulate data with a true interaction term.
   - Estimate stratum-specific causal effects using standardization within strata.
4. Optional extension: show non-collapsibility of the odds ratio with a simple simulation.

#### Instructor solution sketch (for generating the solution notebook/key)

1. **Compute stratum-specific effects**
   - Risk difference and risk ratio within each level of effect modifier M.
2. **Effect-measure modification**
   - Show that “effect modification” depends on scale:
     - additive: RD differs by M
     - multiplicative: RR differs by M
3. **Interpretation**
   - Clarify difference between effect modification and confounding:
     - modification is about heterogeneity of causal effect
     - confounding is bias due to common causes.
4. **Coding (if included)**
   - Use a simple simulated dataset with known interaction term:
     - e.g., \(logit\,Pr(Y=1)=\beta_0+\beta_A A+\beta_M M+\beta_{AM} A\times M\)
   - Plot stratum-specific risks and effect measures.

---

## Lecture 5 — Causal diagrams (DAGs), d-separation, and collider bias
### Assets to generate (slides + notebook + homework)
- Slides: `slides/L05_dags_dseparation.md` (outline + speaker notes) → (optional) export to PPTX/Google Slides
- Notebook (student): `notebooks/L05_dags_dseparation_student.ipynb`
- Notebook (solution, instructor): `instructor_solutions/L05_dags_dseparation_solution.ipynb`
- Homework prompt: `assignments/HW05_dags_dseparation.md`
- Homework solutions: `instructor_solutions/HW05_dags_dseparation_solution.md`
- Optional concept check: `quizzes/Q05_dags_dseparation_concept_check.md`


### Learning goals
- Read a DAG and identify:
  - causal paths, backdoor paths
  - colliders and descendants of colliders
- Use d-separation to decide which paths are open/blocked under conditioning.
- Translate “adjustment set” logic into an analysis plan.

### Required reading
- Hernán & Robins, Chapter 6 (DAGs). https://miguelhernan.org/whatifbook

### Suggested/optional classic
- Pearl (1995) “Causal diagrams for empirical research” (original DAG formalism).
  - Oxford page (abstract): https://academic.oup.com/biomet/article-abstract/82/4/669/251647
- Robins (2001) on background knowledge in etiologic inference.

### In-class activity
- “Adjustment set speed dating”: 6 DAGs on slides; groups propose adjustment sets and justify.

### Colab notebook idea
**Notebook 05:** “DAGs as objects”
- Use `networkx` + `graphviz` to draw DAGs.
- Manually code simple d-separation checks (or use a lightweight library if you prefer).
- Demonstrate collider bias by simulation and by DAG reasoning.

### Homework
1. For each provided DAG (you give 5–6), answer:
   - Is adjustment for L needed to identify effect of A on Y?
   - Is adjustment for collider C harmful?
2. Coding (simulation):
   - Create a collider structure A → C ← U → Y and show how conditioning on C induces association between A and Y.
3. “Design thinking”: give one example of how study design can reduce collider/selection bias.

#### Instructor solution sketch (for generating the solution notebook/key)

1. **DAG tasks**
   - Provide correct d-separation answers for the in-class questions (open/blocked paths).
   - For each DAG, list:
     - backdoor paths from A to Y
     - minimal sufficient adjustment set(s).
2. **Collider bias demonstration**
   - Simulate A → S ← Y (or A ← U → Y with selection S depending on A and Y).
   - Show that conditioning on S (or selecting S=1) induces association between A and Y even when no causal effect.
3. **Visualization**
   - Draw DAG using `networkx` + `matplotlib` (or `graphviz`).
   - Plot association (risk difference) overall vs within S=1.
4. **Key narrative**
   - Three structural sources of association: causal effect, common causes, conditioning on common effects (colliders).

---

## Lecture 6 — Confounding: definition, confounders, and adjustment strategies
### Assets to generate (slides + notebook + homework)
- Slides: `slides/L06_confounding.md` (outline + speaker notes) → (optional) export to PPTX/Google Slides
- Notebook (student): `notebooks/L06_confounding_student.ipynb`
- Notebook (solution, instructor): `instructor_solutions/L06_confounding_solution.ipynb`
- Homework prompt: `assignments/HW06_confounding.md`
- Homework solutions: `instructor_solutions/HW06_confounding_solution.md`
- Optional concept check: `quizzes/Q06_confounding_concept_check.md`


### Learning goals
- Define confounding as lack of exchangeability due to common causes.
- Compare definitions of a “confounder” and why purely statistical criteria are insufficient.
- Connect confounding control to DAG-based adjustment sets.

### Required reading
- Hernán & Robins, *What If*, Chapter 7 (Confounding). https://miguelhernan.org/whatifbook

### In-class activity
- Students propose a DAG for a clinical question (e.g., ICU sedative choice → delirium).
- Discuss which variables are confounders vs mediators vs colliders.

### Colab notebook idea
**Notebook 06:** “Confounding in code”
- Simulate confounding with multiple L’s.
- Demonstrate:
  - crude association
  - adjusted estimate via standardization (small L)
  - adjusted estimate via IPW (more flexible)

### Homework
1. Provide a short critique of “change-in-estimate >10%” as a confounder rule.
2. From a DAG, label variables as:
   - confounder
   - mediator
   - collider
   - proxy/surrogate confounder
3. Coding:
   - Simulate a setting with a mediator and show why adjusting for mediator changes the estimand.
4. Write 5 sentences: what does “no unmeasured confounding” mean in practice?

#### Instructor solution sketch (for generating the solution notebook/key)

1. **Definitions**
   - Confounding as lack of exchangeability due to common causes (backdoor paths).
   - Distinguish “confounding” vs “confounder”; explain why some confounder definitions fail (e.g., change-in-estimate with non-collapsible OR).
2. **Backdoor criterion workflow**
   - From a DAG: identify open backdoor paths; choose a set that blocks them without conditioning on colliders/mediators.
3. **Coding**
   - Simulate A ← U → Y with measured L as proxy/partial confounder:
     - Show adjustment works when L is a true common cause.
   - Compute crude vs adjusted estimands (standardization or regression).
4. **Instructor key points**
   - Adjustment target: exchangeability, not “statistical significance”.
   - Overadjustment and collider adjustment can introduce bias.

---

## Lecture 7 — Selection bias (structure and adjustment)
### Assets to generate (slides + notebook + homework)
- Slides: `slides/L07_selection_bias.md` (outline + speaker notes) → (optional) export to PPTX/Google Slides
- Notebook (student): `notebooks/L07_selection_bias_student.ipynb`
- Notebook (solution, instructor): `instructor_solutions/L07_selection_bias_solution.ipynb`
- Homework prompt: `assignments/HW07_selection_bias.md`
- Homework solutions: `instructor_solutions/HW07_selection_bias_solution.md`
- Optional concept check: `quizzes/Q07_selection_bias_concept_check.md`


### Learning goals
- Recognize selection bias as conditioning on a collider (selection variable).
- Identify common epidemiologic selection mechanisms:
  - Berkson’s bias, incidence-prevalence bias, differential loss to follow-up.
- Use IP weighting (or standardization) to adjust for censoring/selection under assumptions.

### Required reading
- Hernán & Robins, Chapter 8. https://miguelhernan.org/whatifbook

### Suggested/optional (high-yield)
- Greenland (2003) on collider-stratification bias.

### In-class activity
- “Loss to follow-up DAG”: build a DAG with censoring C and discuss when weighting works.

### Colab notebook idea
**Notebook 07:** “IP weights for censoring”
- Create missingness depending on (A, L).
- Estimate censoring weights W* and apply to recover the target estimand.

### Homework
1. Give a DAG where selection bias occurs and explain in 3–4 sentences.
2. Coding:
   - Simulate data with censoring C that depends on A and L.
   - Estimate censoring weights and compute weighted effect estimate.
3. Diagnostics:
   - Plot weight distribution; discuss positivity (extreme weights).
4. Short essay: difference between confounding weights and censoring weights; when to multiply them.

#### Instructor solution sketch (for generating the solution notebook/key)

1. **Selection mechanisms**
   - Distinguish:
     - selection on exposure and outcome (collider) vs selection on confounder.
2. **Simulation**
   - Generate A, Y with no causal effect (or known effect) and define selection indicator S influenced by both A and Y.
   - Show:
     - unbiased estimate in full data
     - biased estimate when restricting to S=1.
3. **Fix (teaching-level)**
   - Demonstrate inverse probability of selection weighting (IPSW) when selection model is known/estimated:
     - \(w_i = 1/Pr(S=1|A,L)\) (or stabilized).
4. **Visualization**
   - Compare estimates and weight distributions; show how extreme weights relate to near-positivity problems in selection.

---

## Lecture 8 — Why model? (estimators, models, bias-variance tradeoff)
### Assets to generate (slides + notebook + homework)
- Slides: `slides/L08_estimators_models.md` (outline + speaker notes) → (optional) export to PPTX/Google Slides
- Notebook (student): `notebooks/L08_estimators_models_student.ipynb`
- Notebook (solution, instructor): `instructor_solutions/L08_estimators_models_solution.ipynb`
- Homework prompt: `assignments/HW08_estimators_models.md`
- Homework solutions: `instructor_solutions/HW08_estimators_models_solution.md`
- Optional concept check: `quizzes/Q08_estimators_models_concept_check.md`


### Learning goals
- Define estimand, estimator, estimate.
- Understand why we need models for high-dimensional covariates.
- Introduce outcome regression (linear/logistic) and interpretation of parameters.

### Required reading
- Hernán & Robins, Chapter 11. https://miguelhernan.org/whatifbook

### In-class activity
- Walk through a simple logistic regression and ask: “Which estimand does this directly estimate?”

### Colab notebook idea
**Notebook 08:** “Outcome regression for causal inference”
- Use NHEFS-like variables (or a simplified dataset):
  - Fit outcome model E[Y|A,L]
  - Predict Y under A=1 and A=0 for everyone
  - Average predictions → standardized mean/risk

### Homework
1. Explain why “E[Y|A=1] − E[Y|A=0]” is generally not causal in observational data.
2. Coding:
   - Fit two outcome models:
     (i) correct specification, (ii) misspecified.
   - Compare causal estimates under both; discuss bias-variance tradeoff.
3. Optional: use cross-validation to compare predictive performance vs causal target (discussion).

#### Instructor solution sketch (for generating the solution notebook/key)

1. **Estimator vs model**
   - Clarify: g-formula and IPW are estimators; regression/PS are models used to estimate nuisance components.
2. **Bias–variance demonstration**
   - Simulate nonlinear true outcome model.
   - Fit:
     - (i) misspecified linear/logistic model
     - (ii) flexible model (splines or tree-based) as optional extension
   - Compare out-of-sample error and causal estimand bias.
3. **Key takeaways**
   - More flexibility can reduce bias but may increase variance; diagnostics and sensitivity are required.

---

## Lecture 9 — Standardization and the (parametric) g-formula
### Assets to generate (slides + notebook + homework)
- Slides: `slides/L09_gformula_standardization.md` (outline + speaker notes) → (optional) export to PPTX/Google Slides
- Notebook (student): `notebooks/L09_gformula_standardization_student.ipynb`
- Notebook (solution, instructor): `instructor_solutions/L09_gformula_standardization_solution.ipynb`
- Homework prompt: `assignments/HW09_gformula_standardization.md`
- Homework solutions: `instructor_solutions/HW09_gformula_standardization_solution.md`
- Optional concept check: `quizzes/Q09_gformula_standardization_concept_check.md`


> **Mapping note:** In your provided slide deck, “Standardization” appears as **Lecture 10**. Keep the numbering consistent with your semester schedule if needed.

### Learning goals
- Compute marginal causal effects via:
  - nonparametric standardization (few covariates)
  - parametric g-formula (many covariates)
- Use bootstrap to build confidence intervals.
- Understand what “model misspecification” means for causal estimands.

### Required reading
- Hernán & Robins, standardization/g-formula sections (and/or the aligned chapter you already use).

### In-class activity
- Derive the g-formula for a point exposure using law of total probability.

### Colab notebook idea
**Notebook 09:** “Standardization end-to-end”
- Use NHEFS (smoking cessation) style dataset:
  - outcome: weight gain (continuous) and death (binary)
  - estimate ACE using:
    - crude
    - age-standardization (few strata)
    - parametric g-formula with multiple covariates
  - bootstrap CI

### Homework
1. Derive the standardization formula for Pr(Y^a=1) under conditional exchangeability.
2. Coding:
   - Implement g-formula for both a continuous and binary outcome.
   - Bootstrap 500 replicates for understood CI method.
3. Diagnostics:
   - Check positivity by plotting propensity score or treatment probability by covariates (simple bins).
4. Interpretation:
   - Write a short paragraph explaining the meaning of the standardized estimate.

#### Instructor solution sketch (for generating the solution notebook/key)

1. **Parametric g-formula implementation**
   - Fit outcome model: \(E[Y|A,L]\) (e.g., logistic for binary Y, linear for continuous).
   - Predict counterfactual outcomes:
     - set A=1 for all, predict \(\hat Y^{1}_i\); average → \(\widehat{E}[Y^{1}]\)
     - set A=0 for all, predict \(\hat Y^{0}_i\); average → \(\widehat{E}[Y^{0}]\)
2. **Effect measure**
   - Compute RD/RR (or mean difference) from the two standardized predictions.
3. **Uncertainty**
   - Bootstrap the full procedure (including refitting models).
4. **Compare to IPW**
   - Implement IPW estimate on same dataset; discuss differences (model dependence vs weight instability).

---

## Lecture 10 — Instrumental variables (IV): when exchangeability is not plausible

### Why this lecture matters (one sentence)
IV methods are the main “escape hatch” when **treatment–outcome exchangeability is not plausible** because of *unmeasured confounding*, but they trade that assumption for **instrumental conditions** that are also largely unverifiable.

### Assets to generate (slides + notebook + homework)
- Slides: `slides/L10_instrumental_variables.md` (outline + speaker notes) → (optional) export to PPTX/Google Slides
- Notebook (student): `notebooks/L10_instrumental_variables_student.ipynb`
- Notebook (solution, instructor): `instructor_solutions/L10_instrumental_variables_solution.ipynb`
- Homework prompt: `assignments/HW10_instrumental_variables.md`
- Homework solutions: `instructor_solutions/HW10_instrumental_variables_solution.md`
- Optional concept check: `quizzes/Q10_instrumental_variables_concept_check.md`

### Learning goals
By the end, students should be able to:
1. **Define an IV** and explain why it can identify a causal effect even with unmeasured exposure–outcome confounding.
2. State and interpret the **three instrumental conditions** using a DAG:
   - **Relevance:** Z affects A.
   - **Exclusion restriction:** Z affects Y only through A (no direct Z→Y).
   - **Independence:** Z and Y do not share common causes (or other sources of lack of exchangeability).
3. Explain why conditions (2) and (3) are **not testable** from observed data, and how we can sometimes partially *falsify* them.
4. Compute:
   - **Wald estimator** (binary Z, binary A; or binary Z with continuous Y)
   - **2SLS** (continuous outcomes; optionally A binary as a linear probability model “first stage”)
5. Explain **LATE/CACE interpretation** under **monotonicity**, and why we cannot identify who the compliers are.
6. Recognize **weak instruments** and explain why they amplify bias and increase variance.
7. Explain why IV can still be biased by **selection/censoring**, and how **inverse probability of censoring weights (IPCW)** can be combined with IV.

### Minimal required reading (choose one)
- Hernán & Robins, *What If* — short recap of IV intuition (if you want to keep reading minimal).
- A short epidemiology-friendly IV primer (you can provide as a 2–3 page handout).

### Core lecture outline (teaching flow)
1. **Motivation:** what breaks when conditional exchangeability fails
   - Reminder: regression / g-formula / IPW all rely on “no unmeasured confounding”.
2. **IV definition + DAG**
   - Z influences A; A influences Y; U confounds A–Y; Z independent of U; no direct Z→Y.
3. **IV in randomized trials with noncompliance**
   - Randomization as an instrument; “always-takers / never-takers / compliers / defiers”.
   - Monotonicity = no defiers; interpretation becomes LATE among compliers.
4. **IV in observational studies**
   - Examples of proposed instruments (keep practical and clinical):
     - provider/physician preference (proxied by prior prescribing)
     - access (distance, calendar period)
     - price/cost (e.g., cigarette price in NHEFS-style examples)
     - Mendelian randomization (conceptual only; do not expand into genetics methods)
5. **Estimation**
   - Wald estimator (binary Z): (E[Y|Z=1]−E[Y|Z=0]) / (E[A|Z=1]−E[A|Z=0])
   - 2SLS for continuous Y:
     - Stage 1: A ~ Z (+ baseline covariates)
     - Stage 2: Y ~ Â (+ baseline covariates)
   - Emphasize what the estimate means (ATE vs LATE).
6. **Limitations + diagnostics**
   - Why exclusion and independence are hard.
   - **Weak instrument warning:** small first-stage effect → unstable estimate; bias amplification.
   - “Falsification” mindset: tests can reject assumptions but cannot prove them.
7. **IV + selection bias (advanced but high-yield)**
   - If follow-up depends on A/L (or other variables), IV can induce Z–Y non-exchangeability.
   - Combine IV with **IPCW** (typically nonstabilized for censoring adjustment when A→C exists).

### Colab notebook plan (Python-first, but include R/SAS notes)
**Notebook 10A (simulation): “IV rescues unmeasured confounding (sometimes)”**
- Simulate U that confounds A→Y.
- Create Z that affects A but not Y directly.
- Compare:
  - naive regression
  - g-formula/IPW (still biased because U unmeasured)
  - Wald + 2SLS (approximately recovers true effect when IV assumptions hold)
- Add a “weak instrument” slider: shrink Z→A and show instability.

**Notebook 10B (applied): “Adjusted 2SLS with baseline covariates”**
- Use a public dataset (NHEFS-style or synthetic) so it runs instantly.
- Show:
  - first-stage regression + F-statistic
  - second-stage estimate + robust SE
  - sensitivity: instrument strength, alternate covariate sets

**Implementation notes**
- Python: `linearmodels` (IV2SLS) or `statsmodels.sandbox.regression.gmm.IV2SLS` if needed.
- R (optional): `AER::ivreg()` demo only; SAS (optional): `PROC SYSLIN` (brief pointer).

### Homework (team-based)
1. **Conceptual (DAG + assumptions)**
   - Draw a DAG for an IV setting and list which arrows/paths correspond to each instrumental condition.
2. **Computation**
   - Compute the Wald estimator by hand on a toy 2×2 table (Z binary, A binary, Y continuous or binary).
3. **Coding (Python preferred; R/SAS allowed)**
   - Run an adjusted 2SLS, report:
     - first-stage estimate and a strength diagnostic (F-stat or partial R²)
     - second-stage estimate + robust SE
4. **Critical thinking**
   - Give one plausible exclusion restriction violation in a clinical setting and explain how it would bias results.
5. **Advanced (optional)**
   - Demonstrate how censoring related to treatment could bias IV; apply IPCW and compare.

#### Instructor solution sketch (for generating the solution notebook/key)
- Provide (i) a clear assumptions checklist, (ii) worked Wald example, (iii) 2SLS code + outputs,
  and (iv) one falsification-style check plus a weak-IV demonstration.
---

## Lecture 11 — IP weighting for confounding (propensity scores) and diagnostics
### Assets to generate (slides + notebook + homework)
- Slides: `slides/L11_ipw_propensity.md` (outline + speaker notes) → (optional) export to PPTX/Google Slides
- Notebook (student): `notebooks/L11_ipw_propensity_student.ipynb`
- Notebook (solution, instructor): `instructor_solutions/L11_ipw_propensity_solution.ipynb`
- Homework prompt: `assignments/HW11_ipw_propensity.md`
- Homework solutions: `instructor_solutions/HW11_ipw_propensity_solution.md`
- Optional concept check: `quizzes/Q11_ipw_propensity_concept_check.md`


### Learning goals
- Estimate causal effects by weighting individuals by inverse probability of treatment.
- Understand stabilized vs non-stabilized weights and why stabilization helps.
- Diagnose positivity and weight instability; basic remedies (truncation, alternative modeling).
- Compare “modeling f[A|L]” (IPW) vs “modeling f[Y|A,L]” (g-formula).

### Required reading
- Hernán & Robins, Chapter 12 (IPW/MSMs intro). https://miguelhernan.org/whatifbook

### In-class activity
- Compute weights by hand for a 2-strata example; interpret pseudo-population.

### Colab notebook idea
**Notebook 11:** “IPW pipeline”
- Fit propensity model Pr(A=1|L).
- Compute stabilized weights.
- Check covariate balance pre/post weighting (SMD plots).
- Estimate weighted mean difference / weighted risk ratio.

### Homework
1. Define stabilized weight and explain (in words) what it does.
2. Coding:
   - Estimate IPW for smoking cessation → weight gain.
   - Compare to g-formula estimate from Lecture 9.
3. Diagnostics:
   - Show distribution of weights + report % truncated at 1st/99th percentile (if you choose truncation).
4. Write-up:
   - Discuss which method you trust more for this dataset and why.

#### Instructor solution sketch (for generating the solution notebook/key)

1. **Propensity score model**
   - Fit \(\hat e(L)=Pr(A=1|L)\) via logistic regression (baseline).
2. **Weights**
   - Unstabilized: \(w= A/\hat e(L) + (1-A)/(1-\hat e(L))\)
   - Stabilized: \(sw= Pr(A)/\hat e(L)\) for treated and \(Pr(1-A)/(1-\hat e(L))\) for untreated.
3. **Diagnostics**
   - Positivity: PS overlap plot.
   - Weight distribution: histogram; identify extreme weights; apply truncation (e.g., 1st/99th percentile).
   - Balance: standardized mean differences before/after weighting.
4. **Causal effect**
   - Weighted outcome mean difference (or weighted regression).
5. **Narrative**
   - IPW targets marginal estimand; main failure modes are positivity and PS misspecification.

---

## Lecture 12 — Capstone: marginal structural models, target trial emulation, and time-to-event outcomes
### Assets to generate (slides + notebook + homework)
- Slides: `slides/L12_msm_time_varying.md` (outline + speaker notes) → (optional) export to PPTX/Google Slides
- Notebook (student): `notebooks/L12_msm_time_varying_student.ipynb`
- Notebook (solution, instructor): `instructor_solutions/L12_msm_time_varying_solution.ipynb`
- Homework prompt: `assignments/HW12_msm_time_varying.md`
- Homework solutions: `instructor_solutions/HW12_msm_time_varying_solution.md`
- Optional concept check: `quizzes/Q12_msm_time_varying_concept_check.md`


### Learning goals
- Explain MSMs (structural + marginal): why they are useful for time-varying confounding under sustained strategies.
- Fit a simple MSM and interpret causal parameters; combine treatment weights with censoring/selection weights.
- Specify a target trial protocol (eligibility, strategies, time zero, follow-up, outcome, estimand, analysis plan).
- Identify and explain immortal time bias and other time-alignment pitfalls; show how target trial thinking prevents them.
- Define and estimate causal effects for time-to-event outcomes using a discrete-time hazard approach and/or risk by time t.

### Additional capstone modules (integrate into this same 120-min session)

**Module A — Target trial emulation (protocol + pitfalls)**
- Translate an observational question into a **target trial** specification:
  1. eligibility criteria
  2. treatment strategies (A=1 vs A=0) with a clear time zero
  3. hypothetical assignment mechanism (randomization conceptually)
  4. follow-up period and censoring rules
  5. outcome definition
  6. causal contrast/estimand (ITT vs per-protocol; choose one and justify)
  7. analysis plan aligned with assumptions
- Diagnose and prevent common design/analysis errors:
  - immortal time bias (misaligned time zero)
  - selection/censoring tied to treatment initiation
  - misclassification of baseline vs post-baseline covariates

**Module B — Causal survival analysis (time-to-event outcomes)**
- Define causal questions for time-to-event endpoints (time zero, follow-up, censoring).
- Teach **one simple, robust approach**: discrete-time hazards (person-period data) and estimation of:
  - risk by time t (e.g., 30-day risk), and/or
  - survival curves under strategies via g-formula prediction and/or IPW.
- (Optional) IPCW for informative censoring and comparison to naive analysis.

**Instructor guidance (scope control)**
- Keep methods minimal and aligned with prior lectures: g-formula + IPW/weights + clear identification assumptions.
- Mention competing risks only briefly (definition + why it complicates interpretation), without adding additional estimators.

### Required reading
- Continue Hernán & Robins, Chapter 12 + MSM sections. https://miguelhernan.org/whatifbook

### Colab notebook idea
**Notebook 12:** “MSM + selection weights”
- Use NHEFS style data with censoring indicator C (missing outcome).
- Fit:
  - MSM for mean difference
  - MSM with baseline effect modifier (e.g., age)
- Combine stabilized treatment and censoring weights.

### Homework (required; feeds the final project)
**Team-based unless noted.** Submit: (i) a target-trial protocol (1–2 pages), (ii) a notebook for the survival lab, and (iii) a brief write-up.

#### Part A — Target trial protocol (1–2 pages; “protocol v2”)
- Use **your semester project question** (preferably MIMIC-IV). If MIMIC access is still pending, write the protocol using the provided demo/synthetic data and state how it will map to MIMIC variables later.
- Use the template below (copy/paste headings; keep it concise):
  1. **Title + causal question** (population, strategies, outcome, horizon)
  2. **Eligibility criteria** (inclusion/exclusion)
  3. **Treatment strategies** (define interventions; include a grace period if needed)
  4. **Treatment assignment in the emulation** (how you will emulate randomization; confounders set)
  5. **Time zero + follow-up** (avoid immortal time; define censoring)
  6. **Outcome definition** (and competing risks if relevant)
  7. **Estimand(s)** (e.g., risk difference at 28 days; target population)
  8. **Causal model + assumptions** (DAG; where exchangeability/positivity/consistency might fail)
  9. **Primary analysis plan** (estimator + diagnostics: overlap/weights/balance; model checks)
  10. **Sensitivity/robustness** (≥2 items: alternative windows, trimming, negative control discussion, etc.)

**Deliverable:** `assignments/HW12_target_trial_protocol.md` (or PDF export) + DAG figure.

#### Part B — Discrete-time survival lab (coding + figures)
Using `data/synthetic_time_to_event.csv` (provided), implement:
1. **Reshape** to person–period (“long”) format on a discrete time grid.
2. **Fit pooled logistic hazard models** (unadjusted and adjusted; optional weighted).
3. **Estimate and plot**:
   - Survival curves under two strategies (e.g., treat vs not treat) using standardization (or weighting).
   - Risk by time *t* (choose *t* = end of follow-up) with uncertainty via bootstrap (team-level).
4. **Selection/censoring**:
   - Add censoring weights (or use provided censoring indicator) and compare results.

**Deliverables:** `notebooks/L12_survival_student.ipynb` + `assignments/HW12_survival_writeup.md` (≤1 page; 2–3 plots + interpretation).

#### Part C — MSM extension (optional but recommended)
Repeat Part B with time-varying confounding using the lecture’s longitudinal synthetic dataset:
- compute stabilized treatment (and censoring) weights
- fit a simple MSM and compare against a naïve model

#### Reflection (individual; 5–8 sentences)
State the **single most plausible remaining bias** in your analysis and why (confounding, measurement, selection, time alignment, etc.).

#### Instructor solution sketch (for generating the solution notebook/key)
A. **Target trial protocol key**
- Provide a “minimal acceptable” protocol example and a checklist keyed to the template headings.
- Include common pitfalls: immortal time, post-baseline covariate adjustment, ill-defined strategies, and positivity failures.

B. **Discrete-time survival solution**
- Build person–period data; fit pooled logistic hazard; compute \\(\hat S(t)\\) under strategies via standardization.
- Bootstrap at the individual level (cluster bootstrap) for risk by time *t*; plot survival/cumulative incidence curves.
- Add censoring weights when censoring depends on past history.

C. **MSM time-varying solution**
- Simulate longitudinal data with \\(L_t\\) affected by past \\(A\\) and affecting future \\(A\\) and \\(Y\\).
- Stabilized treatment weights:
  \\[
    sw_i = \prod_t \frac{Pr(A_t\mid \bar A_{t-1})}{Pr(A_t\mid \bar A_{t-1}, \bar L_t)}
  \\]
- Add censoring weights if dropout depends on past history; multiply weights.
- Fit weighted pooled logistic (or weighted regression) for the outcome on treatment history; include effect modification if asked.
- Diagnostics: weight mean near 1; check tails; truncation; positivity checks.


## A. Project milestones (recommended)
1. **Milestone 0 (Week 2–3):** MIMIC access started + short tutorial notebook run.
2. **Proposal (Week 4):** 1–2 pages: target trial protocol (v1) + DAG + feasibility (tables/variables).
3. **Analysis plan (Week 6):** estimand + identification + estimator + diagnostics plan.
4. **Midterm check-in (Week 8):** preliminary cohort + baseline table + positivity/overlap check.
5. **Capstone deliverable (Week 12):** updated target trial protocol (v2) + discrete-time survival analysis appendix (even if your primary outcome is not time-to-event).
6. **Final report (end):** 6–10 pages + appendix; code + reproducible pipeline.

## B. Project evaluation rubric (simple)
- Target trial clarity (20%)
- DAG and assumptions (20%)
- Correct implementation of at least one estimator (25%)
- Diagnostics (positivity, weights, balance, sensitivity discussion) (20%)
- Reproducibility + writing quality (15%)

## C. MIMIC-friendly project ideas (point-treatment versions)
Pick questions that can be treated as **baseline/early exposure** to avoid time-varying complexity.

1. **Early vasopressor use** (A: vasopressor within first X hours) → mortality or shock reversal
2. **Early antibiotics** (A: antibiotics within first X hours) → mortality / ICU length of stay
3. **High vs low tidal volume strategy** (A: average tidal volume category in first 24h) → mortality
4. **Sedation strategy** (A: benzodiazepine vs propofol early) → delirium proxy / ventilation duration
5. **Transfusion threshold** (A: transfusion within first 24h above/below Hb threshold) → outcomes

For each topic:
- define time zero (ICU admission or intubation)
- define exposure window (first 6–24h)
- define outcome window (in-hospital or 28-day)
- define confounders measured before exposure window

## D. Minimum methodological requirement
Each team must implement at least **two** of:
- g-formula/standardization (parametric)
- IPW with MSM
- (Optional) IV if a plausible instrument exists (rare in ICU; be cautious)

## E. Required deliverables (GitHub structure)
- `/project/proposal.md`
- `/project/analysis_plan.md`
- `/project/report.md` (or PDF)
- `/project/notebooks/` (clean, runnable)
- `/project/src/` (helper functions)
- `/project/sql/` (cohort extraction queries)
- `/project/results/` (tables/figures; no row-level data)

---

# 6) High-yield “improvements” that add learning without adding confusion

1. **One running example across lectures.**  
   Keep the NHEFS smoking cessation example as the anchor for Lectures 8–12, so students can compare methods fairly.
2. **Target trial in every assignment.**  
   Forces clear thinking and prevents “model-first” analysis.
3. **Diagnostic culture.**  
   For every causal estimate, require:
   - positivity check (treatment probability overlap)
   - weight distribution (for IPW)
   - balance check (SMD before/after weighting)
4. **Small simulation before real data.**  
   A 15-minute simulation clarifies why assumptions matter.
5. **“Assumptions ledger” slide.**  
   End each lecture with a checklist: identification assumptions + estimation assumptions (modeling).
6. **Rubric for causal language.**  
   Students must write: “Under assumptions X, Y, Z, we estimate …” (no casual causal claims).

---

## 7) Optional recitations (if you have time)
- Recitation A: “SQL + cohort building in MIMIC (safe + reproducible)”
- Recitation B: “Bootstrap, robust SE, and reporting uncertainty”
- Recitation C: “GitHub workflow: issues, PRs, code review in teams”

---

## 8) Appendix: ready-to-copy homework question bank (extra)

If you need more items quickly, you can reuse these across lectures:

- Define the estimand and specify the target population.
- Identify which variables are pre-treatment vs post-treatment.
- Draw a DAG and propose a minimal adjustment set.
- Identify potential positivity violations and propose fixes.
- Compare two estimators (g-formula vs IPW) and explain differences.
- Write a limitations paragraph with at least 3 plausible biases.

---



# 9) Copy/paste instruction packs for external AIs (Cursor, NotebookLM)

This section is designed so you can **paste** it directly into an AI tool and get consistent outputs that match the course plan.

---

## 9.1 Cursor instruction pack (generate the full teaching repository)

### What Cursor should produce (definition of done)
A GitHub repository that includes:
1. **Runnable Colab notebooks** for every lecture (student version) + instructor solutions (kept private).
2. A small **Python package** (`src/`) with reusable causal utilities (standardization, IPW, balance, bootstrapping, plotting).
3. **Assignment prompts** + **solution keys** (conceptual + code pointers).
4. A top-level `README.md` with:
   - course overview
   - how to run notebooks locally and in Colab
   - an index table listing every notebook with an **Open-in-Colab link**.
5. CI/linting so the repo stays clean (pre-commit + GitHub Actions).
6. **No row-level MIMIC data** in the repo (only synthetic and/or NHEFS).

### Repository blueprint (required structure)
Use this structure exactly (you can add more files, but keep these paths stable):

```
phs564-causal-inference/
  README.md
  LICENSE
  CITATION.cff
  pyproject.toml
  requirements.txt
  environment.yml              # optional
  .gitignore
  .pre-commit-config.yaml
  .github/workflows/ci.yml

  notebooks/
    L01_..._student.ipynb
    ...
    L12_..._student.ipynb

  instructor_solutions/        # keep private (private repo or private branch)
    L01_..._solution.ipynb
    ...
    L12_..._solution.ipynb
    HW01_..._solution.md
    ...
    HW12_..._solution.md

  assignments/
    HW01_...md
    ...
    HW12_...md

  quizzes/                     # optional but recommended
    Q01_...md
    ...
    Q12_...md

  slides/                      # NotebookLM outputs can be stored here too
    L01_...md
    ...
    L12_...md

  src/phs564_ci/
    __init__.py
    datasets/
      __init__.py
      nhefs.py                 # loader + brief documentation
      synthetic.py             # generators used across lectures
    estimators/
      __init__.py
      standardization.py
      ipw.py
      iv.py                    # for Lecture 10 (simple 2SLS/Wald)
      msm.py                   # for Lecture 12 (teaching-level)
    diagnostics/
      __init__.py
      positivity.py
      balance.py
      weights.py
    plotting/
      __init__.py
      causal_plots.py          # PS overlap, weights, standardized risk plots
      dag_plots.py             # DAG drawing helper
    utils/
      __init__.py
      bootstrap.py
      metrics.py
      typing.py

  sql/
    mimic/
      README.md                # “how to run SQL locally” + notes on not sharing data
      cohort_template.sql
      example_sepsis_cohort.sql
      example_statins_cohort.sql

  scripts/
    make_colab_index.py        # auto-generates notebook index + Colab links
    smoke_test_notebooks.py    # optional: run notebooks headless
```

### Coding standards (must enforce)
- Use **type hints**, docstrings, and clear variable names.
- Prefer `numpy`, `pandas`, `statsmodels`, `scikit-learn`, `matplotlib`, `scipy`.
- Keep causal estimators transparent (avoid “black box” ML unless explicitly requested).
- Use deterministic seeds (`np.random.default_rng(2025)`).
- Keep notebooks **teaching-first**:
  - brief markdown explanation
  - small functions imported from `src/`
  - plots with labeled axes and captions
  - 1–2 “stop and think” questions per notebook

### Colab requirements (critical)
- Every notebook must run in Colab from a fresh runtime.
- If extra packages are needed, install them in the first cell with:
  - `pip install -q <package>`
- Include an “Open in Colab” badge at the top of each notebook (in markdown).

Badge template:
```md
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
  https://colab.research.google.com/github/<ORG>/<REPO>/blob/main/notebooks/<NOTEBOOK_NAME>.ipynb
)
```

### Data governance requirements (MIMIC)
- Do NOT write code that prints or exports patient-level rows as examples.
- Any cohort extraction must be expressed as **SQL templates** + configuration instructions.
- The repo may contain:
  - SQL queries
  - schemas/variable dictionaries
  - aggregated results (tables/figures)
  - synthetic demo datasets that mimic the MIMIC structure
- The repo must NOT contain:
  - row-level MIMIC extracts
  - cached query outputs
  - “sample patients” or screenshots of patient-level records

### Student vs instructor materials (solution handling)
- Generate **two versions** of each lecture notebook:
  - `notebooks/*_student.ipynb`: contains TODO cells, questions, partial code.
  - `instructor_solutions/*_solution.ipynb`: complete working notebook with answers.
- Keep `instructor_solutions/` in a **private repo or private branch**.
- In the public/student repo, include only the student notebooks and assignment prompts.

### What Cursor should implement per lecture
For each lecture, implement exactly what is described in this plan:
- Use the “Colab notebook idea” section for each lecture as the notebook specification.
- Use the “Homework” and “Instructor solution sketch” sections to generate:
  - `assignments/HWXX_*.md`
  - `instructor_solutions/HWXX_*_solution.md`
- Ensure lecture notebooks share a common style and import shared utilities from `src/`.

### Copy/paste prompt to give Cursor (recommended)
Paste the block below into Cursor and attach this course plan markdown as the source of truth.

```text
You are an expert scientific Python engineer and causal inference TA.

GOAL:
Create a GitHub repository called "phs564-causal-inference" that implements the entire teaching repo described in the attached course plan markdown.

HARD CONSTRAINTS:
- Follow the repository structure exactly (paths and naming).
- Create student notebooks in /notebooks and instructor solutions in /instructor_solutions.
- Every notebook must run in Google Colab from a fresh runtime.
- Do NOT include any row-level MIMIC data or outputs.
- Code must be clean, minimal, and pedagogical: type hints, docstrings, tests where appropriate.

TASKS (in order):
1) Scaffold the repo with README, requirements, pyproject, pre-commit, CI.
2) Implement the src/phs564_ci package (datasets, estimators, diagnostics, plotting, utils).
3) Create all lecture notebooks (L01–L12) as student versions, matching the notebook ideas in the plan.
4) Create the corresponding instructor solution notebooks (L01–L12) that fully solve each notebook.
5) Create HW prompts (HW01–HW12) and solution keys using the plan's homework + instructor sketches.
6) Create an auto-generated index of notebooks with Open-in-Colab links.
7) Run a smoke test to ensure notebooks execute top-to-bottom (at least locally; Colab-compatibility is required).

OUTPUT:
- A complete file tree with all files created.
- A short "how to use" section in README (local vs Colab).
```

---

## 9.2 NotebookLM instruction pack (generate slide decks + speaker notes)

### What NotebookLM should produce
For each lecture (L01–L12):
1. A slide deck outline with **slide-by-slide content** and **speaker notes**.
2. A short “reading guide” (½–1 page) summarizing what students must extract from the chapter.
3. 5–8 concept-check questions (with answers) for quick quizzes.

### Slide style requirements
- 35–45 slides per lecture (up to 120 minutes), **minimal text**, high signal.
- Every lecture must include:
  1. Title + learning objectives
  2. “Where we are in the causal workflow” (1-slide map)
  3. Key definitions/assumptions (clearly labeled)
  4. One worked example (prefer the running example when possible)
  5. One short active-learning task (pair/share)
  6. Summary (3–5 takeaways) + next lecture preview
  7. References/readings (chapter + 1–2 optional)

### Consistency rules
- Keep notation consistent with *What If* and this plan.
- Do not introduce new methods beyond the plan.
- If uncertain, quote/paraphrase from the provided sources rather than inventing.

### Output format (easy to convert to slides)
Write each lecture deck as Markdown like:

```
# L01 — <title>

## Slide 1 — Title
- ...
Speaker notes:
- ...

## Slide 2 — Learning objectives
- ...
Speaker notes:
- ...
...
```

### Copy/paste prompt to give NotebookLM
Upload the following as sources:
- This course plan markdown
- Hernán & Robins *What If* (relevant chapters)
- Any existing departmental slides you want to reuse/adapt

Then paste:

```text
Using ONLY the provided sources, generate a slide deck for Lecture <XX> that follows the course plan.

REQUIREMENTS:
- 25–35 slides.
- Minimal text; clear definitions; labeled assumptions.
- Include one worked example and one active-learning task.
- Provide speaker notes for every slide (1–4 sentences).
- End with a summary slide + reading for next lecture.
- Output as Markdown in the exact "Slide-by-slide" format specified in the plan.
```

---

## 9.3 QA checklist (use after AI-generated materials are produced)

### Content QA (causal correctness)
- Are estimands explicitly defined (ATE vs ATT vs per-protocol)?
- Are assumptions labeled exactly where they are used (consistency/exchangeability/positivity)?
- Do DAG adjustment recommendations avoid conditioning on colliders/mediators?

### Code QA (teaching usability)
- Does each notebook run top-to-bottom in Colab?
- Are figures labeled and interpretable without verbal explanation?
- Are “TODO” tasks unambiguous for students?

### Compliance QA (MIMIC)
- No patient-level data in repo.
- SQL queries + code do not output or “preview” row-level patient data in documentation.

---

*End of course build plan.*