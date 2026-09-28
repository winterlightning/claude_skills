"""Reconstruction of the reference gift box, tied bow, and front heart."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "5862a2a1-e7c8-522a-812d-2db80570e593"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__gift-heart/20260926T165410Z-thuan-mac/reference/gift heart_5862a2a1-e7c8-522a-812d-2db80570e593.svg"
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = "gift-heart"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "rewards"
    aliases = ()
    keywords = ("gift", "box", "bow", "heart")

    def build(self):
        # Reference fit: two bow loops above a broad lid and box, a centered
        # ribbon, and a heart hanging through the lower front edge.
        self.add_arc("bow-left", (12,13), (24,13), radius_x=6, radius_y=7)
        self.add_arc("bow-right", (24,13), (36,13), radius_x=6, radius_y=7)
        self.add_polyline("lid", (8,13),(40,13),(42,15),(42,20),(40,22),(8,22),(6,20),(6,15),closed=True)
        self.add_polyline("box-left", (6,22),(6,38),(21,38))
        self.add_polyline("box-right", (42,22),(42,38),(27,38))
        self.add_line("ribbon", (24,13),(24,22))
        self.add_bezier("heart-left", (24,32), ((21,30),(17,30),(15,30)))
        self.add_line("heart-lower-left", (15,30),(24,42))
        self.add_line("heart-lower-right", (24,42),(33,30))
        self.add_bezier("heart-right", (33,30), ((31,30),(27,30),(24,32)))
        self.add_contour("heart", "heart-left", "heart-lower-left", "heart-lower-right", "heart-right", closed=True)
        for part in ("bow-left", "bow-right", "box-left", "box-right", "ribbon"):
            self.relate("connect", part, "lid")
        self.relate("connect", "bow-left", "bow-right")
        self.relate("connect", "box-left", "heart-lower-left")
        self.relate("connect", "box-right", "heart-lower-right")
