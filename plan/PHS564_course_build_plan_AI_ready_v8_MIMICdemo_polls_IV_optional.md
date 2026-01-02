# PHS564 — Causal Inference Methods in Epidemiologic Research (Draft course build plan)

**Format:** 12 sessions (up to 120 min each) + optional recitations/labs
**Student work mode:** 2-person teams for coding + mini-projects; individual for short concept checks (optional).  
**Peer evaluation:** short confidential peer check-ins (mid-course and end) to support fair team grading; may adjust team scores by ±10% when there is strong evidence of unequal contribution.
**Primary computing track:** Python (Colab). R/SAS allowed for deliverables, but templates/examples will be in Python.  
**Prerequisites (assumed):** graduate-level epidemiology/biostatistics; comfort with regression (linear/logistic); basic probability; ability to read scientific papers. Coding can be beginner–intermediate, but students must be able to run and modify notebooks.
**Pre-course setup (recommended):** complete the short “Python + Jupyter warm-up” notebook (provided) and ensure access to GitHub + Google Colab.
**Primary dataset for teaching:** **MIMIC-IV Demo** (public) + course-provided **analysis-ready extracts** derived from the Demo schema (no credentialing required).
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

### B. Suggested grading (align with your syllabus template)
- **In-class exit polls (end-of-class concept checks): 10%**
  - low-stakes; mostly completion + 1–2 knowledge checks
- **Homework assignments + project milestones (team-based): 65%**
  - short write-up + notebook outputs + required diagnostics figures
- **Final exam (individual, closed-collaboration): 25%**
- **Peer evaluation:** used as a multiplier/flag for team accountability (optional but recommended)

### C. Team policy (2-person teams)
- Teams are formed in **Week 1** to intentionally mix:
  - one member with stronger **clinical context**
  - one member with stronger **programming comfort**
- Stable teams reduce coordination overhead, but **both members must touch the code**.
  - Each homework/project submission must include a **GitHub contributions** link (commits/PRs).
  - A short “contributions” section states what each partner did and what each learned.
- Encourage one “pair-programming” session per assignment (screen-share) to prevent a permanent “coder vs writer” split.


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
  - `/data/` (store **small, analysis-ready MIMIC-IV Demo extracts** and toy simulation data only; **never** store row-level full MIMIC-IV data)
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
- No row-level **full** MIMIC-IV data committed or uploaded; Demo-based extracts may be stored if small, otherwise downloaded via script.
- Solution notebooks stored in a private location (private repo/branch or instructor-only folder ignored by git).

---
## 3) Data plan: MIMIC-IV Demo for everything; full MIMIC-IV optional for the final project

### 3.1 Core teaching dataset (required for everyone)
- **All** in-class examples, notebooks, and homework are built on **MIMIC-IV Demo** (publicly available) plus **course-provided analysis-ready extracts** (CSV/Parquet) derived from Demo.
- Goal: **zero credentialing bottlenecks**. Every student should be able to run Week 1 notebooks on Day 1.
- The repository will include:
  - `data/README.md` documenting each extract (cohort definition, variables, units, missingness, outcome window).
  - `data/download_data.py` that downloads extracts into `data/raw/` (from GitHub Releases or a Penn State-hosted link).
  - `sql/` scripts showing how each extract was produced from the Demo schema (transparency), but **SQL execution is optional** for homework.

### 3.2 Optional: full MIMIC-IV for the final project (student choice)
- Teams may choose to run their capstone target-trial emulation on **full MIMIC-IV** (credentialed PhysioNet access).
- **Deadline:** teams intending to use full MIMIC-IV should complete required credentialing by **Week 4**.
- **Plan B (no penalty):** if a team is not credentialed by Week 4, they complete the final project using **MIMIC-IV Demo** (same protocol + pipeline, smaller N).
- **Governance:** never commit or upload row-level **full** MIMIC-IV data to GitHub/Colab/Canvas. Share **code + SQL + aggregate outputs only**.

### 3.3 What “MIMIC-IV Demo” means operationally
To keep the causal focus (not data plumbing), we treat most analyses as **baseline/early exposure** problems:
- time zero = ICU admission (or first ICU day)
- exposure window = first 6–24h
- follow-up window = 28-day mortality, ICU LOS, ventilation duration, etc.
- confounders = measured before the exposure window

