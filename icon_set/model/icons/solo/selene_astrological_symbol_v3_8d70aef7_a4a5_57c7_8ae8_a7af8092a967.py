"""Moved the lunar arc as one unit and shortened the lower stem.

Keyshape VRECT_L: visible bounds (6, 2, 42, 46).
Reference: moon: coherent lunar curve.
"""
# Independent repair of selene-astrological-symbol; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8d70aef7-a4a5-57c7-8ae8-a7af8092a967'
SOURCE_PATH = 'pictographic-primitives/culture/batch-06/astrology selene_8d70aef7-a4a5-57c7-8ae8-a7af8092a967.svg'
AUTHOR = 'gpt-6'

class SeleneAstrologicalSymbolVariant3(Solo48):
    icon_id = 'selene-astrological-symbol-v3'
    variant_of = 'selene-astrological-symbol'
    variant_label = 'Fit current SOLO48 bounds and spacing'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('selene', 'astrology', 'moon', 'symbol', 'horoscope', 'glyph', 'lunar', 'goddess')

    # Symbol plan: retain the subject and shared attachment stations;
    # fit the current keyshape by adjusting the owning cap, base or repeat.
    def build(self) -> None:
        self.add_arc('upper-tip', (8, 8), (24, 4), radius_x=16, radius_y=4)
        self.add_arc('upper', (24, 4), (40, 20), radius_x=16)
        self.add_arc('lower', (40, 20), (24, 36), radius_x=16)
        self.add_arc('lower-tip', (24, 36), (8, 32), radius_x=16, radius_y=4)
        self.add_contour('moon', 'upper-tip', 'upper', 'lower', 'lower-tip')
        self.add_polyline('stem', (24, 36), (24, 40), (24, 44))
        self.add_polyline('crossbar', (17, 40), (24, 40), (31, 40))
        self.relate('connect', 'moon', 'stem')
        self.relate('connect', 'stem', 'crossbar')
