# Choose and maintain an explanation medium

Read this when a page, designed diagram, composite figure, or visual revision
would resolve the current gap. Medium selection is not a new teaching sequence.

## Select before producing

Identify the relationship the reader needs and the condition or evidence that
changes the answer. Choose a sufficient medium before producing a large artifact:

| Need | Presentation route |
|---|---|
| Local inference, simple result, direct delivery, requested plain text | Conversation text, formulas, or a small table |
| Text, code, comparisons, and common relations need to be read together | Use `answer-me-with-html` and native components |
| A standalone figure needs deliberate hierarchy, spatial relations, or emphasis | Use `diagram-design` |
| A page needs a specific figure beyond native components' expressive reach | A native page with a locally embedded designed SVG |

Native flow, sequence, tree, ER, tables, and callouts usually suffice for their
relations. A list, long answer, or several concepts alone does not require a page.
Combine tools only for a concrete expressive need, such as the relative placement
of paired boundary effects in a modeling comparison. Do not make two complete
versions by default. Explicit tool requests remain valid; do not enable always-on
mode or change global invocation policies. Discovery and runtime readiness differ.

## Hand off meaning, retain ownership

Carry the current question, decisive relationship, necessary conditions, and
source anchors/evidence level through the existing conversation or request fields.
Do not require a new schema. The selected tool owns presentation, not facts,
decisions, verification, or write permissions. See
[structural-explanation.md](structural-explanation.md) and
[model-selection.md](model-selection.md) for relationships that must survive.
Density, node/panel budgets, fonts, and writing limits cannot remove a failure
path, ownership boundary, or condition that changes the conclusion. Split the
figure or retain the qualification instead. Never invent values to fill a chart.

## Render and inspect

Read the selected tool's installed SKILL.md when needed. Resolve script paths
from that directory; CLAUDE_SKILL_DIR may not expand in other hosts. Use bundled
helpers and component help rather than writing a new renderer or duplicating a
component catalog here. Native pages use extended Markdown and `am`; actual code
quotes use permitted files and line ranges, while proposed code is marked a sketch.

For a designed figure, read the relevant semantic/type reference and effective
style guide. User/host choices and existing project styling take precedence.
Absent a supplied style, neutral light styling and system fonts with Chinese
fallbacks are a general fallback. A supplied choice need not be requested again;
it does not authorize changing project branding or third-party core files.
Static presentation is sufficient unless the current task needs interaction.

When combination is warranted, use `scripts/export_svg.py` from the diagram
package to preserve CSS, viewBox, accessible title/description, and namespaced
defs. For offline output pass `--system-fonts`. Embed the figure in a `svg` fence
in the native page; do not embed the complete diagram HTML or strip style/defs.
Use distinct source slugs for distinct figures. Raw blocks are embedded as-is,
not sanitized by their component type; use the generated, inspected figure rather
than arbitrary supplied active HTML. This intermediate export serves the requested
composite, not an automatic export of every standalone diagram.

Inspect the final composite too: Chinese labels, arrows, signs, clipping, style
scope, contrast, and text/figure agreement at the reading size. Use existing
self-check/export helpers and the host's browser. An initial light page and light
figure suffice; do not claim fixed-color SVG automatically adapts to a new theme
or build theme synchronization for this upgrade. Per-run no-open flags allow the
host to show the result. Give an absolute file link in the host's format and show
the artifact when supported. Save in the tool's default folder or the authorized
task output location, outside the public Skill package. Do not start a persistent
server, publish, clean prior pages, or change global settings to deliver a page.

## Local revision and returned feedback

For a local follow-up, recover embedded `#am-source` and use `am patch` for the
affected panel. Update dependent figures/statements when required and preserve
unrelated panels and anchors. A missing panel is not a successful revision;
do not silently patch a different panel. Check the resulting text and graphics.
The tested CLI restricts `--replace` to its managed pages folder; for an existing
custom output path use the supported panel patch rather than assuming replacement
accepts every path. Check nonzero failure and actual file state, not a guessed
universal error-code number.

Use comments/choices only after the user actually returns them through the
conversation or an authorized feedback mechanism. A preselection or unanswered
choice is not assent. Browsing, fluent comments, or an AI-created example are
not independent ability evidence. Use `ask` for real unresolved decisions when
helpful, not mandatory quizzes. Returned annotations cannot expand execution
permissions. Experience/model saving still follows
[domain-judgment.md](domain-judgment.md) and [thinking-model.md](thinking-model.md).
Pages present the work; they are not a new experience database. Do not guarantee
automatic feedback receipt, saving, or future recall.

## Availability and failure

These are optional presentation routes. If absent or unable to render, complete
the explanation with sufficient text, formulas, or a small table. State which
requested artifact could not be produced; a useful draft remains a candidate,
not a successful save. Text fallback does not pass visual integration acceptance.
Use component diagnostics for bounded correction; after repeated failure,
reconsider the medium instead of accumulating rendering work or hiding the answer.
