"""A dachshund face: a broad domed head with long ears hanging to either side of the chin.

Symbol plan: mirrored about x=24. One closed outline: a broad half-elliptical dome (rx 20,
ry 14 about (24,22)) over short straight sides, and a bottom edge of three lobes - the two ear lobes at the
bottom corners and a shallower chin lobe between them - meeting at two notches (17,35)
and (31,35). From each notch an inner ear line rises into the head, separating ear from
face, as in the reference. The nose is a single dot on the axis, 8.9 from the ear lines.
Lucide construction: 'dog' - head silhouette of few cubic runs with hanging ear lobes.
Keyshape HRECT_L: centerline x 4..44 (head sides), y 8..40 (dome top, ear lobes).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "44442ee3-de41-53ab-af82-3e69c47a0ecc"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__dachshund-face/20260926T044250Z-thuan-mac/reference/dachshund_44442ee3-de41-53ab-af82-3e69c47a0ecc.svg"
AUTHOR = "claude-opus-5-5"


class DachshundFace(Solo48):
    icon_id = "dachshund-face"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ("dachshund", "sausage-dog", "wiener-dog")
    keywords = ("dog", "dachshund", "sausage-dog", "wiener", "breed", "pet", "face", "floppy-ears", "puppy")

    def build(self) -> None:
        self.add_arc("dome", (4, 22), (44, 22), radius_x=20, radius_y=14, sweep=True)
        self.add_line("side-right", (44, 22), (44, 32))
        self.add_bezier("ear-right", (44, 32), ((44, 37), (42, 40), (38, 40)), ((34, 40), (32, 38), (31, 35)))
        self.add_bezier("chin", (31, 35), ((30, 37), (27, 38), (24, 38)), ((21, 38), (18, 37), (17, 35)))
        self.add_bezier("ear-left", (17, 35), ((16, 38), (14, 40), (10, 40)), ((6, 40), (4, 37), (4, 32)))
        self.add_line("side-left", (4, 32), (4, 22))
        self.add_contour("head", "dome", "side-right", "ear-right", "chin", "ear-left", "side-left", closed=True)
        self.add_line("ear-line-left", (17, 35), (15, 24))
        self.add_line("ear-line-right", (31, 35), (33, 24))
        self.relate("connect", "head", "ear-line-left")
        self.relate("connect", "head", "ear-line-right")
        self.add_dot("nose", (24, 25))