Each lecture’s notebook uses a single extract, e.g.:
- `cohort_L01_antibiotics_28d.parquet`
- `cohort_L08_ps_ipw.parquet`
- `cohort_L10_survival.parquet`
- `cohort_L11_msm_longitudinal.parquet`

These are designed to be small, runnable on Colab, and reproducible from the Demo schema.

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

---

## Lecture 8 — IP weighting for confounding (propensity scores) + diagnostics (MIMIC-IV Demo)
### Assets to generate (slides + notebook + homework + poll)
- Slides: `slides/L08_ipw_propensity.md` → (optional) export to PPTX/Google Slides
- Notebook (student): `notebooks/L08_ipw_propensity_student.ipynb` (**fill-in-the-blanks; pipeline provided**)
- Notebook (solution, instructor): `instructor_solutions/L08_ipw_propensity_solution.ipynb`
- Homework prompt: `assignments/HW08_ipw_propensity.md`
- Homework solutions: `instructor_solutions/HW08_ipw_propensity_solution.md`
- Exit poll: `polls/P08_exit_poll.md`

### Learning goals
- Explain IP weighting as **creating a pseudo-population** where treatment is independent of measured confounders.
- Fit a propensity model \(e(L)=Pr(A=1|L)\) and compute **unstabilized** and **stabilized** weights.
- Diagnose failure modes: **lack of overlap/positivity**, extreme weights, imbalance after weighting.
- Produce a defensible causal estimate + a minimal diagnostics panel.

### Required reading
- Hernán & Robins, *What If*, Chapter 12 (IPW basics + intuition): https://miguelhernan.org/whatifbook

### In-class activity (10–12 min)
- Hand-calculation on a 2×2 stratified example: compute weights and interpret the pseudo-population.

### Colab notebook plan (MIMIC-IV Demo)
**Notebook 08:** “IPW pipeline (complete) — students only change the model”
- Data: `cohort_L08_ps_ipw.parquet` (baseline/early exposure cohort; binary A; binary or continuous Y)
- Provided (do not ask students to write):
  - data loading + basic EDA
  - helper functions: `compute_ipw()`, `plot_ps_overlap()`, `love_plot_smd()`, `plot_weights()`
- Student tasks:
  1. Specify the **propensity model formula** (and justify covariates as pre-treatment).
  2. Compute stabilized weights.
  3. Run diagnostics (overlap, weights, balance).
  4. Estimate marginal causal effect (weighted mean/risk difference; optionally weighted GLM).

### Homework (team-based; structured and short)
1. **Target trial block (mandatory):** eligibility, time zero, exposure window, outcome window, estimand.
2. **Coding:** run the IPW pipeline; submit a single notebook and a 1–2 page memo.
3. **Diagnostics panel (required figures):**
   - `ps_overlap.png`, `weights_hist.png`, `love_plot.png` saved to `figures/L08/`
4. **Interpretation:** 5–8 sentences: “Under assumptions … we estimate …”; mention one limitation.

#### Instructor solution sketch
- Provide a baseline PS model (logit), show stabilized weights, truncation (1/99) as sensitivity, and balance thresholds (|SMD|<0.1 rule-of-thumb).

---

## Lecture 9 — Standardization + (parametric) g-formula (and “why model”) (MIMIC-IV Demo)
### Assets to generate (slides + notebook + homework + poll)
- Slides: `slides/L09_gformula_standardization.md`
- Notebook (student): `notebooks/L09_gformula_standardization_student.ipynb` (**fill-in-the-blanks; pipeline provided**)
- Notebook (solution, instructor): `instructor_solutions/L09_gformula_standardization_solution.ipynb`
- Homework prompt: `assignments/HW09_gformula_standardization.md`
- Homework solutions: `instructor_solutions/HW09_gformula_standardization_solution.md`
- Exit poll: `polls/P09_exit_poll.md`

### Learning goals
- Derive and implement standardization:
  - \(Pr(Y^a=1)=\sum_l Pr(Y=1|A=a,L=l)\,Pr(L=l)\) (discrete \(L\))  
  - parametric g-formula for high-dimensional \(L\)
- Connect **estimand → identification → estimator → computation** (this is the “why model” message).
- Compare g-formula vs IPW and articulate tradeoffs (model dependence vs weight instability).
- Bootstrap the full procedure for uncertainty.

