'Gemini zodiac symbol.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7629f1dd-dc6f-5a09-a98f-f5af67d076a4'
SOURCE_PATH = 'pictographic-primitives/culture/batch-03/astrology gemini_7629f1dd-dc6f-5a09-a98f-f5af67d076a4.svg'
AUTHOR = 'gpt-6'

class GeminiZodiacSymbol(Solo48):
    icon_id = 'gemini-zodiac-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    categories = ('culture', 'primitives')
    aliases = ()
    keywords = ('gemini', 'zodiac', 'astrology', 'twins', 'horoscope', 'star sign', 'symbol', 'air')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_6_6 = (6, 6)
        p_17_10 = (17, 10)
        p_31_10 = (31, 10)
        p_42_6 = (42, 6)
        p_6_42 = (6, 42)
        p_17_38 = (17, 38)
        p_31_38 = (31, 38)
        p_42_42 = (42, 42)
        self.add_arc('top-left', p_6_6, p_17_10, radius_x=35, radius_y=35, sweep=False, large_arc=False)
        self.add_arc('top-middle', p_17_10, p_31_10, radius_x=49, radius_y=49, sweep=False, large_arc=False)
        self.add_arc('top-right', p_31_10, p_42_6, radius_x=35, radius_y=35, sweep=False, large_arc=False)
        self.add_arc('bottom-left', p_6_42, p_17_38, radius_x=35, radius_y=35, sweep=True, large_arc=False)
        self.add_arc('bottom-middle', p_17_38, p_31_38, radius_x=49, radius_y=49, sweep=True, large_arc=False)
        self.add_arc('bottom-right', p_31_38, p_42_42, radius_x=35, radius_y=35, sweep=True, large_arc=False)
        self.add_line('left', p_17_10, p_17_38)
        self.add_line('right', p_31_10, p_31_38)
        self.add_contour('top', 'top-left', 'top-middle', 'top-right', closed=False)
        self.add_contour('bottom', 'bottom-left', 'bottom-middle', 'bottom-right', closed=False)
        self.relate('connect', 'left', 'top')
        self.relate('connect', 'left', 'bottom')
        self.relate('connect', 'right', 'top')
        self.relate('connect', 'right', 'bottom')
