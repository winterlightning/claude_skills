"""A golf ball sitting above its tee.

Symbol plan: mirrored about x=24. The ball is an r12 circle of four quarter arcs centred
(24,16). The tee is a T below it: a slightly cupped bar (ends at y=37, middle y=38, 9 below
the ball) spanning the full width, with the peg dropping from its middle to the bottom
edge. An r14 ball left only a 3-unit peg stub.
Lucide construction: circle and straight strokes, as in 'circle' over a 'T'-shaped stand.
Keyshape VRECT_M: centerline x 10..38 (tee cup ends), y 4..44 (ball top, peg).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "42647a30-ca0f-4367-83c0-c22c024b7067"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__golf-ball-tee/20260926T035939Z-thuan-mac/reference/golf_42647a30-ca0f-4367-83c0-c22c024b7067.svg"
AUTHOR = "claude-opus-5-5"


class GolfBallTee(Solo48):
    icon_id = "golf-ball-tee"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports/golf"
    aliases = ("golf", "golf-ball", "tee")
    keywords = ("golf", "ball", "tee", "sport", "course", "drive", "club", "game")

    def build(self) -> None:
        n, e, s, w = (24, 4), (36, 16), (24, 28), (12, 16)
        self.add_arc("ball-ne", n, e, radius_x=12, sweep=True)
        self.add_arc("ball-se", e, s, radius_x=12, sweep=True)
        self.add_arc("ball-sw", s, w, radius_x=12, sweep=True)
        self.add_arc("ball-nw", w, n, radius_x=12, sweep=True)
        self.add_contour("ball", "ball-ne", "ball-se", "ball-sw", "ball-nw", closed=True)
        self.add_bezier("tee-cup", (10, 37), ((16, 38), (20, 38), (24, 38)), ((28, 38), (32, 38), (38, 37)))
        self.add_line("tee-peg", (24, 38), (24, 44))
        self.relate("connect", "tee-cup", "tee-peg")
