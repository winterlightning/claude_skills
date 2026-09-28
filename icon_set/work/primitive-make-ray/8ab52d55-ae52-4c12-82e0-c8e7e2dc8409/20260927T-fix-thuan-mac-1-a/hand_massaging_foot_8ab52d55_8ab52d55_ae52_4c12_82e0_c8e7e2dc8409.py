"""Hand massaging the sole of a foot.

Symbol plan: foot = open outline from the heel (r10 corner) up the left
edge to a big toe (r4 semicircle, top y=6) and four smaller r3 toe bumps
stepping down to the right, ending where it disappears behind the hand at
the hand's top-left corner (32,17). Hand = open outline rising from the
wrist at the bottom: a 45-degree thumb tube (8.5 wide, r5 tip) pressing
up-left into the sole, the crotch, and a mitten of fingers (10 wide, r5
top) down to the bottom edge.
Revision: the rejected drawing tangled foot and hand into one crossing
scribble with no toes; the reference shows a toed foot and a separate
hand whose thumb presses the sole.
Omitted: the reference's two small pressure arcs (a 15-unit band between
foot edge and thumb cannot hold an arc with 8 clearance each side).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8ab52d55-ae52-4c12-82e0-c8e7e2dc8409"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__hand-massaging-foot-8ab52d55/20260927T153253Z-thuan-mac-1/reference/massage foot_8ab52d55-ae52-4c12-82e0-c8e7e2dc8409.svg"
AUTHOR = "claude-opus-5-5"


class HandMassagingFoot(Solo48):
    icon_id = "hand-massaging-foot-8ab52d55"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("primitives", "health")
    aliases = ("massage foot", "foot massage", "reflexology")
    keywords = ("massage", "foot", "hand", "reflexology", "spa", "therapy")

    def build(self) -> None:
        self.add_arc("foot-heel", (16, 40), (6, 30), radius_x=10, sweep=True)
        self.add_line("foot-edge", (6, 30), (6, 10))
        self.add_arc("foot-big-toe", (6, 10), (14, 10), radius_x=4, sweep=True)
        toes = ((14, 10), (19, 11), (24, 13), (28, 15), (32, 17))
        for i in range(4):
            self.add_arc(f"foot-toe-{i}", toes[i], toes[i + 1], radius_x=3, sweep=True)
        self.add_contour("foot", "foot-heel", "foot-edge", "foot-big-toe",
                         *(f"foot-toe-{i}" for i in range(4)))

        self.add_line("hand-wrist", (30, 42), (30, 39))
        self.add_line("hand-thumb-low", (30, 39), (20, 29))
        self.add_arc("hand-thumb-tip", (20, 29), (26, 23), radius_x=5, sweep=True)
        self.add_line("hand-thumb-up", (26, 23), (32, 29))
        self.add_line("hand-fingers-left", (32, 29), (32, 17))
        self.add_arc("hand-fingers-top", (32, 17), (42, 17), radius_x=5, sweep=True)
        self.add_line("hand-back", (42, 17), (42, 42))
        self.add_contour("hand", "hand-wrist", "hand-thumb-low", "hand-thumb-tip",
                         "hand-thumb-up", "hand-fingers-left", "hand-fingers-top", "hand-back")
        self.relate("connect", "foot", "hand")
