'Jewellery display bust.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81b7ac5c-a567-5591-8a55-414eb7643373'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-02/necklace stand_81b7ac5c-a567-5591-8a55-414eb7643373.svg'
AUTHOR = 'gpt-6'

class JewelleryDisplayBust(Solo48):
    icon_id = 'jewellery-display-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    categories = ('primitives', 'accessories')
    aliases = ()
    keywords = ('display', 'bust', 'stand', 'mannequin', 'jewellery', 'jewelry', 'shop', 'retail', 'necklace')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_18_4 = (18, 4)
        p_30_4 = (30, 4)
        p_30_8 = (30, 8)
        p_37_15 = (37, 15)
        p_40_19 = (40, 19)
        p_40_24 = (40, 24)
        p_37_29 = (37, 29)
        p_31_38 = (31, 38)
        p_28_44 = (28, 44)
        p_20_44 = (20, 44)
        p_17_38 = (17, 38)
        p_11_29 = (11, 29)
        p_8_24 = (8, 24)
        p_8_19 = (8, 19)
        p_11_15 = (11, 15)
        p_18_8 = (18, 8)
        p_12_44 = (12, 44)
        p_36_44 = (36, 44)
        self.add_line('neck-top', p_18_4, p_30_4)
        self.add_line('neck-r', p_30_4, p_30_8)
        self.add_arc('shoulder-r', p_30_8, p_37_15, radius_x=7, radius_y=7, sweep=False, large_arc=False)
        self.add_arc('corner-r', p_37_15, p_40_19, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('side-r', p_40_19, p_40_24)
        self.add_arc('turn-r', p_40_24, p_37_29, radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_line('taper-r', p_37_29, p_31_38)
        self.add_arc('foot-r', p_31_38, p_28_44, radius_x=8, radius_y=9, sweep=False, large_arc=False)
        self.add_line('base', p_28_44, p_20_44)
        self.add_arc('foot-l', p_20_44, p_17_38, radius_x=8, radius_y=9, sweep=False, large_arc=False)
        self.add_line('taper-l', p_17_38, p_11_29)
        self.add_arc('turn-l', p_11_29, p_8_24, radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_line('side-l', p_8_24, p_8_19)
        self.add_arc('corner-l', p_8_19, p_11_15, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('shoulder-l', p_11_15, p_18_8, radius_x=7, radius_y=7, sweep=False, large_arc=False)
        self.add_line('neck-l', p_18_8, p_18_4)
        self.add_line('base-left', p_12_44, p_20_44)
        self.add_line('base-right', p_28_44, p_36_44)
        self.add_contour('bust', 'neck-top', 'neck-r', 'shoulder-r', 'corner-r', 'side-r', 'turn-r', 'taper-r', 'foot-r', 'base', 'foot-l', 'taper-l', 'turn-l', 'side-l', 'corner-l', 'shoulder-l', 'neck-l', closed=True)
        self.relate('connect', 'base-left', 'bust')
        self.relate('connect', 'base-right', 'bust')
