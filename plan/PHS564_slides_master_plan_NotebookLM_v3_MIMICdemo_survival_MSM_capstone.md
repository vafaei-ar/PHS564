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

## L08 — IP weighting for confounding (propensity scores) + diagnostics (MIMIC-IV Demo)

**Duration target:** 100–115 min  
**Slide count target:** ~65–75 slides (≈1:30/slide including brief pauses)

### Deck metadata for NotebookLM
- **Filename:** `L08_ipw_propensity.pptx`
- **Theme:** simple, minimal; consistent notation across lectures.
- **Figures:** generated by `lectures/L08_*/notebook_student.ipynb` and saved to `lectures/L08_*/figures/`.
- **End-of-class:** include an **Exit Poll** slide (5 min).

### Slide-by-slide plan

**Section A — Setup & motivation (10–12 min)**
- 01. **Title: IPW for confounding + diagnostics** — Key: what we will do today — Visual: none
- 02. **Where IPW fits** — Key: identification vs estimation — Visual: pipeline: (estimand → assumptions → estimator → computation)
- 03. **Running example (MIMIC Demo cohort)** — Key: early exposure A, outcome Y, covariates L — Visual: ICU timeline (t0, exposure window, follow-up)
- 04. **Reminder: conditional exchangeability** — Key: what must be true for IPW to work — Visual: DAG A←L→Y
- 05. **Target estimand** — Key: marginal RD/RR/ATE; why marginal matters — Visual: E[Y^1]-E[Y^0]

**Section B — Propensity score intuition (15–18 min)**
- 06. **Propensity score definition** — Key: e(L)=Pr(A=1|L) — Visual: formula
- 07. **Why weights?** — Key: build pseudo-population — Visual: “reweighting” cartoon (treated down/up)
- 08. **Unstabilized weights** — Key: w=A/e + (1-A)/(1-e) — Visual: formula
- 09. **Stabilized weights** — Key: sw=Pr(A)/e and Pr(1-A)/(1-e) — Visual: formula + note on variance
- 10. **Interpretation** — Key: weighted sample mimics randomized trial (conditional on measured L) — Visual: DAG with broken backdoor
- 11. **What IPW does NOT fix** — Key: unmeasured confounding; measurement error — Visual: U node in DAG

**Section C — Practical modeling choices (15–18 min)**
- 12. **Choosing L for the PS model** — Key: pre-treatment confounders only — Visual: checklist
- 13. **Do not include mediators** — Key: post-treatment variables break it — Visual: DAG A→M→Y
- 14. **Functional form matters** — Key: interactions/nonlinearity in e(L) — Visual: logistic curve with misfit
- 15. **High-dimensional note** — Key: keep it simple (logit) for pedagogy; mention ML as optional — Visual: “optional” box

**Section D — Diagnostics culture (25–30 min)**
- 16. **Why diagnostics are mandatory** — Key: IPW fails silently — Visual: warning icon
- 17. **Overlap / positivity** — Key: check PS overlap — Visual placeholder: `figures/L08/ps_overlap.png`
- 18. **Interpreting overlap** — Key: regions with no support → extrapolation — Visual: highlight non-overlap
- 19. **Weight distribution** — Key: extreme weights dominate — Visual placeholder: `figures/L08/weights_hist.png`
- 20. **Weight summary stats** — Key: mean ~1 (stabilized), max, % > 10 — Visual: table
- 21. **Truncation (sensitivity)** — Key: 1/99 or 5/95 as tradeoff — Visual: before/after weight hist
- 22. **Balance idea** — Key: weighting should balance L — Visual: pre/post “two distributions”
- 23. **Standardized mean difference (SMD)** — Key: definition and rule-of-thumb |SMD|<0.1 — Visual: formula
- 24. **Love plot** — Key: show balance improvement — Visual placeholder: `figures/L08/love_plot.png`
- 25. **If balance is poor** — Key: revise PS model; consider interactions; consider trimming — Visual: decision tree

**Section E — Estimation & interpretation (15–20 min)**
- 26. **Weighted estimator (marginal mean)** — Key: weighted mean difference — Visual: formula
- 27. **Weighted regression (optional)** — Key: GLM with weights; robust SE mention — Visual: code snippet
- 28. **Uncertainty** — Key: bootstrap vs robust SE (high-level) — Visual: two boxes
- 29. **Reporting template** — Key: “Under assumptions … we estimate …” — Visual: sentence template
- 30. **Common failure modes recap** — Key: positivity, misspec PS, unmeasured confounding — Visual: checklist

