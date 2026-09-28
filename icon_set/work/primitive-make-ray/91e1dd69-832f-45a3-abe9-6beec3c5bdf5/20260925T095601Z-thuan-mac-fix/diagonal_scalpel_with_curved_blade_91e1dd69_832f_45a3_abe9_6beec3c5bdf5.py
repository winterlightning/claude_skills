"""Razor cut: a scalpel lying on the diagonal - rounded handle at the upper
right, a ferrule band, and a blade with a straight back and a curved belly
that sweeps to the point at the lower left.

Symbol plan: one closed outline on the 45-degree axis x+y=48. The handle end
is a radius-5 cap whose 3-4-5 points sit on the side lines x+y=41 (back) and
x+y=55 (belly side); the band is one cross line perpendicular to the axis,
sharing its end points with the outline; the blade back runs from the band to
the point (6,42), and the belly is one cubic arriving at the point nearly
horizontally, giving a sharp tip.
Keyshape SQUARE: cap top y=6 / right x=42, point (6,42).
Lucide construction: pipette / scalpel-like diagonal tool with a round end.
Revision of the rejected drawing ("Bad stroke drawn"): the old drawing had a
thick lumpy handle and a stubby blade; here the handle is straight-sided with
a true round end and the blade tapers to a point.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "91e1dd69-832f-45a3-abe9-6beec3c5bdf5"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__diagonal-scalpel-with-curved-blade/20260925T092544Z-thuan-mac/reference/razor cut_91e1dd69-832f-45a3-abe9-6beec3c5bdf5.svg"
AUTHOR = "claude-opus-5-5"

CAP = (37, 11)
CAP_R = 5
BAND_BACK = (24, 17)    # band end on the back line x+y=41
POINT = (6, 42)         # blade point, lowest and leftmost


class DiagonalScalpelWithCurvedBlade(Solo48):
    icon_id = "diagonal-scalpel-with-curved-blade"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("razor-cut", "scalpel")
    keywords = ("razor", "cut", "scalpel", "blade", "knife", "surgery", "craft")

    def build(self) -> None:
        cx, cy = CAP
        back_cap, belly_cap = (cx - 3, cy - 4), (cx + 4, cy + 3)
        band_belly = (BAND_BACK[0] + 7, BAND_BACK[1] + 7)
        self.add_arc("cap", back_cap, belly_cap, radius_x=CAP_R)
        self.add_line("handle-belly", belly_cap, band_belly)
        self.add_bezier("belly", band_belly, ((28, 32), (20, 40), POINT))
        self.add_line("back", POINT, BAND_BACK)
        self.add_line("handle-back", BAND_BACK, back_cap)
        self.add_contour("scalpel", "cap", "handle-belly", "belly",
                         "back", "handle-back", closed=True)
        self.add_line("band", BAND_BACK, band_belly)
        self.relate("connect", "scalpel", "band")
