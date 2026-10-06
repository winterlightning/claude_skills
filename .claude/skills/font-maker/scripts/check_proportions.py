#!/usr/bin/env python3
"""Compare a glyph set's widths with real-font proportions (from measure_reference.py).

Widths are ink widths relative to H (capitals and digits) or n (lowercase), the same way the
reference is measured. Prints each glyph next to the reference range and checks ordering rules
every reference font agrees on. A stroke-gap rule can make some ratios impossible (e.g. H can't
be narrower than two stems plus the minimum gap); report those as forced, don't hide them.

    python3 check_proportions.py --reference reference.json Letters/official
"""
import argparse, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import glyphs as G

E = 0.05  # widths within this are equal (float noise in curve bounds)
RULES = [  # (description, function of width map w) -- skipped when a needed glyph is missing
    ('I is the narrowest capital', lambda w: all(w['I'] <= w[c] + E for c in w if c.isupper())),
    ('W is the widest capital', lambda w: all(w['W'] + E >= w[c] for c in w if c.isupper())),
    ('M wider than N', lambda w: w['M'] > w['N']),
    ('O at least as wide as H', lambda w: w['O'] + E >= w['H']),
    ('E narrower than H', lambda w: w['E'] < w['H']),
    ('F and L narrower than E', lambda w: w['F'] < w['E'] and w['L'] < w['E']),
    ('0 narrower than O', lambda w: w['0'] < w['O']),
    ('1 is the narrowest digit', lambda w: all(w['1'] < w[d] for d in '023456789')),
    ('digits no wider than H', lambda w: all(w[d] <= w['H'] + 0.05 for d in '023456789')),
    ('i is the narrowest lowercase', lambda w: all(w['i'] <= w[c] + E for c in w if c.islower())),
    ('m and w are the widest lowercase', lambda w: min(w['m'], w['w']) + E >= max(w[c] for c in w if c.islower() and c not in 'mw')),
    ('o at least as wide as n', lambda w: w['o'] + E >= w['n']),
    ('f, j, r, t narrower than n', lambda w: all(w[c] < w['n'] for c in 'fjrt')),
]

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('inputs', nargs='+'); ap.add_argument('--reference', required=True)
    ap.add_argument('--tolerance', type=float, default=0.12, help='flag ratios this far outside the reference range')
    a = ap.parse_args()
    ref = json.load(open(a.reference)); files = G.collect(a.inputs)
    w = {}
    for f in files:
        x0, _, x1, _ = G.ink_bounds(G.load(f)); w[G.char_of(f)] = x1 - x0
    print(f"{'glyph':6}{'ink':>7}{'ratio':>7}   reference range   centre x")
    for f in files:
        c = G.char_of(f); base = 'n' if c.islower() else 'H'
        if base not in w:
            continue
        r = w[c] / w[base]; rr = [d['widths'].get(c) for d in ref if c in d['widths']]
        lo, hi = min(rr), max(rr); flag = '' if lo - a.tolerance <= r <= hi + a.tolerance else '  <- outside'
        x0, _, x1, _ = G.ink_bounds(G.load(f)); cx = (x0 + x1) / 2
        print(f"{c:6}{w[c]:7.2f}{r:7.2f}   {lo:.2f} to {hi:.2f}      {cx:5.2f}{flag}")
    print()
    for name, fn in RULES:
        try:
            print(('ok   ' if fn(w) else 'FAIL ') + name)
        except KeyError:
            pass

if __name__ == '__main__':
    main()
