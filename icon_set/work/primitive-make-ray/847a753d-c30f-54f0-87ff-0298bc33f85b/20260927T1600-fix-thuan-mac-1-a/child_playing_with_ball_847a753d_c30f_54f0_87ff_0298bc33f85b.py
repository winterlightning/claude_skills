"""Child playing with a ball: a stick child with both arms raised in a V beside a ball.

Revision of the disapproved drawing, whose elbow-bent arms read as a candelabra and
whose legs were running. Plan (SQUARE, centerline (6,6)-(42,42)): head r5 at (18,11)
straight above the torso (18,24)-(18,36) so the detached gap is exactly 8 on
centerlines / 4 visible; straight V arms from (18,30) to (6,20) and (30,20) clearing
the head by more than 8; standing legs to (14,42) and (22,42); ball r5 at (37,37).
Human reference: icon_set/references/human_ref/full_body_ref.png (arms-up pose).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "847a753d-c30f-54f0-87ff-0298bc33f85b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__child-playing-with-ball/20260927T150749Z-thuan-mac-1/reference/kids play ball_847a753d-c30f-54f0-87ff-0298bc33f85b.svg"
AUTHOR = "claude-fable-5-1"


class ChildPlayingWithBall(Solo48):
    icon_id = "child-playing-with-ball"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "kids"
    aliases = ("kid with ball", "kids play ball")
    keywords = ("child", "kid", "playing", "ball", "arms up", "play")

    def circle(self, name, x, y, r):
        pts = [(x - r, y), (x, y - r), (x + r, y), (x, y + r)]
        for j in range(4):
            self.add_arc(f"{name}-{j}", pts[j], pts[(j + 1) % 4], radius_x=r)
        self.add_contour(name, *(f"{name}-{j}" for j in range(4)), closed=True)

    def build(self) -> None:
        self.circle("head", 18, 11, 5)
        self.add_line("torso", (18, 24), (18, 30))
        self.add_line("hips", (18, 30), (18, 36))
        self.add_polyline("arms", (6, 20), (18, 30), (30, 20))
        self.add_polyline("legs", (14, 42), (18, 36), (22, 42))
        self.relate("connect", "torso", "hips")
        self.relate("connect", "torso", "arms")
        self.relate("connect", "hips", "arms")
        self.relate("connect", "hips", "legs")
        self.mark_human_figure("child", head="head", torso="torso", torso_junction="start")
        self.circle("ball", 37, 37, 5)
