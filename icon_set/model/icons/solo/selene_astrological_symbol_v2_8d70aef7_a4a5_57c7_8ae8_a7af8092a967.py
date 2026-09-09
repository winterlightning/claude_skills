# Variant of selene-astrological-symbol; parent file remains unchanged.
"""A true right semicircle over a cross. VRECT_L centerline bounds (8,2)-(40,46). The crossbar supplies the left extreme. No useful local Lucide subject match; circular arcs replace flattened lunar tips."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8d70aef7-a4a5-57c7-8ae8-a7af8092a967'
SOURCE_PATH = 'pictographic-primitives/culture/batch-06/astrology selene_8d70aef7-a4a5-57c7-8ae8-a7af8092a967.svg'
AUTHOR = 'gpt-6'

class SeleneAstrologicalSymbolVariant2(Solo48):
    icon_id = 'selene-astrological-symbol-v2'
    variant_of = 'selene-astrological-symbol'
    variant_label = 'True semicircular moon'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('selene', 'astrology', 'moon', 'symbol', 'horoscope', 'glyph', 'lunar', 'goddess')

    def build(self) -> None:
        # VRECT_L extremes (8,2)-(40,46); a true right semicircle.
        self.add_arc('moon-top', (24,2), (40,18), radius_x=16)
        self.add_arc('moon-bottom', (40,18), (24,34), radius_x=16)
        self.add_contour('moon', 'moon-top', 'moon-bottom')
        self.add_polyline('stem', (24,34), (24,40), (24,46))
        self.add_polyline('crossbar', (8,40), (24,40), (40,40))
        self.relate('connect', 'moon', 'stem')
        self.relate('connect', 'stem', 'crossbar')
