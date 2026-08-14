---
name: new-customer-share-demand-gen
description: Checks how much of a campaign's reported conversions came from people who had never bought before, so upper-funnel spend is judged on the job it was bought to do. Use before scaling upper funnel, when a campaign reports well but the customer base is not growing, or when deciding between prospecting and retargeting budget.
---

# Is This Bringing New Customers - Demand Gen

## Use this skill when

The campaign was bought to find new people and nobody has checked whether it did.

Common user requests:

- "Is Demand Gen bringing new customers or just repeat buyers?"
- "Our order count is up and our customer count is not."
- "Should this budget go to prospecting or retargeting?"
- "Is upper funnel doing its job?"

## Required input

Minimum useful data:

- Campaign report with conversions and conversion value for the closed range.
- New versus returning customer split from the shop or CRM for the same range.
- Total customers acquired in the range, from the business.

Recommended additional data:

- The same split for the period before this campaign launched.
- First-order value against repeat-order value.
- Whether the account uses a new-customer acquisition goal or customer lists for exclusion.

## Before analysis

1. Establish what the business counts as a new customer: first order ever, or first order in a window. The two produce very different numbers and both are defensible.
2. Confirm the business can actually split new from returning. Where it cannot, this skill produces a bounded estimate from total customer growth, and says so.
3. Check whether existing customers are excluded from the campaign. If they are not, a high repeat share is a targeting decision rather than a discovery.
4. Confirm the range is closed.

## Analysis workflow

1. Compare total customers acquired in the range against the period before the campaign launched, on equal-length windows.
2. Compute the new-customer share of the business's orders in the range, and compare it against the pre-campaign baseline.
3. Where the account can attribute at customer level, compute the campaign's own new-customer share directly.
4. Compute cost per new customer, not cost per conversion, and put the two side by side.
5. Compare first-order value for new customers against the account average, so a cheap new customer of low value is visible rather than flattering.
6. State whether the campaign is doing the job it was bought for, and what it would cost to keep doing it.

## Decision rules

Every threshold is a starting heuristic, not a Google rule. Recalibrate per account.

| Verdict | Criteria |
|---|---|
| Doing its job | New-customer share of campaign conversions above roughly 60% [heuristic], and total customers acquired rose alongside the spend |
| Mixed | New-customer share 30-60%, OR total customers flat while orders rose |
| Not doing its job | New-customer share under roughly 30%, OR existing customers are not excluded and the repeat share matches the account baseline |

Exclusion rule: before calling a campaign bad at finding new people, check whether it was ever told to. A prospecting campaign without a customer exclusion is buying repeat orders by design and the fix is one setting, not a pause.

Value rule: cost per new customer is only half the answer. A cheap new customer whose first order is well below the account average may be a discount hunter, so report first-order value next to the cost.

## Output format

### New-customer verdict

Doing its job, mixed, or not doing its job.

### Customer growth, equal windows

| Window | Spend | Orders | Customers | New customers | New share |
|---|---:|---:|---:|---:|---:|

### Cost per new customer

Against cost per conversion, side by side.

### First-order value

New customers against the account average.

### Missing data

Whether the split was measured or estimated, and what that costs in confidence.

## Practical example

Campaign reports 88 conversions. The shop shows 61 new customers in the range against 44 in the equal window before launch, so 17 of the growth is attributable at cohort level at best. New-customer share of campaign conversions is 71%, cost per new customer is 2.4 times cost per conversion, and first-order value for new customers sits 18% below the account average. Output: doing its job on discovery, with a flag that the new cohort is buying cheaper and the second-order rate is the number to watch next.

## Guardrails

- Do not report a campaign-level new-customer share the account cannot attribute. Say it is cohort-level.
- Do not judge discovery on a campaign that never excluded existing customers.
- Do not present cost per new customer without first-order value beside it.
- Do not compare unequal windows.
