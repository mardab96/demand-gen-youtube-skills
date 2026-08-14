---
name: feed-readiness-check-demand-gen
description: Checks whether a product feed is complete and clean enough for a feed-driven Demand Gen campaign to show the right products at the right price, before budget goes behind it. Use before launching a feed-based campaign, when a campaign shows a narrow slice of the catalogue, or when the ads show prices the shop does not have.
---

# Is Your Feed Ready For Demand Gen - Demand Gen

## Use this skill when

The campaign will pull products from a feed and nobody has read the feed.

Common user requests:

- "Can we run this off the feed?"
- "Why does it only show six products?"
- "The price in the ad is wrong."
- "Half the catalogue never appears."

## Required input

Minimum useful data:

- Feed diagnostics from the merchant account: total items, active, disapproved, pending.
- A sample of feed rows with the fields present.
- The number of products the business believes it sells.

Recommended additional data:

- Disapproval reasons grouped by count.
- Image availability and size per item.
- Which products the business actually wants promoted.

## Before analysis

1. Compare item count in the feed with the count the business believes it has. A gap here explains most narrow-delivery complaints before any field is examined.
2. Check when the feed last refreshed. A stale feed with correct fields is still wrong on price and availability.
3. Confirm which fields this campaign type needs, and separate them from fields that are merely nice to have.
4. Note that disapprovals and omissions look identical from the campaign side.

## Analysis workflow

1. Build the funnel of the catalogue: total items, submitted, active, actually eligible to serve.
2. Group disapprovals by reason and count, and rank by how many items each reason blocks.
3. Check the required fields across the sample: identifier, title, price, availability, image, product category.
4. Check title quality separately from title presence. A title that is a bare SKU is present and useless.
5. Check price and availability against the shop for a handful of items, so freshness is measured rather than assumed.
6. Rank fixes by number of items unlocked, and name which are the shop's job and which are the feed's.

## Decision rules

Every threshold is a starting heuristic, not a Google rule. Recalibrate per account.

| Verdict | Criteria |
|---|---|
| Feed is ready | 90%+ of intended products active [heuristic], required fields present on all sampled rows, price and availability match the shop on spot checks |
| Fix before scaling | 70-90% active, OR one disapproval reason blocking more than 10% of items |
| Not ready | Under 70% active, OR price or availability wrong on any spot check, OR identifiers missing |

Price rule: a single wrong price in a spot check fails the whole feed. It is the one defect that damages trust with the customer rather than merely reducing reach.

Title rule: titles that are SKUs or model codes pass a completeness check and fail the campaign. Report them as a defect even though nothing is technically missing.

## Output format

### Feed verdict

Ready, fix before scaling, or not ready.

### Catalogue funnel

| Stage | Items | Share of intended |
|---|---:|---:|

### Disapprovals by reason

| Reason | Items blocked | Whose fix |
|---|---:|---|

### Field check

| Field | Present | Quality issue |
|---|---|---|

### Spot checks

Item, feed price, shop price, feed availability, shop availability.

### Fix order

Ranked by items unlocked.

## Practical example

Feed submits 1,240 items against a catalogue of 1,900. Of those, 812 are active, which is **43% of the intended catalogue** and puts the feed in the "not ready" band on its own. One disapproval reason accounts for 310 blocked items, which is **25% of what was submitted and 16% of the intended catalogue** — both denominators stated, because the guardrail at the bottom of this skill forbids a bare percentage and an earlier draft of this example broke it.

Two of five spot-checked prices are stale by one promotional cycle.

Verdict: **not ready**. The single disapproval reason ranks first in the fix order because it unlocks more items than anything else available, and the price staleness is flagged as blocking regardless of any count, because a wrong price damages trust with the customer rather than merely reducing reach.

## Guardrails

- Do not judge a feed by field presence alone. Check quality and freshness.
- Do not treat missing items as disapproved items; they need different fixes.
- Do not recommend launching a feed campaign with wrong prices under any reach argument.
- Do not report a percentage without saying what the denominator is.
