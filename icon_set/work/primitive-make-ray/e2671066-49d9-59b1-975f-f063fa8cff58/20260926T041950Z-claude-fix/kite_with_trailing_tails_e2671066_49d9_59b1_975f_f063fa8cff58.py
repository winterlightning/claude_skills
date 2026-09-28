"""A kite flying: a diamond kite at the top-right with a cross spar, and two wavy tails
trailing from its lower point.

Symbol plan: the kite is a near-square quadrilateral TL=(18,8), TR=(42,6), BR=(40,28),
BL=(16,30) with both spars crossing at M=(29,18), so its four triangles stay open at
48px as in the reference. Two S-curved tails leave the lower-left corner BL: one trailing
left, one hanging down, diverging at about 110 degrees.
Lucide construction: 'kite' - quadrilateral kite with crossed spars and a wavy tail.
Keyshape SQUARE: centerline x 6..42 (left tail end, top-right corner), y 6..42 (top-right
corner, lower tail end).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e2671066-49d9-59b1-975f-f063fa8cff58"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__kite-with-trailing-tails/20260926T035939Z-thuan-mac/reference/outdoors kite flying_e2671066-49d9-59b1-975f-f063fa8cff58.svg"
AUTHOR = "claude-opus-5-5"


class KiteWithTrailingTails(Solo48):
    icon_id = "kite-with-trailing-tails"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "outdoors/leisure"
    aliases = ("outdoors-kite-flying", "kite", "kite-flying")
    keywords = ("kite", "flying", "wind", "outdoors", "toy", "summer", "sky", "play", "tail")

    def build(self) -> None:
        TL, TR, BR, BL = (18, 8), (42, 6), (40, 28), (16, 30)
        M = (29, 18)
        self.add_polyline("kite", TL, TR, BR, BL, closed=True)
        self.add_polyline("spar-long", BL, M, TR)
        self.add_polyline("spar-cross", TL, M, BR)
        self.relate("connect", "kite", "spar-long")
        self.relate("connect", "kite", "spar-cross")
        self.relate("connect", "spar-long", "spar-cross")
        self.add_bezier("tail-left", BL, ((10, 29), (10, 35), (6, 38)))
        self.add_bezier("tail-down", BL, ((19, 34), (17, 38), (20, 42)))
        self.relate("connect", "kite", "tail-left")
        self.relate("connect", "kite", "tail-down")
        self.relate("connect", "tail-left", "tail-down")
