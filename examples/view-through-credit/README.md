# Worked example: Did They Buy Or Did They Just Watch

`campaign_export.csv` is a three-campaign Google Ads export for one closed fortnight,
with all three conversion columns present. `business_record.txt` is what the shop
recorded over the same dates. `output.md` is what the skill produces from the two.

This is the example most likely to change someone's mind about a Demand Gen campaign,
which is why it is checked in. The campaign looks mid-table on the reported number and
is the most expensive thing in the account once the credit is separated properly.

The arithmetic is checkable by hand, and the direction matters more than the numbers:

```
click-through  = Conversions − Engaged-view      = 94 − 58 = 36
total credited = Conversions + View-through      = 94 + 72 = 166
cost per click-through conversion                = 4180 / 36 = 116.11
```

If your own export has no engaged-view column, you cannot compute click-through at
all. Report `Conversions` as click-through plus engaged-view, unresolved. That is a
worse-looking output and a truer one.
