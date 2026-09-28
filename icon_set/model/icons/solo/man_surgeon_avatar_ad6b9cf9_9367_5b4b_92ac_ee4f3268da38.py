"""Man surgeon avatar: a portrait bust of a surgeon in a scrub cap and a surgical
face mask.

Revision (disapproved, reason not recorded): the rejected drawing was a square
bandana-like cap with side ties over a bare jaw, which reads as a bandit; the
original's identity is the rounded scrub cap and the face mask covering the lower
face, with the eyes left open between them. Both are restored.

Symbol plan: mirror axis x=24. The scrub cap is a closed half-disc: a radius-10
dome about (24,14) (top y=4) on a straight hem (14,14)-(34,14). The mask is a
closed half-disc below it: a straight top edge (16,23)-(32,23) over a radius-8
jaw arc (bottom 31). Its top edge runs on as ear straps to x=10/38.
The open 9-unit band between hem and mask is the eye line.
Shoulders start 4 below the mask's chin (touching ink, avatar rule) at y=35.
Omissions: the face's side outline between cap and mask (with it, the eye band is
a closed 4-unit hole, below the 6-unit minimum), the mask pleats and the scrubs'
V-neck (a V under the neckline closes a triangle below the hole minimum).
Human reference: icon_set/references/human_ref/user.svg (bust proportions).
Lucide construction: 'user-round' bust; 'hard-hat' style dome for the cap.
Keyshape VRECT_L: centerline x 8..40 (shoulders), y 4 (cap) .. 44.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = "ad6b9cf9-9367-5b4b-92ac-ee4f3268da38"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__man-surgeon-avatar/20260926T175625Z-thuan-mac-1/reference/man surgeon_ad6b9cf9-9367-5b4b-92ac-ee4f3268da38.svg"
AUTHOR = "claude-opus-5-5"
HUMAN_REFERENCE = "icon_set/references/human_ref/user.svg"

CX = 24
CAP_CY, CAP_R = 14, 10
MASK_Y, MASK_R = 23, 8
HEAD_BOTTOM = MASK_Y + MASK_R


class ManSurgeonAvatar(Solo48):
    icon_id = "man-surgeon-avatar-solo"
    human_construction = "bust"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "avatars"
    aliases = ("surgeon", "doctor-mask")
    keywords = ("man", "surgeon", "doctor", "mask", "scrub", "cap", "medical", "avatar", "bust", "portrait")

    def build(self) -> None:
        self.add_arc("cap-left", (CX - CAP_R, CAP_CY), (CX, CAP_CY - CAP_R), radius_x=CAP_R)
        self.add_arc("cap-right", (CX, CAP_CY - CAP_R), (CX + CAP_R, CAP_CY), radius_x=CAP_R)
        self.add_line("cap-hem", (CX + CAP_R, CAP_CY), (CX - CAP_R, CAP_CY))
        self.add_contour("cap", "cap-left", "cap-right", "cap-hem", closed=True)

        ml, mr = (CX - MASK_R, MASK_Y), (CX + MASK_R, MASK_Y)
        self.add_line("mask-top", ml, mr)
        self.add_arc("mask-jaw", mr, ml, radius_x=MASK_R)
        self.add_contour("mask", "mask-top", "mask-jaw", closed=True)
        self.add_line("strap-left", ml, (CX - MASK_R - 6, MASK_Y))
        self.add_line("strap-right", mr, (CX + MASK_R + 6, MASK_Y))
        self.relate("connect", "mask", "strap-left")
        self.relate("connect", "mask", "strap-right")

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
        self.relate("connect", "mask", "body-top")
        self.relate("connect", "mask", "body-top-right")
