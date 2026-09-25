'Two stick figures.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.\nHuman construction: icon_set/references/human_ref/full_body_ref.png and\nicon_set/references/human_ref/user.svg. Circular head radius 4,\nwith exactly 8 units of centerline head-to-body separation (4 visible units).'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6c0a315d-d919-5e6b-8ff3-48d670cea3b4'
SOURCE_PATH = 'pictographic-primitives/culture/batch-07/primitive symbols group_6c0a315d-d919-5e6b-8ff3-48d670cea3b4.svg'
AUTHOR = 'gpt-6'

class TwoStickFigures(Solo48):
    icon_id = 'two-stick-figures'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('stick figure', 'people', 'primitive', 'cave art', 'pair', 'symbols', 'human', 'ancient')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_10_10 = (10, 10)
        p_18_10 = (18, 10)
        p_12_22 = (12, 22)
        p_16_22 = (16, 22)
        p_14_22 = (14, 22)
        p_14_32 = (14, 32)
        p_6_42 = (6, 42)
        p_20_42 = (20, 42)
        p_6_28 = (6, 28)
        p_24_30 = (24, 30)
        p_30_10 = (30, 10)
        p_38_10 = (38, 10)
        p_32_22 = (32, 22)
        p_36_22 = (36, 22)
        p_34_22 = (34, 22)
        p_34_32 = (34, 32)
        p_28_42 = (28, 42)
        p_42_42 = (42, 42)
        p_42_28 = (42, 28)
        self.add_arc('left-head-top', p_10_10, p_18_10, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('left-head-bottom', p_18_10, p_10_10, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('left-shoulders', p_12_22, p_16_22)
        self.add_line('left-body', p_14_22, p_14_32)
        self.add_line('left-legs-0', p_6_42, p_14_32)
        self.add_line('left-legs-1', p_14_32, p_20_42)
        self.add_line('left-outer-arm', p_12_22, p_6_28)
        self.add_line('left-inner-arm', p_16_22, p_24_30)
        self.add_arc('right-head-top', p_30_10, p_38_10, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('right-head-bottom', p_38_10, p_30_10, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('right-shoulders', p_32_22, p_36_22)
        self.add_line('right-body', p_34_22, p_34_32)
        self.add_line('right-legs-0', p_28_42, p_34_32)
        self.add_line('right-legs-1', p_34_32, p_42_42)
        self.add_line('right-outer-arm', p_36_22, p_42_28)
        self.add_line('right-inner-arm', p_32_22, p_24_30)
        self.add_contour('left-head', 'left-head-top', 'left-head-bottom', closed=True)
        self.add_contour('left-legs', 'left-legs-0', 'left-legs-1', closed=False)
        self.add_contour('right-head', 'right-head-top', 'right-head-bottom', closed=True)
        self.add_contour('right-legs', 'right-legs-0', 'right-legs-1', closed=False)
        self.relate('connect', 'left-shoulders', 'left-body')
        self.relate('connect', 'left-body', 'left-legs')
        self.relate('connect', 'left-shoulders', 'left-outer-arm')
        self.relate('connect', 'left-shoulders', 'left-inner-arm')
        self.relate('connect', 'right-shoulders', 'right-body')
        self.relate('connect', 'right-body', 'right-legs')
        self.relate('connect', 'right-shoulders', 'right-outer-arm')
        self.relate('connect', 'right-shoulders', 'right-inner-arm')
        self.relate('connect', 'left-inner-arm', 'right-inner-arm')
