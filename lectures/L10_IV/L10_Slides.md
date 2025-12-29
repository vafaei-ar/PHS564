# L10 — Instrumental variables (IV): when exchangeability is not plausible

## Slide 1 — Title
- PHS564: Causal Inference Methods in Epidemiologic Research
- Lecture 10: Instrumental variables (IV): when exchangeability is not plausible
Speaker notes:
- Today we learn a tool that can (under strict assumptions) solve the problem of unmeasured confounding: the Instrumental Variable (IV).

## Slide 2 — Motivation
- What if there is a variable $U$ that affects both $A$ and $Y$, but we cannot measure it?
- Standardization and IPW will fail.
- We need a variable $Z$ that affects $A$ but is independent of $U$ and only affects $Y$ through $A$.
Speaker notes:
- Figure title: U-Confounding; type: Draw (vector); file path: figures/L10/u_confounding.png; what it shows: A <- U -> Y; alt-text: A DAG showing unmeasured confounding.

## Slide 3 — IV DAG
- The structure: $Z \rightarrow A \rightarrow Y$, with $A \leftarrow U \rightarrow Y$.
- $Z$ is the "Instrument."
Speaker notes:
- Figure title: IV DAG; type: Draw (vector); file path: figures/L10/iv_dag.png; what it shows: Z -> A -> Y with U affecting A and Y; alt-text: The standard instrumental variable DAG.

## Slide 4 — Assumption: relevance
- $Z$ must have a strong effect on the treatment $A$.
- If $Z$ doesn't affect $A$, it's not an instrument.
Speaker notes:
- Figure title: Relevance; type: Draw (vector); file path: figures/L10/iv_relevance.png; what it shows: highlighting the Z -> A arrow; alt-text: The relevance assumption: Z must cause A.

## Slide 5 — Assumption: exclusion
- $Z$ only affects $Y$ through its effect on $A$.
- There are no other paths from $Z$ to $Y$.
Speaker notes:
- Figure title: Exclusion; type: Draw (vector); file path: figures/L10/iv_exclusion.png; what it shows: a DAG with a red 'X' over any direct Z -> Y arrow; alt-text: The exclusion restriction: Z only affects Y via A.

## Slide 6 — Assumption: independence
- $Z$ is independent of all unmeasured causes of the outcome ($U$).
- This is often satisfied by randomizing $Z$ (e.g., Mendelian Randomization).
Speaker notes:
- Figure title: Independence; type: Draw (vector); file path: figures/L10/iv_independence.png; what it shows: no arrows between Z and U; alt-text: The independence assumption: Z is as-good-as randomized.

## Slide 7 — Assumption: monotonicity
- "No defiers."
- Everyone who is assigned treatment because of $Z$ actually takes it (or is unaffected), but no one does the opposite of what $Z$ suggests.
Speaker notes:
- Figure title: Compliance Types; type: Draw (vector); file path: figures/L10/compliance_types.png; what it shows: Always-takers, Never-takers, Compliers, and a 'forbidden' Defier; alt-text: Diagram of the four compliance types in IV.

## Slide 8 — Compliance classes
- Always-takers: $A=1$ regardless of $Z$.
- Never-takers: $A=0$ regardless of $Z$.
- Compliers: $A=Z$.
Speaker notes:
- Figure title: Class Diagram; type: Draw (vector); file path: figures/L10/compliance_classes.png; what it shows: icons for each compliance type; alt-text: Summary of the compliance classes.

## Slide 9 — Wald estimator
- Formula: $ATE_{IV} = \frac{E[Y | Z=1] - E[Y | Z=0]}{E[A | Z=1] - E[A | Z=0]}$
- "The effect of the instrument on the outcome, divided by the effect of the instrument on the treatment."
Speaker notes:
- Figure title: Wald Formula; type: Draw (vector); file path: figures/L10/wald_formula.png; what it shows: the Wald estimator formula; alt-text: The mathematical formula for the Wald estimator.

## Slide 10 — LATE interpretation
- Under monotonicity, the IV estimate is the **Local Average Treatment Effect (LATE)**.
- This is the effect ONLY among the **Compliers**.
Speaker notes:
- Figure title: Highlight Compliers; type: Draw (vector); file path: figures/L10/late_highlight.png; what it shows: whole population with a subset labeled 'Compliers' highlighted; alt-text: Diagram showing that IV measures the effect in the complier subgroup.

