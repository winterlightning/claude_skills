"""A devil: a horned figure with a long pointed tail curling up beside it.

Human construction: icon_set/references/human_ref/user.svg (circular outlined head over
rounded shoulders, open bottom). The head (r5, centre (14,13)) sits exactly 8 above the
torso's flat top (y=26) on centerlines (4 visible); the point under the head is the
nearest body point. Two horns grow from the head's side points and curl
up to y=6. The torso has r4 shoulders and straight sides to the
bottom edge. The tail leaves the torso's right side low, swings out and curves up to the
top-right, ending in an arrowhead chevron.
Lucide construction: 'user' (head over shoulders); tail as a smooth cubic with a chevron
tip as in 'arrow-up-right'.
Keyshape SQUARE: centerline x 6..42 (torso side, arrowhead), y 6..42 (horn tips, torso).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "08403821-8001-5c1f-9788-1e4dc890984f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__devil-figure-with-tail/20260926T044250Z-thuan-mac/reference/devil_08403821-8001-5c1f-9788-1e4dc890984f.svg"
AUTHOR = "claude-opus-5-5"


class DevilFigureWithTail(Solo48):
    icon_id = "devil-figure-with-tail"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "mythology/fantasy"
    aliases = ("devil", "demon", "satan")
    keywords = ("devil", "demon", "horns", "tail", "evil", "halloween", "hell", "satan", "costume")

    def build(self) -> None:
        # head: two half circles; horns grow from its side points and curl up
        hl, hr = (9, 13), (19, 13)
        self.add_arc("head-top", hl, hr, radius_x=5, sweep=True)
        self.add_arc("head-bottom", hr, hl, radius_x=5, sweep=True)
        self.add_contour("head", "head-top", "head-bottom", closed=True)
        self.add_bezier("horn-left", hl, ((7, 12), (6, 9.5), (6, 6)))
        self.add_bezier("horn-right", hr, ((21, 12), (22, 9.5), (22, 6)))
        self.relate("connect", "head", "horn-left")
        self.relate("connect", "head", "horn-right")
        # torso: flat top, r4 shoulders, open bottom
        self.add_line("torso-side-left", (6, 42), (6, 30))
        self.add_arc("torso-shoulder-left", (6, 30), (10, 26), radius_x=4, sweep=True)
        self.add_line("torso-top-left", (10, 26), (14, 26))
        self.add_line("torso-top-right", (14, 26), (18, 26))
        self.add_arc("torso-shoulder-right", (18, 26), (22, 30), radius_x=4, sweep=True)
        self.add_line("torso-side-right-upper", (22, 30), (22, 36))
        self.add_line("torso-side-right-lower", (22, 36), (22, 42))
        self.add_contour("torso", "torso-side-left", "torso-shoulder-left", "torso-top-left", "torso-top-right",
                         "torso-shoulder-right", "torso-side-right-upper", "torso-side-right-lower")
        self.mark_human_figure("devil", head="head", torso="torso-top-right", torso_junction="start")
        # tail with arrowhead
        tip = (40, 12)
        self.add_bezier("tail", (22, 36), ((30, 40), (38, 38), (38, 28)), ((38, 22), (39, 16), tip))
        self.add_polyline("arrowhead", (34, 13), tip, (42, 18))
        self.relate("connect", "torso", "tail")
        self.relate("connect", "tail", "arrowhead")
