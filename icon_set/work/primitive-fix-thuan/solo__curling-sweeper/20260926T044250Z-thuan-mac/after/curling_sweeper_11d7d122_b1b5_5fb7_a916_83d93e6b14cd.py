"""A curling sweeper: a figure leaning into a sweep, pushing a broom whose flat head rests on the ice at the lower left.

Symbol plan: stick figure per the shared full-body reference: ring head (r5) straight
above the neck, exactly 8 on centerlines (4 units of ink); a torso leaving the neck
vertically and easing back to the hips; a front arm reaching down-left to the hand on
the broom handle (shared endpoint); a back arm bent out to the right; legs apart. The
broom is a 45-degree handle from the hand to the top of a flat oval head (6x3
half-axes) on the ice. Every limb stays 8+ from the broom and from each other.
Lucide construction: none; figure from icon_set/references/human_ref/full_body_ref.png.
Keyshape SQUARE: centerline x 6..42 (broom head, back hand), y 6..42 (head top, feet).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "11d7d122-b1b5-5fb7-a916-83d93e6b14cd"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__curling-sweeper/20260926T044250Z-thuan-mac/reference/sport curling_11d7d122-b1b5-5fb7-a916-83d93e6b14cd.svg"
AUTHOR = "claude-opus-5-5"


class CurlingSweeper(Solo48):
    icon_id = "curling-sweeper"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports/winter"
    aliases = ("sport curling", "curling", "curler")
    keywords = ("curling", "sweeper", "broom", "ice", "winter sport", "olympics", "sport", "athlete")

    def build(self) -> None:
        hx, hy, hr = 28, 11, 5
        neck = (hx, hy + hr + 8)
        hips = (26, 33)
        hand = (19, 27)
        bx, by, brx, bry = 12, 37, 6, 3   # broom head oval
        # head
        pts = [(hx - hr, hy), (hx, hy - hr), (hx + hr, hy), (hx, hy + hr)]
        names = ("head-nw", "head-ne", "head-se", "head-sw")
        for i, n in enumerate(names):
            self.add_arc(n, pts[i], pts[(i + 1) % 4], radius_x=hr)
        self.add_contour("head", *names, closed=True)
        # body
        self.add_bezier("torso", neck, ((hx, 28), (27, 31), hips))
        self.mark_human_figure("sweeper", head="head", torso="torso", torso_junction="start")
        self.add_line("arm-front", neck, hand)
        self.add_polyline("arm-back", neck, (36, 25), (42, 32))
        self.add_line("leg-front", hips, (26, 42))
        self.add_line("leg-back", hips, (36, 42))
        for part in ("arm-front", "arm-back", "leg-front", "leg-back"):
            self.relate("connect", "torso", part)
        self.relate("connect", "arm-front", "arm-back")
        self.relate("connect", "leg-front", "leg-back")
        # broom
        top = (bx, by - bry)
        self.add_line("handle", hand, top)
        self.relate("connect", "arm-front", "handle")
        opts = [(bx - brx, by), top, (bx + brx, by), (bx, by + bry)]
        names = ("broom-nw", "broom-ne", "broom-se", "broom-sw")
        for i, n in enumerate(names):
            self.add_arc(n, opts[i], opts[(i + 1) % 4], radius_x=brx, radius_y=bry)
        self.add_contour("broom", *names, closed=True)
        self.relate("connect", "handle", "broom")
