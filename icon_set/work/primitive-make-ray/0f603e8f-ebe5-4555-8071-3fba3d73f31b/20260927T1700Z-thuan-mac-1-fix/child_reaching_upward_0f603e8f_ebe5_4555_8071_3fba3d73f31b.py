"""A child in a continuous silhouette lifting one arm overhead.

The original source supplies the pose and connected outline; the shared human
full-body reference supplies the simple round head and limb proportions.
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
        members = []
        def line(name, a, b):
            self.add_line(name, a, b)
            members.append(name)
        def curve(name, a, c1, c2, b):
            self.add_bezier(name, a, (c1, c2, b))
            members.append(name)

        curve("head-left", (18, 17), (14, 16), (13, 13), (14, 10))
        curve("head-top", (14, 10), (14, 6), (18, 4), (23, 4))
        curve("head-right", (23, 4), (29, 4), (32, 9), (30, 13))
        line("neck-right", (30, 13), (27, 17))
        line("shoulder-right", (27, 17), (30, 17))
        line("arm-upper", (30, 17), (37, 8))
        curve("raised-hand", (37, 8), (39, 7), (40, 8), (40, 10))
        line("arm-lower", (40, 10), (30, 23))
        line("side-right", (30, 23), (32, 27))
        line("right-leg-outer", (32, 27), (32, 42))
        curve("right-foot", (32, 42), (32, 44), (29, 44), (26, 44))
        line("right-leg-inner", (26, 44), (24, 42))
        line("crotch-right", (24, 42), (24, 33))
        line("crotch-left", (24, 33), (22, 32))
        line("left-leg-inner", (22, 32), (17, 40))
        line("left-foot-inner", (17, 40), (11, 44))
        curve("left-foot", (11, 44), (9, 44), (8, 42), (8, 40))
        line("left-leg-outer", (8, 40), (16, 31))
        line("side-left", (16, 31), (17, 25))
        line("left-arm-inner", (17, 25), (12, 31))
        curve("left-hand", (12, 31), (10, 32), (8, 30), (8, 28))
        line("left-arm-outer", (8, 28), (8, 24))
        line("shoulder-left", (8, 24), (16, 18))
        line("neck-left", (16, 18), (18, 17))
        self.add_contour("child-silhouette", *members, closed=True)
