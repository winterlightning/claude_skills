"""Scorpio M with a curved entry and arrow-ended tail. Bounds (2,2)-(46,46)."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3cf9ffb1-60a9-54fd-a8ae-b4088d1c0ab0'
SOURCE_PATH = 'pictographic-primitives/culture/batch-06/astrology scorpio_3cf9ffb1-60a9-54fd-a8ae-b4088d1c0ab0.svg'
AUTHOR = 'astra-chatgpt'


class ScorpioZodiacSymbol(Solo48):
    icon_id = 'scorpio-zodiac-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture"
    aliases = ()
    keywords = ('scorpio', 'zodiac', 'astrology', 'scorpion', 'sting', 'horoscope', 'star sign', 'symbol')

    def build(self) -> None:
        self.add_arc("entry", (2,2), (7,9), radius_x=5, radius_y=7)
        self.add_line("left-stem", (7,9), (7,32))
        self.add_contour("entry-stem", "entry", "left-stem")
        self.add_arc("first-hump", (7,9), (21,9), radius_x=7)
        self.add_line("middle-stem", (21,9), (21,32))
        self.add_contour("first", "first-hump", "middle-stem")
        self.add_arc("second-hump", (21,9), (35,9), radius_x=7)
        self.add_line("last-stem", (35,9), (35,32))
        self.add_arc("tail-turn", (35,32), (42,39), radius_x=7, sweep=False)
        self.add_line("tail", (42,39), (46,39))
        self.add_contour("second", "second-hump", "last-stem", "tail-turn", "tail")
        self.add_polyline("stinger", (39,32), (46,39), (39,46))
        self.relate("connect", "entry-stem", "first")
        self.relate("connect", "first", "second")
        self.relate("connect", "second", "stinger")
