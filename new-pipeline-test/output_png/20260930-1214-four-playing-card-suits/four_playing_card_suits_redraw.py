"""four-playing-card-suits (redraw of the new-pipeline traced SVG).

Plan: the four suits in a 2x2 grid on SQUARE (centerline box (6,6)-(42,42)),
the keyshape the metrics suggest. Each suit owns a 14x14 cell and the two
gutters are exactly 8 on centerlines: columns x=6..20 (axis 13) and 28..42
(axis 35), rows y=6..20 and 28..42. All mirrored about their own axis.
- heart (upper left): two r4.5 lobes centred 2.5 either side of the axis at
  y=10.5, crossing in the top notch, straight tangent sides down to the point
  (13,20). Lobe tops are the top extreme, the left lobe the left extreme.
- diamond (upper right): 45 degree square, vertices (35,6) (42,13) (35,20)
  (28,13); its right vertex is the right extreme.
- club (lower left): three r4.5 lobes (top one centred (13,32.5), top y=28)
  walked as one outline; the two side lobes cross exactly at (13,39), where
  a single-stroke stem runs down to the bottom extreme (13,42).
- spade (lower right): an upside-down heart on the same side-lobe pair as
  the club, apex (35,28) 8 under the diamond, lobes crossing at (35,39) and
  the same stem to (35,42).
One lobe definition (LOBE_R, LOBE_DX, JOIN_Y) drives heart, club and spade,
so the curved suits stay a matched set. Curves are exact circle arcs turned
into cubics, split at every extreme so the keyshape edge is a knot. The
generated image's hollow flared stems became single Lucide-style strokes:
at 48 px a hollow stem is a sliver hole.
Reference: Lucide heart / diamond / club / spade (circle lobes, tangent
straight sides, stem as a separate line from the lobe junction).
Tried r4 lobes 3 off the axis first: deeper club notches, but the club
(4.9), spade (5.2) and heart (5.8) holes missed the 6 floor.

Metric issues (re-measured with svg_metrics.py on the redraw: 0 issues):
- clearance e0/e1 (heart-diamond 6.3), e0/e3 + e0/e4 (diamond-spade 4.9),
  e1/e2 (heart-club 4.8), e2/e4 (club-spade 5.5): each suit sits in its own
  cell and every gutter is exactly 8 on centerlines.
- hole (13.8,33.9) club 3.7 -> 6.2; hole (34.6,33.0) spade 5.5 -> 5.9
  (heart 6.6, diamond 5.8; all pass the metrics floor): r4.5 lobes and
  single-stroke stems in place of hollow flared ones.
- keyshape-short-axis (y 99%): heart lobe tops and diamond reach y=6, the
  stems y=42, the heart lobe x=6, diamond and spade lobe x=42.
- stroke-width (trace 2.75): redrawn at stroke 4 with 8-unit gaps.
None left unrepaired. validate_icon() valid, build_gate.py PASS (0/0).
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6c01ed88-1571-4e62-904d-509e18f64c7d"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1214-four-playing-card-suits/four-playing-card-suits_raw.svg"
AUTHOR = "claude-opus-5-5"

LEFT_AX, RIGHT_AX = 13, 35      # suit axes (cells 6..20 and 28..42)
TOP_Y, BOTTOM_Y = 6, 42         # SQUARE top / bottom
LOBE_R = 4.5                    # every lobe
LOBE_DX = 2.5                   # lobe centres 2.5 either side of the axis
HEART_POINT_Y = 20              # heart point; 8 above the club's top lobe
DIAMOND_HALF = 7
JOIN_Y = 39                     # club / spade side lobes meet here
STEM_Y = BOTTOM_Y               # stem bottom
CLUB_TOP_CY = 32.5              # club top lobe; its top is y=28
SPADE_APEX_Y = 28               # 8 below the diamond's bottom vertex

K = 4 / 3 * math.tan(math.pi / 8)  # quarter-circle cubic handle


def ang(c, p):
    return math.degrees(math.atan2(p[1] - c[1], p[0] - c[0])) % 360


def arc(c, r, a0, a1, clockwise):
    """Cubics for the circle arc (c, r) from angle a0 to a1 (degrees, y down;
    clockwise on screen = increasing angle), split at every multiple of 90 so
    the extremes are knots."""
    if clockwise:
        a1 = a1 if a1 > a0 else a1 + 360
        cuts = [a0] + [a for a in range(math.floor(a0) + 1, math.ceil(a1)) if a % 90 == 0] + [a1]
    else:
        a1 = a1 if a1 < a0 else a1 - 360
        cuts = [a0] + [a for a in range(math.ceil(a0) - 1, math.floor(a1), -1) if a % 90 == 0] + [a1]
    out = []
    for s, e in zip(cuts, cuts[1:]):
        t0, t1 = math.radians(s), math.radians(e)
        h = 4 / 3 * math.tan((t1 - t0) / 4) * r
        p0 = (c[0] + r * math.cos(t0), c[1] + r * math.sin(t0))
        p1 = (c[0] + r * math.cos(t1), c[1] + r * math.sin(t1))
        out.append(((p0[0] - h * math.sin(t0), p0[1] + h * math.cos(t0)),
                    (p1[0] + h * math.sin(t1), p1[1] - h * math.cos(t1)), p1))
    return out


def line(p, q):
    """A straight run as a cubic, so it can sit inside one smooth outline."""
    return ((p[0] + (q[0] - p[0]) / 3, p[1] + (q[1] - p[1]) / 3),
            (p[0] + 2 * (q[0] - p[0]) / 3, p[1] + 2 * (q[1] - p[1]) / 3), q)


def outer_tangent(p, c, r):
    """The tangent point on circle (c, r) from p on the outer (smaller x) side."""
    d = math.hypot(c[0] - p[0], c[1] - p[1])
    base, t, run = math.atan2(c[1] - p[1], c[0] - p[0]), math.asin(r / d), math.sqrt(d * d - r * r)
    pts = [(p[0] + run * math.cos(base + s * t), p[1] + run * math.sin(base + s * t)) for s in (1, -1)]
    return min(pts, key=lambda q: q[0])


def crossings(c0, c1, r):
    """Both intersections of two equal circles."""
    mx, my = (c0[0] + c1[0]) / 2, (c0[1] + c1[1]) / 2
    dx, dy = c1[0] - c0[0], c1[1] - c0[1]
    d = math.hypot(dx, dy)
    h = math.sqrt(r * r - (d / 2) ** 2)
    return [(mx - s * h * dy / d, my + s * h * dx / d) for s in (1, -1)]


def mirrored_back(ax, start, segs):
    """The walk start -> segs mirrored about x=ax and reversed, ending at start."""
    m = lambda q: (2 * ax - q[0], q[1])
    knots = [start] + [s[2] for s in segs]
    return [(m(segs[i][1]), m(segs[i][0]), m(knots[i])) for i in range(len(segs) - 1, -1, -1)]


class FourPlayingCardSuitsRedraw(Solo48):
    icon_id = "four-playing-card-suits-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "entertainment/games"
    aliases = ("card suits", "playing card suits", "hearts diamonds clubs spades")
    keywords = ("cards", "suits", "heart", "diamond", "club", "spade", "poker", "casino", "game")

    def build(self) -> None:
        r = LOBE_R
        # Heart: point -> left side -> left lobe over the top -> notch, mirrored back.
        ax = LEFT_AX
        point = (ax, HEART_POINT_Y)
        cl, cr = (ax - LOBE_DX, TOP_Y + r), (ax + LOBE_DX, TOP_Y + r)
        notch = min(crossings(cl, cr, r), key=lambda q: q[1])
        t = outer_tangent(point, cl, r)
        left = [line(point, t)] + arc(cl, r, ang(cl, t), ang(cl, notch), clockwise=True)
        self.add_bezier("heart", point, *left, *mirrored_back(ax, point, left))
        self.add_contour("heart-outline", "heart", closed=True)

        # Diamond: 45 degree square filling its cell.
        ax, h = RIGHT_AX, DIAMOND_HALF
        cy = TOP_Y + h
        self.add_polyline("diamond", (ax, TOP_Y), (ax + h, cy), (ax, cy + h), (ax - h, cy), closed=True)

        # Club and spade share the side-lobe pair: centres at the axis +/- LOBE_DX,
        # low enough that the two circles cross exactly at (axis, JOIN_Y).
        side_cy = JOIN_Y - math.sqrt(r * r - LOBE_DX * LOBE_DX)

        # Club: join -> under and round the left lobe -> notch -> top lobe to its
        # top, mirrored back to the join; the stem hangs from the join.
        ax = LEFT_AX
        join = (ax, JOIN_Y)
        cl, ct = (ax - LOBE_DX, side_cy), (ax, CLUB_TOP_CY)
        notch = min(crossings(ct, cl, r), key=lambda q: q[0])
        left = (arc(cl, r, ang(cl, join), ang(cl, notch), clockwise=True)
                + arc(ct, r, ang(ct, notch), 270, clockwise=True))
        self.add_bezier("club", join, *left, *mirrored_back(ax, join, left))
        self.add_contour("club-outline", "club", closed=True)
        self.add_line("club-stem", join, (ax, STEM_Y))
        self.relate("connect", "club-stem", "club-outline")

        # Spade: apex -> left side -> round and under the left lobe -> join,
        # mirrored back to the apex; same stem as the club.
        ax = RIGHT_AX
        apex, join = (ax, SPADE_APEX_Y), (ax, JOIN_Y)
        cl = (ax - LOBE_DX, side_cy)
        t = outer_tangent(apex, cl, r)
        left = [line(apex, t)] + arc(cl, r, ang(cl, t), ang(cl, join), clockwise=False)
        self.add_bezier("spade", apex, *left, *mirrored_back(ax, apex, left))
        self.add_contour("spade-outline", "spade", closed=True)
        self.add_line("spade-stem", join, (ax, STEM_Y))
        self.relate("connect", "spade-stem", "spade-outline")
