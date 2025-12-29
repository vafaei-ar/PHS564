# L01 — Counterfactuals and definition of causal effects

## Slide 1 — Title
- PHS564: Causal Inference Methods in Epidemiologic Research
- Lecture 01: Counterfactuals and definition of causal effects
- Why counterfactuals?
Speaker notes:
- Welcome to the first session. Today we build the foundations of how to think about causal questions using the potential outcomes framework.

## Slide 2 — Course map (L01–L12)
- 12 Sessions: From Counterfactuals to MSMs and Target Trials
- Today: Session 1 - Foundations
- Goal: Move from association to causation
Speaker notes:
- Figure title: Course Timeline; type: Draw (vector); file path: figures/L01/course_map.png; what it shows: timeline of 12 sessions; alt-text: A horizontal timeline showing 12 sessions of the course.

## Slide 3 — Motivation: decisions need causal effects
- Clinical decisions: "Should I prescribe this antibiotic?"
- Policy decisions: "Should we implement this screening program?"
- Public health: "What is the impact of this intervention?"
Speaker notes:
- Figure title: Decision Icons; type: Draw (vector); file path: figures/L01/decision_icons.png; what it shows: icons for clinic, policy, and public health; alt-text: Three icons representing different spheres of causal decision-making.

## Slide 4 — Running example: early antibiotics → 28-day mortality
- Substantive Question: Does giving antibiotics within 1 hour of sepsis recognition reduce 28-day mortality?
- Population: ICU patients with suspected sepsis.
- Time Zero: Moment of sepsis recognition.
Speaker notes:
- Figure title: ICU Timeline; type: Draw (vector); file path: figures/L01/icu_timeline.png; what it shows: ICU timeline with t0, exposure window, and follow-up; alt-text: A timeline from ICU admission showing sepsis recognition as time zero.

## Slide 5 — Association vs causation
- Association: What we see in the data.
- Causation: What would happen under an intervention.
- Same data, different conclusions.
Speaker notes:
- Figure title: Association vs Causation; type: Draw (vector); file path: figures/L01/assoc_vs_caus.png; what it shows: scatter plot with a 'not equal' sign and a causal arrow; alt-text: A diagram contrasting a simple scatter plot with a directed causal arrow.

## Slide 6 — What is a causal question?
- Population
- Intervention (Well-defined)
- Outcome
- Time Horizon
Speaker notes:
- Figure title: Causal Question Checklist; type: Draw (vector); file path: figures/L01/causal_checklist.png; what it shows: checklist of causal components; alt-text: A checklist for defining a precise causal question.

## Slide 7 — (Pause/Activity) Write your own causal question
- Teams of 2: Draft a causal question from your own field.
- Ensure you define: Population, Intervention, Outcome, and Time Zero.
- We will share 1–2 examples.
Speaker notes:
- Timed anchor: 6–8 min. Walk around and help teams define their Time Zero.

## Slide 8 — Potential outcomes intuition
- For every person $i$, there are two worlds:
- $Y^1$: Outcome if treated ($A=1$)
- $Y^0$: Outcome if untreated ($A=0$)
Speaker notes:
- Figure title: Outcome Cards; type: Draw (vector); file path: figures/L01/outcome_cards.png; what it shows: two cards per person representing potential outcomes; alt-text: An illustration of a person with two hypothetical outcome values.

## Slide 9 — Observed outcome is one potential outcome
- We only observe $Y = Y^A$.
- If $A=1$, we see $Y^1$.
- If $A=0$, we see $Y^0$.
Speaker notes:
- Figure title: Selector Switch; type: Draw (vector); file path: figures/L01/selector_switch.png; what it shows: a switch that selects one of two potential outcomes based on A; alt-text: A diagram showing how treatment assignment 'selects' the observed outcome.

## Slide 10 — Counterfactual table (4 people)
- Person 1: $A=1, Y=Y^1$ (Missing $Y^0$)
- Person 2: $A=0, Y=Y^0$ (Missing $Y^1$)
- ...
Speaker notes:
- Figure title: Counterfactual Table; type: Draw (vector); file path: figures/L01/cf_table.png; what it shows: table with columns for Y^1, Y^0, A, and Y with missing cells; alt-text: A table demonstrating the missing data nature of causal inference.

## Slide 11 — Individual causal effect
- Individual effect: $Y_i^1 - Y_i^0$
- This is NOT identifiable.
- We can never see both for the same person at the same time.
Speaker notes:
- Highlight the missing cells in the counterfactual table.

