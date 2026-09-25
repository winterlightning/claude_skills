'Desktop monitor splayed stand.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The HRECT_L visible envelope is (2, 6, 46, 42).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '290363ae-c3b3-42fa-a00e-0c632d7eefaa'
SOURCE_PATH = 'pictographic-primitives/computers/batch-03/desktop computer_290363ae-c3b3-42fa-a00e-0c632d7eefaa.svg'
AUTHOR = 'gpt-6'

class DesktopMonitorSplayedStand(Solo48):
    icon_id = 'desktop-monitor-splayed-stand'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    aliases = ()
    keywords = ('desktop', 'monitor', 'splayed', 'stand')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_9_8 = (9, 8)
        p_39_8 = (39, 8)
        p_44_12 = (44, 12)
        p_44_25 = (44, 25)
        p_44_28 = (44, 28)
        p_39_32 = (39, 32)
        p_29_32 = (29, 32)
        p_19_32 = (19, 32)
        p_9_32 = (9, 32)
        p_4_28 = (4, 28)
        p_4_25 = (4, 25)
        p_4_12 = (4, 12)
        p_18_40 = (18, 40)
        p_30_40 = (30, 40)
        p_14_40 = (14, 40)
        p_34_40 = (34, 40)
        self.add_line('top', p_9_8, p_39_8)
        self.add_arc('ne', p_39_8, p_44_12, radius_x=5, radius_y=4, sweep=True, large_arc=False)
        self.add_line('right-upper', p_44_12, p_44_25)
        self.add_line('right-lower', p_44_25, p_44_28)
        self.add_arc('se', p_44_28, p_39_32, radius_x=5, radius_y=4, sweep=True, large_arc=False)
        self.add_line('bottom-right', p_39_32, p_29_32)
        self.add_line('bottom-mid', p_29_32, p_19_32)
        self.add_line('bottom-left', p_19_32, p_9_32)
        self.add_arc('sw', p_9_32, p_4_28, radius_x=5, radius_y=4, sweep=True, large_arc=False)
        self.add_line('left-lower', p_4_28, p_4_25)
        self.add_line('left-upper', p_4_25, p_4_12)
        self.add_arc('nw', p_4_12, p_9_8, radius_x=5, radius_y=4, sweep=True, large_arc=False)
        self.add_line('leg-left', p_19_32, p_18_40)
        self.add_line('leg-right', p_29_32, p_30_40)
        self.add_line('foot-left', p_14_40, p_18_40)
        self.add_line('foot-mid', p_18_40, p_30_40)
        self.add_line('foot-right', p_30_40, p_34_40)
        self.add_contour('screen', 'top', 'ne', 'right-upper', 'right-lower', 'se', 'bottom-right', 'bottom-mid', 'bottom-left', 'sw', 'left-lower', 'left-upper', 'nw', closed=True)
        self.add_contour('foot', 'foot-left', 'foot-mid', 'foot-right', closed=False)
        self.relate('connect', 'screen', 'leg-left')
        self.relate('connect', 'leg-left', 'foot')
        self.relate('connect', 'screen', 'leg-right')
        self.relate('connect', 'leg-right', 'foot')
