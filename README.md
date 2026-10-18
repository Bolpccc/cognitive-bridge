# Cognitive Bridge

`cognitive-bridge` helps with real problems like a knowledgeable colleague:
notice when an established concept, theory, or method opens a useful way to
understand, distinguish, search, decide, or act, and explain its fit and limits.
It also repairs a specific missing connection when the user is stuck. Helpful
knowledge need not change the immediate plan; better recognition and transfer
are worthwhile too. A direct answer is sufficient when extra explanation adds
nothing to the task.

Local package version: `v3.0.0` (not a publication claim). This major version
changes the default emphasis from gap repair and learner support to knowledge
selection and proportionate collaboration. Existing request fields, domain
ownership, personal-model authorization, and optional presentation routes remain
compatible. See [VERSIONING.md](VERSIONING.md) and [CHANGELOG.md](CHANGELOG.md).

## Install

```bash
git clone https://github.com/Bolpccc/cognitive-bridge.git \
  ~/.codex/skills/cognitive-bridge
```

This repository's local installer deletes and rebuilds an existing target.
For an installation with local changes, compare and back up first, then merge
and synchronize affected files instead of using that replacement path. A local
checkout or installation does not imply the public repository has this version.

## Use

```text
Use $cognitive-bridge to help with this problem: notice useful established
ideas, explain why they fit, and repair any missing connection without
turning the task into a lesson.
```

Selection depends on what an idea contributes to the actual question, not on
how many relevant terms exist. It may expose a distinction, a known method,
a failure or a trade-off; competing explanations may remain provisional.
Names and specific recommendations need appropriate evidence. The
[concept-introduction contrasts](references/concept-introduction.md) illustrate
selection and restraint without prescribing a reply template or term quota.

The [derivation](references/derivation-example.md),
[structural](references/structural-explanation.md), and
[model-selection](references/model-selection.md) contrasts retain the existing
support for method rationale, correspondence, compensation, and conditional
simplification. Ordinary calculations and explicit direct-answer requests stay
direct. Headers, summaries, checks, and visuals are choices, not required or
forbidden forms. User requests and upstream source/answer constraints still govern.

Personal models and [domain experience](references/domain-judgment.md) remain
background support under the user's or active workspace's authorization. Relevant
calls still read a supplied model as instructed; details are in
[thinking-model guidance](references/thinking-model.md). Answer length can follow
the current request without a capability assessment. Changes to an ability
judgment still require actual performance evidence, and review remains dynamic.
Records stay in their authorized existing locations, outside the public package.
Unavailable records or failed writes do not block the answer or establish saved
state. These instructions are not a background listener or a learning-outcome claim.

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

Anonymized study conversations informed earlier explanation support. Users repeatedly asked
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

The [v3.0.0 local validation record](evals/results/v3.0.0.md) documents the core
rewrite, preservation checks, and the distinction between authored answer
contrasts and independent behavior evidence. The older browser acceptance gap
remains separate; local v3.0.0 installation does not close it.