### Required reading
- Hernán & Robins, g-formula/standardization sections (aligned chapter in *What If*).

### In-class activity (8–10 min)
- Whiteboard derivation of the g-formula for a point exposure using the law of total probability.

### Colab notebook plan (MIMIC-IV Demo)
**Notebook 09:** “G-formula end-to-end”
- Data: `cohort_L09_gformula.parquet` (same substantive cohort as L08 if possible)
- Provided:
  - outcome-model skeleton (linear/logistic) + prediction under A=1 and A=0
  - bootstrap wrapper
- Student tasks:
  1. Specify \(E[Y|A,L]\) model (formula; include nonlinear terms if justified).
  2. Produce standardized estimates for \(E[Y^1]\) and \(E[Y^0]\) + effect measure (RD/RR/mean difference).
  3. Run bootstrap (≥200 replicates; adjustable for time) and plot bootstrap distribution.

### Homework
1. **Derivation:** write the standardization formula and state conditional exchangeability + positivity.
2. **Coding:** g-formula estimate + bootstrap CI.
3. **Comparison (short):** contrast with IPW results from L08 (one paragraph).

#### Instructor solution sketch
- Show a “simple model” and “richer model” sensitivity; emphasize interpretation of estimand vs model coefficients.

---

## Lecture 10 — Causal survival analysis: time-to-event outcomes, censoring, discrete-time hazards (MIMIC-IV Demo)
### Assets to generate (slides + notebook + homework + poll)
- Slides: `slides/L10_causal_survival.md`
- Notebook (student): `notebooks/L10_causal_survival_student.ipynb` (**fill-in-the-blanks; pipeline provided**)
- Notebook (solution, instructor): `instructor_solutions/L10_causal_survival_solution.ipynb`
- Homework prompt: `assignments/HW10_causal_survival.md`
- Homework solutions: `instructor_solutions/HW10_causal_survival_solution.md`
- Exit poll: `polls/P10_exit_poll.md`

### Learning goals
- Distinguish **risk** vs **hazard** vs **survival**; know what effect measure you are estimating.
- Convert a cohort into **person-period** (discrete time) data and fit pooled logistic hazards.
- Handle **right censoring** with **IPCW**; understand when censoring is “informative”.
- Produce causal survival curves under a point treatment (and interpret assumptions).

### Required reading
- Hernán & Robins, sections on censoring and survival (target trial chapters/sections as applicable).

### In-class activity (10 min)
- “Time-zero & censoring audit” on a clinical vignette: identify immortal time and define censoring rules.

### Colab notebook plan (MIMIC-IV Demo)
**Notebook 10:** “Discrete-time survival with IPCW”
- Data: `cohort_L10_survival.parquet` with:
  - baseline covariates \(L\)
  - point exposure \(A\) in first 6–24h
  - follow-up time \(T\) and event indicator \(\Delta\)
  - censoring indicator (if applicable; or administrative censoring)
- Provided:
  - function `make_person_period(df, t_max, id_col, t_col, event_col)`
  - hazard model skeleton + prediction under A=1 and A=0
  - plotting utilities for survival curves
- Student tasks:
  1. Specify hazard model (pooled logistic) and compute survival curves.
  2. If informative censoring is included in the exercise: fit censoring model and compute IPCW; re-estimate curves.

### Homework
1. Define your target trial for a time-to-event outcome and specify censoring rules.
2. Coding: produce unweighted and IPCW-weighted survival curves; interpret differences.
3. Short answer: why “hazard ratio” is not automatically a causal effect measure without assumptions.

#### Instructor solution sketch
- Show (i) naive Kaplan–Meier by A (associational), (ii) standardized/weighted causal survival curves, (iii) sensitivity to censoring model and truncation.

---

## Lecture 11 — Time-varying treatment and confounding: marginal structural models (MSMs) (MIMIC-IV Demo)
### Assets to generate (slides + notebook + homework + poll)
- Slides: `slides/L11_msm_time_varying.md`
- Notebook (student): `notebooks/L11_msm_time_varying_student.ipynb` (**fill-in-the-blanks; pipeline provided**)
- Notebook (solution, instructor): `instructor_solutions/L11_msm_time_varying_solution.ipynb`
- Homework prompt: `assignments/HW11_msm_time_varying.md`
- Homework solutions: `instructor_solutions/HW11_msm_time_varying_solution.md`
- Exit poll: `polls/P11_exit_poll.md`

