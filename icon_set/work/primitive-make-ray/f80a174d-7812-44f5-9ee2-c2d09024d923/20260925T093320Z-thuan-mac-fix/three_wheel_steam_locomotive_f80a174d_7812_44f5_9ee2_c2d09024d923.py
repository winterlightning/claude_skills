"""Side view of a toy steam locomotive: tall cab, boiler with chimney, rounded
nose and three wheels.

Symbol plan: one body contour from the cab's rear foot around cab, chimney and
nose to the front foot; the frame runs through the wheel centres (y=36), so each
wheel is a closed circle of radius 4 whose left and right points are shared with
the frame segments and the two body walls (declared connections). The three
wheels repeat one definition at x = 8, 24, 40.
Keyshape HRECT_L: cab wall x=4, nose x=44, chimney top y=8, wheel bottoms y=40.
Lucide construction: train-front (rounded body corners, straight chimney/cab
runs); no side-view locomotive exists locally.
Revision of the rejected drawing ("Bad stroke drawn"): the old drawing had a
wheel fused into the cab and two floating wheels; here wheels, cab and boiler
share one frame line.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f80a174d-7812-44f5-9ee2-c2d09024d923"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__three-wheel-steam-locomotive/20260925T092544Z-thuan-mac/reference/steam engine_f80a174d-7812-44f5-9ee2-c2d09024d923.svg"
AUTHOR = "claude-opus-5-5"

FRAME = 36
WHEEL_R = 4
WHEELS = (8, 24, 40)


class ThreeWheelSteamLocomotive(Solo48):
    icon_id = "three-wheel-steam-locomotive"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("steam-engine", "steam-locomotive")
    keywords = ("steam", "engine", "locomotive", "train", "railway")

    def path(self, name, start, steps, closed=False):
        members = []
        for index, (kind, *args) in enumerate(steps):
            tag = f"{name}-{index + 1}"
            if kind == "L":
                end = args[0]
                self.add_line(tag, start, end)
            else:
                end, radius, sweep = args
                self.add_arc(tag, start, end, radius_x=radius, sweep=sweep)
            start = end
            members.append(tag)
        self.add_contour(name, *members, closed=closed)

    def build(self) -> None:
        r = WHEEL_R
        self.path("body", (4, FRAME), [
            ("L", (4, 12)),                 # cab rear wall
            ("A", (6, 10), 2, True),
            ("L", (20, 10)),                # cab roof
            ("A", (22, 12), 2, True),
            ("L", (22, 20)),                # cab front wall
            ("L", (30, 20)),                # boiler top
            ("L", (30, 8)),                 # chimney
            ("L", (38, 8)),
            ("L", (38, 20)),
            ("L", (40, 20)),
            ("A", (44, 24), 4, True),       # rounded nose
            ("L", (44, FRAME)),             # front wall
        ])
        self.add_dot("cab-window", (13, 19))
        for index, x in enumerate(WHEELS, 1):
            self.path(f"wheel-{index}", (x - r, FRAME), [
                ("A", (x, FRAME - r), r, True),
                ("A", (x + r, FRAME), r, True),
                ("A", (x, FRAME + r), r, True),
                ("A", (x - r, FRAME), r, True),
            ], closed=True)
        self.relate("connect", "body", "wheel-1")
        self.relate("connect", "body", "wheel-3")
        for index in range(1, len(WHEELS)):
            left, right = WHEELS[index - 1] + r, WHEELS[index] - r
            self.add_line(f"frame-{index}", (left, FRAME), (right, FRAME))
            self.relate("connect", f"frame-{index}", f"wheel-{index}")
            self.relate("connect", f"frame-{index}", f"wheel-{index + 1}")
