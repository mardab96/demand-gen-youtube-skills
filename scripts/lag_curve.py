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
Optional, reported as a second curve when present:
    view_through_conversions

Credit types fill on different schedules, so the skill asks for the curves
separately. Where they diverge, the waiting rule follows the slower one.

Exit code 0 on success, 2 when the inputs cannot produce a curve.
"""
import csv
import statistics
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


def waiting_rule(median_share):
    """Thresholds live in conversion-lag-read-demand-gen/SKILL.md, Decision rules."""
    if median_share >= 0.70:
        return "judge after 2-3 days"
    if median_share >= 0.40:
        return "judge after 7 days"
    return "judge after 14 days"


def main(early_path, late_path):
    early, late = read(early_path), read(late_path)
    shared = [d for d in late if d in early]
    if not shared:
        print("STOP: the two files share no dates. Pull the same range twice.", file=sys.stderr)
        return 2

    has_vt = any(v for _, v in list(early.values()) + list(late.values()))

    print(f"Overlapping days: {len(shared)}\n")
    header = f"{'date':<12}{'early':>10}{'final':>10}{'visible':>10}"
    if has_vt:
        header += f"{'vt visible':>12}"
    print(header)

    ratios, vt_ratios = [], []
    for d in shared:
        e, e_vt = early[d]
        l, l_vt = late[d]
        if l <= 0:
            continue
        share = e / l
        ratios.append(share)
        row = f"{d:<12}{e:>10.1f}{l:>10.1f}{share:>9.0%}"
        if has_vt:
            if l_vt > 0:
                vt_share = e_vt / l_vt
                vt_ratios.append(vt_share)
                row += f"{vt_share:>11.0%}"
            else:
                row += f"{'-':>12}"
        print(row)

    if not ratios:
        print("\nSTOP: no day had a final value above zero.", file=sys.stderr)
        return 2

    # statistics.median, never ratios[n // 2]: on an even number of days the latter
    # returns the upper middle value, which OVERSTATES how much was visible on day
    # one and therefore SHORTENS the waiting rule. That error runs in the direction
    # of the premature pause this whole skill exists to prevent.
    median = statistics.median(ratios)
    print(f"\nMedian share of the final value visible at first pull: {median:.0%}")
    print(f"Waiting rule: {waiting_rule(median)}")

    if vt_ratios:
        vt_median = statistics.median(vt_ratios)
        print(f"\nView-through credit only, same measure: {vt_median:.0%}")
        print(f"Waiting rule on that curve alone: {waiting_rule(vt_median)}")
        if waiting_rule(vt_median) != waiting_rule(median):
            print("The two curves disagree. Take the slower rule, per the skill.")

    print("\nThis is a measured curve only if the two pulls are days apart on a closed")
    print("range, and only if 'first pull' is a fixed number of days after each day.")
    print("A single export cannot produce this number at all.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1], sys.argv[2]))
