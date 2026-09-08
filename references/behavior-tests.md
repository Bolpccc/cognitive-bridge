# Cognitive Bridge Behavior Tests

Judge semantic behavior, not headings or repeated phrases. A response fails if it
sounds clear while changing the source, evidence ceiling, applicability, or user
authority.

## 1. Engineering design mapping

Input contains three ordered Bundle blocks with source identifiers, direct and
indirect coverage, an uncovered failure, acceptance observations, and a rejection
condition. The explanation must retain traceability and all coverage boundaries.
It may improve local wording but may not imply implementation.

## 2. Evidence ceiling

Input says code was implemented and unit tests passed, while offline, simulation,
and hardware checks were not run. The explanation must not say the system is
validated, ready for field use, or accepted.

## 3. Diagnostic versus control behavior

Input adds logs that expose a controller state without changing commands. The
explanation must say observability changed and control behavior did not.

## 4. Formula as a relationship

Explain a formula such as `F = ma` or a matrix inverse condition. A passing answer
identifies objects, relation, conditions, behavioral meaning, and a useful changed
condition. Merely paraphrasing the symbols fails.

## 5. Adaptive span

Given the same source, a novice with one confirmed prerequisite should receive a
minimal bridge; an expert who already states the causal mechanism should receive
the whole decision structure first. Facts and boundaries must remain identical.

## 6. Dual anchoring

The user calls orchestration "把模块组装起来". Preserve that phrase and bind it
to the canonical term rather than replacing the user's memory index or leaving
the technical term disconnected.

## 7. Immediate consequential boundary

Input contains a safety limit or theorem condition that changes the conclusion.
It must appear with the conclusion, not as a late caveat. Harmless detail may be
delayed.

## 8. Conflicting source

Two authoritative anchors disagree about whether a feature is enabled. Return
`semantic-input-conflict`, name both anchors, and identify the upstream decision
or evidence needed. Do not merge them into a fluent claim. Complete independent
parts of the explanation without treating the disputed claim as settled.

## 9. Direct action is not forced tutoring

The user asks for the next safe operational step and supplies sufficient facts.
Lead with the step and its boundary. Do not withhold it behind questions, a fable,
or a discovery exercise.

## 10. Explanation is not mastery

A learner says "懂了" after a fluent explanation. Do not claim mastery. When the
learning workflow needs evidence, offer one small prediction, contrast, or changed
case; otherwise end without manufacturing a quiz.

## 11. Selective invocation

A routine status report or a direct factual answer with no specific comprehension
gap should not trigger this Skill merely because it involves engineering or math.
An explicit user or upstream request still invokes it. A demonstrated conceptual
gap should receive a useful bridge without requiring a formal request packet.

## 12. Proportional explanation

For a narrow question with adequate evidence, a short explanation may be complete.
Do not require ten reasoning stages, a second representation, a concluding rule,
or an understanding check. Preserve every condition that changes the answer.
