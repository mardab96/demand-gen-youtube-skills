---
name: engaged-view-quality-demand-gen
description: Separates impressions and engaged views in a Google Ads Demand Gen or YouTube campaign so a campaign is not judged on the metric that flatters it, and states which of them the business should care about. Use when a video campaign reports huge view counts with nothing downstream, or before comparing two campaigns that count views differently.
---

# Are These Views Real Attention - Demand Gen

## Use this skill when

The view count is large and nobody can say what it bought.

Common user requests:

- "We got 400,000 views, what does that mean?"
- "Why is our view rate so high and our traffic so low?"
- "Which view number should I put in the report?"
- "Is this campaign working?"

## Required input

Minimum useful data:

- Google Ads report with impressions, engaged views and clicks for the campaign. **Demand Gen does not report the 30-second `Views` counter that Video campaigns use; if you are looking for it, that is why you cannot find it.**
- The video asset lengths.
- Spend and conversions for the same closed range.

Recommended additional data:

- Audience retention or view-rate curves per asset if available.
- The same metrics for a comparable earlier period.
- What the business considers a meaningful outcome.

## Before analysis

1. Write down what each counter actually counts in this account, because the definitions differ by campaign type and a mixed report is unreadable.
2. Confirm asset lengths. A ten-second asset and a ninety-second asset cannot share a view-rate benchmark.
3. Ask what the campaign is for: awareness, consideration or action. The right view metric follows from that, not the other way around.
4. Confirm the date range is closed.

## Analysis workflow

1. Build the ladder: impressions, engaged views, clicks, conversions, with the drop between each step as a percentage.
2. Compute engaged views as a share of impressions, and clicks as a share of engaged views.
3. Compare per asset, not just per campaign. One long asset can drag the whole campaign average.
4. Identify where the ladder actually breaks: attention, or the step after attention.
5. State which single number belongs in the report and why, and which ones are decoration.
6. Where the campaign is for action, judge it on the last two steps and say that the view counters are not the case.

## Decision rules

Every threshold is a starting heuristic, not a Google rule. Recalibrate per account.

| Verdict | Criteria |
|---|---|
| Attention is real | Engaged views at least roughly 10% of impressions [heuristic] **and** clicks at least 2% of engaged views |
| Attention without action | Engaged views at least roughly 10% of impressions **and** clicks under 2% of engaged views |
| Weak attention | Engaged views 5-10% of impressions, whatever the click rate |
| Not attention | Engaged views under roughly 5% of impressions |

These four bands are exhaustive and mutually exclusive on purpose. Read the engaged-view share first, then the click rate only if the first test cleared 10%. A rubric with a gap in it still produces a verdict, and that verdict is invented.

Asset-length rule: compare like with like. Where asset lengths differ by more than roughly double, report per asset and refuse the campaign average.

Awareness rule: a campaign genuinely bought for awareness is allowed to stop at engaged views, but say so explicitly in the output so nobody quotes the view count as performance later.

## Output format

### Attention verdict

Real, attention without action, or not attention.

### The ladder

| Step | Count | Drop from previous |
|---|---:|---:|

### Per asset

| Asset | Length | Engaged view share | Clicks per engaged view |
|---|---:|---:|---:|

### The one number for the report

Which metric, and what it does and does not say.

### Missing data

What the account could not report.

## Practical example

Campaign reports 6.9 million impressions and 412,000 engaged views, so the engaged-view share is 6.0% and clicks are 0.4% of engaged views. Two of four assets are 90 seconds and carry most of the impressions.

Verdict: **weak attention**, not "not attention" — 6.0% sits in the 5-10% band, above the 5% floor. The click rate is not read at campaign level at all, because the first test did not clear 10%.

The asset-length rule then forbids stopping there: the four assets differ by more than double in length, so the campaign average is refused and the per-asset table is the output. It shows the two short assets at 13% and 11% engaged-view share with clicks at 2.4% and 2.1% of engaged views, which is "attention is real" on both counts, while the two long assets sit at 3%. The recommendation is to judge on the short assets and cut the long ones. The 412,000 figure goes in no report.

## Guardrails

- Do not report a raw view count as a result.
- Do not average across assets of very different lengths.
- Do not call a campaign failed on view metrics alone when it was bought for action; go to the last two steps.
- Do not invent a definition for a counter. If the account's definition is unclear, say so.
