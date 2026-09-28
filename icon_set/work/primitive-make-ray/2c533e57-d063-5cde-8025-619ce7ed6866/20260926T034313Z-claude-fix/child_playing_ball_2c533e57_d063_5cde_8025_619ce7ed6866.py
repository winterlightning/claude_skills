"""A child playing ball: a running stick figure leaning toward a small ball on the left.

Symbol plan: stick figure per the shared full-body reference (running/approaching-ball
pose) with a child's large head: ring head (r6) straight above the neck, exactly 8 on centerlines (4 units of ink);
a curved torso leaving the neck vertically and leaning back-left to the hips; a front arm
reaching horizontally toward the ball, a back arm swinging down-right; a back leg
stretched down-left and a bent front leg stepping down-right. The ball is a small circle
(r3, the approved 6-diameter circle) at the left, at least 8 from the arm and leg.
Asymmetric by design (motion to the left, as in the reference).
Lucide construction: none; pose from icon_set/references/human_ref/full_body_ref.png and
the approved football-player-approaching-ball placement (head on the torso's tangent).
Keyshape SQUARE: centerline x 6..42 (ball, back hand), y 6..42 (head top, feet).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2c533e57-d063-5cde-8025-619ce7ed6866"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__child-playing-ball/20260926T034135Z-thuan-mac/reference/family child play ball_2c533e57-d063-5cde-8025-619ce7ed6866.svg"
AUTHOR = "claude-opus-5-5"


class ChildPlayingBall(Solo48):
    icon_id = "child-playing-ball"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/activity"
    aliases = ("child play ball", "kid with ball")
    keywords = ("child", "kid", "ball", "play", "running", "football", "game", "family", "sport")

    def build(self) -> None:
        hx, hy, hr = 27, 12, 6
        neck = (hx, hy + hr + 8)
        hips = (22, 34)
        ball, br = (9, 32), 3
        # head
        pts = [(hx - hr, hy), (hx, hy - hr), (hx + hr, hy), (hx, hy + hr)]
        names = ("head-nw", "head-ne", "head-se", "head-sw")
        for i, name in enumerate(names):
            self.add_arc(name, pts[i], pts[(i + 1) % 4], radius_x=hr)
        self.add_contour("head", *names, closed=True)
        # torso: vertical at the neck, leaning back-left to the hips
        self.add_bezier("torso", neck, ((hx, 29), (25, 32), hips))
        self.mark_human_figure("child", head="head", torso="torso", torso_junction="start")
        # limbs
        self.add_line("arm-front", neck, (19, neck[1]))
        self.add_polyline("arm-back", neck, (35, 32), (42, 32))
        self.add_line("leg-back", hips, (16, 42))
        self.add_polyline("leg-front", hips, (29, 38), (29, 42))
        for part in ("arm-front", "arm-back", "leg-back", "leg-front"):
            self.relate("connect", "torso", part)
        self.relate("connect", "arm-front", "arm-back")
        self.relate("connect", "leg-back", "leg-front")
        # ball
        pts = [(ball[0] - br, ball[1]), (ball[0], ball[1] - br), (ball[0] + br, ball[1]), (ball[0], ball[1] + br)]
        names = ("ball-nw", "ball-ne", "ball-se", "ball-sw")
        for i, name in enumerate(names):
            self.add_arc(name, pts[i], pts[(i + 1) % 4], radius_x=br)
        self.add_contour("ball", *names, closed=True)
