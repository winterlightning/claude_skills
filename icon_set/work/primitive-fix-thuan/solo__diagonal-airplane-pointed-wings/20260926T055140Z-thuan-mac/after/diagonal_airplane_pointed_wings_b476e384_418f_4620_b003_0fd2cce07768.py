"""An airplane with long pointed swept wings, seen from above and flying diagonally up to the right.

Symbol plan: mirror-symmetric about the diagonal x + y = 48 (M(x, y) = (48 - y, 48 - x)).
The fuselage is a 45-degree tube between x + y = 41 and x + y = 55 with an r5 round nose
(3-4-5 end points about (37, 11)). Each main wing is a long swept triangle ending in a sharp
point at the keyshape corner (6, 8); each tail fin is a smaller triangle with a sharp tip,
and the two fins meet in a notch on the axis at (14, 34). The wing trailing edge sits more
than 8 from the fin root.
Lucide construction: 'plane' - diagonal fuselage with a round nose, swept wings and tail fins.
Keyshape SQUARE: centerline 6..42 (nose top 6 / right 42, pointed wing tips x 6 / y 42, fin tips x 6 / y 42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b476e384-418f-4620-b003-0fd2cce07768"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__diagonal-airplane-pointed-wings/20260926T055140Z-thuan-mac/reference/plane_b476e384-418f-4620-b003-0fd2cce07768.svg"
AUTHOR = "claude-opus-5-5"


def _m(p):
    return (48 - p[1], 48 - p[0])


class DiagonalAirplanePointedWings(Solo48):
    icon_id = "diagonal-airplane-pointed-wings"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transport"
    aliases = ("plane", "airplane", "aeroplane", "flight")
    keywords = ("plane", "airplane", "flight", "travel", "airport", "aviation", "jet", "trip")

    def build(self) -> None:
        nose_l, nose_r = (34, 7), (41, 14)
        # upper-left half, from the nose back to the tail notch
        upper = [nose_l, (29, 12), (6, 8), (21, 20), (15, 26), (6, 26), (14, 34)]
        lower = [_m(p) for p in upper]  # nose_r ... tail notch
        self.add_arc("nose", nose_l, nose_r, radius_x=5)
        names = ["nose"]
        # lower-right half: nose_r -> tail notch
        for i in range(len(lower) - 1):
            n = f"lower-{i + 1}"
            self.add_line(n, lower[i], lower[i + 1])
            names.append(n)
        # upper-left half back: tail notch -> nose_l
        rev = list(reversed(upper))
        for i in range(len(rev) - 1):
            n = f"upper-{len(rev) - 1 - i}"
            self.add_line(n, rev[i], rev[i + 1])
            names.append(n)
        self.add_contour("airplane", *names, closed=True)
