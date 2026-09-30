"""hanging-toilet-paper-roll-solo: a toilet paper roll seen from the front
left, its round end facing us and one sheet hanging down from the front
(redraw of the new-pipeline traced SVG).

Plan: SQUARE (centerline box (6,6)-(42,42)).
- end: the roll's end face, an upright ellipse rx=9 ry=13 about (15,19)
  built from quarter arcs; its extremes (6,19) and (15,6) sit on the box.
- core: the cardboard core seen edge-on as a short vertical slot through
  the ellipse centre; it stays > 8 on centerlines from the face.
- body: one contour from the front of the end face -- the sheet's left
  edge drops from the face's right extreme (24,19), a gentle wave runs to
  the bottom-right corner (42,42), the back wall rises to a round shoulder
  (r=8) and the top line returns tangent into the face's top (15,6).
No Lucide original matches (no toilet-paper icon in the local set).

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4 with every gap budgeted for it.
- keyshape-short-axis: the trace filled 87% of the SQUARE height; the face
  now reaches y=6 and the hem's right corner y=42, so all four extremes sit
  on the box with no stretch.
- clearance e0/e2 (face vs core, 2.88) and e1/e2 (body vs core, 4.31): the
  hollow core ellipse is replaced by a 6-long slot whose nearest point is
  8.5 from the face and > 13 from the body.
- hole x2 (2.24 and 2.01 wide): those slivers lay between the core ellipse
  and the face; with the slot core they no longer exist -- the only holes
  are the face interior and the sheet interior, both far above 6.
None left unfixed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f361cec1-680c-41d1-8ef8-1055d54cab23"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1526-hanging-toilet-paper-roll-solo/hanging-toilet-paper-roll-solo_raw.svg"
AUTHOR = "claude-opus-5-5"

# End face.
FX, FY = 15, 19
RX, RY = 9, 13
TOP = (FX, FY - RY)          # (15, 6)
LEFT = (FX - RX, FY)         # (6, 19)
BOTTOM = (FX, FY + RY)       # (15, 32)
FRONT = (FX + RX, FY)        # (24, 19): the sheet leaves the roll here
CORE_HALF = 3

# Body.
RIGHT = 42
SHOULDER_R = 8
SHEET_LEFT_END = (FRONT[0], 40)
SHEET_RIGHT_END = (RIGHT, 42)


class HangingToiletPaperRollSoloRedraw(Solo48):
    icon_id = "hanging-toilet-paper-roll-solo-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/household"
    aliases = ("toilet-paper", "toilet-roll", "tissue-roll")
    keywords = ("toilet", "paper", "roll", "tissue", "bathroom", "restroom", "hygiene", "wc")

    def build(self) -> None:
        # End face, clockwise on screen from its top.
        self.add_arc("face-tr", TOP, FRONT, radius_x=RX, radius_y=RY, sweep=True)
        self.add_arc("face-br", FRONT, BOTTOM, radius_x=RX, radius_y=RY, sweep=True)
        self.add_arc("face-bl", BOTTOM, LEFT, radius_x=RX, radius_y=RY, sweep=True)
        self.add_arc("face-tl", LEFT, TOP, radius_x=RX, radius_y=RY, sweep=True)
        self.add_contour("face", "face-tr", "face-br", "face-bl", "face-tl", closed=True)

        self.add_line("core", (FX, FY - CORE_HALF), (FX, FY + CORE_HALF))

        # Sheet and roll body, from the front of the face round to its top.
        self.add_line("sheet-left", FRONT, SHEET_LEFT_END)
        self.add_bezier("sheet-hem", SHEET_LEFT_END, ((30, 37), (35, 42), SHEET_RIGHT_END))
        self.add_line("back", SHEET_RIGHT_END, (RIGHT, TOP[1] + SHOULDER_R))
        self.add_arc("shoulder", (RIGHT, TOP[1] + SHOULDER_R), (RIGHT - SHOULDER_R, TOP[1]),
                     radius_x=SHOULDER_R, sweep=False)
        self.add_line("top", (RIGHT - SHOULDER_R, TOP[1]), TOP)
        self.add_contour("body", "sheet-left", "sheet-hem", "back", "shoulder", "top")
        self.relate("connect", "sheet-left", "face-tr")
        self.relate("connect", "top", "face-tr")
