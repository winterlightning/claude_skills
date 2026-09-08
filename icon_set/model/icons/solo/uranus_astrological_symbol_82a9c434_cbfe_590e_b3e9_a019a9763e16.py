"""Uranus with paired crescent arms and lower orb; bounds (5,2)-(43,46).

Construction reference: Lucide venus for attached circular orb; paired elliptical arms follow supplied reference.
Centerline extremes are the declared keyshape's exact bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82a9c434-cbfe-590e-b3e9-a019a9763e16'
SOURCE_PATH = 'pictographic-primitives/culture/batch-07/astrology uranus_82a9c434-cbfe-590e-b3e9-a019a9763e16.svg'


class UranusAstrologicalSymbol(Solo48):
    icon_id = 'uranus-astrological-symbol'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('uranus', 'astrology', 'planet', 'symbol', 'horoscope', 'glyph', 'sky', 'air')

    def build(self) -> None:
        self.add_arc("orb-right", (24, 32), (24, 46), radius_x=7)
        self.add_arc("orb-left", (24, 46), (24, 32), radius_x=7)
        self.add_contour("orb", "orb-right", "orb-left", closed=True)
        self.add_polyline("stem", (24, 2), (24, 15), (24, 32))
        self.add_polyline("bar", (13, 15), (24, 15), (35, 15))
        for side, x, mid, sweep in (("left", 5, 13, True), ("right", 43, 35, False)):
            self.add_arc(side+"-top", (x, 2), (mid, 15), radius_x=8, radius_y=13, sweep=sweep)
            self.add_arc(side+"-bottom", (mid, 15), (x, 28), radius_x=8, radius_y=13, sweep=sweep)
            self.add_contour(side, side+"-top", side+"-bottom")
            self.relate("connect", side, "bar")
        self.relate("connect", "stem", "bar")
        self.relate("connect", "stem", "orb")
