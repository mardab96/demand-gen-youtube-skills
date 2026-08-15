---
name: winning-video-finder-demand-gen
description: Finds which individual asset carried a Demand Gen campaign and which ones rode along, so the next production round copies the thing that worked instead of the campaign average. Use after a campaign has run long enough to separate assets, before commissioning new creative, or when a campaign result cannot be traced to anything specific.
---

# Which Video Actually Did The Work - Demand Gen

## Use this skill when

The campaign worked and nobody can say which asset made it work.

Common user requests:

- "Which video should we make more of?"
- "The campaign is fine, what do I brief next?"
- "Is it the creative or the audience?"
- "Can I turn the weak ones off?"

## Required input

Minimum useful data:

- Asset-level report: impressions, engaged views, clicks, conversions and spend per asset.
- Asset lengths, formats and the date each entered the campaign.
- The campaign objective and bid strategy.

Recommended additional data:

- Thumbnails or short descriptions of what each asset shows.
- The hook of each asset, meaning what happens in the first three seconds.
- Any asset paused mid-flight and when.

## How to pull this

Interface labels move between Google Ads releases. Where a name below does not match what you see, the report is still the one described.

1. Open the asset-level report for the campaign, not the campaign or ad-group total.
2. Add: `Impressions`, `Cost`, `Conversions`, `Clicks` and the performance label where the account shows one.
3. Set a closed date range long enough that each asset has meaningful volume, and record the date each asset entered the campaign.
4. **The trap:** assets do not get equal exposure, so the one with the most conversions is often just the one that was served most. An asset live for four days is not comparable to one live for forty, and nothing in the report will warn you.

## Before analysis

1. Check how long each asset has been live. An asset added last week cannot be compared with one that has run a month.
2. Check whether spend was distributed or concentrated. Where the system gave one asset most of the impressions, its result is partly a delivery artefact.
3. Confirm the campaign is not so small that per-asset numbers are noise.
4. Note that assets inside one campaign do not compete cleanly; this is a read, not an experiment.

## Analysis workflow

1. Normalise: compute cost per result and conversion rate per asset, not raw totals.
2. Rank assets by outcome per unit of spend, then check whether the ranking survives when you restrict to assets with comparable time in market.
3. Identify the concentration: what share of impressions and of conversions the top asset carries.
4. Separate three cases: an asset that won on merit, an asset that won because it got the delivery, and an asset that never got enough impressions to be judged.
5. Describe what the winner has in common that the others do not, in concrete terms, such as hook, length, format, or whether a person speaks.
6. Turn that into a brief for the next round, and a list of assets safe to retire.

## Decision rules

Every threshold is a starting heuristic, not a Google rule. Recalibrate per account.

**Run the tests in this order.** The delivery-artefact test comes first, and when it fires you exclude that asset and re-run the other two on what is left. Without a stated order, one asset can satisfy two rows at once and the verdict depends on which row you read first.

| Order | Verdict | Criteria |
|---:|---|---|
| 1 | Delivery artefact, not a winner | One asset holds 70%+ of impressions [heuristic] and its cost per result is within roughly 15% of the campaign average. Exclude it, then run tests 2 and 3 on the remainder |
| 2 | Clear winner | One asset at least roughly 30% better on cost per result than the average of the remainder, on 1,000+ impressions and 14+ days live |
| 3 | No winner yet | Everything else: assets within roughly 30% of each other, OR the leader is under 1,000 impressions, OR the leader is under 14 days live |

Retirement rule: an asset with meaningful impressions and materially worse cost per result is a retirement candidate. An asset with almost no impressions is not a loser; it never got a hearing, and pausing it teaches nothing.

Brief rule: describe the winner by what it does, not by its file name. "A person speaking to camera in the first two seconds, no music intro" is a brief; "asset 4" is not.

## Output format

### Winner verdict

Clear winner, no winner yet, or delivery artefact.

### Asset table

| Asset | Days live | Impressions | Engaged views | Clicks | Conversions | Cost per result |
|---|---:|---:|---:|---:|---:|---:|

### What the winner has that the others do not

Concrete, describable attributes.

### Next brief

What to make more of, in a form a creator can act on.

### Retire

Assets to stop, and assets that were never really tested.

## Practical example

Six assets. Test 1: one asset carries **74%** of impressions at a cost per result 6% off the campaign average, so it fires the delivery-artefact rule and is excluded.

Test 2 on the remaining five: one asset has 2,300 impressions over 21 days at a cost per result **44% better than the average of the remainder**. That clears all three conditions, so it is the **clear winner** — the earlier draft of this example called it "no winner", which its own table does not support.

Two assets sit under 400 impressions and are marked untested rather than failed, because test 3's impression floor is about whether an asset got a hearing, not about whether it is any good.

The brief for the next round is built on the winner's opening, described by what it does: a person speaking to camera inside the first two seconds, no music intro.

## Guardrails

- Do not call the highest-spend asset the winner by default.
- Do not compare assets with very different time in market without saying so.
- Do not pause an asset that never received impressions and call it a decision.
- Do not describe a winner by file name.
