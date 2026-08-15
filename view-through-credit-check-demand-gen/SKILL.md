---
name: view-through-credit-check-demand-gen
description: Separates the three ways a Demand Gen conversion can be credited, click-through, engaged-view and view-through, so a result is not read as action when most of it is exposure. Use before scaling, when Demand Gen reports strong conversions the rest of the account cannot find, or when comparing Demand Gen against Search on the same report.
---

# Did They Buy Or Did They Just Watch - Demand Gen

## Three kinds of credit, not two

Read this before anything else, because getting it wrong is the most common way this
campaign type gets misjudged, and subtracting one column from another gives the wrong
answer:

| Credit type | What happened | Where it hides |
|---|---|---|
| Click-through | The person clicked the ad and converted | The base conversion count |
| **Engaged-view** | The person watched roughly ten seconds or more, did not click, and converted within a few days | **Inside the headline conversion figure on Demand Gen and Video campaigns**, which is why the count looks large without matching traffic |
| View-through | The person saw the ad, did not engage with it, and converted later | Usually a separate column, often excluded from the main count |

Engaged-view credit is the one people miss, because it is neither a click nor a
classic view-through, and on this campaign type it is frequently the largest of the
three.

🔴 **The arithmetic follows from where each one sits, and getting the direction wrong
is worse than not splitting at all.** `Conversions` contains click-through **and**
engaged-view. `View-through conv.` sits outside it, as its own additive column. So:

```
click-through  =  Conversions  −  Engaged-view conversions
total credited =  Conversions  +  View-through conv.
```

**Subtracting view-through from `Conversions` removes a quantity that was never in
there.** It returns `Conversions` unchanged and labels it click-through, which is the
exact mistake this skill exists to prevent, and an earlier version of this file made
it in its own worked example. If the account does not expose an engaged-view column,
you cannot compute click-through: report `Conversions` as **click-through plus
engaged-view, unresolved**, and say so.

## Use this skill when

The campaign reports conversions and nothing else in the business moved.

Common user requests:

- "Demand Gen says 90 conversions, where are they?"
- "Can I compare this to Search?"
- "How much of this is view-through?"
- "Should I scale this campaign?"

## When another skill owns the question

Three skills in this pack are reached by the same sentence, so each says here which
one owns it rather than leaving the reader to guess:

- **"Demand Gen reports conversions and revenue is flat."** Start here only if the
  question is *how the conversions were credited*. If the question is *whether the
  spend caused anything*, that is `incremental-lift-design-demand-gen`. If the
  question is *whether another campaign already had those people*, that is
  `campaign-overlap-check-demand-gen`.
- This skill never designs a test. When its output points at causation, it names the
  lift skill and stops.

## Required input

Minimum useful data:

- Google Ads report with the conversion columns split out.
- Spend and the conversion action being counted.
- Business-recorded conversions for the same closed range.

Recommended additional data:

- The same split for Search or another click-driven campaign, as a contrast.
- The conversion window in use.
- Any concurrent brand activity that would raise baseline demand.

## How to pull this

1. In Google Ads, open the campaign report and use the column picker, not a default view.
2. Under Conversions, add: `Conversions`, `All conv.`, `View-through conv.` and `Engaged-view conversions`. On many accounts the last two are not shown by default and their absence is the reason people think the split is unavailable.
3. Set the date range to a closed period. Nothing here works on an open range.
4. Export at campaign level, and repeat for one click-driven campaign in the same account as a contrast.
5. **The trap:** `Conversions` and `All conv.` are different columns and on this campaign type the gap between them is routinely large. Note which one every figure in your analysis came from, and say so in the output. Subtracting the wrong pair produces a click-through figure that silently includes engaged-view credit.

## Confirm this in the account before you subtract anything

This skill rests on one claim: that engaged-view credit is counted inside the
`Conversions` column while view-through credit sits outside it. On most accounts
that holds. It is not a law of physics, it is a consequence of how the account's
conversion actions are configured, so confirm it here rather than assuming it.

1. Open the conversion actions list in the account's settings.
2. For each action you care about, note whether it is marked primary, and what
   its counting and inclusion settings say. Actions excluded from the main
   reporting column will not be in `Conversions` no matter what this skill says.
3. If the account has several conversion actions and the campaign optimises to
   one while the report totals all of them, say so in the output. That single
   mismatch explains more platform-versus-backend arguments than credit type does.

