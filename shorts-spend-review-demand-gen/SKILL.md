---
name: shorts-spend-review-demand-gen
description: Checks whether short-form vertical placement is absorbing a campaign's budget at a cost per outcome the business would not choose deliberately, and whether that is a targeting problem or a creative-shape problem. Use when a campaign leans heavily to short-form, when cheap impressions coincide with flat results, or before adding vertical assets.
---

# Is Shorts Eating Your Budget - Demand Gen

## Use this skill when

Impressions are cheap, plentiful, and not turning into anything.

Common user requests:

- "Why did our CPM collapse?"
- "Is Shorts wasting our budget?"
- "We got tons of views and no traffic."
- "Should I make vertical videos or not?"

## Required input

Minimum useful data:

- Campaign report split by placement or format where the account exposes it.
- Impressions, spend, engaged views, clicks and conversions per split.
- The asset list with aspect ratios.

Recommended additional data:

- The same split before and after any creative change.
- Cost per thousand impressions per split.
- Conversion value per split if tracked.

## Before analysis

1. Establish what the account can actually report. Where the split is unavailable, say so and stop rather than inferring it from cheap impressions.
2. Note the asset ratios. A set that is mostly vertical will lean short-form by construction, and that is a creative decision, not a platform ambush.
3. Confirm the date range is closed.
4. Remember cheap impressions are not automatically bad. The question is what they cost per outcome.

## Analysis workflow

1. Compare cost per thousand impressions, cost per engaged view and cost per conversion across splits.
2. Compute share of spend against share of conversions for the short-form split specifically.
3. Check whether the short-form share rose after a creative change, a budget change, or on its own.
4. Distinguish a cheap-and-useful split from a cheap-and-empty one using outcomes, never using volume.
5. Where the split is genuinely underperforming, identify the lever the account actually has: creative shape, exclusion where permitted, or campaign separation.
6. State what the campaign's overall numbers look like with that split removed, so the tradeoff is visible.

## Decision rules

Every threshold is a starting heuristic, not a Google rule. Recalibrate per account.

| Verdict | Criteria |
|---|---|
| Short-form is earning its place | Its share of conversions within roughly 15 percentage points of its share of spend [heuristic] |
| Watch it | Conversion share 15-35 points below spend share |
| Act | Conversion share more than 35 points below spend share, OR the split takes 40%+ of budget with near-zero conversions |

Creative-shape rule: before treating this as a targeting problem, check whether the campaign has any non-vertical assets at all. If it does not, the split is a consequence of the asset set and the first move is production, not exclusion.

Awareness exception: where the campaign was bought for reach, cheap impressions are the point. Say so and judge on cost per engaged view rather than cost per conversion.

## Output format

### Split verdict

Earning its place, watch, or act.

### Comparison

| Split | Spend share | Impression share | Conversion share | Cost per engaged view | Cost per conversion |
|---|---:|---:|---:|---:|---:|

### Campaign without this split

What the headline numbers become, and what volume is lost.

### Recommended lever

Creative, exclusion or separation, with the reason.

### Missing data

Whether the account could report the split at all.

## Practical example

Short-form takes 46% of spend and returns 4% of conversions, while cost per thousand impressions is a fifth of the campaign average. The asset set is five vertical videos and nothing else. Output: act, but the lever is production not exclusion, because the campaign currently has nowhere else to serve. Removing the split entirely would cut spend to a level the budget could not absorb.

## Guardrails

- Do not read cheap impressions as waste. Price them by outcome.
- Do not recommend exclusion before checking the asset ratios.
- Do not infer a split the account did not report.
- Do not apply the conversion test to a campaign bought for reach.
