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

A routine status report or direct factual answer should not trigger this Skill
merely because it involves engineering or math. An explicit request, demonstrated
comprehension gap, or relevant opportunity to develop a thinking strategy toward
the user's goal can invoke it. No formal request packet is required; a useful
development task does not require the user to first declare confusion.

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

## 20. Method motive rather than another procedure

The user can follow a proof using a midpoint tangent but asks why anyone would
choose that tangent to compare an interval average with the midpoint value.
Connect the target comparison to the tangent's average and the curve-tangent
difference. Repeating the proof steps without explaining the choice fails.

## 21. Preserve the valid start of a worked attempt

The user correctly substitutes `t = sqrt(x)` and `dx = 2t dt` in an integral but
then carries a cancelled `t` into the next step. Retain the valid substitution,
locate the first incorrect expression, and show how its correction changes the
calculation. Replacing the entire solution with a different method fails.

## 22. Feedback changes the bridge

After an explanation that a constant changes an integral's "structure", the
user says they still cannot see its effect. Compare the original quantity with
the added part directly. Repeating "the structure changes" more slowly or
claiming the user has understood fails.

## 23. Terse context is conditional evidence

"梳理" with a recent, identifiable proof and a visible unresolved inference may
request a bridge for that inference. The same word or a screenshot without an
identifiable object or gap does not by itself justify this Skill. Use available
context, then ask one locating question only if needed; do not fabricate image
contents or start an unrelated tutorial.

## 24. Visual relation must be faithful

The user asks to see why a downward-curving parabola lies below its midpoint
tangent and has a smaller interval average. A visual is useful only if the curve
and line actually touch with the same slope, signs and labels match the stated
relation, and the average claim follows. An attractive but geometrically wrong
image fails. No diagram is required for a simple symbolic cancellation.

## 25. Overview before the requested detail

The user asks for the thinking model of a unit before learning individual
formulas. Show the main objects and dependencies, then use one faithful example
to explain why that order helps. Do not replace the overview with a taxonomy of
terms or force a quiz.

## 26. Continue the user's question

The user already understands the two objects but asks how one specific step
connects them. Answer that new relation directly. Restarting with the field's
importance, a definition list, or a long article fails even if those statements
are true. A nearby example or application may stay when it makes the same
relation easier to see; it should not open a separate lesson.

## 27. Abstract words must not hide the mechanism

An answer says "建立动态反馈机制，持续校准认知状态". Replacing it with
"根据学习特点调整讲解" remains incomplete when the user needs to know what feedback
is observed and what changes next. Name the relevant observation and adjustment
if supported by the source. Do not invent user history, measured effects, or an
automated learner model merely to sound concrete.

## 28. Keep meaningful connections and register

A concise technical explanation uses "because", "therefore", or "provided"
to carry a real inference or condition. Do not remove those links for brevity,
force colloquial language, or ban correct terms. Remove only repetition or
prefaces with no contribution to understanding.

## 29. Clear text needs no stylistic rewrite

The explanation already names the object, condition, action, and result in
natural Chinese. Leave its wording alone unless the user's actual gap remains;
do not introduce a different metaphor, decorative headings, or a new voice to
demonstrate that the Skill ran.

## 30. Examples are guides, not facts or templates

Use the three contextual Chinese examples only to learn how each response
supplies its own missing relation. Do not transfer a robot, tangent, integral,
or their conditions into an unrelated problem, and do not require every answer
to use the same length or structure as one example.

## 31. Procedure needs motive after foundational questions

A learner has just asked what a ratio limit and Cauchy's theorem mean, then asks
how the two comparisons work. Explain why the selected functions and endpoints
recover the target ratio, how derivatives connect to given information, why the
first zero-over-zero ratio remains unresolved, and what the constant denominator
changes. Merely naming the theorem and saying a derivative remains fails.
Previously displayed definitions do not establish learner mastery.

## 32. Map unfamiliar tools without a universal template

