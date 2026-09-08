"""Mercury: crescent horns, circular body, and lower cross.

Construction: Lucide venus: circle attached at its cardinal point to a simple cross.
Keyshape VRECT_M; centerline extremes are the visible bounds inset by 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6f7cdbf8-30d8-5d08-bdb8-561dcf643682'
SOURCE_PATH = 'pictographic-primitives/culture/batch-05/astrology mercury_6f7cdbf8-30d8-5d08-bdb8-561dcf643682.svg'
AUTHOR = 'astra-chatgpt'


class MercuryAstrologicalSymbol(Solo48):
    icon_id = 'mercury-astrological-symbol'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('mercury', 'astrology', 'planet', 'horns', 'symbol', 'horoscope', 'glyph', 'hermes')

    def build(self) -> None:
        self.add_arc("horn-left", (11,2), (24,12), radius_x=13, radius_y=10, sweep=False)
        self.add_arc("horn-right", (24,12), (37,2), radius_x=13, radius_y=10, sweep=False)
        self.add_contour("horns", "horn-left", "horn-right")
        self.add_arc("ring-right", (24,12), (24,34), radius_x=11)
        self.add_arc("ring-left", (24,34), (24,12), radius_x=11)
        self.add_contour("ring", "ring-right", "ring-left", closed=True)
        self.add_polyline("stem", (24,34), (24,40), (24,46))
        self.add_polyline("crossbar", (16,40), (24,40), (32,40))
        self.relate("connect", "ring", "horns")
        self.relate("connect", "ring", "stem")
        self.relate("connect", "stem", "crossbar")