**Section F — Worked example (MIMIC Demo) (20–25 min)**
- 31. **Notebook walkthrough: data & cohort** — Key: what’s in the extract — Visual: schema mini-table
- 32. **Notebook cell: PS model specification** — Key: students only edit formula — Visual: code snippet placeholder
- 33. **Notebook output: overlap** — Visual: `ps_overlap.png`
- 34. **Notebook output: weights** — Visual: `weights_hist.png`
- 35. **Notebook output: balance** — Visual: `love_plot.png`
- 36. **Effect estimate + interpretation** — Visual: result table
- 37. **Sensitivity: truncation** — Visual: before/after estimate plot

**Section G — Wrap-up + Exit Poll (5–7 min)**
- 38. **Key takeaways** — 3 bullets — Visual: none
- 39. **Exit Poll (graded participation)** — Include 4 MCQs + 1 muddiest point — Visual: QR/link placeholder  
  - Q1: stabilized weight definition (treated)  
  - Q2: positivity failure meaning  
  - Q3: what love plot measures  
  - Q4: one-sentence pseudo-population interpretation  
  - free text: muddiest point

---

## L09 — Standardization + (parametric) g-formula (MIMIC-IV Demo)

**Duration target:** 100–115 min  
**Slide count target:** ~65–75 slides

### Deck metadata for NotebookLM
- **Filename:** `L09_gformula_standardization.pptx`
- **Figures:** `lectures/L09_*/figures/` from notebook.
- **End-of-class:** Exit Poll slide.

### Slide-by-slide plan

**Section A — Motivation & estimand (10–12 min)**
- 01. **Title: Standardization & g-formula** — Visual: none
- 02. **Where we are** — Key: compare to IPW — Visual: estimator comparison table
- 03. **Target estimand** — Key: E[Y^1]-E[Y^0] or RD/RR — Visual: formula
- 04. **Identification reminder** — Key: exchangeability + positivity + consistency — Visual: checklist

**Section B — Standardization intuition (15–18 min)**
- 05. **Stratified standardization** — Key: few L strata — Visual: weighted average cartoon
- 06. **Standardization formula** — Key: sum over L — Visual: equation
- 07. **Interpretation** — Key: reweight stratum-specific risks to population distribution — Visual: two-step diagram
- 08. **Limits in high dimension** — Key: many strata → sparse — Visual: exploding table

**Section C — Parametric g-formula algorithm (20–25 min)**
- 09. **Algorithm overview** — Key: model E[Y|A,L], predict under A=1 and A=0, average — Visual: 3-step flow
- 10. **Outcome model choices** — Key: linear/logistic; keep simple — Visual: model menu
- 11. **Model misspecification** — Key: prediction ≠ causation — Visual: “good fit, wrong estimand” caution
- 12. **Why model? (compressed)** — Key: estimator vs model vs estimate — Visual: definitions slide
- 13. **Nonlinearity note** — Key: splines/interactions optional — Visual: optional box

**Section D — Uncertainty: bootstrap (15–18 min)**
- 14. **Why bootstrap** — Key: estimator is multi-step — Visual: resampling diagram
- 15. **Bootstrap procedure** — Key: resample individuals, refit, recompute — Visual: steps
- 16. **Bootstrap distribution** — Visual placeholder: `figures/L09/bootstrap_effect_hist.png`
- 17. **CI reporting** — Key: percentile CI; show as table — Visual: table

**Section E — Compare to IPW (10–12 min)**
- 18. **Tradeoffs** — Key: g-formula model dependence vs IPW positivity — Visual: side-by-side failure modes
- 19. **Sanity checks** — Key: compare crude, adjusted (g-formula), weighted (IPW) — Visual: 3 estimates plot
- 20. **Reporting** — Key: minimal causal language template — Visual: sentence template

**Section F — Worked example (MIMIC Demo) (20–25 min)**
- 21. **Notebook: cohort & variables** — Visual: schema mini-table
- 22. **Notebook: outcome model specification cell** — Visual: code snippet placeholder
- 23. **Notebook: standardized predictions under A=1 vs A=0** — Visual placeholder: `figures/L09/standardized_predictions.png`
- 24. **Notebook: bootstrap effect distribution** — Visual: `bootstrap_effect_hist.png`
- 25. **Short sensitivity** — Key: richer model vs simpler model — Visual: table

