"""Avatar fire fighter woman: a firefighter's portrait bust - a tall round helmet with
a thin curved brim over a round face, and a protective coat with a chest band and centre fastening.

Symbol plan: mirror symmetry about x=24. Portrait-bust construction (shared human
reference, user.svg proportions): the head is one radius-10 circle about (24,14);
its upper half is the helmet dome (top y=4) and its lower half the face (jaw y=24).
The brim is one thin stroke of four tangent cubics from (8,22) to (40,22): it rises
through the head's side points (14,14)/(34,14) to a crest (24,12) inside the dome,
so it arches across the helmet and droops well past it at both sides. The coat's shoulders start exactly 4 below the jaw
(touching ink), with a chest band on y=42 and a centre fastening.
Revision (reviewer: "Make the helmet taller and rounder, with a thin curved brim"):
the flattened rx16/ry12 helmet on a straight full-width brim is now a round dome
(radius 10, as tall as it is wide) with a thin curved brim.
Omission: the reference's side hair; beside a radius-10 face at the x=8 edge it
cannot keep 8 from the face outline.
Lucide construction: 'user-round' bust; 'hard-hat' dome with brim.
Keyshape VRECT_L: centerline x 8..40 (brim, shoulders), y 4 (helmet) .. 44.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = "3eee532b-a6a4-5e11-9099-320f9bab18ea"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__avatar-fire-fighter-woman/20260926T073832Z-thuan-mac/reference/avatar fire fighter woman_3eee532b-a6a4-5e11-9099-320f9bab18ea.svg"
AUTHOR = "claude-opus-5-5"
HUMAN_REFERENCE = "icon_set/references/human_ref/user.svg"

CX, CY, R = 24, 14, 10
HEAD_BOTTOM = CY + R


class AvatarFireFighterWoman(Solo48):
    icon_id = "fire-fighter-woman-avatar-solo"
    human_construction = "bust"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "avatars"
    aliases = ("firefighter-woman", "fire-fighter")
    keywords = ("avatar", "fire", "fighter", "firefighter", "woman", "helmet", "bust", "portrait")

    def build(self) -> None:
        left, right = (CX - R, CY), (CX + R, CY)
        self.add_arc("helmet-left", left, (CX, CY - R), radius_x=R, sweep=True)
        self.add_arc("helmet-right", (CX, CY - R), right, radius_x=R, sweep=True)
        self.add_arc("face-right", right, (CX, HEAD_BOTTOM), radius_x=R, sweep=True)
        self.add_arc("face-left", (CX, HEAD_BOTTOM), left, radius_x=R, sweep=True)
        self.add_contour("head", "helmet-left", "helmet-right", "face-right", "face-left", closed=True)
        self.add_bezier("brim", (8, 22),
                        ((9, 18.5), (11, 15.5), left),
                        ((17, 12.5), (20, 12), (CX, 12)),
                        ((28, 12), (31, 12.5), right),
                        ((37, 15.5), (39, 18.5), (40, 22)))
        self.relate("connect", "head", "brim")
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
        self.add_line("body-band", (8, 42), (40, 42))
        self.relate("connect", "body-band", "body-left")
        self.relate("connect", "body-band", "body-right")
        self.add_line("body-fastening", (CX, top), (CX, 42))
        self.relate("connect", "body-fastening", "body-top")
        self.relate("connect", "body-fastening", "body-top-right")
        self.relate("connect", "body-fastening", "body-band")
        self.relate("connect", "head", "body-top")
        self.relate("connect", "head", "body-top-right")
