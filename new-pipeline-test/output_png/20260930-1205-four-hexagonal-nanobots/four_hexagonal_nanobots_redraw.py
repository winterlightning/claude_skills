"""four-hexagonal-nanobots (redraw of the new-pipeline traced SVG).

Plan: four identical hollow pointy-top hexagons in a two-by-two grid, on
SQUARE (centerline box (6,6)-(42,42)), the keyshape the metrics suggest
(fill 1.0 x 1.0, matches the square shape hint).
- one hexagon definition (HEX_W wide, HEX_H tall, SLANT rise on each
  shoulder), repeated at four centres mirrored about x=24 and y=24.
- columns: outer flat sides on x=6 / x=42 (left/right extremes).
- rows: top points on y=6, bottom points on y=42 (top/bottom extremes).
- the column gutter and the point-to-point row gutter are both >= 8 on
  centerlines (4 of clear ink).
Every hexagon is one closed polyline, so its corners paint as round joins,
as in the generated image. No Lucide match for a hexagon grid; Lucide
`hexagon` informed the single cell (pointy-top, straight edges, round joins).

Metric issues:
- clearance e0/e1 and e2/e3 (6.7 apart across the column gutter): the
  hexagons are narrowed so the gutter between the facing flat sides is 12.
- clearance e0/e2 and e1/e3 (3.3 point-to-point, ink overlapping): each
  hexagon is 14 tall, so the bottom point of the upper row sits exactly 8
  above the top point of the lower row.
- stroke-width (trace 2.77 after fitting): redrawn at stroke 4 with the
  gaps above measured at stroke 4.
Holes: each cell interior is 8 wide on ink (>= 6 inscribed).
Nothing dropped: the source has only the four outlines.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a4ac6021-31ac-4b55-8c99-d25a6ba3e475"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1205-four-hexagonal-nanobots/four-hexagonal-nanobots_raw.svg"
AUTHOR = "claude-opus-5-5"

LO, HI = 6, 42          # SQUARE centerline box
HEX_W = 12              # flat side to flat side
HEX_H = 14              # point to point; row gutter = 36 - 2*14 = 8
SLANT = 4               # rise of each shoulder edge (~34 degrees, near-regular)
CENTRES_X = (LO + HEX_W // 2, HI - HEX_W // 2)
CENTRES_Y = (LO + HEX_H // 2, HI - HEX_H // 2)


class FourHexagonalNanobotsRedraw(Solo48):
    icon_id = "four-hexagonal-nanobots-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ("nanobots", "hexagon grid", "four hexagons")
    keywords = ("nanobot", "nanotechnology", "hexagon", "robot", "swarm", "science")

    def build(self) -> None:
        hw, hh = HEX_W // 2, HEX_H // 2
        for row, cy in enumerate(CENTRES_Y):
            for col, cx in enumerate(CENTRES_X):
                self.add_polyline(
                    f"bot-{row}{col}",
                    (cx, cy - hh),
                    (cx + hw, cy - hh + SLANT),
                    (cx + hw, cy + hh - SLANT),
                    (cx, cy + hh),
                    (cx - hw, cy + hh - SLANT),
                    (cx - hw, cy - hh + SLANT),
                    closed=True,
                )
