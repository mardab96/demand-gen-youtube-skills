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

## How to pull this

Interface labels move between Google Ads releases. Where a name below does not match what you see, the report is still the one described.

1. Open the campaign's assets view, which lists every image, video, headline and description in the campaign.
2. Add the policy or approval status column. This is the whole reason to pull it rather than looking at the campaign in the editor.
3. Record the aspect ratio of every asset. Where the interface does not show it, take it from the source file dimensions.
4. Note the count of headlines and descriptions too. A format with one headline has no rotation and behaves like a single asset.
5. **The trap:** a rejected or policy-limited asset looks exactly like an absent one in delivery, and exactly like a present one in a list of what you uploaded. Pull the status column or this skill will count assets that are not running.

## Before analysis

1. Start from the inventory below, then list what this campaign actually has. The gap is the whole analysis. Without a written spec the coverage grid has no rows and the model invents the left-hand column on every run.

**Asset inventory this skill grades against** `[heuristic — verify against current Google specs before treating a gap as a fact, these change]`:

| Type | Ratios that matter | Why it matters here |
|---|---|---|
| Image | 1.91:1 landscape, 1:1 square, 4:5 portrait | Missing 1:1 or 4:5 narrows feed and vertical surfaces sharply |
| Video | 16:9 landscape, 9:16 vertical, 1:1 square | Vertical-only sets concentrate on short-form by construction; landscape-only sets never reach it at all |
| Logo | 1:1, and 4:1 landscape where the format asks for it | Absence blocks some layouts entirely rather than degrading them |

Treat headline and description counts as part of coverage too: a format with one headline has no rotation and behaves like a single asset.
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

Read top to bottom and stop at the first row that matches, so an account that is
both thin and blocked is reported by its worse problem.

| Order | Verdict | Criteria |
|---:|---|---|
| 1 | Coverage is blocking delivery | A required ratio from the inventory absent entirely, OR spend concentrated on one surface that matches the only ratio present |
| 2 | Coverage is thin | A required ratio present with only one asset, OR one rejected asset in a format with no backup |
| 3 | Coverage is adequate | Every required ratio present with at least two assets each [heuristic] and no rejected assets |

The spend clause was removed from row 3 deliberately. This skill's first stated
trigger is a pre-launch check, where spend is zero and no distribution exists
yet, and requiring it there meant a fully prepared campaign matched no row at
all. Where the campaign is live, read the distribution with
`money-split-review-demand-gen` instead: concentration is a delivery question,
and it belongs to the skill that can act on it.

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

Campaign has four 9:16 videos, no 1:1, no 16:9 and no images at all. Two of the four videos are policy-limited, so the campaign has **two working assets, not four**, and both are the same shape.

Verdict: **coverage is blocking delivery** — five ratios from the inventory are absent entirely. Count them against the table above rather than from memory: image 1.91:1, image 1:1, image 4:5, video 16:9 and video 1:1. Logo coverage is unstated in this example, which is its own finding and goes in the missing-data section rather than being assumed present.

Production list, ranked by what each unlocks rather than by effort: two 16:9 videos first, since landscape video is the shape this campaign cannot reach at all; then 1:1 and 4:5 statics; then 1.91:1 landscape statics and a 1:1 video. Replacing the two policy-limited verticals comes after all of that, because the campaign already delivers in that shape.

**Handoff, so this does not become the same finding twice:** if the operator also arrived here from a spend-concentration reading, that read belongs to `money-split-review-demand-gen` and this skill supplies only the production list. Do not restate the surface split; cite it.

## Guardrails

- Do not recommend new assets without checking for rejections first.
- Do not treat one asset in a format as coverage.
- Do not confuse a coverage gap with creative fatigue; they need different work.
- Do not promise a surface will be reached once an asset exists. Say it becomes possible.
