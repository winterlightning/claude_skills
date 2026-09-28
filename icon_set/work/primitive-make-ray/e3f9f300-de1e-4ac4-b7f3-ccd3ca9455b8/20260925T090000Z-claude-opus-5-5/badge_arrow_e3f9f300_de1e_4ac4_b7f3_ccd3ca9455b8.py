"""Badge arrow: an upright tag with a pointed roof (a house-shaped arrow badge).

Symbol plan: one closed contour mirrored about x=24 -- roof apex on the top
edge, 3:4 roof slopes to shoulders, straight walls, small radius-4 bottom
corners as in the reference's softened base. Lucide: `badge` informed the
single closed outline; no closer match.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e3f9f300-de1e-4ac4-b7f3-ccd3ca9455b8"
SOURCE_PATH = "icon_set/work/todo-references/badge arrow_e3f9f300-de1e-4ac4-b7f3-ccd3ca9455b8.svg"
AUTHOR = "claude-opus-5-5"

CX, TOP, BOTTOM = 24, 4, 44
HALF = 16                 # VRECT_L centerline half width -> x 8..40
SHOULDER = 16             # roof rise 12 over run 16 (3:4)
CORNER = 4


class BadgeArrow(Solo48):
    icon_id = "badge-arrow"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/badge"
    aliases = ("arrow badge", "pointer badge", "tag up")
    keywords = ("badge", "arrow", "up", "pentagon", "tag", "label")

    def build(self) -> None:
        l, r = CX - HALF, CX + HALF
        self.add_line("roof-left", (CX, TOP), (l, SHOULDER))
        self.add_line("wall-left", (l, SHOULDER), (l, BOTTOM - CORNER))
        self.add_arc("corner-left", (l, BOTTOM - CORNER), (l + CORNER, BOTTOM), radius_x=CORNER, radius_y=CORNER, sweep=False)
        self.add_line("base", (l + CORNER, BOTTOM), (r - CORNER, BOTTOM))
        self.add_arc("corner-right", (r - CORNER, BOTTOM), (r, BOTTOM - CORNER), radius_x=CORNER, radius_y=CORNER, sweep=False)
        self.add_line("wall-right", (r, BOTTOM - CORNER), (r, SHOULDER))
        self.add_line("roof-right", (r, SHOULDER), (CX, TOP))
        self.add_contour(
            "outline", "roof-left", "wall-left", "corner-left", "base",
            "corner-right", "wall-right", "roof-right", closed=True,
        )
