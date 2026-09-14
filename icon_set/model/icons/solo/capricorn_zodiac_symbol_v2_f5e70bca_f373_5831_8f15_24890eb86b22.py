# Variant of capricorn-zodiac-symbol; parent file remains unchanged.
'capricorn-zodiac-symbol: Repositioned the outer contours to the exact keyshape width while retaining the defining details. Keyshape HRECT_L; SOLO48 stroke 4. Reviewed at 48 px in both themes.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f5e70bca-f373-5831-8f15-24890eb86b22'
SOURCE_PATH = 'pictographic-primitives/culture/batch-01/astrology capricorn_f5e70bca-f373-5831-8f15-24890eb86b22.svg'
AUTHOR = 'gpt-6'

class CapricornZodiacSymbolVariant2(Solo48):
    icon_id = 'capricorn-zodiac-symbol-v2'
    variant_of = 'capricorn-zodiac-symbol'
    variant_label = 'Correct width and full spacing review'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('capricorn', 'zodiac', 'astrology', 'goat', 'sea goat', 'horoscope', 'star sign', 'symbol')

    def build(self) -> None:
        self.add_arc('left-crest', (4, 8), (12, 16), radius_x=8)
        self.add_line('left-downstroke', (12, 16), (14, 30))
        self.add_line('upstroke', (14, 30), (26, 10))
        self.add_arc('right-crest', (26, 10), (30, 14), radius_x=4)
        self.add_line('downstroke', (30, 14), (30, 30))
        self.add_arc('tail-curve', (30, 30), (20, 40), radius_x=10)
        self.add_line('tail-tip', (20, 40), (18, 40))
        self.add_contour('body', 'left-crest', 'left-downstroke', 'upstroke', 'right-crest', 'downstroke', 'tail-curve', 'tail-tip')
        self.add_arc('loop-upper', (30, 30), (44, 30), radius_x=7)
        self.add_arc('loop-lower', (44, 30), (30, 30), radius_x=7)
        self.add_contour('loop', 'loop-upper', 'loop-lower', closed=True)
        self.relate('connect', 'body', 'loop')
