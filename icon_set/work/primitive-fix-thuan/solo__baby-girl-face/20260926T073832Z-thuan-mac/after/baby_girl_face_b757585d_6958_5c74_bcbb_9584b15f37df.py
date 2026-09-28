"""Baby girl face: a round baby face with small ears and a symmetrical bow above the
head.

Symbol plan: mirror symmetry about x=24. The face is a radius-13 circle about
(24,31), split at the ear points (12,26)/(12,36) and (36,26)/(36,36) (integer points
of that circle) and at the top and chin. The ears are half ellipses (rx 4, ry 5)
bulging outward. The bow is a bowtie: two triangular loops sharing the knot vertex
(24,8), each flaring to an 8-tall outer edge at the canvas side; its lower edges
stay 9+ from the face and the knot 10 above the crown. Two dot eyes sit 8 apart
at y=30, each 8.9 from the outline.
Revision (reviewer: "Add a symmetrical bow at the top. Make the circle face"): the
egg-shaped face is now a circle, and a mirrored bow sits on top.
Omission: the reference's closed-eye arcs and smile; inside a radius-13 face only
two dots keep 8+ from the outline and from each other.
Lucide construction: 'baby' face circle with dot eyes; bowtie as in 'bow-tie'-style
double triangle.
Keyshape VRECT_L: centerline x 8 (bow, ears) .. 40, y 4 (bow) .. 44 (chin).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b757585d-6958-5c74-bcbb-9584b15f37df"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__baby-girl-face/20260926T073832Z-thuan-mac/reference/baby girl_b757585d-6958-5c74-bcbb-9584b15f37df.svg"
AUTHOR = "claude-opus-5-5"

KNOT = (24, 8)


def mx(p):
    return (48 - p[0], p[1])


class BabyGirlFace(Solo48):
    icon_id = "baby-girl-face"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/family"
    aliases = ("baby-girl",)
    keywords = ("baby", "girl", "face", "bow", "infant", "child", "newborn")

    def build(self) -> None:
        r = 13
        self.add_arc("crown-right", (24, 18), (36, 26), radius_x=r, sweep=True)
        self.add_arc("ear-right", (36, 26), (36, 36), radius_x=4, radius_y=5, sweep=True)
        self.add_arc("cheek-right", (36, 36), (24, 44), radius_x=r, sweep=True)
        self.add_arc("cheek-left", (24, 44), (12, 36), radius_x=r, sweep=True)
        self.add_arc("ear-left", (12, 36), (12, 26), radius_x=4, radius_y=5, sweep=True)
        self.add_arc("crown-left", (12, 26), (24, 18), radius_x=r, sweep=True)
        self.add_contour("face", "crown-right", "ear-right", "cheek-right", "cheek-left",
                         "ear-left", "crown-left", closed=True)
        self.add_polyline("bow-left", KNOT, (8, 4), (8, 12), closed=True)
        self.add_polyline("bow-right", KNOT, mx((8, 4)), mx((8, 12)), closed=True)
        self.relate("connect", "bow-left", "bow-right")
        self.add_dot("eye-left", (20, 30))
        self.add_dot("eye-right", (28, 30))
