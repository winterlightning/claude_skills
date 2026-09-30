"""diagonal-paperclip (redraw of the new-pipeline traced SVG).

Plan: one open wire on SQUARE (centerline box (6,6)-(42,42)), four parallel
45-degree strands on the lines x+y = 30 / 42 / 54 / 66, every neighbouring
pair 12 apart in x+y = 8.49 between centerlines (the stroke-4 minimum is 8).
The strands are joined by three nested U-turns, as in the generated image:
- big turn (upper right) joins strand 1 and strand 4 about C1 = (29,19),
  radius 12.73 at the strand ends (C1 -+ (9,9)); its top knot (29,6) and right
  knot (42,19) carry axis tangents, so the top and right extremes are exact.
- lower-left turn joins strand 4 and strand 2 about C2 = (21,33), radius 8.49
  at the strand ends (C2 -+ (6,6)); its bottom knot (21,42) is the bottom
  extreme.
- small inner turn joins strand 2 and strand 3, concentric with the big turn
  (C1 -+ (3,3), apex (32,16)), leaving the same 8.49 gap inside the big turn.
- free ends: strand 1 runs out to (6,24), the left extreme; strand 3 stops at
  (25,29), on the axis of the lower-left turn, 10.2 from both of its strands.
Turns are tangent-continuous cubics through integer knots (a true semicircle
on a 45-degree axis cannot have integer ends and integer extremes at once).

Metric issues fixed:
- stroke-width (info): the trace stroke fitted to 2.77; redrawn at stroke 4
  with every strand gap widened to 8.49 on centerlines (the trace had 4.2-6.6)
  so no gap shrinks below the 8-unit minimum.
No junctions, clearance, hole or human issues were listed.
Lucide `paperclip` informed the construction (one wire, nested concentric
return bends, 45-degree strands at a uniform pitch).
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5473937d-c579-47bd-9ac8-1ed8c210eb47"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1220-diagonal-paperclip-batch-021-13/diagonal-paperclip-batch-021-13_raw.svg"
AUTHOR = "claude-opus-5-5"

C1 = (29, 19)              # big turn and small turn centre
C2 = (21, 33)              # lower-left turn centre
FREE_A = (6, 24)           # strand 1 free end (x+y = 30)
FREE_B = (25, 29)          # strand 3 free end (x+y = 54)

UP_RIGHT = (1, -1)
DOWN_LEFT = (-1, 1)


def _off(c, d):
    return (c[0] + d[0], c[1] + d[1])


def _unit(v):
    n = math.hypot(*v)
    return (v[0] / n, v[1] / n)


def _turn(knots):
    """Cubic segments through (point, tangent) knots, circle-style handles."""
    segments = []
    for (p0, t0), (p3, t3) in zip(knots, knots[1:]):
        u0, u3 = _unit(t0), _unit(t3)
        angle = math.acos(max(-1.0, min(1.0, u0[0] * u3[0] + u0[1] * u3[1])))
        chord = math.dist(p0, p3)
        h = chord * (4 / 3) * math.tan(angle / 4) / (2 * math.sin(angle / 2))
        c1 = (round(p0[0] + u0[0] * h, 3), round(p0[1] + u0[1] * h, 3))
        c2 = (round(p3[0] - u3[0] * h, 3), round(p3[1] - u3[1] * h, 3))
        segments.append((c1, c2, p3))
    return segments


class DiagonalPaperclipRedraw(Solo48):
    icon_id = "diagonal-paperclip-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/office"
    aliases = ("paperclip", "paper clip", "attachment")
    keywords = ("attach", "attachment", "clip", "file", "office", "stationery")

    def build(self) -> None:
        p1 = _off(C1, (-9, -9))            # strand 1 top end
        p4 = _off(C1, (9, 9))              # strand 4 top end
        q4 = _off(C2, (6, 6))              # strand 4 bottom end
        q2 = _off(C2, (-6, -6))            # strand 2 bottom end
        s2 = _off(C1, (-3, -3))            # strand 2 top end
        s3 = _off(C1, (3, 3))              # strand 3 top end

        self.add_line("strand-1", FREE_A, p1)
        self.add_bezier("big-turn", p1, *_turn([
            (p1, UP_RIGHT),
            (_off(C1, (0, -13)), (1, 0)),  # top extreme y = 6
            (_off(C1, (13, 0)), (0, 1)),   # right extreme x = 42
            (p4, DOWN_LEFT),
        ]))
        self.add_line("strand-4", p4, q4)
        self.add_bezier("lower-turn", q4, *_turn([
            (q4, DOWN_LEFT),
            (_off(C2, (0, 9)), (-1, 0)),   # bottom extreme y = 42
            (_off(C2, (-9, 0)), (0, -1)),
            (q2, UP_RIGHT),
        ]))
        self.add_line("strand-2", q2, s2)
        self.add_bezier("small-turn", s2, *_turn([
            (s2, UP_RIGHT),
            (_off(C1, (3, -3)), (1, 1)),
            (s3, DOWN_LEFT),
        ]))
        self.add_line("strand-3", s3, FREE_B)
        self.add_contour("wire", "strand-1", "big-turn", "strand-4", "lower-turn",
                         "strand-2", "small-turn", "strand-3")
