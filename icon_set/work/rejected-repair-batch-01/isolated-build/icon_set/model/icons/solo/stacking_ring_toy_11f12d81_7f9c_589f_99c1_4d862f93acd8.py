'Stacking ring toy.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '11f12d81-7f9c-589f-99c1-4d862f93acd8'
SOURCE_PATH = 'pictographic-primitives/babies/toy_11f12d81-7f9c-589f-99c1-4d862f93acd8.svg'
AUTHOR = 'gpt-6'

class StackingRingToy(Solo48):
    icon_id = 'stacking-ring-toy'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/babies'
    aliases = ()
    keywords = ('stacking', 'ring', 'toy', 'infant', 'nursery')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_19_10 = (19, 10)
        p_29_10 = (29, 10)
        p_29_13 = (29, 13)
        p_19_13 = (19, 13)
        p_18_13 = (18, 13)
        p_30_13 = (30, 13)
        p_30_22 = (30, 22)
        p_18_22 = (18, 22)
        p_15_22 = (15, 22)
        p_33_22 = (33, 22)
        p_33_32 = (33, 32)
        p_15_32 = (15, 32)
        p_12_32 = (12, 32)
        p_36_32 = (36, 32)
        p_36_42 = (36, 42)
        p_12_42 = (12, 42)
        self.add_arc('peg-top', p_19_10, p_29_10, radius_x=5, radius_y=4, sweep=True, large_arc=False)
        self.add_line('peg-right', p_29_10, p_29_13)
        self.add_line('peg-left', p_19_13, p_19_10)
        self.add_line('top-top', p_18_13, p_30_13)
        self.add_arc('top-right', p_30_13, p_30_22, radius_x=6, radius_y=5, sweep=True, large_arc=False)
        self.add_line('top-bottom', p_30_22, p_18_22)
        self.add_arc('top-left', p_18_22, p_18_13, radius_x=6, radius_y=5, sweep=True, large_arc=False)
        self.add_line('middle-top', p_15_22, p_33_22)
        self.add_arc('middle-right', p_33_22, p_33_32, radius_x=6, radius_y=5, sweep=True, large_arc=False)
        self.add_line('middle-bottom', p_33_32, p_15_32)
        self.add_arc('middle-left', p_15_32, p_15_22, radius_x=6, radius_y=5, sweep=True, large_arc=False)
        self.add_line('bottom-top', p_12_32, p_36_32)
        self.add_arc('bottom-right', p_36_32, p_36_42, radius_x=6, radius_y=5, sweep=True, large_arc=False)
        self.add_line('bottom-bottom', p_36_42, p_12_42)
        self.add_arc('bottom-left', p_12_42, p_12_32, radius_x=6, radius_y=5, sweep=True, large_arc=False)
        self.add_contour('peg', 'peg-left', 'peg-top', 'peg-right', closed=False)
        self.add_contour('top', 'top-top', 'top-right', 'top-bottom', 'top-left', closed=True)
        self.add_contour('middle', 'middle-top', 'middle-right', 'middle-bottom', 'middle-left', closed=True)
        self.add_contour('bottom', 'bottom-top', 'bottom-right', 'bottom-bottom', 'bottom-left', closed=True)
        self.relate('connect', 'peg', 'top')
        self.relate('connect', 'top', 'middle')
        self.relate('connect', 'middle', 'bottom')
