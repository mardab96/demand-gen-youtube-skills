#!/usr/bin/env python3
"""Fill curve and waiting rule for Demand Gen results.

Owned by: conversion-lag-read-demand-gen/SKILL.md
That skill's Decision rules are the single home for the thresholds below. This
script restates them as literals because code cannot cite, and every restatement
carries the citation comment above it. If the two disagree, the skill is right
and this file is stale.

Why a script: the arithmetic is a per-day comparison of two exports of the same
date range pulled days apart, and a model reading two CSVs by eye will quietly
mismatch rows. The waiting rule is the whole output of that skill, so it should
be computed, not estimated.

Usage:
    python3 lag_curve.py early.csv late.csv --as-of YYYY-MM-DD

`--as-of` is the date the EARLY file was pulled, and it is required. Without it
there is no way to know how old each day was when it was first seen, and every
day in the range was a different age. Pooling those into one average overstates
how much is visible on day one, which shortens the waiting rule -- the same
direction as the premature pause this skill exists to prevent. An earlier
version of this script pooled them and printed a caveat underneath the verdict,
which is not a gate.

Both files: a Google Ads daily export of the SAME closed date range, pulled at
different times. Required columns, matched case-insensitively and tolerant of
Google's punctuation, so `View-through conv.` is recognised as written:
    date, conversions
Optional, reported as separate curves when present:
    view-through conv., engaged-view conversions

Credit types fill on different schedules, so the curves are reported
separately. Where they diverge, the waiting rule follows the slower one.

Exit code 0 on success, 2 when the inputs cannot produce a curve.
"""
import csv
import datetime
import re
import statistics
import sys
from collections import OrderedDict

# Google writes these columns several ways depending on the export surface.
# Anything not listed is ignored rather than guessed at.
ALIASES = {
    "date": {"date", "day"},
    # `Conversions` and `All conv.` are DIFFERENT columns and on this campaign type
    # the gap between them is routinely large. An earlier version accepted both into
    # this slot, so a file listing `All conv.` first fed a different column than one
    # listing `Conversions` first -- same week, same data, two different verdicts,
    # and nothing in the output said which column had been used. That is the exact
    # failure money-split-review-demand-gen warns about in its Decision rules.
    "conversions": {"conversions", "conv"},
    "all_conversions": {"allconv", "allconversions", "allconv."},
    "view_through": {
        "viewthroughconv", "viewthroughconversions", "viewthroughconv.",
        "vtconv", "viewthrough",
    },
    "engaged_view": {
        "engagedviewconversions", "engagedviewconv", "engagedview",
        "engagedviewconv.",
    },
}


def canon(name):
    """Strip everything that varies between exports: case, spaces, dots, dashes."""
    return re.sub(r"[^a-z0-9]", "", (name or "").lower())


def map_headers(fieldnames):
    """Return {our_name: actual_column}, plus the columns we did not recognise."""
    found, seen = {}, []
    for col in fieldnames or []:
        c = canon(col)
        seen.append(col)
        for ours, accepted in ALIASES.items():
            if c in {canon(a) for a in accepted} and ours not in found:
                found[ours] = col
    return found, seen


def find_header(path):
    """Google Ads prepends the report name and date range above the real header.

    Return the number of rows to skip. Detected by looking for the first row that
    contains a column this script recognises, rather than by assuming a fixed
    count, because the preamble is two rows on some exports and three on others.
    """
    with open(path, newline="", encoding="utf-8-sig") as fh:
        for i, row in enumerate(csv.reader(fh)):
            if i > 10:
                break
            cells = {canon(c) for c in row}
            if cells & {canon(a) for a in ALIASES["date"]}:
                return i
    return 0


def read(path):
    """Return (rows, header_map, all_headers, dropped_row_count).

    A row whose numbers will not parse is counted, never silently dropped: an
    unreadable file and a file that genuinely says zero must not look the same.
    """
    rows, dropped = OrderedDict(), 0
    skip = find_header(path)
    with open(path, newline="", encoding="utf-8-sig") as fh:
        for _ in range(skip):
            fh.readline()
        reader = csv.DictReader(fh)
        found, headers = map_headers(reader.fieldnames)
        if "date" not in found or "conversions" not in found:
            return None, found, headers, 0
        for r in reader:
            d = (r.get(found["date"]) or "").strip()
            if not d:
                dropped += 1
                continue

            def num(key):
                if key not in found:
                    return None
                raw = (r.get(found[key]) or "").strip().replace(",", "")
                if raw == "":
                    return 0.0
                try:
                    return float(raw)
                except ValueError:
                    return None

            conv = num("conversions")
            if conv is None:
                dropped += 1
                continue
            entry = rows.setdefault(d, {"conversions": 0.0, "all_conversions": None,
                                        "view_through": None, "engaged_view": None,
                                        "_rows": 0})
            entry["conversions"] += conv
            for key in ("all_conversions", "view_through", "engaged_view"):
                v = num(key)
                if v is not None:
                    entry[key] = (entry[key] or 0.0) + v
            entry["_rows"] += 1
    return rows, found, headers, dropped


