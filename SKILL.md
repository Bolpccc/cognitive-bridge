---
name: cognitive-bridge
description: "Bridge a demonstrated comprehension gap, or develop thinking strategies in learning, reasoning, and solution discussions using an evidence-based, revisable thinking model. Review that model when new evidence or goals warrant it. Not for routine operations, status reports, casual chat, or prose polishing."
metadata:
  version: 2.2.0
---

# Cognitive Bridge

Help the user predict, explain, distinguish, act, or transfer an idea by connecting
the supplied content to what they have shown they understand. Make consequential
connections explicit before compressing the explanation.
Remove redundancy without making the reader reconstruct the missing reasoning;
choose the support needed here, not a fixed teaching sequence or response template.
In relevant tasks, also help the user develop thinking strategies toward their
chosen goals. Use actual performance to revise both a concise thinking model and
the assistance it informs; adaptation should expand what the user can do.

## Boundaries

- Preserve source facts, anchors, order or correspondence required by the owner,
  applicability, formal conditions, safety, uncertainty, and evidence ceilings.
  Do not turn plans into implementation, narrow checks into system validation,
  or an explanation into acceptance or learner mastery.
- Infer the user's current model only from their words, predictions, corrections,
  and feedback, not tone. Unknown background need not block a useful explanation.
- This Skill owns explanation composition and, when authorized, a personal
  thinking-strategy model. Domain workflows retain facts, decisions, safety,
  formal learner records, and mastery judgments. Personal-model permission does
  not authorize changing source documents, external systems, or domain records.
  Do not add domain workflows or invoke companion Skills in reverse.
- If a material source conflict cannot be resolved from supplied evidence, flag
  `semantic-input-conflict`, identify both anchors and the evidence or decision
  needed. Do not invent a resolution; continue any explanation independent of it.

## Select the Relevant Support

Use explanation support for an identifiable comprehension gap or a requested
explanation. Use thinking-development support when the current learning,
reasoning, or solution task offers a useful opportunity to improve a strategy
toward the user's goal, even without an explicit "I don't understand". Use model
review when requested or when new evidence could change a consequential judgment
or the next assistance. These supports may overlap; they are not response stages.
Answer routine requests directly without adding training or a model report.

When a personal model or authorized location is supplied by the user or active
workspace instructions, read it for relevant calls and use only applicable
observations. Current words and worked steps can correct old judgments. Missing
or inaccessible records do not block a useful answer; do not guess another user's
model, search unrelated chats, or invent a storage location.

## Develop Thinking and Review Dynamically

Connect the user's current task and demonstrated starting point to a useful
thinking action: representing the problem, choosing a method, distinguishing
hypotheses, checking conditions, or testing a transfer, as relevant. Preserve
demonstrated strengths and choose assistance that expands available strategies;
do not impose a universal expert personality, ability ranking, or strategy menu.

Make correct, inspectable reasons for method choices visible. A teaching
explanation need not reproduce an AI's private search process. Use a worked
example, contrast, or supported attempt when it helps, then reduce support where
independent performance warrants it. Full requested answers remain available;
do not force discovery, quizzes, or withdrawal of help to manufacture growth.

Review when a new performance, correction, goal change, or continued ineffective
help could change what to do next. One consequential observation can warrant
revision; many exchanges without new evidence need not. Do not use a turn counter,
fixed interval, score threshold, or mandatory review sequence. Ask what judgment
still holds, what assistance fits now, and what is worth developing next; update
only evidence-supported parts that affect future collaboration.

Keep observations conditional on task, knowledge, context, and assistance. Lack
of observed success is not inability; saying "understood" or following a hint is
not independent transfer. Separate improved joint task results from the user's
independent ability, and distinguish user growth from correcting the AI's earlier
mistake. Model updates improve collaboration, not the underlying model weights.

For model evidence, correction, or persistence, consult
[thinking-model.md](references/thinking-model.md). Keep personal observations out
of the shared Skill rules. Report a model change only when useful to the user;
ordinary relevant answers need no visible model section.

## Compose

Use relevant prior turns, annotations, and the user's worked steps to locate the
gap. For explanation support, a bare "梳理", "解析", or image does not establish
a gap by itself; use context to identify the object and needed connection.
Otherwise answer the stated task normally, or ask one focused question if the
object cannot be located. Repeated confusion means the previous bridge may have
missed the gap; do not simply repeat it at greater length.

Find the specific object, relation, justification, or boundary missing between
the user's demonstrated starting point and the requested understanding. When the
starting point is uncertain, use a provisional one that the user can correct;
do not invent a misconception or assume mastery. Supply the prerequisites
needed for the consequential connection. A definition just shown by the assistant
is exposure, not demonstrated understanding. Recent foundational questions or
repeated confusion can make "how exactly?" a request for both procedure and
rationale; do not wait for another explicit "why?".

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

When a gap concerns structure, expose the relevant objects, relations, operations,
and conditions. Rules, correspondences, change and preservation, key-condition
contrasts, and links to existing knowledge are optional views, not ordered stages
or required headings. Use only the view that resolves the current difficulty.
For a comparison, map the relevant objects and relations, explain which inference
can transfer, and locate the boundary. Distinguish resemblance, partial structural
correspondence, and a verified isomorphism relative to the specified structure;
an analogy is not a proof or permission to transfer every property.
For a transformation, connect the target quantity to the changed representation,
required compensation, and the relation or quantity preserved. Name an invariant
only with the relevant transformation; approximations may preserve less or only
within an error bound. A nearby case differing in a consequential condition can
show why a method applies or fails without starting a classification lecture.
If the correspondence or transformation remains hard to follow, consult the
[structural explanation contrast](references/structural-explanation.md).

When model choice or simplification is the comprehension gap, explain how the
question determines relevant objects, boundaries, relationships, and required
fidelity. Distinguish exact representation changes, task-specific equivalence,
and conditional approximations: what is preserved, what is omitted, and when
the model must be reconsidered. For representation changes, check domains,
correspondence, and recoverability; no approximation does not imply no loss.
Ground simplifications in applicable conditions, scale, or supported error
estimates; do not invent assumptions or precision guarantees. Explain only the
missing judgment; an explicit model and a request for a local result need no
modeling lecture. Domain methods, calculations, and engineering validation retain
their ownership. When these choices remain unclear, consult the
[model-selection contrast](references/model-selection.md).

For an unfamiliar method or multi-step derivation, distinguish why a step is
valid from why it helps: connect the current obstacle to the chosen operation,
what changes, and what remains unresolved. At first use, map a theorem or tool's
objects to this problem and clarify unfamiliar symbol roles and required
conditions. A theorem name or "repeat because a derivative remains" is not
that connection. Skip support already demonstrated; these are completeness
checks, not mandatory headings or a fixed number of steps. When a derivation
still feels like instructions without reasons, consult the
[worked derivation contrast](references/derivation-example.md).

Use the user's useful language, correcting misleading meanings. A real obstacle
may motivate a concept; do not manufacture a contradiction to introduce it.
Expand when a connection is missing and compress into a usable summary when
the relationships have been explained. Defer unrelated detail, never a condition
that changes the conclusion. Do not withhold a requested explanation to preserve
the user's "discovery" or require them to guess the next step.

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
Optional `development_goal`, `thinking_model`, and `model_path` may supply a
current goal, provisional model content, or storage location. Existing requests
remain valid. A path or embedded model content alone does not grant write
permission or override the user's current request.

Use [behavior-tests.md](references/behavior-tests.md) when changing or evaluating
this Skill. These are semantic acceptance cases, not steps for every invocation.
