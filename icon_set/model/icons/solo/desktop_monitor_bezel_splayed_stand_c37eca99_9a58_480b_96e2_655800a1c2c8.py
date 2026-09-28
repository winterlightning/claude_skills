'Desktop monitor bezel splayed stand.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c37eca99-9a58-480b-96e2-655800a1c2c8'
SOURCE_PATH = 'pictographic-primitives/computers/batch-03/desktop computer pc_c37eca99-9a58-480b-96e2-655800a1c2c8.svg'
AUTHOR = 'gpt-6'

class DesktopMonitorBezelSplayedStand(Solo48):
    icon_id = 'desktop-monitor-bezel-splayed-stand'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    categories = ('computers', 'primitives')
    aliases = ()
    keywords = ('desktop', 'monitor', 'bezel', 'splayed', 'stand')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_10_6 = (10, 6)
        p_38_6 = (38, 6)
        p_42_11 = (42, 11)
        p_42_25 = (42, 25)
        p_42_29 = (42, 29)
        p_38_33 = (38, 33)
        p_28_33 = (28, 33)
        p_20_33 = (20, 33)
        p_10_33 = (10, 33)
        p_6_29 = (6, 29)
        p_6_25 = (6, 25)
        p_6_11 = (6, 11)
        p_18_42 = (18, 42)
        p_30_42 = (30, 42)
        p_15_42 = (15, 42)
        p_33_42 = (33, 42)
        self.add_line('top', p_10_6, p_38_6)
        self.add_arc('ne', p_38_6, p_42_11, radius_x=4, radius_y=5, sweep=True, large_arc=False)
        self.add_line('right-upper', p_42_11, p_42_25)
        self.add_line('right-lower', p_42_25, p_42_29)
        self.add_arc('se', p_42_29, p_38_33, radius_x=4, radius_y=5, sweep=True, large_arc=False)
        self.add_line('bottom-right', p_38_33, p_28_33)
        self.add_line('bottom-mid', p_28_33, p_20_33)
        self.add_line('bottom-left', p_20_33, p_10_33)
        self.add_arc('sw', p_10_33, p_6_29, radius_x=4, radius_y=5, sweep=True, large_arc=False)
        self.add_line('left-lower', p_6_29, p_6_25)
        self.add_line('left-upper', p_6_25, p_6_11)
        self.add_arc('nw', p_6_11, p_10_6, radius_x=4, radius_y=5, sweep=True, large_arc=False)
        self.add_line('bezel', p_6_25, p_42_25)
        self.add_line('leg-left', p_20_33, p_18_42)
        self.add_line('leg-right', p_28_33, p_30_42)
        self.add_line('foot-left', p_15_42, p_18_42)
        self.add_line('foot-mid', p_18_42, p_30_42)
        self.add_line('foot-right', p_30_42, p_33_42)
        self.add_contour('screen', 'top', 'ne', 'right-upper', 'right-lower', 'se', 'bottom-right', 'bottom-mid', 'bottom-left', 'sw', 'left-lower', 'left-upper', 'nw', closed=True)
        self.add_contour('foot', 'foot-left', 'foot-mid', 'foot-right', closed=False)
        self.relate('connect', 'bezel', 'screen')
        self.relate('connect', 'screen', 'leg-left')
        self.relate('connect', 'leg-left', 'foot')
        self.relate('connect', 'screen', 'leg-right')
        self.relate('connect', 'leg-right', 'foot')
