#!/usr/bin/env python3
"""Measure real fonts: glyph widths, vertical guide lines, crossbars and dots.

Writes a JSON the other tools read. Everything is a ratio, so it applies to any grid:
  widths      ink width / ink width of H (capitals, digits) or n (lowercase)
  lines       ink heights as a fraction of cap height: x-height, ascender, descender,
              t and f crossbar top and bottom, i stem top, i dot bottom and top, t top
  stroke      stem width / cap height (to compare weight)

    python3 measure_reference.py --out reference.json                 # default macOS sans fonts
    python3 measure_reference.py --font "/path/A.ttf" --font "/path/B.otf:Bold" --out ref.json

A font entry is path or path:face-name (for .ttc collections). Prefer fonts close to the target
style (weight, rounded or not, condensed or not); report which ones you used.
"""
import argparse, json, os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

S = '/System/Library/Fonts/Supplemental/'
DEFAULT = [S + 'Arial Rounded Bold.ttf', '/System/Library/Fonts/Helvetica.ttc:Helvetica Bold',
           S + 'DIN Alternate Bold.ttf', S + 'Arial Bold.ttf']
UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'; LOWER = 'abcdefghijklmnopqrstuvwxyz'; DIGITS = '0123456789'

def open_font(spec, size=600):
    path, _, face = spec.partition(':')
    if path.endswith('.ttc') and face:
        for i in range(32):
            try:
                f = ImageFont.truetype(path, size, index=i)
            except OSError:
                break
            if ' '.join(f.getname()) == face or face in ' '.join(f.getname()):
                return f
    return ImageFont.truetype(path, size)

def ink(font, ch, size=600):
    im = Image.new('L', (size * 2, size * 2), 0)
    ImageDraw.Draw(im).text((size // 2, size // 4), ch, font=font, fill=255)
    return np.array(im) > 128

def measure(spec):
    f = open_font(spec)
    def box(ch):
        a = ink(f, ch); ys, xs = np.where(a); return a, xs.min(), xs.max(), ys.min(), ys.max()
    _, hx0, hx1, ht, hb = box('H'); cap = hb - ht; base = hb
    rel = lambda y: round(float((base - y) / cap), 3)
    H = hx1 - hx0; n = box('n'); nw = n[2] - n[1]
    widths = {c: round(float((box(c)[2] - box(c)[1]) / H), 3) for c in UPPER + DIGITS}
    widths.update({c: round(float((box(c)[2] - box(c)[1]) / nw), 3) for c in LOWER})
    def bar(ch):
        a, x0, x1, y0, y1 = box(ch); w = a.sum(1); top = y0
        # crossbar: the widest rows in the top part of the glyph (above mid height)
        mid = (y0 + y1) // 2; wmax = w[y0:mid].max()
        rows = [y for y in range(y0, mid) if w[y] >= 0.85 * wmax]
        return rel(min(rows)), rel(max(rows))
    a, _, _, it, ib = box('i'); filled = a.any(1); gap = [y for y in range(it, ib) if not filled[y]]
    I = box('I'); stroke = (I[2] - I[1]) / cap
    lines = {'x_height': rel(box('x')[3]), 'o_top': rel(box('o')[3]), 'o_bottom': rel(box('o')[4]),
             'ascender': rel(box('d')[3]), 'descender': rel(box('p')[4]), 'g_bottom': rel(box('g')[4]),
             't_top': rel(box('t')[3]), 'f_top': rel(box('f')[3]),
             't_bar': bar('t'), 'f_bar': bar('f'),
             'i_stem_top': rel(max(gap) + 1) if gap else None,
             'i_dot_bottom': rel(min(gap) - 1) if gap else None, 'i_dot_top': rel(it)}
    return {'font': spec, 'name': ' '.join(f.getname()), 'stroke_over_cap': round(float(stroke), 3),
            'widths': widths, 'lines': lines}

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--font', action='append', help='font path or path:face (repeatable)')
    ap.add_argument('--out', default='reference.json')
    a = ap.parse_args()
    specs = a.font or [s for s in DEFAULT if os.path.exists(s.partition(':')[0])]
    data = [measure(s) for s in specs]
    json.dump(data, open(a.out, 'w'), indent=1)
    keys = ['x_height', 'ascender', 'descender', 't_top', 't_bar', 'f_bar', 'i_stem_top', 'i_dot_bottom', 'i_dot_top']
    for d in data:
        print(d['name'], '| stroke/cap', d['stroke_over_cap'])
        print('   ' + '  '.join(f"{k} {d['lines'][k]}" for k in keys))
    print(f"\nwrote {a.out}")

if __name__ == '__main__':
    main()