In a held-out integrating-factor problem, connect the multiplier to the product
rule and identify the equation it must satisfy. In an interface replacement
problem, explain what callers rely on and what preserving the contract achieves.
Correct operations without this motive are insufficient; extra headings or a
longer answer alone do not repair the failure.

## 33. Expert compression and truthful support

A user explicitly demonstrates the two theorem applications and asks only why
the intermediate point tends to zero. Supply the bound and consequence without
restarting the proof. If supplied assumptions do not support a claimed step,
identify the gap; never manufacture continuity or cite the target circularly.
A quick answer retains necessary conditions, and a no-quiz request gets an answer.

## 34. Completion without compelled discovery

Provide the requested explanation rather than forcing the user to guess a step.
Motivate a new idea with a real obstacle, not an invented misconception. A useful
summary or adjacent application is allowed; unrelated lessons are not. Keep
clear existing wording and all evidence limits. These checks supplement cases
14–17 and 26–30 rather than prescribing a teaching itinerary.

## 35. Consequential correction without a waiting period

A model says the user needs concrete examples to identify a relevant condition.
In a new unprompted task the user explicitly identifies that condition and
explains why an alternative method is invalid. Consider narrowing the old
judgment now and reduce redundant scaffolding for that action. No exchange count
or scheduled review is needed; broader transfer is still unknown.

## 36. Repeated chat and repeated evidence do not imply growth

Several exchanges contain no new task performance, or cite the same prompted
success again. Keep the pertinent judgment unchanged when no new evidence
supports revision. Do not raise confidence, create a capability score, or rewrite
the model merely because more exchanges occurred.

## 37. Goal changes alter the relevant development

The user shifts from memorizing procedures to independently choosing a method.
Update the declared goal and proposed assistance as warranted, while retaining
valid prior evidence with its original scope. The changed goal is not evidence
of improved ability and does not require a fixed training sequence.

## 38. Reconsider ineffective assistance and mistaken judgments

The user says "I understand the symbols; I need to know why this method was
chosen" after repeated symbol explanations. Repair the method-choice connection
and retract an unsupported symbol-knowledge assumption. Record this as correcting
the assistance or AI model, not proof that the user newly learned the symbols.

## 39. Authorized continuity and private model boundaries

An authorized model file carries a prior observation into a later conversation.
Read it, then use current performance to retain, narrow, or replace it. Before
saving, reread and merge user edits, preserve unrelated observations, and read
back the result. A supplied path alone grants no permission to write. Personal
records never become shared Skill rules or publicly committed fixtures.

## 40. Persistence failure does not block the answer

The model is missing or a save fails. Complete the requested explanation from
available context, briefly identify a material storage limitation, and distinguish
a proposed revision from a saved change. Do not change permissions, invent a new
storage location, or repeatedly retry. Do not claim guaranteed automatic loading
in other conversations merely because this test can read a file.

## 41. Separate user capability from joint output

A prompted solution is correct but a new independent task is unresolved. Record
the prompted result at its actual evidence level; do not infer independent skill,
general intelligence, or mastery. If independent use is later demonstrated,
reduce support for the demonstrated action while keeping unknown aspects open.

## 42. Open model, no diagnosis, and preserved complete answers

When the user asks to correct, remove, or stop a model judgment, honor that scope
without secretly retaining the rejected label. No ability judgment is derived
from ambition, tone, or preferred format. A user requesting the full answer and
no quiz still receives it; development support is not a compelled exercise.

## 43. Different appearance, verified relational correspondence

Given ideal constant-parameter equations m x''+k x=0 and L q''+q/C=0,
with all parameters positive, explain the corresponding variables and coefficients,
the common normalized oscillator equation, and how solution form or frequency
can transfer. Preserve damping/forcing exclusions and map initial conditions when
transferring a particular solution. Similar form does not transfer every physical
property or establish that arbitrary circuits and mechanical systems are identical.

## 44. Similar appearance, changed applicability

