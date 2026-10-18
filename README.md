# Cognitive Bridge

`cognitive-bridge` is a public Agent Skill for bridging comprehension gaps and
developing thinking strategies toward a user's chosen goals. It connects useful
explanations, a concise revisable thinking model, and subsequent performance that
can change both the model and the assistance. In real tasks it can also help form,
reuse, and calibrate domain judgments using relevant existing experience.

It is not a general prose humanizer and does not replace domain expertise. The
source owner still controls facts, formal conditions, evidence, safety,
domain persistence, and decisions. The Skill may maintain a personal thinking
model only within the user's authorization; formal learning records and mastery
judgments remain with their domain owners.

Local package version: `v2.4.0` (not a publication claim). See [VERSIONING.md](VERSIONING.md) for the SemVer
contract and [CHANGELOG.md](CHANGELOG.md) for release history.

## Install

```bash
git clone https://github.com/Bolpccc/cognitive-bridge.git \
  ~/.codex/skills/cognitive-bridge
```

## Use

```text
Use $cognitive-bridge to explain this from what I already understand while
preserving every condition and evidence boundary.
```

Use it selectively in learning, reasoning, and solution discussions when it can
help with a comprehension gap or a thinking strategy relevant to the current
goal. Solution comparisons, diagnosis, and result reviews can offer useful
judgment opportunities without an explicit declaration of confusion. Current
understanding and interruption cost determine whether extra support is useful;
routine operations, simple results, and status reports remain direct answers. Existing
request fields remain valid; optional `development_goal`, `thinking_model`, and
`model_path` carry a goal, model content, or location without granting permission
to write by themselves.

For a structural gap, the explanation can expose relevant object/relationship
correspondences, why a transformation preserves the target, its required
compensation, and where a method or analogy stops applying. The
[structural explanation contrast](references/structural-explanation.md) uses a
continuous-function linear substitution; it is optional support, not a fixed
teaching sequence. Resemblance, partial correspondence, and a verified isomorphism
remain distinct. Existing invocation scope, inputs, and ownership remain unchanged.

When the missing judgment concerns choosing or simplifying a model, explain why
the question needs certain relationships and why other details can be omitted
or must be restored. Task-specific equivalence preserves specified results under
specified conditions; exact representation changes still require domain and
recoverability checks. The optional [model-selection contrast](references/model-selection.md)
uses a person, rope, and stone to expose these choices and supported approximation
errors. It is explanation support, not authority to replace domain methods,
calculations, or validation. An already specified model and a local calculation
do not require an added modeling explanation.

Relevant prior experience can inform the next choice after checking which
conditions match and which changed. New results can narrow or correct an old
judgment; changed conditions are different from a mistake in the prior reasoning.
The optional [domain-judgment guidance](references/domain-judgment.md) explains
evidence and writeback. Use existing domain records and their authorized workflow,
not a new experience library or automatic chat archive. Existing `source_content`
and `source_anchors` can carry experience and its provenance; no new required
request fields or domain write permissions are introduced. An unavailable record
or failed saving leaves a candidate in the current answer when useful, not a
claim of persistence or guaranteed recall in another conversation.

For continuity, provide a model or add its authorized local location and write
scope to your active workspace instructions. On relevant calls, the Skill reads
that model, adapts assistance, and reviews consequential judgments when new
evidence or goals warrant it. There is no fixed exchange count or review period.
Private model records stay outside this repository and the installed package.
An unavailable model never blocks the requested explanation. See the
[thinking-model guidance](references/thinking-model.md) for evidence and saving.
This is an agent instruction workflow, not a background listener or guaranteed
activation in chats that do not load the Skill and model.

MIT License. See [LICENSE](LICENSE).

## Design basis

The Skill uses cognitive and learning research to choose support for a specific
gap. These studies do not establish that this Skill improves human learning:

