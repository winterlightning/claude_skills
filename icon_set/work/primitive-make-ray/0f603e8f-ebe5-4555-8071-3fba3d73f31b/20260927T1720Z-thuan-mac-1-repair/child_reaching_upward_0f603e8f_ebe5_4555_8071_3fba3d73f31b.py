"""A child lifting the right arm and stepping with the left leg.

The source supplies the pose. The shared full-body human reference supplies
the round head, simple limbs, and exact detached head clearance. The original
continuous silhouette is reduced to the pose's identifying lines at 48px.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "0f603e8f-ebe5-4555-8071-3fba3d73f31b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__child-reaching-upward/20260927T164357Z-thuan-mac-1/reference/child reaching_0f603e8f-ebe5-4555-8071-3fba3d73f31b.svg"
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = "child-reaching-upward"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people"
    aliases = ("reaching child",)
    keywords = ("child", "reach", "upward", "raised arm")

    def build(self):
        self.add_arc("head-upper", (15, 10), (27, 10), radius_x=6, sweep=True)
        self.add_arc("head-lower", (27, 10), (15, 10), radius_x=6, sweep=True)
        self.add_contour("head", "head-upper", "head-lower", closed=True)
        self.add_line("torso", (21, 24), (21, 34))
        self.add_line("left-arm", (21, 24), (8, 32))
        self.add_polyline("right-arm", (21, 24), (34, 24), (40, 8))
        self.add_polyline("left-leg", (21, 34), (14, 40), (8, 42))
        self.add_line("right-leg", (21, 34), (29, 44))
        for part in ("left-arm", "right-arm", "left-leg", "right-leg"):
            self.relate("connect", "torso", part)
        self.relate("connect", "left-arm", "right-arm")
        self.relate("connect", "left-leg", "right-leg")
        self.mark_human_figure("child", head="head", torso="torso", torso_junction="start")
