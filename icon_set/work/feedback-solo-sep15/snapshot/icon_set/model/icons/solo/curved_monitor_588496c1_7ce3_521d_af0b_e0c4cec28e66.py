'Curved monitor.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The HRECT_L visible envelope is (2, 6, 46, 42).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '588496c1-7ce3-521d-af0b-e0c4cec28e66'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/screen curved_588496c1-7ce3-521d-af0b-e0c4cec28e66.svg'
AUTHOR = 'gpt-6'

class CurvedMonitor(Solo48):
    icon_id = 'curved-monitor'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('monitor', 'curved', 'screen', 'display', 'widescreen', 'gaming', 'computer', 'ultrawide')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_4_8 = (4, 8)
        p_15_10 = (15, 10)
        p_33_10 = (33, 10)
        p_44_8 = (44, 8)
        p_44_33 = (44, 33)
        p_33_32 = (33, 32)
        p_28_32 = (28, 32)
        p_20_32 = (20, 32)
        p_15_32 = (15, 32)
        p_4_33 = (4, 33)
        p_18_40 = (18, 40)
        p_30_40 = (30, 40)
        p_13_40 = (13, 40)
        p_35_40 = (35, 40)
        self.add_arc('top-left', p_4_8, p_15_10, radius_x=34, radius_y=31, sweep=False, large_arc=False)
        self.add_line('top-middle', p_15_10, p_33_10)
        self.add_arc('top-right', p_33_10, p_44_8, radius_x=34, radius_y=31, sweep=False, large_arc=False)
        self.add_line('side-right', p_44_8, p_44_33)
        self.add_arc('bottom-right', p_44_33, p_33_32, radius_x=34, radius_y=31, sweep=False, large_arc=False)
        self.add_line('bottom-middle-1', p_33_32, p_28_32)
        self.add_line('bottom-middle-2', p_28_32, p_20_32)
        self.add_line('bottom-middle-3', p_20_32, p_15_32)
        self.add_arc('bottom-left', p_15_32, p_4_33, radius_x=34, radius_y=31, sweep=False, large_arc=False)
        self.add_line('side-left', p_4_33, p_4_8)
        self.add_line('stand-1', p_20_32, p_18_40)
        self.add_line('stand-2', p_18_40, p_30_40)
        self.add_line('stand-3', p_30_40, p_28_32)
        self.add_line('base-left', p_13_40, p_18_40)
        self.add_line('base-right', p_30_40, p_35_40)
        self.add_contour('screen', 'top-left', 'top-middle', 'top-right', 'side-right', 'bottom-right', 'bottom-middle-1', 'bottom-middle-2', 'bottom-middle-3', 'bottom-left', 'side-left', closed=True)
        self.add_contour('stand', 'stand-1', 'stand-2', 'stand-3', closed=False)
        self.relate('connect', 'screen', 'stand')
        self.relate('connect', 'stand', 'base-left')
        self.relate('connect', 'stand', 'base-right')
