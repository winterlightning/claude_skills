"""Butternut squash: a narrow neck rising to the upper right from a round bulb,
with a short stem growing from the top of the neck.

Symbol plan: one closed body contour of tangent-continuous cubic runs through
six integer nodes (neck top, neck side, waist, bulb bottom, bulb side, back);
the stem is one open curve whose base is a node on the neck cap, leaving it
at a wide angle so no wedge forms. Deliberately asymmetric: the squash leans.
Keyshape SQUARE, centerline box (6,6)-(42,42).
Lucide construction: no squash; pear/eggplant construction (bulb plus
tapered neck, separate stem stroke) informed the drawing.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "0e2a3b90-793a-5161-aa41-5a7e08f9195c"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__butternut-squash-vegetable-batch-010-11/20260925T092530Z-thuan-mac/reference/butternutsquash_0e2a3b90-793a-5161-aa41-5a7e08f9195c.svg"
AUTHOR = "claude-opus-5-5"


class ButternutSquash(Solo48):
    icon_id = "butternut-squash-vegetable-batch-010-11"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ("butternut squash", "squash")
    keywords = ("squash", "butternut", "gourd", "vegetable")

    def build(self) -> None:
        stem_base = (36, 14)
        self.path("body", stem_base, [
            ("C", (38, 15), (41, 17), (41, 21)),   # neck shoulder
            ("C", (41, 25), (33, 27), (29, 32)),   # neck side into the waist
            ("C", (26, 36), (24, 42), (17, 42)),   # waist to bulb bottom
            ("C", (10, 42), (6, 37), (6, 31)),     # bulb bottom to side
            ("C", (6, 25), (12, 24), (18, 21)),    # bulb back to neck
            ("C", (22, 19), (25, 13), (30, 13)),   # back of neck to top
            ("C", (32, 13), (34, 13), stem_base),  # neck cap
        ], closed=True)
        # The stem continues the neck's axis up and to the right.
        self.path("stem", stem_base, [
            ("C", (37, 11), (39, 7), (42, 6)),
        ])
        self.relate("connect", "body", "stem")

    def path(self, name, start, commands, closed=False):
        members = []
        here = start
        for index, (kind, *args) in enumerate(commands):
            member = f"{name}-{index + 1}"
            if kind == "L":
                self.add_line(member, here, args[0])
                here = args[0]
            else:
                self.add_bezier(member, here, (args[0], args[1], args[2]))
                here = args[2]
            members.append(member)
        self.add_contour(name, *members, closed=closed)
