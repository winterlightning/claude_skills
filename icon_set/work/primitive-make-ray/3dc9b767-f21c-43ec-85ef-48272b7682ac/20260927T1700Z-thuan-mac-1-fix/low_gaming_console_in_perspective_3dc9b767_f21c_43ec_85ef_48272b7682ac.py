"""A low game console in perspective with the reference's top control.

Lucide box informed the shared top and side junctions. Perspective is
intentionally asymmetric, as in the source drawing.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3dc9b767-f21c-43ec-85ef-48272b7682ac"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__low-gaming-console-in-perspective/20260927T164357Z-thuan-mac-1/reference/playstation four_3dc9b767-f21c-43ec-85ef-48272b7682ac.svg"
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = "low-gaming-console-in-perspective"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    aliases = ("game console",)
    keywords = ("console", "perspective", "power control")

    def build(self):
        self.add_polyline(
            "outline", (4, 22), (26, 8), (44, 18),
            (40, 31), (22, 40), (4, 32), closed=True,
        )
        self.add_polyline("top-seam", (4, 22), (22, 29), (44, 18))
        self.add_line("front-corner", (22, 29), (22, 40))
        self.add_dot("power-control", (26, 18))
        self.relate("connect", "outline", "top-seam")
        self.relate("connect", "outline", "front-corner")
        self.relate("connect", "top-seam", "front-corner")
