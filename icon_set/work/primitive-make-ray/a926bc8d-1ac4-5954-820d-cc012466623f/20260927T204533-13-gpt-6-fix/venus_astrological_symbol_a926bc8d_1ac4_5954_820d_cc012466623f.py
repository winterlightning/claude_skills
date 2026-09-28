"""Broadened the ring to a gentle oval and inset the stem, preserving the centered cross.

VRECT_L: visible ink (6, 2, 42, 46). Upright envelope accommodates the object’s vertical construction.
Lucide venus: centered ring and cross.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a926bc8d-1ac4-5954-820d-cc012466623f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__venus-astrological-symbol/20260927T133645Z-thuan-mac-1/reference/astrology venus_a926bc8d-1ac4-5954-820d-cc012466623f.svg'
AUTHOR = "gpt-6"

class VenusAstrologicalSymbol(Solo48):
    icon_id = 'venus-astrological-symbol'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    categories = ('culture', 'primitives')
    aliases = ()
    keywords = ('venus', 'astrology', 'planet', 'symbol', 'horoscope', 'glyph', 'feminine', 'aphrodite')

    def build(self) -> None:
        self.add_arc('circle-right', (24, 4), (24, 32), radius_x=14, radius_y=14)
        self.add_arc('circle-left', (24, 32), (24, 4), radius_x=14, radius_y=14)
        self.add_contour('circle', 'circle-right', 'circle-left', closed=True)
        self.add_polyline('stem', (24, 32), (24, 38), (24, 44))
        self.add_polyline('crossbar', (18, 38), (24, 38), (30, 38))
        self.relate('connect', 'circle', 'stem')
        self.relate('connect', 'stem', 'crossbar')
