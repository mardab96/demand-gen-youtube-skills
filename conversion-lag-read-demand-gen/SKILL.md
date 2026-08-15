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
- **If only one pull exists, this cannot be measured at all.** A single export tells you what each past day looks like today; it can never tell you what that day looked like when it was fresh, which is the entire quantity. Say the waiting rule is unavailable, start taking a weekly snapshot now, and come back when the second pull exists. Do not substitute a historical daily series and present it as a curve.

Recommended additional data:

- The conversion action and its counting window.
- Whether view-through conversions are included in the figure.
- The business's own timestamps for the outcome.

## How to pull this

Interface labels move between Google Ads releases. Where a name below does not match what you see, the report is still the one described.

1. Export the campaign report segmented by day for a closed range, and **write down the date you pulled it**. That date is the input the script needs.
2. Add: `Conversions`, `View-through conv.` and `Engaged-view conversions`.
3. Wait several days and export the identical range again, unchanged in every respect except the pull date.
4. **The trap:** the two files must cover the same range, not the same number of days. Re-running "last 7 days" a week later gives you two different weeks and a curve that means nothing, and it is the single most common way this measurement gets ruined.

## Before analysis

1. Ask whether two pulls exist. Without them, stop and say so; there is no fallback that produces this number.
2. Check whether the reported figure includes view-through credit. That fills on a different schedule and mixing them hides both.
3. Confirm the conversion window. A long window cannot be final before it has elapsed.
4. Ask how long the business's own cycle runs from first exposure to recorded outcome.

## Analysis workflow

1. For each day in the overlap, compare the value at first pull against the later pull.
   **Run `../scripts/lag_curve.py early.csv late.csv --as-of YYYY-MM-DD` rather than doing this by eye.** It owns none of the thresholds, it implements the ones in this file, and it exists because matching two CSVs day by day is where a manual read silently misaligns rows. Its output is the fill curve, the flattening day and the waiting rule.
2. Compute the share of the final figure visible by AGE, meaning how old each day was when the early pull was taken. One pull over a seven-day range gives you seven ages at once: the last day of the range was one day old, the first was seven. That is the fill curve, and `--as-of` is required precisely because without the pull date those ages are unknowable. Averaging days of different ages into one number overstates the day-one share, which shortens the waiting rule in the same direction as the premature pause this skill exists to prevent.
3. Where possible, compute the curve separately for each credit type the account exposes: click-through, engaged-view and view-through. They fill on different schedules, and Demand Gen carries engaged-view credit inside the headline count, so a single blended curve hides the fastest and the slowest signal at once.
4. Identify the day the curve flattens.
5. Convert it into a waiting rule expressed in days.
6. Re-read any decision taken inside the unfinished window and say whether it would still hold.

## Decision rules

Every threshold is a starting heuristic, not a Google rule. Recalibrate per account.

"Visible at day one" means the share of a day's eventual figure that was showing
when that day was one day old. Read it off the fill curve, never off a pooled
average of days of mixed ages. Where the range contains no one-day-old day, the
youngest available age is a ceiling: the true day-one share is lower and the
waiting rule is at least as long.

**A measured plateau beats this table.** Where your two pulls span enough days
that the curve stops rising inside the range, the age at which it levels off IS
the waiting rule, and the bands below are not consulted. They exist for the
common case where the range is too short to reach the plateau, and a day-one
share is the only thing you can read. `../scripts/lag_curve.py` applies that
precedence itself and says which of the two it used.

The bands, for that fallback case. Read top to bottom and stop at the first row
that matches.

| Verdict | Criteria |
|---|---|
| Judge after 14 days | Under 40% visible at day one [heuristic], OR view-through credit is more than half of total credited (`Conversions + View-through conv.`), OR the sale needs a human step such as a call, a quote or a viewing |
| Judge after 7 days | 40% up to but not including 70% visible at day one |
| Judge after 2-3 days | 70% or more visible at day one |

Do-not-decide rule: no pause, no cut and no asset kill inside the unfinished window. Where a call must come sooner, make it on leading indicators such as cost per engaged view or click-through rate, and say in the output that it is a leading-indicator call.

Launch rule: a new campaign is also inside its learning period, so early figures are unfinished twice. Do not read a launch through this skill alone.

## Output format

### Waiting rule (or: unavailable, when only one pull exists)

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

Two pulls a week apart show 38% of the final figure visible at day one and 71% at day three, with view-through filling considerably later than click-through.

Verdict: **judge after 14 days**, not seven. 38% is below the 40% line, and the view-through clause points the same way, so both criteria in that row fire. An earlier draft of this example said seven days, which its own table forbids.

A campaign cut on its second day at a cost per result of 61 would have settled near 32. The cut is flagged for reversal, and cost per engaged view is proposed as the leading indicator for calls that genuinely cannot wait fourteen days.

## Guardrails

- Do not present an estimated curve as measured.
- Do not mix click-through and view-through into one curve without saying so.
- Do not use lag as a reason never to decide. Produce a number.
- Do not carry a curve from one campaign type to another.
