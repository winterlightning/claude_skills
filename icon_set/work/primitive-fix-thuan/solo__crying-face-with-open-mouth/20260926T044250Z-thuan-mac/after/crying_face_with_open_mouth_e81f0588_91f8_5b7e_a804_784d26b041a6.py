"""A crying face: a round face with closed eyes, a tear running from one eye and an open, downturned mouth.

Symbol plan: the head is one circle (r20). The eyes are two closed-eye arcs (r3 half
circles, mirrored about x=24). A tear falls as a short stroke from the right eye's outer
corner (shared endpoint). The mouth is an open D turned down: a half-circle arch (r6)
over a flat lower lip. Everything stays within radius 12 of the centre, 8+ from the rim.
The reference's worried eyebrows are dropped: brows 8 above the eyes and 8 inside the
rim do not fit.
Lucide construction: 'frown' face construction (circle, eyes, mouth).
Keyshape CIRCLE: centerline radius 20 about (24,24).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e81f0588-91f8-5b7e-a804-784d26b041a6"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__crying-face-with-open-mouth/20260926T044250Z-thuan-mac/reference/sad crying_e81f0588-91f8-5b7e-a804-784d26b041a6.svg"
AUTHOR = "claude-opus-5-5"


class CryingFaceWithOpenMouth(Solo48):
    icon_id = "crying-face-with-open-mouth"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/emotion"
    aliases = ("sad crying", "crying face", "sobbing")
    keywords = ("crying", "sad", "tear", "upset", "sob", "unhappy", "emoji", "face", "grief")

    def build(self) -> None:
        c, r = 24, 20
        self.add_arc("head-top", (c - r, c), (c + r, c), radius_x=r)
        self.add_arc("head-bottom", (c + r, c), (c - r, c), radius_x=r)
        self.add_contour("head", "head-top", "head-bottom", closed=True)
        ey = 19
        self.add_arc("eye-l", (14, ey), (20, ey), radius_x=3)
        self.add_arc("eye-r", (28, ey), (34, ey), radius_x=3)
        self.add_line("tear", (34, ey), (34, 24))
        self.relate("connect", "eye-r", "tear")
        my, mr = 34, 6
        self.add_arc("mouth-arch", (c - mr, my), (c + mr, my), radius_x=mr)
        self.add_line("mouth-lip", (c + mr, my), (c - mr, my))
        self.add_contour("mouth", "mouth-arch", "mouth-lip", closed=True)
