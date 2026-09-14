"""Widened the crescent horns with shared radii and inset the top and cross ends.

VRECT_L: visible ink (6, 2, 42, 46). Upright envelope accommodates the object’s vertical construction.
Lucide venus: cardinal circle-to-stem attachment.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6f7cdbf8-30d8-5d08-bdb8-561dcf643682'
SOURCE_PATH = 'pictographic-primitives/culture/batch-05/astrology mercury_6f7cdbf8-30d8-5d08-bdb8-561dcf643682.svg'
AUTHOR = 'gpt-6'

class MercuryAstrologicalSymbolVariant2(Solo48):
    icon_id = 'mercury-astrological-symbol-v2'
    variant_of = 'mercury-astrological-symbol'
    variant_label = 'Exact keyshape envelope and clear spacing'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('mercury', 'astrology', 'planet', 'horns', 'symbol', 'horoscope', 'glyph', 'hermes')

    def build(self) -> None:
        self.add_arc('horn-left', (8, 4), (24, 12), radius_x=16, radius_y=8, sweep=False)
        self.add_arc('horn-right', (24, 12), (40, 4), radius_x=16, radius_y=8, sweep=False)
        self.add_contour('horns', 'horn-left', 'horn-right')
        self.add_arc('ring-right', (24, 12), (24, 34), radius_x=11)
        self.add_arc('ring-left', (24, 34), (24, 12), radius_x=11)
        self.add_contour('ring', 'ring-right', 'ring-left', closed=True)
        self.add_polyline('stem', (24, 34), (24, 40), (24, 44))
        self.add_polyline('crossbar', (16, 40), (24, 40), (32, 40))
        self.relate('connect', 'ring', 'horns')
        self.relate('connect', 'ring', 'stem')
        self.relate('connect', 'stem', 'crossbar')
