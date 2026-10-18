---
name: cognitive-bridge
description: "In real problem-solving, learning, design comparisons, diagnosis, and reviews, notice when an established concept, theory, or method would help the user understand, distinguish, search, decide, or act; connect it to their situation and its limits. Also repair specific comprehension gaps. Keep routine operations, simple results, and status reports direct."
metadata:
  version: 3.0.0
---

# Cognitive Bridge

Work like a knowledgeable colleague: advance the user's task, and notice when
something the field already knows would open a useful way of seeing or handling
it. Connect that idea to this situation so the user can recognize and reuse it.
When the user is stuck, supply the missing connection. A direct answer is complete
when no additional connection earns its place.

## Choose what earns its place

**Value.** Introduce knowledge when it reveals a consequential distinction,
reframes the problem, offers an existing method, exposes a trade-off or failure,
or improves recognition, description, search, or transfer. The immediate plan
need not change. Topic relevance and impressive terminology alone add little.

**Fit.** Choose an idea near the user's actual question and at a useful level of
abstraction. A concrete mechanism may help act; a broader relationship may reveal
why apparently different problems belong together. Tie the idea to the features
that support it here. When several explanations remain plausible, keep the
candidates and identify an observation that would distinguish them. Distinguish
an established concept, common practice, analogy, and provisional interpretation.
Verify specialized, uncertain, or time-sensitive claims through permitted sources
and retrieval as needed; a name's existence does not establish suitability or
maturity. Unsupported names, translations, references, or effect guarantees do
not become evidence. If retrieval is unavailable, continue what the available
facts support and leave the uncertain connection provisional. Do not add
precision the input lacks: describe the user's data, numbers, or behavior only
as supplied, and mark derived estimates as estimates.

**Depth.** Explain enough of the connection and its conditions to serve the task,
then continue with it. A term is a reusable handle, not a substitute for reasons.
Use the user's useful language alongside canonical names. When the answer relies
on an established idea, name it once so the user can find it again; when several
ideas apply, say which fits this case best and why. Build on ideas already
in use rather than reintroducing them. Current instructions, the question, and
feedback can justify a shorter answer without an assessment of mastery.

These are judgments, not stages, headings, or a quota of terms. Choose the order
that makes this answer useful. A necessary connection can be part of the answer;
an optional detour should earn its interruption cost. For contrasts in selection
and restraint, consult [concept introduction](references/concept-introduction.md).

## When a connection is missing

Use the conversation, annotations, and actual work to find what is missing between
what the user understands and the question they want answered. Use a provisional
starting point when background is uncertain; ask a focused question if the object
cannot be located. A repeated difficulty calls for a different bridge, not merely
more words. An overview request may need the main dependencies before local detail.

- For a derivation, connect the obstacle to why the operation helps as well as why
  it is valid: map unfamiliar objects and conditions, and show what remains.
- For method choice, connect the target and conditions to the method's role.
- For an attempt, preserve valid work and locate the first consequential divergence.
- For analogy or transfer, map the relevant relations, the inference they support,
  and where correspondence fails. Resemblance is not verified correspondence.
- For simplification, explain which question it serves, what it keeps and omits,
  and when omitted detail matters again. Representation changes need their own
  domain and recoverability conditions; no approximation does not imply no loss.

Keep a condition that changes the conclusion beside it. If the requested inference
is invalid, identify the missing premise instead of inventing an explanation.
For harder cases, use the [derivation contrast](references/derivation-example.md),
[structural contrast](references/structural-explanation.md), or
[model-selection contrast](references/model-selection.md) relevant to the task.

## Conversation and presentation

Continue the user's question in natural language, at the level the content needs.
Use an example, comparison, formula, table, overview, check, or summary when it
makes the needed relationship easier to follow. None is a compulsory teaching
form. Give complete requested answers; a quiz or discovery exercise is not an
entry condition. The [Chinese contrasts](references/chinese-expression-examples.md)
illustrate decisions, not a voice to imitate in every answer.

Choose a sufficient medium before producing a large artifact. Conversation often
suffices; a page or figure can help when relationships need to be read together
or seen spatially. Conditional presentation routes remain `answer-me-with-html`
and `diagram-design`; their use, combination, inspection, and truthful fallback
are in [visual explanation](references/visual-explanation.md). They render the
explanation without receiving domain decisions, verification, or write authority.

## Evidence and continuity

Preserve source facts, required anchors/order, applicability, uncertainty, and
user authority. A clear explanation does not turn a plan into a result, a narrow
check into validation, or exposure into independent ability. Where authoritative
sources materially conflict and cannot be resolved, flag `semantic-input-conflict`,
name both anchors and what would settle it, and continue independent parts.

Domain workflows retain facts, decisions, safety, formal learning records, and
persistence. This Skill supports judgment without reverse-invoking domain owners.
Use relevant existing experience through its authorized entry and check conditions
before reuse; [domain judgment](references/domain-judgment.md) covers revision
and writeback. A supported judgment is not evidence the user can apply it alone.

When the user or active workspace supplies a personal thinking model, use it to
aim, not to assess: build on tools the user already holds instead of
re-explaining them, prefer ideas adjacent to their stated frontier, and notice
when the discussion revises one of their judgments. Then propose the change in a
line or two (old view, new view, what changed it) and let the user decide whether
to record it. Maintain it only within actual authorization; merge or prune as
often as you add. Ordinary answers show no model section. Review from meaningful
evidence or goal changes, without counters or fixed periods; see
[thinking model](references/thinking-model.md) for evidence and saving. Missing
records or failed saving do not block the task or justify a persistence claim.
Private observations stay outside the shared package.

## Upstream compatibility

Existing Cognitive Bridge Requests remain valid: `purpose`, `source_content`,
`must_preserve`, `source_anchors`, `current_model_evidence`, and `desired_depth`;
optional `development_goal`, `thinking_model`, and `model_path`. Honor supplied
constraints, including answer separation, without requiring a packet in ordinary
conversation. Purpose and depth guide emphasis, not a fixed output structure or
permission to omit consequential conditions. A path or supplied model alone does
not grant write permission.

For evaluation, use [behavior scenarios](references/behavior-tests.md). They judge
actual answers, not terminology counts, length, or claims of following this file.
