from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a926bc8d-1ac4-5954-820d-cc012466623f'
SOURCE_PATH = 'pictographic-primitives/culture/batch-07/astrology venus_a926bc8d-1ac4-5954-820d-cc012466623f.svg'
AUTHOR = 'gpt-6'

class VenusAstrologicalSymbolVariant2(Solo48):
    icon_id = 'venus-astrological-symbol-v2'
    variant_of = 'venus-astrological-symbol'
    variant_label = 'Exact keyshape envelope and clear spacing'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('venus', 'astrology', 'planet', 'symbol', 'horoscope', 'glyph', 'feminine', 'aphrodite')

    def build(self) -> None:
        self.add_arc('circle-right', (24, 4), (24, 30), radius_x=16, radius_y=13)
        self.add_arc('circle-left', (24, 30), (24, 4), radius_x=16, radius_y=13)
        self.add_contour('circle', 'circle-right', 'circle-left', closed=True)
        self.add_polyline('stem', (24, 30), (24, 38), (24, 44))
        self.add_polyline('crossbar', (16, 38), (24, 38), (32, 38))
        self.relate('connect', 'circle', 'stem')
        self.relate('connect', 'stem', 'crossbar')
