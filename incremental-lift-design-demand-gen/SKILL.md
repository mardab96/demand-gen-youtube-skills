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

- Total business revenue or lead volume by week for at least 8 weeks.
- Campaign spend by week for the same period.
- The campaign under question with its reported conversions.

Recommended additional data:

- Revenue by region where the business sells across several.
- Any past period when this campaign was off.
- Promotional and seasonal calendar.

## Before analysis

1. Establish the baseline: what a week looks like with none of this spend. Without such a period, the test has to create one.
2. Confirm the business can read outcomes at the level the test will split on.
3. Ask what loss the business will accept during the test. A holdout costs real outcomes and that is the price of the answer.
4. Check the window for promotions or seasonality. Either one makes the result unreadable.

## Analysis workflow

1. Compute weekly business outcomes, their median and their spread, so the test can be sized against real noise.
   **Run `scripts/baseline_spread.py weekly.csv` for this step.** It implements the readiness thresholds in this file and returns a non-zero exit code when the baseline cannot support a readable test, so a decorative holdout has to be approved deliberately rather than by accident.
2. Choose the shape: geo split where regions are comparable, audience holdout where they are not, on-off where the account is small and the baseline is quiet.
3. Size the test: how many weeks are needed for a difference to clear normal variation.
4. Define the single read-out metric, taken from business data and never from the platform's own conversions.
5. Write down the expected result under both hypotheses before the test runs.
6. Set the stop rule and the maximum acceptable loss.
7. State plainly what the test will not answer.

## Decision rules

Every threshold is a starting heuristic, not a Google rule. Recalibrate per account.

| Verdict | Criteria |
|---|---|
| Test is readable | Weekly outcome variation under roughly 25% of its median [heuristic], 8+ weeks of history, no promotion in the window |
| Needs a longer window | Variation 25-50%, or fewer than 8 weeks of history |
| Do not run it yet | Variation above 50%, OR a promotion inside the window, OR outcomes cannot be read at the split level |

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

**One platform constraint to state in the output, because the reader will hit it immediately:** Google Ads drafts and experiments do not cover this campaign type, so a geo split has to be built by hand as two duplicate campaigns on separate geographies. That carries its own learning period and its own budget, and both belong in the cost the business is accepting. Google's own Conversion Lift study is the alternative worth asking your rep about before building it yourself; it is usually gated on spend.

## Guardrails

- Do not read the test on the platform's own conversions.
- Do not run it through a promotion or a seasonal peak.
- Do not report a result inside normal variation as a finding.
- Do not present a holdout as free. State the expected cost up front.
- Do not treat an accidental past pause as a clean test without checking what else changed.
