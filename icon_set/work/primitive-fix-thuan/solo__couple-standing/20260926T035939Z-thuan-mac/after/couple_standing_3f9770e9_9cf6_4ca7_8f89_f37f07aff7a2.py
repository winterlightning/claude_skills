"""A man and a woman standing side by side: restroom-style figures.

Human construction: icon_set/references/human_ref/full_body_ref.png (the dress figure:
circular head, rounded-top flared dress, two straight legs) and user.svg. Shared
parameters: head radius 5, head centre y=11, body top y=24, so each detached head sits
exactly 8 above its body's nearest point on centerlines (4 visible): 11 + 5 + 8 = 24.
Woman (axis x=13): an r4 round-topped dress whose sides flare from (9,28)/(17,28) to the
hem (6..19, y 35), legs 8 apart to the bottom edge. Man (axis x=35): a torso with r3 top
corners x 29..42, y 24..35 and legs 8 apart. Figures are 10 apart at hem/torso level.
Lucide construction: 'person-standing'-style figures; restroom pictogram vocabulary.
Keyshape SQUARE: centerline x 6..42 (hem, torso side), y 6..42 (heads, feet).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3f9770e9-9cf6-4ca7-8f89-f37f07aff7a2"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__couple-standing/20260926T035939Z-thuan-mac/reference/multiple man woman_3f9770e9-9cf6-4ca7-8f89-f37f07aff7a2.svg"
AUTHOR = "claude-opus-5-5"

HEAD_R, HEAD_Y, BODY_Y, HIP_Y = 5, 11, 24, 35


class CoupleStanding(Solo48):
    icon_id = "couple-standing"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/groups"
    aliases = ("multiple-man-woman", "man-and-woman", "restroom-couple")
    keywords = ("man", "woman", "couple", "people", "restroom", "toilet", "gender", "family", "pair")

    def _head(self, name, cx):
        self.add_arc(f"{name}-top", (cx - HEAD_R, HEAD_Y), (cx + HEAD_R, HEAD_Y), radius_x=HEAD_R, sweep=True)
        self.add_arc(f"{name}-bottom", (cx + HEAD_R, HEAD_Y), (cx - HEAD_R, HEAD_Y), radius_x=HEAD_R, sweep=True)
        self.add_contour(name, f"{name}-top", f"{name}-bottom", closed=True)

    def build(self) -> None:
        # woman
        w = 13
        self._head("woman-head", w)
        self.add_arc("dress-cap-right", (w, BODY_Y), (w + 4, BODY_Y + 4), radius_x=4, sweep=True)
        self.add_line("dress-side-right", (w + 4, BODY_Y + 4), (19, HIP_Y))
        self.add_line("dress-hem-right", (19, HIP_Y), (17, HIP_Y))
        self.add_line("dress-hem-mid", (17, HIP_Y), (9, HIP_Y))
        self.add_line("dress-hem-left", (9, HIP_Y), (6, HIP_Y))
        self.add_line("dress-side-left", (6, HIP_Y), (w - 4, BODY_Y + 4))
        self.add_arc("dress-cap-left", (w - 4, BODY_Y + 4), (w, BODY_Y), radius_x=4, sweep=True)
        self.add_contour("dress", "dress-cap-right", "dress-side-right", "dress-hem-right", "dress-hem-mid",
                         "dress-hem-left", "dress-side-left", "dress-cap-left", closed=True)
        self.add_line("woman-leg-left", (9, HIP_Y), (9, 42))
        self.add_line("woman-leg-right", (17, HIP_Y), (17, 42))
        self.relate("connect", "dress", "woman-leg-left")
        self.relate("connect", "dress", "woman-leg-right")
        self.mark_human_figure("woman", head="woman-head", torso="dress-cap-right", torso_junction="start")
        # man
        m, x0, x1, r = 35, 29, 42, 3
        self._head("man-head", m)
        self.add_line("torso-top-right", (m, BODY_Y), (x1 - r, BODY_Y))
        self.add_arc("torso-corner-right", (x1 - r, BODY_Y), (x1, BODY_Y + r), radius_x=r, sweep=True)
        self.add_line("torso-side-right", (x1, BODY_Y + r), (x1, HIP_Y))
        self.add_line("torso-hip-right", (x1, HIP_Y), (39, HIP_Y))
        self.add_line("torso-hip-mid", (39, HIP_Y), (31, HIP_Y))
        self.add_line("torso-hip-left", (31, HIP_Y), (x0, HIP_Y))
        self.add_line("torso-side-left", (x0, HIP_Y), (x0, BODY_Y + r))
        self.add_arc("torso-corner-left", (x0, BODY_Y + r), (x0 + r, BODY_Y), radius_x=r, sweep=True)
        self.add_line("torso-top-left", (x0 + r, BODY_Y), (m, BODY_Y))
        self.add_contour("torso", "torso-top-right", "torso-corner-right", "torso-side-right", "torso-hip-right",
                         "torso-hip-mid", "torso-hip-left", "torso-side-left", "torso-corner-left",
                         "torso-top-left", closed=True)
        self.add_line("man-leg-left", (31, HIP_Y), (31, 42))
        self.add_line("man-leg-right", (39, HIP_Y), (39, 42))
        self.relate("connect", "torso", "man-leg-left")
        self.relate("connect", "torso", "man-leg-right")
        self.mark_human_figure("man", head="man-head", torso="torso-top-right", torso_junction="start")
