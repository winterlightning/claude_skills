'Pair of teardrop earrings.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef2a4929-2eb7-4242-b6c1-b1b1a7b79511'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-06/earrings oriental_ef2a4929-2eb7-4242-b6c1-b1b1a7b79511.svg'
AUTHOR = 'gpt-6'

class PairOfTeardropEarrings(Solo48):
    icon_id = 'pair-of-teardrop-earrings'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('pair', 'of', 'teardrop', 'earrings')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_9_10 = (9, 10)
        p_17_10 = (17, 10)
        p_13_14 = (13, 14)
        p_13_22 = (13, 22)
        p_6_35 = (6, 35)
        p_20_35 = (20, 35)
        p_31_10 = (31, 10)
        p_39_10 = (39, 10)
        p_35_14 = (35, 14)
        p_35_22 = (35, 22)
        p_28_35 = (28, 35)
        p_42_35 = (42, 35)
        self.add_arc('left-stud-top', p_9_10, p_17_10, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('left-stud-bottom', p_17_10, p_9_10, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('left-post', p_13_14, p_13_22)
        self.add_line('left-sides-0', p_6_35, p_13_22)
        self.add_line('left-sides-1', p_13_22, p_20_35)
        self.add_arc('left-base', p_20_35, p_6_35, radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('right-stud-top', p_31_10, p_39_10, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('right-stud-bottom', p_39_10, p_31_10, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('right-post', p_35_14, p_35_22)
        self.add_line('right-sides-0', p_28_35, p_35_22)
        self.add_line('right-sides-1', p_35_22, p_42_35)
        self.add_arc('right-base', p_42_35, p_28_35, radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_contour('left-stud', 'left-stud-top', 'left-stud-bottom', closed=True)
        self.add_contour('left-drop', 'left-sides-0', 'left-sides-1', 'left-base', closed=True)
        self.add_contour('right-stud', 'right-stud-top', 'right-stud-bottom', closed=True)
        self.add_contour('right-drop', 'right-sides-0', 'right-sides-1', 'right-base', closed=True)
        self.relate('connect', 'left-stud', 'left-post')
        self.relate('connect', 'left-drop', 'left-post')
        self.relate('connect', 'right-stud', 'right-post')
        self.relate('connect', 'right-drop', 'right-post')