## Slide 11 — (Pause/Activity) Critique IV candidates
- Candidate 1: Distance to the hospital as an IV for surgery.
- Candidate 2: Month of birth as an IV for length of schooling.
- Candidate 3: Genetic variant as an IV for alcohol consumption.
- Discuss assumptions for each.
Speaker notes:
- Timed anchor: 8 min. Critical evaluation of IV candidates.

## Slide 12 — Weak instruments
- If $Z$ only weakly affects $A$, the denominator of the Wald estimator is near 0.
- This leads to huge variance and bias towards the observational estimate if assumptions are slightly violated.
Speaker notes:
- Figure title: Weak IV; type: From notebook; file path: figures/L10/weak_iv.png; what it shows: two sampling distributions, one for a strong IV and one for a weak IV; alt-text: Comparison of strong and weak instruments.

## Slide 13 — First-stage strength (concept)
- F-statistic: A measure of how much $Z$ explains $A$.
- Rule of thumb: $F > 10$ (though higher is better).
Speaker notes:
- Figure title: Gauge Icon; type: Draw (vector); file path: figures/L10/iv_gauge.png; what it shows: a gauge with a needle in the 'Strong' zone; alt-text: Icon for instrument strength.

## Slide 14 — 2SLS pipeline
- Two-Stage Least Squares:
  - Stage 1: Regress $A$ on $Z$ to get predicted $\hat{A}$.
  - Stage 2: Regress $Y$ on $\hat{A}$.
Speaker notes:
- Figure title: Two-Stage Boxes; type: Draw (vector); file path: figures/L10/2sls_pipeline.png; what it shows: two connected boxes for Stage 1 and Stage 2; alt-text: A diagram of the 2SLS estimation process.

## Slide 15 — 2SLS interpretation caution
- Remember: 2SLS with one instrument gives you the LATE.
- It is NOT the average effect for the whole population unless everyone is a complier.
Speaker notes:
- Figure title: Caution Box; type: Draw (vector); file path: figures/L10/iv_caution.png; what it shows: warning sign; alt-text: Caution about the interpretation of IV results.

## Slide 16 — Multiple instruments (brief)
- You can use many instruments at once to improve precision.
- "Overidentification" tests can check if the instruments are consistent with each other.
Speaker notes:
- Figure title: Multiple Z; type: Draw (vector); file path: figures/L10/multiple_z.png; what it shows: Z1, Z2, Z3 all pointing to A; alt-text: Using multiple instruments in an IV analysis.

## Slide 17 — IV vs confounding adjustment
- Confounding Adjustment: Needs all common causes measured.
- IV: Needs a valid instrument; doesn't care about unmeasured $U$.
Speaker notes:
- Figure title: Comparison Table; type: Draw (vector); file path: figures/L10/iv_vs_adj.png; what it shows: 2x2 table comparing the two approaches; alt-text: Comparison of IV and standard confounding adjustment.

## Slide 18 — IV + selection/censoring risk
- If your instrument $Z$ or outcome $Y$ affects survival ($S$), it can create a collider path that invalidates the instrument.
Speaker notes:
- Figure title: S Collider; type: Draw (vector); file path: figures/L10/iv_selection.png; what it shows: IV DAG with a new node S; alt-text: How selection bias can break an IV analysis.

## Slide 19 — Summary
- IV can solve unmeasured confounding.
- But it relies on "invisible" assumptions (Exclusion, Independence).
- It measures the effect only in the compliers.
Speaker notes:
- Recap.

## Slide 20 — Homework: simulate IV strength
- You will create a simulation with a strong vs. weak instrument and compare the bias and variance of the resulting estimates.
Speaker notes:
- Figure title: HW IV Sim; type: From notebook placeholder; file path: figures/L10/hw_iv_sim.png; what it shows: sample output plots; alt-text: Placeholder for the IV simulation homework.

## Slide 21 — Homework: IV plausibility memo
- Choose an IV candidate from a published paper and write a critique of its exclusion restriction and independence assumptions.
Speaker notes:
- Figure title: Memo Template; type: Draw (vector); file path: figures/L10/iv_memo.png; what it shows: layout for the critique memo; alt-text: Template for the IV plausibility homework.

## Slide 22 — Reading
- Read IV lecture notes and the *What If* IV section.
Speaker notes:
- Assigned reading.

## Slides 23-78 — [L10 Practice/backup modules as per plan]
- (Worked examples for the Wald estimator and drills for identifying exclusion violations).
Speaker notes:
- Pacing buffer slides.
