# Worked examples

Two end-to-end runs with real inputs, so you can see what these skills hand back
before you install anything.

They are not the same kind of artefact, and the difference matters if you are
checking our work. `conversion-lag/output.txt` is program output: run the command
in that folder and you get that file back, byte for byte. `view-through-credit/`
is a worked read, written out the way the skill's output format asks for it,
because that skill has no script - its whole job is getting one subtraction the
right way round.

- **`conversion-lag/`** — two pulls of the same week, five days apart, run through
  `scripts/lag_curve.py`. Produces the waiting rule for the account.
- **`view-through-credit/`** — a three-campaign export plus what the shop recorded,
  showing a campaign that reads mid-table and is the most expensive in the account
  once exposure credit is taken out.

Both are small enough to check by hand, on purpose. If a skill's output cannot be
recomputed from its own inputs, that is a defect in the skill, not a feature.
