"""Automatic drive gear shown as the AUTO wordmark, one SOLO48 text icon.

Symbol plan: monoline capitals A-U-T-O in reading order on a 2x2 grid (AU over
TO); a single row of four letters needs ~56 centerline units against a 32-unit
budget. Two columns of CELL_W and two rows of CELL_H separated by GAP make every
letter-to-letter clearance exactly the 8-unit MIC; 12x16 cells keep the
reference's ~0.72 cap proportion. A has a blunted apex and a low crossbar on a
1:4 integer leg slope; U is straight walls into a tangent semicircle; T's bar
is split at the stem; O is a stadium. Lucide: no letterform match; U/O follow
the stadium/semicircle construction of `pill`.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f89489d3-928e-4d8e-8a13-9ff760315c90"
SOURCE_PATH = "icon_set/work/todo-references/automatic drive gear_f89489d3-928e-4d8e-8a13-9ff760315c90.svg"
AUTHOR = "claude-opus-5-5"

LEFT, TOP = 8, 4          # VRECT_L centerline box (8,4)-(40,44)
CELL_W, CELL_H, GAP = 12, 16, 8
COL = (LEFT, LEFT + CELL_W + GAP)
ROW = (TOP, TOP + CELL_H + GAP)
R = CELL_W // 2           # bowl radius shared by U and O


class AutomaticDriveGear(Solo48):
    icon_id = "automatic-drive-gear"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/vehicle"
    aliases = ("auto", "automatic transmission", "auto gear")
    keywords = ("auto", "automatic", "drive", "gear", "transmission", "text")

    def build(self) -> None:
        x0, y0 = COL[0], ROW[0]
        x1, y1 = x0 + CELL_W, y0 + CELL_H
        self.add_polyline(
            "a-outline",
            (x0, y1), (x0 + 1, y1 - 4), (x0 + 4, y0), (x1 - 4, y0), (x1 - 1, y1 - 4), (x1, y1),
        )
        self.add_line("a-crossbar", (x0 + 1, y1 - 4), (x1 - 1, y1 - 4))
        self.relate("connect", "a-outline-1", "a-crossbar")
        self.relate("connect", "a-outline-5", "a-crossbar")

        x0, y0 = COL[1], ROW[0]
        x1, y1 = x0 + CELL_W, y0 + CELL_H
        self.add_line("u-left", (x0, y0), (x0, y1 - R))
        self.add_arc("u-bowl", (x0, y1 - R), (x1, y1 - R), radius_x=R, radius_y=R, sweep=False)
        self.add_line("u-right", (x1, y1 - R), (x1, y0))
        self.add_contour("u", "u-left", "u-bowl", "u-right")

        x0, y0 = COL[0], ROW[1]
        x1, y1 = x0 + CELL_W, y0 + CELL_H
        xm = x0 + CELL_W // 2
        self.add_line("t-bar-left", (x0, y0), (xm, y0))
        self.add_line("t-bar-right", (xm, y0), (x1, y0))
        self.add_contour("t-bar", "t-bar-left", "t-bar-right")
        self.add_line("t-stem", (xm, y0), (xm, y1))
        self.relate("connect", "t-bar-left", "t-bar-right", "t-stem")

        x0, y0 = COL[1], ROW[1]
        x1, y1 = x0 + CELL_W, y0 + CELL_H
        self.add_arc("o-top", (x0, y0 + R), (x1, y0 + R), radius_x=R, radius_y=R, sweep=True)
        self.add_line("o-right", (x1, y0 + R), (x1, y1 - R))
        self.add_arc("o-bottom", (x1, y1 - R), (x0, y1 - R), radius_x=R, radius_y=R, sweep=True)
        self.add_line("o-left", (x0, y1 - R), (x0, y0 + R))
        self.add_contour("o", "o-top", "o-right", "o-bottom", "o-left", closed=True)
