"""Four-ring cooktop seen from above.

Symbol plan: rounded-square hob (6..42, corner radius 6) holding a
2x2 grid of burners (6x6 rounded squares, corner r2) centred at 17/31 on both axes; ring to
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
        # Burner: 6x6 rounded square, corner radius 2, so the faces towards
        # the hob and towards each other are straight and certify at 8.
        h, c = 3, 2
        for i, (x, y) in enumerate(((17, 17), (31, 17), (17, 31), (31, 31))):
            x0, y0, x1, y1 = x - h, y - h, x + h, y + h
            self.add_line(f"burner-{i}-t", (x0 + c, y0), (x1 - c, y0))
            self.add_arc(f"burner-{i}-tr", (x1 - c, y0), (x1, y0 + c), radius_x=c)
            self.add_line(f"burner-{i}-r", (x1, y0 + c), (x1, y1 - c))
            self.add_arc(f"burner-{i}-br", (x1, y1 - c), (x1 - c, y1), radius_x=c)
            self.add_line(f"burner-{i}-b", (x1 - c, y1), (x0 + c, y1))
            self.add_arc(f"burner-{i}-bl", (x0 + c, y1), (x0, y1 - c), radius_x=c)
            self.add_line(f"burner-{i}-l", (x0, y1 - c), (x0, y0 + c))
            self.add_arc(f"burner-{i}-tl", (x0, y0 + c), (x0 + c, y0), radius_x=c)
            self.add_contour(f"burner-{i}", *(f"burner-{i}-{k}" for k in
                             ("t", "tr", "r", "br", "b", "bl", "l", "tl")), closed=True)
