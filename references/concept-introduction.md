# Introduce an idea that earns its place

Read when choosing whether and how to introduce an established idea. These are
constructed contrasts, not diagnoses, user performance, or a reply template.
Their terminology is incidental: judge the connection and the next useful move.

## A concept opens a better question

**Situation:** A dashboard shows a higher overall completion rate, although both
groups' rates fell. Group A went from 90% to 80%, B from 50% to 40%; A's share
of cases rose from 20% to 80%. The question is whether the process improved.

**Weak:** This relates to statistics, aggregation, confounding, and Simpson's
paradox. Here are their definitions.

**Useful:** The overall rate rose from 58% to 72% because many more cases came
from the higher-rate group, even though each group's result fell. This is the
kind of reversal called Simpson's paradox. Compare the group rates and case mix
separately before attributing improvement to the process. These figures alone
do not establish what caused either change.

**Selection:** The idea changes which comparison answers the question. The
arithmetic is observable evidence for the aggregation effect, not a causal study.

## The decision is settled, but the idea is still useful

**Situation:** A team will keep an old data-file reader available. They want a
better way to describe why reusing column names did not make a new format safe.
In this fictional case, `distance` changed from meters to centimeters.

**Weak:** First redesign the architecture around adapters and dependency inversion.

**Useful:** The shared name hides a changed meaning: a value of 100 now represents
one meter rather than a hundred. That belongs to the format's semantic contract,
alongside units and conventions. This gives you a useful search and discussion
term even though you have already decided to retain the old reader.

**Selection:** Better recognition and description count as value. No new
architecture decision is needed to justify introducing the term.

## An attractive name is not yet a diagnosis

**Situation:** An event-monitoring screen reports alternating short and long
durations. Start and finish times come from different machines; synchronization
and actual queuing time are unknown.

**Weak:** This is queue saturation. Increase capacity.

**Useful:** These durations combine execution timing with the difference between
two clocks. Clock skew is one candidate; variable waiting or execution time is
another. A same-clock measurement and a check of how timestamps are produced
would separate measurement effects from actual delay before choosing a remedy.

**Selection:** Identifying a consequential distinction is useful even when the
right answer is not yet a preferred mechanism. No platform setting is inferred.

## Knowledge is available, but nothing extra is needed

**Situation:** A known unit price is 12 and the user requests only the cost of
three units, with no tax or other charge in the supplied conditions.

**Weak:** This is an opportunity to introduce linear models and dimensional analysis.

**Useful:** 36.

**Selection:** The result already serves the task. A related theory would not
improve this answer. If a later question asks why proportionality holds, that
different task may warrant an explanation.

For a stuck inference, use the existing
[derivation](derivation-example.md), [structure](structural-explanation.md), or
[model-selection](model-selection.md) contrasts. For reuse and records, follow
[domain judgment](domain-judgment.md); reading this example does not establish
user mastery or authorize saving anything.