SLASH = re.compile(r"^\s*(\d{1,2})/(\d{1,2})/(\d{4})\s*$")


def slash_order(samples):
    """Decide whether d/m/Y or m/d/Y, or admit it cannot be decided.

    01/07/2026 is the first of July in one convention and the seventh of January
    in the other, and guessing wrong shifts every age in the curve. Only the file
    itself can settle it, and only when some value exceeds 12 in one position.
    Returns 'dmy', 'mdy', or None for undecidable.
    """
    first_over, second_over = False, False
    for s in samples:
        m = SLASH.match(s or "")
        if not m:
            continue
        a, b = int(m.group(1)), int(m.group(2))
        if a > 12:
            first_over = True
        if b > 12:
            second_over = True
    if first_over and not second_over:
        return "dmy"
    if second_over and not first_over:
        return "mdy"
    return None


def parse_date(s, order=None):
    s = (s or "").strip()
    for fmt in ("%Y-%m-%d", "%Y/%m/%d"):
        try:
            return datetime.datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    if SLASH.match(s):
        if order is None:
            return None
        fmt = "%d/%m/%Y" if order == "dmy" else "%m/%d/%Y"
        try:
            return datetime.datetime.strptime(s, fmt).date()
        except ValueError:
            return None
    return None


def waiting_rule(day_one_share):
    """Thresholds live in conversion-lag-read-demand-gen/SKILL.md, Decision rules.

    Bands are half-open so a value sitting exactly on a boundary lands in one
    row only: 70% is 'judge after 2-3 days', 40% is 'judge after 7 days'.
    """
    if day_one_share >= 0.70:
        return "judge after 2-3 days"
    if day_one_share >= 0.40:
        return "judge after 7 days"
    return "judge after 14 days"


def curve_for(pairs, label):
    """pairs: list of (age_in_days, early, late). Returns {age: share}."""
    by_age = {}
    for age, early, late in pairs:
        if late <= 0:
            continue
        by_age.setdefault(age, []).append(early / late)
    return {age: statistics.median(v) for age, v in sorted(by_age.items())}


def fill_shape(curve):
    """Describe what the curve does across the ages present.

    Measured as the rise from the youngest day to the oldest, not as the first
    adjacent pair that happens to sit close together. Two earlier versions got
    this wrong in the same direction: both announced a plateau on a curve that
    was merely noisy, and one printed "flattens at 1 day" directly above "wait
    14 days". A curve that never rises has not flattened. It has told you the
    filling happens outside the range you pulled, which is a different fact and
    a more useful one.
    """
    ages = sorted(curve)
    if len(ages) < 2:
        return ("single age in this range - one point has no shape", None)
    youngest, oldest = curve[ages[0]], curve[ages[-1]]
    rise = oldest - youngest
    if rise <= 0.10:
        return (f"essentially flat from {ages[0]} to {ages[-1]} days old, around "
                f"{youngest:.0%}. Nothing here shows the figure filling, so the fill "
                f"happens later than {ages[-1]} days. Pull a wider range before "
                "trusting any plateau", None)
    for a in ages:
        if oldest - curve[a] <= 0.05:
            return (f"rises to roughly {oldest:.0%} and levels off by {a} days old", a)
    return (f"still rising at {ages[-1]} days old - this range does not reach the plateau", None)


