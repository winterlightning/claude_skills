'Pisces zodiac symbol.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'def8aba9-0520-5c6a-9e0d-92c25af53243'
SOURCE_PATH = 'pictographic-primitives/culture/batch-05/astrology cancer_def8aba9-0520-5c6a-9e0d-92c25af53243.svg'
AUTHOR = 'gpt-6'

class PiscesZodiacSymbol(Solo48):
    icon_id = 'pisces-zodiac-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    categories = ('culture', 'primitives')
    aliases = ()
    keywords = ('pisces', 'zodiac', 'astrology', 'fish', 'horoscope', 'star sign', 'symbol', 'water')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_8_4 = (8, 4)
        p_16_24 = (16, 24)
        p_8_44 = (8, 44)
        p_40_4 = (40, 4)
        p_32_24 = (32, 24)
        p_40_44 = (40, 44)
        p_10_24 = (10, 24)
        p_38_24 = (38, 24)
        self.add_arc('left-top', p_8_4, p_16_24, radius_x=8, radius_y=20, sweep=True, large_arc=False)
        self.add_arc('left-bottom', p_16_24, p_8_44, radius_x=8, radius_y=20, sweep=True, large_arc=False)
        self.add_arc('right-top', p_40_4, p_32_24, radius_x=8, radius_y=20, sweep=False, large_arc=False)
        self.add_arc('right-bottom', p_32_24, p_40_44, radius_x=8, radius_y=20, sweep=False, large_arc=False)
        self.add_line('bar-1', p_10_24, p_16_24)
        self.add_line('bar-2', p_16_24, p_32_24)
        self.add_line('bar-3', p_32_24, p_38_24)
        self.add_contour('left', 'left-top', 'left-bottom', closed=False)
        self.add_contour('right', 'right-top', 'right-bottom', closed=False)
        self.add_contour('bar', 'bar-1', 'bar-2', 'bar-3', closed=False)
        self.relate('connect', 'bar', 'left')
        self.relate('connect', 'bar', 'right')
