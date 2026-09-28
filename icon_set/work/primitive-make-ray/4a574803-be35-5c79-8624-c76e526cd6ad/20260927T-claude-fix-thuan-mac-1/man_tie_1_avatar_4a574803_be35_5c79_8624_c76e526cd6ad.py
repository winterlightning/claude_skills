"""Man tie 1 avatar: a portrait bust of a businessman -- a plain round head over
shoulders with a necktie hanging from the collar.

Revision (disapproved, reason not recorded): the rejected drawing added a swept
hair lock the original does not have, and its "tie" was only a V-neck running
into a single line, which reads as a Y, not a tie. The original shows a plain
round head and a real tie: a blade that widens below the knot and ends in a
point. Both are restored.

Symbol plan: mirror axis x=24. Head is a radius-10 circle about (24,14) (top 4,
chin 24). Shoulders start 4 below the chin (touching ink, avatar rule) at y=28 with a
wide collar line (14,28)-(34,28) and short rx-6 shoulder rounds, the reference's
square-shouldered jacket.
The tie hangs from the collar at (24,28) as one closed kite: widest at (17,37)/
(31,37), pointed tip at (24,44), so its diagonals are 14 x 16 and its opening
clears the 6-unit hole minimum.
Omissions: the shirt collar points and the knot's own outline (both close holes
under the neckline below the 6-unit minimum).
Human reference: icon_set/references/human_ref/user.svg (bust proportions).
Lucide construction: 'user-round' bust.
Keyshape VRECT_L: centerline x 8..40 (shoulders), y 4 (head) .. 44 (shoulders, tie tip).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = "4a574803-be35-5c79-8624-c76e526cd6ad"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__man-tie-1-avatar/20260926T175625Z-thuan-mac-1/reference/man tie_4a574803-be35-5c79-8624-c76e526cd6ad.svg"
AUTHOR = "claude-opus-5-5"
HUMAN_REFERENCE = "icon_set/references/human_ref/user.svg"

CX, CY, R = 24, 14, 10
HEAD_BOTTOM = CY + R


class ManTie1Avatar(Solo48):
    icon_id = "man-tie-1-avatar"
    human_construction = "bust"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "avatars"
    aliases = ("businessman", "office-man", "man-with-tie")
    keywords = ("man", "tie", "necktie", "business", "office", "avatar", "bust", "portrait")

    def build(self) -> None:
        left, right = (CX - R, CY), (CX + R, CY)
        self.add_arc("head-top-left", left, (CX, CY - R), radius_x=R)
        self.add_arc("head-top-right", (CX, CY - R), right, radius_x=R)
        self.add_arc("head-bottom-right", right, (CX, HEAD_BOTTOM), radius_x=R)
        self.add_arc("head-bottom-left", (CX, HEAD_BOTTOM), left, radius_x=R)
        self.add_contour("head", "head-top-left", "head-top-right", "head-bottom-right", "head-bottom-left", closed=True)

        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line("body-left-side", (8, 44), (8, 42))
        self.add_arc("body-left-shoulder", (8, 42), (14, top), radius_x=6, radius_y=42 - top)
        self.add_contour("body-left", "body-left-side", "body-left-shoulder")
        self.add_line("body-top", (14, top), (CX, top))
        self.add_line("body-top-right", (CX, top), (34, top))
        self.add_arc("body-right-shoulder", (34, top), (40, 42), radius_x=6, radius_y=42 - top)
        self.add_line("body-right-side", (40, 42), (40, 44))
        self.add_contour("body-right", "body-right-shoulder", "body-right-side")
        self.relate("connect", "body-left", "body-top")
        self.relate("connect", "body-top", "body-top-right")
        self.relate("connect", "body-top-right", "body-right")
        self.relate("connect", "head", "body-top")
        self.relate("connect", "head", "body-top-right")

        self.add_polyline("tie", (CX, top), (CX + 7, 37), (CX, 44), (CX - 7, 37), closed=True)
        self.relate("connect", "tie", "body-top")
        self.relate("connect", "tie", "body-top-right")
        self.relate("connect", "tie", "head")