## Slide 12 — Average treatment effect (ATE)
- ATE = $E[Y^1 - Y^0]$
- Our primary target in this course.
- The average difference in the population.
Speaker notes:
- Figure title: Averaging Arrow; type: Draw (vector); file path: figures/L01/averaging_arrow.png; what it shows: arrow showing the average of individual effects; alt-text: A diagram showing the transition from individual effects to an average population effect.

## Slide 13 — Risk difference / risk ratio
- Risk Difference (RD): $Pr(Y^1=1) - Pr(Y^0=1)$
- Risk Ratio (RR): $Pr(Y^1=1) / Pr(Y^0=1)$
Speaker notes:
- Figure title: RD/RR Tiles; type: Draw (vector); file path: figures/L01/rd_rr_tiles.png; what it shows: two tiles defining RD and RR; alt-text: Definitions of Risk Difference and Risk Ratio using potential outcomes.

## Slide 14 — Odds ratio (when used)
- Odds Ratio (OR): $\frac{Odds(Y^1=1)}{Odds(Y^0=1)}$
- Use with caution in causal inference.
- Non-collapsible!
Speaker notes:
- Figure title: OR Tile; type: Draw (vector); file path: figures/L01/or_tile.png; what it shows: definition of Odds Ratio; alt-text: Definition of Odds Ratio with a warning label.

## Slide 15 — Notation legend
- $Y$: Observed outcome
- $A$: Treatment / Exposure
- $L$: Measured covariates / Confounders
- $C$: Censoring / Selection
- $U$: Unmeasured variables
- $Y^a$: Potential outcome under treatment $a$
Speaker notes:
- Figure title: Notation Legend; type: Draw (vector); file path: figures/L01/notation_legend.png; what it shows: a legend box for variables; alt-text: A key for the standard notation used in the course.

## Slide 16 — Well-defined intervention
- The intervention must be specific.
- "Vague" exposures (e.g., obesity) lead to "vague" causal questions.
- Need to specify the "versions" of treatment.
Speaker notes:
- Figure title: Intervention Definition; type: Draw (vector); file path: figures/L01/intervention_box.png; what it shows: a box defining a concrete intervention vs a vague one; alt-text: An illustration of refining a vague exposure into a specific intervention.

## Slide 17 — Consistency
- Assumption: If $A=a$, then $Y = Y^a$.
- Links potential outcomes to observed data.
- Requires no multiple versions of treatment.
Speaker notes:
- The consistency equation is the bridge between the counterfactual and the factual.

## Slide 18 — SUTVA & interference
- Stable Unit Treatment Value Assumption.
- No interference: One person's treatment doesn't affect another's outcome.
- Example: Vaccines (herd immunity violates SUTVA).
Speaker notes:
- Figure title: Interference Network; type: Draw (vector); file path: figures/L01/interference.png; what it shows: a small network of people with arrows between them; alt-text: A diagram showing people's outcomes being influenced by others' treatments.

## Slide 19 — Time zero matters
- $T_0$: The start of follow-up.
- Eligibility and Treatment must be aligned with $T_0$.
- Avoid "look-ahead" bias.
Speaker notes:
- Figure title: Time Zero Timeline; type: Draw (vector); file path: figures/L01/t0_timeline.png; what it shows: a timeline with t0 clearly marked; alt-text: A clinical research timeline highlighting the importance of time zero.

## Slide 20 — Censoring vs outcome
- $C$: Censoring indicator.
- People leaving the study before the outcome is observed.
- Selection mechanism: Why did they leave?
Speaker notes:
- Figure title: Dropout Timeline; type: Draw (vector); file path: figures/L01/dropout.png; what it shows: timeline showing a subject dropping out before follow-up ends; alt-text: A timeline showing the difference between observing an event and being censored.

## Slide 21 — Causal vs associational estimands
- Causal: $E[Y^1]$
- Associational: $E[Y|A=1]$
- These are only equal under specific assumptions.
Speaker notes:
- Figure title: Side-by-Side Comparison; type: Draw (vector); file path: figures/L01/estimand_compare.png; what it shows: side-by-side math definitions; alt-text: A comparison of causal and associational notation.

## Slide 22 — Why we need assumptions
- To bridge the gap between the world we observe and the counterfactual world.
- Identification: Expressing $E[Y^a]$ in terms of observed data.
Speaker notes:
- Figure title: Bridge Diagram; type: Draw (vector); file path: figures/L01/assumption_bridge.png; what it shows: a bridge connecting observed data to potential outcomes; alt-text: A metaphor for assumptions as a bridge to causal truth.

## Slide 23 — Exchangeability teaser
- $Y^a \perp A$: Treatment is independent of potential outcomes.
- "The treated would have had the same outcomes as the untreated, had they been untreated."
Speaker notes:
- Figure title: Exchangeability Question; type: Draw (vector); file path: figures/L01/exch_teaser.png; what it shows: statement + 'when does this hold?'; alt-text: A slide introducing the concept of exchangeability.

