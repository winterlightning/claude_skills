"""A circle above a cross; bounds (11,2)-(37,46).

Construction reference: Lucide venus: circular head and centered cross.
Centerline extremes are the declared keyshape's exact bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a926bc8d-1ac4-5954-820d-cc012466623f'
SOURCE_PATH = 'pictographic-primitives/culture/batch-07/astrology venus_a926bc8d-1ac4-5954-820d-cc012466623f.svg'
AUTHOR = 'astra-chatgpt'


class VenusAstrologicalSymbol(Solo48):
    icon_id = 'venus-astrological-symbol'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('venus', 'astrology', 'planet', 'symbol', 'horoscope', 'glyph', 'feminine', 'aphrodite')

    def build(self) -> None:
        self.add_arc("circle-right", (24, 2), (24, 28), radius_x=13)
        self.add_arc("circle-left", (24, 28), (24, 2), radius_x=13)
        self.add_contour("circle", "circle-right", "circle-left", closed=True)
        self.add_polyline("stem", (24, 28), (24, 38), (24, 46))
        self.add_polyline("crossbar", (16, 38), (24, 38), (32, 38))
        self.relate("connect", "circle", "stem")
        self.relate("connect", "stem", "crossbar")
