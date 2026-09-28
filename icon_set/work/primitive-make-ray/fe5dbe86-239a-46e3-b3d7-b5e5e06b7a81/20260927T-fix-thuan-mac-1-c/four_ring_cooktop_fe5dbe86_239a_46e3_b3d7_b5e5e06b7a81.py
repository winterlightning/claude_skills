"""Four-ring cooktop seen from above.

Symbol plan: rounded-square hob (6..42, corner radius 6) holding a
2x2 grid of burner rings (r3) centred at 17/31 on both axes; ring to
frame and ring to ring are exactly 8 on centerlines. The hob sides are
standalone straight lines joined to their corner arcs so the ring-to-
wall gap certifies at 8.
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
        parts = [
            ("line", "hob-top", (a + r, a), (b - r, a)),
            ("arc", "hob-tr", (b - r, a), (b, a + r)),
            ("line", "hob-right", (b, a + r), (b, b - r)),
            ("arc", "hob-br", (b, b - r), (b - r, b)),
            ("line", "hob-bottom", (b - r, b), (a + r, b)),
            ("arc", "hob-bl", (a + r, b), (a, b - r)),
            ("line", "hob-left", (a, b - r), (a, a + r)),
            ("arc", "hob-tl", (a, a + r), (a + r, a)),
        ]
        for kind, name, p, q in parts:
            if kind == "line":
                self.add_line(name, p, q)
            else:
                self.add_arc(name, p, q, radius_x=r)
        for i, part in enumerate(parts):
            self.relate("connect", part[1], parts[(i + 1) % len(parts)][1])
        rr = 3
        for i, (x, y) in enumerate(((17, 17), (31, 17), (17, 31), (31, 31))):
            self.add_arc(f"burner-{i}-1", (x, y - rr), (x + rr, y), radius_x=rr)
            self.add_arc(f"burner-{i}-2", (x + rr, y), (x, y + rr), radius_x=rr)
            self.add_arc(f"burner-{i}-3", (x, y + rr), (x - rr, y), radius_x=rr)
            self.add_arc(f"burner-{i}-4", (x - rr, y), (x, y - rr), radius_x=rr)
            self.add_contour(f"burner-{i}", *(f"burner-{i}-{k}" for k in range(1, 5)), closed=True)
