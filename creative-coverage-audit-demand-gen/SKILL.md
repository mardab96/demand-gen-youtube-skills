---
name: creative-coverage-audit-demand-gen
description: Checks whether a Demand Gen campaign has the asset ratios, lengths and formats it needs to appear everywhere it is allowed to, because missing assets silently narrow delivery. Use before launch, when a campaign concentrates on one surface, or when delivery is smaller than the budget should buy.
---

# What Your Creative Is Missing - Demand Gen

## Use this skill when

The campaign cannot spend properly and nobody has looked at the asset list.

Common user requests:

- "Why is it not spending?"
- "Do I need vertical video?"
- "What assets should I make next?"
- "Everything is going to one placement."

## Required input

Minimum useful data:

- The full asset list for the campaign: every image and video, with aspect ratio and length.
- Spend and impressions by surface where available.
- Which formats the campaign is set to use.

Recommended additional data:

- Asset-level performance where the account reports it.
- The date each asset was added.
- Any assets rejected or limited by policy.

## Before analysis

1. List what the campaign type can serve, then list what this campaign actually has. The gap is the whole analysis.
2. Check for policy-limited or rejected assets before concluding anything is missing; a rejected asset looks identical to an absent one in delivery.
3. Note asset age. A set that has not changed in months is a fatigue question, not a coverage question, and belongs elsewhere.
4. Confirm the campaign is not budget-limited for an unrelated reason.

## Analysis workflow

1. Build a coverage grid: required ratios and formats down one side, present or absent across the other.
2. Mark each gap as blocking, limiting or cosmetic.
3. Cross-check the gaps against the surface split. A missing ratio usually shows up as a surface the campaign never reaches.
4. Count assets per format. One asset in a format is coverage on paper and fragility in practice.
5. Rank the missing assets by what each would unlock, not by how easy it is to make.
6. Produce a production list a designer can work from without further explanation.

## Decision rules

Every threshold is a starting heuristic, not a Google rule. Recalibrate per account.

| Verdict | Criteria |
|---|---|
| Coverage is adequate | Every required ratio present with at least two assets each [heuristic], no rejected assets, spend reaching more than one surface |
| Coverage is thin | A required ratio present with only one asset, OR one rejected asset in a format with no backup |
| Coverage is blocking delivery | A required ratio absent entirely, OR spend concentrated on one surface that matches the only ratio present |

Two-per-format rule: a single asset per format means one rejection or one fatigue curve takes the whole format offline. Treat one as zero when planning production.

Order rule: rank production by unlocked surface, not by effort. The cheapest asset to make is rarely the one holding delivery back.

## Output format

### Coverage verdict

Adequate, thin, or blocking.

### Coverage grid

| Format or ratio | Assets present | Rejected | Status |
|---|---:|---:|---|

### What each gap costs

| Gap | What it blocks | Priority |
|---|---|---|

### Production list

Concrete assets to make, in order.

### Missing data

What the account did not expose, such as asset-level performance.

## Practical example

Campaign has four vertical videos, no square, no landscape and no static images. Spend is 71% on one surface. Two of the four videos are policy-limited. Output: coverage is blocking delivery, production list starts with two landscape videos and two square statics rather than more vertical, and a note that the campaign has effectively two working assets, not four.

## Guardrails

- Do not recommend new assets without checking for rejections first.
- Do not treat one asset in a format as coverage.
- Do not confuse a coverage gap with creative fatigue; they need different work.
- Do not promise a surface will be reached once an asset exists. Say it becomes possible.
