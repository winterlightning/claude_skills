"""Standing mink in profile: long low body on the ground, raised head, rounded tail tip.

Symbol plan: one closed silhouette contour (tail tip -> ground -> chest -> head ->
neck -> back -> tail top); the ground run is shared by tail and feet.
Keyshape HRECT_M: tail tip x=4, nose x=44, head crown y=10, ground y=38.
Lucide construction: rabbit / squirrel profile animals - one continuous
silhouette with smooth tangent-continuous cubic back and head.
Revision of the rejected drawing ("Bad stroke drawn"): the old open polyline
with a sharp elbow chest and jagged head is replaced by a smooth closed body.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f8a2935a-35c7-45b5-9d40-0387e3eeffbe"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__standing-mink/20260925T092544Z-thuan-mac/reference/mink_f8a2935a-35c7-45b5-9d40-0387e3eeffbe.svg"
AUTHOR = "claude-opus-5-5"

GROUND = 38
TAIL_TOP = 30


class StandingMink(Solo48):
    icon_id = "standing-mink"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("mink",)
    keywords = ("standing", "mink", "weasel", "animal", "fur")

    def path(self, name, start, steps, closed=False):
        members = []
        for index, (kind, *args) in enumerate(steps):
            tag = f"{name}-{index + 1}"
            if kind == "L":
                end = args[0]
                self.add_line(tag, start, end)
            elif kind == "C":
                c1, c2, end = args
                self.add_bezier(tag, start, (c1, c2, end))
            else:
                end, radius, sweep = args
                self.add_arc(tag, start, end, radius_x=radius, sweep=sweep)
            start = end
            members.append(tag)
        self.add_contour(name, *members, closed=closed)

    def build(self) -> None:
        self.path("mink", (8, TAIL_TOP), [
            ("A", (8, GROUND), 4, False),            # rounded tail tip, x min 4
            ("L", (19, GROUND)),                    # hind foot
            ("L", (19, 33)),                        # hind leg front
            ("A", (28, 33), 5, True),               # belly arch between the legs
            ("L", (28, GROUND)),                    # front leg back
            ("L", (36, GROUND)),                    # front foot
            ("L", (36, 28)),                        # chest
            ("C", (36, 24), (38, 22), (41, 21)),    # throat into jaw
            ("C", (43, 20.5), (44, 19), (44, 17)),  # chin to nose
            ("C", (43, 14), (40, 10), (35, 10)),    # tapered muzzle to crown
            ("C", (32, 10), (30, 12), (28, 15)),    # nape
            ("C", (27, 18), (24, 18), (20, 18)),    # neck into back
            ("C", (14, 18), (11, 23), (11, TAIL_TOP)),  # rounded rump to tail base
            ("L", (8, TAIL_TOP)),                   # tail top
        ], closed=True)
