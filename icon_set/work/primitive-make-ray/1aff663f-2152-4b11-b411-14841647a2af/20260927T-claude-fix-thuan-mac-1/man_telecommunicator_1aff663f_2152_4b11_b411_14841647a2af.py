"""Man telecommunicator avatar: a portrait bust of a call-centre operator wearing a
headset -- an ear cup on the right side of the head with a microphone boom
reaching across the cheek toward the mouth.

Revision (disapproved, reason not recorded): the rejected drawing pushed two
horizontal bars straight through the head and hung a tie line under the chin, so
the headset did not read; the original shows one rounded ear cup covering the
right ear and a boom running from it along the face. Both are restored.

Symbol plan: face is a radius-10 circle about (24,14) (top 4, jaw 24), on the
body axis so the jaw/shoulder avatar contact certifies. Its right arc between
(32,8) and (32,20) is covered by the ear cup: flat edges to x=34 and a radius-6
back about (34,14) reaching x=40 (the cup is open to the face, so it closes no
narrow hole). The boom is one cubic from the cup's lower corner (32,20) curving
up-left to end free at the mouth (24,15), 9 from every face edge. Shoulders are
the shared bust, 4 below the jaw (touching ink) at y=28. The cup on the right is
the reference's deliberate asymmetry.
Omissions: the swept hair fringe and headband (neither keeps 8 from the boom\nor the face outline inside a radius-10 head).
Human reference: icon_set/references/human_ref/user.svg (bust proportions).
Lucide construction: 'user-round' bust; 'headset' ear cup and boom.
Keyshape VRECT_L: centerline x 8..40 (shoulders, cup), y 4 (head) .. 44.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = "1aff663f-2152-4b11-b411-14841647a2af"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__man-telecommunicator-1-1-avatar/20260926T175625Z-thuan-mac-1/reference/man telecommunicator_1aff663f-2152-4b11-b411-14841647a2af.svg"
AUTHOR = "claude-opus-5-5"
HUMAN_REFERENCE = "icon_set/references/human_ref/user.svg"

HX, HY, R = 24, 14, 10
HEAD_BOTTOM = HY + R
BOOM_Y = 15


class ManTelecommunicator11Avatar(Solo48):
    icon_id = "man-telecommunicator-1-1-avatar"
    human_construction = "bust"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "avatars"
    aliases = ("call-center-operator", "headset-man", "telephone-operator")
    keywords = ("man", "telecommunicator", "operator", "headset", "call", "support", "avatar", "bust", "portrait")

    def build(self) -> None:
        # Face circle about (24,14); its right arc between (32,8) and (32,20)
        # is covered by the ear cup: flat top/bottom to x=34 and a radius-6
        # back about (34,14) reaching x=40.
        self.add_arc("face-lower-right", (32, 20), (HX, HEAD_BOTTOM), radius_x=R)
        self.add_arc("face-lower-left", (HX, HEAD_BOTTOM), (HX - R, HY), radius_x=R)
        self.add_arc("face-upper-left", (HX - R, HY), (HX, HY - R), radius_x=R)
        self.add_arc("face-upper-right", (HX, HY - R), (32, 8), radius_x=R)
        self.add_line("cup-top", (32, 8), (34, 8))
        self.add_arc("cup-back", (34, 8), (34, 20), radius_x=6)
        self.add_line("cup-bottom", (34, 20), (32, 20))
        self.add_contour("head", "face-lower-right", "face-lower-left", "face-upper-left",
                         "face-upper-right", "cup-top", "cup-back", "cup-bottom", closed=True)
        # Boom: from the cup's lower corner, curving up-left to the mouth.
        self.add_bezier("boom", (32, 20), ((30, 18), (27, 16), (HX, 15)))
        self.relate("connect", "head", "boom")

        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line("body-left-side", (8, 44), (8, 42))
        self.add_arc("body-left-shoulder", (8, 42), (18, top), radius_x=10, radius_y=42 - top)
        self.add_contour("body-left", "body-left-side", "body-left-shoulder")
        self.add_line("body-top", (18, top), (HX, top))
        self.add_line("body-top-right", (HX, top), (30, top))
        self.add_arc("body-right-shoulder", (30, top), (40, 42), radius_x=10, radius_y=42 - top)
        self.add_line("body-right-side", (40, 42), (40, 44))
        self.add_contour("body-right", "body-right-shoulder", "body-right-side")
        self.relate("connect", "body-left", "body-top")
        self.relate("connect", "body-top", "body-top-right")
        self.relate("connect", "body-top-right", "body-right")
        self.relate("connect", "head", "body-top")
        self.relate("connect", "head", "body-top-right")
