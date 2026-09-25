'Ring in presentation box.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f3bc943-720e-5b56-a91f-b2c1b67623f8'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-03/ring in case_8f3bc943-720e-5b56-a91f-b2c1b67623f8.svg'
AUTHOR = 'gpt-6'

class RingInPresentationBox(Solo48):
    icon_id = 'ring-in-presentation-box'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('ring', 'engagement ring', 'box', 'case', 'proposal', 'jewellery', 'jewelry', 'diamond', 'gift')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_13_4 = (13, 4)
        p_35_4 = (35, 4)
        p_40_9 = (40, 9)
        p_40_34 = (40, 34)
        p_40_39 = (40, 39)
        p_35_44 = (35, 44)
        p_13_44 = (13, 44)
        p_8_39 = (8, 39)
        p_8_34 = (8, 34)
        p_8_9 = (8, 9)
        p_16_34 = (16, 34)
        p_32_34 = (32, 34)
        p_24_25 = (24, 25)
        p_17_18 = (17, 18)
        p_21_12 = (21, 12)
        p_27_12 = (27, 12)
        p_31_18 = (31, 18)
        self.add_line('case-0', p_13_4, p_35_4)
        self.add_arc('case-1', p_35_4, p_40_9, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('case-2-attach-0', p_40_9, p_40_34)
        self.add_line('case-2-attach-1', p_40_34, p_40_39)
        self.add_arc('case-3', p_40_39, p_35_44, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('case-4', p_35_44, p_13_44)
        self.add_arc('case-5', p_13_44, p_8_39, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('case-6-attach-0', p_8_39, p_8_34)
        self.add_line('case-6-attach-1', p_8_34, p_8_9)
        self.add_arc('case-7', p_8_9, p_13_4, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('tray-attach-0', p_8_34, p_16_34)
        self.add_line('tray-attach-1', p_16_34, p_32_34)
        self.add_line('tray-attach-2', p_32_34, p_40_34)
        self.add_arc('ring-left', p_16_34, p_24_25, radius_x=8, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('ring-right', p_24_25, p_32_34, radius_x=8, radius_y=9, sweep=True, large_arc=False)
        self.add_line('gem-1', p_24_25, p_17_18)
        self.add_line('gem-2', p_17_18, p_21_12)
        self.add_line('gem-3', p_21_12, p_27_12)
        self.add_line('gem-4', p_27_12, p_31_18)
        self.add_line('gem-5', p_31_18, p_24_25)
        self.add_contour('case', 'case-0', 'case-1', 'case-2-attach-0', 'case-2-attach-1', 'case-3', 'case-4', 'case-5', 'case-6-attach-0', 'case-6-attach-1', 'case-7', closed=True)
        self.add_contour('tray', 'tray-attach-0', 'tray-attach-1', 'tray-attach-2', closed=False)
        self.add_contour('ring', 'ring-left', 'ring-right', closed=False)
        self.add_contour('gem', 'gem-1', 'gem-2', 'gem-3', 'gem-4', 'gem-5', closed=True)
        self.relate('connect', 'case', 'tray')
        self.relate('connect', 'gem', 'ring')
        self.relate('connect', 'ring', 'tray')
