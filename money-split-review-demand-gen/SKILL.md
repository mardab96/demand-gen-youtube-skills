---
name: money-split-review-demand-gen
description: Breaks a Google Ads Demand Gen campaign down by channel across YouTube, Discover, Gmail and Display, because the campaign reports one blended result by default even though the channels can be reported and controlled separately. Use before scaling, when results move without a change, when a campaign looks fine and feels wrong, or when cheap impressions arrive in volume and nothing follows.
---

# Where Your Money Actually Went - Demand Gen

## Use this skill when

One campaign spent across four channels - YouTube, Discover, Gmail and Display - and reported a single number.

Whether short-form appears as its own row and its own switch, or sits inside a single YouTube entry, differs between accounts. Check your campaign's own channel controls before concluding a row is missing. [HIPOTEZA — review 2026-11-15.]

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

## How to pull this

Interface labels move between Google Ads releases. Where a name below does not match what you see, the report is still the one described.

1. Open the campaign, then the channel or placement breakdown for it. Interface labels for this view move between releases; you are looking for the report that lists YouTube, Discover, Gmail and Display as separate rows rather than one campaign total.
2. Add, at minimum: `Cost`, `Impressions`, `Clicks`, `Conversions` and `Conv. value`. Without cost and conversions on the same rows there is no gap to measure.
3. Set a closed date range with no format-mix change inside it. A campaign that gained a new asset shape mid-range will show a split that describes the change, not the campaign.
4. Separately, open the campaign settings and note which channels are switched on. An enabled channel taking no spend and a disabled channel look identical in a report that only lists what spent.
5. **The trap:** the exact set of channel rows differs between accounts and has changed over time. If a row you expected is missing, check the campaign's channel controls before concluding the report is broken.

## Before analysis

1. Pull the channel-level report. Confirm which channels the campaign is set to use, and which of those actually took spend — a channel enabled and unused is a different finding from one disabled.
2. Confirm the date range is closed.
3. **Check the campaign's channel controls before anything else.** Demand Gen exposes channel selection — YouTube, Discover, Gmail and Display — so what you find here turns into a channel decision, a creative decision, or both. This is the lever, and it is in the campaign settings.
   ⚠️ Confirmed present by the account owner on 2026-08-14. An earlier version of this skill was written on the assumption that no such control existed and that the split was usually unavailable; that assumption was wrong and shaped the whole file. If you are working in an account or market where the controls are not present, the fallback read below still applies, but treat it as the exception rather than the expected case.
4. Check whether the campaign changed format mix in the range. That moves the split on its own.

## Analysis workflow

1. Lay out spend, impressions, clicks and conversions per available surface.
2. Compute cost per result and click-through rate per surface, not just share of spend.
3. Compare share of spend against share of conversions. The gap is the finding.
4. Check whether one surface carries most of the impressions but little of the outcome.
5. Look at whether the format mix explains the split: a campaign with only vertical video will lean to short-form YouTube inventory by construction.
6. Turn the read into one of three moves, named the same way in the output section below: **exclusion** (switch a channel off), **creative mix** (give the campaign somewhere else worth spending), or **accept** the split and say why.

## Decision rules

Every threshold is a starting heuristic, not a Google rule. Recalibrate per account.

Read one number and one number only: **the gap in percentage points between a surface's share of spend and its share of conversions.** The three bands below partition that single number, so no campaign falls between them and none matches two. An earlier version added a second condition to the bottom row, which reintroduced exactly the ambiguity this table exists to remove.

| Verdict | Criteria |
|---|---|
| Split is healthy | Largest gap 15 points or below [heuristic], whatever the channel's share of spend |
| Watch it | Largest gap above 15 points, up to and including 35 |
| Act on the split | Largest gap above 35 points |

A gap of exactly 15 points is healthy and exactly 35 is watch it. The earlier
wording said "above 15" in one row and "15-35" in the next, which put both
endpoints in two rows at once - in a table whose own opening sentence claims it
partitions the number.

`Conversions` and `All conv.` are different columns and on this campaign type the difference is routinely large. **State which column every figure came from.** Two people reading the same export with different columns will produce different verdicts, and neither will know why.

Format rule: **before turning a channel off, check the creative mix.** A split caused by owning only one asset ratio is a creative problem wearing a targeting costume, and disabling a channel will not fix it — it will shrink delivery and leave the same asset gap. Where the campaign has no assets for the channels you would keep, production comes first and the channel decision waits.

Fallback rule, for the accounts where the channel report is genuinely unavailable: **do not stop, and do not infer the split either.** Switch to the read the account can support — format mix against spend pattern, cost per thousand impressions against the account's other campaign types, and week-on-week movement in that figure — and say plainly which of the two reads you ran. This is now the exception, not the default; where the channel report exists, use it.

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
