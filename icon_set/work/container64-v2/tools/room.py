"""Largest axis-aligned square a symbol can use inside a container.

The container's centerline must stay >= 4 from the square (MIC 2 + half stroke
2), and the square's centre must be inside the drawing's closed interior when
there is one. Prints the best side and centre for each SVG path set given.
"""
import math, re, sys
from svgpathtools import parse_path
def points(ds):
    pts = []
    for d in ds:
        for seg in parse_path(d):
            n = max(8, int(seg.length() * 2))
            pts += [seg.point(i / n) for i in range(n + 1)]
    return [(p.real, p.imag) for p in pts]
def clearance(px, py, cx, cy, h):
    dx = max(abs(px - cx) - h, 0); dy = max(abs(py - cy) - h, 0)
    return math.hypot(dx, dy) if (dx or dy) else -1
def best(ds):
    pts = points(ds); top = (0, None)
    for cx2 in range(24, 41):
        for cy2 in range(24, 41):
            cx, cy = cx2, cy2
            lo, hi = 0, 32
            while hi - lo > .25:
                h = (lo + hi) / 2
                ok = all(clearance(px, py, cx, cy, h) >= 4 for px, py in pts)
                lo, hi = (h, hi) if ok else (lo, h)
            if 2 * lo > top[0]: top = (2 * lo, (cx, cy))
    return top
if __name__ == '__main__':
    for arg in sys.argv[1:]:
        ds = re.findall(r' d="([^"]+)"', open(arg).read()) if arg.endswith('.svg') else [arg]
        side, c = best(ds); print(f'{side:5.1f}  centre {c}  {arg[-60:]}')
