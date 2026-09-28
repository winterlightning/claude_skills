"""Man japan avatar: a portrait bust of a man in a conical straw hat (kasa) and a
wrap-front robe.

Revision (disapproved, reason not recorded): the rejected drawing was a generic
head with swept hair and a rounded neckline; the original's identity is the wide
conical hat that shades the face and the crossed robe collar. Both are restored.

Symbol plan: mirror axis x=24 for hat, face and shoulders. The hat is one closed
triangle, apex (24,4), brim (8,16)-(40,16); its sides run 3:4 (a 12x16 rise). The
face is a radius-8 jaw arc hanging from the brim at (16,16)/(32,16) (bottom 24).
Shoulders start 4 below the jaw (touching ink, avatar rule) at y=28. The robe's
overlapping lapel is one 1:2 stroke from the chin contact point (24,28) down-left
to (20,36), the direction of the reference; the deliberate asymmetry is the wrap front of the reference.
Omissions: the under-lapel of the crossed collar (it would close a hole under the
neckline narrower than the 6-unit minimum).
Human reference: icon_set/references/human_ref/user.svg (bust proportions).
Lucide construction: 'user-round' bust; 'triangle' for the hat.
Keyshape VRECT_L: centerline x 8..40 (brim, shoulders), y 4 (apex) .. 44.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = "3c937449-3b63-4517-a7b7-4088598ee58d"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__man-japan-avatar/20260926T175625Z-thuan-mac-1/reference/man japan_3c937449-3b63-4517-a7b7-4088598ee58d.svg"
AUTHOR = "claude-opus-5-5"
HUMAN_REFERENCE = "icon_set/references/human_ref/user.svg"

CX = 24
BRIM_Y, FACE_R = 16, 8
HEAD_BOTTOM = BRIM_Y + FACE_R


class ManJapanAvatar(Solo48):
    icon_id = "man-japan-avatar"
    human_construction = "bust"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "avatars"
    aliases = ("japanese-man", "kasa-hat-man")
    keywords = ("man", "japan", "japanese", "conical", "hat", "kasa", "kimono", "avatar", "bust", "portrait")

    def build(self) -> None:
        fl, fr = (CX - FACE_R, BRIM_Y), (CX + FACE_R, BRIM_Y)
        self.add_line("hat-left", (8, BRIM_Y), (CX, 4))
        self.add_line("hat-right", (CX, 4), (40, BRIM_Y))
        self.add_line("brim-right", (40, BRIM_Y), fr)
        self.add_line("brim-mid", fr, fl)
        self.add_line("brim-left", fl, (8, BRIM_Y))
        self.add_contour("hat", "hat-left", "hat-right", "brim-right", "brim-mid", "brim-left", closed=True)
        self.add_arc("jaw", fr, fl, radius_x=FACE_R, sweep=True)
        self.relate("connect", "hat", "jaw")

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
        self.add_line("lapel", (CX, top), (CX - 4, top + 8))
        self.relate("connect", "lapel", "body-top")
        self.relate("connect", "lapel", "body-top-right")
        self.relate("connect", "jaw", "lapel")
        self.relate("connect", "jaw", "body-top")
        self.relate("connect", "jaw", "body-top-right")
