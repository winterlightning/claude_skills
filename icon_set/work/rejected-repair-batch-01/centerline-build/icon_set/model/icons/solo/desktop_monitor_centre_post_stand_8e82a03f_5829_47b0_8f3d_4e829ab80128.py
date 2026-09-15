'Desktop monitor centre post stand.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e82a03f-5829-47b0-8f3d-4e829ab80128'
SOURCE_PATH = 'pictographic-primitives/computers/batch-01/desktop monitor back_8e82a03f-5829-47b0-8f3d-4e829ab80128.svg'
AUTHOR = 'gpt-6'

class DesktopMonitorCentrePostStand(Solo48):
    icon_id = 'desktop-monitor-centre-post-stand'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ('desktop-monitor', 'monitor-on-stand')
    keywords = ('monitor', 'display', 'screen', 'computer', 'stand')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_9_6 = (9, 6)
        p_39_6 = (39, 6)
        p_42_10 = (42, 10)
        p_42_29 = (42, 29)
        p_39_33 = (39, 33)
        p_24_33 = (24, 33)
        p_9_33 = (9, 33)
        p_6_29 = (6, 29)
        p_6_10 = (6, 10)
        p_24_42 = (24, 42)
        p_17_42 = (17, 42)
        p_31_42 = (31, 42)
        self.add_line('top', p_9_6, p_39_6)
        self.add_arc('upper-right', p_39_6, p_42_10, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('right', p_42_10, p_42_29)
        self.add_arc('lower-right', p_42_29, p_39_33, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('bottom-right', p_39_33, p_24_33)
        self.add_line('bottom-left', p_24_33, p_9_33)
        self.add_arc('lower-left', p_9_33, p_6_29, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('left', p_6_29, p_6_10)
        self.add_arc('upper-left', p_6_10, p_9_6, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('post', p_24_33, p_24_42)
        self.add_line('foot-1', p_17_42, p_24_42)
        self.add_line('foot-2', p_24_42, p_31_42)
        self.add_contour('screen', 'top', 'upper-right', 'right', 'lower-right', 'bottom-right', 'bottom-left', 'lower-left', 'left', 'upper-left', closed=True)
        self.add_contour('foot', 'foot-1', 'foot-2', closed=False)
        self.relate('connect', 'screen', 'post')
        self.relate('connect', 'post', 'foot')
