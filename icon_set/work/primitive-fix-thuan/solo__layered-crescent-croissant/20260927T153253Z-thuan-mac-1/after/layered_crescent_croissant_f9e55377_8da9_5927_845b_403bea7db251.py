"""Layered crescent croissant (breakfast croissant).

Symbol plan: a fat crescent on the diagonal, convex towards the bottom-right
and mirror-symmetric about y=x like the reference. Three rolls: a big middle
layer between seams (33,15)-(42,26) and (15,33)-(26,42), set below the
line joining the horn tips so the top-left edge dips like a crescent, and two rolled horns.
Each horn rises from its seam along a convex inner edge that arrives flat at
the tip (38,6) (top extreme) and rounds over to a rightmost node (42,11) with
a vertical tangent (right extreme), then returns to the seam. The middle
layer bulges out on both faces. Every cubic keeps its controls inside the
keyshape, so the extremes are the integer nodes themselves.
Revision: the rejected drawing was a lumpy blob with a single seam that did
not read as a croissant; the reference is a fat crescent of layered rolls.
Reduced: the reference's five layers become three at 48 px (a second seam
per side would sit under 8 from the first).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f9e55377-8da9-5927-845b-403bea7db251"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__layered-crescent-croissant/20260927T153253Z-thuan-mac-1/reference/breakfast croissant_f9e55377-8da9-5927-845b-403bea7db251.svg"
AUTHOR = "claude-opus-5-5"


def _m(p):
    return (p[1], p[0])


class LayeredCrescentCroissant(Solo48):
    icon_id = "layered-crescent-croissant"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ("croissant", "breakfast croissant")
    keywords = ("croissant", "pastry", "bakery", "breakfast", "french", "crescent")

    def build(self) -> None:
        a2, b2, tip, rim = (33, 15), (42, 26), (38, 6), (42, 11)
        inner = ((34, 10), (35, 6), tip)          # seam -> tip, arrives flat
        crown = ((40, 6), (42, 8), rim)         # tip -> rightmost node
        back = ((42, 16), (42, 21), b2)          # rightmost node -> seam
        m = lambda seg: tuple(_m(p) for p in seg)
        rev = lambda start, seg: (seg[1], seg[0], start)

        # outline, clockwise from the right seam's inner end
        self.add_bezier("horn-right-inner", a2, inner)
        self.add_bezier("horn-right-crown", tip, crown)
        self.add_bezier("horn-right-back", rim, back)
        self.add_bezier("middle-outer", b2, ((42, 36), (36, 42), _m(b2)))
        self.add_bezier("horn-left-back", _m(b2), rev(_m(rim), m(back)))
        self.add_bezier("horn-left-crown", _m(rim), rev(_m(tip), m(crown)))
        self.add_bezier("horn-left-inner", _m(tip), rev(_m(a2), m(inner)))
        self.add_bezier("middle-inner", _m(a2), ((18, 26), (26, 18), a2))
        self.add_contour("pastry", "horn-right-inner", "horn-right-crown", "horn-right-back",
                         "middle-outer", "horn-left-back", "horn-left-crown",
                         "horn-left-inner", "middle-inner", closed=True)
        self.add_line("seam-right", a2, b2)
        self.add_line("seam-left", _m(a2), _m(b2))
        self.relate("connect", "pastry", "seam-right")
        self.relate("connect", "pastry", "seam-left")
