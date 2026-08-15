---
name: incremental-lift-design-demand-gen
description: Designs a geo split or holdout that answers whether upper-funnel spend causes outcomes or reports outcomes that would have happened anyway, and says when the account is too noisy to run one. Use when a campaign reports well while business results stay flat, before scaling upper-funnel budget, or before cutting a campaign that reports strongly.
---

# Would These Sales Happen Anyway - Demand Gen

## Use this skill when

The reported result is good and the business cannot feel it.

Common user requests:

- "Demand Gen reports 90 conversions and revenue is flat."
- "How do I prove this is working?"
- "Can I just turn it off for a week?"
- "Is upper funnel worth it for us?"

## When another skill owns the question

This skill is the end of the line for causation. Two others route here rather than
answer it themselves, and neither should be run instead of this one:

- **"How was this credited?"** belongs to `view-through-credit-check-demand-gen`.
  It splits the reported count three ways and stops. When its output points at
  causation, it names this skill.
- **"Did another campaign already have these people?"** belongs to
  `campaign-overlap-check-demand-gen`. It sizes the suspicion from platform sums
  against the business total and stops, because overlap cannot be settled from
  platform data. It names this skill too.

So arriving here means the question has already been narrowed to whether the spend
caused anything. **This skill designs the test. It does not hand the question on.**
Its only permitted refusal is to say the account's baseline is too noisy to produce
a readable one, which is a verdict, not a handoff.

## Required input

Minimum useful data:

- Total business revenue or lead volume by week for at least 8 weeks.
- Campaign spend by week for the same period.
- The campaign under question with its reported conversions.

Recommended additional data:

- Revenue by region where the business sells across several.
- Any past period when this campaign was off.
- Promotional and seasonal calendar.

## How to pull this

Interface labels move between Google Ads releases. Where a name below does not match what you see, the report is still the one described.

1. The input here is a business outcome, not a platform report. Pull weekly revenue, orders or leads from the shop or CRM for at least the last eight weeks, and twelve if you have them.
2. One row per week, two columns: `week` and `value`. That is exactly what `../scripts/baseline_spread.py` reads.
3. Mark every week that contained a promotion, a price change, a stockout or a seasonal peak.
4. **The trap:** never use platform-reported conversions as the baseline. A test built to measure whether the platform's numbers are real cannot be judged against the platform's numbers.

## Before analysis

1. Establish the baseline: what a week looks like with none of this spend. Without such a period, the test has to create one.
2. Confirm the business can read outcomes at the level the test will split on.
3. Ask what loss the business will accept during the test. A holdout costs real outcomes and that is the price of the answer.
4. Check the window for promotions or seasonality. Either one makes the result unreadable.

## Analysis workflow

1. Compute weekly business outcomes, their median and their spread, so the test can be sized against real noise.
   **Run `../scripts/baseline_spread.py weekly.csv` for this step.** It implements the readiness thresholds in this file and returns exit code 1 when the baseline cannot support a readable test, so a decorative holdout has to be approved deliberately rather than by accident. Exit code 2 is different and means it could not read your file at all; do not read that as a verdict about the account.
2. Choose the shape: geo split where regions are comparable, audience holdout where they are not, on-off where the account is small and the baseline is quiet.
3. Size the test: how many weeks are needed for a difference to clear normal variation.
4. Define the single read-out metric, taken from business data and never from the platform's own conversions.
5. Write down the expected result under both hypotheses before the test runs.
6. Set the stop rule and the maximum acceptable loss.
7. State plainly what the test will not answer.

## Decision rules

Every threshold is a starting heuristic, not a Google rule. Recalibrate per account.

Two measures of variation, not one, and both are gated. **Typical variation** is
the median week's distance from the median week. **Worst-week variation** is the
single furthest week's distance from it. A history can be calm on the first and
still be unusable because of the second, and that is the case a single measure
misses. `scripts/baseline_spread.py` prints both and implements exactly the
bands below.

Read the table top to bottom and stop at the first row that matches. Bands are
written so that no value can satisfy two rows.

| Verdict | Criteria |
|---|---|
| Do not run it yet | A promotion or seasonal peak inside the window, OR outcomes cannot be read at the split level, OR typical variation above 50% [heuristic], OR worst-week variation above 100% |
| Needs a longer window | Fewer than 8 weeks of history, OR typical variation above 25% (up to and including 50%), OR worst-week variation above 60% (up to and including 100%) |
| Test is readable | Everything else: 8+ weeks, typical variation 25% or under, worst week 60% or under, no promotion in the window |

Size rule: a holdout too small returns a result that cannot clear noise, which reads as "no effect" and gets quoted as proof of one. Where the baseline cannot support a readable holdout, say the test is unavailable rather than running a decorative one.

Read rule: report the observed difference next to normal weekly variation, always as a range. A point estimate here invites a conclusion the data cannot carry.

## Output format

### Test readiness

Readable, needs longer window, or not yet.

### Design

| Element | Choice | Why |
|---|---|---|

### Baseline

Weekly business figures, median and spread.

### Stop rule and maximum loss

The number that ends the test early, and the cost being accepted.

### What this will not answer

Named explicitly.

## Practical example

Campaign reports 61 conversions a week; business revenue has been flat for **nine weeks** with 17% variation around its median and no promotion planned. Nine weeks clears the eight-week floor and 17% clears the 25% spread line, so the verdict is **readable**. An earlier draft of this example used six weeks, which its own entry condition rejects.

Design: a three-week geo holdout across two comparable regions, read on shop revenue rather than platform conversions, expected outcomes written down in advance, and a stop rule at a 20% revenue drop in the held-out region.

**One platform constraint to state in the output, because the reader will hit it immediately:** Google Ads does run experiments on this campaign type, but not in the geo-holdout shape this design needs, and drafts are not available for it, so a geo split has to be built by hand as two duplicate campaigns on separate geographies. [HIPOTEZA — review 2026-11-15: confirm which experiment types Demand Gen currently supports before relying on this sentence.] That carries its own learning period and its own budget, and both belong in the cost the business is accepting. Google's own Conversion Lift study is the alternative worth asking your rep about before building it yourself; it is usually gated on spend.

## Guardrails

- Do not read the test on the platform's own conversions.
- Do not run it through a promotion or a seasonal peak.
- Do not report a result inside normal variation as a finding.
- Do not present a holdout as free. State the expected cost up front.
- Do not treat an accidental past pause as a clean test without checking what else changed.
