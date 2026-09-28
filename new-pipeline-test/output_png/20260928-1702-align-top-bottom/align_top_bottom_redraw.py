"""align-top-bottom (redraw of the new-pipeline traced SVG).

Plan: two full-width alignment rails with one bar hanging from the top rail
on the left and one bar standing on the bottom rail on the right, HRECT_M
(centerline box (4,10)-(44,38)).
- rails: horizontal lines y=10 and y=38 from x=4 to x=44; they are the four
  extremes. Each rail is split where its bar attaches so the two share nodes.
- bars: one repeat definition (BAR_W x BAR_H open U) mirrored through the
  centre (24,24): the top bar hangs from the top rail at x 8..20, the bottom
  bar stands on the bottom rail at x 28..40. The rail closes each bar, so the
  bars read as rectangles flush with their alignment edge.
Reference: Lucide `align-vertical-justify-start/end` (rails + hollow bars);
the generated PNG for bar placement (top-left, bottom-right).

Metric issues:
- clearance e0/e1 (3.05) and e2/e3 (2.69): fixed. At stroke 4 a free bar
  needs 8 from its rail, which leaves both bars in the same 18..30 band and
  loses the top/bottom meaning, so each bar now sits on its rail with shared,
  declared connect nodes.
- hole at (9.4,15.4) and (38.7,27.7) (0.8 wide): fixed, bars are 12 wide on
  centerlines (8 inner ink) and 18 tall.
- keyshape-short-axis (x fill 96%): fixed, rails end exactly on x=4 and 44.
- stroke-width info: redrawn at stroke 4 with every gap budgeted at 8
  (bars are 8 apart horizontally).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f31f1d33-4050-4371-af56-548e54cec150"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1702-align-top-bottom/align-top-bottom_raw.svg"
AUTHOR = "claude-opus-5-5"

LEFT, RIGHT = 4, 44      # rail ends
TOP, BOTTOM = 10, 38     # rail heights
BAR_X = 8                # top bar left edge; the bottom bar mirrors it
BAR_W = 12
BAR_H = 18


class AlignTopBottomRedraw(Solo48):
    icon_id = "align-top-bottom-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "editing/alignment"
    aliases = ("align-top-bottom", "align top and bottom")
    keywords = ("align", "alignment", "top", "bottom", "distribute", "layout", "edge")

    def _rail_with_bar(self, name: str, y: int, x0: int, dy: int) -> None:
        x1 = x0 + BAR_W
        self.add_line(f"{name}-rail-a", (LEFT, y), (x0, y))
        self.add_line(f"{name}-rail-b", (x0, y), (x1, y))
        self.add_line(f"{name}-rail-c", (x1, y), (RIGHT, y))
        self.add_polyline(f"{name}-bar", (x0, y), (x0, y + dy), (x1, y + dy), (x1, y))
        for leg, a, b in (("1", "a", "b"), ("3", "b", "c")):
            self.relate("connect", f"{name}-bar-{leg}", f"{name}-rail-{a}")
            self.relate("connect", f"{name}-bar-{leg}", f"{name}-rail-{b}")

    def build(self) -> None:
        self._rail_with_bar("top", TOP, BAR_X, BAR_H)
        self._rail_with_bar("bottom", BOTTOM, 48 - BAR_X - BAR_W, -BAR_H)
