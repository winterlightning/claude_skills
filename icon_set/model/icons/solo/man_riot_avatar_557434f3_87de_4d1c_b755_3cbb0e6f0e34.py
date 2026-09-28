"""Man riot avatar: a rioter in a pulled-up hood with a bandana mask covering the
lower face, leaving only an eye band showing.

Revision (disapproved, reason not recorded): the rejected drawing was a plain ring
head with a square knob on top over T-shaped shoulders; the original's identity
is the hood framing the face and the pointed bandana over the nose and mouth.
Both are restored.

Symbol plan: mirror axis x=24. The hood is one open contour: a radius-16 crown
about (24,20) (top 4, sides x=8/40) falling straight to the bottom edge (44), hood
and shoulders in one silhouette as in the reference. The face opening is a
closed shield inside it, 10 from the hood: a radius-6 brow arc about (24,20)
(top 14), straight cheeks x=18/30 down to y=28, and two radius-15 (9-12-15) arcs
meeting in a pointed chin at (24,40). The bandana's top edge (18,24)-(30,24)
splits the opening into the eye band (14-24) and the pointed mask below.
Omissions: the eyes (no 8-unit room in the 10-high eye band) and the shoulder
flare below the hood (the hood already fills the keyshape width).
Human reference: icon_set/references/human_ref/user.svg (bust proportions).
Lucide construction: 'user-round' crown; no hood glyph in Lucide.
Keyshape VRECT_L: centerline x 8..40 (hood), y 4 (crown) .. 44.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "557434f3-87de-4d1c-b755-3cbb0e6f0e34"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__man-riot-avatar/20260926T175625Z-thuan-mac-1/reference/man riot_557434f3-87de-4d1c-b755-3cbb0e6f0e34.svg"
AUTHOR = "claude-opus-5-5"
HUMAN_REFERENCE = "icon_set/references/human_ref/user.svg"

CX, CY = 24, 20
HOOD_R, FACE_R = 16, 6
MASK_Y, CHEEK_BOTTOM, CHIN_Y, CHIN_R = 24, 28, 40, 15


class ManRiotAvatar(Solo48):
    icon_id = "man-riot-avatar-solo"
    human_construction = "bust"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "avatars"
    aliases = ("rioter", "hooded-protester", "masked-man")
    keywords = ("man", "riot", "rioter", "protest", "hood", "hoodie", "bandana", "mask", "avatar", "bust")

    def build(self) -> None:
        hl, hr = CX - HOOD_R, CX + HOOD_R
        self.add_line("hood-left-side", (hl, 44), (hl, CY))
        self.add_arc("hood-left", (hl, CY), (CX, CY - HOOD_R), radius_x=HOOD_R)
        self.add_arc("hood-right", (CX, CY - HOOD_R), (hr, CY), radius_x=HOOD_R)
        self.add_line("hood-right-side", (hr, CY), (hr, 44))
        self.add_contour("hood", "hood-left-side", "hood-left", "hood-right", "hood-right-side")

        fl, fr = CX - FACE_R, CX + FACE_R
        self.add_arc("brow-left", (fl, CY), (CX, CY - FACE_R), radius_x=FACE_R)
        self.add_arc("brow-right", (CX, CY - FACE_R), (fr, CY), radius_x=FACE_R)
        self.add_line("cheek-right-upper", (fr, CY), (fr, MASK_Y))
        self.add_line("cheek-right-lower", (fr, MASK_Y), (fr, CHEEK_BOTTOM))
        self.add_arc("chin-right", (fr, CHEEK_BOTTOM), (CX, CHIN_Y), radius_x=CHIN_R)
        self.add_arc("chin-left", (CX, CHIN_Y), (fl, CHEEK_BOTTOM), radius_x=CHIN_R)
        self.add_line("cheek-left-lower", (fl, CHEEK_BOTTOM), (fl, MASK_Y))
        self.add_line("cheek-left-upper", (fl, MASK_Y), (fl, CY))
        self.add_contour("face", "brow-left", "brow-right", "cheek-right-upper", "cheek-right-lower",
                         "chin-right", "chin-left", "cheek-left-lower", "cheek-left-upper", closed=True)
        self.add_line("mask-top", (fl, MASK_Y), (fr, MASK_Y))
        self.relate("connect", "face", "mask-top")
