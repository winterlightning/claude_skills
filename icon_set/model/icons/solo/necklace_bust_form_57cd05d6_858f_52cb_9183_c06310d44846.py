'Necklace bust form.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '57cd05d6-858f-52cb-9183-c06310d44846'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-03/necklace_57cd05d6-858f-52cb-9183-c06310d44846.svg'
AUTHOR = 'gpt-6'

class NecklaceBustForm(Solo48):
    icon_id = 'necklace-bust-form'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('necklace', 'bust', 'form', 'display', 'mannequin', 'jewellery', 'jewelry', 'torso', 'stand')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_16_4 = (16, 4)
        p_32_4 = (32, 4)
        p_35_11 = (35, 11)
        p_40_13 = (40, 13)
        p_33_44 = (33, 44)
        p_15_44 = (15, 44)
        p_8_13 = (8, 13)
        p_13_11 = (13, 11)
        self.add_line('neck-top', p_16_4, p_32_4)
        self.add_arc('neck-right-top', p_32_4, p_35_11, radius_x=8, radius_y=9, sweep=False, large_arc=False)
        self.add_arc('neck-right-bottom', p_35_11, p_40_13, radius_x=8, radius_y=9, sweep=False, large_arc=False)
        self.add_line('base-1', p_40_13, p_33_44)
        self.add_line('base-2', p_33_44, p_15_44)
        self.add_line('base-3', p_15_44, p_8_13)
        self.add_arc('neck-left-bottom', p_8_13, p_13_11, radius_x=8, radius_y=9, sweep=False, large_arc=False)
        self.add_arc('neck-left-top', p_13_11, p_16_4, radius_x=8, radius_y=9, sweep=False, large_arc=False)
        self.add_arc('necklace', p_13_11, p_35_11, radius_x=11, radius_y=17, sweep=False, large_arc=False)
        self.add_contour('form', 'neck-top', 'neck-right-top', 'neck-right-bottom', 'base-1', 'base-2', 'base-3', 'neck-left-bottom', 'neck-left-top', closed=True)
        self.relate('connect', 'form', 'necklace')
