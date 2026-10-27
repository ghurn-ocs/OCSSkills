# Gate scorecard and metric dictionary

Set targets before testing using baseline, customer needs, risk, economics and expected sample size. These formulas are conventions to adapt explicitly, not universal industry benchmarks. Every row needs population/segment, time window, denominator, instrument/query, baseline, target, guardrail, observed value/interval, evidence ID, owner and gate status. Preserve definitions across comparisons or document changes.

| Dimension | Metric / operational definition | Acceptance decision |
|---|---|---|
| Scientific validity | Predicted effect versus baseline with uncertainty; rival explanation tests | Discriminating evidence supports bounded claim |
| Paid demand | Paid eligible customers / eligible customers offered at stated terms | Meet declared demand criterion; do not substitute survey intent |
| Viability | Revenue less incremental service, implementation, support and acquisition costs; sensitivity ranges | Sustainable value under stated assumptions |
| Process | Elapsed lead time, touch time, first-pass successful outputs / all outputs, cost / successful outcome | Reduce system burden without shifting hidden cost |
| Task usability | Unassisted successful attempts / eligible attempts; time distribution and error/recovery rate | Critical tasks meet declared success and burden targets |
| Accessibility | Applicable WCAG 2.2 A/AA criteria and complete-process results | No unresolved applicable criterion failure for claimed AA scope |
| Quality | Error rate, availability, p95/p99 latency, integrity defects under stated load | Meet SLOs and no unowned release-blocking risk |
| Compatibility | Passing protected contract fixtures / required fixtures, upgrade and restore outcomes | All required supported behavior preserved |
| Activation | Eligible new customers reaching verified first value / eligible new customers | Improve declared activation/time-to-value objective |
| Retention | Original cohort members returning for meaningful value in interval / original eligible cohort | Evaluate at natural cadence; show cohorts and censoring |
| Churn | Customers lost during period / customers at period start | Separate revenue/logo and involuntary/voluntary loss |
| CSAT | Responses meeting declared satisfied cutoff / valid responses | Report scale, question, trigger, distribution and response rate |
| Advocacy | Qualified referred customers, activation and retained referrals / defined eligible referrers or invites | Track actual referral behavior separately from intent |

Status meanings: pass (evidence meets criterion), fail (criterion missed), hold (insufficient or unreliable evidence), justified-not-applicable (reason and owner). Attach adverse subgroup outcomes. Use no weighted sum to override hard guardrails.

Illustrative only: a team could predeclare a critical-task success floor of 90%, a maximum p95 time of 2 minutes, and no data-integrity regressions. Those numbers require contextual justification, sample-size planning and uncertainty analysis before use; they are not supplied standards. Demand/retention targets must follow the proposed business and usage cycle.
