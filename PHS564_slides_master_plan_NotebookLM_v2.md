# PHS564 — Slides Master Plan for NotebookLM (12 sessions)

This Markdown file is a **detailed deck blueprint** (slide titles + key content + figure instructions) for each lecture.

## NotebookLM generation rules
1. Generate **one deck per lecture** (L01–L12), 16:9.
2. Keep ≈ **1:30 per slide average**; slides labeled **(Pause/Activity)** are timed anchors.
3. Minimal text; one idea/slide; consistent notation (`Y^a`, `A`, `Y`, `L`, `C`, `U`).
4. Put assumptions in a standard callout: **Consistency**, **Exchangeability**, **Positivity**, **Correct specification** (as relevant).
5. For every figure slide include in speaker notes:
   - Figure title; type (Draw/From notebook); file path `figures/LXX/<name>.png`; what it shows; alt-text.
6. If a figure file is missing, insert a placeholder box: `FIGURE PLACEHOLDER: figures/LXX/<name>.png`.


## Figure sourcing
- Conceptual diagrams (DAGs, flowcharts, tables): **Draw (vector)**.
- Statistical graphics (overlap, weights, love plots, survival curves): **From notebook**, saved under `figures/LXX/`.


## L01 — Counterfactuals and definition of causal effects
**Target duration:** 100–110 min  
**Target slides:** 68–72

### Opening & motivation (Slides 1–7)
- 01. **Title** — Key: Course + lecture title; why counterfactuals — Visual: None — Notes: Frame today as foundations.
- 02. **Course map (L01–L12)** — Key: Where we are; where we're going — Visual: Draw (vector): timeline of 12 sessions
- 03. **Motivation: decisions need causal effects** — Key: Clinical & policy decisions — Visual: Draw (vector): icons (clinic/policy/public health)
- 04. **Running example: early antibiotics → 28-day mortality** — Key: Define the substantive question — Visual: Draw (vector): ICU timeline (t0, exposure window, follow-up)
- 05. **Association vs causation** — Key: Same data, different conclusions — Visual: Draw (vector): scatter + '≠' + causal arrow
- 06. **What is a causal question?** — Key: Population, intervention, outcome, time horizon — Visual: Draw (vector): checklist
- 07. ****(Pause/Activity)** Write your own causal question** — Key: Teams of 2 draft question; share 1–2 — Visual: Prompt-only slide — Notes: 6–8 min

### Potential outcomes & estimands (Slides 8–15)
- 08. **Potential outcomes intuition** — Key: Each person has Y^1 and Y^0 — Visual: Draw (vector): two outcome cards/person
- 09. **Observed outcome is one potential outcome** — Key: We see Y = Y^A — Visual: Draw (vector): selector switch
- 10. **Counterfactual table (4 people)** — Key: Show missing counterfactuals — Visual: Draw (vector): table with Y^1, Y^0, A, Y
- 11. **Individual causal effect** — Key: Y^1 − Y^0 is not identifiable — Visual: Draw (vector): highlight missing cells
- 12. **Average treatment effect (ATE)** — Key: E[Y^1 − Y^0] as target — Visual: Draw (vector): averaging arrow
- 13. **Risk difference / risk ratio** — Key: RD and RR definitions — Visual: Draw (vector): 2 tiles RD/RR
- 14. **Odds ratio (when used)** — Key: OR as effect measure; caution — Visual: Draw (vector): OR tile
- 15. **Notation legend** — Key: Y, A, L, C, U; Y^a — Visual: Draw (vector): legend box

### Assumptions basics (Slides 16–20)
- 16. **Well-defined intervention** — Key: Versions of treatment matter — Visual: Draw (vector): intervention definition box
- 17. **Consistency** — Key: If A=a then Y=Y^a — Visual: Equation + words (vector)
- 18. **SUTVA & interference** — Key: When one unit affects another — Visual: Draw (vector): small network
- 19. **Time zero matters** — Key: Define t0 to avoid bias — Visual: Draw (vector): timeline with t0 highlighted
- 20. **Censoring vs outcome** — Key: C not equal Y; selection mechanism — Visual: Draw (vector): timeline with dropout

### Bridging causal ↔ observed (Slides 21–26)
- 21. **Causal vs associational estimands** — Key: E[Y^1] vs E[Y|A=1] — Visual: Draw (vector): side-by-side
- 22. **Why we need assumptions** — Key: To link Y^a to observed data — Visual: Draw (vector): bridge diagram
- 23. **Exchangeability teaser** — Key: Y^a ⫫ A (or conditional) — Visual: Draw (vector): statement + 'when?'
- 24. **Confounding teaser** — Key: L affects A and Y — Visual: Draw (vector): 3-node A←L→Y
- 25. **Selection bias teaser** — Key: Conditioning on S creates bias — Visual: Draw (vector): A→S←Y
- 26. **Measurement bias teaser** — Key: Misclassification of A or Y — Visual: Draw (vector): noisy measurement icon

### Worked micro-examples (Slides 27–32)
- 27. **Micro-example: transplant** — Key: Define estimand; discuss t0 — Visual: Draw (vector): timeline + eligibility
- 28. **Micro-example: transplant potential outcomes** — Key: Observed vs missing — Visual: Draw (vector): mini table
- 29. **Micro-example: smoking → lung cancer** — Key: Confounding by SES — Visual: Draw (vector): DAG A←L→Y (no rules yet)
- 30. **Micro-example: ICU fluids** — Key: Versions of treatment; consistency — Visual: Draw (vector): treatment strategy box
- 31. ****(Pause/Activity)** List candidate confounders** — Key: Teams list pre-treatment causes of A and Y — Visual: Prompt-only — Notes: 6 min
- 32. **Skill: define unit of analysis** — Key: patient vs encounter vs time — Visual: Draw (vector): unit diagram

### Notation practice (Slides 33–37)
- 33. **Translate statements to notation (1)** — Key: “Risk if everyone treated” → E[Y^1] — Visual: Draw (vector): text→notation
- 34. **Translate statements to notation (2)** — Key: “Risk among treated” → E[Y|A=1] — Visual: Draw (vector): text→notation
- 35. **Translate statements to notation (3)** — Key: Causal RD → E[Y^1]−E[Y^0] — Visual: Draw (vector): notation tile
- 36. **Translate assumptions to notation** — Key: Conditional exchangeability — Visual: Draw (vector): Y^a ⫫ A | L
- 37. **Common notation pitfalls** — Key: conditioning on post-treatment — Visual: Draw (vector): warning

### Checks & wrap (Slides 38–42)
- 38. ****(Pause/Activity)** Concept check (3 questions)** — Key: Teams answer; quick discussion — Visual: Prompt-only — Notes: 5 min
- 39. **Common misconceptions** — Key: counterfactuals encode questions — Visual: Draw (vector): myth/fact
- 40. **Summary: what we defined** — Key: Potential outcomes; estimands; time zero — Visual: Draw (vector): 3 bullets
- 41. **Preview: RCT identification next time** — Key: Randomization → exchangeability — Visual: Draw (vector): L01→L02
- 42. **Homework + reading** — Key: Deliverables + Ch.1 — Visual: Draw (vector): checklist

### Practice/backup (Slides 43–72)
- 43. **L01 Practice/backup: Rewrite vague causal questions into well-defined interventions** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 44. **L01 Practice/backup: More potential-outcomes tables (binary + continuous outcomes)** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 45. **L01 Practice/backup: Choose RD vs RR for different policy questions** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 46. **L01 Practice/backup: Time-zero pitfalls (immortal time miniature examples)** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 47. **L01 Practice/backup: Interference examples (vaccines, ICU bed assignment)** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 48. **L01 Practice/backup: Glossary drill (estimand vs estimator vs identification)** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 49. **L01 Practice/backup: Mini-quiz: notation translation (5 items)** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 50. **L01 Practice/backup: Mini-quiz: identify which bias type (confounding/selection/measurement)** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 51. **L01 Practice/backup (2): Rewrite vague causal questions into well-defined interventions** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 52. **L01 Practice/backup (2): More potential-outcomes tables (binary + continuous outcomes)** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 53. **L01 Practice/backup (2): Choose RD vs RR for different policy questions** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 54. **L01 Practice/backup (2): Time-zero pitfalls (immortal time miniature examples)** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 55. **L01 Practice/backup (2): Interference examples (vaccines, ICU bed assignment)** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 56. **L01 Practice/backup (2): Glossary drill (estimand vs estimator vs identification)** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 57. **L01 Practice/backup (2): Mini-quiz: notation translation (5 items)** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 58. **L01 Practice/backup (2): Mini-quiz: identify which bias type (confounding/selection/measurement)** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 59. **L01 Practice/backup (3): Rewrite vague causal questions into well-defined interventions** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 60. **L01 Practice/backup (3): More potential-outcomes tables (binary + continuous outcomes)** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 61. **L01 Practice/backup (3): Choose RD vs RR for different policy questions** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 62. **L01 Practice/backup (3): Time-zero pitfalls (immortal time miniature examples)** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 63. **L01 Practice/backup (3): Interference examples (vaccines, ICU bed assignment)** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 64. **L01 Practice/backup (3): Glossary drill (estimand vs estimator vs identification)** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 65. **L01 Practice/backup (3): Mini-quiz: notation translation (5 items)** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 66. **L01 Practice/backup (3): Mini-quiz: identify which bias type (confounding/selection/measurement)** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 67. **L01 Practice/backup (4): Rewrite vague causal questions into well-defined interventions** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 68. **L01 Practice/backup (4): More potential-outcomes tables (binary + continuous outcomes)** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 69. **L01 Practice/backup (4): Choose RD vs RR for different policy questions** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 70. **L01 Practice/backup (4): Time-zero pitfalls (immortal time miniature examples)** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 71. **L01 Practice/backup (4): Interference examples (vaccines, ICU bed assignment)** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).
- 72. **L01 Practice/backup (4): Glossary drill (estimand vs estimator vs identification)** — Key: Add one concrete example + 1 question to ask the class — Visual: Draw (vector) or None — Notes: Use as pacing buffer (2–4 min each).

## L02 — Causal effects in ideal randomized trials
**Target duration:** 100–110 min  
**Target slides:** 70–74

### RCT identification core (Slides 1–10)
- 01. **Title** — Key: Ideal randomized trials: identification and estimation — Visual: None
- 02. **Course map** — Key: L02: randomization identifies E[Y^a] — Visual: Draw (vector): map highlight
- 03. **Target trial (preview)** — Key: protocol components — Visual: Draw (vector): checklist
- 04. **Randomization mechanism** — Key: A assigned by chance — Visual: Draw (vector): coin/lottery
- 05. **Unconditional exchangeability** — Key: Y^a ⫫ A — Visual: Assumption callout (vector)
- 06. **Identification result** — Key: E[Y^a]=E[Y|A=a] — Visual: Equation chain (vector)
- 07. **Estimands in RCT** — Key: RD/RR; ITT vs PP — Visual: Draw (vector): tiles
- 08. **Estimator: difference in means** — Key: sample RD — Visual: Minimal formula
- 09. **CI intuition** — Key: sampling variation — Visual: Draw (vector): error bars
- 10. **(Pause/Activity) RCT abstract dissection** — Key: identify estimand/estimator/target pop — Visual: Prompt-only — Notes: 7 min

### ITT, adherence, censoring (Slides 11–19)
- 11. **ITT effect** — Key: effect of assignment — Visual: Draw (vector): assigned→outcome
- 12. **Per-protocol effect** — Key: effect of adhering — Visual: Draw (vector): adherence pathway
- 13. **Noncompliance categories** — Key: always/never/compliers — Visual: Draw (vector): compliance table
- 14. **Why ITT preserves randomization** — Key: bias protection — Visual: Draw (vector): shield
- 15. **When PP needs adjustment** — Key: adherence confounding — Visual: Draw (vector): DAG with adherence
- 16. **Loss to follow-up** — Key: selection in trials — Visual: Draw (vector): dropout timeline
- 17. **CONSORT flow** — Key: reporting standards — Visual: Draw (vector): flow diagram
- 18. **Blinding & measurement bias** — Key: what blinding prevents — Visual: Draw (vector): bias channels
- 19. **(Pause/Activity) design a mini RCT** — Key: teams specify t0, A, Y, follow-up — Visual: Prompt-only — Notes: 8–10 min

