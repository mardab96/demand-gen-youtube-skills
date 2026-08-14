---
name: audience-signal-review-demand-gen
description: Reviews what the campaign told Google to look for and what Google went and found, so a broad audience is a choice rather than an accident. Use before scaling, when a campaign reaches people the business does not recognise, or when several audience segments perform identically.
---

# Who Google Thinks You Want - Demand Gen

## Use this skill when

The campaign is reaching someone, and nobody has checked who.

Common user requests:

- "Who are we actually reaching?"
- "Should I add more audience segments?"
- "Our lookalike segment does nothing."
- "Is the targeting even doing anything?"

## Required input

Minimum useful data:

- The audience segments attached to the campaign, with type: first-party list, lookalike segment, custom segment, in-market, affinity.
- Performance by segment where the account reports it.
- The size and age of each first-party list feeding a lookalike segment.

Recommended additional data:

- Audience insights or demographic breakdowns the account exposes.
- What the business knows about who actually buys.
- Any exclusions applied.

## Before analysis

1. Separate what constrains delivery from what merely hints at it. Some segment types narrow the auction, others are signals the system may ignore when it finds better.
2. Read each list's size and age. A stale seed produces a segment aimed at last year's customer.
3. Ask the business who its good customers are, in plain terms, before judging whether the segments match.
4. Note whether the campaign is new. Early delivery reflects the signal more than late delivery does.

## Analysis workflow

1. Tabulate every segment with its type, size, age and share of spend.
2. Mark each as a hard constraint or a soft signal, and say which is which in the output, because most confusion here comes from treating a signal as a filter.
3. Compare delivery against the described good customer: age, geography, device, interest where visible.
4. Identify segments carrying spend without carrying outcomes.
5. Check whether several segments are built from the same underlying list, in which case they are one hypothesis wearing several names.
6. Propose either a better signal the business can supply from data it already holds, or a deliberate decision to run broad.

## Decision rules

Every threshold is a starting heuristic, not a Google rule. Recalibrate per account.

| Verdict | Criteria |
|---|---|
| Signal is doing work | Segments differ in cost per result by more than roughly 25% [heuristic] and the leading one matches the described customer |
| Signal is decorative | Segments within roughly 15% of each other, which usually means delivery ignored them |
| Signal is misaimed | Leading segment does not match the described customer, OR every seed list is older than 90 days |

Same-seed rule: segments built from one list are not independent tests. Read them together or the account will keep adding variations of the same idea.

Broad rule: running broad is a legitimate choice on this campaign type. It stops being legitimate when nobody decided it and everyone believes the segments are steering.

## Output format

### Signal verdict

Doing work, decorative, or misaimed.

### Segment table

| Segment | Type | Constraint or signal | Size | Age | Spend share | Cost per result |
|---|---|---|---:|---|---:|---:|

### Delivery against the described customer

Where they match and where they do not.

### Proposed signal

A better list the business can produce, or an explicit decision to run broad.

### Missing data

What the account did not expose about delivery.

## Practical example

Four segments, three of them lookalike variants built from the same 900-member purchaser list uploaded in April. Cost per result differs by 6% across all four. Output: signal is decorative, the three variants are one hypothesis, and the recommendation is a refreshed seed from the last 180 days of buyers plus an explicit decision about whether broad is acceptable while the seed rebuilds.

## Guardrails

- Do not describe a soft signal as targeting.
- Do not judge segments in a campaign's first days.
- Do not treat variants of one seed as separate tests.
- Do not propose an audience the business cannot actually build.
