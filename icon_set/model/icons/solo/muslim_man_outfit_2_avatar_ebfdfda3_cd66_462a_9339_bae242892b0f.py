"""Muslim man outfit 2 avatar: a portrait bust of a man in a kufi (round prayer
cap) and a thobe with a buttoned placket below the collar.

Revision (disapproved, reason not recorded): the rejected drawing gave a bare head
a swept hair lock and drew two long vertical strokes down the body; the original's
identity is the close-fitting kufi across the top of the head and the thobe's
collar with its short centre placket. Both are restored.

Symbol plan: mirror axis x=24. The head is one closed outline: a radius-10 crown
about (24,14) (top 4), straight temples x=14/34 from y=14 to 16 and a radius-10
jaw about (24,16) (chin 26). The kufi is the crown closed by its hem line
(14,14)-(34,14): the cap is as wide as the head, as in the reference. Shoulders
start 4 below the chin (touching ink, avatar rule) at y=30; the collar is the
neckline (18,30)-(30,30) and the placket runs from its centre to (24,38).
Omissions: the kufi's band stitching (a second line inside the cap closes a hole
below the 6-unit minimum) and the sleeve seams (they cannot keep 8 from the
shoulder arcs).
Human reference: icon_set/references/human_ref/user.svg (bust proportions).
Lucide construction: 'user-round' bust.
Keyshape VRECT_L: centerline x 8..40 (shoulders), y 4 (kufi) .. 44.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = "ebfdfda3-cd66-462a-9339-bae242892b0f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__muslim-man-outfit-2-avatar/20260926T175625Z-thuan-mac-1/reference/muslim man outfit_ebfdfda3-cd66-462a-9339-bae242892b0f.svg"
AUTHOR = "claude-opus-5-5"
HUMAN_REFERENCE = "icon_set/references/human_ref/user.svg"

CX, R = 24, 10
CAP_Y, JAW_Y = 14, 16
HEAD_BOTTOM = JAW_Y + R


class MuslimManOutfit2Avatar(Solo48):
    icon_id = "muslim-man-outfit-2-avatar-solo"
    human_construction = "bust"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "avatars"
    aliases = ("muslim-man", "kufi-man", "thobe")
    keywords = ("man", "muslim", "kufi", "taqiyah", "cap", "thobe", "outfit", "avatar", "bust", "portrait")

    def build(self) -> None:
        hl, hr = CX - R, CX + R
        self.add_arc("kufi-left", (hl, CAP_Y), (CX, CAP_Y - R), radius_x=R)
        self.add_arc("kufi-right", (CX, CAP_Y - R), (hr, CAP_Y), radius_x=R)
        self.add_line("temple-right", (hr, CAP_Y), (hr, JAW_Y))
        self.add_arc("jaw-right", (hr, JAW_Y), (CX, HEAD_BOTTOM), radius_x=R)
        self.add_arc("jaw-left", (CX, HEAD_BOTTOM), (hl, JAW_Y), radius_x=R)
        self.add_line("temple-left", (hl, JAW_Y), (hl, CAP_Y))
        self.add_contour("head", "kufi-left", "kufi-right", "temple-right", "jaw-right",
                         "jaw-left", "temple-left", closed=True)
        self.add_line("kufi-hem", (hl, CAP_Y), (hr, CAP_Y))
        self.relate("connect", "head", "kufi-hem")

        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line("body-left-side", (8, 44), (8, 42))
        self.add_arc("body-left-shoulder", (8, 42), (18, top), radius_x=10, radius_y=42 - top)
        self.add_contour("body-left", "body-left-side", "body-left-shoulder")
        self.add_line("body-top", (18, top), (CX, top))
        self.add_line("body-top-right", (CX, top), (30, top))
        self.add_arc("body-right-shoulder", (30, top), (40, 42), radius_x=10, radius_y=42 - top)
        self.add_line("body-right-side", (40, 42), (40, 44))
        self.add_contour("body-right", "body-right-shoulder", "body-right-side")
        self.relate("connect", "body-left", "body-top")
        self.relate("connect", "body-top", "body-top-right")
        self.relate("connect", "body-top-right", "body-right")
        self.add_line("placket", (CX, top), (CX, top + 8))
        self.relate("connect", "placket", "body-top")
        self.relate("connect", "placket", "body-top-right")
        self.relate("connect", "head", "body-top")
        self.relate("connect", "head", "body-top-right")
        self.relate("connect", "head", "placket")