### Learning goals
- Recognize time-varying confounding affected by prior treatment.
- Construct stabilized weights over time:
  - treatment weights \(W_A\)
  - censoring weights \(W_C\)
  - combined weights \(W=W_A	imes W_C\)
- Fit a simple MSM (weighted pooled logistic/GLM) and interpret the parameter as a **marginal causal effect** under assumptions.

### Required reading
- Hernán & Robins, MSM sections (typically Chapter 12 continuation / longitudinal chapters).

### In-class activity (10–12 min)
- “Why standard adjustment fails”: walk through a time-varying DAG and identify the blocked/unblocked paths.

### Colab notebook plan (MIMIC-IV Demo)
**Notebook 11:** “MSM pipeline (procedural, not black-box)”
- Data: `cohort_L11_msm_longitudinal.parquet` (person-period; includes \(A_t, L_t, C_t, Y\))
- Provided:
  - weight construction scaffolding with explicit dataframe columns:
    - `pA_denom`, `pA_num`, `wA`, `pC_denom`, `pC_num`, `wC`, `W = wA*wC`
  - diagnostic plots: weights over time; truncation; balance over time (simple)
- Student tasks:
  1. Specify numerator/denominator models (formulas).
  2. Compute stabilized weights and diagnose.
  3. Fit weighted MSM and interpret.

### Homework
1. Draw a time-varying DAG for your cohort; explain why \(L_t\) is problematic.
2. Coding: construct weights and fit an MSM; include weight diagnostics.
3. Interpretation: 1 paragraph on assumptions + one key limitation.

#### Instructor solution sketch
- Provide “minimal models” for numerator/denominator; show truncation and sensitivity.

---

## Lecture 12 — Capstone: target trial emulation workshop + project presentations (MIMIC-IV Demo or full MIMIC-IV optional)
### Assets to generate (slides + workshop materials + poll)
- Slides: `slides/L12_target_trial_capstone.md`
- Workshop notebook (student): `notebooks/L12_target_trial_workshop_student.ipynb` (mostly complete; checklists + placeholders)
- Instructor reference: `instructor_solutions/L12_target_trial_workshop_solution.ipynb`
- Project protocol template: `project/target_trial_protocol_template.md`
- Exit poll: `polls/P12_exit_poll.md`

### Learning goals
- Convert an informal clinical question into a **complete target trial protocol**:
  eligibility, time zero, treatment strategies, assignment, follow-up, outcomes, causal contrast, analysis plan.
- Stress-test protocol choices for bias: time zero, censoring, competing risks (brief), positivity.
- Produce a “protocol v2” that is executable as code + tables/figures.

### In-class structure (highly structured, to avoid chaos)
1. **20 min:** protocol checklist walkthrough + common failure modes (immortal time, conditioning on post-treatment).
2. **40–50 min:** team work time (protocol v2 + analysis plan in the repo).
3. **30–40 min:** rapid presentations (3–4 min/team): protocol + one diagnostic figure + next steps.
4. **5 min:** exit poll + “muddiest point”.

### Capstone deliverables (submitted by each team)
- `project/protocol_v2.md` (target trial protocol)
- `project/notebooks/analysis.ipynb` (runs end-to-end on Demo; full MIMIC optional)
- `project/report.md` (≤6 pages; assumptions + results + limitations)
- `project/results/` (tables/figures; aggregate only)

### Optional mini-module (asynchronous): Instrumental variables (IV) — **not core**
- Provide as a **short handout + optional notebook**:
  - `optional/IV/slides_IV_short.md` (≈20 slides)
  - `optional/IV/notebook_IV_simulation.ipynb` (strong vs weak IV demo)
- Message to students: IV is powerful but rare in EHR settings; included for completeness, not required.



# 6) High-yield “improvements” that add learning without adding confusion

1. **One running example across lectures.**  
   Use **one MIMIC-IV Demo cohort** as the running anchor across the applied lectures (e.g., early antibiotics → 28-day mortality), so students can compare methods fairly.
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