**Section G — Wrap-up + Exit Poll (5–7 min)**
- 26. **Key takeaways** — Visual: none
- 27. **Exit Poll** — 3–4 MCQs + 1 short answer  
  - Q1: g-formula algorithm step order  
  - Q2: what g-formula is sensitive to  
  - Q3: bootstrap meaning  
  - Q4: why prediction can fail causally  
  - muddiest point

---

## L10 — Causal survival analysis (time-to-event, censoring, discrete-time hazards) (MIMIC-IV Demo)

**Duration target:** 110–120 min  
**Slide count target:** ~70–80 slides

### Deck metadata for NotebookLM
- **Filename:** `L10_causal_survival.pptx`
- **Figures:** `lectures/L10_*/figures/` from notebook.
- **End-of-class:** Exit Poll slide.

### Slide-by-slide plan

**Section A — Time-to-event basics (15–18 min)**
- 01. **Title: Causal survival analysis** — Visual: none
- 02. **Why survival in EHR** — Key: censoring is everywhere — Visual: follow-up timeline
- 03. **T, Δ notation** — Key: event time + event indicator — Visual: table
- 04. **Risk vs hazard vs survival** — Key: definitions — Visual: three formulas
- 05. **What estimand do we want?** — Key: survival curve under A=1 vs A=0; RMST optional — Visual: S^a(t)

**Section B — Time zero & bias traps (10–12 min)**
- 06. **Time zero is a design choice** — Key: define eligibility and exposure window — Visual: ICU timeline
- 07. **Immortal time bias example** — Key: exposure defined after t0 — Visual: shaded “immortal” window
- 08. **Censoring rules** — Key: administrative vs informative — Visual: censoring icons

**Section C — Discrete-time hazard modeling (20–25 min)**
- 09. **Person-period data** — Key: expand each subject over time intervals — Visual: wide→long table
- 10. **Pooled logistic hazard model** — Key: logit Pr(event at t | history) — Visual: equation
- 11. **From hazard to survival** — Key: multiply (1-h_t) — Visual: survival recursion
- 12. **Prediction under A=1/A=0** — Key: standardize/average — Visual: algorithm flow

**Section D — Censoring adjustment (IPCW) (20–25 min)**
- 13. **When censoring is informative** — Visual: DAG with C
- 14. **IPCW idea** — Key: reweight uncensored to represent full cohort — Visual: reweighting cartoon
- 15. **Censoring model** — Key: Pr(C=0|history) — Visual: formula
- 16. **Weights diagnostics** — Key: extreme weights again — Visual placeholder: `figures/L10/censoring_weights_hist.png`
- 17. **Weighted survival curves** — Visual placeholder: `figures/L10/survival_curves_weighted.png`

**Section E — Worked example (MIMIC Demo) (20–25 min)**
- 18. **Notebook: cohort & follow-up** — Visual: schema mini-table
- 19. **Notebook: create person-period** — Visual: code snippet placeholder
- 20. **Notebook: unweighted curves** — Visual placeholder: `figures/L10/survival_curves_unweighted.png`
- 21. **Notebook: IPCW-weighted curves** — Visual: `survival_curves_weighted.png`
- 22. **Interpretation** — Key: what curve difference means; assumptions — Visual: annotation on curve

**Section F — Wrap-up + Exit Poll (5–7 min)**
- 23. **Key takeaways** — Visual: none
- 24. **Exit Poll**  
  - Q1: S(t)=Pr(T>t)  
  - Q2: discrete-time hazard uses pooled logistic  
  - Q3: IPCW condition  
  - Q4: why time zero matters  
  - muddiest point

---

## L11 — Time-varying treatment & confounding: marginal structural models (MSMs) (MIMIC-IV Demo)

**Duration target:** 110–120 min  
**Slide count target:** ~70–80 slides

### Deck metadata for NotebookLM
- **Filename:** `L11_msm_time_varying.pptx`
- **Figures:** `lectures/L11_*/figures/` from notebook.
- **End-of-class:** Exit Poll slide.

### Slide-by-slide plan

