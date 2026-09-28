'Descending lunar node symbol.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '42841092-ec74-56d4-aedd-b98302173838'
SOURCE_PATH = 'pictographic-primitives/culture/batch-02/astrology tail node_42841092-ec74-56d4-aedd-b98302173838.svg'
AUTHOR = 'gpt-6'

class DescendingLunarNodeSymbol(Solo48):
    icon_id = 'descending-lunar-node-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    categories = ('culture', 'primitives')
    aliases = ()
    keywords = ('lunar node', 'astrology', 'descending', 'south node', 'symbol', 'horoscope', 'glyph', 'moon')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_8_11 = (8, 11)
        p_20_11 = (20, 11)
        p_28_11 = (28, 11)
        p_40_11 = (40, 11)
        p_17_35 = (17, 35)
        p_31_35 = (31, 35)
        self.add_arc('left-ring-top', p_8_11, p_20_11, radius_x=6, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('left-ring-bottom', p_20_11, p_8_11, radius_x=6, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('right-ring-top', p_28_11, p_40_11, radius_x=6, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('right-ring-bottom', p_40_11, p_28_11, radius_x=6, radius_y=7, sweep=True, large_arc=False)
        self.add_line('left-arm', p_20_11, p_17_35)
        self.add_arc('bowl', p_17_35, p_31_35, radius_x=7, radius_y=9, sweep=False, large_arc=False)
        self.add_line('right-arm', p_31_35, p_28_11)
        self.add_contour('left-ring', 'left-ring-top', 'left-ring-bottom', closed=True)
        self.add_contour('right-ring', 'right-ring-top', 'right-ring-bottom', closed=True)
        self.add_contour('node', 'left-arm', 'bowl', 'right-arm', closed=False)
        self.relate('connect', 'node', 'left-ring')
        self.relate('connect', 'node', 'right-ring')
