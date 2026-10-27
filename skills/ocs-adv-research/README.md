# ocs-adv-research

Author: **Glenn Hurn**. Version **0.9.0**. Generic, reusable first-principles research and practical product-improvement skill, released under MIT. Anyone may use, modify and redistribute it under the license. No private product/project material is included.

This release connects falsifiable scientific inquiry with segmentation, ICP and buying roles, paid-demand validation, process performance, UX/accessibility, security, compatible modernization and customer lifecycle outcomes. It provides staged decisions and reusable evidence, experiment, test and metric templates. It does not guarantee commercial success or grant production authority.

**Provenance limitation:** the original attached source was unavailable; source fidelity remains unverified. See [source notes](references/sources.md). The research and engineering guidance is usable independently of that comparison.

## Install

Requires an agent supporting filesystem skills. Python 3.9+ is needed only for bundled lint/tests; research needs source access or user-provided evidence. No API keys or external packages are required for lint/tests. Superpowers is optional: use installed skills if present, otherwise the explicit design/planning/TDD/verification workflow is included. Do not claim unavailable plugin execution.

Extract the ZIP. Copy the entire `ocs-adv-research` directory, retaining `SKILL.md`, `references`, and `templates` together. Inspect any existing same-name skill before copying; do not overwrite local changes without review.

- Codex personal installation: `~/.agents/skills/ocs-adv-research/`.
- Codex project installation: `.agents/skills/ocs-adv-research/` in the chosen repository.
- Claude Code personal installation: `~/.claude/skills/ocs-adv-research/`.
- Claude Code project installation: `.claude/skills/ocs-adv-research/`.
- Other Agent Skills hosts: place the folder in the host's documented discovery location, or explicitly ask the agent to read `SKILL.md` and linked references. A Markdown upload alone does not guarantee automatic installation.

Reload or start a new session if required, inspect the host's available skills and invoke explicitly. See [Codex documentation](https://learn.chatgpt.com/docs/build-skills), [Claude documentation](https://code.claude.com/docs/en/skills) and the [portable specification](https://agentskills.io/specification).

## Invoke

Codex:

```text
$ocs-adv-research Investigate how to reduce onboarding abandonment for a generic scheduling tool. Start in research-only mode. Separate end users from budget owners, compare a process-only intervention, identify missing evidence, and deliver G0–G3 artifacts. Do not contact people, spend money or modify production.
```

Claude Code uses `/ocs-adv-research` with the same request. In other hosts, name the skill and provide its local path.

Implementation example:

```text
Use ocs-adv-research to improve this application's search latency within the authorized local repository. Preserve all supported APIs, saved queries and workflows. Establish a baseline, investigate mechanisms, define customer-relevant targets, use red-green-refactor, and produce a compatibility/test matrix plus a proposed staged rollout. Deployment is outside this request.
```

## Validate

From the skill folder:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

The lint checks this package's simple frontmatter, directory name, relative Markdown links and symlink exclusion. It is not a full YAML/Markdown validator, a security scanner or proof of agent behavior. Review [behavioral scenarios](tests/behavioral-scenarios.md) before expanding instructions. Keep private research workbooks outside the skill directory.

## Contents and contribution

Start at [SKILL.md](SKILL.md). Copy [research workbook](templates/research-workbook.md) and [scorecard](templates/scorecard.md) into a private project. References disclose methods and sources. Contributions should preserve generic scope, source attribution, backward compatibility and evidence honesty. Never add customer records, unpublished strategy, credentials, private repositories or confidential source attachments. Re-run validation and behavioral review after changes.
