"""A person in crescent lunge (yoga): front knee bent square, back leg extended long,
torso upright, one arm raised.

Human construction: icon_set/references/human_ref/full_body_ref.png (stick figure:
circular outlined head, single-stroke torso and limbs). The torso is upright from the
hip H=(22,34) to the neck S=(22,22); the r4 head is centred (22,10) on that axis, so its
outline is exactly 8 from the neck on centerlines (4 visible) and S is the nearest body
point. The raised arm leaves the shoulder A=(22,26), 4 below the neck, and rises to
(37,13); its nearest approach to the head outline is 8.1. The front thigh is level from
the hip to the knee (42,34) and the shin drops to the floor; the back leg extends
straight to the lower-left corner.
Lucide construction: 'person-standing' - round-ended single-stroke limbs.
Keyshape SQUARE: centerline x 6..42 (back foot, front knee/shin), y 6..42 (head, feet).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a860d136-343f-4827-85ad-e36b66cfa52a"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__crescent-lunge-pose/20260926T035939Z-thuan-mac/reference/crescent lunge pose_a860d136-343f-4827-85ad-e36b66cfa52a.svg"
AUTHOR = "claude-opus-5-5"


class CrescentLungePose(Solo48):
    icon_id = "crescent-lunge-pose"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports/yoga"
    aliases = ("crescent-lunge", "anjaneyasana", "high-lunge")
    keywords = ("yoga", "lunge", "crescent", "pose", "stretch", "fitness", "exercise", "asana", "person")

    def build(self) -> None:
        C, S, A, H, r = (22, 10), (22, 22), (22, 26), (22, 34), 4
        self.add_arc("head-top", (C[0] - r, C[1]), (C[0] + r, C[1]), radius_x=r, sweep=True)
        self.add_arc("head-bottom", (C[0] + r, C[1]), (C[0] - r, C[1]), radius_x=r, sweep=True)
        self.add_contour("head", "head-top", "head-bottom", closed=True)
        self.add_line("torso-upper", S, A)
        self.add_line("torso-lower", A, H)
        self.add_contour("torso", "torso-upper", "torso-lower")
        self.add_line("arm", A, (37, 13))
        self.add_polyline("front-leg", H, (42, 34), (42, 42))
        self.add_line("back-leg", H, (6, 42))
        self.relate("connect", "torso", "arm")
        self.relate("connect", "torso", "front-leg")
        self.relate("connect", "torso", "back-leg")
        self.relate("connect", "front-leg", "back-leg")
        self.mark_human_figure("person", head="head", torso="torso-upper", torso_junction="start")