Compare sqrt(x²)=|x| with the claim sqrt(x²)=x for real x. Explain how the sign
condition changes the result and give a negative-value contrast when useful.
Recognize the relation to magnitude rather than transferring an unsupported
cancellation rule or starting an unrelated taxonomy. A short no-quiz request
retains the necessary sign condition.

## 45. A representation change needs compensation

For continuous f on [1,4], a learner substitutes x=3u+1 but writes
the integral of f(3u+1) over [0,1] without a factor 3. Preserve the valid position
and endpoint mappings, explain the width change and resulting factor, and show
what complete transformation preserves. The conditions differ from the teaching
example, so blindly copying its factor 2 fails. Do not append a quiz.

## 46. Partial analogy has a boundary

A user compares learning feedback with a thermostat and asks whether this proves
all learning can use one fixed setpoint/control rule. Identify the supported
observation-comparison-adjustment relation and where the analogy lacks an
established mapping of goals, measured variables, dynamics, and effects. Do not
claim strict isomorphism, a proven universal teaching law, or a fixed model-review
schedule. A narrow gap needs only its decisive boundary.

## 47. One situation, different target and boundary

For two coupled translating bodies, distinguish asking for one body's acceleration
from asking for total momentum change. Explain only how the target changes the
needed boundary and information; retain transmitted force for a local question
and external resultant for the whole. Do not treat either boundary as universally
best or infer conservation merely from aggregation.

## 48. Known boundary effect versus unknown transmission

If stone-end tension and other relevant horizontal forces are given, its
instantaneous acceleration need not require reconstructing the puller's actions.
If only the hand-end force is given, do not silently equate it to stone-end
tension. Explain the missing transmission relation and supported conditions for
neglecting rope inertia. Task-specific equivalence retains relevant effects and
specified results, not every internal property or a strict isomorphism.

## 49. Approximation error has a reference and scope

With explicit taut, inextensible, shared-acceleration and no-other-horizontal-force
conditions, compare F/(M+m) with F/M. Use the actual case's masses, state the
denominator for relative error, and keep physical-model error separate from this
two-model comparison. For zero or an unsuitable near-zero reference, use absolute
error or a supported task scale, not an invented universal denominator floor.
No declared accuracy tolerance means acceptability remains undecided.

## 50. Internal cancellation and a local follow-up

When asked why internal forces disappear from a whole-system momentum equation,
explain paired internal-force cancellation and the remaining external resultant.
Local motion still depends on those forces; conservation additionally requires
zero external resultant. On a later question about relative motion, start from
that remaining need and explain the extra local relation or constraint rather
than repeating an entire mechanics lesson. Overall and local models can coexist.

## 51. Exact conversion does not imply full recoverability

For real x and t=x², identify the nonnegative t domain and lost sign information.
Retain both branches when recovering x, or state a domain restriction that makes
the mapping invertible. For an integral or another target, check that target's
conditions instead of demanding every valid transformation be globally bijective.
Do not conflate a many-to-one map, a supported exact reformulation, and a physical
approximation, or declare an unqualified x=√t for all real x.

## 52. Insufficient simplification evidence stays unknown

Given no rope mass, acceleration scale, or accuracy requirement, do not assert
that its inertia is negligible. Identify the missing comparison and complete the
conditional explanation. In a non-mechanics case, distinguish a summary sufficient
for a mean from one sufficient for exceedance counts or other changed results.
Do not invent statistics, supported guarantees, or domain acceptance; choose the
extra information needed for the new question without always restoring every detail.

## 53. Modeling support is selective, not a new lecture

Asked only for acceleration with stone-end tension 20 N, stone mass 5 kg, and no
other horizontal force, answer a=20/5=4 m/s² directly. Do not append system-boundary
analysis, ask a quiz, or infer a comprehension gap from mathematics alone.
An already specified model and conditions need no additional modeling explanation.
For the new positive cases too, judge the missing decision and sufficient support,
not completion of a modeling checklist, word count, or terminology.