### Adjustment, simulation, wrap (Slides 20–32)
- 20. **Covariate adjustment in RCT** — Key: precision gain — Visual: Draw (vector): bias vs variance slider
- 21. **Stratified estimator (toy)** — Key: compute within strata then average — Visual: Draw (vector): table arithmetic
- 22. **Regression adjustment (toy)** — Key: model + plug-in — Visual: Draw (vector): model→predict
- 23. **Simulation: RCT vs observational** — Key: randomization removes confounding — Visual: From notebook: figures/L02/sim_rct_vs_obs.png
- 24. **Subgroup analyses cautions** — Key: multiplicity; post hoc — Visual: Draw (vector): caution box
- 25. **Harms reporting** — Key: absolute risks matter — Visual: Draw (vector): RD emphasis
- 26. **Summary** — Key: what RCT identifies; pitfalls — Visual: None
- 27. **Homework: simulate RCT** — Key: estimate RD + CI; interpret — Visual: From notebook placeholder: figures/L02/hw_sim.png
- 28. **Homework: critique paper** — Key: estimand clarity + threats — Visual: Draw (vector): checklist
- 29. **Reading** — Key: Hernán & Robins Ch. 2 — Visual: None
- 30. **Exit ticket** — Key: 1 thing learned; 1 question — Visual: Prompt-only — Notes: 2 min
- 31. **Backup: notation legend** — Key: Y^a, ITT, PP — Visual: Draw (vector): legend
- 32. **Backup: course map** — Key: today vs next — Visual: Draw (vector)