### Definition of done (what Cursor must produce)
A GitHub repository that includes, for **each lecture L01–L12**:
1. A **student notebook** (Colab-ready) with a **nearly-complete pipeline** where students only fill a few marked cells (model specification, a derivation, an interpretation).
2. A matching **instructor solution notebook** (kept private; generate it anyway).
3. A short **assignment prompt** (team-based) + an **answer key** (kept private).
4. A short **exit poll** (3–5 questions) + answer key.
5. A dedicated `figures/` folder where the notebook saves all plots used in slides.

In addition:
- A small, clean Python package under `src/` providing reusable utilities (IPW, g-formula, bootstrapping, balance diagnostics, survival helpers, plotting).
- A top-level `README.md` that explains:
  - environment setup (local + Colab)
  - how to download the course extracts
  - an index table with **Open-in-Colab links** for every student notebook
  - where to find each lecture’s materials
- Lightweight CI/linting (`ruff`, `black`, `pre-commit`, GitHub Actions) to keep the repo stable.

### Pedagogical constraints (non-negotiable)
- **Procedural and explicit > black box.** Avoid class-heavy designs.
  - Good: explicitly create `weights` columns and show formulas in code comments.
  - Bad: `estimator.fit(data)` hiding logic.
- Student notebooks must run end-to-end **before** students edit anything.
- Keep Python difficulty below the causal inference difficulty.
  - Students should mostly change formulas, covariate sets, and interpret diagnostics—not debug syntax.

### Data policy (non-negotiable)
- **All graded work must run on MIMIC-IV Demo** + course-provided analysis-ready extracts (CSV/Parquet).
- **Never** commit or upload row-level **full** MIMIC-IV data.
- For **MIMIC-IV Demo extracts**:
  - If extracts are small, they may live in the repo under `data/derived/` **or**
  - Provide `data/download_data.py` to download them from a release/bucket into `data/raw/`.
- Always include a variable dictionary and cohort definition for each extract.

### Required repository structure (separate directory per lecture)
Use this structure exactly (you can add more files, but keep these paths stable):

```
phs564-causal-inference/
  README.md
  DATA_SOURCES.md
  LICENSE
  CITATION.cff
  pyproject.toml
  requirements.txt
  .gitignore
  .pre-commit-config.yaml
  .github/workflows/ci.yml

  data/
    README.md
    download_data.py
    raw/                       # empty by default
    derived/                   # optional small extracts (Demo only)
    dictionaries/              # variable dictionaries/codebooks
      cohort_L08_ps_ipw.md
      cohort_L10_survival.md
      ...

  lectures/
    L01_counterfactuals/
      slides_outline.md
      notebook_student.ipynb
      poll_exit.md
      assignment.md
      figures/                 # notebooks save plots here
      sql/                     # optional (Demo extraction for transparency)
      solutions/               # keep private in real life (generate anyway)
        notebook_solution.ipynb
        assignment_solution.md
        poll_exit_key.md

    L02_rcts/
      ...
    ...
    L12_target_trial_capstone/
      ...

  src/phs564_ci/
    __init__.py
    io.py                      # loading extracts + paths
    plotting.py
    diagnostics.py             # overlap, weights, balance
    ipw.py
    gformula.py
    survival.py
    msm.py
    utils.py

  project/
    target_trial_protocol_template.md
    grading_rubric.md
    submission_checklist.md

  optional/
    IV/
      slides_IV_short.md
      notebook_IV_simulation.ipynb
```

### Notebook build rules (make them Colab-friendly)
- At the top of each student notebook:
  - a single “Install dependencies” cell (fast; pinned minimal versions)
  - a single “Download data” cell calling `python data/download_data.py --lecture LXX`
  - `import` section with short comments
- Use `pathlib` for paths; avoid OS-specific behavior.
- All plots saved deterministically to `lectures/LXX_*/figures/`.

### Minimum required figures per applied lecture
Each applied lecture notebook must output at least:
- **L08 (IPW):** PS overlap + weight histogram + love plot
- **L09 (g-formula):** standardized predictions under A=1/A=0 + bootstrap distribution
- **L10 (survival):** survival curves (unweighted + weighted) + censoring/weight diagnostic
- **L11 (MSM):** weight distribution over time + one marginal effect plot/table

### Team accountability hooks
- Each assignment should instruct teams to include:
  - link to the GitHub commits/PRs
  - a short “contributions” section stating what each partner did
- Provide a simple script `scripts/verify_contributions.py` that checks both partners committed.


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