**Modelled conversions.** Some of what the platform reports was not observed. It
was estimated, because consent choices and browser restrictions mean a share of
real conversions are never directly linked to the ad that caused them, and the
platform fills that hole with a model. This matters here for one reason: it is
a second, independent explanation for the same gap this skill measures. A
campaign whose reported total exceeds the shop's count may be crediting exposure
(what this skill is about), or may be modelling behaviour it could not see, or
both, and the split between those two is not something the report will hand you.

Do not present the credit split as the complete account of the gap. Where the
numbers still disagree after this analysis, modelling is the next place to look,
and after that the plain possibility that not every order came from advertising
at all.

## Before analysis

1. Read the conversion window off the account. A long window with view-through credit will claim a lot by construction.
2. Confirm which conversion action is being counted and whether it is the one the business cares about.
3. Confirm the range is closed.
4. Note that view-through credit is not fraud. It is a modelling choice, and the question is what to bet on it.

## Analysis workflow

1. Split reported conversions three ways: click-through, engaged-view and view-through, as counts and as shares. Where the account exposes only two of the three, say which one is missing and treat the remainder as unresolved rather than folding it into click-through.
2. Recompute cost per conversion on click-through only, and state both numbers side by side.
3. Compare Demand Gen's view-through share against a click-driven campaign in the same account, so the reader has a contrast rather than an absolute.
4. Compare the click-through figure against business-recorded conversions for the range.
5. Say what the campaign looks like if the business plans on the click-through number alone.
6. Where view-through share is high and the business cannot see the outcome, route the question to a lift test rather than declaring the campaign good or bad.

## Decision rules

Every threshold is a starting heuristic, not a Google rule. Recalibrate per account.

| Verdict | Criteria |
|---|---|
| Comparable to click campaigns | Click-through is 75% or more of **total credited** [heuristic], where total credited is `Conversions + View-through conv.` — state the denominator in the output, because the two candidate denominators differ by nearly a factor of two |
| Report both numbers | Click-through 40% up to but not including 75% of total credited |
| Do not compare this to Search | Click-through under 40% of total credited, OR click-through below what the business can independently see, OR **the account cannot separate engaged-view credit at all**, in which case click-through is unknown rather than low |

Comparison rule: never put a Demand Gen cost per conversion next to a Search cost per conversion without stating the view-through share of each. The two numbers answer different questions and the comparison is the single most common way this campaign type gets misjudged.

Escalation rule: high view-through share plus flat business results is not proof of failure. It is the exact condition a lift test exists for, and that is the recommendation.

## Output format

### Credit verdict

Comparable, report both, or not comparable.

### Split

| Measure | Click-through | Engaged-view | View-through | Total credited |
|---|---:|---:|---:|---:|

State which column each figure came from. Where engaged-view is unavailable, put
`unresolved` in the click-through cell rather than a number.

### Cost per conversion, both ways

Click-through only, and as reported.

### What to do next

Plan on the stricter number, or run a lift test, with the reason.

### Missing data

Whether the account exposed the split at all.

## Practical example

Demand Gen reports 94 in `Conversions` at 21 cost per conversion, so spend on the range is 1,974. `View-through conv.` shows 72 in its own column. The engaged-view segment splits the 94 into 58 engaged-view and 36 click-through.

Work it in this order, because the direction is the whole point:

- click-through = `Conversions` minus engaged-view = 94 - 58 = **36**. It is never `Conversions` minus view-through, because view-through was never inside `Conversions` to begin with. Subtracting it removes something that was never in the total and hands back a click-through figure that is too small by exactly the engaged-view count.
- total credited = `Conversions` plus `View-through conv.` = 94 + 72 = **166**
- click-through share = 36 / 166 = **22%**, which is under the 40% line
- click-through cost per conversion = 1,974 / 36 = **54.83**, against the 21 the platform reports

Search in the same account runs at 4% view-through. Business orders are flat week on week. Output: not comparable to Search, plan on 54.83 rather than 21, and the recommendation is a lift test rather than a scale or a pause.

## Guardrails

- Do not present total conversions as the headline when view-through dominates.
- Do not compare across campaign types without stating both view-through shares.
- Do not call view-through credit fake. Call it exposure credit and price it accordingly.
- Do not recommend a pause on this evidence alone.
