---
name: audience-signal-review-demand-gen
description: Reviews what a Google Ads Demand Gen campaign told Google to look for and what Google went and found, so a broad audience is a choice rather than an accident. Use before scaling, when a campaign reaches people the business does not recognise, or when several audience segments perform identically.
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

**Read in this order and stop at the first that fires.** A stale seed and a flat spread routinely appear together, and an unordered table lets the reader pick the gentler answer.

| Order | Verdict | Criteria |
|---:|---|---|
| 1 | Not enough to judge | Any segment under roughly 30 results in the window [heuristic], or the account reports no segment-level performance at all |
| 2 | Signal is misaimed | Every seed list older than 90 days, OR the leading segment does not match the described customer |
| 3 | Signal is decorative | Segments within 15% of each other on cost per result |
| 4 | Signal is doing work | Spread above 25% and the leader matches the described customer |

When the account exposes no segment-level performance this skill stops at row 1. It has no fallback read, unlike `money-split-review-demand-gen`, and inventing a verdict from the segment list alone would be exactly the thing this pack refuses elsewhere.

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

Four segments, three of them lookalike variants built from the same 900-member purchaser list uploaded in April. Cost per result differs by 6% across all four. Read in order. Row 1 does not fire, the segments have volume. **Row 2 fires**: the only seed is four months old, past the 90-day line. Verdict: **signal is misaimed**, and rows 3 and 4 are never reached. An earlier draft called this decorative, which was the softer of two rows that both matched.

The distinction is not cosmetic. Decorative means delivery ignored your signal; misaimed means it followed a signal pointing at last year's customer. Only the second is fixed by a new seed, which is what the recommendation says. The three variants are one hypothesis, and the recommendation is a refreshed seed from the last 180 days of buyers plus an explicit decision about whether broad is acceptable while the seed rebuilds.

## Guardrails

- Do not describe a soft signal as targeting.
- Do not judge segments in a campaign's first days.
- Do not treat variants of one seed as separate tests.
- Do not propose an audience the business cannot actually build.
