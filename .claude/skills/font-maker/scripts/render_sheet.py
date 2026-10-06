#!/usr/bin/env python3
"""Render glyphs for visual review: a contact sheet at several pixel sizes, optional guide lines,
and words set with a fixed gap between letters (centreline gap = stroke + min gap).

    python3 render_sheet.py Letters/official --out sheet.png --px 48 160
    python3 render_sheet.py Letters/official --words "Hamburgefonstiv" "pdf jpg 5g" \
        --lines 2 7 17 22.5 --out words.png

Look at every sheet at the real target size before claiming a glyph reads. Requires rsvg-convert.
"""
import argparse, os, subprocess, sys, tempfile
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import glyphs as G

def raster(svg_text, w_px, h_px):
    with tempfile.NamedTemporaryFile('w', suffix='.svg', delete=False) as t:
        t.write(svg_text); name = t.name
    out = name + '.png'
    subprocess.run(['rsvg-convert', '-w', str(w_px), '-h', str(h_px), '-b', 'white', '-o', out, name], check=True)
    im = Image.open(out).convert('RGB'); os.remove(name); os.remove(out); return im

def inner(path):
    s = open(path).read(); return s[s.index('>') + 1:s.rindex('</svg>')]

def word_svg(word, lib, gap, lines, stroke):
    x = 0.0; parts = []; H = max(G.load(p)['canvas'][1] for p in lib.values())
    for ch in word:
        if ch == ' ':
            x += gap * 2; continue
        if ch not in lib:
            print(f'skipping {ch!r}: no glyph in the inputs', file=sys.stderr); continue
        g = G.load(lib[ch]); x0, _, x1, _ = G.bounds(g)
        parts.append(f'<g transform="translate({x - x0 + stroke / 2} 0)">{inner(lib[ch])}</g>'); x += (x1 - x0) + gap
    W = x - gap + stroke
    guide = ''.join(f'<line x1="0" x2="{W}" y1="{y}" y2="{y}" stroke="#e8590c" stroke-width="0.3"/>' for y in lines)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">{guide}{"".join(parts)}</svg>', W, H

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('inputs', nargs='+'); ap.add_argument('--out', default='sheet.png')
    ap.add_argument('--px', type=int, nargs='+', default=[48, 160], help='height in pixels of the tallest glyph canvas')
    ap.add_argument('--words', nargs='*', default=[]); ap.add_argument('--lines', type=float, nargs='*', default=[])
    ap.add_argument('--min-gap', type=float, default=4.0); ap.add_argument('--cols', type=int, default=13)
    a = ap.parse_args()
    files = G.collect(a.inputs); lib = {G.char_of(f): f for f in files}
    stroke = G.load(files[0])['stroke']; rows = []
    hmax = max(G.load(f)['canvas'][1] for f in files)   # one scale for every glyph: px is the tallest canvas
    for px in a.px:
        tiles = []; k = px / hmax
        for f in files:
            g = G.load(f); cw, ch = g['canvas']
            svg = open(f).read()
            if a.lines:
                guide = ''.join(f'<line x1="0" x2="{cw}" y1="{y}" y2="{y}" stroke="#e8590c" stroke-width="0.3"/>' for y in a.lines)
                svg = svg.replace('>', '>' + guide, 1)
            tiles.append(raster(svg, max(1, round(k * cw)), max(1, round(k * ch))))
        cols = a.cols; tw = max(t.width for t in tiles); n = (len(tiles) + cols - 1) // cols
        sheet = Image.new('RGB', (cols * (tw + 6) + 6, n * (px + 6) + 6), '#ccc')
        for i, t in enumerate(tiles):
            sheet.paste(t, (6 + (i % cols) * (tw + 6), 6 + (i // cols) * (px + 6)))
        rows.append(sheet)
    for word in a.words:
        svg, W, H = word_svg(word, lib, stroke + a.min_gap, a.lines, stroke)
        px = max(a.px); rows.append(raster(svg, round(px * W / H), px))
    out = Image.new('RGB', (max(r.width for r in rows), sum(r.height + 10 for r in rows)), 'white'); y = 0
    for r in rows:
        out.paste(r, (0, y)); y += r.height + 10
    out.save(a.out); print('wrote', a.out)

if __name__ == '__main__':
    main()
