"""Raised-arm superhero action figure with a flared cape."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "68dd83e8-24b3-4e97-b65e-c0e9bbe882de"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__superhero-action-figure/20260927T155415Z-thuan-mac-1/reference/figure figurine cape hero show model_68dd83e8-24b3-4e97-b65e-c0e9bbe882de.svg"
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = "superhero-action-figure"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "kids"
    aliases = ("superhero-figurine",)
    keywords = ("superhero", "action", "figure", "cape")

    def build(self):
        # Mirrored raised arms and cape flanks surround a distinct head and stance.
        self.add_arc("head-top", (19, 11), (29, 11), radius_x=5)
        self.add_arc("head-bottom", (29, 11), (19, 11), radius_x=5)
        self.add_contour("head", "head-top", "head-bottom", closed=True)
        self.add_polyline("upper-body", (16, 24), (24, 26), (32, 24))
        self.add_line("torso", (24, 26), (24, 32))
        self.add_polyline("arms-left", (16, 24), (6, 22), (6, 12))
        self.add_polyline("arms-right", (32, 24), (42, 22), (42, 12))
        self.add_polyline("legs", (14, 42), (24, 32), (34, 42))
        self.add_polyline("cape-left", (16, 24), (8, 35), (12, 35))
        self.add_polyline("cape-right", (32, 24), (40, 35), (36, 35))
        for part in ("arms-left", "cape-left"):
            self.relate("connect", part, "upper-body")
        for part in ("arms-right", "cape-right"):
            self.relate("connect", part, "upper-body")
        self.relate("connect", "torso", "upper-body")
        self.relate("connect", "torso", "legs")
        self.mark_human_figure("hero", head="head", torso="torso", torso_junction="start")
