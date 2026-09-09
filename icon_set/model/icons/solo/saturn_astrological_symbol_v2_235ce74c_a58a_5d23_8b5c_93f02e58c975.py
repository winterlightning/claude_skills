# Variant of saturn-astrological-symbol; parent file remains unchanged.
"""Saturn with a lowered curved shoulder to open the gap below the crossbar. VRECT_L bounds (8,2)-(40,46). Preserve the directional scythe; no useful local Lucide subject match."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '235ce74c-a58a-5d23-8b5c-93f02e58c975'
SOURCE_PATH = 'pictographic-primitives/culture/batch-06/astrology saturn_235ce74c-a58a-5d23-8b5c-93f02e58c975.svg'
AUTHOR = 'gpt-6'

class SaturnAstrologicalSymbolVariant2(Solo48):
    icon_id = 'saturn-astrological-symbol-v2'
    variant_of = 'saturn-astrological-symbol'
    variant_label = 'Open crossbar clearance'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('saturn', 'astrology', 'planet', 'scythe', 'symbol', 'horoscope', 'glyph', 'cronus')

    def build(self) -> None:
        self.add_line('stem-top', (16, 2), (16, 10))
        self.add_line('stem-bottom', (16, 10), (16, 26))
        self.add_polyline('crossbar', (8, 10), (16, 10), (28, 10))
        self.add_arc('shoulder', (16, 26), (40, 26), radius_x=12, radius_y=7)
        self.add_arc('sickle', (40, 26), (16, 46), radius_x=24, radius_y=20)
        self.add_contour('saturn', 'stem-top', 'stem-bottom', 'shoulder', 'sickle')
        self.relate('connect', 'saturn', 'crossbar')
