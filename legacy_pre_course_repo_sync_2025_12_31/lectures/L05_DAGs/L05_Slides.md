# L05 — Causal diagrams (DAGs), d-separation, and collider bias

## Slide 1 — Title
- PHS564: Causal Inference Methods in Epidemiologic Research
- Lecture 05: Causal diagrams (DAGs), d-separation, and collider bias
Speaker notes:
- Today we learn the language of Directed Acyclic Graphs (DAGs). DAGs are not just pictures; they are rigorous mathematical tools for identifying bias.

## Slide 2 — Why DAGs
- Explicit Assumptions: "A DAG is a mathematical encoding of your causal knowledge."
- Identification: Tells you *exactly* which variables to adjust for.
- Communication: A visual way to share your model with others.
Speaker notes:
- Figure title: Assumptions to DAG; type: Draw (vector); file path: figures/L05/assumptions_to_dag.png; what it shows: flow from written assumption to a mini-DAG; alt-text: A diagram showing how text assumptions translate into a DAG.

## Slide 3 — DAG basics
- Node: A variable.
- Edge: A directed arrow representing a potential causal effect.
- Acyclic: No paths can lead back to the starting node.
Speaker notes:
- Figure title: Annotated DAG; type: Draw (vector); file path: figures/L05/annotated_dag.png; what it shows: a DAG with nodes labeled A, Y, L and arrows; alt-text: An example of a Directed Acyclic Graph.

## Slide 4 — Paths & associations
- Causal path: $A \rightarrow Y$.
- Non-causal path: $A \leftarrow L \rightarrow Y$.
- Association flows through "open" paths.
Speaker notes:
- Figure title: Path Highlight; type: Draw (vector); file path: figures/L05/path_highlight.png; what it shows: a DAG with one path glowing/highlighted; alt-text: A DAG with a specific path highlighted to show association flow.

## Slide 5 — Three structures
- Chain: $A \rightarrow B \rightarrow C$
- Fork: $A \leftarrow B \rightarrow C$ (Confounding)
- Collider: $A \rightarrow B \leftarrow C$ (Selection)
Speaker notes:
- Figure title: 3 Mini-DAGs; type: Draw (vector); file path: figures/L05/three_structures.png; what it shows: chain, fork, and collider side-by-side; alt-text: The three fundamental building blocks of DAGs.

## Slide 6 — d-separation: chain
- In $A \rightarrow B \rightarrow C$, $A$ and $C$ are associated.
- Conditioning on $B$ **blocks** the path.
Speaker notes:
- Figure title: Chain Blocked; type: Draw (vector); file path: figures/L05/chain_blocked.png; what it shows: a chain with a box around the middle node; alt-text: A diagram showing how conditioning on a mediator blocks association.

## Slide 7 — d-separation: fork
- In $A \leftarrow B \rightarrow C$, $A$ and $C$ are associated.
- Conditioning on $B$ **blocks** the path (removes confounding).
Speaker notes:
- Figure title: Fork Blocked; type: Draw (vector); file path: figures/L05/fork_blocked.png; what it shows: a fork with a box around the common cause; alt-text: A diagram showing how conditioning on a common cause blocks confounding.

## Slide 8 — d-separation: collider
- In $A \rightarrow B \leftarrow C$, $A$ and $C$ are NOT associated.
- Conditioning on $B$ **opens** the path!
Speaker notes:
- Figure title: Collider Opened; type: Draw (vector); file path: figures/L05/collider_opened.png; what it shows: a collider with a box around the middle node and a new dashed association arrow; alt-text: A diagram showing how conditioning on a collider induces bias.

## Slide 9 — Backdoor intuition
- A "backdoor path" is any path from $A$ to $Y$ that starts with an arrow pointing into $A$.
- These are the paths we must block to identify the causal effect.
Speaker notes:
- Figure title: Backdoor Highlight; type: Draw (vector); file path: figures/L05/backdoor_highlight.png; what it shows: a complex DAG with one 'backdoor' path highlighted in red; alt-text: A DAG illustrating the concept of a backdoor path.

## Slide 10 — (Pause/Activity) Collider identification drill
- Look at the three DAGs provided.
- Vote: Which one has a collider?
Speaker notes:
- Timed anchor: 8 min. Class poll on collider structures.

## Slide 11 — DAG practice: confounding
- $A \leftarrow L \rightarrow Y$
- Should we adjust for $L$? Yes.
Speaker notes:
- Figure title: Confounding DAG; type: Draw (vector); file path: figures/L05/practice_confounding.png; what it shows: simple confounding DAG; alt-text: A DAG showing confounding.

## Slide 12 — DAG practice: confounding — Answer
- Adjusting for $L$ blocks the non-causal path.
Speaker notes:
- Visual solution for the previous slide.

## Slide 13 — DAG practice: mediator
- $A \rightarrow M \rightarrow Y$
- Should we adjust for $M$ to get the **total** effect of $A$ on $Y$? No.
Speaker notes:
- Figure title: Mediator DAG; type: Draw (vector); file path: figures/L05/practice_mediator.png; what it shows: simple mediator DAG; alt-text: A DAG showing mediation.

## Slide 14 — DAG practice: mediator — Answer
- Adjusting for $M$ blocks part of the causal effect.
Speaker notes:
- Visual solution.

## Slide 15 — DAG practice: collider
- $A \rightarrow S \leftarrow Y$
- If we condition on $S$ (e.g., only include hospitalized patients), do we get bias? Yes.
Speaker notes:
- Figure title: Collider Practice; type: Draw (vector); file path: figures/L05/practice_collider.png; what it shows: simple collider DAG; alt-text: A DAG showing collider bias.

