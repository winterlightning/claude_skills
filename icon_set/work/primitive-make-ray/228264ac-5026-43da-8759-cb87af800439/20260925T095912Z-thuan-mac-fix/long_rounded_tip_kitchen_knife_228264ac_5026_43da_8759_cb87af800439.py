"""Long kitchen knife on the diagonal: a rounded handle at the lower left, a
bolster line, and a long straight blade ending in a rounded tip at the upper
right.

Symbol plan: one closed outline on the 45-degree axis x+y=48 with parallel
side lines x+y=41 (back) and x+y=55 (edge), 9.9 apart. The handle end is a
radius-5 cap whose 3-4-5 points land on both side lines; the tip is a
quarter circle of radius 7 about (35,13) from the back's end (35,6) to the
edge's end (42,13); the bolster is a cross line perpendicular to the axis with
shared end points (declared connection).
Keyshape SQUARE: handle cap left x=6 / bottom y=42, tip top y=6 / right x=42.
Lucide construction: utensils / knife (long straight blade, rounded handle).
Revision of the rejected drawing ("Bad stroke drawn"): the old drawing was a
short curved sickle with a stubby handle; here the knife is long and straight
with a round handle end and a rounded tip.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "228264ac-5026-43da-8759-cb87af800439"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__long-rounded-tip-kitchen-knife/20260925T092544Z-thuan-mac/reference/blade_228264ac-5026-43da-8759-cb87af800439.svg"
AUTHOR = "claude-opus-5-5"

HANDLE_CAP = (11, 37)
HANDLE_R = 5
TIP_CENTRE = (35, 13)
TIP_R = 7
BOLSTER_BACK = (18, 23)     # on the back line x+y=41


class LongRoundedTipKitchenKnife(Solo48):
    icon_id = "long-rounded-tip-kitchen-knife"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("blade", "table-knife", "kitchen-knife")
    keywords = ("blade", "knife", "kitchen", "cut", "cooking", "utensil")

    def build(self) -> None:
        hx, hy = HANDLE_CAP
        tx, ty = TIP_CENTRE
        cap_back, cap_edge = (hx - 4, hy - 3), (hx + 3, hy + 4)
        tip_back, tip_edge = (tx, ty - TIP_R), (tx + TIP_R, ty)
        bolster_edge = (BOLSTER_BACK[0] + 7, BOLSTER_BACK[1] + 7)
        self.add_line("back", cap_back, tip_back)
        self.add_arc("tip", tip_back, tip_edge, radius_x=TIP_R)
        self.add_line("edge", tip_edge, cap_edge)
        self.add_arc("handle-cap", cap_edge, cap_back, radius_x=HANDLE_R)
        self.add_contour("knife", "back", "tip", "edge", "handle-cap", closed=True)
        self.add_line("bolster", BOLSTER_BACK, bolster_edge)
        self.relate("connect", "knife", "bolster")
