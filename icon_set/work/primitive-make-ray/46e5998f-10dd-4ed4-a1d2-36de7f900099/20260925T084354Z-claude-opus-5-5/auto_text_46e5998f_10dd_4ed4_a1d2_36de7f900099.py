"""AUTO wordmark, hand-authored as one SOLO48 text icon.

Symbol plan: four monoline capitals A-U-T-O in reading order on a 2x2 grid
(AU over TO), because a single row of four letters needs 56 centerline units
of width against a 32-unit budget. Shared parameters: two columns of width
CELL_W separated by GAP, two rows of height CELL_H separated by GAP, so every
letter-to-letter clearance is exactly the 8-unit MIC. Cell ratio 12x16 keeps
the reference's ~0.72 cap proportion.

- A: blunted apex (short flat top, painted with round joins, standing in for
  the reference's small rounded peak), straight legs on a 1:4 integer slope,
  crossbar low (75%) as in the reference.
- U: two straight walls into a semicircular bowl, tangent-continuous.
- T: crossbar split at the stem so the stem shares an endpoint.
- O: stadium (semicircle / straight sides / semicircle), matching the
  reference's upright rounded O with short straight flanks.

Lucide: no letterform icon was useful; the construction follows Lucide's
stadium/semicircle joins (e.g. `pill`) for U and O.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "46e5998f-10dd-4ed4-a1d2-36de7f900099"
SOURCE_PATH = "icon_set/work/todo-references/auto (text)_46e5998f-10dd-4ed4-a1d2-36de7f900099.svg"
AUTHOR = "claude-opus-5-5"

LEFT, TOP = 8, 4          # VRECT_L centerline box (8,4)-(40,44)
CELL_W, CELL_H, GAP = 12, 16, 8
COL = (LEFT, LEFT + CELL_W + GAP)
ROW = (TOP, TOP + CELL_H + GAP)
R = CELL_W // 2           # bowl radius shared by U and O


class AutoText(Solo48):
    icon_id = "auto-text"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "typeface/word"
    aliases = ("auto", "automatic")
    keywords = ("auto", "text", "word", "wordmark", "automatic", "mode")

    def build(self) -> None:
        # A -- top-left cell.
        x0, y0 = COL[0], ROW[0]
        x1, y1 = x0 + CELL_W, y0 + CELL_H
        self.add_polyline(
            "a-outline",
            (x0, y1), (x0 + 1, y1 - 4), (x0 + 4, y0), (x1 - 4, y0), (x1 - 1, y1 - 4), (x1, y1),
        )
        self.add_line("a-crossbar", (x0 + 1, y1 - 4), (x1 - 1, y1 - 4))
        self.relate("connect", "a-outline-1", "a-crossbar")
        self.relate("connect", "a-outline-5", "a-crossbar")

        # U -- top-right cell.
        x0, y0 = COL[1], ROW[0]
        x1, y1 = x0 + CELL_W, y0 + CELL_H
        self.add_line("u-left", (x0, y0), (x0, y1 - R))
        self.add_arc("u-bowl", (x0, y1 - R), (x1, y1 - R), radius_x=R, radius_y=R, sweep=False)
        self.add_line("u-right", (x1, y1 - R), (x1, y0))
        self.add_contour("u", "u-left", "u-bowl", "u-right")

        # T -- bottom-left cell.
        x0, y0 = COL[0], ROW[1]
        x1, y1 = x0 + CELL_W, y0 + CELL_H
        xm = x0 + CELL_W // 2
        self.add_line("t-bar-left", (x0, y0), (xm, y0))
        self.add_line("t-bar-right", (xm, y0), (x1, y0))
        self.add_contour("t-bar", "t-bar-left", "t-bar-right")
        self.add_line("t-stem", (xm, y0), (xm, y1))
        self.relate("connect", "t-bar-left", "t-bar-right", "t-stem")

        # O -- bottom-right cell, stadium.
        x0, y0 = COL[1], ROW[1]
        x1, y1 = x0 + CELL_W, y0 + CELL_H
        self.add_arc("o-top", (x0, y0 + R), (x1, y0 + R), radius_x=R, radius_y=R, sweep=True)
        self.add_line("o-right", (x1, y0 + R), (x1, y1 - R))
        self.add_arc("o-bottom", (x1, y1 - R), (x0, y1 - R), radius_x=R, radius_y=R, sweep=True)
        self.add_line("o-left", (x0, y1 - R), (x0, y0 + R))
        self.add_contour("o", "o-top", "o-right", "o-bottom", "o-left", closed=True)
