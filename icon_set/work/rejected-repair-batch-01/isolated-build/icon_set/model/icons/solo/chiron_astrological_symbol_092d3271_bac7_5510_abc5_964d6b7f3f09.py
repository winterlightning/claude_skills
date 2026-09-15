"""Widened the key bow and inset the stem and bow ends on VRECT_L.

VRECT_L: visible ink (6, 2, 42, 46). Upright envelope accommodates the object’s vertical construction.
No useful exact local Lucide match; retained the inspected parent silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '092d3271-bac7-5510-abc5-964d6b7f3f09'
SOURCE_PATH = 'pictographic-primitives/culture/batch-01/astrology chiron_092d3271-bac7-5510-abc5-964d6b7f3f09.svg'
AUTHOR = 'gpt-6'

class ChironAstrologicalSymbol(Solo48):
    icon_id = 'chiron-astrological-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('chiron', 'astrology', 'key', 'symbol', 'asteroid', 'horoscope', 'glyph', 'healing')

    def build(self) -> None:
        self.add_arc('ring-right', (24, 24), (24, 44), radius_x=16, radius_y=10)
        self.add_arc('ring-left', (24, 44), (24, 24), radius_x=16, radius_y=10)
        self.add_contour('ring', 'ring-right', 'ring-left', closed=True)
        self.add_polyline('stem', (24, 4), (24, 12), (24, 24))
        self.add_polyline('branches', (36, 4), (24, 12), (36, 20))
        self.relate('connect', 'stem', 'ring')
        self.relate('connect', 'stem', 'branches')
