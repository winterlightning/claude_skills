"""Crescent head wrench (redraw of the new-pipeline traced SVG).

Plan: VRECT_M keyshape, centerline box (10,4)-(38,44), one closed outline
mirrored about x = 24. The head is two quarter-ellipse jaws (rx 8, ry 10,
centres (18,14) and (30,14)) that rise from the side extremes x = 10 / 38 to
blunt tips at (18,4) / (30,4); the tips meet the vertical mouth walls at a
right angle. The mouth is a 12-wide slot (walls x = 18 / 30) closed by a
semicircle (centre (24,10), r 6) bottoming at y = 16. Below the side extremes
an S-cubic with vertical tangents at both ends pulls each side in to the
handle walls x = 18 / 30 at y = 26, so head, neck and handle are
tangent-continuous. The handle ends in a semicircle (centre (24,38), r 6)
whose apex is the bottom extreme y = 44. Extremes: left 10, right 38 (jaw
sides), top 4 (tips), bottom 44 (handle end).

Metric issues fixed:
- stroke-width: redrawn at stroke 4; all spacing budgeted for it.
- keyshape-short-axis: the head now spans x 10..38, so all four extremes sit
  exactly on the VRECT_M box (the trace filled only 66% of the x axis).
- hole (4.4 inscribed): the handle walls and mouth walls are 12 apart on
  centerlines, leaving an 8-wide ink-free channel (need 6).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "47ad292e-443e-5fb5-a71a-0d263bd6ed9e"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1107-crescent-head-wrench/crescent-head-wrench_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
HALF = 6            # half-width of the mouth and the handle (walls at 18 / 30)
TOP, BOTTOM = 4, 44
SIDE = 14           # half-width of the head (sides at 10 / 38)
JAW_Y = 14          # height of the head's side extremes
MOUTH_Y = 10        # where the mouth walls meet the mouth semicircle
NECK_Y = 26         # where the S-curves reach the handle walls
END_Y = BOTTOM - HALF
BEND = 6            # cubic handle length on the neck S-curve


class CrescentHeadWrenchRedraw(Solo48):
    icon_id = "crescent-head-wrench-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ("open end wrench", "spanner", "crescent wrench")
    keywords = ("wrench", "spanner", "tool", "repair", "mechanic", "hardware", "fix")

    def build(self) -> None:
        l, r = AXIS - HALF, AXIS + HALF
        sl, sr = AXIS - SIDE, AXIS + SIDE
        jaw_rx, jaw_ry = SIDE - HALF, JAW_Y - TOP

        self.add_line("mouth-l", (l, TOP), (l, MOUTH_Y))
        self.add_arc("mouth", (l, MOUTH_Y), (r, MOUTH_Y), radius_x=HALF, sweep=False)
        self.add_line("mouth-r", (r, MOUTH_Y), (r, TOP))
        self.add_arc("jaw-r", (r, TOP), (sr, JAW_Y), radius_x=jaw_rx, radius_y=jaw_ry)
        self.add_bezier("neck-r", (sr, JAW_Y),
                        ((sr, JAW_Y + BEND), (r, NECK_Y - BEND), (r, NECK_Y)))
        self.add_line("handle-r", (r, NECK_Y), (r, END_Y))
        self.add_arc("end", (r, END_Y), (l, END_Y), radius_x=HALF)
        self.add_line("handle-l", (l, END_Y), (l, NECK_Y))
        self.add_bezier("neck-l", (l, NECK_Y),
                        ((l, NECK_Y - BEND), (sl, JAW_Y + BEND), (sl, JAW_Y)))
        self.add_arc("jaw-l", (sl, JAW_Y), (l, TOP), radius_x=jaw_rx, radius_y=jaw_ry)
        self.add_contour("wrench", "mouth-l", "mouth", "mouth-r", "jaw-r", "neck-r",
                         "handle-r", "end", "handle-l", "neck-l", "jaw-l", closed=True)
