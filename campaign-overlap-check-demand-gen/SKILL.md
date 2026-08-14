---
name: campaign-overlap-check-demand-gen
description: Finds where Demand Gen, Performance Max, Video and Search campaigns are reaching and converting the same people, so the account is not paying twice and crediting three times. Use before adding a campaign type, when total results stay flat while a new campaign reports well, or during any budget reallocation.
---

# Are You Paying Twice For The Same Person - Demand Gen

## Use this skill when

A new campaign reports conversions and the account total did not move.

Common user requests:

- "Demand Gen is converting but revenue is flat."
- "Is this cannibalising Search?"
- "Should we run PMax and Demand Gen together?"
- "Where do I cut first?"

## When another skill owns the question

Enter here when the question is **whether another campaign already had these people**.

- If the question is *how the conversions were credited* — click, engaged view or
  exposure — that is `view-through-credit-check-demand-gen`, and it should be run
  first, because a large exposure share explains a platform-versus-business gap
  without any overlap at all.
- This skill sizes the suspicion and stops. **It never settles causation**, because
  overlap cannot be proven from platform data. When the sum exceeds the business
  total, it names the likely pairs and hands the settlement to
  `incremental-lift-design-demand-gen`.

## Required input

Minimum useful data:

- All active campaigns with spend, conversions and conversion value for the same closed range.
- Campaign types and the conversion actions each is optimising toward.
- Total business conversions for the range.

Recommended additional data:

- Account totals for the period before the newest campaign launched.
- Branded versus non-branded split on Search.
- Any audience exclusions between campaigns.

## Before analysis

1. Establish the account timeline: when each campaign launched, so before-and-after is available at all.
2. Confirm every campaign counts the same conversion action; where they do not, say so, because the totals are not addable.
3. Get the business total. Platform sums almost never equal it and the gap is the subject here.
4. Note that overlap between campaign types cannot be proven from platform data alone. This skill sizes the suspicion and says what would settle it.

## Analysis workflow

1. Sum platform-reported conversions across campaigns and compare with the business total for the same range.
2. Plot the account before and after the newest campaign launched: did total business outcomes rise by roughly what the new campaign claims?
3. Check branded Search volume in the same window. A rise alongside a new upper-funnel campaign is expected; a fall alongside a new campaign claiming credit is a warning.
4. Identify campaign pairs most likely to serve the same person: same audience source, same product, overlapping geography.
5. Where the sum exceeds the business total, distribute the excess across the likely pairs and state it as a range, not a figure.
6. Name the test that would settle it, rather than declaring a winner.

## Decision rules

Every threshold is a starting heuristic, not a Google rule. Recalibrate per account.

| Verdict | Criteria |
|---|---|
| No visible double counting | Platform sum within roughly 1.15x the business total [heuristic] |
| Suspected overlap | Platform sum 1.15-1.6x the business total, OR the newest campaign's claimed conversions exceed the rise in business total |
| Overlap is the working assumption | Platform sum above 1.6x business total, OR business total flat while a campaign claims material volume |

Launch-window rule: compare equal-length windows either side of the launch and say what else changed. A promotion or a seasonal shift in that window makes the comparison unusable, and saying so is the correct output.

Settlement rule: overlap is settled by turning something off in a controlled way, not by reasoning about attribution models. Hand that to the lift-test skill rather than concluding here.

## Output format

### Overlap verdict

None visible, suspected, or working assumption.

### Platform sum against business total

| Campaign | Type | Spend | Reported conversions |
|---|---|---:|---:|
| Platform sum | | | |
| Business total | | | |

### Before and after launch

Equal windows, with what else changed in each.

### Most likely pairs

Which campaigns are probably serving the same person, and why.

### What would settle it

The specific test, and its cost.

## Practical example

Four campaigns report 212 conversions combined; the shop recorded 129 for the same closed fortnight. Demand Gen launched three weeks ago claiming 61, and the business total rose by 11 against the preceding fortnight. Branded Search volume is unchanged. Output: overlap is the working assumption, Demand Gen and remarketing named as the likely pair, and a two-week geo holdout proposed as the settlement rather than a pause.

## Guardrails

- Do not add conversions across campaigns counting different actions.
- Do not declare cannibalisation from platform data alone.
- Do not compare windows in which a promotion ran.
- Do not recommend a pause as a diagnostic. Recommend a controlled test.
