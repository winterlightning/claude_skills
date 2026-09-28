"""arrow down rounded outline (redraw of the new-pipeline traced SVG).

Plan: VRECT_M (centerline box (10,4)-(38,44)), after Lucide `arrow-down`
(vertical shaft plus a 90-degree chevron sharing the tip). The generated
image is a hollow double-line drawing of that same three-stroke arrow (the
choice brief: shaft + two symmetric arms); the "rounded outline" is the
round-capped stroke itself, so it is rebuilt as single stroke-4 centerlines
with round caps and joins rather than as the trace's closed silhouette.
- shaft: x = AXIS_X from the top (AXIS_X, 4) (the y=4 extreme) down to the
  tip (AXIS_X, 44) (the y=44 extreme).
- head: chevron (10, 44 - ARM) -> tip -> (38, 44 - ARM), 45-degree arms
  ARM = 14 per axis, so the arm ends are the x=10 and x=38 extremes.
  Mirrored about x=24; shares the tip with the shaft (declared connect).
Metric issues:
- stroke-width (trace 2.4): redrawn at stroke 4 on the integer grid.
- keyshape-short-axis (x filled 84%): fixed; arm ends on x=10 and x=38,
  shaft top on y=4 and tip on y=44, so all four VRECT_M extremes are exact.
- hole (1.13 wide at [23.9, 40.9]): fixed. It was the sliver between the
  inner and outer walls of the traced outline at the tip; drawn as
  centerlines the arrow has no enclosed region, and the openings between
  each arm end and the shaft are ARM = 14 >= 8.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6747c5ea-98ee-4045-b34c-2a968c515c7a"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1730-arrow-down-rounded-outline/arrow-down-rounded-outline_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS_X = 24
TOP_Y = 4
TIP_Y = 44
ARM = 14


class ArrowDownRoundedOutlineRedraw(Solo48):
    icon_id = "arrow-down-rounded-outline-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/arrows"
    aliases = ("down arrow", "arrow downward", "arrow down")
    keywords = ("arrow", "down", "downward", "direction", "download", "descend", "south")

    def build(self) -> None:
        tip = (AXIS_X, TIP_Y)
        self.add_line("shaft", (AXIS_X, TOP_Y), tip)
        self.add_polyline("head", (AXIS_X - ARM, TIP_Y - ARM), tip,
                          (AXIS_X + ARM, TIP_Y - ARM))
        self.relate("connect", "head", "shaft")
