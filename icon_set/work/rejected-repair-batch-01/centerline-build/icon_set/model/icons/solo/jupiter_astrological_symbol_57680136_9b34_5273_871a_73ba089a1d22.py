'Jupiter astrological symbol.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '57680136-9b34-5273-871a-73ba089a1d22'
SOURCE_PATH = 'pictographic-primitives/culture/batch-04/astrology jupiter_57680136-9b34-5273-871a-73ba089a1d22.svg'
AUTHOR = 'gpt-6'

class JupiterAstrologicalSymbol(Solo48):
    icon_id = 'jupiter-astrological-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('jupiter', 'astrology', 'planet', 'symbol', 'horoscope', 'glyph', 'zeus', 'expansion')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_8_4 = (8, 4)
        p_14_4 = (14, 4)
        p_22_13 = (22, 13)
        p_18_23 = (18, 23)
        p_10_31 = (10, 31)
        p_32_31 = (32, 31)
        p_40_31 = (40, 31)
        p_32_13 = (32, 13)
        p_32_44 = (32, 44)
        self.add_line('crest', p_8_4, p_14_4)
        self.add_arc('hook', p_14_4, p_22_13, radius_x=8, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('sweep', p_22_13, p_18_23, radius_x=13, radius_y=15, sweep=True, large_arc=False)
        self.add_line('diagonal', p_18_23, p_10_31)
        self.add_line('bar-left', p_10_31, p_32_31)
        self.add_line('bar-right', p_32_31, p_40_31)
        self.add_line('stem-top', p_32_13, p_32_31)
        self.add_line('stem-bottom', p_32_31, p_32_44)
        self.add_contour('bowl', 'crest', 'hook', 'sweep', 'diagonal', 'bar-left', 'bar-right', closed=False)
        self.add_contour('stem', 'stem-top', 'stem-bottom', closed=False)
        self.relate('connect', 'bowl', 'stem')
