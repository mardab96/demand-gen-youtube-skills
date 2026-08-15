---
name: weekly-readout-demand-gen
description: Produces the recurring Demand Gen update that separates facts from hypotheses from next actions, and names what needs a human decision, so a weekly report stops being a screenshot of the dashboard. Use every week on an active campaign, before a client or stakeholder call, or when someone asks how the campaign is going.
---

# The Weekly Demand Gen Readout - Demand Gen

## Use this skill when

Someone needs to know how it went without reading the account.

Common user requests:

- "Write the weekly update."
- "What do I tell the client?"
- "How is Demand Gen doing?"
- "Summarise the week."

## Required input

Minimum useful data:

- This week and last week: spend, impressions, engaged views, clicks, conversions, cost per result.
- Any change made during the week, with its date.
- The campaign's stated goal.

Recommended additional data:

- Business-recorded outcomes for the same period.
- The account's conversion lag, so unfinished days are handled correctly.
- View-through share, if the campaign reports it.

## How to pull this

Interface labels move between Google Ads releases. Where a name below does not match what you see, the report is still the one described.

1. Pull the campaign report for the closed week and for the week before it, so every number has a comparison.
2. Add the columns the readout will quote, and note for each which column it came from.
3. Pull the change history for the account over both weeks. A budget change, a bid change or a new asset explains most week-on-week movement, and a readout written without it will report a consequence as a discovery.
4. **The trap:** the last few days of "this week" are still filling. If you have no measured lag for the account, say so in the readout rather than assuming a window — the direction of that error is the same every single week, so it compounds into a trend that is not there.

## Before analysis

1. Apply the conversion lag before writing anything. A readout that treats the last three days as final will be wrong every week in the same direction.
2. Get the change log. A movement with a known cause is not a finding, and reporting it as one destroys trust in the rest.
3. Confirm what the campaign was bought for, because the headline metric follows from that.
4. Decide what the reader can actually act on. Everything else is context, and context goes below the fold.

## Analysis workflow

1. State the week in one sentence against the goal, before any table.
2. Put this week next to last week for the metrics that matter to the goal, and mark which days are still filling.
3. Separate three things explicitly: what happened (facts), what might explain it (hypotheses), what to do (actions).
4. For each hypothesis, name the evidence that would confirm or kill it, so next week has something to close.
5. List decisions the human has to make, with what each one costs and by when.
6. List what could not be answered this week and what would answer it.


## When another skill owns the question

- **"How long until these numbers are finished?"** That belongs to
  `conversion-lag-read-demand-gen`, which is the only skill in this pack that
  measures the fill curve, and the only one that owns the waiting-rule
  thresholds. This skill consumes that answer and never restates the curve. If
  you do not have a measured lag for the account, say so here rather than
  assuming a window: a readout that guesses the window is wrong in the same direction every week.

## Decision rules

Every threshold is a starting heuristic, not a Google rule. Recalibrate per account.

| Section | Rule |
|---|---|
| Facts | Only numbers from finished days. Anything inside the lag window is labelled as filling |
| Hypotheses | Never presented as causes. Each carries the check that would settle it |
| Actions | Each is one move with an owner. "Optimise the campaign" is not an action |
| Decisions | Only items the human must choose, each with its cost |

Movement rule: no movement is reported as a finding until it is checked against the change log. A budget increase explains a cost rise and is not an insight.

Honesty rule: a flat week is reported as a flat week. Manufacturing a finding to fill the readout is the failure mode this format exists to prevent.

## Output format

### The week in one line

Against the stated goal.

### This week against last

| Metric | Last week | This week | Change | Days still filling |
|---|---:|---:|---:|---|

### Facts

Finished-day numbers only.

### Hypotheses

| Hypothesis | Evidence for | What would settle it |
|---|---|---|

### Actions

| Action | Owner | By when |
|---|---|---|

### Decisions needed

| Decision | Options | Cost of each |
|---|---|---|

### Not answered this week

What, and what it would take.

## Practical example

Cost per result rose 34%. The change log shows the budget rose 60% on the Tuesday, so the rise is reported as expected rather than as a finding. Two days sit inside the lag window and are marked filling. The one real hypothesis is that a new asset is absorbing impressions at a worse rate, with the asset-level split named as the check for next week. One decision goes to the human: hold the higher budget for a second week or revert, with the cost of each stated.

## Guardrails

- Do not report unfinished days as results.
- Do not present a hypothesis as a cause.
- Do not invent a finding for a flat week.
- Do not write an action nobody owns.
- Do not include a metric the reader cannot act on just because it is available.
