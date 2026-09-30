"""controls-rewind (redraw of the new-pipeline traced SVG).

Plan: two identical hollow left-pointing triangles on HRECT_M (centerline box
(4,10)-(44,38)), sharing the horizontal axis y=24 and mirrored about it.
- One triangle definition (tip, back edge x, half-height) is repeated at two
  x offsets, so both have the same size and angles.
- Each triangle is one closed polyline: tip (x0,24) -> back top (x0+16,10) ->
  back bottom (x0+16,38), painted with round joins like the generated image.
- Width 16, height 28: left triangle x 4..20, right triangle x 28..44. The
  right triangle's tip sits 8 from the left back edge on centerlines (4 ink).
Extremes: left tip x=4, right back edge x=44, back corners y=10 and y=38 --
every side of the HRECT_M box is touched exactly. Lucide `rewind` informed
the construction (two equal closed triangles on one axis); its 2-unit gap is
widened to the profile's 8-unit centerline clearance.

Metric issues:
- clearance e1/e2 3.85 (need 8): fixed. The right tip is now exactly 8 from
  the left triangle's back edge on centerlines.
- clearance e0/e1 7.79 (need 8, one triangle's slanted edge vs its own back
  edge): fixed. Each triangle is now one closed contour whose three sides
  meet at shared round joins, not separate parts; its interior inscribed
  circle is radius 6.35 on centerlines (8.7 ink hole, need 6).
- keyshape-short-axis (y filled 86%, stretch 1.17): fixed, the back corners
  sit on y=10 and y=38.
- stroke-width 2.67 (info): redrawn at stroke 4 with spacing budgeted for it.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2736daad-03fd-5c48-9a0d-f54eed191916"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1109-controls-rewind/controls-rewind_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS_Y = 24
HALF_H = 14            # back corners at y=10 and y=38
WIDTH = 16             # tip to back edge
TIPS = (4, 28)         # left and right triangle tips; gap 28 - (4 + 16) = 8


class ControlsRewindRedraw(Solo48):
    icon_id = "controls-rewind-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "media/controls"
    aliases = ("rewind", "fast backward")
    keywords = ("rewind", "back", "media", "player", "controls", "reverse")

    def build(self) -> None:
        for name, tip in zip(("left", "right"), TIPS):
            back = tip + WIDTH
            self.add_polyline(
                name,
                (tip, AXIS_Y),
                (back, AXIS_Y - HALF_H),
                (back, AXIS_Y + HALF_H),
                closed=True,
            )
