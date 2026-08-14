---
name: frequency-creep-review-demand-gen
description: Checks whether rising cost in a Google Ads Demand Gen or YouTube campaign is being caused by showing the same ads to the same shrinking pool of people, and separates that from creative fatigue and from auction pressure. Use when cost per result climbs without a change, when reach flattens while spend rises, or before increasing budget on a working campaign.
---

# Why Your Frequency Is Climbing - Demand Gen

## Use this skill when

Costs are rising and nothing was changed.

Common user requests:

- "Costs went up and I did not touch anything."
- "Are we burning the audience?"
- "Should I raise the budget?"
- "Is this fatigue or saturation?"

## Required input

Minimum useful data:

- Weekly impressions, reach or unique users, spend and results for at least six weeks.
- The audience definition and its size where the account estimates it.
- Asset list with the date each was added.

Recommended additional data:

- Cost per thousand impressions by week.
- Any budget or targeting change with its date.
- Competitor or seasonal context the business knows about.

## Before analysis

1. Confirm the account reports reach or unique users. Without it, frequency is inferred and must be labelled as inferred.
2. Get the change log first. A budget rise three weeks ago explains most of what follows.
3. Confirm the asset set has not changed, otherwise fatigue and saturation are tangled and cannot be separated here.
4. Note that rising cost has at least three ordinary causes and this skill separates them rather than picking one.

## Analysis workflow

1. Plot impressions divided by reach per week, which is the frequency trend.
2. Plot reach itself. Saturation looks like frequency rising while reach flattens.
3. Plot cost per thousand impressions. Auction pressure looks like that rising while frequency stays flat.
4. Plot result rate per impression. Fatigue looks like that falling while frequency and reach both hold.
5. Match the observed pattern to one of those three shapes, and say which one the data supports.
6. Where the shape is saturation, size the remaining audience and say how long the current spend can run before it repeats itself further.

## Decision rules

Every threshold is a starting heuristic, not a Google rule. Recalibrate per account.

**Run the tests in this order and stop at the first that fires.** Without an order, one series can match Healthy, auction pressure and fatigue at once, and the verdict becomes whichever row the reader looked at first.

1. Unresolved (window test) → 2. Saturation → 3. Fatigue → 4. Auction pressure → 5. Healthy.

Every shape carries a tolerance, because "stable" and "flat" without a number mean the verdict depends on who reads the chart. All comparisons are against the same metric four weeks earlier, on a series split at any budget change.

| Order | Verdict | Criteria |
|---:|---|---|
| 1 | Unresolved | Fewer than six weeks of data after the last budget change. Nothing below is readable until this clears |
| 2 | Saturation | Frequency up more than 25% [heuristic] while reach is within 10% or falling, sustained 3+ weeks |
| 3 | Fatigue | Result rate per impression down more than 20% while both frequency and reach change by 15% or less |
| 4 | Auction pressure | Cost per thousand impressions up more than 20% while frequency change is 15% or less |
| 5 | Healthy | Frequency change 15% or less and reach up 10% or more |

Every boundary uses "more than" or "or less" so a series sitting exactly on a number lands in one row, not two.

The last row exists because these four shapes do not cover every series, and a rubric that pretends otherwise will label a mixed pattern as whichever shape it half resembles.

Budget rule: never diagnose saturation across a budget change without splitting the series at the change date. A budget rise produces every symptom of saturation for a fortnight and then stops.

Audience-size rule: where the audience estimate is small relative to weekly reach, saturation is the expected outcome rather than a defect, and the recommendation is audience expansion, not creative.

## Output format

### Pattern verdict

Unresolved, saturation, fatigue, auction pressure, or healthy — named with the test number that fired.

### Weekly series

| Week | Spend | Reach | Impressions | Frequency | Cost per thousand | Result rate |
|---|---:|---:|---:|---:|---:|---:|

### Which shape the data matches

The reasoning, stated against the three shapes.

### Runway

At current spend, how long before frequency rises further, if saturation.

### Missing data

Whether reach was reported or inferred.

## Practical example

Six weeks of data. Frequency moves 1.9 to 3.4 while weekly reach falls 12%, cost per thousand impressions is flat and result rate per impression is unchanged. Budget rose 40% in week two. Test 1 fires and stops everything else: six weeks total with the budget rising in week two leaves roughly four weeks after the change, and the window rule needs six. Verdict: **Unresolved**.

The shape looks like saturation — frequency up 79%, reach down 12%, held three weeks — and an earlier draft of this example reported it as such. It is not available yet. Say what the shape suggests, say the window is too short to claim it, and name the date the series becomes readable. Two more weeks of stable budget settle it.

Had the window cleared, the reading would have been with the series split at the budget change so the first fortnight is excluded, and audience expansion recommended ahead of any new creative.

## Guardrails

- Do not diagnose across a budget change without splitting the series.
- Do not call rising cost fatigue without checking the result rate.
- Do not report inferred frequency as measured.
- Do not recommend new creative for a saturation pattern; it will not fix it.
