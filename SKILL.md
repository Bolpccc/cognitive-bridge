---
name: cognitive-bridge
description: "Bridge a specific comprehension gap (e.g. 没懂, 推不出来, 停在这里), or compose an upstream-requested explanation. Not for routine answers or prose polishing."
metadata:
  version: 1.2.0
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

Find the specific object, relation, justification, or boundary missing between
the user's demonstrated starting point and the requested understanding. When the
starting point is uncertain, use a provisional one that the user can correct;
do not invent a misconception or assume mastery. Supply only the prerequisites
needed to make the consequential connection explicit.

Choose an example, contrast, causal account, formula step, analogy, or overview
for that gap. Keep an example when continuity helps; replace it if it misleads.
Use canonical terms and the user's useful phrases, but do not let unfamiliar
terms stand in for the explanation. For formulas, connect objects and operations
to their meaning and conditions. Keep conclusion-changing conditions alongside
the conclusion.

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

An upstream workflow may supply a Cognitive Bridge Request with `purpose`,
`source_content`, `must_preserve`, `source_anchors`, `current_model_evidence`, and
`desired_depth`. Honor those constraints when supplied; otherwise work directly
from the conversation without constructing a packet or interrogating the user.

Use [behavior-tests.md](references/behavior-tests.md) when changing or evaluating
this Skill. These are semantic acceptance cases, not steps for every invocation.
