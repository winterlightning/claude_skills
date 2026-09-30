"""Crop rotate (redraw of the new-pipeline traced SVG).

Plan: SQUARE keyshape, centerline box (6,6)-(42,42). Two crossing crop
strokes frame a 16x16 crop box (12,20)-(28,36): the L stroke drops from
(12,14) down the left wall and runs right along the floor to (34,36); the
inverted L runs from (6,20) along the top and down the right wall to (28,42).
Every projecting end is 6 long. They cross at shared nodes (12,20) and
(28,36). A clockwise quarter arc (centre (28,16), r 10) rises above the box's
top-right corner from (28,6) to (38,16), where an open chevron (34,12)-(38,16)-
(42,12) points down. Extremes: left 6 (top stroke), top 6 (arc start),
right 42 (chevron wing), bottom 42 (right wall). The arc grew from the
trace's ~r 9 and the box shrank from ~19 to 16 so the arrow reads as an
arrow at 48 px while keeping its clearance to the box corner.

Metric issues fixed:
- stroke-width: redrawn at stroke 4; all spacing budgeted for it.
- stroke-count: 7 traced strokes -> 4 (two crop strokes, arc, chevron).
- keyshape-short-axis: the y axis now reaches 6 and 42, exact SQUARE fit.
- clearance e0/e1/e2 vs e4/e6 (arrow against crop top/right wall): the arc
  is centred 4 above the box corner (28,20), so every arrow point is >= 10
  from the crop strokes (chevron inner wing 10, arc >= 10.8, arc start 14).
- clearance e3/e4, e5/e6 (crop strokes crossing): intentional crossings, now
  shared nodes declared with relate("connect").
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b05e7a98-e0c7-5855-a771-4dc4b12ff639"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1101-crop-rotate/crop-rotate_raw.svg"
AUTHOR = "claude-opus-5-5"

# crop box and projection length
LEFT, TOP, RIGHT, BOTTOM = 12, 20, 28, 36
PROJ = 6

# rotation arrow: clockwise quarter arc about (28,16), chevron at its end
ARC_R = 10
ARC_START = (28, 6)
ARC_END = (38, 16)
HEAD = 4


class CropRotateRedraw(Solo48):
    icon_id = "crop-rotate-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/editing"
    aliases = ("crop and rotate", "rotate crop")
    keywords = ("crop", "rotate", "image", "photo", "edit", "transform", "clockwise")

    def build(self) -> None:
        self.add_polyline("crop-l", (LEFT, TOP - PROJ), (LEFT, TOP), (LEFT, BOTTOM),
                          (RIGHT, BOTTOM), (RIGHT + PROJ, BOTTOM))
        self.add_polyline("crop-r", (LEFT - PROJ, TOP), (LEFT, TOP), (RIGHT, TOP),
                          (RIGHT, BOTTOM), (RIGHT, BOTTOM + PROJ))
        self.relate("connect", "crop-l", "crop-r")

        self.add_arc("rotate", ARC_START, ARC_END, radius_x=ARC_R, sweep=True)
        ex, ey = ARC_END
        self.add_polyline("head", (ex - HEAD, ey - HEAD), ARC_END, (ex + HEAD, ey - HEAD))
        self.relate("connect", "rotate", "head")
