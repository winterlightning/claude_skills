"""Bay: a rounded basin of water whose shoreline steps down in an S-curve to a
shelf, with a headland post rising on the right and curling out to sea; two
long low wave lines sit on the water.

Symbol plan: the shore is one closed contour (top-left corner radius 6, top
edge, convex/concave radius-3 S-curve, shelf, right side, radius-12 bottom
corners). The headland is a radius-4 curl leaving the shelf's end node. Waves are two tilde runs of shared half-hump width, the
upper one left and the lower one right so they clear each other and the
shore by 8. Keyshape SQUARE, centerline box (6,6)-(42,42).
Lucide construction: waves (half-hump tilde runs); shore corners follow
Lucide's arc-cornered outline construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "95af3736-8137-457c-a403-3663a17cb3af"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__curved-bay-with-two-wave-lines/20260925T092530Z-thuan-mac/reference/bay_95af3736-8137-457c-a403-3663a17cb3af.svg"
AUTHOR = "claude-opus-5-5"

HUMP = 6       # half-wave width
LIFT = 1.6     # control offset; peak height is 0.75 * LIFT


class CurvedBay(Solo48):
    icon_id = "curved-bay-with-two-wave-lines"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places"
    aliases = ("bay", "cove", "harbor")
    keywords = ("bay", "water", "waves", "coast", "sea", "cove")

    def build(self) -> None:
        shelf = (38, 12)
        self.add_arc("shore-1", (6, 12), (12, 6), radius_x=6)
        self.add_line("shore-2", (12, 6), (24, 6))
        self.add_arc("shore-3", (24, 6), (27, 9), radius_x=3)
        self.add_arc("shore-4", (27, 9), (30, 12), radius_x=3, sweep=False)
        self.add_line("shore-5", (30, 12), shelf)
        self.add_line("shore-6", shelf, (38, 30))
        self.add_arc("shore-7", (38, 30), (26, 42), radius_x=12)
        self.add_line("shore-8", (26, 42), (18, 42))
        self.add_arc("shore-9", (18, 42), (6, 30), radius_x=12)
        self.add_line("shore-10", (6, 30), (6, 12))
        self.add_contour("shore", *[f"shore-{i}" for i in range(1, 11)], closed=True)
        self.add_arc("headland", shelf, (42, 8), radius_x=4)
        self.relate("connect", "shore", "headland")
        self.wave("wave-upper", (15, 20), 2)
        self.wave("wave-lower", (16, 31), 2)

    def wave(self, name, start, humps, phase=0):
        x, y = start
        segments = []
        for index in range(humps):
            lift = -LIFT if (index + phase) % 2 == 0 else LIFT
            segments.append(((x + 2, y + lift), (x + HUMP - 2, y + lift), (x + HUMP, y)))
            x += HUMP
        self.add_bezier(name, start, *segments)
