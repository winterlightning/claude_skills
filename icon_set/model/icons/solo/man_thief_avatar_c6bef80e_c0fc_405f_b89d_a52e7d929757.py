"""Man thief avatar: a portrait bust of a thief in a balaclava -- the knitted mask
covers the whole head and neck, leaving only holes for the eyes and mouth.

Revision (disapproved, reason not recorded): the rejected drawing was a round head
with a pair of large goggle-like rings and a crossbar, over a shirt with a chest
band; it read as goggles, not a mask. The original is a balaclava: one continuous
head-and-neck silhouette with two eye holes and a mouth hole. That is restored.

Symbol plan: mirror axis x=24. The mask is one open contour: a radius-13 head
circle about (24,17) (top 4) running round the crown to the 5-12-13 points
(19,29)/(29,29), where it turns straight down into the neck (to y=33) and out
over radius-11 shoulders to (8,44)/(40,44). No chin line: the mask flows into the
neck, as in the reference, so there is no separate head/body contact; a hem
line (19,33)-(29,33) marks where the mask tucks into the collar. Eye holes
are dots at (20,15)/(28,15) and the mouth hole a dot at (24,22): every dot is 8+
from the others and from the mask outline (the nearest outline points to the
mouth are the neck corners, 8.6 away).
Omissions: the eye/mouth hole outlines (rings cannot keep 8 from each other in a
26-wide head) and the chin seam.
Human reference: icon_set/references/human_ref/user.svg (bust proportions).
Lucide construction: 'user-round' bust; no balaclava glyph in Lucide.
Keyshape VRECT_L: centerline x 8..40 (shoulders), y 4 (crown) .. 44.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "c6bef80e-c0fc-405f-b89d-a52e7d929757"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__man-thief-avatar/20260926T175625Z-thuan-mac-1/reference/man thief_c6bef80e-c0fc-405f-b89d-a52e7d929757.svg"
AUTHOR = "claude-opus-5-5"
HUMAN_REFERENCE = "icon_set/references/human_ref/user.svg"

CX, CY, R = 24, 17, 13
NECK_L, NECK_R, NECK_TOP, NECK_BOTTOM = 19, 29, 29, 33


class ManThiefAvatar(Solo48):
    icon_id = "man-thief-avatar-solo"
    human_construction = "bust"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "avatars"
    aliases = ("burglar", "robber", "balaclava-man")
    keywords = ("man", "thief", "burglar", "robber", "balaclava", "mask", "crime", "avatar", "bust", "portrait")

    def build(self) -> None:
        self.add_arc("left-shoulder", (8, 44), (NECK_L, NECK_BOTTOM), radius_x=11)
        self.add_line("neck-left", (NECK_L, NECK_BOTTOM), (NECK_L, NECK_TOP))
        self.add_arc("mask-left", (NECK_L, NECK_TOP), (CX - R, CY), radius_x=R)
        self.add_arc("mask-crown-left", (CX - R, CY), (CX, CY - R), radius_x=R)
        self.add_arc("mask-crown-right", (CX, CY - R), (CX + R, CY), radius_x=R)
        self.add_arc("mask-right", (CX + R, CY), (NECK_R, NECK_TOP), radius_x=R)
        self.add_line("neck-right", (NECK_R, NECK_TOP), (NECK_R, NECK_BOTTOM))
        self.add_arc("right-shoulder", (NECK_R, NECK_BOTTOM), (40, 44), radius_x=11)
        self.add_contour("mask", "left-shoulder", "neck-left", "mask-left", "mask-crown-left",
                         "mask-crown-right", "mask-right", "neck-right", "right-shoulder")
        # The mask's hem where it tucks into the collar.
        self.add_line("hem", (NECK_L, NECK_BOTTOM), (NECK_R, NECK_BOTTOM))
        self.relate("connect", "mask", "hem")
        self.add_dot("eye-left", (20, 15))
        self.add_dot("eye-right", (28, 15))
        self.add_dot("mouth", (CX, 22))
