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
    vals, weeks = [], []
    with open(path, newline="", encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh):
            key = {k.strip().lower(): (v or "").strip() for k, v in r.items()}
            try:
                vals.append(float(key["value"]))
                weeks.append(key.get("week", ""))
            except (KeyError, ValueError):
                continue

    if len(vals) < 4:
        print(f"STOP: only {len(vals)} usable weeks. Need at least 4 to say anything.", file=sys.stderr)
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

    # Thresholds live in incremental-lift-design-demand-gen/SKILL.md, Decision rules.
    # Bramkujemy na OBU: mediana odchylen mowi o typowym tygodniu, maksimum lapie
    # serie z jednym tygodniem skrajnym. Sama mediana przepuszczala serie, w ktorej
    # jeden tydzien odstaje o 300%, a to jest dokladnie ten szum, ktory zjada wynik
    # holdoutu. Skill nazywa to "weekly outcome variation"; tutaj to znaczy: typowy
    # tydzien pod progiem I zaden tydzien nie odstaje ponad dwukrotnie od niego.
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
