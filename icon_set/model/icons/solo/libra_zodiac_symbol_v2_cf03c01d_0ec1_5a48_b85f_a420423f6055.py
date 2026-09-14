# Variant of libra-zodiac-symbol; parent file remains unchanged.
"""Libra dome above a parallel baseline. Extremes (2,8)-(46,40). Mirrored arch, no useful Lucide subject match; no features dropped."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cf03c01d-0ec1-5a48-b85f-a420423f6055'
SOURCE_PATH = 'pictographic-primitives/culture/batch-04/astrology libra_cf03c01d-0ec1-5a48-b85f-a420423f6055.svg'
AUTHOR = 'gpt-6'

class LibraZodiacSymbolVariant2(Solo48):
    icon_id = 'libra-zodiac-symbol-v2'
    variant_of = 'libra-zodiac-symbol'
    variant_label = 'Correct width and full spacing review'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('libra', 'zodiac', 'astrology', 'scales', 'balance', 'horoscope', 'star sign', 'symbol')

    def build(self) -> None:
        self.add_line('left-arm', (4, 26), (12, 26))
        self.add_arc('dome', (12, 26), (36, 26), radius_x=13, large_arc=True)
        self.add_line('right-arm', (36, 26), (44, 26))
        self.add_contour('crown', 'left-arm', 'dome', 'right-arm')
        self.add_line('baseline', (4, 40), (44, 40))
