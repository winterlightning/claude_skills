'Drop earrings with diamond beads.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '513ef66c-4b4f-5bab-8e0c-b825fb43e517'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-01/accessories earrings oriental_513ef66c-4b4f-5bab-8e0c-b825fb43e517.svg'
AUTHOR = 'gpt-6'

class DropEarringsWithDiamondBeads(Solo48):
    icon_id = 'drop-earrings-with-diamond-beads'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('earring', 'earrings', 'drop earring', 'jewellery', 'jewelry', 'diamond', 'bead', 'accessory', 'fashion')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_10_9 = (10, 9)
        p_20_9 = (20, 9)
        p_15_15 = (15, 15)
        p_15_26 = (15, 26)
        p_20_35 = (20, 35)
        p_15_44 = (15, 44)
        p_8_35 = (8, 35)
        p_28_9 = (28, 9)
        p_38_9 = (38, 9)
        p_33_15 = (33, 15)
        p_33_26 = (33, 26)
        p_40_35 = (40, 35)
        p_33_44 = (33, 44)
        p_28_35 = (28, 35)
        self.add_arc('left-hook', p_10_9, p_20_9, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('left-curl', p_20_9, p_15_15, radius_x=5, radius_y=6, sweep=True, large_arc=False)
        self.add_line('left-wire', p_15_15, p_15_26)
        self.add_line('left-diamond-1', p_15_26, p_20_35)
        self.add_line('left-diamond-2', p_20_35, p_15_44)
        self.add_line('left-diamond-3', p_15_44, p_8_35)
        self.add_line('left-diamond-4', p_8_35, p_15_26)
        self.add_arc('right-hook', p_28_9, p_38_9, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('right-curl', p_38_9, p_33_15, radius_x=5, radius_y=6, sweep=True, large_arc=False)
        self.add_line('right-wire', p_33_15, p_33_26)
        self.add_line('right-diamond-1', p_33_26, p_40_35)
        self.add_line('right-diamond-2', p_40_35, p_33_44)
        self.add_line('right-diamond-3', p_33_44, p_28_35)
        self.add_line('right-diamond-4', p_28_35, p_33_26)
        self.add_contour('left-hanger', 'left-hook', 'left-curl', 'left-wire', closed=False)
        self.add_contour('left-diamond', 'left-diamond-1', 'left-diamond-2', 'left-diamond-3', 'left-diamond-4', closed=True)
        self.add_contour('right-hanger', 'right-hook', 'right-curl', 'right-wire', closed=False)
        self.add_contour('right-diamond', 'right-diamond-1', 'right-diamond-2', 'right-diamond-3', 'right-diamond-4', closed=True)
        self.relate('connect', 'left-hanger', 'left-diamond')
        self.relate('connect', 'right-hanger', 'right-diamond')
