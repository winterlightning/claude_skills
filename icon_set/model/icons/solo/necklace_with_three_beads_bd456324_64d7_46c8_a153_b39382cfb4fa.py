'Necklace with three beads.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd456324-64d7-46c8-a153-b39382cfb4fa'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-01/diy jewelry_bd456324-64d7-46c8-a153-b39382cfb4fa.svg'
AUTHOR = 'gpt-6'

class NecklaceWithThreeBeads(Solo48):
    icon_id = 'necklace-with-three-beads'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    categories = ('primitives', 'accessories')
    aliases = ()
    keywords = ('necklace', 'bead', 'beaded', 'jewellery', 'jewelry', 'diy', 'craft', 'cord', 'accessory')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_13_6 = (13, 6)
        p_6_13 = (6, 13)
        p_11_27 = (11, 27)
        p_35_6 = (35, 6)
        p_42_13 = (42, 13)
        p_37_27 = (37, 27)
        p_24_28 = (24, 28)
        p_17_35 = (17, 35)
        p_31_35 = (31, 35)
        self.add_arc('left-curl', p_13_6, p_6_13, radius_x=7, radius_y=7, sweep=False, large_arc=False)
        self.add_arc('left-cord', p_6_13, p_11_27, radius_x=5, radius_y=14, sweep=False, large_arc=False)
        self.add_arc('right-curl', p_35_6, p_42_13, radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('right-cord', p_42_13, p_37_27, radius_x=5, radius_y=14, sweep=True, large_arc=False)
        self.add_line('left-bead', p_11_27, p_11_27)
        self.add_line('right-bead', p_37_27, p_37_27)
        self.add_line('thread-left', p_11_27, p_24_28)
        self.add_line('thread-right', p_37_27, p_24_28)
        self.add_arc('main-bead-top', p_17_35, p_31_35, radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('main-bead-bottom', p_31_35, p_17_35, radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_contour('left', 'left-curl', 'left-cord', closed=False)
        self.add_contour('right', 'right-curl', 'right-cord', closed=False)
        self.add_contour('main-bead', 'main-bead-top', 'main-bead-bottom', closed=True)
        self.relate('connect', 'left', 'left-bead')
        self.relate('connect', 'left', 'thread-left')
        self.relate('connect', 'left-bead', 'thread-left')
        self.relate('connect', 'right', 'right-bead')
        self.relate('connect', 'right', 'thread-right')
        self.relate('connect', 'right-bead', 'thread-right')
        self.relate('connect', 'thread-left', 'thread-right')
        self.relate('connect', 'thread-left', 'main-bead')
        self.relate('connect', 'thread-right', 'main-bead')
