"""A corgi head silhouette: big rounded upright ears, a flat crown, cheek notches and the neck, open at the bottom.

Symbol plan: one open outline, symmetric about x=24, left to right: the left neck side
rises to the cheek notch; the ear's outer edge bulges out to its widest point (x=6) and
rounds over the tip (y=6); the inner edge sweeps down to the flat crown; then the same
mirrored. Every extreme is an integer bezier knot with an axis tangent, so the ears
meet the envelope exactly.
Lucide construction: 'cat'/'dog' head outline with upright ears.
Keyshape SQUARE: centerline x 6..42 (ear bulges), y 6..42 (ear tips, neck).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "c75020d7-8516-4fa5-af3e-737a8f244554"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__corgi-head-silhouette/20260926T044250Z-thuan-mac/reference/corgi_c75020d7-8516-4fa5-af3e-737a8f244554.svg"
AUTHOR = "claude-opus-5-5"


def _m(p):
    return (48 - p[0], p[1])


class CorgiHeadSilhouette(Solo48):
    icon_id = "corgi-head-silhouette"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/pets"
    aliases = ("corgi", "dog head", "corgi silhouette")
    keywords = ("corgi", "dog", "ears", "pet", "puppy", "head", "silhouette", "animal", "breed")

    def build(self) -> None:
        base, notch, wide, tip, crown = (7, 42), (12, 24), (6, 12), (11, 6), (19, 15)
        self.add_bezier("neck-l", base, ((8, 34), (10, 28), notch))
        self.add_bezier("ear-outer-l", notch, ((8, 21), (6, 17), wide), ((6, 8), (8, 6), tip))
        self.add_bezier("ear-inner-l", tip, ((14, 6), (16, 12), crown))
        self.add_line("crown", crown, _m(crown))
        self.add_bezier("ear-inner-r", _m(crown), (_m((16, 12)), _m((14, 6)), _m(tip)))
        self.add_bezier("ear-outer-r", _m(tip), (_m((8, 6)), _m((6, 8)), _m(wide)),
                        (_m((6, 17)), _m((8, 21)), _m(notch)))
        self.add_bezier("neck-r", _m(notch), (_m((10, 28)), _m((8, 34)), _m(base)))
        self.add_contour("head", "neck-l", "ear-outer-l", "ear-inner-l", "crown", "ear-inner-r",
                         "ear-outer-r", "neck-r")
