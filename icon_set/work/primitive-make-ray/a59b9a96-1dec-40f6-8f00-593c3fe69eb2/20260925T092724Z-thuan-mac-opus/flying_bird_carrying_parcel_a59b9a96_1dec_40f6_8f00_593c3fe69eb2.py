"""Dropshipper: a dove flying right with its wing raised, carrying a taped
parcel that hangs from its foot at lower left.

Symbol plan: the dove's body is one closed outline (beak, crown, nape,
back, pointed tail, belly, chest) through integer nodes with tangent
cubics; the raised wing is an open run from the nape node to a tip and back
to a back node, so it shares both ends with the body. A foot stroke drops
from the lowest belly node to the parcel's top-right corner. The parcel is a
closed square with one tape stroke from its top edge, 8 from each side.
Deliberately asymmetric (flight to the right).
Keyshape SQUARE, centerline box (6,6)-(42,42).
Lucide construction: bird (dove silhouette with raised wing) and package
(box with a tape seam).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a59b9a96-1dec-40f6-8f00-593c3fe69eb2"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__flying-bird-carrying-taped-parcel/20260925T092530Z-thuan-mac/reference/dropshipper bird box_a59b9a96-1dec-40f6-8f00-593c3fe69eb2.svg"
AUTHOR = "claude-opus-5-5"


class FlyingBirdCarryingParcel(Solo48):
    icon_id = "flying-bird-carrying-taped-parcel"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shopping"
    aliases = ("dropshipper", "bird delivery", "parcel delivery")
    keywords = ("bird", "dove", "parcel", "package", "delivery", "dropship", "box")

    def build(self) -> None:
        nape, back, belly = (32, 13), (26, 16), (32, 26)
        self.path("dove", (42, 14), [
            ("C", (39, 10), (38, 9), (36, 9)),         # beak to crown
            ("C", (34, 9), (33, 11), nape),            # crown to nape
            ("C", (30, 15), (28, 16), back),           # nape to back
            ("C", (20, 17), (13, 17), (8, 15)),        # back to tail tip
            ("C", (13, 21), (24, 25), belly),          # tail underside to belly
            ("C", (35, 26), (37, 23), (38, 19)),       # belly to chest
            ("C", (39, 17), (40, 15), (42, 14)),       # chest to beak
        ], closed=True)
        self.path("wing", nape, [
            ("C", (29, 8), (23, 6), (14, 6)),          # leading edge to tip
            ("C", (16, 11), (20, 15), back),           # trailing edge
        ])
        self.relate("connect", "dove", "wing")
        corner = (22, 32)
        self.add_line("foot", belly, corner)
        self.relate("connect", "dove", "foot")
        self.add_polyline("parcel", (6, 32), (14, 32), corner, (22, 42), (6, 42), closed=True)
        self.add_line("tape", (14, 32), (14, 34))
        self.relate("connect", "parcel", "foot")
        self.relate("connect", "parcel", "tape")

    def path(self, name, start, commands, closed=False):
        members = []
        here = start
        for index, (kind, *args) in enumerate(commands):
            member = f"{name}-{index + 1}"
            self.add_bezier(member, here, (args[0], args[1], args[2]))
            here = args[2]
            members.append(member)
        self.add_contour(name, *members, closed=closed)
