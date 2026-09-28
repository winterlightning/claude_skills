"""Layered crescent croissant (breakfast croissant).

Symbol plan: a crescent on the diagonal, convex towards the bottom-right and
mirror-symmetric about y=x like the reference. Inner (concave) edge = r25 arc
about (6,6) from horn tip (31,6) to horn tip (6,31). Body = r30 quarter arc
about (12,12) from (42,12) to (12,42) (exact right and bottom extremes).
Each horn is a cubic from the body end to its tip whose controls never cross
the keyshape edge, so the tips land exactly on y=6 / x=6 and meet the inner
edge at a point. Two seams (30,13)-(42,12) and (13,30)-(12,42) divide the
rolled horns from the big middle layer.
Revision: the rejected drawing was a lumpy blob with a single seam that did
not read as a crescent; the reference is a crescent of layered rolls.
Reduced: the reference's five layers become three (a seam pair nearer the
middle would sit under 8 apart).
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
        tip, seam_in, body_end = (31, 6), (30, 13), (42, 12)
        c1, c2 = (42, 8), (35, 6)
        # outline: right tip -> inner edge -> left tip -> left horn -> body -> right horn
        self.add_arc("inner-right", tip, seam_in, radius_x=25, sweep=True)
        self.add_arc("inner-middle", seam_in, _m(seam_in), radius_x=25, sweep=True)
        self.add_arc("inner-left", _m(seam_in), _m(tip), radius_x=25, sweep=True)
        self.add_bezier("horn-left", _m(tip), (_m(c2), _m(c1), _m(body_end)))
        self.add_arc("body", _m(body_end), body_end, radius_x=30, sweep=False)
        self.add_bezier("horn-right", body_end, (c1, c2, tip))
        self.add_contour("pastry", "inner-right", "inner-middle", "inner-left",
                         "horn-left", "body", "horn-right", closed=True)
        self.add_line("seam-right", seam_in, body_end)
        self.add_line("seam-left", _m(seam_in), _m(body_end))
        self.relate("connect", "pastry", "seam-right")
        self.relate("connect", "pastry", "seam-left")
