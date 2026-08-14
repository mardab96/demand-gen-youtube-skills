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

The view-through column fills on roughly the same curve here. That is not always
true, and where it is not, the skill reports the two curves separately so a campaign
is not judged on a blend of a fast signal and a slow one.
