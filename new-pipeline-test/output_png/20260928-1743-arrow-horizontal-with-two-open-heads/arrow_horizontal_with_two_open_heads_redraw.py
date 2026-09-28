"""arrow horizontal with two open heads (redraw of the new-pipeline traced SVG).

Plan: HRECT_M (centerline box (4,10)-(44,38)), after Lucide `move-horizontal`
(one shaft on the axis, an open chevron at each end sharing the shaft's end
point), which is the generated image's construction. Mirrored about x=24.
- shaft: y=SHAFT_Y from the left tip (4, 24) to the right tip (44, 24), the
  x=4 and x=44 extremes.
- heads: chevrons with 45-degree arms HEAD_ARM units per axis, as in the
  image. HEAD_ARM = 14 puts the arm ends on y=10 and y=38, the HRECT_M
  short-axis extremes. Each head shares its tip with the shaft (declared
  connect).
Metric issues:
- stroke-width (trace 2.4): redrawn at stroke 4 on the integer grid.
- stroke-count (7 strokes, budget 6): fixed; the two degenerate cap blobs
  (e1, e5) are gone and each open head is one polyline, so the icon is 3
  strokes (shaft + two heads).
- keyshape-short-axis (y filled 47%): fixed; the arm ends reach y=10 and
  y=38 and the tips x=4 and x=44, so all four HRECT_M extremes are exact.
  The heads are larger than in the image (14 vs ~9 units per arm) because
  the tolerance-0 fit leaves no other way to fill the short axis.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d940547b-c44c-47a1-b2e3-3fd157a39a48"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1743-arrow-horizontal-with-two-open-heads/arrow-horizontal-with-two-open-heads_raw.svg"
AUTHOR = "claude-opus-5-5"

LEFT_X = 4
RIGHT_X = 44
SHAFT_Y = 24
HEAD_ARM = 14


class ArrowHorizontalWithTwoOpenHeadsRedraw(Solo48):
    icon_id = "arrow-horizontal-with-two-open-heads-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/arrows"
    aliases = ("double-headed arrow", "left right arrow", "move horizontal")
    keywords = ("arrow", "horizontal", "both ways", "left", "right", "resize", "width")

    def build(self) -> None:
        left_tip = (LEFT_X, SHAFT_Y)
        right_tip = (RIGHT_X, SHAFT_Y)

        self.add_line("shaft", left_tip, right_tip)
        self.add_polyline("left-head", (LEFT_X + HEAD_ARM, SHAFT_Y - HEAD_ARM),
                          left_tip, (LEFT_X + HEAD_ARM, SHAFT_Y + HEAD_ARM))
        self.add_polyline("right-head", (RIGHT_X - HEAD_ARM, SHAFT_Y - HEAD_ARM),
                          right_tip, (RIGHT_X - HEAD_ARM, SHAFT_Y + HEAD_ARM))
        self.relate("connect", "left-head", "shaft")
        self.relate("connect", "right-head", "shaft")
