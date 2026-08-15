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
    "conversions": {"conversions", "conv", "allconv", "allconversions"},
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


def read(path):
    """Return (rows, header_map, all_headers, dropped_row_count).

    A row whose numbers will not parse is counted, never silently dropped: an
    unreadable file and a file that genuinely says zero must not look the same.
    """
    rows, dropped = OrderedDict(), 0
    with open(path, newline="", encoding="utf-8-sig") as fh:
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
            rows[d] = {
                "conversions": conv,
                "view_through": num("view_through"),
                "engaged_view": num("engaged_view"),
            }
    return rows, found, headers, dropped


def parse_date(s):
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d"):
        try:
            return datetime.datetime.strptime(s.strip(), fmt).date()
        except ValueError:
            continue
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


def flattening_day(curve):
    """First age at which the curve is within 5 points of the next reading."""
    ages = sorted(curve)
    for a, b in zip(ages, ages[1:]):
        if abs(curve[b] - curve[a]) <= 0.05:
            return a
    return None


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
                "This is a header problem, not an empty account. Re-export with "
                "the date and conversions columns present.",
                file=sys.stderr,
            )
            return 2

    if e_dropped or l_dropped:
        print(f"Note: {e_dropped + l_dropped} row(s) had unreadable numbers and were skipped.\n")

    shared = [d for d in late if d in early]
    if not shared:
        print("STOP: the two files share no dates. Pull the same range twice.", file=sys.stderr)
        return 2

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
    for d in shared:
        dt = parse_date(d)
        if dt is None:
            weird.append(d)
            continue
        age = (as_of - dt).days
        if age < 1:
            weird.append(d)
            continue
        rows.append((age, d, early[d], late[d]))
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

    over = 0
    main_pairs, extra_pairs = [], {k: [] for k, _ in extras}
    for age, d, e, l in rows:
        if l["conversions"] <= 0:
            continue
        share = e["conversions"] / l["conversions"]
        if share > 1.0:
            over += 1
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
        print(f"\nWarning: {over} day(s) show more in the early pull than in the late one. "
              "A day cannot un-fill; the ranges or the files are mismatched.")

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

    youngest = min(curve)
    day_one = curve[youngest]
    flat = flattening_day(curve)
    print(f"\nShare visible at {youngest} day(s) old: {day_one:.0%}")
    flat_txt = f"{flat} day{'s' if flat != 1 else ''} old" if flat else "not within this range"
    print(f"Curve flattens at: {flat_txt}")
    if youngest > 1:
        print(f"NOTE: the youngest day in this range was already {youngest} days old at "
              "the first pull, so the true day-one share is LOWER than the figure "
              "above and the real waiting rule is at least as long as the one below.")
    print(f"Waiting rule: {waiting_rule(day_one)}")

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
