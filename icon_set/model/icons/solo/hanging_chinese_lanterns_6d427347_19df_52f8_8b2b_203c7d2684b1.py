'Hanging chinese lanterns.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6d427347-19df-52f8-8b2b-203c7d2684b1'
SOURCE_PATH = 'pictographic-primitives/culture/batch-03/chinese lantern_6d427347-19df-52f8-8b2b-203c7d2684b1.svg'
AUTHOR = 'gpt-6'

class HangingChineseLanterns(Solo48):
    icon_id = 'hanging-chinese-lanterns'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    categories = ('culture', 'primitives')
    aliases = ()
    keywords = ('lantern', 'chinese', 'festival', 'lunar new year', 'hanging', 'bunting', 'celebration', 'asian')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_6_6 = (6, 6)
        p_13_8 = (13, 8)
        p_35_8 = (35, 8)
        p_42_6 = (42, 6)
        p_13_17 = (13, 17)
        p_19_26 = (19, 26)
        p_13_35 = (13, 35)
        p_6_26 = (6, 26)
        p_9_17 = (9, 17)
        p_16_17 = (16, 17)
        p_9_35 = (9, 35)
        p_16_35 = (16, 35)
        p_13_42 = (13, 42)
        p_35_16 = (35, 16)
        p_42_22 = (42, 22)
        p_35_31 = (35, 31)
        p_29_22 = (29, 22)
        p_32_16 = (32, 16)
        p_39_16 = (39, 16)
        p_32_31 = (32, 31)
        p_39_31 = (39, 31)
        p_35_37 = (35, 37)
        self.add_line('cord-1', p_6_6, p_13_8)
        self.add_line('cord-2', p_13_8, p_35_8)
        self.add_line('cord-3', p_35_8, p_42_6)
        self.add_line('left-suspension', p_13_8, p_13_17)
        self.add_arc('left-ne', p_13_17, p_19_26, radius_x=6, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('left-se', p_19_26, p_13_35, radius_x=6, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('left-sw', p_13_35, p_6_26, radius_x=7, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('left-nw', p_6_26, p_13_17, radius_x=7, radius_y=9, sweep=True, large_arc=False)
        self.add_line('left-cap', p_9_17, p_16_17)
        self.add_line('left-base', p_9_35, p_16_35)
        self.add_line('left-tassel', p_13_35, p_13_42)
        self.add_line('right-suspension', p_35_8, p_35_16)
        self.add_arc('right-ne', p_35_16, p_42_22, radius_x=7, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('right-se', p_42_22, p_35_31, radius_x=7, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('right-sw', p_35_31, p_29_22, radius_x=6, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('right-nw', p_29_22, p_35_16, radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('right-cap', p_32_16, p_39_16)
        self.add_line('right-base', p_32_31, p_39_31)
        self.add_line('right-tassel', p_35_31, p_35_37)
        self.add_contour('cord', 'cord-1', 'cord-2', 'cord-3', closed=False)
        self.add_contour('left', 'left-ne', 'left-se', 'left-sw', 'left-nw', closed=True)
        self.add_contour('right', 'right-ne', 'right-se', 'right-sw', 'right-nw', closed=True)
        self.relate('connect', 'left', 'left-suspension', 'left-cap')
        self.relate('connect', 'left', 'left-tassel', 'left-base')
        self.relate('connect', 'cord', 'left-suspension')
        self.relate('connect', 'right', 'right-suspension', 'right-cap')
        self.relate('connect', 'right', 'right-tassel', 'right-base')
        self.relate('connect', 'cord', 'right-suspension')
