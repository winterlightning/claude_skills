'Leo zodiac symbol.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f909b4b5-36ec-56b9-97c5-2e94aec05d2b'
SOURCE_PATH = 'pictographic-primitives/culture/batch-04/astrology leo_f909b4b5-36ec-56b9-97c5-2e94aec05d2b.svg'
AUTHOR = 'gpt-6'

class LeoZodiacSymbol(Solo48):
    icon_id = 'leo-zodiac-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('leo', 'zodiac', 'astrology', 'lion', 'mane', 'horoscope', 'star sign', 'symbol')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_18_38 = (18, 38)
        p_8_38 = (8, 38)
        p_15_17 = (15, 17)
        p_33_17 = (33, 17)
        p_30_38 = (30, 38)
        p_40_38 = (40, 38)
        self.add_arc('loop-top', p_18_38, p_8_38, radius_x=5, radius_y=6, sweep=False, large_arc=False)
        self.add_arc('loop-bottom', p_8_38, p_18_38, radius_x=5, radius_y=6, sweep=False, large_arc=False)
        self.add_line('rise', p_18_38, p_15_17)
        self.add_arc('arch', p_15_17, p_33_17, radius_x=9, radius_y=13, sweep=True, large_arc=False)
        self.add_line('fall', p_33_17, p_30_38)
        self.add_arc('tail', p_30_38, p_40_38, radius_x=5, radius_y=6, sweep=False, large_arc=False)
        self.add_contour('loop', 'loop-top', 'loop-bottom', closed=True)
        self.add_contour('mane', 'rise', 'arch', 'fall', 'tail', closed=False)
        self.relate('connect', 'loop', 'mane')
