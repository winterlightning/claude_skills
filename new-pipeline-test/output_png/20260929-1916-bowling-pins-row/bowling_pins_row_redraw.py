"""bowling-pins-row (redraw of the new-pipeline traced SVG).

Plan: three bowling pins on SQUARE (centerline box (6,6)-(42,42)), mirrored
about x=24, drawn as a formation: one front pin in the middle and two back
pins set 9 to each side and 3 higher, half hidden behind it.
- one pin profile (half outline, top-down): head circle r6, a neck pinched
  to about 9 wide, a belly 18 wide and a flat 10-wide base. Arcs are cubic
  quarter/partial circles with integer knots.
- front pin: the profile and its mirror closed into one contour; it owns the
  y=42 base extreme.
- back pins: the same profile shifted (-9,-3) / mirrored, drawn only where
  it shows: from the knot where its head crosses the front head, over the
  head (the y=6 extreme), down the outer side (belly on the x=6 / x=42
  extremes) and along its base to the knot where it disappears behind the
  front pin. Both ends are knots of the front contour, declared connect.
  Its foot taper is a little steeper than the front pin's so the two stay
  8 apart down to the shared base knot (build gate internal-spacing).
Metric issues:
- clearance e0-e1 / e0-e2 (pins 3.2 apart): three separate pins cannot fit
  at 8 spacing (3 bellies of at least 16 + two gaps of 8 > 40 on any
  keyshape), so the back pins overlap and join the front pin at shared knots
  instead of floating 3 apart. Fixed.
- holes at [10.1,13.2] / [37.8,13.2] (necks pinched shut): every neck stays
  at least 8 wide on centerlines, so each pin interior is one open hole.
  Fixed.
- keyshape-short-axis (HRECT_M x fill 96%): the overlapping formation is
  as tall as it is wide, so it moves to SQUARE with all four extremes exact.
- stroke-width (trace 2.55): drawn at stroke 4 with 8-unit spacing.
No useful Lucide match (Lucide has no bowling pins).
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d972c303-2754-4efe-82ae-c0b2f535370b"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1916-bowling-pins-row/bowling-pins-row_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
HEAD_C = (24, 15)       # front head centre, r6
HEAD_R = 6
BACK_SHIFT = (-9, -3)   # left back pin = front pin moved left 9, up 3

# Front pin, left half, top-down knots.
TOP = (24, 9)
HEAD_W = (18, 15)
HEAD_SW = (19, 18)
BELLY = (15, 32)
FOOT = (19, 42)
NECK_OUT = 3.0          # handle leaving the head into the neck
BELLY_IN = 6.0          # handle arriving at the belly
FOOT_C1 = (15, 36.5)
FOOT_C2 = (16.5, 40.5)

HEAD_JOIN = (21, 10)    # back head crosses the front head here
BASE_Y = 39             # back pins' base, 3 above the front base
# Back pins' lower taper, a little steeper than the front one so it keeps
# 8 from the front pin's taper all the way down to the shared base knot.
BACK_FOOT = (9, 39)
BACK_FOOT_C = ((6, 34), (7, 37.5))


def mx(p):
    return (2 * AXIS - p[0], p[1])


def arc_controls(c, p0, p1):
    """Cubic handles for a circle-like arc about c from p0 to p1 (short way)."""
    a0 = math.atan2(p0[1] - c[1], p0[0] - c[0])
    a1 = math.atan2(p1[1] - c[1], p1[0] - c[0])
    d = (a1 - a0 + math.pi) % (2 * math.pi) - math.pi
    k = 4 / 3 * math.tan(d / 4)
    r0 = math.hypot(p0[0] - c[0], p0[1] - c[1])
    r1 = math.hypot(p1[0] - c[0], p1[1] - c[1])
    c1 = (p0[0] - k * r0 * math.sin(a0), p0[1] + k * r0 * math.cos(a0))
    c2 = (p1[0] + k * r1 * math.sin(a1), p1[1] - k * r1 * math.cos(a1))
    return (round(c1[0], 3), round(c1[1], 3)), (round(c2[0], 3), round(c2[1], 3))


def split_at_y(p0, c1, c2, p3, y):
    """Split a cubic where it crosses y; snap the new knot to the grid."""
    def pt(t):
        u = 1 - t
        return tuple(u**3 * a + 3 * u * u * t * b + 3 * u * t * t * cc + t**3 * d
                     for a, b, cc, d in zip(p0, c1, c2, p3))
    lo, hi = 0.0, 1.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if (pt(mid)[1] - y) * (p3[1] - p0[1]) < 0:
            lo = mid
        else:
            hi = mid
    t = (lo + hi) / 2
    lerp = lambda a, b: tuple(a_ + (b_ - a_) * t for a_, b_ in zip(a, b))
    ab, bc, cd = lerp(p0, c1), lerp(c1, c2), lerp(c2, p3)
    abc, bcd = lerp(ab, bc), lerp(bc, cd)
    knot = tuple(round(v) for v in lerp(abc, bcd))
    r3 = lambda p: (round(p[0], 3), round(p[1], 3))
    return (r3(ab), r3(abc), knot), (r3(bcd), r3(cd), p3)


def front_left_segments():
    """Front pin left half, top-down, as (c1, c2, knot) from TOP."""
    t = (HEAD_SW[0] - HEAD_C[0], HEAD_SW[1] - HEAD_C[1])
    n = math.hypot(*t)
    neck_dir = (-t[1] / n, t[0] / n)          # tangent leaving the head, CCW
    if neck_dir[1] < 0:
        neck_dir = (-neck_dir[0], -neck_dir[1])
    neck = (
        (round(HEAD_SW[0] + neck_dir[0] * NECK_OUT, 3), round(HEAD_SW[1] + neck_dir[1] * NECK_OUT, 3)),
        (BELLY[0], BELLY[1] - BELLY_IN),
        BELLY,
    )
    lower_a, lower_b = split_at_y(BELLY, FOOT_C1, FOOT_C2, FOOT, BASE_Y)
    return [
        (*arc_controls(HEAD_C, TOP, HEAD_JOIN), HEAD_JOIN),
        (*arc_controls(HEAD_C, HEAD_JOIN, HEAD_W), HEAD_W),
        (*arc_controls(HEAD_C, HEAD_W, HEAD_SW), HEAD_SW),
        neck,
        lower_a,
        lower_b,
    ]


def reverse(start, segs):
    """Reverse a cubic run: returns (new_start, segments)."""
    pts = [start] + [s[2] for s in segs]
    out = []
    for i in range(len(segs) - 1, -1, -1):
        c1, c2, _ = segs[i]
        out.append((c2, c1, pts[i]))
    return pts[-1], out


def mirror_segs(segs):
    return [tuple(mx(p) for p in s) for s in segs]


def shift(p):
    return (p[0] + BACK_SHIFT[0], p[1] + BACK_SHIFT[1])


class BowlingPinsRowRedraw(Solo48):
    icon_id = "bowling-pins-row-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports/bowling"
    aliases = ("bowling pins", "skittles", "ten pin bowling")
    keywords = ("bowling", "pins", "skittles", "tenpin", "alley", "strike", "sport", "game")

    def build(self) -> None:
        left = front_left_segments()   # TOP->JOIN, JOIN->W, W->SW, SW->BELLY, BELLY->BASE, BASE->FOOT
        base_join = left[4][2]
        right = mirror_segs(left)

        # Front pin: one closed contour, clockwise from the head top, split at
        # the four knots where the back pins attach.
        self.add_bezier("front-head-r", TOP, right[0])
        self.add_bezier("front-side-r", mx(HEAD_JOIN), *right[1:5])
        self.add_bezier("front-foot-r", mx(base_join), right[5])
        self.add_line("front-base", mx(FOOT), FOOT)
        _, up = reverse(TOP, left)     # FOOT -> ... -> TOP
        self.add_bezier("front-foot-l", FOOT, up[0])
        self.add_bezier("front-side-l", base_join, *up[1:5])
        self.add_bezier("front-head-l", HEAD_JOIN, up[5])
        self.add_contour("front", "front-head-r", "front-side-r", "front-foot-r", "front-base",
                         "front-foot-l", "front-side-l", "front-head-l", closed=True)

        # Left back pin: the same profile shifted, from the head knot over
        # the head and down the outside to its foot, then its base back to
        # the knot where it disappears behind the front pin.
        bc = shift(HEAD_C)
        b_top = shift(TOP)
        b_segs = [(*arc_controls(bc, HEAD_JOIN, b_top), b_top),
                  (*arc_controls(bc, b_top, shift(HEAD_W)), shift(HEAD_W))]
        for c1, c2, k in left[2:4]:
            b_segs.append((shift(c1), shift(c2), shift(k)))
        b_segs.append((*BACK_FOOT_C, BACK_FOOT))
        b_foot = BACK_FOOT
        self.add_bezier("back-l", HEAD_JOIN, *b_segs)
        self.add_line("back-l-base", b_foot, base_join)
        self.add_contour("back-left", "back-l", "back-l-base")

        self.add_bezier("back-r", mx(HEAD_JOIN), *mirror_segs(b_segs))
        self.add_line("back-r-base", mx(b_foot), mx(base_join))
        self.add_contour("back-right", "back-r", "back-r-base")

        for side in ("back-left", "back-right"):
            self.relate("connect", side, "front")