### Practice/backup (Slides 33–72)
- 33. **L02 Practice/backup: Worked example: ITT from 2×2 table (with CI)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 34. **L02 Practice/backup: Worked example: PP vs ITT interpretation** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 35. **L02 Practice/backup: Vignette: differential dropout and bias direction** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 36. **L02 Practice/backup: Practice: identify randomization vs allocation concealment** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 37. **L02 Practice/backup: Practice: interpret CI correctly (coverage intuition)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 38. **L02 Practice/backup: Mini-quiz: estimand vs estimator (8 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 39. **L02 Practice/backup: Practice: CONSORT checklist items** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 40. **L02 Practice/backup: Pitfall: post-randomization covariate adjustment** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 41. **L02 Practice/backup: Pitfall: per-protocol without addressing adherence confounding** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 42. **L02 Practice/backup: Optional: cluster randomized trial intuition (ICC concept)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 43. **L02 Practice/backup (2): Worked example: ITT from 2×2 table (with CI)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 44. **L02 Practice/backup (2): Worked example: PP vs ITT interpretation** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 45. **L02 Practice/backup (2): Vignette: differential dropout and bias direction** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 46. **L02 Practice/backup (2): Practice: identify randomization vs allocation concealment** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 47. **L02 Practice/backup (2): Practice: interpret CI correctly (coverage intuition)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 48. **L02 Practice/backup (2): Mini-quiz: estimand vs estimator (8 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 49. **L02 Practice/backup (2): Practice: CONSORT checklist items** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 50. **L02 Practice/backup (2): Pitfall: post-randomization covariate adjustment** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 51. **L02 Practice/backup (2): Pitfall: per-protocol without addressing adherence confounding** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 52. **L02 Practice/backup (2): Optional: cluster randomized trial intuition (ICC concept)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 53. **L02 Practice/backup (3): Worked example: ITT from 2×2 table (with CI)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 54. **L02 Practice/backup (3): Worked example: PP vs ITT interpretation** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 55. **L02 Practice/backup (3): Vignette: differential dropout and bias direction** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 56. **L02 Practice/backup (3): Practice: identify randomization vs allocation concealment** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 57. **L02 Practice/backup (3): Practice: interpret CI correctly (coverage intuition)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 58. **L02 Practice/backup (3): Mini-quiz: estimand vs estimator (8 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 59. **L02 Practice/backup (3): Practice: CONSORT checklist items** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 60. **L02 Practice/backup (3): Pitfall: post-randomization covariate adjustment** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 61. **L02 Practice/backup (3): Pitfall: per-protocol without addressing adherence confounding** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 62. **L02 Practice/backup (3): Optional: cluster randomized trial intuition (ICC concept)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 63. **L02 Practice/backup (4): Worked example: ITT from 2×2 table (with CI)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 64. **L02 Practice/backup (4): Worked example: PP vs ITT interpretation** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 65. **L02 Practice/backup (4): Vignette: differential dropout and bias direction** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 66. **L02 Practice/backup (4): Practice: identify randomization vs allocation concealment** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 67. **L02 Practice/backup (4): Practice: interpret CI correctly (coverage intuition)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 68. **L02 Practice/backup (4): Mini-quiz: estimand vs estimator (8 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 69. **L02 Practice/backup (4): Practice: CONSORT checklist items** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 70. **L02 Practice/backup (4): Pitfall: post-randomization covariate adjustment** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 71. **L02 Practice/backup (4): Pitfall: per-protocol without addressing adherence confounding** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 72. **L02 Practice/backup (4): Optional: cluster randomized trial intuition (ICC concept)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).

## L03 — Causal effects in observational studies (identifiability and assumptions)
**Target duration:** 105–115 min  
**Target slides:** 72–78

### Assumptions + roadmap (Slides 1–10)
- 01. **Title** — Key: Observational studies: assumptions & identification — Visual: None
- 02. **Course map** — Key: L03: replace randomization with assumptions — Visual: Draw (vector): map highlight
- 03. **Why observational?** — Key: ethics/cost/rare exposures — Visual: Draw (vector): icons
- 04. **Running example: early antibiotics** — Key: severity confounding — Visual: Draw (vector): timeline + severity
- 05. **Identification roadmap** — Key: estimand → assumptions → method — Visual: Draw (vector): pipeline
- 06. **Conditional exchangeability** — Key: Y^a ⫫ A | L — Visual: Assumption callout
- 07. **Positivity** — Key: Pr(A=a|L=l)>0 — Visual: Draw (vector): overlap sketch
- 08. **Consistency** — Key: well-defined interventions — Visual: Callout
- 09. **What must be in L?** — Key: pre-treatment common causes — Visual: Draw (vector): checklist
- 10. **(Pause/Activity) Which assumption is fragile here?** — Key: teams choose & justify — Visual: Prompt-only — Notes: 6–7 min

### Identification intuition (Slides 11–19)
- 11. **Identification by standardization** — Key: E[Y^a]=Σ_l E[Y|A=a,L=l]P(L=l) — Visual: Equation with labels
- 12. **Standardization intuition** — Key: reweight stratum-specific outcomes — Visual: Draw (vector): strata + weights
- 13. **Identification by IPW (preview)** — Key: E[Y^a]=E[ w_a Y ] (concept) — Visual: Draw (vector): weighting schematic
- 14. **Positivity failure demo** — Key: non-overlap leads to instability — Visual: From notebook: figures/L03/overlap_bad.png
- 15. **Extreme weights intuition** — Key: small Pr(A|L) → huge weights — Visual: Draw (vector): denominator shrink
- 16. **Unmeasured confounding** — Key: U breaks exchangeability — Visual: Draw (vector): DAG A←U→Y
- 17. **Measurement error in L** — Key: residual confounding — Visual: Draw (vector): noisy L
- 18. **Practical: define time zero** — Key: avoid immortal time — Visual: Draw (vector): t0 highlight
- 19. **(Pause/Activity) List L for your project** — Key: teams list covariates — Visual: Prompt-only — Notes: 7–8 min

### Wrap + homework (Slides 20–30)
- 20. **Selection bias teaser** — Key: conditioning on S — Visual: Draw (vector): A→S←Y
- 21. **Transportability teaser** — Key: target vs study pop — Visual: Draw (vector): two circles
- 22. **Summary: assumptions** — Key: exchangeability/positivity/consistency — Visual: Draw (vector): legend
- 23. **Summary: two method families** — Key: g-formula vs IPW — Visual: Draw (vector): fork
- 24. **Homework: overlap diagnostics** — Key: plots + interpretation — Visual: From notebook placeholder: figures/L03/hw_overlap.png
- 25. **Homework: assumptions memo** — Key: which plausible; what threatens them — Visual: Draw (vector): rubric mini-grid
- 26. **Reading** — Key: Hernán & Robins Ch. 3 — Visual: None
- 27. **Exit ticket** — Key: 1 assumption + 1 design fix — Visual: Prompt-only — Notes: 2 min
- 28. **Backup: notation legend** — Key: Y^a ⫫ A|L; positivity — Visual: Draw (vector)
- 29. **Backup: g-formula schematic** — Key: algorithm preview — Visual: Draw (vector)
- 30. **Backup: IPW schematic** — Key: algorithm preview — Visual: Draw (vector)

### Practice/backup (Slides 31–75)
- 31. **L03 Practice/backup: Worked example: 2-stratum standardization (compute E[Y^1], E[Y^0])** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 32. **L03 Practice/backup: Worked example: positivity violation and what to do (restriction vs model)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 33. **L03 Practice/backup: Vignette: unmeasured confounding—what variable would fix it?** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 34. **L03 Practice/backup: Practice: classify variables as pre/post exposure on a timeline** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 35. **L03 Practice/backup: Mini-quiz: which assumption is violated? (10 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 36. **L03 Practice/backup: Practice: translate 8 English statements into potential outcomes notation** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 37. **L03 Practice/backup: Practice: interpret overlap plots (good vs bad overlap)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 38. **L03 Practice/backup: Pitfall: adjusting for post-treatment severity** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 39. **L03 Practice/backup: Pitfall: defining exposure using future information (look-ahead bias)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 40. **L03 Practice/backup: Optional: negative control outcome/exposure (concept only)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 41. **L03 Practice/backup (2): Worked example: 2-stratum standardization (compute E[Y^1], E[Y^0])** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 42. **L03 Practice/backup (2): Worked example: positivity violation and what to do (restriction vs model)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 43. **L03 Practice/backup (2): Vignette: unmeasured confounding—what variable would fix it?** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 44. **L03 Practice/backup (2): Practice: classify variables as pre/post exposure on a timeline** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 45. **L03 Practice/backup (2): Mini-quiz: which assumption is violated? (10 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 46. **L03 Practice/backup (2): Practice: translate 8 English statements into potential outcomes notation** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 47. **L03 Practice/backup (2): Practice: interpret overlap plots (good vs bad overlap)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 48. **L03 Practice/backup (2): Pitfall: adjusting for post-treatment severity** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 49. **L03 Practice/backup (2): Pitfall: defining exposure using future information (look-ahead bias)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 50. **L03 Practice/backup (2): Optional: negative control outcome/exposure (concept only)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 51. **L03 Practice/backup (3): Worked example: 2-stratum standardization (compute E[Y^1], E[Y^0])** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 52. **L03 Practice/backup (3): Worked example: positivity violation and what to do (restriction vs model)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 53. **L03 Practice/backup (3): Vignette: unmeasured confounding—what variable would fix it?** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 54. **L03 Practice/backup (3): Practice: classify variables as pre/post exposure on a timeline** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 55. **L03 Practice/backup (3): Mini-quiz: which assumption is violated? (10 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 56. **L03 Practice/backup (3): Practice: translate 8 English statements into potential outcomes notation** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 57. **L03 Practice/backup (3): Practice: interpret overlap plots (good vs bad overlap)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 58. **L03 Practice/backup (3): Pitfall: adjusting for post-treatment severity** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 59. **L03 Practice/backup (3): Pitfall: defining exposure using future information (look-ahead bias)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 60. **L03 Practice/backup (3): Optional: negative control outcome/exposure (concept only)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 61. **L03 Practice/backup (4): Worked example: 2-stratum standardization (compute E[Y^1], E[Y^0])** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 62. **L03 Practice/backup (4): Worked example: positivity violation and what to do (restriction vs model)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 63. **L03 Practice/backup (4): Vignette: unmeasured confounding—what variable would fix it?** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 64. **L03 Practice/backup (4): Practice: classify variables as pre/post exposure on a timeline** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 65. **L03 Practice/backup (4): Mini-quiz: which assumption is violated? (10 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 66. **L03 Practice/backup (4): Practice: translate 8 English statements into potential outcomes notation** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 67. **L03 Practice/backup (4): Practice: interpret overlap plots (good vs bad overlap)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 68. **L03 Practice/backup (4): Pitfall: adjusting for post-treatment severity** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 69. **L03 Practice/backup (4): Pitfall: defining exposure using future information (look-ahead bias)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 70. **L03 Practice/backup (4): Optional: negative control outcome/exposure (concept only)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 71. **L03 Practice/backup (5): Worked example: 2-stratum standardization (compute E[Y^1], E[Y^0])** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 72. **L03 Practice/backup (5): Worked example: positivity violation and what to do (restriction vs model)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 73. **L03 Practice/backup (5): Vignette: unmeasured confounding—what variable would fix it?** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 74. **L03 Practice/backup (5): Practice: classify variables as pre/post exposure on a timeline** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 75. **L03 Practice/backup (5): Mini-quiz: which assumption is violated? (10 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).

## L04 — Effect modification and effect-measure modification
**Target duration:** 95–105 min  
**Target slides:** 64–70

### Core concepts + examples (Slides 1–12)
- 01. **Title** — Key: Effect modification and effect-measure modification — Visual: None
- 02. **Why heterogeneity matters** — Key: targeting + equity — Visual: Draw (vector): icons
- 03. **Definitions** — Key: effect modification vs interaction vs EMM — Visual: Draw (vector): definitions panel
- 04. **Scale dependence** — Key: RD vs RR can disagree — Visual: Draw (vector): RD/RR panel
- 05. **Numeric example setup** — Key: two strata (L=0/1) risks — Visual: Draw (vector): 2×2 tables
- 06. **Compute RD by stratum** — Key: show arithmetic — Visual: Draw (vector): arithmetic
- 07. **Compute RR by stratum** — Key: show arithmetic — Visual: Draw (vector): arithmetic
- 08. **Visualize risks by stratum** — Key: bar plot — Visual: From notebook: figures/L04/risk_by_group.png
- 09. **Interpretation guidance** — Key: biologic vs public health questions — Visual: Draw (vector): checklist
- 10. **Interaction in regression** — Key: A×L term — Visual: Minimal formula
- 11. **Marginal vs conditional effects** — Key: what models output — Visual: Draw (vector): contrast
- 12. **(Pause/Activity) choose scale for 2 questions** — Key: policy vs mechanism — Visual: Prompt-only — Notes: 7 min

### Reporting + wrap (Slides 13–23)
- 13. **Reporting template** — Key: table + figure + narrative — Visual: Draw (vector): template
- 14. **Pitfalls** — Key: multiple testing; sparse strata — Visual: Draw (vector): warning list
- 15. **Transportability teaser** — Key: effect differs across populations — Visual: Draw (vector): two circles
- 16. **Summary** — Key: key takeaways — Visual: None
- 17. **Homework: scale dependence simulation** — Key: generate and interpret — Visual: From notebook placeholder: figures/L04/hw_scale.png
- 18. **Homework: interpretation write-up** — Key: interaction term interpretation — Visual: Draw (vector): rubric mini-grid
- 19. **Reading** — Key: What If EMM sections — Visual: None
- 20. **Exit ticket** — Key: RD vs RR difference in words — Visual: Prompt-only — Notes: 2 min
- 21. **Backup: forest plot layout** — Key: how to display heterogeneity — Visual: Draw (vector)
- 22. **Backup: interaction examples** — Key: linear vs logistic — Visual: Draw (vector)
- 23. **Backup: glossary** — Key: effect modification, interaction, EMM — Visual: Draw (vector)

### Practice/backup (Slides 24–68)
- 24. **L04 Practice/backup: Worked example: effect modification by sex on RD scale** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 25. **L04 Practice/backup: Worked example: same data on RR scale (contrast interpretation)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 26. **L04 Practice/backup: Practice: interpret interaction coefficient (logistic regression)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 27. **L04 Practice/backup: Practice: interpret interaction coefficient (linear model)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 28. **L04 Practice/backup: Mini-quiz: which statement is correct? (10 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 29. **L04 Practice/backup: Pitfall: interpreting stratum-specific association as causal without identification** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 30. **L04 Practice/backup: Visualization: forest plot with RD and RR side-by-side** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 31. **L04 Practice/backup: Optional: additive interaction measures (RERI) as enrichment (clearly labeled optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 32. **L04 Practice/backup (2): Worked example: effect modification by sex on RD scale** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 33. **L04 Practice/backup (2): Worked example: same data on RR scale (contrast interpretation)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 34. **L04 Practice/backup (2): Practice: interpret interaction coefficient (logistic regression)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 35. **L04 Practice/backup (2): Practice: interpret interaction coefficient (linear model)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 36. **L04 Practice/backup (2): Mini-quiz: which statement is correct? (10 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 37. **L04 Practice/backup (2): Pitfall: interpreting stratum-specific association as causal without identification** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 38. **L04 Practice/backup (2): Visualization: forest plot with RD and RR side-by-side** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 39. **L04 Practice/backup (2): Optional: additive interaction measures (RERI) as enrichment (clearly labeled optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 40. **L04 Practice/backup (3): Worked example: effect modification by sex on RD scale** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 41. **L04 Practice/backup (3): Worked example: same data on RR scale (contrast interpretation)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 42. **L04 Practice/backup (3): Practice: interpret interaction coefficient (logistic regression)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 43. **L04 Practice/backup (3): Practice: interpret interaction coefficient (linear model)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 44. **L04 Practice/backup (3): Mini-quiz: which statement is correct? (10 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 45. **L04 Practice/backup (3): Pitfall: interpreting stratum-specific association as causal without identification** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 46. **L04 Practice/backup (3): Visualization: forest plot with RD and RR side-by-side** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 47. **L04 Practice/backup (3): Optional: additive interaction measures (RERI) as enrichment (clearly labeled optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 48. **L04 Practice/backup (4): Worked example: effect modification by sex on RD scale** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 49. **L04 Practice/backup (4): Worked example: same data on RR scale (contrast interpretation)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 50. **L04 Practice/backup (4): Practice: interpret interaction coefficient (logistic regression)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 51. **L04 Practice/backup (4): Practice: interpret interaction coefficient (linear model)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 52. **L04 Practice/backup (4): Mini-quiz: which statement is correct? (10 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 53. **L04 Practice/backup (4): Pitfall: interpreting stratum-specific association as causal without identification** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 54. **L04 Practice/backup (4): Visualization: forest plot with RD and RR side-by-side** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 55. **L04 Practice/backup (4): Optional: additive interaction measures (RERI) as enrichment (clearly labeled optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 56. **L04 Practice/backup (5): Worked example: effect modification by sex on RD scale** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 57. **L04 Practice/backup (5): Worked example: same data on RR scale (contrast interpretation)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 58. **L04 Practice/backup (5): Practice: interpret interaction coefficient (logistic regression)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 59. **L04 Practice/backup (5): Practice: interpret interaction coefficient (linear model)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 60. **L04 Practice/backup (5): Mini-quiz: which statement is correct? (10 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 61. **L04 Practice/backup (5): Pitfall: interpreting stratum-specific association as causal without identification** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 62. **L04 Practice/backup (5): Visualization: forest plot with RD and RR side-by-side** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 63. **L04 Practice/backup (5): Optional: additive interaction measures (RERI) as enrichment (clearly labeled optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 64. **L04 Practice/backup (6): Worked example: effect modification by sex on RD scale** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 65. **L04 Practice/backup (6): Worked example: same data on RR scale (contrast interpretation)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 66. **L04 Practice/backup (6): Practice: interpret interaction coefficient (logistic regression)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 67. **L04 Practice/backup (6): Practice: interpret interaction coefficient (linear model)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 68. **L04 Practice/backup (6): Mini-quiz: which statement is correct? (10 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).

## L05 — Causal diagrams (DAGs), d-separation, and collider bias
**Target duration:** 110–120 min  
**Target slides:** 78–82

### Foundations (Slides 1–10)
- 01. **Title** — Key: Causal diagrams (DAGs), d-separation, and collider bias — Visual: None
- 02. **Why DAGs** — Key: make assumptions explicit — Visual: Draw (vector): assumptions→DAG
- 03. **DAG basics** — Key: nodes/edges; causal meaning — Visual: Draw (vector): annotated DAG
- 04. **Paths & associations** — Key: open vs blocked paths — Visual: Draw (vector): path highlight
- 05. **Three structures** — Key: chain/fork/collider — Visual: Draw (vector): 3 mini-DAGs
- 06. **d-separation: chain** — Key: conditioning blocks — Visual: Draw (vector): chain blocked
- 07. **d-separation: fork** — Key: conditioning blocks confounding — Visual: Draw (vector): fork blocked
- 08. **d-separation: collider** — Key: conditioning opens — Visual: Draw (vector): collider opened
- 09. **Backdoor intuition** — Key: noncausal paths from A to Y — Visual: Draw (vector): backdoor highlight
- 10. **(Pause/Activity) collider identification drill** — Key: 3 DAGs; vote — Visual: Draw (vector): practice DAGs — Notes: 8 min

### Practice DAGs with answers (Slides 11–26)
- 11. **DAG practice: confounding** — Key: A←L→Y; choose adjustment — Visual: Draw (vector): DAG; highlight paths — Notes: Ask for adjustment set
- 12. **DAG practice: confounding — Answer** — Key: open/closed paths; valid sets — Visual: Draw (vector): annotated DAG — Notes: 1–2 min
- 13. **DAG practice: mediator** — Key: A→M→Y; total vs direct effect — Visual: Draw (vector): DAG; highlight paths — Notes: Ask for adjustment set
- 14. **DAG practice: mediator — Answer** — Key: open/closed paths; valid sets — Visual: Draw (vector): annotated DAG — Notes: 1–2 min
- 15. **DAG practice: collider** — Key: A→S←Y; conditioning effect — Visual: Draw (vector): DAG; highlight paths — Notes: Ask for adjustment set
- 16. **DAG practice: collider — Answer** — Key: open/closed paths; valid sets — Visual: Draw (vector): annotated DAG — Notes: 1–2 min
- 17. **DAG practice: selection bias** — Key: conditioning on S in cohort — Visual: Draw (vector): DAG; highlight paths — Notes: Ask for adjustment set
- 18. **DAG practice: selection bias — Answer** — Key: open/closed paths; valid sets — Visual: Draw (vector): annotated DAG — Notes: 1–2 min
- 19. **DAG practice: M-bias** — Key: conditioning on S opens U-path — Visual: Draw (vector): DAG; highlight paths — Notes: Ask for adjustment set
- 20. **DAG practice: M-bias — Answer** — Key: open/closed paths; valid sets — Visual: Draw (vector): annotated DAG — Notes: 1–2 min
- 21. **DAG practice: instrument** — Key: Z→A→Y; what to adjust? — Visual: Draw (vector): DAG; highlight paths — Notes: Ask for adjustment set
- 22. **DAG practice: instrument — Answer** — Key: open/closed paths; valid sets — Visual: Draw (vector): annotated DAG — Notes: 1–2 min
- 23. **DAG practice: competing exposure** — Key: A←L→B→Y; minimal adjustment — Visual: Draw (vector): DAG; highlight paths — Notes: Ask for adjustment set
- 24. **DAG practice: competing exposure — Answer** — Key: open/closed paths; valid sets — Visual: Draw (vector): annotated DAG — Notes: 1–2 min
- 25. **DAG practice: measurement error** — Key: L* measured; implications — Visual: Draw (vector): DAG; highlight paths — Notes: Ask for adjustment set
- 26. **DAG practice: measurement error — Answer** — Key: open/closed paths; valid sets — Visual: Draw (vector): annotated DAG — Notes: 1–2 min

### Adjustment + project work (Slides 27–33)
- 27. **Adjustment sets cheat-sheet** — Key: block backdoor; avoid colliders — Visual: Draw (vector): rule summary
- 28. **Overadjustment bias** — Key: mediator/descendant of collider — Visual: Draw (vector): warning DAG
- 29. **From DAG to analysis plan** — Key: define L for models/weights — Visual: Draw (vector): mapping
- 30. **(Pause/Activity) Your project DAG workshop** — Key: teams sketch DAG + adjustment set — Visual: Prompt-only + blank DAG — Notes: 10 min
- 31. **Common mistakes** — Key: conditioning on descendants; forgetting time order — Visual: Draw (vector): mistakes list
- 32. **Homework: DAG + justification** — Key: deliverable template — Visual: Draw (vector): template
- 33. **Reading** — Key: What If DAG chapter — Visual: None

### Practice/backup (Slides 34–82)
- 34. **L05 Practice/backup: More DAG drills: identify adjustment set (8 additional DAGs)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 35. **L05 Practice/backup: Mini-quiz: d-separation true/false (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 36. **L05 Practice/backup: Pitfall set: adjusting for colliders in EHR studies** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 37. **L05 Practice/backup: Pitfall set: conditioning on diagnosis codes that are consequences of A** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 38. **L05 Practice/backup: Visualization: 'open path' highlighting animation frames (static equivalents)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 39. **L05 Practice/backup: Optional: front-door intuition (clearly labeled optional; no do-calculus)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 40. **L05 Practice/backup (2): More DAG drills: identify adjustment set (8 additional DAGs)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 41. **L05 Practice/backup (2): Mini-quiz: d-separation true/false (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 42. **L05 Practice/backup (2): Pitfall set: adjusting for colliders in EHR studies** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 43. **L05 Practice/backup (2): Pitfall set: conditioning on diagnosis codes that are consequences of A** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 44. **L05 Practice/backup (2): Visualization: 'open path' highlighting animation frames (static equivalents)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 45. **L05 Practice/backup (2): Optional: front-door intuition (clearly labeled optional; no do-calculus)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 46. **L05 Practice/backup (3): More DAG drills: identify adjustment set (8 additional DAGs)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 47. **L05 Practice/backup (3): Mini-quiz: d-separation true/false (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 48. **L05 Practice/backup (3): Pitfall set: adjusting for colliders in EHR studies** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 49. **L05 Practice/backup (3): Pitfall set: conditioning on diagnosis codes that are consequences of A** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 50. **L05 Practice/backup (3): Visualization: 'open path' highlighting animation frames (static equivalents)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 51. **L05 Practice/backup (3): Optional: front-door intuition (clearly labeled optional; no do-calculus)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 52. **L05 Practice/backup (4): More DAG drills: identify adjustment set (8 additional DAGs)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 53. **L05 Practice/backup (4): Mini-quiz: d-separation true/false (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 54. **L05 Practice/backup (4): Pitfall set: adjusting for colliders in EHR studies** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 55. **L05 Practice/backup (4): Pitfall set: conditioning on diagnosis codes that are consequences of A** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 56. **L05 Practice/backup (4): Visualization: 'open path' highlighting animation frames (static equivalents)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 57. **L05 Practice/backup (4): Optional: front-door intuition (clearly labeled optional; no do-calculus)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 58. **L05 Practice/backup (5): More DAG drills: identify adjustment set (8 additional DAGs)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 59. **L05 Practice/backup (5): Mini-quiz: d-separation true/false (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 60. **L05 Practice/backup (5): Pitfall set: adjusting for colliders in EHR studies** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 61. **L05 Practice/backup (5): Pitfall set: conditioning on diagnosis codes that are consequences of A** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 62. **L05 Practice/backup (5): Visualization: 'open path' highlighting animation frames (static equivalents)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 63. **L05 Practice/backup (5): Optional: front-door intuition (clearly labeled optional; no do-calculus)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 64. **L05 Practice/backup (6): More DAG drills: identify adjustment set (8 additional DAGs)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 65. **L05 Practice/backup (6): Mini-quiz: d-separation true/false (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 66. **L05 Practice/backup (6): Pitfall set: adjusting for colliders in EHR studies** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 67. **L05 Practice/backup (6): Pitfall set: conditioning on diagnosis codes that are consequences of A** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 68. **L05 Practice/backup (6): Visualization: 'open path' highlighting animation frames (static equivalents)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 69. **L05 Practice/backup (6): Optional: front-door intuition (clearly labeled optional; no do-calculus)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 70. **L05 Practice/backup (7): More DAG drills: identify adjustment set (8 additional DAGs)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 71. **L05 Practice/backup (7): Mini-quiz: d-separation true/false (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 72. **L05 Practice/backup (7): Pitfall set: adjusting for colliders in EHR studies** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 73. **L05 Practice/backup (7): Pitfall set: conditioning on diagnosis codes that are consequences of A** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 74. **L05 Practice/backup (7): Visualization: 'open path' highlighting animation frames (static equivalents)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 75. **L05 Practice/backup (7): Optional: front-door intuition (clearly labeled optional; no do-calculus)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 76. **L05 Practice/backup (8): More DAG drills: identify adjustment set (8 additional DAGs)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 77. **L05 Practice/backup (8): Mini-quiz: d-separation true/false (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 78. **L05 Practice/backup (8): Pitfall set: adjusting for colliders in EHR studies** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 79. **L05 Practice/backup (8): Pitfall set: conditioning on diagnosis codes that are consequences of A** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 80. **L05 Practice/backup (8): Visualization: 'open path' highlighting animation frames (static equivalents)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 81. **L05 Practice/backup (8): Optional: front-door intuition (clearly labeled optional; no do-calculus)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 82. **L05 Practice/backup (9): More DAG drills: identify adjustment set (8 additional DAGs)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).

## L06 — Confounding: definition, confounders, and adjustment strategies
**Target duration:** 105–115 min  
**Target slides:** 72–78

### Core concepts + methods (Slides 1–11)
- 01. **Title** — Key: Confounding: definition, confounders, and adjustment strategies — Visual: None
- 02. **Confounding (counterfactual definition)** — Key: E[Y^a|A] ≠ E[Y^a] — Visual: Equation (vector)
- 03. **Role taxonomy** — Key: confounder/mediator/collider/instrument/proxy — Visual: Draw (vector): role table
- 04. **Selecting variables: DAG-first** — Key: minimal sufficient adjustment set — Visual: Draw (vector): DAG→set
- 05. **Adjustment methods map** — Key: stratify/regress/match/weight — Visual: Draw (vector): grid
- 06. **Stratification (toy)** — Key: compute within strata — Visual: Draw (vector): table
- 07. **Standardization recap** — Key: average stratum-specific risks — Visual: Draw (vector): weights
- 08. **Regression adjustment** — Key: model E[Y|A,L] and predict — Visual: Draw (vector): model→predict
- 09. **Matching** — Key: pairs/sets; check balance — Visual: Draw (vector): matching schematic
- 10. **Propensity score (preview)** — Key: e(L)=Pr(A=1|L) — Visual: Formula tile
- 11. **(Pause/Activity) choose adjustment set** — Key: given DAG; teams decide — Visual: Draw (vector): DAG — Notes: 7 min

### Pitfalls + wrap (Slides 12–22)
- 12. **When adjustment harms** — Key: collider/mediator/positivity — Visual: Draw (vector): warning list
- 13. **Overadjustment example** — Key: A→M→Y; total effect bias — Visual: Draw (vector): mediator DAG
- 14. **Instrument adjustment caution** — Key: adjusting Z may amplify bias — Visual: Draw (vector): IV DAG
- 15. **Practical timeline check** — Key: pre vs post exposure variables — Visual: Draw (vector): timeline bins
- 16. **Balance is the goal** — Key: compare groups after adjustment — Visual: Draw (vector): balance scale
- 17. **Summary** — Key: confounding + method choices — Visual: None
- 18. **Homework: compare methods** — Key: regression vs stratification on toy data — Visual: From notebook placeholder: figures/L06/hw_compare.png
- 19. **Homework: DAG justification memo** — Key: ½ page — Visual: Draw (vector): rubric mini-grid
- 20. **Reading** — Key: What If confounding sections — Visual: None
- 21. **Exit ticket** — Key: one confounder vs mediator example — Visual: Prompt-only — Notes: 2 min
- 22. **Backup: checklist** — Key: what to report in adjusted analysis — Visual: Draw (vector)

### Practice/backup (Slides 23–78)
- 23. **L06 Practice/backup: Worked example: age confounding — stratification then standardization** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 24. **L06 Practice/backup: Worked example: same data — regression plug-in** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 25. **L06 Practice/backup: Worked example: matching concept + balance check** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 26. **L06 Practice/backup: Mini-quiz: role classification (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 27. **L06 Practice/backup: Pitfall: adjusting for baseline collider created by sampling** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 28. **L06 Practice/backup: Visualization: SMD concept (before/after) (vector)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 29. **L06 Practice/backup: Optional: doubly robust intuition (label optional; no deep theory)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 30. **L06 Practice/backup (2): Worked example: age confounding — stratification then standardization** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 31. **L06 Practice/backup (2): Worked example: same data — regression plug-in** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 32. **L06 Practice/backup (2): Worked example: matching concept + balance check** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 33. **L06 Practice/backup (2): Mini-quiz: role classification (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 34. **L06 Practice/backup (2): Pitfall: adjusting for baseline collider created by sampling** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 35. **L06 Practice/backup (2): Visualization: SMD concept (before/after) (vector)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 36. **L06 Practice/backup (2): Optional: doubly robust intuition (label optional; no deep theory)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 37. **L06 Practice/backup (3): Worked example: age confounding — stratification then standardization** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 38. **L06 Practice/backup (3): Worked example: same data — regression plug-in** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 39. **L06 Practice/backup (3): Worked example: matching concept + balance check** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 40. **L06 Practice/backup (3): Mini-quiz: role classification (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 41. **L06 Practice/backup (3): Pitfall: adjusting for baseline collider created by sampling** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 42. **L06 Practice/backup (3): Visualization: SMD concept (before/after) (vector)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 43. **L06 Practice/backup (3): Optional: doubly robust intuition (label optional; no deep theory)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 44. **L06 Practice/backup (4): Worked example: age confounding — stratification then standardization** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 45. **L06 Practice/backup (4): Worked example: same data — regression plug-in** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 46. **L06 Practice/backup (4): Worked example: matching concept + balance check** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 47. **L06 Practice/backup (4): Mini-quiz: role classification (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 48. **L06 Practice/backup (4): Pitfall: adjusting for baseline collider created by sampling** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 49. **L06 Practice/backup (4): Visualization: SMD concept (before/after) (vector)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 50. **L06 Practice/backup (4): Optional: doubly robust intuition (label optional; no deep theory)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 51. **L06 Practice/backup (5): Worked example: age confounding — stratification then standardization** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 52. **L06 Practice/backup (5): Worked example: same data — regression plug-in** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 53. **L06 Practice/backup (5): Worked example: matching concept + balance check** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 54. **L06 Practice/backup (5): Mini-quiz: role classification (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 55. **L06 Practice/backup (5): Pitfall: adjusting for baseline collider created by sampling** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 56. **L06 Practice/backup (5): Visualization: SMD concept (before/after) (vector)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 57. **L06 Practice/backup (5): Optional: doubly robust intuition (label optional; no deep theory)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 58. **L06 Practice/backup (6): Worked example: age confounding — stratification then standardization** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 59. **L06 Practice/backup (6): Worked example: same data — regression plug-in** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 60. **L06 Practice/backup (6): Worked example: matching concept + balance check** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 61. **L06 Practice/backup (6): Mini-quiz: role classification (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 62. **L06 Practice/backup (6): Pitfall: adjusting for baseline collider created by sampling** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 63. **L06 Practice/backup (6): Visualization: SMD concept (before/after) (vector)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 64. **L06 Practice/backup (6): Optional: doubly robust intuition (label optional; no deep theory)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 65. **L06 Practice/backup (7): Worked example: age confounding — stratification then standardization** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 66. **L06 Practice/backup (7): Worked example: same data — regression plug-in** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 67. **L06 Practice/backup (7): Worked example: matching concept + balance check** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 68. **L06 Practice/backup (7): Mini-quiz: role classification (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 69. **L06 Practice/backup (7): Pitfall: adjusting for baseline collider created by sampling** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 70. **L06 Practice/backup (7): Visualization: SMD concept (before/after) (vector)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 71. **L06 Practice/backup (7): Optional: doubly robust intuition (label optional; no deep theory)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 72. **L06 Practice/backup (8): Worked example: age confounding — stratification then standardization** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 73. **L06 Practice/backup (8): Worked example: same data — regression plug-in** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 74. **L06 Practice/backup (8): Worked example: matching concept + balance check** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 75. **L06 Practice/backup (8): Mini-quiz: role classification (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 76. **L06 Practice/backup (8): Pitfall: adjusting for baseline collider created by sampling** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 77. **L06 Practice/backup (8): Visualization: SMD concept (before/after) (vector)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 78. **L06 Practice/backup (8): Optional: doubly robust intuition (label optional; no deep theory)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).

## L07 — Selection bias (structure and adjustment)
**Target duration:** 100–110 min  
**Target slides:** 68–74

### Core selection bias + IPCW (Slides 1–10)
- 01. **Title** — Key: Selection bias (structure and adjustment) — Visual: None
- 02. **Selection as collider bias** — Key: conditioning on S opens path — Visual: Draw (vector): A→S←Y
- 03. **Examples** — Key: loss to follow-up; ICU admission; complete-case — Visual: Draw (vector): 3 tiles
- 04. **DAG: dropout depends on L and Y** — Key: bias direction intuition — Visual: Draw (vector): DAG
- 05. **Censoring notation** — Key: C=0 observed — Visual: Draw (vector): legend
- 06. **IPCW intuition** — Key: reweight observed to full cohort — Visual: Draw (vector): reweighting
- 07. **IPCW steps** — Key: fit Pr(C=0|history) → weights → analysis — Visual: Draw (vector): pipeline
- 08. **Weight diagnostics** — Key: hist; tail; truncation — Visual: From notebook: figures/L07/ipcw_weights.png
- 09. **Stabilized censoring weights** — Key: reduce variance — Visual: Formula tile
- 10. **(Pause/Activity) identify S and its causes** — Key: teams label selection mechanism — Visual: Prompt-only — Notes: 7 min

### Missingness + wrap (Slides 11–18)
- 11. **MCAR/MAR/MNAR (brief)** — Key: conceptual; link to DAGs — Visual: Draw (vector): tiles
- 12. **Complete-case bias** — Key: when selection depends on Y or causes — Visual: Draw (vector): warning
- 13. **Sensitivity framing** — Key: what-if selection stronger? — Visual: Draw (vector): sensitivity dial
- 14. **Summary** — Key: selection bias + IPCW — Visual: None
- 15. **Homework: IPCW on toy data** — Key: compute; diagnose; estimate effect — Visual: From notebook placeholder: figures/L07/hw_ipcw.png
- 16. **Homework: DAG + assumption check** — Key: write-up — Visual: Draw (vector): rubric mini-grid
- 17. **Reading** — Key: What If selection bias sections — Visual: None
- 18. **Exit ticket** — Key: one selection bias example — Visual: Prompt-only — Notes: 2 min

### Practice/backup (Slides 19–74)
- 19. **L07 Practice/backup: Worked example: loss to follow-up in an RCT (what remains unbiased?)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 20. **L07 Practice/backup: Worked example: selection into ICU (Berkson-like)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 21. **L07 Practice/backup: Practice: build censoring model covariate list** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 22. **L07 Practice/backup: Practice: interpret weight histogram and choose truncation** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 23. **L07 Practice/backup: Mini-quiz: MCAR/MAR/MNAR classification (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 24. **L07 Practice/backup: Pitfall: conditioning on missingness indicator as covariate** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 25. **L07 Practice/backup: Optional: multiple imputation vs IPCW (high-level comparison)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 26. **L07 Practice/backup (2): Worked example: loss to follow-up in an RCT (what remains unbiased?)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 27. **L07 Practice/backup (2): Worked example: selection into ICU (Berkson-like)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 28. **L07 Practice/backup (2): Practice: build censoring model covariate list** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 29. **L07 Practice/backup (2): Practice: interpret weight histogram and choose truncation** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 30. **L07 Practice/backup (2): Mini-quiz: MCAR/MAR/MNAR classification (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 31. **L07 Practice/backup (2): Pitfall: conditioning on missingness indicator as covariate** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 32. **L07 Practice/backup (2): Optional: multiple imputation vs IPCW (high-level comparison)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 33. **L07 Practice/backup (3): Worked example: loss to follow-up in an RCT (what remains unbiased?)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 34. **L07 Practice/backup (3): Worked example: selection into ICU (Berkson-like)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 35. **L07 Practice/backup (3): Practice: build censoring model covariate list** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 36. **L07 Practice/backup (3): Practice: interpret weight histogram and choose truncation** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 37. **L07 Practice/backup (3): Mini-quiz: MCAR/MAR/MNAR classification (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 38. **L07 Practice/backup (3): Pitfall: conditioning on missingness indicator as covariate** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 39. **L07 Practice/backup (3): Optional: multiple imputation vs IPCW (high-level comparison)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 40. **L07 Practice/backup (4): Worked example: loss to follow-up in an RCT (what remains unbiased?)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 41. **L07 Practice/backup (4): Worked example: selection into ICU (Berkson-like)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 42. **L07 Practice/backup (4): Practice: build censoring model covariate list** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 43. **L07 Practice/backup (4): Practice: interpret weight histogram and choose truncation** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 44. **L07 Practice/backup (4): Mini-quiz: MCAR/MAR/MNAR classification (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 45. **L07 Practice/backup (4): Pitfall: conditioning on missingness indicator as covariate** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 46. **L07 Practice/backup (4): Optional: multiple imputation vs IPCW (high-level comparison)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 47. **L07 Practice/backup (5): Worked example: loss to follow-up in an RCT (what remains unbiased?)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 48. **L07 Practice/backup (5): Worked example: selection into ICU (Berkson-like)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 49. **L07 Practice/backup (5): Practice: build censoring model covariate list** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 50. **L07 Practice/backup (5): Practice: interpret weight histogram and choose truncation** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 51. **L07 Practice/backup (5): Mini-quiz: MCAR/MAR/MNAR classification (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 52. **L07 Practice/backup (5): Pitfall: conditioning on missingness indicator as covariate** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 53. **L07 Practice/backup (5): Optional: multiple imputation vs IPCW (high-level comparison)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 54. **L07 Practice/backup (6): Worked example: loss to follow-up in an RCT (what remains unbiased?)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 55. **L07 Practice/backup (6): Worked example: selection into ICU (Berkson-like)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 56. **L07 Practice/backup (6): Practice: build censoring model covariate list** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 57. **L07 Practice/backup (6): Practice: interpret weight histogram and choose truncation** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 58. **L07 Practice/backup (6): Mini-quiz: MCAR/MAR/MNAR classification (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 59. **L07 Practice/backup (6): Pitfall: conditioning on missingness indicator as covariate** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 60. **L07 Practice/backup (6): Optional: multiple imputation vs IPCW (high-level comparison)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 61. **L07 Practice/backup (7): Worked example: loss to follow-up in an RCT (what remains unbiased?)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 62. **L07 Practice/backup (7): Worked example: selection into ICU (Berkson-like)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 63. **L07 Practice/backup (7): Practice: build censoring model covariate list** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 64. **L07 Practice/backup (7): Practice: interpret weight histogram and choose truncation** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 65. **L07 Practice/backup (7): Mini-quiz: MCAR/MAR/MNAR classification (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 66. **L07 Practice/backup (7): Pitfall: conditioning on missingness indicator as covariate** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 67. **L07 Practice/backup (7): Optional: multiple imputation vs IPCW (high-level comparison)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 68. **L07 Practice/backup (8): Worked example: loss to follow-up in an RCT (what remains unbiased?)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 69. **L07 Practice/backup (8): Worked example: selection into ICU (Berkson-like)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 70. **L07 Practice/backup (8): Practice: build censoring model covariate list** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 71. **L07 Practice/backup (8): Practice: interpret weight histogram and choose truncation** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 72. **L07 Practice/backup (8): Mini-quiz: MCAR/MAR/MNAR classification (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 73. **L07 Practice/backup (8): Pitfall: conditioning on missingness indicator as covariate** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 74. **L07 Practice/backup (8): Optional: multiple imputation vs IPCW (high-level comparison)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).

## L08 — Why model? (estimators, models, bias-variance tradeoff)
**Target duration:** 90–100 min  
**Target slides:** 60–66

### Core modeling ideas (Slides 1–9)
- 01. **Title** — Key: Why model? (estimators, models, bias–variance tradeoff) — Visual: None
- 02. **Estimator vs model vs estimand** — Key: definitions — Visual: Draw (vector): three boxes
- 03. **Plug-in estimators** — Key: model → predict under A=1 and A=0 — Visual: Draw (vector): pipeline
- 04. **Bias–variance tradeoff** — Key: under/overfit — Visual: From notebook: figures/L08/bias_variance.png
- 05. **Misspecification demo** — Key: wrong functional form changes effect estimate — Visual: From notebook: figures/L08/misspecification_demo.png
- 06. **Parametric vs flexible models** — Key: tradeoffs; interpretability — Visual: Draw (vector): slider
- 07. **Bootstrap for uncertainty** — Key: steps — Visual: Draw (vector): bootstrap loop
- 08. **Robust SE (concept)** — Key: why with weights — Visual: Draw (vector): sandwich icon
- 09. **(Pause/Activity) propose a model + checks** — Key: teams specify model and diagnostics — Visual: Prompt-only — Notes: 8 min

### Wrap + homework (Slides 10–15)
- 10. **Model checks you must do** — Key: calibration; residuals; extrapolation — Visual: Draw (vector): checklist
- 11. **When modeling fails** — Key: positivity violations → extrapolation — Visual: Draw (vector): warning
- 12. **Summary** — Key: models as tools; not truth — Visual: None
- 13. **Homework: simulate misspecification impact** — Key: compare models — Visual: From notebook placeholder: figures/L08/hw_mis.png
- 14. **Homework: write model-check plan** — Key: for your project — Visual: Draw (vector): template
- 15. **Reading** — Key: short notes + What If modeling sections — Visual: None

### Practice/backup (Slides 16–66)
- 16. **L08 Practice/backup: Worked example: logistic vs linear probability model (interpretation)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 17. **L08 Practice/backup: Practice: choose transformations (age spline vs linear) — concept** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 18. **L08 Practice/backup: Practice: interpret a calibration plot** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 19. **L08 Practice/backup: Mini-quiz: identify overfitting and extrapolation (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 20. **L08 Practice/backup: Pitfall: interpreting p-values as causal evidence** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 21. **L08 Practice/backup: Optional: cross-fitting / sample splitting (concept; optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 22. **L08 Practice/backup (2): Worked example: logistic vs linear probability model (interpretation)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 23. **L08 Practice/backup (2): Practice: choose transformations (age spline vs linear) — concept** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 24. **L08 Practice/backup (2): Practice: interpret a calibration plot** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 25. **L08 Practice/backup (2): Mini-quiz: identify overfitting and extrapolation (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 26. **L08 Practice/backup (2): Pitfall: interpreting p-values as causal evidence** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 27. **L08 Practice/backup (2): Optional: cross-fitting / sample splitting (concept; optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 28. **L08 Practice/backup (3): Worked example: logistic vs linear probability model (interpretation)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 29. **L08 Practice/backup (3): Practice: choose transformations (age spline vs linear) — concept** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 30. **L08 Practice/backup (3): Practice: interpret a calibration plot** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 31. **L08 Practice/backup (3): Mini-quiz: identify overfitting and extrapolation (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 32. **L08 Practice/backup (3): Pitfall: interpreting p-values as causal evidence** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 33. **L08 Practice/backup (3): Optional: cross-fitting / sample splitting (concept; optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 34. **L08 Practice/backup (4): Worked example: logistic vs linear probability model (interpretation)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 35. **L08 Practice/backup (4): Practice: choose transformations (age spline vs linear) — concept** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 36. **L08 Practice/backup (4): Practice: interpret a calibration plot** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 37. **L08 Practice/backup (4): Mini-quiz: identify overfitting and extrapolation (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 38. **L08 Practice/backup (4): Pitfall: interpreting p-values as causal evidence** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 39. **L08 Practice/backup (4): Optional: cross-fitting / sample splitting (concept; optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 40. **L08 Practice/backup (5): Worked example: logistic vs linear probability model (interpretation)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 41. **L08 Practice/backup (5): Practice: choose transformations (age spline vs linear) — concept** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 42. **L08 Practice/backup (5): Practice: interpret a calibration plot** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 43. **L08 Practice/backup (5): Mini-quiz: identify overfitting and extrapolation (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 44. **L08 Practice/backup (5): Pitfall: interpreting p-values as causal evidence** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 45. **L08 Practice/backup (5): Optional: cross-fitting / sample splitting (concept; optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 46. **L08 Practice/backup (6): Worked example: logistic vs linear probability model (interpretation)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 47. **L08 Practice/backup (6): Practice: choose transformations (age spline vs linear) — concept** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 48. **L08 Practice/backup (6): Practice: interpret a calibration plot** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 49. **L08 Practice/backup (6): Mini-quiz: identify overfitting and extrapolation (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 50. **L08 Practice/backup (6): Pitfall: interpreting p-values as causal evidence** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 51. **L08 Practice/backup (6): Optional: cross-fitting / sample splitting (concept; optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 52. **L08 Practice/backup (7): Worked example: logistic vs linear probability model (interpretation)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 53. **L08 Practice/backup (7): Practice: choose transformations (age spline vs linear) — concept** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 54. **L08 Practice/backup (7): Practice: interpret a calibration plot** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 55. **L08 Practice/backup (7): Mini-quiz: identify overfitting and extrapolation (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 56. **L08 Practice/backup (7): Pitfall: interpreting p-values as causal evidence** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 57. **L08 Practice/backup (7): Optional: cross-fitting / sample splitting (concept; optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 58. **L08 Practice/backup (8): Worked example: logistic vs linear probability model (interpretation)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 59. **L08 Practice/backup (8): Practice: choose transformations (age spline vs linear) — concept** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 60. **L08 Practice/backup (8): Practice: interpret a calibration plot** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 61. **L08 Practice/backup (8): Mini-quiz: identify overfitting and extrapolation (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 62. **L08 Practice/backup (8): Pitfall: interpreting p-values as causal evidence** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 63. **L08 Practice/backup (8): Optional: cross-fitting / sample splitting (concept; optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 64. **L08 Practice/backup (9): Worked example: logistic vs linear probability model (interpretation)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 65. **L08 Practice/backup (9): Practice: choose transformations (age spline vs linear) — concept** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 66. **L08 Practice/backup (9): Practice: interpret a calibration plot** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).

## L09 — Standardization and the (parametric) g-formula
**Target duration:** 105–115 min  
**Target slides:** 72–78

### Core algorithm (Slides 1–12)
- 01. **Title** — Key: Standardization and the (parametric) g-formula — Visual: None
- 02. **Goal** — Key: estimate E[Y^a] using an outcome model — Visual: Draw (vector): target box
- 03. **g-formula identification** — Key: E[Y^a]=Σ_l E[Y|A=a,L=l]P(L=l) — Visual: Equation + assumption labels
- 04. **Algorithm overview** — Key: fit → set A → predict → average → bootstrap — Visual: Draw (vector): pipeline
- 05. **Toy dataset** — Key: L,A,Y table — Visual: Draw (vector): mini table
- 06. **Step 1: fit E[Y|A,L]** — Key: model choices — Visual: Draw (vector): model box
- 07. **Step 2: create A=1 dataset** — Key: copy and set A — Visual: Draw (vector): data copy
- 08. **Step 3: predict Y under A=1** — Key: Ŷ^1 — Visual: Draw (vector): prediction arrow
- 09. **Step 4: average Ŷ^1** — Key: E[Ŷ^1] — Visual: Draw (vector): averaging
- 10. **Repeat for A=0** — Key: E[Ŷ^0] — Visual: Draw (vector): repeat
- 11. **Compute ATE** — Key: E[Ŷ^1]-E[Ŷ^0] — Visual: Formula tile
- 12. **(Pause/Activity) implement g-formula (toy)** — Key: guided coding — Visual: Prompt-only — Notes: 15 min

### Diagnostics + wrap (Slides 13–21)
- 13. **Plot: predicted risks** — Key: treated vs untreated — Visual: From notebook: figures/L09/gformula_risk.png
- 14. **Diagnostics: calibration** — Key: observed vs predicted — Visual: From notebook: figures/L09/model_check_calibration.png
- 15. **Uncertainty: bootstrap CI** — Key: procedure — Visual: Draw (vector): bootstrap loop
- 16. **Extrapolation warning** — Key: positivity failures — Visual: Draw (vector): warning
- 17. **Communication: report assumptions** — Key: what to report — Visual: Draw (vector): reporting template
- 18. **Summary** — Key: g-formula steps + pitfalls — Visual: None
- 19. **Homework: g-formula on provided dataset** — Key: deliver plots + estimate — Visual: From notebook placeholder: figures/L09/hw_output.png
- 20. **Homework: methods paragraph draft** — Key: write-up — Visual: Draw (vector): template
- 21. **Reading** — Key: What If g-formula sections — Visual: None

### Practice/backup (Slides 22–78)
- 22. **L09 Practice/backup: Worked example: choosing functional form for L (continuous)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 23. **L09 Practice/backup: Worked example: compare LPM vs logistic for binary outcomes** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 24. **L09 Practice/backup: Practice: interpret predicted risk curves and CIs** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 25. **L09 Practice/backup: Mini-quiz: match algorithm steps to formula components (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 26. **L09 Practice/backup: Pitfall: including post-treatment covariates in outcome model** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 27. **L09 Practice/backup: Pitfall: bootstrap at wrong level (rows vs individuals)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 28. **L09 Practice/backup: Optional: g-computation for continuous outcomes (brief)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 29. **L09 Practice/backup (2): Worked example: choosing functional form for L (continuous)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 30. **L09 Practice/backup (2): Worked example: compare LPM vs logistic for binary outcomes** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 31. **L09 Practice/backup (2): Practice: interpret predicted risk curves and CIs** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 32. **L09 Practice/backup (2): Mini-quiz: match algorithm steps to formula components (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 33. **L09 Practice/backup (2): Pitfall: including post-treatment covariates in outcome model** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 34. **L09 Practice/backup (2): Pitfall: bootstrap at wrong level (rows vs individuals)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 35. **L09 Practice/backup (2): Optional: g-computation for continuous outcomes (brief)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 36. **L09 Practice/backup (3): Worked example: choosing functional form for L (continuous)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 37. **L09 Practice/backup (3): Worked example: compare LPM vs logistic for binary outcomes** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 38. **L09 Practice/backup (3): Practice: interpret predicted risk curves and CIs** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 39. **L09 Practice/backup (3): Mini-quiz: match algorithm steps to formula components (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 40. **L09 Practice/backup (3): Pitfall: including post-treatment covariates in outcome model** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 41. **L09 Practice/backup (3): Pitfall: bootstrap at wrong level (rows vs individuals)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 42. **L09 Practice/backup (3): Optional: g-computation for continuous outcomes (brief)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 43. **L09 Practice/backup (4): Worked example: choosing functional form for L (continuous)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 44. **L09 Practice/backup (4): Worked example: compare LPM vs logistic for binary outcomes** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 45. **L09 Practice/backup (4): Practice: interpret predicted risk curves and CIs** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 46. **L09 Practice/backup (4): Mini-quiz: match algorithm steps to formula components (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 47. **L09 Practice/backup (4): Pitfall: including post-treatment covariates in outcome model** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 48. **L09 Practice/backup (4): Pitfall: bootstrap at wrong level (rows vs individuals)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 49. **L09 Practice/backup (4): Optional: g-computation for continuous outcomes (brief)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 50. **L09 Practice/backup (5): Worked example: choosing functional form for L (continuous)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 51. **L09 Practice/backup (5): Worked example: compare LPM vs logistic for binary outcomes** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 52. **L09 Practice/backup (5): Practice: interpret predicted risk curves and CIs** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 53. **L09 Practice/backup (5): Mini-quiz: match algorithm steps to formula components (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 54. **L09 Practice/backup (5): Pitfall: including post-treatment covariates in outcome model** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 55. **L09 Practice/backup (5): Pitfall: bootstrap at wrong level (rows vs individuals)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 56. **L09 Practice/backup (5): Optional: g-computation for continuous outcomes (brief)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 57. **L09 Practice/backup (6): Worked example: choosing functional form for L (continuous)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 58. **L09 Practice/backup (6): Worked example: compare LPM vs logistic for binary outcomes** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 59. **L09 Practice/backup (6): Practice: interpret predicted risk curves and CIs** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 60. **L09 Practice/backup (6): Mini-quiz: match algorithm steps to formula components (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 61. **L09 Practice/backup (6): Pitfall: including post-treatment covariates in outcome model** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 62. **L09 Practice/backup (6): Pitfall: bootstrap at wrong level (rows vs individuals)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 63. **L09 Practice/backup (6): Optional: g-computation for continuous outcomes (brief)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 64. **L09 Practice/backup (7): Worked example: choosing functional form for L (continuous)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 65. **L09 Practice/backup (7): Worked example: compare LPM vs logistic for binary outcomes** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 66. **L09 Practice/backup (7): Practice: interpret predicted risk curves and CIs** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 67. **L09 Practice/backup (7): Mini-quiz: match algorithm steps to formula components (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 68. **L09 Practice/backup (7): Pitfall: including post-treatment covariates in outcome model** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 69. **L09 Practice/backup (7): Pitfall: bootstrap at wrong level (rows vs individuals)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 70. **L09 Practice/backup (7): Optional: g-computation for continuous outcomes (brief)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 71. **L09 Practice/backup (8): Worked example: choosing functional form for L (continuous)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 72. **L09 Practice/backup (8): Worked example: compare LPM vs logistic for binary outcomes** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 73. **L09 Practice/backup (8): Practice: interpret predicted risk curves and CIs** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 74. **L09 Practice/backup (8): Mini-quiz: match algorithm steps to formula components (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 75. **L09 Practice/backup (8): Pitfall: including post-treatment covariates in outcome model** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 76. **L09 Practice/backup (8): Pitfall: bootstrap at wrong level (rows vs individuals)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 77. **L09 Practice/backup (8): Optional: g-computation for continuous outcomes (brief)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 78. **L09 Practice/backup (9): Worked example: choosing functional form for L (continuous)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).

## L10 — Instrumental variables (IV): when exchangeability is not plausible
**Target duration:** 105–115 min  
**Target slides:** 72–78

### Core IV setup (Slides 1–11)
- 01. **Title** — Key: Instrumental variables (IV): when exchangeability is not plausible — Visual: None
- 02. **Motivation** — Key: unmeasured confounding; why IV — Visual: Draw (vector): U→A,Y
- 03. **IV DAG** — Key: Z→A→Y with U→A,Y — Visual: Draw (vector): IV DAG
- 04. **Assumption: relevance** — Key: Z affects A — Visual: Draw (vector): highlight Z→A
- 05. **Assumption: exclusion** — Key: no Z→Y direct path — Visual: Draw (vector): forbidden arrow
- 06. **Assumption: independence** — Key: Z ⫫ U — Visual: Draw (vector): independence label
- 07. **Assumption: monotonicity** — Key: no defiers — Visual: Draw (vector): compliance types
- 08. **Compliance classes** — Key: always/never/complier/defier — Visual: Draw (vector): class diagram
- 09. **Wald estimator** — Key: ratio of reduced forms — Visual: Formula tile
- 10. **LATE interpretation** — Key: effect among compliers — Visual: Draw (vector): highlight compliers
- 11. **(Pause/Activity) critique IV candidates** — Key: teams evaluate assumptions — Visual: Prompt-only — Notes: 8 min

### Estimation + diagnostics + wrap (Slides 12–22)
- 12. **Weak instruments** — Key: bias + large SE — Visual: From notebook: figures/L10/weak_iv.png
- 13. **First-stage strength (concept)** — Key: F-statistic intuition — Visual: Draw (vector): gauge icon
- 14. **2SLS pipeline** — Key: stage 1 Â; stage 2 Y~Â — Visual: Draw (vector): two-stage boxes
- 15. **2SLS interpretation caution** — Key: depends on assumptions; LATE vs ATE — Visual: Draw (vector): caution box
- 16. **Multiple instruments (brief)** — Key: overidentification tests not proofs — Visual: Draw (vector): multiple Z
- 17. **IV vs confounding adjustment** — Key: what IV solves/doesn't — Visual: Draw (vector): comparison table
- 18. **IV + selection/censoring risk** — Key: selection can invalidate IV — Visual: Draw (vector): add S collider
- 19. **Summary** — Key: assumptions + interpretation — Visual: None
- 20. **Homework: simulate IV strength** — Key: strong vs weak Z; compare bias — Visual: From notebook placeholder: figures/L10/hw_iv_sim.png
- 21. **Homework: IV plausibility memo** — Key: write a structured critique — Visual: Draw (vector): memo template
- 22. **Reading** — Key: IV lecture notes + What If IV section — Visual: None

### Practice/backup (Slides 23–78)
- 23. **L10 Practice/backup: Worked example: compute Wald estimator from group means** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 24. **L10 Practice/backup: Practice: interpret LATE in words (3 scenarios)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 25. **L10 Practice/backup: Practice: identify exclusion violations (8 vignettes)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 26. **L10 Practice/backup: Mini-quiz: which IV assumption fails? (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 27. **L10 Practice/backup: Pitfall: using instruments that affect care pathways directly** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 28. **L10 Practice/backup: Optional: control function intuition (clearly optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 29. **L10 Practice/backup (2): Worked example: compute Wald estimator from group means** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 30. **L10 Practice/backup (2): Practice: interpret LATE in words (3 scenarios)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 31. **L10 Practice/backup (2): Practice: identify exclusion violations (8 vignettes)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 32. **L10 Practice/backup (2): Mini-quiz: which IV assumption fails? (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 33. **L10 Practice/backup (2): Pitfall: using instruments that affect care pathways directly** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 34. **L10 Practice/backup (2): Optional: control function intuition (clearly optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 35. **L10 Practice/backup (3): Worked example: compute Wald estimator from group means** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 36. **L10 Practice/backup (3): Practice: interpret LATE in words (3 scenarios)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 37. **L10 Practice/backup (3): Practice: identify exclusion violations (8 vignettes)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 38. **L10 Practice/backup (3): Mini-quiz: which IV assumption fails? (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 39. **L10 Practice/backup (3): Pitfall: using instruments that affect care pathways directly** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 40. **L10 Practice/backup (3): Optional: control function intuition (clearly optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 41. **L10 Practice/backup (4): Worked example: compute Wald estimator from group means** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 42. **L10 Practice/backup (4): Practice: interpret LATE in words (3 scenarios)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 43. **L10 Practice/backup (4): Practice: identify exclusion violations (8 vignettes)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 44. **L10 Practice/backup (4): Mini-quiz: which IV assumption fails? (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 45. **L10 Practice/backup (4): Pitfall: using instruments that affect care pathways directly** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 46. **L10 Practice/backup (4): Optional: control function intuition (clearly optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 47. **L10 Practice/backup (5): Worked example: compute Wald estimator from group means** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 48. **L10 Practice/backup (5): Practice: interpret LATE in words (3 scenarios)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 49. **L10 Practice/backup (5): Practice: identify exclusion violations (8 vignettes)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 50. **L10 Practice/backup (5): Mini-quiz: which IV assumption fails? (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 51. **L10 Practice/backup (5): Pitfall: using instruments that affect care pathways directly** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 52. **L10 Practice/backup (5): Optional: control function intuition (clearly optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 53. **L10 Practice/backup (6): Worked example: compute Wald estimator from group means** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 54. **L10 Practice/backup (6): Practice: interpret LATE in words (3 scenarios)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 55. **L10 Practice/backup (6): Practice: identify exclusion violations (8 vignettes)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 56. **L10 Practice/backup (6): Mini-quiz: which IV assumption fails? (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 57. **L10 Practice/backup (6): Pitfall: using instruments that affect care pathways directly** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 58. **L10 Practice/backup (6): Optional: control function intuition (clearly optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 59. **L10 Practice/backup (7): Worked example: compute Wald estimator from group means** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 60. **L10 Practice/backup (7): Practice: interpret LATE in words (3 scenarios)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 61. **L10 Practice/backup (7): Practice: identify exclusion violations (8 vignettes)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 62. **L10 Practice/backup (7): Mini-quiz: which IV assumption fails? (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 63. **L10 Practice/backup (7): Pitfall: using instruments that affect care pathways directly** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 64. **L10 Practice/backup (7): Optional: control function intuition (clearly optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 65. **L10 Practice/backup (8): Worked example: compute Wald estimator from group means** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 66. **L10 Practice/backup (8): Practice: interpret LATE in words (3 scenarios)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 67. **L10 Practice/backup (8): Practice: identify exclusion violations (8 vignettes)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 68. **L10 Practice/backup (8): Mini-quiz: which IV assumption fails? (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 69. **L10 Practice/backup (8): Pitfall: using instruments that affect care pathways directly** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 70. **L10 Practice/backup (8): Optional: control function intuition (clearly optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 71. **L10 Practice/backup (9): Worked example: compute Wald estimator from group means** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 72. **L10 Practice/backup (9): Practice: interpret LATE in words (3 scenarios)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 73. **L10 Practice/backup (9): Practice: identify exclusion violations (8 vignettes)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 74. **L10 Practice/backup (9): Mini-quiz: which IV assumption fails? (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 75. **L10 Practice/backup (9): Pitfall: using instruments that affect care pathways directly** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 76. **L10 Practice/backup (9): Optional: control function intuition (clearly optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 77. **L10 Practice/backup (10): Worked example: compute Wald estimator from group means** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 78. **L10 Practice/backup (10): Practice: interpret LATE in words (3 scenarios)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).

## L11 — IP weighting for confounding (propensity scores) and diagnostics
**Target duration:** 110–120 min  
**Target slides:** 78–82

### Core IPTW + diagnostics (Slides 1–13)
- 01. **Title** — Key: IP weighting for confounding (propensity scores) and diagnostics — Visual: None
- 02. **Goal of IPTW** — Key: create pseudo-population w/ exchangeability — Visual: Draw (vector): reweighting sketch
- 03. **Propensity score definition** — Key: e(L)=Pr(A=1|L) — Visual: Formula tile
- 04. **IPTW weights** — Key: w = A/e(L) + (1-A)/(1-e(L)) — Visual: Formula tile
- 05. **Stabilized weights** — Key: reduce variance — Visual: Formula tile
- 06. **Pipeline** — Key: fit PS → compute weights → diagnose → estimate — Visual: Draw (vector): pipeline
- 07. **Overlap plot** — Key: PS by treatment groups — Visual: From notebook: figures/L11/overlap.png
- 08. **Weight histogram** — Key: tails/extremes — Visual: From notebook: figures/L11/weights_hist.png
- 09. **Balance (love plot)** — Key: SMD before/after weighting — Visual: From notebook: figures/L11/love_plot.png
- 10. **Truncation/trimming** — Key: bias-variance tradeoff — Visual: Draw (vector): slider
- 11. **Weighted effect estimation** — Key: weighted mean diff or weighted regression — Visual: Draw (vector): estimator box
- 12. **Robust SE** — Key: sandwich; why needed — Visual: Draw (vector): sandwich icon
- 13. **(Pause/Activity) compute weights & balance** — Key: teams run notebook — Visual: Prompt-only — Notes: 15–18 min

### Specification + wrap (Slides 14–21)
- 14. **PS model specification tips** — Key: include confounders; avoid post-A — Visual: Draw (vector): checklist
- 15. **Common failures** — Key: extreme weights; poor overlap; wrong covariates — Visual: Draw (vector): warning list
- 16. **Reporting template** — Key: PS model + balance + effect + diagnostics — Visual: Draw (vector): template
- 17. **Summary** — Key: IPTW + diagnostics — Visual: None
- 18. **Homework: IPTW analysis** — Key: deliver overlap + love plot + effect estimate — Visual: From notebook placeholder: figures/L11/hw_results.png
- 19. **Homework: methods paragraph draft** — Key: short write-up — Visual: Draw (vector): template
- 20. **Reading** — Key: What If propensity score/IPTW sections — Visual: None
- 21. **Exit ticket** — Key: what did balance plot tell you? — Visual: Prompt-only — Notes: 2 min

### Practice/backup (Slides 22–82)
- 22. **L11 Practice/backup: Worked example: compute weights for e(L)=0.2 and e(L)=0.8** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 23. **L11 Practice/backup: Practice: interpret love plot thresholds (SMD < 0.1 rule-of-thumb)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 24. **L11 Practice/backup: Practice: choose truncation threshold and justify** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 25. **L11 Practice/backup: Mini-quiz: match diagnostic to problem (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 26. **L11 Practice/backup: Pitfall: including instruments in PS model (variance inflation)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 27. **L11 Practice/backup: Optional: matching vs weighting comparison (concept)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 28. **L11 Practice/backup (2): Worked example: compute weights for e(L)=0.2 and e(L)=0.8** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 29. **L11 Practice/backup (2): Practice: interpret love plot thresholds (SMD < 0.1 rule-of-thumb)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 30. **L11 Practice/backup (2): Practice: choose truncation threshold and justify** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 31. **L11 Practice/backup (2): Mini-quiz: match diagnostic to problem (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 32. **L11 Practice/backup (2): Pitfall: including instruments in PS model (variance inflation)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 33. **L11 Practice/backup (2): Optional: matching vs weighting comparison (concept)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 34. **L11 Practice/backup (3): Worked example: compute weights for e(L)=0.2 and e(L)=0.8** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 35. **L11 Practice/backup (3): Practice: interpret love plot thresholds (SMD < 0.1 rule-of-thumb)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 36. **L11 Practice/backup (3): Practice: choose truncation threshold and justify** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 37. **L11 Practice/backup (3): Mini-quiz: match diagnostic to problem (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 38. **L11 Practice/backup (3): Pitfall: including instruments in PS model (variance inflation)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 39. **L11 Practice/backup (3): Optional: matching vs weighting comparison (concept)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 40. **L11 Practice/backup (4): Worked example: compute weights for e(L)=0.2 and e(L)=0.8** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 41. **L11 Practice/backup (4): Practice: interpret love plot thresholds (SMD < 0.1 rule-of-thumb)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 42. **L11 Practice/backup (4): Practice: choose truncation threshold and justify** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 43. **L11 Practice/backup (4): Mini-quiz: match diagnostic to problem (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 44. **L11 Practice/backup (4): Pitfall: including instruments in PS model (variance inflation)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 45. **L11 Practice/backup (4): Optional: matching vs weighting comparison (concept)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 46. **L11 Practice/backup (5): Worked example: compute weights for e(L)=0.2 and e(L)=0.8** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 47. **L11 Practice/backup (5): Practice: interpret love plot thresholds (SMD < 0.1 rule-of-thumb)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 48. **L11 Practice/backup (5): Practice: choose truncation threshold and justify** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 49. **L11 Practice/backup (5): Mini-quiz: match diagnostic to problem (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 50. **L11 Practice/backup (5): Pitfall: including instruments in PS model (variance inflation)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 51. **L11 Practice/backup (5): Optional: matching vs weighting comparison (concept)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 52. **L11 Practice/backup (6): Worked example: compute weights for e(L)=0.2 and e(L)=0.8** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 53. **L11 Practice/backup (6): Practice: interpret love plot thresholds (SMD < 0.1 rule-of-thumb)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 54. **L11 Practice/backup (6): Practice: choose truncation threshold and justify** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 55. **L11 Practice/backup (6): Mini-quiz: match diagnostic to problem (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 56. **L11 Practice/backup (6): Pitfall: including instruments in PS model (variance inflation)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 57. **L11 Practice/backup (6): Optional: matching vs weighting comparison (concept)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 58. **L11 Practice/backup (7): Worked example: compute weights for e(L)=0.2 and e(L)=0.8** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 59. **L11 Practice/backup (7): Practice: interpret love plot thresholds (SMD < 0.1 rule-of-thumb)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 60. **L11 Practice/backup (7): Practice: choose truncation threshold and justify** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 61. **L11 Practice/backup (7): Mini-quiz: match diagnostic to problem (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 62. **L11 Practice/backup (7): Pitfall: including instruments in PS model (variance inflation)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 63. **L11 Practice/backup (7): Optional: matching vs weighting comparison (concept)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 64. **L11 Practice/backup (8): Worked example: compute weights for e(L)=0.2 and e(L)=0.8** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 65. **L11 Practice/backup (8): Practice: interpret love plot thresholds (SMD < 0.1 rule-of-thumb)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 66. **L11 Practice/backup (8): Practice: choose truncation threshold and justify** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 67. **L11 Practice/backup (8): Mini-quiz: match diagnostic to problem (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 68. **L11 Practice/backup (8): Pitfall: including instruments in PS model (variance inflation)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 69. **L11 Practice/backup (8): Optional: matching vs weighting comparison (concept)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 70. **L11 Practice/backup (9): Worked example: compute weights for e(L)=0.2 and e(L)=0.8** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 71. **L11 Practice/backup (9): Practice: interpret love plot thresholds (SMD < 0.1 rule-of-thumb)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 72. **L11 Practice/backup (9): Practice: choose truncation threshold and justify** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 73. **L11 Practice/backup (9): Mini-quiz: match diagnostic to problem (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 74. **L11 Practice/backup (9): Pitfall: including instruments in PS model (variance inflation)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 75. **L11 Practice/backup (9): Optional: matching vs weighting comparison (concept)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 76. **L11 Practice/backup (10): Worked example: compute weights for e(L)=0.2 and e(L)=0.8** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 77. **L11 Practice/backup (10): Practice: interpret love plot thresholds (SMD < 0.1 rule-of-thumb)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 78. **L11 Practice/backup (10): Practice: choose truncation threshold and justify** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 79. **L11 Practice/backup (10): Mini-quiz: match diagnostic to problem (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 80. **L11 Practice/backup (10): Pitfall: including instruments in PS model (variance inflation)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 81. **L11 Practice/backup (10): Optional: matching vs weighting comparison (concept)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 82. **L11 Practice/backup (11): Worked example: compute weights for e(L)=0.2 and e(L)=0.8** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).

## L12 — Capstone: marginal structural models, target trial emulation, and time-to-event outcomes
**Target duration:** 115–120 min  
**Target slides:** 80–86

### Module A — MSM (Slides 1–12)
- 01. **Title** — Key: Capstone: MSM, target trial emulation, and time-to-event outcomes — Visual: None
- 02. **Capstone roadmap** — Key: MSM → target trial → survival — Visual: Draw (vector): 3-module bar
- 03. **Why time-varying confounding** — Key: severity both affects and is affected by treatment — Visual: Draw (vector): timeline + severity
- 04. **Longitudinal notation** — Key: L_t, A_t, C_t, Y — Visual: Draw (vector): legend
- 05. **Time-varying DAG** — Key: L_t affected by A_{t-1} and affects A_t and Y — Visual: Draw (vector): longitudinal DAG
- 06. **Why naive regression fails** — Key: adjusting for L_t induces bias — Visual: Draw (vector): bias pathway highlight
- 07. **MSM idea** — Key: weighted pseudo-population at each time — Visual: Draw (vector): pseudo-population
- 08. **Treatment weights (concept)** — Key: product of probabilities — Visual: Formula (minimal)
- 09. **Diagnostics: longitudinal weights** — Key: tail behavior over time — Visual: From notebook: figures/L12/weights_long.png
- 10. **MSM estimation** — Key: pooled logistic or weighted regression — Visual: Draw (vector): model box
- 11. **Interpret MSM coefficient** — Key: causal contrast under a regime — Visual: Draw (vector): interpretation box
- 12. **(Pause/Activity) interpret MSM output** — Key: teams interpret β with CI — Visual: Prompt-only — Notes: 7 min

### Module B — Target trial emulation (Slides 13–17)
- 13. **Target trial: protocol checklist** — Key: eligibility, treatment, t0, follow-up, outcome, analysis — Visual: Draw (vector): checklist
- 14. **Emulation mapping table** — Key: protocol element → operational definition — Visual: Draw (vector): 2-column table
- 15. **Immortal time bias** — Key: how it arises; why harmful — Visual: Draw (vector): timeline shaded
- 16. **Design fixes** — Key: align t0, exposure window, follow-up — Visual: Draw (vector): corrected timeline
- 17. **(Pause/Activity) protocol v2 workshop** — Key: teams refine protocol — Visual: Prompt-only — Notes: 10–12 min

### Module C — Discrete-time survival (Slides 18–25)
- 18. **Survival outcomes: why special** — Key: censoring and time-to-event — Visual: Draw (vector): timeline
- 19. **Discrete-time hazard** — Key: h(t)=Pr(T=t|T≥t) — Visual: Formula tile
- 20. **Person-period dataset** — Key: one row per time interval — Visual: Draw (vector): dataset schematic
- 21. **Pooled logistic for hazards** — Key: logit h(t)=α_t+βA+… — Visual: Minimal formula
- 22. **Hazard → survival curve** — Key: S(t)=∏(1-h(k)) — Visual: Draw (vector): product schematic
- 23. **Plot survival curves (toy)** — Key: treated vs untreated — Visual: From notebook: figures/L12/survival_curves.png
- 24. **Weighted pooled logistic (link to MSM)** — Key: combine weights + survival — Visual: Draw (vector): weights + model
- 25. **(Pause/Activity) notebook walk-through** — Key: interpret curves; check assumptions — Visual: Prompt-only — Notes: 12–15 min

### Wrap + project alignment (Slides 26–33)
- 26. **Integrate deliverables** — Key: protocol → analysis plan → repo — Visual: Draw (vector): pipeline
- 27. **Capstone homework recap** — Key: protocol v2 + survival lab + reflection — Visual: Draw (vector): checklist
- 28. **Final project rubric (mini)** — Key: reproducibility, validity, clarity — Visual: Draw (vector): rubric grid
- 29. **Common capstone pitfalls** — Key: immortal time; extreme weights; post-A covariates — Visual: Draw (vector): warning list
- 30. **Course summary** — Key: capabilities gained — Visual: Draw (vector): checklist
- 31. **Next steps** — Key: how to extend methods after course — Visual: Draw (vector): path forward
- 32. **Closing Q&A** — Key: None — Visual: None
- 33. **Thank you slide** — Key: None — Visual: None

### Practice/backup (Slides 34–86)
- 34. **L12 Practice/backup: Worked example: 2 time points — compute simple stabilized weights** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 35. **L12 Practice/backup: Practice: identify time-varying confounder in ICU vignette** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 36. **L12 Practice/backup: Practice: define a dynamic treatment regime in words** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 37. **L12 Practice/backup: Mini-quiz: MSM assumptions and diagnostics (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 38. **L12 Practice/backup: Mini-quiz: target trial components (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 39. **L12 Practice/backup: Practice: find immortal time in a flawed study design (3 vignettes)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 40. **L12 Practice/backup: Practice: interpret survival curves and hazards** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 41. **L12 Practice/backup: Pitfall: informative censoring vs administrative censoring** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 42. **L12 Practice/backup: Optional: competing risks framing (high-level; optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 43. **L12 Practice/backup (2): Worked example: 2 time points — compute simple stabilized weights** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 44. **L12 Practice/backup (2): Practice: identify time-varying confounder in ICU vignette** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 45. **L12 Practice/backup (2): Practice: define a dynamic treatment regime in words** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 46. **L12 Practice/backup (2): Mini-quiz: MSM assumptions and diagnostics (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 47. **L12 Practice/backup (2): Mini-quiz: target trial components (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 48. **L12 Practice/backup (2): Practice: find immortal time in a flawed study design (3 vignettes)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 49. **L12 Practice/backup (2): Practice: interpret survival curves and hazards** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 50. **L12 Practice/backup (2): Pitfall: informative censoring vs administrative censoring** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 51. **L12 Practice/backup (2): Optional: competing risks framing (high-level; optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 52. **L12 Practice/backup (3): Worked example: 2 time points — compute simple stabilized weights** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 53. **L12 Practice/backup (3): Practice: identify time-varying confounder in ICU vignette** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 54. **L12 Practice/backup (3): Practice: define a dynamic treatment regime in words** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 55. **L12 Practice/backup (3): Mini-quiz: MSM assumptions and diagnostics (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 56. **L12 Practice/backup (3): Mini-quiz: target trial components (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 57. **L12 Practice/backup (3): Practice: find immortal time in a flawed study design (3 vignettes)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 58. **L12 Practice/backup (3): Practice: interpret survival curves and hazards** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 59. **L12 Practice/backup (3): Pitfall: informative censoring vs administrative censoring** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 60. **L12 Practice/backup (3): Optional: competing risks framing (high-level; optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 61. **L12 Practice/backup (4): Worked example: 2 time points — compute simple stabilized weights** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 62. **L12 Practice/backup (4): Practice: identify time-varying confounder in ICU vignette** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 63. **L12 Practice/backup (4): Practice: define a dynamic treatment regime in words** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 64. **L12 Practice/backup (4): Mini-quiz: MSM assumptions and diagnostics (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 65. **L12 Practice/backup (4): Mini-quiz: target trial components (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 66. **L12 Practice/backup (4): Practice: find immortal time in a flawed study design (3 vignettes)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 67. **L12 Practice/backup (4): Practice: interpret survival curves and hazards** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 68. **L12 Practice/backup (4): Pitfall: informative censoring vs administrative censoring** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 69. **L12 Practice/backup (4): Optional: competing risks framing (high-level; optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 70. **L12 Practice/backup (5): Worked example: 2 time points — compute simple stabilized weights** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 71. **L12 Practice/backup (5): Practice: identify time-varying confounder in ICU vignette** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 72. **L12 Practice/backup (5): Practice: define a dynamic treatment regime in words** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 73. **L12 Practice/backup (5): Mini-quiz: MSM assumptions and diagnostics (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 74. **L12 Practice/backup (5): Mini-quiz: target trial components (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 75. **L12 Practice/backup (5): Practice: find immortal time in a flawed study design (3 vignettes)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 76. **L12 Practice/backup (5): Practice: interpret survival curves and hazards** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 77. **L12 Practice/backup (5): Pitfall: informative censoring vs administrative censoring** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 78. **L12 Practice/backup (5): Optional: competing risks framing (high-level; optional)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 79. **L12 Practice/backup (6): Worked example: 2 time points — compute simple stabilized weights** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 80. **L12 Practice/backup (6): Practice: identify time-varying confounder in ICU vignette** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 81. **L12 Practice/backup (6): Practice: define a dynamic treatment regime in words** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 82. **L12 Practice/backup (6): Mini-quiz: MSM assumptions and diagnostics (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 83. **L12 Practice/backup (6): Mini-quiz: target trial components (12 items)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 84. **L12 Practice/backup (6): Practice: find immortal time in a flawed study design (3 vignettes)** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 85. **L12 Practice/backup (6): Practice: interpret survival curves and hazards** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).
- 86. **L12 Practice/backup (6): Pitfall: informative censoring vs administrative censoring** — Key: Include 1 concrete example + 1 short check-for-understanding question — Visual: Draw (vector) or From notebook (if plot) — Notes: Use as pacing buffer (2–4 min each).


# Appendix — Figure note template (put in speaker notes for every figure slide)
- **Figure title:** …
- **Type:** Draw (vector) / From notebook
- **File path:** figures/LXX/<name>.png
- **What it shows:** axes, groups, what is highlighted
- **Alt-text:** 1 sentence
- **If missing:** placeholder box with exact path
