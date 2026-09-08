"""Capricorn with an angular left stroke, descending tail and open circular loop."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f5e70bca-f373-5831-8f15-24890eb86b22'
SOURCE_PATH = 'pictographic-primitives/culture/batch-01/astrology capricorn_f5e70bca-f373-5831-8f15-24890eb86b22.svg'
AUTHOR = 'astra-chatgpt'


class CapricornZodiacSymbol(Solo48):
    icon_id = 'capricorn-zodiac-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture"
    aliases = ()
    keywords = ('capricorn', 'zodiac', 'astrology', 'goat', 'sea goat', 'horoscope', 'star sign', 'symbol')

    def build(self) -> None:
        # HRECT_L: visible extremes (0, 6, 48, 42); centerlines inset 2.
        self.add_arc("left-crest", (2,8), (10,16), radius_x=8)
        self.add_line("left-downstroke", (10,16), (14,30))
        self.add_line("upstroke", (14,30), (26,10))
        self.add_arc("right-crest", (26,10), (30,14), radius_x=4)
        self.add_line("downstroke", (30,14), (30,30))
        self.add_arc("tail-curve", (30,30), (20,40), radius_x=10)
        self.add_line("tail-tip", (20,40), (18,40))
        self.add_contour("body", "left-crest", "left-downstroke", "upstroke", "right-crest", "downstroke", "tail-curve", "tail-tip")
        self.add_arc("loop-upper", (30,30), (46,30), radius_x=8)
        self.add_arc("loop-lower", (46,30), (30,30), radius_x=8)
        self.add_contour("loop", "loop-upper", "loop-lower", closed=True)
        self.relate("connect", "body", "loop")
