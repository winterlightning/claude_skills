"""diving block weight (redraw of the new-pipeline traced SVG).

Plan: a wide diving-belt block weight on HRECT_M (centerline box
(4,10)-(44,38)), mirrored about x=24.
- block: one closed rounded rectangle whose four straight sides sit on the
  keyshape extremes x=4, x=44, y=10, y=38, joined by tangent quarter arcs of
  radius CORNER_R (integer centres), so every extreme is exact.
- belt slots: two vertical round-capped strokes at x=AXIS-SLOT_DX and its
  mirror, running SLOT_TOP..SLOT_BOTTOM (19..29); each is 9 on centerlines from the
  top/bottom walls and well clear of the side walls and each other.

Metric issues fixed:
- keyshape-short-axis: the block now spans the full 28-unit short axis
  (y 10..38) instead of 85% of it.
- clearance e0-e1 / e0-e2 (3.24 apart): slots end 9 from the top and bottom
  walls on centerlines.
- holes at the block corners (3.6 inscribed) and inside the slots (1.8):
  the corner pockets were trace artefacts and are gone; the only closed
  hole is the block interior (>6 inscribed everywhere).
- stroke-width: drawn at stroke 4 on the 48 grid, spacing budgeted for it.
Change from the trace: the slots are drawn as single stroke pills, not
outlined rounded rectangles. An outlined slot needs a centerline width of
10 for a 6-unit hole, and two of them plus the 8-unit gap between them (28)
exceed the 24-unit band left inside the side walls, so the outline cannot
pass at stroke 4; a 4-wide pill reads as the same slot at 48 px.
Lucide construction: `rectangle-horizontal` / `battery` style rounded
rectangle (straight sides, tangent corner arcs) with inner stroke marks.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "284b7c04-e252-4531-868f-398d3ef94159"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1151-diving-block-weight/diving-block-weight_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
LEFT, RIGHT, TOP, BOTTOM = 4, 44, 10, 38
CORNER_R = 6
SLOT_DX = 10                   # slots at x=14 and x=34
SLOT_TOP, SLOT_BOTTOM = TOP + 9, BOTTOM - 9  # 9, not 8: exact-8 caps come back review


class DivingBlockWeightRedraw(Solo48):
    icon_id = "diving-block-weight-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports/diving"
    aliases = ("dive weight", "belt weight", "scuba weight")
    keywords = ("diving", "scuba", "weight", "lead", "belt", "block", "ballast")

    def build(self) -> None:
        r = CORNER_R
        # Clockwise from the top-left tangent point (sweep=True in y-down SVG).
        self.add_line("top", (LEFT + r, TOP), (RIGHT - r, TOP))
        self.add_arc("corner-tr", (RIGHT - r, TOP), (RIGHT, TOP + r), radius_x=r)
        self.add_line("right", (RIGHT, TOP + r), (RIGHT, BOTTOM - r))
        self.add_arc("corner-br", (RIGHT, BOTTOM - r), (RIGHT - r, BOTTOM), radius_x=r)
        self.add_line("bottom", (RIGHT - r, BOTTOM), (LEFT + r, BOTTOM))
        self.add_arc("corner-bl", (LEFT + r, BOTTOM), (LEFT, BOTTOM - r), radius_x=r)
        self.add_line("left", (LEFT, BOTTOM - r), (LEFT, TOP + r))
        self.add_arc("corner-tl", (LEFT, TOP + r), (LEFT + r, TOP), radius_x=r)
        self.add_contour(
            "block", "top", "corner-tr", "right", "corner-br",
            "bottom", "corner-bl", "left", "corner-tl", closed=True,
        )

        for side, x in (("l", AXIS - SLOT_DX), ("r", AXIS + SLOT_DX)):
            self.add_line(f"slot-{side}", (x, SLOT_TOP), (x, SLOT_BOTTOM))
