'Desktop monitor curved pedestal.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The HRECT_L visible envelope is (2, 6, 46, 42).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ed39cf15-fc56-485a-8d68-f5b5d3b362db'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/monitor_ed39cf15-fc56-485a-8d68-f5b5d3b362db.svg'
AUTHOR = 'gpt-6'

class DesktopMonitorCurvedPedestal(Solo48):
    icon_id = 'desktop-monitor-curved-pedestal'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('monitor', 'display', 'screen', 'desktop', 'computer', 'stand', 'pedestal', 'device')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_8_8 = (8, 8)
        p_40_8 = (40, 8)
        p_44_11 = (44, 11)
        p_44_27 = (44, 27)
        p_40_30 = (40, 30)
        p_28_30 = (28, 30)
        p_20_30 = (20, 30)
        p_8_30 = (8, 30)
        p_4_27 = (4, 27)
        p_4_11 = (4, 11)
        p_13_40 = (13, 40)
        p_35_40 = (35, 40)
        self.add_line('screen-top', p_8_8, p_40_8)
        self.add_arc('screen-ne', p_40_8, p_44_11, radius_x=4, radius_y=3, sweep=True, large_arc=False)
        self.add_line('screen-right', p_44_11, p_44_27)
        self.add_arc('screen-se', p_44_27, p_40_30, radius_x=4, radius_y=3, sweep=True, large_arc=False)
        self.add_line('screen-bottom-0', p_40_30, p_28_30)
        self.add_line('screen-bottom-1', p_28_30, p_20_30)
        self.add_line('screen-bottom-2', p_20_30, p_8_30)
        self.add_arc('screen-sw', p_8_30, p_4_27, radius_x=4, radius_y=3, sweep=True, large_arc=False)
        self.add_line('screen-left', p_4_27, p_4_11)
        self.add_arc('screen-nw', p_4_11, p_8_8, radius_x=4, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('stand-left', p_20_30, p_13_40, radius_x=7, radius_y=10, sweep=True, large_arc=False)
        self.add_line('stand-base', p_13_40, p_35_40)
        self.add_arc('stand-right', p_35_40, p_28_30, radius_x=7, radius_y=10, sweep=True, large_arc=False)
        self.add_contour('screen', 'screen-top', 'screen-ne', 'screen-right', 'screen-se', 'screen-bottom-0', 'screen-bottom-1', 'screen-bottom-2', 'screen-sw', 'screen-left', 'screen-nw', closed=True)
        self.add_contour('stand', 'stand-left', 'stand-base', 'stand-right', closed=False)
        self.relate('connect', 'screen', 'stand')
