# Changelog

## [1.0.0] - 2026-08-15

First release. Fifteen skills for Demand Gen and YouTube campaigns in Google Ads.

The gap this pack fills: Demand Gen spends across four very different channels - YouTube,
Discover, Gmail and Display - and reports one blended result by default, counts engaged
views on its own terms, and credits conversions to people who never clicked. Most operator questions about it are therefore questions about the report rather
than about the campaign, and that is what these skills answer first.

Every threshold is labelled as a heuristic to recalibrate per account, not as a published
Google rule. Four skills refuse to answer under stated conditions rather than return a number the
data cannot support: `incremental-lift-design`, `feed-readiness-check`,
`conversion-lag-read` and `audience-signal-review`. `money-split-review` is not among
them; it falls back rather than refusing, which is why it is listed separately below.

Three changes came out of a deliverability review before release, which asks of every
skill whether it can produce value from data the reader actually has:

- `shorts-spend-review` was cut. It needed the same surface split as `money-split-review`
  and would have failed in the same accounts, so the pack would have shipped two skills
  that go quiet together.
- `money-split-review` was reshaped. It used to stop when the account could not report the
  split. It now falls back to the read the account can support, and says which of the two
  it ran.
- `new-customer-share` was added in the cut skill's place, because whether upper-funnel
  spend finds people who never bought is the question the campaign type is bought to answer
  and nothing in the pack covered it.