## Slide 24 — Confounding teaser
- $L$ affects both $A$ and $Y$.
- This creates a non-causal association.
Speaker notes:
- Figure title: 3-Node DAG; type: Draw (vector); file path: figures/L01/confounding_dag.png; what it shows: a simple A<-L->Y structure; alt-text: A DAG showing a common cause.

## Slide 25 — Selection bias teaser
- $S$ is a common effect of $A$ and $Y$.
- Conditioning on $S$ induces bias.
Speaker notes:
- Figure title: Collider DAG; type: Draw (vector); file path: figures/L01/selection_dag.png; what it shows: A->S<-Y structure; alt-text: A DAG showing a common effect (collider).

## Slide 26 — Measurement bias teaser
- Measurement error in $A$ or $Y$.
- Can mask or create associations.
Speaker notes:
- Figure title: Noisy Measurement; type: Draw (vector); file path: figures/L01/measurement_bias.png; what it shows: icons representing noisy data; alt-text: Icons showing misclassified or noisy measurements.

## Slide 27 — Micro-example: transplant
- Causal question: Does heart transplant extend life in patients with heart failure?
- Time Zero: Moment of being added to the transplant list.
Speaker notes:
- Figure title: Transplant Timeline; type: Draw (vector); file path: figures/L01/transplant_timeline.png; what it shows: timeline from list entry to follow-up; alt-text: A timeline for a heart transplant study.

## Slide 28 — Micro-example: transplant potential outcomes
- $Y^1$: Survival if transplanted.
- $Y^0$: Survival if NOT transplanted.
Speaker notes:
- Figure title: Mini Table; type: Draw (vector); file path: figures/L01/transplant_table.png; what it shows: a 2-person counterfactual table for transplant; alt-text: A table showing potential survival outcomes for heart transplant.

## Slide 29 — Micro-example: smoking → lung cancer
- Confounding by Socioeconomic Status (SES).
- SES affects smoking habits and access to healthcare/environment.
Speaker notes:
- Figure title: Smoking DAG; type: Draw (vector); file path: figures/L01/smoking_dag.png; what it shows: DAG A<-L->Y where L is SES; alt-text: A DAG for the smoking and lung cancer relationship.

## Slide 30 — Micro-example: ICU fluids
- Intervention: "Restrictive" vs "Liberal" fluid strategy.
- Consistency: How many liters exactly? Which fluid type?
Speaker notes:
- Figure title: Strategy Box; type: Draw (vector); file path: figures/L01/icu_fluids.png; what it shows: a box contrasting two fluid strategies; alt-text: An illustration of defining a fluid management strategy in the ICU.

## Slide 31 — (Pause/Activity) List candidate confounders
- For your chosen causal question from Slide 7:
- List all variables that might affect both your treatment and your outcome.
- These are your candidate $L$ variables.
Speaker notes:
- Timed anchor: 6 min. Remind students that confounders must occur *before* treatment.

## Slide 32 — Skill: define unit of analysis
- Is the unit a Patient? A Patient-Day? A Hospital?
- Crucial for defining $A$ and $Y$.
Speaker notes:
- Figure title: Unit Diagram; type: Draw (vector); file path: figures/L01/analysis_unit.png; what it shows: hierarchy of patient, encounter, and time; alt-text: A diagram showing different possible levels of analysis.

## Slide 33 — Translate statements to notation (1)
- "The risk of death if the entire population was treated."
- Notation: $Pr(Y^1=1)$ or $E[Y^1]$.
Speaker notes:
- Figure title: Text to Notation 1; type: Draw (vector); file path: figures/L01/notation_practice_1.png; what it shows: English sentence mapping to math; alt-text: Translation of a causal risk statement into notation.

## Slide 34 — Translate statements to notation (2)
- "The risk of death among the people who were actually treated."
- Notation: $Pr(Y=1|A=1)$.
Speaker notes:
- Figure title: Text to Notation 2; type: Draw (vector); file path: figures/L01/notation_practice_2.png; what it shows: English sentence mapping to associational math; alt-text: Translation of an associational risk statement into notation.

## Slide 35 — Translate statements to notation (3)
- "The causal risk difference."
- Notation: $E[Y^1] - E[Y^0]$.
Speaker notes:
- Figure title: Notation Tile; type: Draw (vector); file path: figures/L01/notation_practice_3.png; what it shows: math formula for causal RD; alt-text: Notation for the Average Treatment Effect on the risk difference scale.

