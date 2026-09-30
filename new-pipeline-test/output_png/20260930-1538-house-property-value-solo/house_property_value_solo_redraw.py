"""house-property-value-solo (redraw of the new-pipeline traced SVG).

Plan: a gabled house with overhanging eaves and a rising arrow inside, on
SQUARE (the suggested keyshape, fit score 1.12), centerline box (6,6)-(42,42),
the house mirrored on the axis x=24.
- roof: one straight run per side on a 2:3 slope from the apex (24,6) to the
  eave tips (6,18) and (42,18). Each run is split at the wall tops (9,16) and
  (39,16), so the eave stubs stay collinear with the roof, as in the generated
  image, and the walls attach at shared endpoints.
- walls and base: an open U from (9,16) down to the base y=42 and back up to
  (39,16), connected to the roof at both wall tops.
- arrow: a 45 degree shaft from the tail (18,34) up to the tip (31,21) and an
  open right-angle head of two 8-unit arms, (23,21)-(31,21)-(31,29), sharing
  the tip. The tip sits 8 from the right wall, 8.6 from the right roof line;
  the tail sits 8 above the base and 9 from the left wall.
Lucide `house` informed the gabled outline and `arrow-up-right` the arrow
(shaft into the corner of an L-shaped head). The arrow is deliberately
directional, so it is not mirrored; it is shifted as far up-right as the
clearances allow, following the image.

Metric issues fixed:
- clearance e0/e2, e0/e3, e0/e4 (arrowhead 5.85 from the roof): the tip moved
  down to y=21, 8.6 from the right roof line.
- clearance e1/e2 (arrow tail 4.51 from the base): the tail ends at y=34,
  8 above the base.
- clearance e1/e3, e1/e4 (arrowhead 6.91 from the right wall): the tip and the
  vertical head arm sit at x=31, exactly 8 from the wall at x=39.
- keyshape-short-axis (y filled 87%): the roof apex now reaches y=6 and the
  base y=42, so both SQUARE extremes are on the box, as are the eave tips on x.
- stroke-width (info): redrawn at stroke 4 with every gap budgeted at 8.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ec996bcb-4c1a-4d3c-84fb-8218d5fa19b8"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1538-house-property-value-solo/house-property-value-solo_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
APEX_Y, EAVE_Y, WALL_TOP_Y, BASE_Y = 6, 18, 16, 42
EAVE_DX, WALL_DX = 18, 15               # half widths: eave tips, walls
TIP = (31, 21)                          # arrow tip, 8 inside the right wall
SHAFT = 13                              # 45 degree run from tail to tip
HEAD = 8                                # length of each arrowhead arm


class HousePropertyValueSoloRedraw(Solo48):
    icon_id = "house-property-value-solo-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "buildings"
    aliases = ("property value", "home value", "house price rise", "real estate growth")
    keywords = ("house", "home", "property", "value", "price", "rising", "arrow", "growth", "real estate", "investment")

    def build(self) -> None:
        a = AXIS
        apex = (a, APEX_Y)
        left_top, right_top = (a - WALL_DX, WALL_TOP_Y), (a + WALL_DX, WALL_TOP_Y)
        self.add_line("eave-left", (a - EAVE_DX, EAVE_Y), left_top)
        self.add_line("roof-left", left_top, apex)
        self.add_line("roof-right", apex, right_top)
        self.add_line("eave-right", right_top, (a + EAVE_DX, EAVE_Y))
        self.add_contour("roof", "eave-left", "roof-left", "roof-right", "eave-right")

        self.add_polyline(
            "walls", left_top, (a - WALL_DX, BASE_Y), (a + WALL_DX, BASE_Y), right_top
        )
        self.relate("connect", "roof", "walls")

        tx, ty = TIP
        self.add_line("arrow-shaft", (tx - SHAFT, ty + SHAFT), TIP)
        self.add_polyline("arrow-head", (tx - HEAD, ty), TIP, (tx, ty + HEAD))
        self.relate("connect", "arrow-shaft", "arrow-head")