**Section A — Why MSMs exist (15–18 min)**
- 01. **Title: MSMs for time-varying treatment** — Visual: none
- 02. **Problem statement** — Key: L_t affects A_t and Y, and is affected by prior A — Visual: time-varying DAG
- 03. **Why naive adjustment fails** — Key: conditioning on L_t blocks part of causal effect and opens bias — Visual: DAG path highlight
- 04. **Target estimand** — Key: effect of treatment strategies over time — Visual: A_0..A_T notation

**Section B — Stabilized weights over time (25–30 min)**
- 05. **Idea: create pseudo-population over time** — Visual: reweighting timeline
- 06. **Treatment weight components** — Key: numerator vs denominator — Visual: formula
- 07. **Censoring weights** — Key: combine with treatment weights — Visual: W = W_A * W_C
- 08. **Procedural construction** — Key: explicit dataframe columns (pA_num, pA_denom, wA, …) — Visual: table
- 09. **Diagnostics** — Key: weight explosion; truncation — Visual placeholder: `figures/L11/weights_over_time.png`

**Section C — Fitting the MSM (15–18 min)**
- 10. **MSM model form** — Key: weighted pooled logistic / GLM — Visual: equation
- 11. **Interpretation** — Key: marginal effect under assumptions — Visual: interpret coefficient
- 12. **Uncertainty** — Key: robust SE / bootstrap mention — Visual: two boxes

**Section D — Worked example (MIMIC Demo longitudinal extract) (25–30 min)**
- 13. **Notebook: person-period dataset** — Visual: schema mini-table
- 14. **Notebook: compute weights step-by-step** — Visual: code snippet placeholders
- 15. **Notebook: weight diagnostics** — Visual: `weights_over_time.png`
- 16. **Notebook: MSM estimate** — Visual: result table/plot

**Section E — Wrap-up + Exit Poll (5–7 min)**
- 17. **Key takeaways** — Visual: none
- 18. **Exit Poll**  
  - Q1: why time-varying confounding breaks standard adjustment  
  - Q2: what stabilized weights combine  
  - Q3: symptom of failure (extreme weights)  
  - Q4: MSM interpretation  
  - muddiest point

---

## L12 — Capstone: target trial emulation workshop + project presentations (MIMIC-IV Demo; full MIMIC-IV optional)

**Duration target:** 100–120 min  
**Slide count target:** ~55–70 slides (more workshop time → fewer slides)

### Deck metadata for NotebookLM
- **Filename:** `L12_target_trial_capstone.pptx`
- **Figures:** teams present one diagnostic figure from their project (template provided).
- **End-of-class:** Exit Poll slide.

### Slide-by-slide plan

**Section A — Protocol audit checklist (20 min)**
- 01. **Title: Target trial emulation workshop** — Visual: none
- 02. **Workshop agenda** — Key: audit → work time → presentations — Visual: timeline
- 03. **Target trial protocol components** — Key: eligibility, time zero, strategies, follow-up, outcome, estimand, analysis plan — Visual: checklist
- 04. **The three recurring failure modes** — Key: time zero / post-treatment adjustment / positivity — Visual: warning icons
- 05. **Minimal reporting sentence** — Key: “Under assumptions…, we estimate…” — Visual: sentence template

**Section B — Team work time (40–50 min)**
- 06. **Work instructions slide** — Key: open protocol_v2 template; assign roles; commit changes — Visual: steps
- 07. **Required artifacts** — Key: protocol_v2 + one figure + one table + limitations — Visual: checklist
- 08. **Project contribution requirement** — Key: both partners commit code; link commits — Visual: Git icon

**Section C — Rapid presentations (30–40 min)**
- 09. **Presentation template** — Key: 3 slides max: question/protocol, DAG/assumptions, one figure/result — Visual: template thumbnails
- 10. **Discussion prompts** — Key: time zero, censoring, confounders, positivity — Visual: prompt list

**Section D — Wrap-up + optional IV teaser (asynchronous) (5–7 min)**
- 11. **Where IV fits (optional)** — Key: not core; included as handout — Visual: small DAG Z→A→Y with U
- 12. **Course wrap-up** — Key: what to do next in real papers — Visual: none
- 13. **Exit Poll**  
  - Q1: define treatment strategies  
  - Q2: identify immortal time bias risk  
  - Q3: minimal reporting sentence  
  - Q4: biggest bias risk in your project + mitigation  
  - muddiest point
