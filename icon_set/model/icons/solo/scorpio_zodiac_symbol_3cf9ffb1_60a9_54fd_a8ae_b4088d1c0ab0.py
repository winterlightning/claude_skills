"""Lowered both equal humps together; preserved the directional sting.

Keyshape SQUARE: visible bounds (4, 4, 44, 44).
Reference: No useful inspected exact match.
"""
# Independent repair of scorpio-zodiac-symbol-v2; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3cf9ffb1-60a9-54fd-a8ae-b4088d1c0ab0'
SOURCE_PATH = 'pictographic-primitives/culture/batch-06/astrology scorpio_3cf9ffb1-60a9-54fd-a8ae-b4088d1c0ab0.svg'
AUTHOR = 'gpt-6'

class ScorpioZodiacSymbol(Solo48):
    icon_id = 'scorpio-zodiac-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('scorpio', 'zodiac', 'astrology', 'scorpion', 'sting', 'horoscope', 'star sign', 'symbol')

    # Symbol plan: retain the subject and shared attachment stations;
    # fit the current keyshape by adjusting the owning cap, base or repeat.
    def build(self) -> None:
        self.add_arc('entry', (6, 6), (7, 12), radius_x=5, radius_y=6)
        self.add_line('left-stem', (7, 12), (7, 32))
        self.add_contour('entry-stem', 'entry', 'left-stem')
        self.add_arc('first-hump', (7, 12), (19, 12), radius_x=6)
        self.add_line('middle-stem', (19, 12), (19, 32))
        self.add_contour('first', 'first-hump', 'middle-stem')
        self.add_arc('second-hump', (19, 12), (31, 12), radius_x=6)
        self.add_line('last-stem', (31, 12), (31, 32))
        self.add_arc('tail-turn', (31, 32), (38, 39), radius_x=7, sweep=False)
        self.add_line('tail', (38, 39), (42, 39))
        self.add_contour('second', 'second-hump', 'last-stem', 'tail-turn', 'tail')
        self.add_polyline('stinger', (39, 32), (42, 39), (39, 42))
        self.relate('connect', 'entry-stem', 'first')
        self.relate('connect', 'first', 'second')
        self.relate('connect', 'second', 'stinger')
