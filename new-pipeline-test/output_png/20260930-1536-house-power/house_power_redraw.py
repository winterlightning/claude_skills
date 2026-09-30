"""house-power (redraw of the new-pipeline traced SVG).

Plan: a gabled house with overhanging eaves and a lightning bolt inside, on
SQUARE (the suggested keyshape, fit score 1.25), centerline box (6,6)-(42,42),
mirrored on the axis x=24.
- roof: one straight run per side on a 2:3 slope from the apex (24,6) to the
  eave tips (6,18) and (42,18). Each run is split at the wall tops (9,16) and
  (39,16), so the short eave stubs stay collinear with the roof, as in the
  generated image, and the walls attach at shared endpoints.
- walls and base: an open U from (9,16) down to the base y=42 and back up to
  (39,16), connected to the roof at both wall tops.
- bolt: an open zigzag, point-symmetric about (24,25): (24,16) down-left to
  (19,25), across to (29,25), down-left to (24,34). The two diagonals are
  parallel, 8.74 apart; the top clears both roof lines by 8.32 and the bottom
  sits 8 above the base.
Lucide `house` informed the gabled outline and `zap` the bolt direction; the
bolt is reduced to a single stroke because a hollow bolt cannot hold 6-unit
openings inside a 20-unit interior at stroke 4.

Metric issues fixed:
- clearance e0/e2 (bolt 4.06 from the base): the bolt ends at y=34, 8 above
  the base.
- clearance e1/e2 (bolt 7.05 from the roof): the bolt top is at (24,16),
  8.32 from both roof lines.
- hole at (21.4,26.2), 1.79 wide: the hollow bolt is redrawn as an open
  zigzag stroke, so it encloses no hole.
- stroke-width (info): redrawn at stroke 4 with every gap budgeted at 8.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "95e78717-28bd-4a88-951a-54d6ae9c18e6"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1536-house-power/house-power_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
APEX_Y, EAVE_Y, WALL_TOP_Y, BASE_Y = 6, 18, 16, 42
EAVE_DX, WALL_DX = 18, 15               # half widths: eave tips, walls
BOLT_TOP, BOLT_MID, BOLT_BOTTOM = 16, 25, 34
BOLT_DX = 5                             # half width of the middle bar


class HousePowerRedraw(Solo48):
    icon_id = "house-power-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "buildings"
    aliases = ("home power", "house electricity", "home energy", "powered house")
    keywords = ("house", "home", "power", "electricity", "energy", "lightning", "bolt", "utility")

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

        self.add_polyline(
            "bolt",
            (a, BOLT_TOP),
            (a - BOLT_DX, BOLT_MID),
            (a + BOLT_DX, BOLT_MID),
            (a, BOLT_BOTTOM),
        )
