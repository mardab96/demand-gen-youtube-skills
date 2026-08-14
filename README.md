# 15 Claude Skills for Demand Gen and YouTube

A pack of 15 production-ready Claude Skills for the Google Ads campaign type that spends across YouTube, Shorts, Discover and Gmail and reports it as one number. They cover where the money actually went, whether the views were attention, how much of the conversion count is exposure rather than action, creative coverage and winners, audience signal, overlap with your other campaigns, feed readiness, frequency, bid strategy fit, conversion lag, incrementality, landing page fit, and the weekly readout.

Each skill is a self-contained `SKILL.md` with explicit triggers, required inputs, an analysis workflow, decision rules with unit-carrying thresholds, a worked example, an output format and guardrails. **Every threshold is labelled as a heuristic to recalibrate per account, never as a published Google rule**, because most of the numbers people quote for this campaign type are working figures rather than documentation.

Three of them refuse to answer under stated conditions rather than return something the data cannot carry. The lift skill will tell you your account cannot produce a readable holdout instead of designing a decorative one. The feed skill fails a whole feed on a single wrong price, because that defect damages trust with the customer rather than merely reducing reach. The money-split skill stops when the account cannot report the split at all, instead of inferring it from impression volume.

These skills read exports and hand back a decision. They do not need write access, they do not change campaigns, and they do not touch budgets.

## What's inside

| # | Skill | Folder | What it answers |
|---|-------|--------|-----------------|
| 1 | Where Your Money Actually Went | `money-split-review-demand-gen` | Which surface took the budget, and whether it earned it |
| 2 | Are These Views Real Attention | `engaged-view-quality-demand-gen` | Which view counter belongs in the report and which is decoration |
| 3 | Did They Buy Or Did They Just Watch | `view-through-credit-check-demand-gen` | How much of the conversion count is exposure credit |
| 4 | What Your Creative Is Missing | `creative-coverage-audit-demand-gen` | Which missing asset ratio is quietly narrowing delivery |
| 5 | Which Video Actually Did The Work | `winning-video-finder-demand-gen` | Which asset carried the campaign, and what to brief next |
| 6 | Is Shorts Eating Your Budget | `shorts-spend-review-demand-gen` | Whether cheap impressions are buying anything |
| 7 | Who Google Thinks You Want | `audience-signal-review-demand-gen` | Whether your audience signal is steering or decorative |
| 8 | Are You Paying Twice For The Same Person | `campaign-overlap-check-demand-gen` | Where campaign types are converting the same people |
| 9 | Is Your Feed Ready For Demand Gen | `feed-readiness-check-demand-gen` | Whether the catalogue can actually serve |
| 10 | Why Your Frequency Is Climbing | `frequency-creep-review-demand-gen` | Saturation, auction pressure or fatigue |
| 11 | Should This Bid To Clicks Or Conversions | `bidding-strategy-fit-demand-gen` | Whether the bid strategy matches the volume you have |
| 12 | When The Numbers Stop Moving | `conversion-lag-read-demand-gen` | How many days before a result is safe to judge |
| 13 | Would These Sales Happen Anyway | `incremental-lift-design-demand-gen` | Whether the spend causes outcomes or reports them |
| 14 | Where The Click Lands | `landing-match-review-demand-gen` | Whether the page fits traffic that never searched for you |
| 15 | The Weekly Demand Gen Readout | `weekly-readout-demand-gen` | Facts, hypotheses and decisions, separated |

## How to install

### Option A - Claude Code

1. Clone or download this repository.
2. Copy the skill folders into your project's `.claude/skills/` directory, or into the user-level directory at `~/.claude/skills/`.
3. Start a new Claude Code session in that project. Skills activate automatically when their description matches the conversation.

```bash
git clone https://github.com/mardab96/demand-gen-youtube-skills.git
mkdir -p ~/.claude/skills
cp -r demand-gen-youtube-skills/*-demand-gen ~/.claude/skills/
```

### Option B - Other Claude environments

The skills are plain Markdown with YAML frontmatter. Paste the relevant `SKILL.md` into context when you want to use it.

## How to use

Bring exports, not screenshots. Most skills open by asking what the account can actually report, because this campaign type exposes less surface detail than Video campaigns do, and a skill that guesses at the split is worse than one that says it cannot see it.

Start with `money-split-review-demand-gen` if you do not know where to begin. It is the one that most often changes what people think their campaign is doing.

## What these are not

They are not an autopilot. Nothing here logs into your account, changes a bid, pauses a campaign or edits a feed. Every skill ends with a decision handed back to you, and several of them end by saying the data cannot support one yet.

## Licence

MIT. Use them, change them, ship them in your own stack.
