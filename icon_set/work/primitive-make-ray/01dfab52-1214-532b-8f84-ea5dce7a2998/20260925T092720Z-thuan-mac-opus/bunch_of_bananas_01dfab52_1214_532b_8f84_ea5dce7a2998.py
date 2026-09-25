"""Bunch of three bananas hanging from one short square stem.

Symbol plan: the front banana is one closed contour that owns the stem; the
middle and top bananas peek out to its upper left as open outlines whose
edges leave the stem corner and whose blunt tips end on the banana in front.
Every seam meets its neighbour at a real angle, never tangentially, so no
sliver of ink forms. Keyshape SQUARE, centerline box (6,6)-(42,42).
Lucide construction: banana (curved belly, blunt tip, stem cap); re-authored
as a three-fruit bunch following the reference.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "01dfab52-1214-532b-8f84-ea5dce7a2998"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__bunch-of-bananas-batch-010-10/20260925T092530Z-thuan-mac/reference/banana_01dfab52-1214-532b-8f84-ea5dce7a2998.svg"
AUTHOR = "claude-opus-5-5"


class BunchOfBananas(Solo48):
    icon_id = "bunch-of-bananas-batch-010-10"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ("banana bunch",)
    keywords = ("banana", "fruit", "bunch")

    def build(self) -> None:
        crown = (34, 14)
        front_tip = (13, 40)
        middle_join = (23, 33)
        middle_tip = (6, 30)
        top_join = (18, 24)
        top_tip = (6, 14)
        self.add_line("stem", (34, 6), crown)
        # Front banana: a crescent from the crown, down the belly to its tip
        # and back along the inner edge.
        self.path("front", crown, [
            ("C", (39, 16), (42, 21), (42, 27)),
            ("C", (42, 36), (35, 42), (26, 42)),
            ("C", (21, 42), (16, 41), front_tip),
            ("C", (16, 38), (20, 36), middle_join),
            ("C", (29, 29), (33, 22), crown),
        ], closed=True)
        # Middle banana: upper edge from the crown to its tip; its underside
        # disappears behind the front banana.
        self.path("middle", crown, [
            ("C", (30, 20), (24, 23), top_join),
            ("C", (12, 25), (8, 27), middle_tip),
            ("C", (12, 31), (18, 31), middle_join),
        ])
        # Top banana: upper edge from the crown to its tip; its underside
        # disappears behind the middle banana.
        self.path("top", crown, [
            ("C", (27, 17), (13, 18), top_tip),
            ("C", (10, 18), (15, 22), top_join),
        ])
        self.relate("connect", "stem", "front")
        self.relate("connect", "front", "middle")
        self.relate("connect", "front", "top")
        self.relate("connect", "middle", "top")

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
