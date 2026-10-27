# Safe implementation and modernization without deprecation

## Operating modes

Research: analyze and document; no production writes. Isolated prototype: synthetic or approved de-identified data, bounded cost, no live integrations by default; label limitations. Production implementation: work only within authorized scope, repository rules and release authority. Never promote a research notebook or demonstration into production merely because it ran once.

If Superpowers is available, load relevant design/planning/TDD/verification skills. Otherwise write the design, alternatives, acceptance criteria and sequenced plan explicitly, then use the procedure below. A plan is not deployment permission.

## Red-green-refactor

1. Reproduce the baseline and identify externally observable behavior. Add characterization tests for legacy contracts before changing them.
2. Write the smallest meaningful failing test for new behavior or a reproduced bug. Run it and confirm failure is due to the missing behavior, not setup or a typo.
3. Implement the minimum change to pass. Run the targeted test and relevant regression suite.
4. Refactor with tests green. Repeat per behavior. Preserve commands, observed failures and final outcomes in the evidence/test matrix.
5. Verify integration, boundary, error, security, accessibility and performance behavior as appropriate. Unit tests alone do not validate migration, demand or usability.

## No-deprecation contract checklist

Inventory supported APIs and payloads, schema/data semantics, saved files, imports/exports, URLs, integrations/webhooks, permissions, defaults, feature behavior and critical user workflows. Identify versions, owners and representative fixtures. Preserve supported contracts and capabilities throughout this assignment. Do not remove, silently rename, disable, narrow or change default behavior to obtain a cleaner architecture. A version bump or new API version does not excuse breaking existing consumers.

Prefer additive changes, compatibility adapters and internal replacement behind stable interfaces. Use expand-and-migrate schema steps; keep old and new readers/writers compatible during mixed-version operation. Verify idempotence, historical data, partial migration, retries, concurrency, consistency/reconciliation and old-client/new-server behavior. Any destructive contract/column removal is outside this no-deprecation scope. Escalate a requirement conflict with alternatives; do not quietly implement it.

Test feature parity against the inventory, including edge cases and export/recovery paths. A successful fresh install is insufficient: verify upgrade from supported versions, existing settings/data, and reversible transitions. A code rollback cannot undo incompatible data writes; rehearse data recovery separately.

## Product quality and security checklist

Define relevant quality attributes as measurable acceptance criteria: functional correctness, latency distributions under realistic load, availability, data integrity, reliability/recovery, interoperability, maintainability, operability and accessibility. Record workloads, environments, tolerances and resource budgets.

Threat-model assets, trust boundaries, actors and abuse cases. Check authentication/authorization including tenant isolation, input validation, injection, secrets, dependency/supply-chain risks, least privilege, audit logs and sensitive-data handling. Use safe fixtures; no unauthorized penetration testing. Pin and review dependencies, protect build artifacts and investigate root causes of vulnerabilities. NIST SSDF informs lifecycle practices; following this checklist is not a certification.

## Gradual rollout and recovery

Release only with established authority. Use feature flags or compatible routing; default safely and retain existing paths. Example stages are internal, small opt-in cohort, limited canary, expansion, then broad availability; percentages and durations must follow traffic, risk and statistical needs, not a universal recipe.

For each stage specify owner, eligibility, exposure cap, duration, telemetry, baseline/control, promotion rule and rollback trigger. Check errors, p95/p99 latency, integrity, support incidents, task completion and segment-specific harm. A canary detects operational problems; it is not automatically a valid randomized product experiment.

Rehearse flag disablement, application rollback and data restore/reconciliation. Verify backups, restoration time and permitted data-loss limits. Freeze expansion on guardrail breach, stop exposure and invoke the recovery owner. Monitor through a relevant retention/renewal interval before declaring durable commercial success. Keep supported old functionality available; rollout completion does not authorize deprecation.
