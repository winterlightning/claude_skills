'Open cuff bangle.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The HRECT_L visible envelope is (2, 6, 46, 42).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eae03353-ee32-5ad5-8cc4-11d30c280629'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-05/bracelet_eae03353-ee32-5ad5-8cc4-11d30c280629.svg'
AUTHOR = 'gpt-6'

class OpenCuffBangle(Solo48):
    icon_id = 'open-cuff-bangle'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('bracelet', 'bangle', 'cuff', 'jewellery', 'jewelry', 'wrist', 'accessory', 'band')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_15_8 = (15, 8)
        p_4_24 = (4, 24)
        p_44_24 = (44, 24)
        p_33_8 = (33, 8)
        p_33_18 = (33, 18)
        p_35_24 = (35, 24)
        p_13_24 = (13, 24)
        p_15_18 = (15, 18)
        self.add_arc('outer-left', p_15_8, p_4_24, radius_x=11, radius_y=16, sweep=False, large_arc=False)
        self.add_arc('outer-bottom', p_4_24, p_44_24, radius_x=20, radius_y=16, sweep=False, large_arc=False)
        self.add_arc('outer-right', p_44_24, p_33_8, radius_x=11, radius_y=16, sweep=False, large_arc=False)
        self.add_arc('tip-right', p_33_8, p_33_18, radius_x=4, radius_y=5, sweep=False, large_arc=False)
        self.add_arc('inner-right', p_33_18, p_35_24, radius_x=2, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('inner-bottom', p_35_24, p_13_24, radius_x=11, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('inner-left', p_13_24, p_15_18, radius_x=2, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('tip-left', p_15_18, p_15_8, radius_x=4, radius_y=5, sweep=False, large_arc=False)
        self.add_contour('band', 'outer-left', 'outer-bottom', 'outer-right', 'tip-right', 'inner-right', 'inner-bottom', 'inner-left', 'tip-left', closed=True)
