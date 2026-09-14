"""Shortened the stem and sickle extent, keeping the asymmetric hook.

Keyshape VRECT_L: visible bounds (6, 2, 42, 46).
Reference: No useful exact match.
"""
# Independent repair of saturn-astrological-symbol; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '235ce74c-a58a-5d23-8b5c-93f02e58c975'
SOURCE_PATH = 'pictographic-primitives/culture/batch-06/astrology saturn_235ce74c-a58a-5d23-8b5c-93f02e58c975.svg'
AUTHOR = 'gpt-6'

class SaturnAstrologicalSymbolVariant3(Solo48):
    icon_id = 'saturn-astrological-symbol-v3'
    variant_of = 'saturn-astrological-symbol'
    variant_label = 'Fit current SOLO48 bounds and spacing'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('saturn', 'astrology', 'planet', 'scythe', 'symbol', 'horoscope', 'glyph', 'cronus')

    # Symbol plan: retain the subject and shared attachment stations;
    # fit the current keyshape by adjusting the owning cap, base or repeat.
    def build(self) -> None:
        self.add_line('stem-top', (16, 4), (16, 10))
        self.add_line('stem-bottom', (16, 10), (16, 22))
        self.add_polyline('crossbar', (8, 10), (16, 10), (28, 10))
        self.add_arc('shoulder', (16, 22), (40, 22), radius_x=12, radius_y=7)
        self.add_arc('sickle', (40, 22), (16, 44), radius_x=24, radius_y=22)
        self.add_contour('saturn', 'stem-top', 'stem-bottom', 'shoulder', 'sickle')
        self.relate('connect', 'saturn', 'crossbar')
