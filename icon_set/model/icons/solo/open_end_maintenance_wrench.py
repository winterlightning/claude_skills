'Open end maintenance wrench.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/model/icons/solo/open_end_maintenance_wrench.py'
AUTHOR = 'gpt-6'

class OpenEndMaintenanceWrench(Solo48):
    icon_id = 'open-end-maintenance-wrench'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tools'
    categories = ('tools',)
    aliases = ('open-end-wrench', 'wrench', 'spanner')
    keywords = ('wrench', 'spanner', 'tool', 'maintenance', 'repair', 'settings', 'fix')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_8_4 = (8, 4)
        p_8_16 = (8, 16)
        p_24_32 = (24, 32)
        p_40_16 = (40, 16)
        p_40_4 = (40, 4)
        p_31_4 = (31, 4)
        p_31_16 = (31, 16)
        p_17_16 = (17, 16)
        p_17_4 = (17, 4)
        p_24_44 = (24, 44)
        self.add_line('outer-left', p_8_4, p_8_16)
        self.add_arc('outer-bottom-left', p_8_16, p_24_32, radius_x=16, radius_y=16, sweep=False, large_arc=False)
        self.add_arc('outer-bottom-right', p_24_32, p_40_16, radius_x=16, radius_y=16, sweep=False, large_arc=False)
        self.add_line('outer-right', p_40_16, p_40_4)
        self.add_line('right-tip', p_40_4, p_31_4)
        self.add_line('inner-right', p_31_4, p_31_16)
        self.add_arc('jaw-recess', p_31_16, p_17_16, radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_line('inner-left', p_17_16, p_17_4)
        self.add_line('left-tip', p_17_4, p_8_4)
        self.add_line('handle', p_24_32, p_24_44)
        self.add_contour('jaw', 'outer-left', 'outer-bottom-left', 'outer-bottom-right', 'outer-right', 'right-tip', 'inner-right', 'jaw-recess', 'inner-left', 'left-tip', closed=True)
        self.relate('connect', 'jaw', 'handle')
