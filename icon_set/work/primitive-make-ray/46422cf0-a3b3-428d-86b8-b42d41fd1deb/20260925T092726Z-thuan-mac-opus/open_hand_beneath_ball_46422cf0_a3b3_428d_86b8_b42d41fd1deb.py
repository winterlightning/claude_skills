"""Catch: an open hand, palm up, with the thumb raised on the left and the
fingers curling up on the right, about to catch a ball dropping above it.

Symbol plan: the hand is one open run - back of hand on x + y = 34, a
radius-5 thumb tip, the thumb underside 8.5 from the back, the palm crease, the finger's inner edge on the (4,-3)
direction, a radius-5 fingertip semicircle (endpoints centre +/- (3,4)), the
finger's outer edge parallel to the inner one 10 away, the palm's lower edge
8 below the crease, and the wrist's lower edge parallel to the back of the
hand. The ball is a radius-5 circle clearing the thumb and fingertip by 8+.
Keyshape SQUARE, centerline box (6,6)-(42,42).
Lucide construction: hand-helping / hand-coins (thumb tip, palm crease,
fingers rising to a rounded tip, object above).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "46422cf0-a3b3-428d-86b8-b42d41fd1deb"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__open-hand-beneath-ball/20260925T092530Z-thuan-mac/reference/catch_46422cf0-a3b3-428d-86b8-b42d41fd1deb.svg"
AUTHOR = "claude-opus-5-5"


class OpenHandBeneathBall(Solo48):
    icon_id = "open-hand-beneath-ball"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ("catch", "catching ball", "hand and ball")
    keywords = ("catch", "hand", "ball", "palm", "throw", "receive")

    def build(self) -> None:
        crease, lower = 30, 38
        thumb_top, thumb_tip_end, crease_start = (14, 20), (20, 26), (16, crease)
        finger_in, finger_out = (34, 24), (40, 32)      # fingertip centre (37,28)
        self.add_line("hand-1", (6, 28), thumb_top)                       # back of hand
        self.add_arc("hand-2", thumb_top, thumb_tip_end, radius_x=5)      # thumb tip
        self.add_line("hand-3", thumb_tip_end, crease_start)              # thumb underside
        self.add_line("hand-4", crease_start, (26, crease))               # palm crease
        self.add_line("hand-5", (26, crease), finger_in)                  # finger inner edge
        self.add_arc("hand-6", finger_in, finger_out, radius_x=5)         # fingertip
        self.add_line("hand-7", finger_out, (32, lower))                  # finger outer edge
        self.add_line("hand-8", (32, lower), (22, lower))                 # palm lower edge
        self.add_line("hand-9", (22, lower), (18, 42))                    # wrist
        self.add_contour("hand", *[f"hand-{i}" for i in range(1, 10)])
        cx, cy, r = 30, 11, 5
        self.add_arc("ball-1", (cx, cy - r), (cx, cy + r), radius_x=r)
        self.add_arc("ball-2", (cx, cy + r), (cx, cy - r), radius_x=r)
        self.add_contour("ball", "ball-1", "ball-2", closed=True)
