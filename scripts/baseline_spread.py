#!/usr/bin/env python3
"""Is this account quiet enough to read a holdout?

Owned by: incremental-lift-design-demand-gen/SKILL.md
That skill's Decision rules are the single home for the thresholds below. This
script implements them; it does not redefine them.

Why a script: the readiness verdict turns on the spread of weekly business
outcomes around their own median, and eyeballing a column of weekly revenue is
exactly how a decorative holdout gets approved. A test that cannot clear normal
weekly noise still produces a result, and someone always quotes it.

Usage:
    python3 baseline_spread.py weekly.csv

Required columns (case-insensitive): week, value
`value` is the business outcome the test will read: revenue, orders or leads.
Never platform-reported conversions.

Exit code 0 when the baseline supports a readable test, 1 when it does not.
"""
import csv
import statistics
import sys


def main(path):
    vals, unreadable = [], 0
    with open(path, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        headers = reader.fieldnames or []
        lowered = {h.strip().lower(): h for h in headers}

        # A missing column and an empty account are different failures and must not
        # produce the same message. An earlier version reported a misnamed header as
        # "only 0 usable weeks", which sent the operator off to collect more history
        # they already had.
        if "value" not in lowered:
            print(
                "STOP: no column named 'value' in this file.\n"
                f"Columns seen: {', '.join(headers) if headers else '(none)'}\n"
                "'value' is the business outcome the test will read: revenue, orders or "
                "leads. Rename the column and run again. This is a header problem, not "
                "a short history.",
                file=sys.stderr,
            )
            return 1

        for r in reader:
            raw = (r.get(lowered["value"]) or "").strip().replace(",", "")
            try:
                vals.append(float(raw))
            except ValueError:
                unreadable += 1

    if unreadable:
        print(f"Note: {unreadable} row(s) had an unreadable value and were skipped.\n")

    if len(vals) < 4:
        print(f"STOP: the 'value' column parsed on only {len(vals)} week(s). "
              "Need at least 4 to say anything.", file=sys.stderr)
        return 1

    med = statistics.median(vals)
    if med == 0:
        print("STOP: median is zero, spread is undefined.", file=sys.stderr)
        return 1

    deviations = [abs(v - med) / med for v in vals]
    spread = max(deviations)
    typical = statistics.median(deviations)

    print(f"Weeks of history .......... {len(vals)}")
    print(f"Median weekly value ....... {med:,.0f}")
    print(f"Typical deviation ......... {typical:.0%}")
    print(f"Worst week deviation ...... {spread:.0%}")

    # Thresholds live in incremental-lift-design-demand-gen/SKILL.md, Decision rules,
    # which states both of them. This file implements them and defines neither.
    # Both are gated because they catch different failures: the median deviation
    # describes a typical week, the maximum catches a series that is calm apart
    # from one extreme week. The median alone passed a history in which a single
    # week sat 300% off, and that is precisely the noise that eats a holdout result.
    if typical <= 0.25 and spread <= 0.60 and len(vals) >= 8:
        verdict, code = "READABLE - a holdout on this baseline can clear normal noise", 0
    elif typical <= 0.50 and spread <= 1.00:
        verdict, code = "NEEDS A LONGER WINDOW - run more weeks, or expect an unreadable result", 1
    else:
        verdict, code = "DO NOT RUN YET - the week-to-week swing is larger than any effect you could detect", 1

    print(f"\n{verdict}")
    print("\nA promotion or a seasonal peak inside the window invalidates this")
    print("regardless of the numbers above. Check the calendar before trusting it.")
    return code


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
