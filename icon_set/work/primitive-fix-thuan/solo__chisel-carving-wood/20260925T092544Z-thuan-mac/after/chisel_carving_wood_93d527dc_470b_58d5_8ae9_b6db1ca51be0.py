"""Wood carving: a chisel held diagonally, its blade cutting a groove into the
top of a wooden block.

Symbol plan: the handle is a pill on the 45-degree axis x+y=48 with two
radius-5 caps whose 3-4-5 end points sit on the side lines x+y=41 and x+y=55;
the blade leaves the lower cap at its 3-4-5 point (27,20) and runs parallel to
the axis to the groove's lowest point (13,34), where it genuinely touches the
wood (declared connection). The block is closed: wavy carved top, straight
sides and base.
Keyshape SQUARE: block x=6..42 and base y=42, handle cap top y=6.
Lucide construction: pipette-like diagonal pill with round caps for the
handle; square block for the wood.
Revision of the rejected drawing ("Bad stroke drawn"): the old drawing had two
heavy loops for the chisel and a lumpy block; here the chisel is a clean pill
handle with a straight blade touching the carved groove.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "93d527dc-470b-58d5-8ae9-b6db1ca51be0"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__chisel-carving-wood/20260925T092544Z-thuan-mac/reference/wood carving_93d527dc-470b-58d5-8ae9-b6db1ca51be0.svg"
AUTHOR = "claude-opus-5-5"

CAP_TOP = (37, 11)      # upper handle cap centre
CAP_LOW = (31, 17)      # lower handle cap centre
CAP_R = 5
GROOVE = (13, 34)       # lowest point of the carved groove, where the blade bites
WOOD_TOP = 31
WOOD = (6, 42, 42)      # left, right, base


class ChiselCarvingWood(Solo48):
    icon_id = "chisel-carving-wood"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("wood-carving",)
    keywords = ("wood", "carving", "chisel", "woodwork", "craft", "tool")

    def build(self) -> None:
        (tx, ty), (lx, ly) = CAP_TOP, CAP_LOW
        self.add_arc("handle-top", (tx - 3, ty - 4), (tx + 4, ty + 3), radius_x=CAP_R)
        self.add_line("handle-lower-side", (tx + 4, ty + 3), (lx + 3, ly + 4))
        self.add_arc("handle-bottom-a", (lx + 3, ly + 4), (lx - 4, ly + 3), radius_x=CAP_R)
        self.add_arc("handle-bottom-b", (lx - 4, ly + 3), (lx - 4, ly - 3), radius_x=CAP_R)
        self.add_line("handle-upper-side", (lx - 4, ly - 3), (tx - 3, ty - 4))
        self.add_contour("handle", "handle-top", "handle-lower-side", "handle-bottom-a",
                         "handle-bottom-b", "handle-upper-side", closed=True)

        self.add_line("blade", (lx - 4, ly + 3), GROOVE)
        self.relate("connect", "handle", "blade")

        left, right, base = WOOD
        gx, gy = GROOVE
        self.add_line("wood-left", (left, base), (left, WOOD_TOP))
        self.add_bezier("wood-groove-in", (left, WOOD_TOP), ((8.5, WOOD_TOP), (10, gy), GROOVE))
        self.add_bezier("wood-groove-out", GROOVE, ((16.5, gy), (18.5, WOOD_TOP), (23, WOOD_TOP)))
        self.add_line("wood-top", (23, WOOD_TOP), (right, WOOD_TOP))
        self.add_line("wood-right", (right, WOOD_TOP), (right, base))
        self.add_line("wood-base", (right, base), (left, base))
        self.add_contour("wood", "wood-left", "wood-groove-in", "wood-groove-out", "wood-top",
                         "wood-right", "wood-base", closed=True)
        self.relate("connect", "blade", "wood")
