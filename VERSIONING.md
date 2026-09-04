# Versioning

This repository uses Semantic Versioning. `VERSION` is the repository release,
`skills-manifest.json` is the machine-readable source of repository and Skill
versions, and each `SKILL.md` repeats its installed Skill version under
`metadata.version`.

- Patch: wording or implementation corrections that preserve the behavior contract.
- Minor: backward-compatible capability or input-contract additions.
- Major: incompatible trigger, input, output, ownership, or safety-boundary changes.

Every release must update `VERSION`, the affected manifest entries, affected
Skill frontmatter, and `CHANGELOG.md` in one commit. Run `scripts/validate.py`,
install and validate the affected Skill, then create the immutable tag `vX.Y.Z`.
Tags identify repository snapshots; installed copies are identified by each
Skill's `metadata.version`.
