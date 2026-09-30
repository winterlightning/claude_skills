"""downward-reflection-diagram (redraw of the new-pipeline traced SVG).

Plan: a reflection diagram on SQUARE (centerline box (6,6)-(42,42)), five
strokes, laid out as in the generated image:
- tri-top: closed right triangle, right angle at (8,16), apex (8,6), foot
  (24,16); the flat 16-long leg faces the axis.
- tri-bottom: the same triangle mirrored about y=24 (right angle (8,32),
  apex (8,42), foot (24,32)).
- axis: horizontal reflection line y=24 from x=6 to x=26, overhanging both
  triangles by 2 (legs at x=8, feet at x=24).
- arrow: straight downward arrow on the right, shaft x=37 from y=10 to
  y=38 (centred on y=24 like the image), V head with 5-unit wings to
  (32,33) and (42,33).
Symmetry: the triangles and the axis share the mirror y=24; the arrow is
mirrored about its own shaft x=37.
Extremes: x=6 (axis start), x=42 (right wing), y=6 / y=42 (triangle
apexes), so the SQUARE fit is exact.
Clearances (centerlines): triangle legs to axis 8; foot (24,16) to axis end
(26,24) 8.2; axis end to shaft 11; lower foot (24,32) to left wing tip
(32,33) 8.06; upper foot (24,16) to shaft 13.

Metric issues:
- stroke-width (info): redrawn at stroke 4, every gap budgeted at 8.
- clearance e0/e4 and e4/e5 (triangles 4 from the axis): fixed, each
  triangle's flat leg is 8 from the axis.
- hole at [13.5,15.7] and [13.4,32.4] (4.6-4.7 wide, need 6): NOT fixed.
  With the axis between the triangles the 36-unit box leaves each triangle
  10 tall (10 + 8 + 8 + 10 = 36). A triangle's inradius is under half its
  smallest altitude, so it is < 5 and the stroke-4 ink hole (2r - 4) can
  never reach 6. The 16x10 triangles have a centerline inradius of 3.57
  (ink hole about 3.1), which passes the build's hole gate (validate_icon
  valid, build_gate PASS). Turning the triangles so their points face the
  axis (14 tall, 23 wide, ink hole 6.1) fixes the metric, but read as a
  "Z" or an envelope rather than a mirror diagram, so it was rejected.
Lucide construction: `arrow-down` (straight shaft with a symmetric 45-degree
V head) and `flip-vertical-2` (mirrored triangles about a horizontal axis).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "80d9152e-7c3d-4bfe-8c06-1a9d8b17db38"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1203-downward-reflection-diagram/"
    "downward-reflection-diagram_raw.svg"
)
AUTHOR = "claude-opus-5-5"

MIRROR = 24             # reflection axis y
GAP = 8                 # centerline clearance, triangle leg to axis
TRI_H = 10              # triangle height (36 box - 2 gaps) / 2
LEG_X = 8               # triangles' vertical legs
FOOT_X = 24             # triangles' acute feet
AXIS_X0, AXIS_X1 = 6, 26
SHAFT_X = 37
SHAFT_TOP, TIP_Y = 10, 38
WING = 5


class DownwardReflectionDiagramRedraw(Solo48):
    icon_id = "downward-reflection-diagram-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/geometry"
    aliases = ("reflection diagram", "vertical reflection", "flip vertical",
               "mirror down")
    keywords = ("reflection", "mirror", "flip", "vertical", "triangle",
                "axis", "symmetry", "geometry", "transform", "down")

    def build(self) -> None:
        near_top = MIRROR - GAP             # 16
        near_bottom = MIRROR + GAP          # 32

        # the triangle and its mirror image about y=24
        self.add_polyline(
            "tri-top",
            (LEG_X, near_top - TRI_H), (LEG_X, near_top), (FOOT_X, near_top),
            closed=True,
        )
        self.add_polyline(
            "tri-bottom",
            (LEG_X, near_bottom + TRI_H), (LEG_X, near_bottom),
            (FOOT_X, near_bottom),
            closed=True,
        )
        self.add_line("axis", (AXIS_X0, MIRROR), (AXIS_X1, MIRROR))

        # downward arrow
        self.add_line("shaft", (SHAFT_X, SHAFT_TOP), (SHAFT_X, TIP_Y))
        self.add_polyline(
            "head",
            (SHAFT_X - WING, TIP_Y - WING), (SHAFT_X, TIP_Y),
            (SHAFT_X + WING, TIP_Y - WING),
        )
        self.relate("connect", "shaft", "head")
