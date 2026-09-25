"""Chef's knife on the diagonal: a broad blade with a straight spine and a
curved belly rising to the tip at the upper left corner, and a rounded handle at the
lower right.

Symbol plan: one closed outline on the 45-degree axis x-y=0. The
handle's upper side is x-y=7; the handle's lower side
is x-y=-7; the handle end is a radius-5 cap whose 3-4-5 points land on both
side lines. The bolster is a line perpendicular to the axis from the spine to
the heel, and the handle's lower side meets it (shared end points, declared
connection). The spine runs from the tip to the handle's upper side x-y=7
(bending 8 degrees at the bolster); the belly is one cubic leaving the tip
straight down, for a 56-degree point.
Keyshape SQUARE: tip x=6 / y=6, handle cap right x=42 / bottom y=42.
Lucide construction: utensils / knife (long blade with a straight spine and a
rounded handle).
Revision of the rejected drawing ("Bad stroke drawn"): the old drawing had a
thin wedge blade with a heavy kinked handle; here the blade is broad and
smooth and the handle straight with a true round end.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "88acc3ca-ec5a-4cec-af6f-f39df121e302"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__kitchen-chef-knife/20260925T092544Z-thuan-mac/reference/knife 1_88acc3ca-ec5a-4cec-af6f-f39df121e302.svg"
AUTHOR = "claude-opus-5-5"

CAP = (37, 37)
CAP_R = 5
TIP = (6, 6)            # upper-left corner
SPINE_END = (30, 23)    # bolster top, on x-y=7
HANDLE_LOW = (23, 30)   # bolster point on the handle's lower side x-y=-7
HEEL = (18, 35)


class KitchenChefKnife(Solo48):
    icon_id = "kitchen-chef-knife"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("knife", "chef-knife")
    keywords = ("knife", "chef", "kitchen", "cooking", "blade", "cut")

    def build(self) -> None:
        cx, cy = CAP
        cap_upper, cap_lower = (cx + 4, cy - 3), (cx - 3, cy + 4)
        self.add_line("spine", TIP, SPINE_END)
        self.add_line("handle-upper", SPINE_END, cap_upper)
        self.add_arc("handle-cap", cap_upper, cap_lower, radius_x=CAP_R)
        self.add_line("handle-lower", cap_lower, HANDLE_LOW)
        self.add_line("heel", HANDLE_LOW, HEEL)
        self.add_bezier("belly", HEEL, ((10, 30), (6, 17), TIP))
        self.add_contour("knife", "spine", "handle-upper", "handle-cap", "handle-lower",
                         "heel", "belly", closed=True)
        self.add_line("bolster", SPINE_END, HANDLE_LOW)
        self.relate("connect", "knife", "bolster")
