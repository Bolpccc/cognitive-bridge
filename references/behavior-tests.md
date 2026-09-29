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

## 13. Repair the missing relation

The user knows that two modules communicate through an interface but cannot see
why a replacement remains compatible only if the caller's relied-on meaning is
preserved. Explain that dependency from the stated starting point. A slogan such
as "stable contracts reduce coupling" without the missing relation fails; a
fixed story or late reveal of the term is not required.

## 14. Breakpoint with a valid inference

The user understands the premise and says "停在这里，我不知道这一步为什么能推出下一步".
Repair that inference using the current objects and conditions before broadening
the topic. A synonym for the conclusion or an unrelated analogy does not repair it.

## 15. Breakpoint with an invalid inference

The supplied explanation concludes `f(1)=0` solely from `f'(1)=0`. Identify the
unsupported step and what extra information would be needed. Do not invent a
mechanism to make the conclusion appear justified.

## 16. Support follows demonstrated knowledge

Two users ask about the same mechanism. One states the relevant prerequisite but
misses a single link; the other cannot identify the objects. Supply the missing
link to the first and establish the objects for the second. Do not infer either
user's knowledge from confidence, occupation, or terse wording.

## 17. Requested overview and no-quiz boundary

If the user asks for the whole structure before details, give a concise overview
with consequential boundaries. If the user asks a local question and says "不要出题",
answer it without a check. Neither request requires a fixed example-first chain.

## 18. A check only when it serves learning

For a learning task that needs evidence, offer a small prediction or changed case
after the complete explanation unless the teaching owner already owns the check.
For direct action, review, or a user opt-out, end without one. A check never proves
mastery by itself or blocks the requested answer.

## 19. Key links across purposes

With `purpose=act`, lead with the action and limit, then explain a necessary
unfamiliar condition. With `purpose=review`, lead with actual state and evidence
level, then explain why the missing evidence limits the claim. Neither mode should
turn into a full lesson or leave its conclusion resting on unexplained jargon.
