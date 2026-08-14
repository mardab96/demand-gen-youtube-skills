# Worked example: When The Numbers Stop Moving

Two pulls of the same closed week, taken five days apart from the same Demand Gen
campaign. `pull_early.csv` is what the account showed on the Monday after the week
closed. `pull_late.csv` is the same seven days re-pulled the following Saturday.

Run it:

```bash
python3 ../../scripts/lag_curve.py pull_early.csv pull_late.csv
```

`output.txt` is the real output of that command on these files, not a transcription.

## What the skill does with this

The median share of the eventual figure visible at the first pull is **39%**, and
the daily spread is tight, 38% to 45%. That sits below the skill's 40% line, so the
waiting rule is **14 days**, not seven.

The operational consequence is the point of the whole skill. A campaign judged on
that Monday was judged on 39% of its conversions, so its cost per result read
roughly two and a half times higher than it settled at. Every pause made that
morning was made on a number that was still arriving.

The tight spread matters as much as the median. A curve that lands between 38% and
45% every day is a property of this account, so the rule is reusable. A curve that
swung between 20% and 80% would not be, and the skill says to report it as unstable
rather than to average it into a rule.

The script now prints a second curve for view-through credit, and on this data it
lands at 37% against 39% for the total, so both give the same fourteen-day rule. That
is not always true. Where the two disagree, the skill takes the slower one, and the
script says so in its output rather than leaving the reader to notice.

⚠️ **One honest limitation of this sample, which applies to your own data too.** The
early pull is described as "the Monday after the week closed", so for the first day
of the week it is a seven-day-old reading and for the last day it is a one-day-old
reading. A clean curve needs the first pull taken a *fixed* number of days after each
day. The tight 38-45% spread across a sevenfold difference in age is the tell that
this sample is illustrative rather than rigorous. Anchor your own pulls to a fixed
offset.