| Research observation | Design inference and limit |
|---|---|
| [Text coherence interacts with background knowledge](https://doi.org/10.1207/s1532690xci1401_1) in experiments with science texts. | Start from knowledge the user has shown and make necessary links explicit. A conversation is not the same setting as those texts. |
| [Self-explanation prompts improved understanding](https://doi.org/10.1207/s15516709cog1803_3) in a small study of eighth-grade readers. | Ask for a prediction or explanation when the learning task needs evidence, not after every answer. A question alone does not establish mastery. |
| [The usefulness of instructional support changed with learner experience](https://doi.org/10.1037/0022-0663.92.1.126) in multimedia instruction experiments. | Compress demonstrated prerequisites and expand only the current gap. This does not justify inferring expertise from tone. |
| [Reported feeling of learning differed from measured learning](https://doi.org/10.1073/pnas.1821936116) in a university physics study. | Evaluate ease of following an answer separately from independent explanation or transfer. Neither measure alone proves this Skill works. |

The durable aim is to expose the relationships needed for a sound answer while
preserving the source. Examples, terminology order, overviews, and checks are
replaceable ways to do that, not a mandatory lesson sequence.

Natural Chinese expression is a writing and task-context choice, not a result
established by cognitive or neuroscience research. We drew on
[Humanizer-zh](https://github.com/op7418/Humanizer-zh) for context-sensitive
checks of empty phrasing, repetition, voice, and preservation of facts and
certainty. This repository does not depend on or run that editing Skill. Its
[anonymized contextual examples](references/chinese-expression-examples.md)
show how explanation choices vary with the user's question; they are not output
templates or evidence of improved learning.

## Usage-derived design hypotheses

Anonymized study conversations informed this release. Users repeatedly asked
why a proof step follows, why a method was chosen, where their own attempt first
went wrong, or how a local idea fits the whole topic. The Skill now selects
support for those distinct needs and treats a repeated "still don't understand"
as evidence to reconsider the diagnosed gap. A short "梳理" or an image can use
earlier context only when it identifies the learning object and missing link.
These are design inferences from observed requests, not measured improvements
in learning or evidence that the pattern applies to every user or subject.

A visual may make a spatial relation easier to inspect, but wrong geometry or
labels can teach a false relationship. Choose a medium for the current gap:
conversation text for local results, `answer-me-with-html` native components for
mixed explanation pages, or `diagram-design` for a deliberately designed figure.
Combine only when a specific figure cannot be adequately expressed natively.
The optional [visual-explanation guidance](references/visual-explanation.md)
covers handoff, SVG export, local patching, actual returned feedback, and fallback.
These conditional external routes are not hard dependencies of a useful answer.
No always-on rule, new renderer, storage platform, or input field is introduced.
Presentation tools do not receive domain decision or write authority.

The local integration was imported from fixed upstream commits:
[answer-me-with-html](https://github.com/QingYunA/answer-me-with-html/tree/533c39fd47d814a6bee3d9c1df388345f4e4c858/skills/answer-me-with-html)
(CLI 0.5.0, Node.js 20+) and
[diagram-design](https://github.com/cathrynlavery/diagram-design/tree/7a2e22170ee838e859d8142ba825d83f8b6375e6/skills/diagram-design)
(Skill metadata 2.6, packaged Python self-check/export helpers). They remain
independent packages; their code and license copies are not vendored here.
Use the existing skill-installer with those repository paths and fixed refs when
installing the optional routes. Basic package validation does not require them;
`--installed-root` requires both for full integration availability checks. Do not
invent stable SemVer metadata for an upstream package that does not expose it.

## Validation layers

`python3 scripts/validate.py` checks metadata, links, declared dependencies and routes,
and explicit operational invocation references. The invocation linter skips fenced
examples, history/example sections and prohibitions; it is not a semantic parser.
`depends_on` must be acyclic; `routes_to` may intentionally return to another owner.
Run `python3 -m unittest discover -s tests -v` for deterministic negative cases.

`python3 scripts/validate.py --installed-root ~/.codex/skills` additionally checks
actual target availability and optional `external_version_constraints`. Bounds
use comma-separated stable SemVer comparisons (`>=`, `<`, `<=`, `>`, `==`).
Other external Skills without version metadata are checked for presence and name.
A missing companion can still use the documented fallback, but is not a passing
full-integration check. No command automatically installs dependencies.

Real-task fixtures live in `evals/cases.json`; their rubrics assess actual outputs,
not statements about following rules. Model evaluation is manual, not a CI job.
It does not measure human learning or establish a model/Skill superiority claim.
The fixtures paraphrase the observed requests without publishing original chats,
screenshots, names, or personal file paths.
Judge natural phrasing separately from whether the answer supplies the missing
relation and preserves formal conditions; do not use AI-detection scores as a
proxy for either outcome.

For a manual comparison, answer the same fixture in fresh contexts with and
without the Skill, using the same model and source facts. Shuffle and hide the
conditions before judging whether each answer starts from the supplied knowledge,
supplies the missing link, avoids needless expansion, and preserves source
conditions and evidence. Score readability separately from demonstrated
understanding. Only a learner's own explanation, prediction, or use in a changed
case can supply the latter evidence; those outcomes require a separate learner
evaluation and are not inferred from the fixture rubric.

## Why a step helps

The [derivation contrast](references/derivation-example.md) addresses a concrete
failure: correct formulas and theorem names can still leave a beginner to infer
why those steps were chosen. The design hypothesis is that explaining the
obstacle, applicability, object mapping, and effect of a step makes the missing
connection inspectable. It is not a universal sequence of human thought or an
established neuroscience result. Earlier exposure to a definition is not evidence
of understanding. Examples are anonymized reconstructions, not source transcripts.

Thinking-partner and cognitive-apprenticeship approaches informed the choice to
make method decisions visible; we do not import personality diagnoses, mandatory
mental-model menus, or a fixed coaching sequence. Requested complete answers
remain available, with necessary conditions and optional relevant extensions.

For release comparisons, use the previous release and candidate in fresh contexts
with the same model, reasoning setting, case context, and resource access. Keep
held-out integrating-factor and interface cases out of instructional examples.
Judge mathematical/domain correctness, method motive, object mapping, key links,
and unrelated expansion separately. Compare outputs against the deliberately
weak derivation as well; merely adding headings or length must not pass. Record
ties and regressions. This manual check complements the existing no-Skill
comparison and does not supply learner-understanding evidence.

The [v1.6.0 comparison record](evals/results/v1.6.0.md) includes actual outputs,
ties, partial explanations, and evaluation limitations.
The [v2.0.0 local validation record](evals/results/v2.0.0.md) separates package
checks, synthetic file checks, and author walkthroughs from unmeasured automatic
activation and learner outcomes.
The [v2.1.0 author walkthroughs](evals/results/v2.1.0.md) record structural-case
outputs and existing method/contract regressions, with no independent-run or
learner-effect claim.
The [v2.2.0 author walkthroughs](evals/results/v2.2.0.md) assess the missing
modeling judgment, proportionate support, conversion conditions, and the direct
calculation negative case. They retain the same evaluation limits.
The [v2.3.0 validation record](evals/results/v2.3.0.md) separates package checks,
synthetic storage checks, and domain-judgment author walkthroughs from unmeasured
implicit activation, independent behavioral reliability, and learner outcomes.
The [v2.4.0 local artifact record](evals/results/v2.4.0.md) records native pages,
designed SVG export, patching, negative cases and package readback. Browser visual
acceptance was blocked by the available UI access and remains pending; source
inspection and successful rendering are not a substitute for that check.
