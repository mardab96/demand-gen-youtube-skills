#!/usr/bin/env python3
"""Fill curve and waiting rule for Demand Gen results.

Owned by: conversion-lag-read-demand-gen/SKILL.md
That skill's Decision rules are the single home for the thresholds below. This
script implements them; it does not redefine them. If they disagree, the skill
is right and this file is stale.

Why a script: the arithmetic is a per-day comparison of two exports of the same
date range pulled days apart, and a model reading two CSVs by eye will quietly
mismatch rows. The waiting rule is the whole output of that skill, so it should
be computed, not estimated.

Usage:
    python3 lag_curve.py early.csv late.csv

Both files: a Google Ads daily export of the SAME closed date range, pulled at
different times. Required columns (case-insensitive, extra columns ignored):
    date, conversions
Optional, used when present to split the curve:
    view_through_conversions

Exit code 0 always; this is a reporting tool, not a gate.
"""
import csv
import sys
from collections import OrderedDict


def read(path):
    rows = OrderedDict()
    with open(path, newline="", encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh):
            key = {k.strip().lower().replace(" ", "_"): (v or "").strip() for k, v in r.items()}
            d = key.get("date")
            if not d:
                continue
            try:
                conv = float(key.get("conversions", "0") or 0)
            except ValueError:
                continue
            try:
                vt = float(key.get("view_through_conversions", "0") or 0)
            except ValueError:
                vt = 0.0
            rows[d] = (conv, vt)
    return rows


def main(early_path, late_path):
    early, late = read(early_path), read(late_path)
    shared = [d for d in late if d in early]
    if not shared:
        print("STOP: the two files share no dates. Pull the same range twice.", file=sys.stderr)
        return 2

    print(f"Overlapping days: {len(shared)}\n")
    print(f"{'date':<12}{'early':>10}{'final':>10}{'visible':>10}")
    ratios = []
    for d in shared:
        e, _ = early[d]
        l, _ = late[d]
        if l <= 0:
            continue
        share = e / l
        ratios.append(share)
        print(f"{d:<12}{e:>10.1f}{l:>10.1f}{share:>9.0%}")

    if not ratios:
        print("\nSTOP: no day had a final value above zero.", file=sys.stderr)
        return 2

    ratios.sort()
    median = ratios[len(ratios) // 2]
    print(f"\nMedian share of the final value visible at first pull: {median:.0%}")

    # Thresholds live in conversion-lag-read-demand-gen/SKILL.md, Decision rules.
    if median >= 0.70:
        rule = "judge after 2-3 days"
    elif median >= 0.40:
        rule = "judge after 7 days"
    else:
        rule = "judge after 14 days"
    print(f"Waiting rule: {rule}")
    print("\nThis is a measured curve only if the two pulls are days apart on a closed")
    print("range. If they are not, label the result as an estimate, per the skill.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1], sys.argv[2]))
