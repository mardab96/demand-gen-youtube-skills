---
name: bidding-strategy-fit-demand-gen
description: Checks whether a Google Ads Demand Gen campaign's bid strategy matches the conversion volume and signal quality it actually has, because a value or target strategy on thin data optimises toward noise. Use before changing bid strategy, when a campaign will not spend its budget, or when results swing week to week without a change.
---

# Should This Bid To Clicks Or Conversions - Demand Gen

## Use this skill when

The bid strategy was chosen from the goal rather than from the data.

Common user requests:

- "Should I switch to target CPA?"
- "It will not spend the budget."
- "Results swing wildly week to week."
- "Can I bid to ROAS on this?"

## Required input

Minimum useful data:

- Current bid strategy and any target value set.
- Weekly conversions for the optimisation event over at least four weeks.
- Spend, budget and whether the campaign is budget-limited.

Recommended additional data:

- Conversion value data quality, if the campaign bids to value.
- Recent changes to the strategy or target, with dates.
- The conversion lag for this account.

## Before analysis

1. Read the weekly conversion volume before anything else. Almost every finding here follows from it.
2. Check the conversion lag: a strategy that looks starved may simply be reading unfinished weeks.
3. Confirm whether the campaign is limited by budget or by the target. They produce similar complaints and different fixes.
4. Note when the target was last changed. Frequent target edits reset learning and produce the swing the user is describing.

## Analysis workflow

1. Compute weekly conversions for the optimisation event and its stability across weeks.
2. Compare that volume against what each candidate strategy needs to work.
3. Where the campaign bids to value, check whether conversion values are real and varied, or a single default number repeated.
4. Check whether the target is set inside the range the campaign has ever achieved. A target well below any historical result starves delivery.
5. Count strategy and target edits in the period; more than one a fortnight explains instability on its own.
6. Recommend one strategy, and state the volume condition under which the account should move to the next one up.

## Decision rules

Every threshold is a starting heuristic, not a Google rule. Recalibrate per account.

⚠️ **The volume figure people quote for this campaign type is per 30 days, not per week.** The commonly cited guidance for target CPA on Google's non-Search inventory is on the order of 50 conversions in the preceding 30 days, which is roughly 12 a week, not 50. An earlier version of this table used 50 per week and pushed almost every small account into clicks-only bidding, where the conversion signal never grows enough to leave. Treat the numbers below as a starting point and verify against current Google guidance for your campaign type.

| Verdict | Criteria |
|---|---|
| Bid to conversions with a target, or to value | Roughly 50+ conversions in the trailing 30 days [heuristic], stable within roughly 30% week to week, and real varied values if bidding to value |
| Bid to conversions without a target | Roughly 15-50 in the trailing 30 days |
| Bid to clicks for now | Under roughly 15 in the trailing 30 days, OR conversion values are a repeated default |

**The trap in the bottom row, which the earlier version walked straight into:** maximise clicks does not feed the conversion signal, so a campaign parked there does not accumulate its way up to the next band. Where you recommend clicks, also name what will move the account out of it — usually a shallower optimisation event with enough volume, or consolidating ad sets so one of them clears the floor.

Target-realism rule: a target more than roughly 30% away from anything the campaign has achieved is not a target, it is a throttle. Say what the campaign has actually achieved and propose a target inside that range with a plan to tighten it.

Edit-frequency rule: where the target has been edited more than once a fortnight, no strategy recommendation will hold. The first recommendation is to stop editing, with a date to review.

## Output format

### Strategy verdict

Which strategy fits today.

### Volume table

| Week | Conversions | Spend | Cost per result |
|---|---:|---:|---:|

### Target realism

Current target against the range the campaign has achieved.

### Edit history

Changes and dates, and whether they explain the instability.

### Move-up condition

The volume at which to change strategy, stated as a number.

## Practical example

Campaign bids to target CPA at a target 45% below anything it has recorded, on **41 conversions in the trailing 30 days**, with the target edited three times in five weeks.

Verdict: **bid to conversions without a target**. 41 sits in the middle band, so the strategy itself is not the problem; the target is. It is named as a throttle rather than a goal and removed, editing is stopped for four weeks, and the move-up condition to a target is set at a sustained 50 in the trailing 30 days.

Had the campaign been at 11 in thirty days rather than 41, the recommendation would be clicks — together with the named route out, because clicks alone would never get it back.

## Guardrails

- Do not recommend a value strategy where conversion values are a repeated default.
- Do not diagnose starvation without checking conversion lag first.
- Do not recommend a strategy change and a target change in the same week.
- Do not present the volume threshold as a published rule. It is a working figure.
