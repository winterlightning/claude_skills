"""Four-ring cooktop seen from above.

Symbol plan: rounded-square hob (6..42, corner radius 6) holding a
2x2 grid of burner rings (r3) centred at 17/31 on both axes; ring to
frame and ring to ring are exactly 8 on centerlines.
Revision: the rejected drawing reduced the hob to four corner ticks, so
the rings floated without a cooktop; the reference shows a full rounded
frame around the burners. The reference's slightly larger top-left
burner is equalised: the 20-unit interior band only fits r3 rings.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "fe5dbe86-239a-46e3-b3d7-b5e5e06b7a81"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__four-ring-cooktop/20260927T153253Z-thuan-mac-1/reference/cooktop_fe5dbe86-239a-46e3-b3d7-b5e5e06b7a81.svg"
AUTHOR = "claude-opus-5-5"


class FourRingCooktop(Solo48):
    icon_id = "four-ring-cooktop"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/appliance"
    categories = ("primitives", "household")
    aliases = ("cooktop", "hob", "stove top")
    keywords = ("cooktop", "hob", "stove", "burner", "kitchen", "induction")

    def build(self) -> None:
        a, b, r = 6, 42, 6
        self.add_line("hob-top", (a + r, a), (b - r, a))
        self.add_arc("hob-tr", (b - r, a), (b, a + r), radius_x=r)
        self.add_line("hob-right", (b, a + r), (b, b - r))
        self.add_arc("hob-br", (b, b - r), (b - r, b), radius_x=r)
        self.add_line("hob-bottom", (b - r, b), (a + r, b))
        self.add_arc("hob-bl", (a + r, b), (a, b - r), radius_x=r)
        self.add_line("hob-left", (a, b - r), (a, a + r))
        self.add_arc("hob-tl", (a, a + r), (a + r, a), radius_x=r)
        self.add_contour("hob", "hob-top", "hob-tr", "hob-right", "hob-br",
                         "hob-bottom", "hob-bl", "hob-left", "hob-tl", closed=True)
        rr = 3
        for i, (x, y) in enumerate(((17, 17), (31, 17), (17, 31), (31, 31))):
            self.add_arc(f"burner-{i}-t", (x - rr, y), (x + rr, y), radius_x=rr)
            self.add_arc(f"burner-{i}-b", (x + rr, y), (x - rr, y), radius_x=rr)
            self.add_contour(f"burner-{i}", f"burner-{i}-t", f"burner-{i}-b", closed=True)
