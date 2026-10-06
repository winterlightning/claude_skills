#!/usr/bin/env python3
"""Soft (rounded) vertices: replace sharp corners with circles the strokes run tangent to.

A round join only rounds the outside of a corner; the inside stays a point. Building the corner
as a circle of radius r on the centreline rounds the inside too. Place each circle so it touches
the guide line (e.g. a V tip circle centred at baseline - r), so the letter keeps its height.

    from rounded import rounded
    rounded([((4, 2), 0), ((9, 17 - 1.5), 1.5), ((14, 2), 0)])   # soft V on a 19 grid

Nodes are (centre, radius); radius 0 is a sharp point (use it for stroke ends). Large radii in a
narrow letter make tangents impossible (circles overlap) or turn diagonals vertical: keep r small
relative to the space between nodes and look at the result.

    python3 rounded.py "4,2,0 9,15.5,1.5 14,2,0"     # prints the path d
"""
import math, sys
import numpy as np

def _tangent(c1, r1, s1, c2, r2, s2):
    c1 = np.array(c1, float); c2 = np.array(c2, float); D = c2 - c1; L = np.linalg.norm(D); a = s2 * r2 - s1 * r1
    if L <= abs(a):
        raise ValueError('circles overlap: no tangent; use smaller radii')
    for sgn in (1, -1):
        ang = math.atan2(D[1], D[0]) + sgn * math.acos(max(-1, min(1, -a / L)))
        m = np.array([math.cos(ang), math.sin(ang)]); d = np.array([-m[1], m[0]])
        p1 = c1 + s1 * r1 * m; p2 = c2 + s2 * r2 * m; q = p2 - p1
        if q @ d > 0 and abs(q[0] * d[1] - q[1] * d[0]) < 1e-6 * max(1, L):
            return p1, p2
    raise ValueError('no tangent between these nodes')

def rounded(nodes):
    n = len(nodes); sides = [0] * n
    for i in range(1, n - 1):
        A, B, C = (np.array(nodes[k][0], float) for k in (i - 1, i, i + 1))
        sides[i] = 1 if (B - A)[0] * (C - B)[1] - (B - A)[1] * (C - B)[0] > 0 else -1
    segs = [_tangent(nodes[i][0], nodes[i][1], sides[i], nodes[i + 1][0], nodes[i + 1][1], sides[i + 1]) for i in range(n - 1)]
    f = lambda v: f'{v:.4g}'
    d = f"M{f(segs[0][0][0])} {f(segs[0][0][1])}"
    for i, (p1, p2) in enumerate(segs):
        r = nodes[i][1]
        if i > 0 and r > 0:
            d += f"A{r:g} {r:g} 0 0 {1 if sides[i] > 0 else 0} {f(p1[0])} {f(p1[1])}"
        d += f"L{f(p2[0])} {f(p2[1])}"
    return d

if __name__ == '__main__':
    nodes = [((float(x), float(y)), float(r)) for x, y, r in (t.split(',') for t in sys.argv[1].split())]
    print(rounded(nodes))
