"""Step uncle: a user bust (round head over smooth shoulders) with a small
relation badge circle resting on the right shoulder.

Symbol plan: shared human user bust (human_ref/user.svg): head circle r=9 at
(24,13), exact 8-unit centerline gap to the flat shoulder top at y=30, smooth
cubic shoulders; the right shoulder ends on the badge circle at an integer
point of its radius-5 (3-4-5) circle, a declared connection.
Keyshape VRECT_L: shoulder x=8, badge right x=40, head top y=4, base y=44.
Lucide construction: user / user-round (circle head, arched shoulders) and
circle for the badge.
Revision of the rejected drawing ("Bad stroke drawn"): the old drawing used a
flat bottom bar and a badge joined by a tangent smear; here the bust follows
the shared user reference and the badge meets the shoulder cleanly.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "eb0291a2-d110-4e0e-9cb6-552c49ef98d5"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__step-uncle/20260925T092544Z-thuan-mac/reference/step uncle_eb0291a2-d110-4e0e-9cb6-552c49ef98d5.svg"
AUTHOR = "claude-opus-5-5"

HEAD = (24, 13)
HEAD_R = 9
SHOULDER_TOP = 30
BADGE = (35, 39)
BADGE_R = 5


class StepUncle(Solo48):
    icon_id = "step-uncle"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("stepuncle",)
    keywords = ("step", "uncle", "family", "relative", "person", "user")

    def build(self) -> None:
        hx, hy = HEAD
        self.add_arc("head-top", (hx - HEAD_R, hy), (hx + HEAD_R, hy), radius_x=HEAD_R)
        self.add_arc("head-bottom", (hx + HEAD_R, hy), (hx - HEAD_R, hy), radius_x=HEAD_R)
        self.add_contour("head", "head-top", "head-bottom", closed=True)

        bx, by = BADGE
        contact = (bx - 3, by - 4)          # 3-4-5 point on the badge circle
        self.add_bezier("shoulder-left", (8, 44), ((8, 36), (14, SHOULDER_TOP), (20, SHOULDER_TOP)))
        self.add_line("shoulder-top", (20, SHOULDER_TOP), (28, SHOULDER_TOP))
        self.add_bezier("shoulder-right", (28, SHOULDER_TOP), ((30.5, SHOULDER_TOP), (31.5, 33), contact))
        self.add_contour("body", "shoulder-left", "shoulder-top", "shoulder-right")

        self.add_arc("badge-upper", contact, (bx + BADGE_R, by), radius_x=BADGE_R, sweep=True)
        self.add_arc("badge-lower", (bx + BADGE_R, by), contact, radius_x=BADGE_R, large_arc=True, sweep=True)
        self.add_contour("badge", "badge-upper", "badge-lower", closed=True)
        self.relate("connect", "body", "badge")
        self.mark_human_figure("person", head="head", torso="shoulder-top", torso_junction="start")
