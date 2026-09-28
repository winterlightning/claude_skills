"""Upright artillery shell with three separate upper fins."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a7e31bff-1b16-45b4-8791-44858266dfbc"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__symbol-artillery/20260927T155415Z-thuan-mac-1/reference/symbol artillery_a7e31bff-1b16-45b4-8791-44858266dfbc.svg"
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = "symbol-artillery"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "war"
    aliases = ("artillery-shell",)
    keywords = ("artillery", "shell", "fins")

    def build(self):
        # Reference has a tall rounded shell and an open three-prong fin crown.
        self.add_bezier("body-shoulder-left", (13, 24), ((13, 20), (18, 17), (24, 17)))
        self.add_bezier("body-shoulder-right", (24, 17), ((30, 17), (35, 20), (35, 24)))
        self.add_line("body-side-right", (35, 24), (35, 34))
        self.add_arc("body-bottom", (35, 34), (13, 34), radius_x=11, radius_y=10)
        self.add_line("body-side-left", (13, 34), (13, 24))
        self.add_contour("shell", "body-shoulder-left", "body-shoulder-right", "body-side-right", "body-bottom", "body-side-left", closed=True)
        self.add_polyline("left-fin", (8, 4), (8, 16), (13, 24))
        self.add_polyline("middle-fin", (8, 4), (24, 17), (40, 4))
        self.add_polyline("right-fin", (40, 4), (40, 16), (35, 24))
        self.add_line("central-rib", (24, 4), (24, 17))
        self.relate("connect", "left-fin", "middle-fin")
        self.relate("connect", "right-fin", "middle-fin")
        self.relate("connect", "middle-fin", "shell")
        self.relate("connect", "central-rib", "middle-fin")
        self.relate("connect", "central-rib", "shell")
        self.relate("connect", "left-fin", "shell")
        self.relate("connect", "right-fin", "shell")
