# Variant of scorpio-zodiac-symbol; parent file remains unchanged.
"""Scorpio with equal circular humps and clear space beside the arrowhead. SQUARE bounds (2,2)-(46,46). The directional tail remains asymmetric. Lucide zodiac-scorpio informs equal circular humps, a quarter-circle tail bend and a longer horizontal run before the arrow."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3cf9ffb1-60a9-54fd-a8ae-b4088d1c0ab0'
SOURCE_PATH = 'pictographic-primitives/culture/batch-06/astrology scorpio_3cf9ffb1-60a9-54fd-a8ae-b4088d1c0ab0.svg'
AUTHOR = 'gpt-6'

class ScorpioZodiacSymbolVariant2(Solo48):
    icon_id = 'scorpio-zodiac-symbol-v2'
    variant_of = 'scorpio-zodiac-symbol'
    variant_label = 'Clearance beside arrowhead'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('scorpio', 'zodiac', 'astrology', 'scorpion', 'sting', 'horoscope', 'star sign', 'symbol')

    def build(self) -> None:
        # SQUARE (2,2)-(46,46); equal humps, wider arrow-to-stem gap.
        self.add_arc('entry', (2,2), (7,8), radius_x=5, radius_y=6)
        self.add_line('left-stem', (7,8), (7,32))
        self.add_contour('entry-stem', 'entry', 'left-stem')
        self.add_arc('first-hump', (7,8), (19,8), radius_x=6)
        self.add_line('middle-stem', (19,8), (19,32))
        self.add_contour('first', 'first-hump', 'middle-stem')
        self.add_arc('second-hump', (19,8), (31,8), radius_x=6)
        self.add_line('last-stem', (31,8), (31,32))
        self.add_arc('tail-turn', (31,32), (38,39), radius_x=7, sweep=False)
        self.add_line('tail', (38,39), (46,39))
        self.add_contour('second', 'second-hump', 'last-stem', 'tail-turn', 'tail')
        self.add_polyline('stinger', (39,32), (46,39), (39,46))
        self.relate('connect', 'entry-stem', 'first')
        self.relate('connect', 'first', 'second')
        self.relate('connect', 'second', 'stinger')