## Slide 16 — DAG practice: collider — Answer
- Conditioning on $S$ creates a spurious association between $A$ and $Y$.
Speaker notes:
- Visual solution.

## Slide 17 — DAG practice: selection bias
- Study of the effect of treatment $A$ on outcome $Y$, but we only observe survivors ($S=1$).
- $A \rightarrow S \leftarrow U \rightarrow Y$
Speaker notes:
- Figure title: Selection DAG; type: Draw (vector); file path: figures/L05/practice_selection.png; what it shows: DAG with selection node; alt-text: A DAG for selection bias due to survival.

## Slide 18 — DAG practice: selection bias — Answer
- $S$ is a collider. Restricting to $S=1$ opens the path $A \dots U \dots Y$.
Speaker notes:
- Visual solution.

## Slide 19 — DAG practice: M-bias
- A structure that looks like an 'M'.
- $U1 \rightarrow L \leftarrow U2$
Speaker notes:
- Figure title: M-Bias DAG; type: Draw (vector); file path: figures/L05/practice_mbias.png; what it shows: M-shaped DAG structure; alt-text: A DAG illustrating M-bias.

## Slide 20 — DAG practice: M-bias — Answer
- Adjusting for $L$ (the center of the M) induces bias where none existed.
Speaker notes:
- Visual solution.

## Slide 21 — DAG practice: instrument
- $Z \rightarrow A \rightarrow Y$ where $Z$ is randomized.
- Should we adjust for $Z$? No.
Speaker notes:
- Figure title: Instrument DAG; type: Draw (vector); file path: figures/L05/practice_instrument.png; what it shows: simple instrument DAG; alt-text: A DAG for an instrumental variable.

## Slide 22 — DAG practice: instrument — Answer
- $Z$ is a "competing cause" or instrument; adjusting for it can hurt precision but doesn't remove bias.
Speaker notes:
- Visual solution.

## Slide 23 — DAG practice: competing exposure
- $A \leftarrow L \rightarrow B \rightarrow Y$
- Minimal adjustment set? Just $L$.
Speaker notes:
- Figure title: Competing DAG; type: Draw (vector); file path: figures/L05/practice_competing.png; what it shows: DAG with a competing exposure B; alt-text: A DAG with multiple exposures.

## Slide 24 — DAG practice: competing exposure — Answer
- $B$ doesn't cause $A$, so it doesn't need to be adjusted for to identify $A \rightarrow Y$.
Speaker notes:
- Visual solution.

## Slide 25 — DAG practice: measurement error
- $L$ is the true confounder, but we only have $L^*$.
Speaker notes:
- Figure title: Measurement DAG; type: Draw (vector); file path: figures/L05/practice_measure.png; what it shows: DAG with noisy measure; alt-text: A DAG showing measurement error.

## Slide 26 — DAG practice: measurement error — Answer
- Adjusting for $L^*$ leaves residual confounding.
Speaker notes:
- Visual solution.

## Slide 27 — Adjustment sets cheat-sheet
- 1. Block all backdoor paths.
- 2. Do NOT condition on any mediator or descendant of a mediator.
- 3. Do NOT condition on any collider or descendant of a collider.
Speaker notes:
- Figure title: Rule Summary; type: Draw (vector); file path: figures/L05/rules_cheatsheet.png; what it shows: three bulleted rules with mini-DAG icons; alt-text: A cheat-sheet for valid adjustment sets.

## Slide 28 — Overadjustment bias
- Conditioning on a mediator ($A \rightarrow M \rightarrow Y$).
- Conditioning on a descendant of a collider ($A \rightarrow S \leftarrow Y$ and $S \rightarrow Z$).
Speaker notes:
- Figure title: Warning DAG; type: Draw (vector); file path: figures/L05/overadjustment.png; what it shows: two mini-DAGs illustrating overadjustment; alt-text: Visual examples of overadjustment bias.

## Slide 29 — From DAG to analysis plan
- Use your DAG to list the variables for your regression model or propensity score.
Speaker notes:
- Figure title: Mapping; type: Draw (vector); file path: figures/L05/dag_to_plan.png; what it shows: DAG arrows pointing to a list of variables in a Python dictionary; alt-text: Diagram mapping a DAG to a coding analysis plan.

## Slide 30 — (Pause/Activity) Your project DAG workshop
- Draw the DAG for your causal question.
- Identify the minimal adjustment set.
Speaker notes:
- Timed anchor: 10 min. Walk around and check for colliders.

## Slide 31 — Common mistakes
- "Adjust for everything we measured." (NO!)
- "Don't adjust for anything that happens after $A$." (Usually true, but not always).
Speaker notes:
- Figure title: Mistakes List; type: Draw (vector); file path: figures/L05/common_mistakes.png; what it shows: list of 'Don'ts' for DAGs; alt-text: A list of common misconceptions in DAG building.

## Slide 32 — Homework: DAG + justification
- Draw your project DAG using `dagitty.net`.
- Write a 1-sentence justification for each arrow.
Speaker notes:
- Figure title: Template; type: Draw (vector); file path: figures/L05/hw_template.png; what it shows: example DAG and table of justifications; alt-text: A template for the DAG homework assignment.

## Slide 33 — Reading
- Read *What If* Chapter 6: Graphical Representation of Causal Effects.
Speaker notes:
- Essential reading.

## Slides 34-82 — [L05 Practice/backup modules as per plan]
- (Additional DAG drills and mini-quizzes on d-separation).
Speaker notes:
- Pacing buffer slides.
