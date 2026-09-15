'Uranus astrological symbol.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82a9c434-cbfe-590e-b3e9-a019a9763e16'
SOURCE_PATH = 'pictographic-primitives/culture/batch-07/astrology uranus_82a9c434-cbfe-590e-b3e9-a019a9763e16.svg'
AUTHOR = 'gpt-6'

class UranusAstrologicalSymbol(Solo48):
    icon_id = 'uranus-astrological-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('uranus', 'astrology', 'planet', 'symbol', 'horoscope', 'glyph', 'sky', 'air')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_24_31 = (24, 31)
        p_24_44 = (24, 44)
        p_24_4 = (24, 4)
        p_24_16 = (24, 16)
        p_15_16 = (15, 16)
        p_33_16 = (33, 16)
        p_8_4 = (8, 4)
        p_8_28 = (8, 28)
        p_40_4 = (40, 4)
        p_40_28 = (40, 28)
        self.add_arc('orb-right', p_24_31, p_24_44, radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('orb-left', p_24_44, p_24_31, radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('stem-1', p_24_4, p_24_16)
        self.add_line('stem-2', p_24_16, p_24_31)
        self.add_line('bar-1', p_15_16, p_24_16)
        self.add_line('bar-2', p_24_16, p_33_16)
        self.add_arc('left-top', p_8_4, p_15_16, radius_x=7, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('left-bottom', p_15_16, p_8_28, radius_x=7, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('right-top', p_40_4, p_33_16, radius_x=7, radius_y=12, sweep=False, large_arc=False)
        self.add_arc('right-bottom', p_33_16, p_40_28, radius_x=7, radius_y=12, sweep=False, large_arc=False)
        self.add_contour('orb', 'orb-right', 'orb-left', closed=True)
        self.add_contour('stem', 'stem-1', 'stem-2', closed=False)
        self.add_contour('bar', 'bar-1', 'bar-2', closed=False)
        self.add_contour('left', 'left-top', 'left-bottom', closed=False)
        self.add_contour('right', 'right-top', 'right-bottom', closed=False)
        self.relate('connect', 'left', 'bar')
        self.relate('connect', 'right', 'bar')
        self.relate('connect', 'stem', 'bar')
        self.relate('connect', 'stem', 'orb')
