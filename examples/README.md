# Worked examples

Two end-to-end runs with real inputs and the real output, so you can see what these
skills hand back before you install anything.

- **`conversion-lag/`** — two pulls of the same week, five days apart, run through
  `scripts/lag_curve.py`. Produces the waiting rule for the account.
- **`view-through-credit/`** — a three-campaign export plus what the shop recorded,
  showing a campaign that reads mid-table and is the most expensive in the account
  once exposure credit is taken out.

Both are small enough to check by hand, on purpose. If a skill's output cannot be
recomputed from its own inputs, that is a defect in the skill, not a feature.
