'Mars astrological symbol.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '14451638-0bdf-5872-a108-890009443142'
SOURCE_PATH = 'pictographic-primitives/culture/batch-04/astrology mars_14451638-0bdf-5872-a108-890009443142.svg'
AUTHOR = 'gpt-6'

class MarsAstrologicalSymbol(Solo48):
    icon_id = 'mars-astrological-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('mars', 'astrology', 'planet', 'arrow', 'symbol', 'horoscope', 'glyph', 'masculine')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_16_22 = (16, 22)
        p_22_24 = (22, 24)
        p_26_32 = (26, 32)
        p_16_42 = (16, 42)
        p_6_32 = (6, 32)
        p_42_6 = (42, 6)
        p_30_6 = (30, 6)
        p_42_18 = (42, 18)
        self.add_arc('ring-top', p_16_22, p_22_24, radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('ring-tr', p_22_24, p_26_32, radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('ring-br', p_26_32, p_16_42, radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('ring-bl', p_16_42, p_6_32, radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('ring-tl', p_6_32, p_16_22, radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_line('shaft', p_22_24, p_42_6)
        self.add_line('arrow-0', p_30_6, p_42_6)
        self.add_line('arrow-1', p_42_6, p_42_18)
        self.add_contour('ring', 'ring-top', 'ring-tr', 'ring-br', 'ring-bl', 'ring-tl', closed=True)
        self.add_contour('arrow', 'arrow-0', 'arrow-1', closed=False)
        self.relate('connect', 'ring', 'shaft')
        self.relate('connect', 'shaft', 'arrow')
