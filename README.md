# Cognitive Bridge

`cognitive-bridge` is a public Agent Skill for turning domain-bounded content into
an explanation that helps a person form a faithful, usable mental model with less
cognitive work.

It does not humanize prose or replace domain expertise. The source owner still
controls facts, formal conditions, evidence, safety, persistence, and decisions.
The Skill chooses the cognitive entry point, representation, span, and final
compression.

Current release: `v1.0.0`. See [VERSIONING.md](VERSIONING.md) for the SemVer
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
