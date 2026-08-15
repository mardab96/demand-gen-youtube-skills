# AGENTS.md: Demand Gen and YouTube diagnostic skills

This repo is a pack of 15 Claude Skills for recurring Google Ads Demand Gen and
YouTube diagnostics, run from exports. Each skill is a self-contained `SKILL.md`
in its own directory.

## What these skills are for

Demand Gen spends across YouTube, Discover, Gmail and Display and reports one
blended result by default, though the channel breakdown and the channel controls
both exist for the operator who goes to find them. (Shorts is YouTube inventory,
not a separate channel, and is named that way throughout the pack.) It counts views more than one way, and it credits conversions to
people who never clicked. Most operator questions about this campaign type are
therefore questions about the report rather than about the campaign, and that is
what the pack answers first.

## How they behave

- **Read-only.** Nothing here logs into an account, changes a bid, pauses a
  campaign or edits a feed. Every skill ends with a decision handed back to the
  operator.
- **Data-first.** Each skill states what it needs, and what it does when that
  input is missing. Several refuse to produce a number the data cannot support
  rather than estimating one.
- **Thresholds are heuristics.** Every number carries a unit and is labelled as a
  starting point to recalibrate per account, never as published Google guidance.
- **One home per threshold.** A number lives in the owning skill's Decision rules.
  Other skills and examples cite that home rather than restating the value, so the
  pack does not drift apart on the next edit. Scripts are the one exception, since
  code cannot cite: a script may restate a threshold as a literal, and every such
  literal carries a comment naming the skill that owns it. A script that invents a
  threshold with no home is a defect, not an exception.

## Where to start

`view-through-credit-check-demand-gen` needs the least setup and most often changes
a decision: the conversion columns and the business's own order count for the same
closed range.

## How they compose

Several skills deliberately hand off rather than duplicate:

- `view-through-credit-check` and `campaign-overlap-check` both end by routing a
  causation question to `incremental-lift-design`, which is the only skill that
  designs a test.
- `weekly-readout` and `bidding-strategy-fit` both defer the question of unfinished
  days to `conversion-lag-read` instead of restating its curve. Both carry that
  pointer in a "When another skill owns the question" block; if you find one that
  only says "check the conversion lag" in prose, the block was lost in an edit.
- `money-split-review` routes an asset-shape finding to `creative-coverage-audit`
  rather than producing a production list itself.

## Helpers

`scripts/` holds two deterministic helpers for the arithmetic that should not be
eyeballed. Each names the skill that owns its thresholds, and each owning skill
names the script.

- `lag_curve.py` — owned by `conversion-lag-read-demand-gen`
- `baseline_spread.py` — owned by `incremental-lift-design-demand-gen`

`examples/` holds two end-to-end runs with real inputs and real output.

## If you are an agent editing this pack

Change a threshold in exactly one place, then grep the bare number across every
`SKILL.md`, script, example and the README, and reconcile every hit. Recompute each
worked example against its own decision table afterwards. A worked example whose
verdict does not follow from its own numbers is the defect this pack has already
shipped once.
