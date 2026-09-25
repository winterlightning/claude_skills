'Written scroll.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0872fa36-cb40-4048-bfff-5fa6453c601b'
SOURCE_PATH = 'pictographic-primitives/culture/batch-07/greek script_0872fa36-cb40-4048-bfff-5fa6453c601b.svg'
AUTHOR = 'gpt-6'

class WrittenScroll(Solo48):
    icon_id = 'written-scroll'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    categories = ('culture', 'primitives')
    aliases = ()
    keywords = ('scroll', 'parchment', 'manuscript', 'script', 'ancient', 'document', 'writing', 'papyrus')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_6_11 = (6, 11)
        p_11_6 = (11, 6)
        p_16_11 = (16, 11)
        p_16_16 = (16, 16)
        p_16_37 = (16, 37)
        p_21_42 = (21, 42)
        p_26_37 = (26, 37)
        p_26_32 = (26, 32)
        p_37_32 = (37, 32)
        p_42_32 = (42, 32)
        p_42_37 = (42, 37)
        p_37_42 = (37, 42)
        p_6_16 = (6, 16)
        p_32_6 = (32, 6)
        p_37_11 = (37, 11)
        p_25_18 = (25, 18)
        p_28_18 = (28, 18)
        self.add_arc('top-roll-a', p_6_11, p_11_6, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('top-roll-b', p_11_6, p_16_11, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('left-wall-a', p_16_11, p_16_16)
        self.add_line('left-wall-b', p_16_16, p_16_37)
        self.add_arc('bottom-roll-a', p_16_37, p_21_42, radius_x=5, radius_y=5, sweep=False, large_arc=False)
        self.add_arc('bottom-roll-b', p_21_42, p_26_37, radius_x=5, radius_y=5, sweep=False, large_arc=False)
        self.add_line('roll-rise', p_26_37, p_26_32)
        self.add_line('roll-top-1', p_26_32, p_37_32)
        self.add_line('roll-top-2', p_37_32, p_42_32)
        self.add_line('roll-top-3', p_42_32, p_42_37)
        self.add_arc('bottom-corner', p_42_37, p_37_42, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('bottom-edge', p_37_42, p_21_42)
        self.add_line('roll-lip-1', p_6_11, p_6_16)
        self.add_line('roll-lip-2', p_6_16, p_16_16)
        self.add_line('top-edge', p_11_6, p_32_6)
        self.add_arc('top-corner', p_32_6, p_37_11, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('right-wall', p_37_11, p_37_32)
        self.add_line('writing-top', p_25_18, p_28_18)
        self.add_contour('scroll-lower', 'top-roll-a', 'top-roll-b', 'left-wall-a', 'left-wall-b', 'bottom-roll-a', 'bottom-roll-b', 'roll-rise', 'roll-top-1', 'roll-top-2', 'roll-top-3', 'bottom-corner', 'bottom-edge', closed=False)
        self.add_contour('roll-lip', 'roll-lip-1', 'roll-lip-2', closed=False)
        self.add_contour('scroll-upper', 'top-edge', 'top-corner', 'right-wall', closed=False)
        self.relate('connect', 'scroll-lower', 'roll-lip')
        self.relate('connect', 'scroll-lower', 'scroll-upper')
