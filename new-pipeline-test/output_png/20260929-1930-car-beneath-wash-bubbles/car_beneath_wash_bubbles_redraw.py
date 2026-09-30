"""car beneath wash bubbles (redraw of the new-pipeline traced SVG).

Plan: a front-view car with two soap bubbles floating above it, VRECT_L
keyshape (centerline box (8,4)-(40,44)), everything mirrored about x=24
except the bubbles.
- body: one closed contour. Top edge y=32 (the windshield base / divider)
  from cabin foot (11,32) to (37,32), r3 fender arcs rounding down into the
  side walls x=8/40, walls to y=44, 8-wide tyre tabs (x 8..16 / 32..40,
  4 tall) and the raised underbody y=40 between them.
- cabin: one open contour from (11,32) to (37,32) sharing the body's foot
  nodes (declared connect). 1:2 flanks rise to (14,26)/(34,26), cubics
  round them into the roof about the corners (15.5,23)/(32.5,23), and the
  roof runs level at y=23 from (19,23) to (29,23). Each flank and its roof
  corner are one element, so the curve shares its node with the divider;
  the windshield band is 9, keeping the corner's near-level part 8+ above
  the divider.
- bubbles: an r5 ring about (16,9) (top y=4) and an r3 ring about (33,12),
  smaller and lower to the right as in the generated image. Centres 17.26
  apart (9.26 on centerlines), big ring 9 above the roof, small ring 8+
  from the roof corner.
Every arc centre and knot is on the integer grid; nothing is copied from the
trace coordinates.

Metric issues:
- error `clearance` e0/e1 (the two bubbles, 5.72): fixed, 9.26.
- errors `clearance` e0/e3, e1/e3 (bubbles against the roof, 4.69 / 3.2):
  fixed, 9 and 8+ above the roof.
- error `clearance` e2/e3 (divider 7.1 below the roof): fixed, the
  windshield band is 9.
- errors `clearance` e2/e4, e2/e5, e3/e4, e3/e5 (headlights crowding the
  divider and side walls): resolved by removing the headlights, see below.
- errors `hole` (bubble 4.94, small bubble 1.71, windshield corner 3.2):
  fixed, the big ring is r5 (6+ inscribed), the small ring is an r3 ring
  (a 6-diameter circle, exempt), the windshield is a 9-tall trapezoid and
  the body band 8 tall.
- warn `keyshape-short-axis` (x filled 87% on SQUARE): fixed by switching to
  VRECT_L, whose 32x40 box matches the 0.87 aspect; x=8/40 are the side
  walls, y=4 the big bubble top, y=44 the tyre bottoms, all exact.
- info `stroke-width` (trace 2.4, target 4): handled by construction at
  stroke 4; every gap between distinct parts is >= 8 on centerlines.
Dropped: the two headlight strokes. Each needs 8 to the divider and 8 to
the underbody (a 16 body band); with 9 of windshield, 4 of tyre and 18 of
bubble plus gap that is 47 units against 40.
Lucide construction used: `car-front` (sloped cabin over a wide body, wheel
stubs below, the windshield rule at the body top) and `circle` rings.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d7783b02-e678-4b5f-a12d-e6dd227ecdd8"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1930-car-beneath-wash-bubbles/car-beneath-wash-bubbles_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS, WALL_L = 24, 8
ROOF_Y, DIVIDER_Y, UNDER_Y, BOTTOM_Y, TYRE_W = 23, 32, 40, 44, 8
CABIN_FOOT, FLANK_TOP, ROOF_END = (11, 32), (14, 26), (19, 23)  # left side; 1:2 flank
ROOF_CORNER = (15.5, 23)                                        # flank meets the roof line here
BIG_BUBBLE, BIG_R = (16, 9), 5
SMALL_BUBBLE, SMALL_R = (33, 12), 3
K = 0.5523


def _mirror(p):
    return (2 * AXIS - p[0], p[1])


def _straight(p0, p3):
    return ((2 * p0[0] + p3[0]) / 3, (2 * p0[1] + p3[1]) / 3), \
        ((p0[0] + 2 * p3[0]) / 3, (p0[1] + 2 * p3[1]) / 3), p3


def _corner(p0, v, p3):
    c1 = (p0[0] + K * (v[0] - p0[0]), p0[1] + K * (v[1] - p0[1]))
    c2 = (p3[0] + K * (v[0] - p3[0]), p3[1] + K * (v[1] - p3[1]))
    return c1, c2, p3


class CarBeneathWashBubblesRedraw(Solo48):
    icon_id = "car-beneath-wash-bubbles-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/car"
    aliases = ("car wash", "car cleaning", "auto wash")
    keywords = ("car", "wash", "bubbles", "soap", "clean", "vehicle", "auto")

    def build(self) -> None:
        m = _mirror
        shoulder_r = CABIN_FOOT[0] - WALL_L                     # fender arc meets the cabin foot
        shoulder, bottom = (WALL_L, DIVIDER_Y + shoulder_r), (WALL_L, BOTTOM_Y)
        tyre_in, under = (WALL_L + TYRE_W, BOTTOM_Y), (WALL_L + TYRE_W, UNDER_Y)

        self.add_arc("fender-l", shoulder, CABIN_FOOT, radius_x=shoulder_r, sweep=True)
        self.add_line("divider", CABIN_FOOT, m(CABIN_FOOT))
        self.add_arc("fender-r", m(CABIN_FOOT), m(shoulder), radius_x=shoulder_r, sweep=True)
        self.add_line("wall-r", m(shoulder), m(bottom))
        self.add_line("tyre-r-bottom", m(bottom), m(tyre_in))
        self.add_line("tyre-r-in", m(tyre_in), m(under))
        self.add_line("underbody", m(under), under)
        self.add_line("tyre-l-in", under, tyre_in)
        self.add_line("tyre-l-bottom", tyre_in, bottom)
        self.add_line("wall-l", bottom, shoulder)
        self.add_contour("body", "fender-l", "divider", "fender-r", "wall-r", "tyre-r-bottom",
                         "tyre-r-in", "underbody", "tyre-l-in", "tyre-l-bottom", "wall-l",
                         closed=True)

        # each flank and its roof corner are one element rising from the cabin
        # foot, so the curve shares that node with the divider
        self.add_bezier("flank-l", CABIN_FOOT, _straight(CABIN_FOOT, FLANK_TOP),
                        _corner(FLANK_TOP, ROOF_CORNER, ROOF_END))
        self.add_line("roof", ROOF_END, m(ROOF_END))
        self.add_bezier("flank-r", m(ROOF_END),
                        _corner(m(ROOF_END), m(ROOF_CORNER), m(FLANK_TOP)),
                        _straight(m(FLANK_TOP), m(CABIN_FOOT)))
        self.add_contour("cabin", "flank-l", "roof", "flank-r")
        self.relate("connect", "cabin", "body")

        for name, (cx, cy), r in (("bubble-big", BIG_BUBBLE, BIG_R),
                                  ("bubble-small", SMALL_BUBBLE, SMALL_R)):
            n, e, s, w = (cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)
            self.add_arc(f"{name}-ne", n, e, radius_x=r, sweep=True)
            self.add_arc(f"{name}-se", e, s, radius_x=r, sweep=True)
            self.add_arc(f"{name}-sw", s, w, radius_x=r, sweep=True)
            self.add_arc(f"{name}-nw", w, n, radius_x=r, sweep=True)
            self.add_contour(name, f"{name}-ne", f"{name}-se", f"{name}-sw", f"{name}-nw",
                             closed=True)
