'Chinese dragon head.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b142eda-f9a9-5022-b106-7f024266d0b8'
SOURCE_PATH = 'pictographic-primitives/culture/batch-01/chinese dragon_6b142eda-f9a9-5022-b106-7f024266d0b8.svg'
AUTHOR = 'gpt-6'

class ChineseDragonHead(Solo48):
    icon_id = 'chinese-dragon-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    categories = ('culture', 'primitives')
    aliases = ()
    keywords = ('dragon', 'chinese', 'mythology', 'lunar new year', 'beast', 'mask', 'asian', 'legend')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_16_17 = (16, 17)
        p_11_11 = (11, 11)
        p_13_6 = (13, 6)
        p_32_17 = (32, 17)
        p_37_11 = (37, 11)
        p_35_6 = (35, 6)
        p_39_21 = (39, 21)
        p_37_27 = (37, 27)
        p_32_35 = (32, 35)
        p_24_42 = (24, 42)
        p_16_35 = (16, 35)
        p_11_27 = (11, 27)
        p_9_21 = (9, 21)
        p_6_9 = (6, 9)
        p_42_9 = (42, 9)
        p_20_25 = (20, 25)
        p_28_25 = (28, 25)
        p_6_31 = (6, 31)
        p_42_31 = (42, 31)
        self.add_arc('horn-left-lower', p_16_17, p_11_11, radius_x=5, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('horn-left-tip', p_11_11, p_13_6, radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('horn-right-lower', p_32_17, p_37_11, radius_x=5, radius_y=6, sweep=False, large_arc=False)
        self.add_arc('horn-right-tip', p_37_11, p_35_6, radius_x=8, radius_y=8, sweep=False, large_arc=False)
        self.add_arc('brow', p_16_17, p_32_17, radius_x=15, radius_y=3, sweep=True, large_arc=False)
        self.add_line('cheek-right-1', p_32_17, p_39_21)
        self.add_line('cheek-right-2', p_39_21, p_37_27)
        self.add_line('cheek-right-3', p_37_27, p_32_35)
        self.add_line('jaw-right', p_32_35, p_24_42)
        self.add_line('jaw-left', p_24_42, p_16_35)
        self.add_line('cheek-left-1', p_16_35, p_11_27)
        self.add_line('cheek-left-2', p_11_27, p_9_21)
        self.add_line('cheek-left-3', p_9_21, p_16_17)
        self.add_line('antler-left', p_11_11, p_6_9)
        self.add_line('antler-right', p_37_11, p_42_9)
        self.add_line('eye-left', p_20_25, p_20_25)
        self.add_line('eye-right', p_28_25, p_28_25)
        self.add_arc('whisker-left', p_16_35, p_6_31, radius_x=10, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('whisker-right', p_32_35, p_42_31, radius_x=10, radius_y=4, sweep=False, large_arc=False)
        self.add_contour('horn-left', 'horn-left-lower', 'horn-left-tip', closed=False)
        self.add_contour('horn-right', 'horn-right-lower', 'horn-right-tip', closed=False)
        self.add_contour('face', 'brow', 'cheek-right-1', 'cheek-right-2', 'cheek-right-3', 'jaw-right', 'jaw-left', 'cheek-left-1', 'cheek-left-2', 'cheek-left-3', closed=True)
        self.relate('connect', 'horn-left', 'antler-left')
        self.relate('connect', 'horn-right', 'antler-right')
        self.relate('connect', 'face', 'horn-left')
        self.relate('connect', 'face', 'horn-right')
        self.relate('connect', 'face', 'whisker-left')
        self.relate('connect', 'face', 'whisker-right')
