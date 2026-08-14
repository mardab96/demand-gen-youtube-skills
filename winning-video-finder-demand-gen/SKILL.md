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

| Verdict | Criteria |
|---|---|
| Clear winner | One asset with at least roughly 30% better cost per result than the campaign average [heuristic], on 1,000+ impressions and 14+ days live |
| No winner yet | Assets within roughly 20% of each other, OR the leader has under 1,000 impressions |
| Delivery artefact, not a winner | One asset holds 70%+ of impressions and its cost per result is close to the campaign average |

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

Six assets. One carries 68% of impressions at a cost per result close to the average, so it is a delivery artefact rather than a winner. A second asset has 9% of impressions and a cost per result 44% better, on 2,300 impressions over three weeks. Output: no clear winner at campaign level, the small strong asset named as the real signal, brief for the next round built on its opening, and two assets under 400 impressions marked untested rather than failed.

## Guardrails

- Do not call the highest-spend asset the winner by default.
- Do not compare assets with very different time in market without saying so.
- Do not pause an asset that never received impressions and call it a decision.
- Do not describe a winner by file name.
