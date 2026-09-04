---
name: cognitive-bridge
description: "Shape a non-trivial explanation around the user's evidenced current model so they can form a faithful, usable mental model quickly. Use when explaining technical mechanisms, engineering plans or results, abstract concepts, formulas, decision structures, or other material whose raw answer would be correct but cognitively hard to absorb, and when an upstream Skill explicitly requests a cognitive explanation pass. Do not use merely to polish prose, supply missing domain facts, replace a specialist workflow, or withhold a direct answer the user asked for."
metadata:
  version: 1.0.0
---

# Cognitive Bridge

Minimize the time and cognitive work needed for the user to build a correct,
usable mental model. Preserve truth before optimizing fluency.

```text
domain-bounded content + evidence about the user's current model
                         -> smallest faithful cognitive bridge
                         -> explanation the user can use
```

A usable model lets the user do at least one relevant thing: predict what will
happen, explain the causal relation, distinguish the boundary, act correctly,
or recognize the same structure in a changed context.

## Authority Boundary

- Treat the supplied source content, anchors, conditions, status, and evidence
  ceiling as constraints. Do not create or revise domain facts.
- Do not modify source documents, code, Bundles, learner records, or external
  systems. This Skill is conversation-only unless another invoked workflow owns
  persistence.
- Do not upgrade planned to implemented, implementation to validation, a narrow
  check to system proof, or explanation to user acceptance or mastery.
- Do not infer the user's beliefs or ability from tone. Use only their words,
  demonstrated predictions, corrections, and explicit feedback as evidence.
- Keep safety, applicability, responsibility, uncertainty, and conclusion-changing
  conditions visible even when they complicate the explanation.
- If supplied claims conflict in a way that changes the explanation, return
  `semantic-input-conflict` with the conflicting anchors and the decision needed
  from the upstream owner. Do not choose a convenient interpretation.

## Cognitive Bridge Request

Form this packet internally when an upstream Skill has not supplied one:

```text
purpose: understand | decide | act | review
source_content
must_preserve
source_anchors
current_model_evidence
desired_depth: quick | standard | deep
```

Only `purpose` and `source_content` are always required. Unknown user-model
evidence remains `unknown`; it is not a reason to interrogate the user when a
conservative explanation can proceed.

`must_preserve` includes every fact or condition whose omission could change a
decision: formal notation, technical anchors, applicability, safety, ownership,
coverage, evidence state, and any order or correspondence required by the
upstream workflow.

## Build the Bridge

Work through these decisions internally. Do not expose them as a fixed template.

1. **Required use**: decide what the user must be able to predict, explain,
   distinguish, do, or transfer after this answer.
2. **Current anchor**: identify the strongest model already supported by the
   user's words or actions. Preserve their useful phrase as a memory index.
3. **Missing relation**: find the smallest relation preventing the required use.
   Do not dump the complete subject around it.
4. **Entry point**: choose by purpose:
   - `understand`: begin with the missing relation, concrete problem, or tension;
   - `decide`: begin with the real fork, consequence, and invalidation condition;
   - `act`: lead with the outcome and next safe action, then explain why;
   - `review`: lead with actual state and evidence level, then map causes and limits.
5. **Representation**: choose the least expensive faithful form: causal chain,
   state transition, contrast, minimal example, formula-to-object mapping,
   relationship map, or compressed rule. Use a second representation only when
   the first leaves a consequential relation hidden.
6. **Span**: advance by the largest step the available evidence says the user can
   absorb. Slow to one relation or state change when they are stuck; show the
   whole structure first when they already own the prerequisites.
7. **Dual anchor**: retain the user's language and bind it to the canonical term,
   symbol, source heading, or technical identifier when one matters.
8. **Stabilize**: let a newly useful coarse model settle before adding exceptions
   that do not affect the current judgment. Add any conclusion-changing exception
   immediately.
9. **Compress**: finish with the shortest reusable relationship, trigger, or
   decision rule that remains faithful to the source.
10. **Check only when useful**: use one prediction, changed condition, contrast,
    or brief articulation when evidence of understanding matters. Do not turn a
    direct answer or operational report into an unsolicited lesson.

## Explanation Rules

- Prefer causal or operational relationships over category lists.
- Introduce a concept when the underlying problem makes it necessary, except
  when urgency or review value requires the conclusion first.
- Explain formulas as compressed relations: name the objects, operation,
  conditions, what changes, and what remains invariant before expanding algebra.
- Preserve source correspondence when the upstream owner requires it. Cognitive
  reordering may improve local exposition but must not destroy traceability.
- Match depth to the user's purpose. `quick` removes non-decision detail;
  `standard` builds one complete usable model; `deep` adds boundaries,
  counterexamples, and transfer without becoming an encyclopedia.
- Use headings, bullets, diagrams, analogy, and questions only when they reduce
  cognitive work. They are tools, not required style.
- Protect the user's judgment and discovery where those are the task; do not
  protect them by refusing execution or answers they explicitly delegated.

## Companion Contract

Upstream Skills retain semantic ownership:

- Engineering Skills own Bundle correspondence, system behavior, safety,
  interfaces, evidence state, acceptance, and source mutation.
- Teaching Skills own learning goals, source conventions, learner state,
  practice, feedback, transfer, and mastery claims.
- Decision or domain Skills own their facts, alternatives, risk, and authority.

Those Skills may pass a prepared request and use this Skill only to compose the
user-facing explanation. This Skill must not invoke them in reverse; keep the
dependency graph one-way.

## Quality Check

Before returning, verify:

- the explanation preserves every conclusion-changing fact and condition;
- its first move matches the user's purpose rather than a universal teaching style;
- it bridges one real missing relation instead of restating the source;
- a technical or formal reader can return to the source through retained anchors;
- the user can now perform the relevant prediction, distinction, action, or transfer;
- no unsupported understanding, validation, acceptance, or mastery claim was added.

Use [behavior-tests.md](references/behavior-tests.md) when validating or changing
this Skill. The scenarios are semantic acceptance cases, not response templates.
