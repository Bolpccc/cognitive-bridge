# Cognitive Bridge

`cognitive-bridge` is a public Agent Skill for turning domain-bounded content into
an explanation that helps a person form a faithful, usable mental model with less
avoidable cognitive work.

It is not a general prose humanizer and does not replace domain expertise. The
source owner still controls facts, formal conditions, evidence, safety,
persistence, and decisions.
The Skill chooses the cognitive entry point, representation, span, and final
compression.

Current release: `v1.5.0`. See [VERSIONING.md](VERSIONING.md) for the SemVer
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

A visual may make a spatial relation easier to inspect, but it can also teach a
false relationship if the geometry or labels are wrong. The Skill therefore
allows a visual when useful and requires the represented relation to be checked;
it does not require one for every explanation or prescribe a production tool.

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
