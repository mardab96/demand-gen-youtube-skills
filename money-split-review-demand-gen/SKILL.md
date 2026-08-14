---
name: money-split-review-demand-gen
description: Breaks a Demand Gen campaign down by where the money actually went across YouTube in-feed, Shorts, Discover and Gmail, because the campaign reports one blended result for four very different surfaces. Use before scaling, when results move without a change, when a campaign looks fine and feels wrong, or when cheap impressions arrive in volume and nothing follows.
---

# Where Your Money Actually Went - Demand Gen

## Use this skill when

One campaign spent across four surfaces and reported a single number.

Common user requests:

- "Where is this budget actually going?"
- "Demand Gen looks fine but I cannot tell why."
- "Is Shorts getting all of it?"
- "Can I turn off Gmail?"

## When another skill owns the question

When the finding turns out to be the asset set rather than the surfaces, this skill
names the gap and stops. The production list belongs to
`creative-coverage-audit-demand-gen`, which owns the asset inventory. Do not produce
two versions of the same recommendation.

## Required input

Minimum useful data:

- Google Ads report for the Demand Gen campaign, segmented by network or placement where available.
- Spend, impressions, clicks and conversions for the same closed date range.
- Which ad formats are running: video, image, carousel.

Recommended additional data:

- The same split for a second, older period, so drift is visible.
- Conversion value per surface if the account tracks it.
- Any channel exclusions already applied.

## Before analysis

1. Confirm what the account can actually split. Demand Gen exposes less surface detail than Video campaigns do, so name the limit before analysing rather than after.
2. Confirm the date range is closed.
3. Note that surfaces are not separately biddable in Demand Gen. Anything you find turns into a creative or exclusion decision, not a bid decision.
4. Check whether the campaign changed format mix in the range. That moves the split on its own.

## Analysis workflow

1. Lay out spend, impressions, clicks and conversions per available surface.
2. Compute cost per result and click-through rate per surface, not just share of spend.
3. Compare share of spend against share of conversions. The gap is the finding.
4. Check whether one surface carries most of the impressions but little of the outcome.
5. Look at whether the format mix explains the split: a campaign with only vertical video will lean to Shorts by construction.
6. Turn the read into one of three moves: change creative mix, apply an exclusion where the account allows it, or accept the split and say why.

## Decision rules

Every threshold is a starting heuristic, not a Google rule. Recalibrate per account.

Read one number and one number only: **the gap in percentage points between a surface's share of spend and its share of conversions.** The three bands below partition that single number, so no campaign falls between them and none matches two. An earlier version added a second condition to the bottom row, which reintroduced exactly the ambiguity this table exists to remove.

| Verdict | Criteria |
|---|---|
| Split is healthy | No surface with a spend-to-conversion gap above roughly 15 points [heuristic], whatever its share of spend |
| Watch it | Largest gap 15-35 points |
| Act on the split | Largest gap above 35 points |

`Conversions` and `All conv.` are different columns and on this campaign type the difference is routinely large. **State which column every figure came from.** Two people reading the same export with different columns will produce different verdicts, and neither will know why.

Format rule: before recommending an exclusion, check the creative mix. A split caused by having only one asset ratio is a creative problem wearing a targeting costume, and the exclusion will not fix it.

Reporting limit rule: where the account cannot split the surfaces at all, **do not stop, and do not infer the split either.** Switch to the read the account CAN support and say that is what you are doing: format mix against spend pattern, cost per thousand impressions against the account's other campaign types, and week-on-week movement in that figure. That answers the operator's real question, which is whether the money is going somewhere cheap and empty, without pretending to a placement report the platform never gave you. State plainly which of the two reads you ran.

## Output format

### Split verdict

Healthy, watch it, or act.

### Surface table

| Surface | Spend | Share of spend | Impressions | Clicks | Conversions | Share of conversions | Cost per result |
|---|---:|---:|---:|---:|---:|---:|---:|

### The gap

Where share of spend and share of outcome diverge, and by how much.

### Recommended move

Creative mix, exclusion, or accept, with the reason.

### Missing data

Which surfaces the account could not report, and what that blocks.

## Practical example

A campaign spends 71% on one surface that returns 12% of conversions, a gap of 59 points. The creative set is three vertical videos and no landscape or square assets. Verdict: **act on the split** — 59 points is well above the 35-point line; an earlier draft of this example called it watch it. No exclusion recommended even so, and the first move is adding landscape and square assets so the campaign has somewhere else to spend, with a re-read in two weeks.

## Guardrails

- Do not recommend excluding a surface before checking the creative mix.
- Do not treat share of impressions as share of value.
- Do not present a split the account could not report. Say it was unavailable.
- Do not read a split from an open date range.
