"""Mirrored ram horns, retaining the reference's open crests and pointed root."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '28ab2a14-d6a4-56d6-82df-af778631fe00'
SOURCE_PATH = 'pictographic-primitives/culture/batch-01/astrology aries_28ab2a14-d6a4-56d6-82df-af778631fe00.svg'


class AriesZodiacSymbol(Solo48):
    icon_id = 'aries-zodiac-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture"
    aliases = ()
    keywords = ('aries', 'zodiac', 'astrology', 'ram', 'horns', 'horoscope', 'star sign', 'symbol')

    def build(self) -> None:
        # SQUARE: visible extremes (0, 0, 48, 48); centerlines inset 2.
        self.add_arc("horn-left", (2,2), (24,46), radius_x=22, radius_y=44)
        self.add_arc("horn-right", (24,46), (46,2), radius_x=22, radius_y=44)
        self.add_contour("horns", "horn-left", "horn-right")
