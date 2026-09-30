"""coiled snake (redraw of the new-pipeline traced SVG).

Subject: a snake resting in a flat coil -- a broad oval coil on the ground,
a short tail flicking up on the left, and a neck rising from the back right
into a wedge-shaped head that faces left.

Plan: SQUARE, centerline box (6,6)-(42,42).
Extremes: x=6 the coil's left end and the tail tip, x=42 the coil's right
end, y=42 the coil's front, y=6 the head apex.
- coil: one closed true ellipse (centre (24,36), radii 18x6) made of five
  cubics from the exact ellipse subdivision, knotted at (14,31) and (34,31),
  the mirrored points where the tail and neck leave it.
- tail: one cubic from (14,31) sweeping up-left to a round tip at (6,22).
- neck: one cubic from (34,31) bowing right and reaching the head at
  J=(38,17), tangent-continuous with the back of the head.
- head: closed egg of three cubics (back, crown, jaw) pointing left to the
  snout (17,11); the jaw closes back onto J, leaving the neck/jaw notch.
References: generated PNG read for the subject only (oval coil, left tail,
right neck, left-facing head). No useful Lucide snake exists; construction
follows Lucide's single-stroke animals (one continuous line per body part).
No trace coordinates copied.

Keyshape: SQUARE as suggested (score 1.25, fill 100% both axes).

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap budgeted for it.
- clearance e0/e2 and e1/e2 (neck outline and tail 3.7 from the inner
  coil oval): fixed; the coil is now one ring instead of a doubled tube
  (a 36-wide ring cannot hold an inner oval 8 away at stroke 4), so the
  tail and neck only meet the ring at their own declared junctions.
- hole [30.1,9.5] (3.16, the pinch inside the doubled head/neck tube):
  fixed; the neck is one stroke and the head is its own closed egg with an
  interior about 10 tall.
- hole [24.6,34.5] (2.0, the thin inner coil) and hole [23.4,39.6] (0.6):
  fixed; the single ring encloses one oval hole 12 tall on centerlines.
Dropped: the doubled tube outline of neck and coil and the eye (no eye
fits 8 from the head wall at this size).
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "bd9f57fc-780e-5c9d-8047-c776f0b4d870"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1948-coiled-snake/coiled-snake_raw.svg"
AUTHOR = "claude-opus-5-5"

CX, CY, RX, RY = 24, 36, 18, 6   # coil ring: x 6..42, y 30..42
TH = math.acos(-10 / RX)         # ring angle of the tail junction (14,31); neck mirrors it
TAIL_TIP = (6, 22)
J = (38, 17)                     # neck meets the head (jaw notch)
TOP, SNOUT = (29, 6), (17, 11)   # head apex and snout tip


def _ring(t: float) -> tuple[float, float]:
    return (CX + RX * math.cos(t), CY - RY * math.sin(t))


def _ring_arc(t0: float, t1: float, knot):
    """One cubic of the coil ellipse from angle t0 to t1, ending on integer knot."""
    k = 4 / 3 * math.tan((t1 - t0) / 4)
    (x0, y0), (x1, y1) = _ring(t0), _ring(t1)
    c1 = (x0 - k * RX * math.sin(t0), y0 - k * RY * math.cos(t0))
    c2 = (x1 + k * RX * math.sin(t1), y1 + k * RY * math.cos(t1))
    return (round(c1[0], 2), round(c1[1], 2)), (round(c2[0], 2), round(c2[1], 2)), knot


class CoiledSnakeRedraw(Solo48):
    icon_id = "coiled-snake-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ("coiled serpent", "snake coil")
    keywords = ("snake", "serpent", "coil", "reptile", "python", "cobra", "animal", "wild")

    def build(self) -> None:
        # Coil: one closed ellipse, knotted where the tail and neck leave it.
        left, tl, tr = (CX - RX, CY), (CX - 10, CY - 5), (CX + 10, CY - 5)
        right, bottom = (CX + RX, CY), (CX, CY + RY)
        pi = math.pi
        self.add_bezier("coil-tl", left, _ring_arc(pi, TH, tl))
        self.add_bezier("coil-top", tl, _ring_arc(TH, pi - TH, tr))
        self.add_bezier("coil-tr", tr, _ring_arc(pi - TH, 0, right))
        self.add_bezier("coil-br", right, _ring_arc(0, -pi / 2, bottom))
        self.add_bezier("coil-bl", bottom, _ring_arc(-pi / 2, -pi, left))
        self.add_contour("coil", "coil-tl", "coil-top", "coil-tr", "coil-br", "coil-bl", closed=True)

        # Tail: leaves the ring at its upper left and sweeps up to a round tip.
        self.add_bezier("tail", tl, ((9, 29), (TAIL_TIP[0], 26), TAIL_TIP))
        self.relate("connect", "tail", "coil-tl")
        self.relate("connect", "tail", "coil-top")

        # Neck: rises from the ring's upper right, bowing right, into the head.
        self.add_bezier("neck", tr, ((37, 27), (39, 22), J))
        self.relate("connect", "neck", "coil-top")
        self.relate("connect", "neck", "coil-tr")

        # Head: egg pointing left; back continues the neck, jaw closes at J.
        self.add_bezier("head-back", J, ((37, 12), (35, 6), TOP))
        self.add_bezier("head-top", TOP, ((23, 6), (SNOUT[0], 8), SNOUT))
        self.add_bezier("head-jaw", SNOUT, ((SNOUT[0], 15), (30, 17), J))
        self.add_contour("head", "head-back", "head-top", "head-jaw", closed=True)
        self.relate("connect", "neck", "head-back")
        self.relate("connect", "neck", "head-jaw")
