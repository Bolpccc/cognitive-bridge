---
name: cognitive-bridge
description: "Bridge a specific gap in understanding with a faithful mental model, or compose an explanation requested by an upstream workflow. Not for routine answers or prose polishing."
metadata:
  version: 1.1.0
---

# Cognitive Bridge

Help the user predict, explain, distinguish, act, or transfer an idea by connecting
the supplied content to what they already understand. Choose the smallest useful
explanation; there is no required sequence or response template.

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

Use the user's purpose and demonstrated understanding to find the missing
relationship. Choose a concrete example, causal relation, formula, analogy, or
diagram when it helps; retain canonical terms and useful phrases from the user.
For formulas, connect the objects and operations to their meaning and conditions.

Match depth and entry point to the request. Direct action and review requests
should receive the action or actual state promptly. Keep conclusion-changing
conditions with the conclusion; add other detail only when it helps the user.
Use a comprehension check only when the learning task needs evidence, and do not
withhold a requested answer behind a lesson or quiz.

An upstream workflow may supply a Cognitive Bridge Request with `purpose`,
`source_content`, `must_preserve`, `source_anchors`, `current_model_evidence`, and
`desired_depth`. Honor those constraints when supplied; otherwise work directly
from the conversation without constructing a packet or interrogating the user.

Use [behavior-tests.md](references/behavior-tests.md) when changing or evaluating
this Skill. These are semantic acceptance cases, not steps for every invocation.
