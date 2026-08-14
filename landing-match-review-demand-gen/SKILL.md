---
name: landing-match-review-demand-gen
description: Checks whether the page a Demand Gen click lands on matches the promise and the temperature of the ad that sent it, because upper-funnel traffic arrives colder than search traffic and a page built for search will lose it. Use when clicks are cheap and conversions are absent, before scaling a campaign, or when one destination underperforms across every campaign feeding it.
---

# Where The Click Lands - Demand Gen

## Use this skill when

The traffic arrives and nothing happens after.

Common user requests:

- "Cheap clicks, zero conversions."
- "Should I send this to the homepage?"
- "The page converts fine on Search."
- "Do we need a separate landing page for this?"

## Required input

Minimum useful data:

- The destination URL or URLs used by the campaign.
- Sessions, bounce or engagement rate and conversion rate for that traffic, separated by source.
- The ad copy and the creative promise for the assets sending the traffic.

Recommended additional data:

- The same page's figures for search traffic, as a contrast.
- Mobile load time.
- Whether the page asks for a form, a purchase or something lighter.

## Before analysis

1. Open the destination page yourself, on mobile width, and read what it asks the visitor to do.
2. Read the ad promise next to it. Most findings here are a mismatch between the two, and neither number will show it.
3. Confirm the traffic can be separated by source, otherwise search visitors will flatter the page.
4. Note the temperature difference: this traffic did not search for anything, so a page written for existing intent is starting behind.

## Analysis workflow

1. Compare the page's conversion rate for this traffic against the same page for search traffic.
2. Compare engagement or bounce for the same split, so a page that loses people instantly is separated from one that holds them and fails to convert.
3. Check the match on three axes: promise, subject and ask. Ad and page must agree on what was offered, what it is about, and what the visitor must do next.
4. Judge the ask against the temperature: a demo request from cold upper-funnel traffic is a mismatch even when the page is well built.
5. Check load behaviour on mobile, because this traffic is overwhelmingly mobile.
6. Recommend one of three moves: change the ad promise, change the page, or change the ask.

## Decision rules

Every threshold is a starting heuristic, not a Google rule. Recalibrate per account.

| Verdict | Criteria |
|---|---|
| Page is fit for this traffic | Conversion rate at least roughly half the search rate on the same page [heuristic] and engagement comparable |
| Ask is too heavy | Engagement comparable to search traffic but conversion rate under a quarter of it |
| Wrong page | Engagement materially worse than search traffic, meaning people leave before considering the offer |

Homepage rule: sending upper-funnel traffic to a homepage is a decision, not a default. Where it is happening, say what it costs rather than assuming it is wrong; some businesses genuinely need the breadth.

Temperature rule: never recommend only page tweaks when the mismatch is in the ask. A lighter next step is the change, and it usually sits outside the page itself.

## Output format

### Fit verdict

Fit, ask too heavy, or wrong page.

### Split comparison

| Source | Sessions | Engagement | Conversion rate |
|---|---:|---:|---:|

### Match on three axes

| Axis | Ad says | Page says | Match |
|---|---|---|---|

### Recommended move

Promise, page or ask, with the reason.

### Missing data

What could not be separated by source.

## Practical example

Cold traffic converts at 0.3% where search converts at 2.6% on the same page, while engagement is nearly identical across both. The ad promises a free checklist and the page asks for a demo booking. Output: the ask is too heavy rather than the page being wrong, and the recommended move is to deliver the promised checklist on the page with the demo as a secondary step.

## Guardrails

- Do not judge the page without opening it on mobile width.
- Do not blame the page when the mismatch is in the ad promise.
- Do not compare against search traffic without separating the sources.
- Do not recommend a new landing page before checking whether the ask is the problem.
