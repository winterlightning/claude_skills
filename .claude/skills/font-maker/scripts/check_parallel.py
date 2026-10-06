#!/usr/bin/env python3
"""Minimum-gap rule between parallel strokes, measured on centrelines.

Two stroke points that run side by side within --angle degrees of parallel must be at least
stroke + min_gap apart centre to centre. Points closer than one stroke width are a join (the inks
merge), not a gap, and are skipped; so are points on the same short bend (arc distance < 3).
Diagonals meeting at a sharp joint are not parallel and never count.

    python3 check_parallel.py --stroke 4 --min-gap 4 Letters/official
"""
import argparse, math, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import glyphs as G

def sample(paths, step=0.1):
    pts = []
    for pi, P in enumerate(paths):
        L = P.length(); n = max(2, int(L / step)); closed = abs(P.start - P.end) < 1e-6
        for k in range(n + 1):
            s = L * k / n
            try:
                t = P.ilength(s, s_tol=1e-6); d = P.unit_tangent(t)
            except Exception:
                continue
            pts.append((pi, s, P.point(t), d, L, closed))
    return pts

def check(glyph, stroke, min_gap, angle=10.0, tol=0.15):
    """Return None if the glyph passes, else (white gap, point a, point b) for the tightest pair."""
    minc = stroke + min_gap; pts = sample(glyph['paths'])
    if not pts:
        return None
    P = np.array([[q[2].real, q[2].imag] for q in pts]); D = np.array([[q[3].real, q[3].imag] for q in pts])
    ca = math.cos(math.radians(angle)); worst = None
    for i in range(len(pts)):
        v = P - P[i]; dist = np.hypot(v[:, 0], v[:, 1])
        for j in np.where((dist < minc - tol) & (dist >= stroke))[0]:
            if j <= i or abs(D[i] @ D[j]) < ca:
                continue
            if abs((v[j] / dist[j]) @ D[i]) > 0.5:      # collinear, not side by side
                continue
            pi, si, _, _, L, closed = pts[i]; pj, sj = pts[j][0], pts[j][1]
            if pi == pj:
                a = abs(si - sj); a = min(a, L - a) if closed else a
                if a < 3:
                    continue
            if worst is None or dist[j] < worst[0]:
                worst = (dist[j], P[i].round(2).tolist(), P[j].round(2).tolist())
    return None if worst is None else (worst[0] - stroke, worst[1], worst[2])

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('inputs', nargs='+', help='glyph SVGs or folders')
    ap.add_argument('--stroke', type=float, help='stroke width (default: read from each SVG)')
    ap.add_argument('--min-gap', type=float, default=4.0, help='minimum white between parallel strokes')
    ap.add_argument('--angle', type=float, default=10.0, help='degrees within which strokes count as parallel')
    a = ap.parse_args(); fails = 0
    for f in G.collect(a.inputs):
        g = G.load(f); s = a.stroke or g['stroke']; r = check(g, s, a.min_gap, a.angle)
        if r is None:
            print(f"{os.path.relpath(f):40} ok")
        else:
            fails += 1; print(f"{os.path.relpath(f):40} FAIL white {r[0]:.2f} between {r[1]} and {r[2]}")
    print(f"\n{fails} glyph(s) below {a.min_gap} units of white between parallel strokes")

if __name__ == '__main__':
    main()
