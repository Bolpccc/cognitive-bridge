---
name: cognitive-bridge
description: "Explain a specific comprehension gap shown in the request or prior context (e.g. 没懂, 为什么这样做, 这一步求不下去, 这个条件有什么用), or an upstream-requested explanation. Bare 梳理/解析 or an image needs context that identifies the learning gap; not for routine answers or prose polishing."
metadata:
  version: 1.4.0
---

# Cognitive Bridge

Help the user predict, explain, distinguish, act, or transfer an idea by connecting
the supplied content to what they have shown they understand. Choose the shortest
complete explanation, not a fixed teaching sequence or response template.

## Boundaries

- Preserve source facts, anchors, order or correspondence required by the owner,
  applicability, formal conditions, safety, uncertainty, and evidence ceilings.
  Do not turn plans into implementation, narrow checks into system validation,
  or an explanation into acceptance or learner mastery.
- Infer the user's current model only from their words, predictions, corrections,
  and feedback, not tone. Unknown background need not block a useful explanation.
- This Skill owns composition only. Engineering, teaching, and other domain
  workflows retain facts, decisions, learner records, and persistence authority.
  Do not mutate source documents or external systems through this Skill, add
  domain workflows, or invoke companion Skills in reverse.
- If a material source conflict cannot be resolved from supplied evidence, flag
  `semantic-input-conflict`, identify both anchors and the evidence or decision
  needed. Do not invent a resolution; continue any explanation independent of it.

## Compose

Use relevant prior turns, annotations, and the user's worked steps to locate the
gap. A bare "梳理", "解析", or image does not establish one by itself; use this
Skill when context identifies the learning object and a needed connection.
Otherwise answer the stated task normally, or ask one focused question if the
object cannot be located. Repeated confusion means the previous bridge may have
missed the gap; do not simply repeat it at greater length.

Find the specific object, relation, justification, or boundary missing between
the user's demonstrated starting point and the requested understanding. When the
starting point is uncertain, use a provisional one that the user can correct;
do not invent a misconception or assume mastery. Supply only the prerequisites
needed to make the consequential connection explicit.

Match support to the need: for a local inference, show why that step follows or
why it does not; for a method-choice question, connect the goal and conditions
to the method's role; for a user-provided attempt, preserve valid work and locate
the first consequential divergence; for a requested overview, map the main
objects and dependencies before zooming in. These are choices, not stages to
run in every answer.

Choose an example, contrast, causal account, formula step, analogy, or overview
for that gap. Keep an example when continuity helps; replace it if it misleads.
Use canonical terms and the user's useful phrases, but do not let unfamiliar
terms stand in for the explanation. For formulas, connect objects and operations
to their meaning and conditions. Keep conclusion-changing conditions alongside
the conclusion.

When a spatial or structural relation remains hard to follow, or the user asks
to see it, consider a diagram or other visual. Check that its geometry, signs,
labels, and stated relationships are accurate before relying on it. Do not add
a visual when words or a small calculation make the connection clear enough.

When the user identifies a breakpoint, check that the claimed step follows from
its premises and source conditions. If it does, repair that connection before
expanding the topic. If it does not, identify the missing condition or unsupported
inference rather than manufacturing a bridge.

Let purpose determine what comes first: `understand` addresses the gap; `act`
gives the next action and boundary; `review` reports actual state and evidence
level while preserving required source order; `decide` states the consequential
choice and what changes it. Explain any key dependency in every mode. Let
`desired_depth` (`quick`, `standard`, or `deep`) change the amount of support,
never the conditions needed for a sound answer. A requested overview may come
first; a narrow breakpoint may need only one connection.

Use a comprehension check only when the learning task needs evidence and the
teaching owner has not taken responsibility for it. Do not add one when the user
opts out, withhold a requested answer behind a quiz, or treat a fluent response
as proof of mastery. Revise the provisional starting point when feedback shows
that the actual gap differs.

## Natural Chinese Explanation

Continue from the question the user just added and what is already clear; do not
restart a self-contained article for every follow-up. When an abstract sentence
hides who or what acts, under which condition, and with what result, expose the
needed relation rather than merely swapping jargon for colloquial synonyms.
Keep causal, contrast, and conditional links that help the reader follow the
argument; remove only prefaces or repetition that add no understanding. Choose
terms, formality, length, and structure for the task. Do not invent details to
sound concrete, weaken uncertainty, or rewrite sentences that are already clear.
An adjacent example or application can help establish or test the same relation;
use it when it earns its space, without drifting into a separate lesson.
When Chinese phrasing still obscures the bridge, consult
[contextual examples](references/chinese-expression-examples.md); borrow their
decisions, not their wording or facts.

An upstream workflow may supply a Cognitive Bridge Request with `purpose`,
`source_content`, `must_preserve`, `source_anchors`, `current_model_evidence`, and
`desired_depth`. Honor those constraints when supplied; otherwise work directly
from the conversation without constructing a packet or interrogating the user.

Use [behavior-tests.md](references/behavior-tests.md) when changing or evaluating
this Skill. These are semantic acceptance cases, not steps for every invocation.
