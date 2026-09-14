'Neptune astrological symbol.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a181cba1-7a67-5780-bb8c-0de5147faaca'
SOURCE_PATH = 'pictographic-primitives/culture/batch-05/astrology neptune_a181cba1-7a67-5780-bb8c-0de5147faaca.svg'
AUTHOR = 'gpt-6'

class NeptuneAstrologicalSymbol(Solo48):
    icon_id = 'neptune-astrological-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('neptune', 'astrology', 'planet', 'trident', 'symbol', 'horoscope', 'glyph', 'poseidon')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_24_6 = (24, 6)
        p_24_27 = (24, 27)
        p_24_35 = (24, 35)
        p_24_42 = (24, 42)
        p_20_10 = (20, 10)
        p_28_10 = (28, 10)
        p_10_13 = (10, 13)
        p_10_17 = (10, 17)
        p_38_17 = (38, 17)
        p_38_13 = (38, 13)
        p_6_17 = (6, 17)
        p_14_17 = (14, 17)
        p_34_17 = (34, 17)
        p_42_17 = (42, 17)
        p_17_35 = (17, 35)
        p_31_35 = (31, 35)
        self.add_line('shaft-1', p_24_6, p_24_27)
        self.add_line('shaft-2', p_24_27, p_24_35)
        self.add_line('shaft-3', p_24_35, p_24_42)
        self.add_line('centre-tip-1', p_20_10, p_24_6)
        self.add_line('centre-tip-2', p_24_6, p_28_10)
        self.add_line('left-prong', p_10_13, p_10_17)
        self.add_arc('left-bowl', p_10_17, p_24_27, radius_x=14, radius_y=10, sweep=False, large_arc=False)
        self.add_arc('right-bowl', p_24_27, p_38_17, radius_x=14, radius_y=10, sweep=False, large_arc=False)
        self.add_line('right-prong', p_38_17, p_38_13)
        self.add_line('left-tip-1', p_6_17, p_10_13)
        self.add_line('left-tip-2', p_10_13, p_14_17)
        self.add_line('right-tip-1', p_34_17, p_38_13)
        self.add_line('right-tip-2', p_38_13, p_42_17)
        self.add_line('crossbar-1', p_17_35, p_24_35)
        self.add_line('crossbar-2', p_24_35, p_31_35)
        self.add_contour('shaft', 'shaft-1', 'shaft-2', 'shaft-3', closed=False)
        self.add_contour('centre-tip', 'centre-tip-1', 'centre-tip-2', closed=False)
        self.add_contour('fork', 'left-prong', 'left-bowl', 'right-bowl', 'right-prong', closed=False)
        self.add_contour('left-tip', 'left-tip-1', 'left-tip-2', closed=False)
        self.add_contour('right-tip', 'right-tip-1', 'right-tip-2', closed=False)
        self.add_contour('crossbar', 'crossbar-1', 'crossbar-2', closed=False)
        self.relate('connect', 'shaft', 'centre-tip')
        self.relate('connect', 'shaft', 'fork')
        self.relate('connect', 'shaft', 'crossbar')
        self.relate('connect', 'fork', 'left-tip')
        self.relate('connect', 'fork', 'right-tip')