def main(early_path, late_path, as_of):
    early, e_found, e_headers, e_dropped = read(early_path)
    late, l_found, l_headers, l_dropped = read(late_path)

    for path, rows, found, headers in (
        (early_path, early, e_found, e_headers),
        (late_path, late, l_found, l_headers),
    ):
        if rows is None:
            missing = [n for n in ("date", "conversions") if n not in found]
            print(
                f"STOP: {path} has no column this script recognises as "
                f"{' and '.join(missing)}.\nColumns seen: {', '.join(headers)}\n"
                "This is a header problem, not an empty account. Two common causes: "
                "the export still has the report name and date range above the header "
                "row (delete those rows), or the conversions column was never added "
                "in the column picker.",
                file=sys.stderr,
            )
            return 2

    if e_found.get("conversions") != l_found.get("conversions"):
        print(
            f"STOP: the two files use different columns for conversions "
            f"({e_found.get('conversions')!r} vs {l_found.get('conversions')!r}). "
            "Comparing them would produce a fill curve out of two different "
            "measures. Re-export both with the same columns.",
            file=sys.stderr,
        )
        return 2

    print("Columns feeding this run (check these before trusting anything below):")
    print(f"  conversions curve <- {e_found['conversions']!r}")
    if "all_conversions" in e_found:
        print(f"  NOTE: {e_found['all_conversions']!r} is also in this file and is NOT "
              "being used. It is a different measure, usually larger.")
    for key, label in (("view_through", "view-through"), ("engaged_view", "engaged-view")):
        if key in e_found and key in l_found:
            print(f"  {label} curve <- {e_found[key]!r}")
    print()

    if e_dropped or l_dropped:
        print(f"Note: {e_dropped + l_dropped} row(s) had unreadable numbers and were skipped.\n")

    multi = max([r["_rows"] for r in list(early.values()) + list(late.values())] or [1])
    if multi > 1:
        print(f"Note: some dates appear on up to {multi} rows, so this export carries a "
              "second dimension (campaign, ad group, device or network). Rows have been "
              "SUMMED per date. If you wanted one campaign only, filter the export "
              "instead of relying on this.\n")

    all_keys = list(early) + list(late)
    if any(SLASH.match(k or "") for k in all_keys):
        order = slash_order(all_keys)
        if order is None:
            print(
                "STOP: the dates are written as numbers separated by slashes, and "
                "nothing in these files says whether 07/12/2026 means 12 July or "
                "7 December. Guessing shifts every age in the curve. Re-export with "
                "dates as YYYY-MM-DD.",
                file=sys.stderr,
            )
            return 2
        print(f"Dates read as {'day/month/year' if order == 'dmy' else 'month/day/year'}, "
              "inferred from a value above 12 in the files themselves.\n")
    else:
        order = None

    e_dates = {parse_date(d, order): d for d in early if parse_date(d, order)}
    l_dates = {parse_date(d, order): d for d in late if parse_date(d, order)}
    common = sorted(set(e_dates) & set(l_dates))
    if not common:
        if e_dates and l_dates:
            e_lo, e_hi = min(e_dates), max(e_dates)
            l_lo, l_hi = min(l_dates), max(l_dates)
            print(
                f"STOP: the two files share no dates once parsed.\n"
                f"  {early_path}: {e_lo} to {e_hi}\n"
                f"  {late_path}: {l_lo} to {l_hi}\n"
                "The dates parsed cleanly, so this is a range problem, not a format "
                "problem: re-export the SAME closed range, not the same number of days.",
                file=sys.stderr,
            )
        else:
            print("STOP: no readable dates in one or both files. Check the date column "
                  "format.", file=sys.stderr)
        return 2
    shared = [e_dates[d] for d in common]

    # A credit column present in one file and absent in the other cannot produce a
    # curve. Defaulting the missing side to zero manufactures a slow curve out of a
    # missing column, which is the most confident possible way to be wrong here.
    extras = []
    for key, label in (("view_through", "view-through"), ("engaged_view", "engaged-view")):
        in_e, in_l = key in e_found, key in l_found
        if in_e and in_l:
            extras.append((key, label))
        elif in_e or in_l:
            side = "late" if in_e else "early"
            print(f"Note: the {label} column is missing from the {side} file, "
                  f"so no {label} curve is reported. It is not zero; it is absent.\n")

    rows, weird = [], []
    for dt in common:
        d = e_dates[dt]
        age = (as_of - dt).days
        if age < 1:
            weird.append(d)
            continue
        rows.append((age, d, early[d], late[l_dates[dt]]))
    if weird:
        print(f"Note: {len(weird)} day(s) dropped -- unreadable date, or dated on or "
              f"after the early pull of {as_of}.\n")
    if not rows:
        print("STOP: no day in the overlap is older than the early pull date. "
              "Check --as-of.", file=sys.stderr)
        return 2

    rows.sort(key=lambda r: r[0])
    print(f"Early pull taken {as_of}. Overlapping days: {len(rows)}, "
          f"ages {rows[0][0]} to {rows[-1][0]} days.\n")

    header = f"{'age':>5} {'date':<14}{'early':>10}{'final':>10}{'visible':>10}"
    for _, label in extras:
        header += f"{label + ' vis':>17}"
    print(header)

    over, impossible = 0, []
    main_pairs, extra_pairs = [], {k: [] for k, _ in extras}
    for age, d, e, l in rows:
        if l["conversions"] <= 0:
            continue
        share = e["conversions"] / l["conversions"]
        if share > 1.0:
            over += 1
            impossible.append(age)
        else:
            main_pairs.append((age, e["conversions"], l["conversions"]))
        row = f"{age:>4}d {d:<14}{e['conversions']:>9.1f}{l['conversions']:>10.1f}{share:>9.0%}"
        for key, _ in extras:
            ev, lv = e[key], l[key]
            if ev is None or lv is None or lv <= 0:
                row += f"{'-':>17}"
            else:
                extra_pairs[key].append((age, ev, lv))
                row += f"{ev / lv:>16.0%}"
        print(row)

    if not main_pairs:
        print("\nSTOP: no day had a final value above zero.", file=sys.stderr)
        return 2
    if over:
        print(f"\nWarning: {over} day(s) show MORE in the early pull than in the late one "
              f"(ages: {', '.join(str(a) for a in sorted(impossible))}). A day cannot "
              "un-fill, so the two files do not describe the same thing. Those days are "
              "excluded from the curve rather than averaged into it.")
    if not main_pairs:
        print("\nSTOP: every overlapping day was impossible. Check that both files cover "
              "the same range and the same filters.", file=sys.stderr)
        return 2

    curve = curve_for(main_pairs, "conversions")
    print("\nFill curve (share of the final figure visible, by age at first sight)")
    print(f"{'days after':>12}{'conversions':>14}", end="")
    for _, label in extras:
        print(f"{label:>17}", end="")
    print()
    extra_curves = {k: curve_for(extra_pairs[k], k) for k, _ in extras}
    for age in sorted(curve):
        print(f"{age:>11}d{curve[age]:>14.0%}", end="")
        for key, _ in extras:
            v = extra_curves[key].get(age)
            print(f"{v:>17.0%}" if v is not None else f"{'-':>17}", end="")
        print()

    if len(curve) < 3:
        print(f"\nSTOP: only {len(curve)} usable day(s) in the overlap. A waiting rule "
              "built on one or two days is a guess wearing a number. Pull a longer "
              "closed range.", file=sys.stderr)
        return 2

    youngest = min(curve)
    day_one = curve[youngest]
    shape, plateau = fill_shape(curve)
    print(f"\nShare visible at {youngest} day(s) old: {day_one:.0%}")
    print(f"Shape of the curve: {shape}")
    band = waiting_rule(day_one)
    if plateau is not None:
        print(f"Waiting rule: judge after {plateau} days -- MEASURED. The curve reached "
              f"its plateau inside this range, and a measured plateau beats the band "
              f"read off the day-one share, which is only a proxy for it.")
        if band != f"judge after {plateau} days":
            print(f"(The day-one share of {day_one:.0%} alone would have said: {band}. "
                  "Where the two disagree the measured plateau is the answer, per the "
                  "skill's Decision rules.)")
    else:
        print(f"Waiting rule: {band}")
    if youngest > 1:
        print(f"NOTE: the youngest day in this range was already {youngest} days old at "
              "the first pull, so the true day-one share is LOWER than the figure "
              "above and the real waiting rule is at least as long as the one below.")
    for key, label in extras:
        c = extra_curves[key]
        if not c:
            continue
        d1 = c[min(c)]
        print(f"\n{label.capitalize()} credit only: {d1:.0%} visible at {min(c)} day(s) old")
        print(f"Waiting rule on that curve alone: {waiting_rule(d1)}")
        if waiting_rule(d1) != waiting_rule(day_one):
            print("The two curves disagree. Take the slower rule, per the skill.")

    print("\nThis is a measured curve only if both files cover the same closed range")
    print("and --as-of is genuinely the date the early file was pulled.")
    print("A single export cannot produce this number at all.")
    return 0


if __name__ == "__main__":
    args, as_of_raw, rest = [], None, list(sys.argv[1:])
    while rest:
        token = rest.pop(0)
        if token.startswith("--as-of="):
            as_of_raw = token.split("=", 1)[1]
        elif token == "--as-of":
            as_of_raw = rest.pop(0) if rest else None
        elif token.startswith("--"):
            print(f"STOP: unknown option {token!r}.", file=sys.stderr)
            sys.exit(2)
        else:
            args.append(token)
    if len(args) != 2 or not as_of_raw:
        print(__doc__)
        sys.exit(2)
    parsed = parse_date(as_of_raw)
    if parsed is None:
        print(f"STOP: cannot read --as-of {as_of_raw!r} as a date.", file=sys.stderr)
        sys.exit(2)
    sys.exit(main(args[0], args[1], parsed))
