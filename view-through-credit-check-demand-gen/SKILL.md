---
name: view-through-credit-check-demand-gen
description: Separates conversions that followed a click from conversions credited to someone who only saw the ad, so a Demand Gen result is not read as action when most of it is exposure. Use before scaling, when Demand Gen reports strong conversions the rest of the account cannot find, or when comparing Demand Gen against Search on the same report.
---

# Did They Buy Or Did They Just Watch - Demand Gen

## Use this skill when

The campaign reports conversions and nothing else in the business moved.

Common user requests:

- "Demand Gen says 90 conversions, where are they?"
- "Can I compare this to Search?"
- "How much of this is view-through?"
- "Should I scale this campaign?"

## Required input

Minimum useful data:

- Google Ads report with conversions split by click-through and view-through, or with the view-through conversion column present.
- Spend and the conversion action being counted.
- Business-recorded conversions for the same closed range.

Recommended additional data:

- The same split for Search or another click-driven campaign, as a contrast.
- The conversion window in use.
- Any concurrent brand activity that would raise baseline demand.

## Before analysis

1. Read the conversion window off the account. A long window with view-through credit will claim a lot by construction.
2. Confirm which conversion action is being counted and whether it is the one the business cares about.
3. Confirm the range is closed.
4. Note that view-through credit is not fraud. It is a modelling choice, and the question is what to bet on it.

## Analysis workflow

1. Split reported conversions into click-through and view-through, as counts and as shares.
2. Recompute cost per conversion on click-through only, and state both numbers side by side.
3. Compare Demand Gen's view-through share against a click-driven campaign in the same account, so the reader has a contrast rather than an absolute.
4. Compare the click-through figure against business-recorded conversions for the range.
5. Say what the campaign looks like if the business plans on the click-through number alone.
6. Where view-through share is high and the business cannot see the outcome, route the question to a lift test rather than declaring the campaign good or bad.

## Decision rules

Every threshold is a starting heuristic, not a Google rule. Recalibrate per account.

| Verdict | Criteria |
|---|---|
| Comparable to click campaigns | View-through under roughly 25% of reported conversions [heuristic] |
| Report both numbers | View-through 25-60% |
| Do not compare this to Search | View-through above 60%, OR click-through conversions below what the business can independently see |

Comparison rule: never put a Demand Gen cost per conversion next to a Search cost per conversion without stating the view-through share of each. The two numbers answer different questions and the comparison is the single most common way this campaign type gets misjudged.

Escalation rule: high view-through share plus flat business results is not proof of failure. It is the exact condition a lift test exists for, and that is the recommendation.

## Output format

### Credit verdict

Comparable, report both, or not comparable.

### Split

| Measure | Click-through | View-through | Total |
|---|---:|---:|---:|

### Cost per conversion, both ways

Click-through only, and as reported.

### What to do next

Plan on the stricter number, or run a lift test, with the reason.

### Missing data

Whether the account exposed the split at all.

## Practical example

Demand Gen reports 94 conversions at 21 cost per conversion. The split shows 22 click-through and 72 view-through. Search in the same account runs at 4% view-through. Business orders are flat week on week. Output: not comparable to Search, click-through cost per conversion is 90, and the recommendation is a lift test rather than a scale or a pause.

## Guardrails

- Do not present total conversions as the headline when view-through dominates.
- Do not compare across campaign types without stating both view-through shares.
- Do not call view-through credit fake. Call it exposure credit and price it accordingly.
- Do not recommend a pause on this evidence alone.
