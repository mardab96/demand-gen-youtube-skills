---
name: conversion-lag-read-demand-gen
description: Measures how long a Demand Gen result keeps filling in after the day it happened, so nobody pauses a campaign on a number that is still arriving. Use before any pause or budget cut based on recent days, after a launch, or when last week's figures improve after they were exported.
---

# When The Numbers Stop Moving - Demand Gen

## Use this skill when

Someone wants to judge the last few days.

Common user requests:

- "The last three days look awful."
- "Should I pause it?"
- "Why did last week get better after I reported it?"
- "How long do I wait?"

## Required input

Minimum useful data:

- The same campaign report pulled at least twice for an overlapping range, at different times.
- If only one pull exists: 30+ days of daily data for the campaign.

Recommended additional data:

- The conversion action and its counting window.
- Whether view-through conversions are included in the figure.
- The business's own timestamps for the outcome.

## Before analysis

1. Ask whether two pulls exist. Without them the curve is estimated from history and must be labelled as such.
2. Check whether the reported figure includes view-through credit. That fills on a different schedule and mixing them hides both.
3. Confirm the conversion window. A long window cannot be final before it has elapsed.
4. Ask how long the business's own cycle runs from first exposure to recorded outcome.

## Analysis workflow

1. For each day in the overlap, compare the value at first pull against the later pull.
2. Compute the share of the final figure visible after 1, 3, 7 and 14 days.
3. Where possible, compute the curve separately for click-through and view-through, because they differ enough to change the waiting rule.
4. Identify the day the curve flattens.
5. Convert it into a waiting rule expressed in days.
6. Re-read any decision taken inside the unfinished window and say whether it would still hold.

## Decision rules

Every threshold is a starting heuristic, not a Google rule. Recalibrate per account.

| Verdict | Criteria |
|---|---|
| Judge after 2-3 days | 70%+ of the final figure visible at day one [heuristic] |
| Judge after 7 days | 40-70% visible at day one |
| Judge after 14 days | Under 40% visible at day one, OR view-through credit is a large share, OR the business cycle includes a human step |

Do-not-decide rule: no pause, no cut and no asset kill inside the unfinished window. Where a call must come sooner, make it on leading indicators such as cost per engaged view or click-through rate, and say in the output that it is a leading-indicator call.

Launch rule: a new campaign is also inside its learning period, so early figures are unfinished twice. Do not read a launch through this skill alone.

## Output format

### Waiting rule

The number of days after which figures are stable enough to act on.

### Fill curve

| Days after | Share of final visible | Click-through | View-through |
|---:|---:|---:|---:|

### Decisions to revisit

| Decision | Date | Days of data then | Share visible | Still holds |
|---|---|---:|---:|---|

### Missing data

Whether the curve is measured or estimated.

## Practical example

Two pulls a week apart show 38% of the final figure visible at day one and 71% at day three, with view-through filling considerably later than click-through. A campaign cut on its second day at a cost per result of 61 would have settled near 32. Output: waiting rule of seven days, the cut flagged for reversal, and cost per engaged view proposed as the faster indicator.

## Guardrails

- Do not present an estimated curve as measured.
- Do not mix click-through and view-through into one curve without saying so.
- Do not use lag as a reason never to decide. Produce a number.
- Do not carry a curve from one campaign type to another.
