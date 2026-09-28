"""Man indian 2 avatar: a portrait bust of an Indian man in a wrapped turban and a
wrap-front kurta.

Revision (disapproved, reason not recorded): the rejected drawing was a bare round
head with a moustache; the original's identity is the wrapped turban that is wider
than the face, with its folds crossing to a point over the forehead, and the
crossed kurta collar. The turban and collar are restored.

Symbol plan: mirror axis x=24 for turban, face and shoulders. The turban is one
closed contour: a radius-12 dome about (24,16) (top y=4, sides x=12/36) whose lower
edge steps in at 45 degrees to the temples (16,20)/(32,20) and rises 3:4 to a
point (24,14) over the forehead, the crossing folds of the wrap (construction of
the library's turban-wearer). The face is a radius-8 jaw arc between the temples
(bottom 28); shoulders start 4 below it (touching ink, avatar rule) at y=32. The
kurta's overlapping lapel runs 1:2 from the chin contact (24,32) down-left to
(20,40), the reference's wrap direction (deliberate asymmetry).
Omissions: the chin beard (an arch inside the radius-8 face cannot keep 8 from
both the jaw and the turban point) and the turban's inner fold line (splits the
dome into regions narrower than the 6-unit hole minimum).
Human reference: icon_set/references/human_ref/user.svg (bust proportions).
Lucide construction: 'user-round' bust; no turban glyph in Lucide.
Keyshape VRECT_L: centerline x 8..40 (shoulders), y 4 (turban) .. 44.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = "ec6a97bf-8b79-5217-9903-4d323ef660ad"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__man-indian-2-avatar/20260926T175625Z-thuan-mac-1/reference/man indian_ec6a97bf-8b79-5217-9903-4d323ef660ad.svg"
AUTHOR = "claude-opus-5-5"
HUMAN_REFERENCE = "icon_set/references/human_ref/user.svg"

CX = 24
DOME_CY, DOME_R = 16, 12
TEMPLE_Y, FACE_R = 20, 8
HEAD_BOTTOM = TEMPLE_Y + FACE_R


class ManIndian2Avatar(Solo48):
    icon_id = "man-indian-2-avatar"
    human_construction = "bust"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "avatars"
    aliases = ("indian-man", "turban-man")
    keywords = ("man", "indian", "turban", "kurta", "avatar", "bust", "portrait")

    def build(self) -> None:
        dl, dr = (CX - DOME_R, DOME_CY), (CX + DOME_R, DOME_CY)
        tl, tr = (CX - FACE_R, TEMPLE_Y), (CX + FACE_R, TEMPLE_Y)
        self.add_arc("dome-left", dl, (CX, DOME_CY - DOME_R), radius_x=DOME_R)
        self.add_arc("dome-right", (CX, DOME_CY - DOME_R), dr, radius_x=DOME_R)
        self.add_line("wrap-right", dr, tr)
        self.add_line("fold-right", tr, (CX, 14))
        self.add_line("fold-left", (CX, 14), tl)
        self.add_line("wrap-left", tl, dl)
        self.add_contour("turban", "dome-left", "dome-right", "wrap-right", "fold-right", "fold-left", "wrap-left", closed=True)
        self.add_arc("jaw", tr, tl, radius_x=FACE_R, sweep=True)
        self.relate("connect", "turban", "jaw")

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
