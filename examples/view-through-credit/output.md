# Did They Buy Or Did They Just Watch — output on the sample export

### Credit verdict

**Not comparable to Search.**

### Split

| Measure | Click-through | Engaged-view | View-through | Total credited |
|---|---:|---:|---:|---:|
| Demand Gen - Prospecting | **36** | 58 | 72 | 166 |
| Share of total credited | **22%** | 35% | 43% | 100% |
| Search - Brand | 63 | 0 | 3 | 66 |
| Search - Generic | 41 | 0 | 2 | 43 |

The arithmetic, which is the point of this example: `Conversions` on the Demand Gen
row is 94 and already contains the 58 engaged-view conversions, so click-through is
94 − 58 = **36**. View-through sits outside that column, so total credited is
94 + 72 = **166**.

**Subtracting view-through from `Conversions` would have given 22 and called it
click-through.** That is wrong in both directions at once: it removes a quantity that
was never in the 94, and it leaves the engaged-view credit inside. An earlier version
of this example did exactly that, which is why the skill now states the two formulas
before anything else.

### Cost per conversion, three ways

| Campaign | Per `Conversions` | Per click-through |
|---|---:|---:|
| Demand Gen - Prospecting | 44.47 | **116.11** |
| Search - Brand | 14.44 | 14.44 |
| Search - Generic | 66.83 | 66.83 |

### What to do next

Click-through is 22% of total credited, below the skill's 40% line, so the campaign
fails comparability outright. Its reported 44.47 sits between the two Search
campaigns and reads like a mid-table performer. On click-through alone it is 116.11,
nearly double the worst Search campaign.

The platform sum across the three campaigns is 198 against 129 orders in the shop for
the same closed fortnight, a ratio of 1.53. That gap is large enough to be accounted
for by the exposure credit on its own.

None of this proves the campaign is worthless. What it establishes is that the
reported figure cannot sit in the same table as a Search figure, which is what the
account was doing. The recommendation is a holdout, not a pause, and that is
`incremental-lift-design-demand-gen`.

### Missing data

The export does not separate new from returning customers, so whether those 36
click-through conversions were people the account would have reached anyway is still
open. `new-customer-share-demand-gen` answers it from shop data.