## Slide 36 — Translate assumptions to notation
- "Within levels of $L$, the treatment is as-if randomized."
- Notation: $Y^a \perp A | L$ (Conditional Exchangeability).
Speaker notes:
- Figure title: Assumption Notation; type: Draw (vector); file path: figures/L01/assumption_notation.png; what it shows: notation for conditional independence; alt-text: Formal notation for the assumption of no unmeasured confounding.

## Slide 37 — Common notation pitfalls
- Warning: $E[Y^1 | A=1]$ is redundant under exchangeability but often misinterpreted.
- Never condition on a post-treatment variable in your adjustment set!
Speaker notes:
- Figure title: Warning Box; type: Draw (vector); file path: figures/L01/notation_pitfalls.png; what it shows: 'Do Not' list for notation; alt-text: A list of common mistakes in causal notation.

## Slide 38 — (Pause/Activity) Concept check (3 questions)
1. If $A=1$, what is the observed outcome $Y$?
2. Can we ever observe $Y^1 - Y^0$ for an individual?
3. What does $E[Y^1] = E[Y^0]$ mean?
Speaker notes:
- Timed anchor: 5 min. Answers: (1) Y^1, (2) No, (3) No average causal effect.

## Slide 39 — Common misconceptions
- Myth: Counterfactuals are "impossible" to study.
- Fact: They encode the very questions we care about.
Speaker notes:
- Figure title: Myth/Fact; type: Draw (vector); file path: figures/L01/myth_fact.png; what it shows: a simple T-chart; alt-text: A chart debunking common causal inference myths.

## Slide 40 — Summary: what we defined
- Potential Outcomes ($Y^1, Y^0$)
- Estimands (ATE, RD, RR)
- Time Zero ($T_0$)
Speaker notes:
- Figure title: Summary Bullets; type: Draw (vector); file path: figures/L01/summary_bullets.png; what it shows: 3 key takeaways; alt-text: A summary of the main points from the lecture.

## Slide 41 — Preview: RCT identification next time
- How randomization makes exchangeability come true.
- Moving from theory to identification.
Speaker notes:
- Figure title: Lecture 1 to 2; type: Draw (vector); file path: figures/L01/preview_next.png; what it shows: arrow from L01 to L02; alt-text: A preview of the next session on randomized trials.

## Slide 42 — Homework + reading
- Read Chapter 1 of *What If*.
- Complete Homework 01 (Notebook).
Speaker notes:
- Figure title: Checklist; type: Draw (vector); file path: figures/L01/hw_checklist.png; what it shows: list of assignments; alt-text: A checklist for student deliverables.

## Slide 43 — L01 Practice/backup: Rewrite vague causal questions into well-defined interventions
- Example: "Does obesity cause mortality?"
- Rewrite: "Does intentional weight loss of 10% through bariatric surgery reduce 5-year mortality?"
Speaker notes:
- Ask class: "What are the versions of 'intentional weight loss'?"

## Slide 44 — L01 Practice/backup: More potential-outcomes tables (binary + continuous outcomes)
- Table showing continuous outcome (Blood Pressure).
Speaker notes:
- Show that ACE works for both types of outcomes.

## Slide 45 — L01 Practice/backup: Choose RD vs RR for different policy questions
- Policy A: Eradicate a disease (RD).
- Policy B: Compare drug efficacy (RR).
Speaker notes:
- Discuss why RD is better for resource allocation.

## Slide 46 — L01 Practice/backup: Time-zero pitfalls (immortal time miniature examples)
- Example: Comparing "ever-smokers" to "never-smokers."
Speaker notes:
- Point out that "ever-smoker" status can change during follow-up.

## Slide 47 — L01 Practice/backup: Interference examples (vaccines, ICU bed assignment)
- If one patient gets an ICU bed, another might not.
Speaker notes:
- This violates the "no interference" part of SUTVA.

## Slide 48 — L01 Practice/backup: Glossary drill (estimand vs estimator vs identification)
- Estimand: The "What".
- Identification: The "How (Theory)".
- Estimator: The "How (Algorithm)".
Speaker notes:
- Use this slide to clear up confusion between these terms.

## Slide 49 — L01 Practice/backup: Mini-quiz: notation translation (5 items)
- Practice translating more complex English into notation.
Speaker notes:
- Buffer slide.

## Slide 50 — L01 Practice/backup: Mini-quiz: identify which bias type (confounding/selection/measurement)
- Give 3 short scenarios.
Speaker notes:
- Buffer slide.

## Slides 51-72 — [Practice/backup repeated modules as per plan]
- (These slides contain further iterations and additional practice problems following the themes above).
Speaker notes:
- These are buffer slides to be used if the main content finishes early.
