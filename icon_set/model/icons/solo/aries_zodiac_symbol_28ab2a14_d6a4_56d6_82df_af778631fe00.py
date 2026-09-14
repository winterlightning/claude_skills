'Aries zodiac symbol.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '28ab2a14-d6a4-56d6-82df-af778631fe00'
SOURCE_PATH = 'pictographic-primitives/culture/batch-01/astrology aries_28ab2a14-d6a4-56d6-82df-af778631fe00.svg'
AUTHOR = 'gpt-6'

class AriesZodiacSymbol(Solo48):
    icon_id = 'aries-zodiac-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('aries', 'zodiac', 'astrology', 'ram', 'horns', 'horoscope', 'star sign', 'symbol')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_6_6 = (6, 6)
        p_24_42 = (24, 42)
        p_42_6 = (42, 6)
        self.add_arc('horn-left', p_6_6, p_24_42, radius_x=18, radius_y=36, sweep=True, large_arc=False)
        self.add_arc('horn-right', p_24_42, p_42_6, radius_x=18, radius_y=36, sweep=True, large_arc=False)
        self.add_contour('horns', 'horn-left', 'horn-right', closed=False)
