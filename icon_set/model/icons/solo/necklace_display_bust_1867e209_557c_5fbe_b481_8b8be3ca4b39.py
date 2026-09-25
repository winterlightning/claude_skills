'Necklace display bust.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1867e209-557c-5fbe-b481-8b8be3ca4b39'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-01/necklace stand_1867e209-557c-5fbe-b481-8b8be3ca4b39.svg'
AUTHOR = 'gpt-6'

class NecklaceDisplayBust(Solo48):
    icon_id = 'necklace-display-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    categories = ('primitives', 'accessories')
    aliases = ()
    keywords = ('necklace', 'display', 'bust', 'stand', 'mannequin', 'jewellery', 'jewelry', 'shop', 'retail')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_19_4 = (19, 4)
        p_29_4 = (29, 4)
        p_29_9 = (29, 9)
        p_35_17 = (35, 17)
        p_37_17 = (37, 17)
        p_40_20 = (40, 20)
        p_40_29 = (40, 29)
        p_31_39 = (31, 39)
        p_31_44 = (31, 44)
        p_17_44 = (17, 44)
        p_17_39 = (17, 39)
        p_8_29 = (8, 29)
        p_8_20 = (8, 20)
        p_11_17 = (11, 17)
        p_13_17 = (13, 17)
        p_19_9 = (19, 9)
        self.add_line('neck-top', p_19_4, p_29_4)
        self.add_line('neck-r', p_29_4, p_29_9)
        self.add_arc('shoulder-r', p_29_9, p_35_17, radius_x=6, radius_y=7, sweep=False, large_arc=False)
        self.add_line('shoulder-r-out', p_35_17, p_37_17)
        self.add_arc('corner-r', p_37_17, p_40_20, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('side-r', p_40_20, p_40_29)
        self.add_line('taper-r', p_40_29, p_31_39)
        self.add_line('foot-r', p_31_39, p_31_44)
        self.add_line('base', p_31_44, p_17_44)
        self.add_line('foot-l', p_17_44, p_17_39)
        self.add_line('taper-l', p_17_39, p_8_29)
        self.add_line('side-l', p_8_29, p_8_20)
        self.add_arc('corner-l', p_8_20, p_11_17, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('shoulder-l-out', p_11_17, p_13_17)
        self.add_arc('shoulder-l', p_13_17, p_19_9, radius_x=6, radius_y=7, sweep=False, large_arc=False)
        self.add_line('neck-l', p_19_9, p_19_4)
        self.add_arc('necklace', p_13_17, p_35_17, radius_x=11, radius_y=15, sweep=False, large_arc=False)
        self.add_contour('bust', 'neck-top', 'neck-r', 'shoulder-r', 'shoulder-r-out', 'corner-r', 'side-r', 'taper-r', 'foot-r', 'base', 'foot-l', 'taper-l', 'side-l', 'corner-l', 'shoulder-l-out', 'shoulder-l', 'neck-l', closed=True)
        self.relate('connect', 'necklace', 'bust')
