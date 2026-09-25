'Desktop monitor pedestal stand.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd60dfa85-47eb-534e-b0f2-ac618c2fc24b'
SOURCE_PATH = 'pictographic-primitives/computers/batch-02/desktop computer pc_d60dfa85-47eb-534e-b0f2-ac618c2fc24b.svg'
AUTHOR = 'gpt-6'

class DesktopMonitorPedestalStand(Solo48):
    icon_id = 'desktop-monitor-pedestal-stand'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    categories = ('computers', 'other', 'primitives-generate')
    aliases = ('desktop-display',)
    keywords = ('computer', 'screen', 'device', 'lucide-monitor')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_9_6 = (9, 6)
        p_39_6 = (39, 6)
        p_42_10 = (42, 10)
        p_42_25 = (42, 25)
        p_42_29 = (42, 29)
        p_39_33 = (39, 33)
        p_28_33 = (28, 33)
        p_20_33 = (20, 33)
        p_9_33 = (9, 33)
        p_6_29 = (6, 29)
        p_6_25 = (6, 25)
        p_6_10 = (6, 10)
        p_17_42 = (17, 42)
        p_31_42 = (31, 42)
        self.add_line('top', p_9_6, p_39_6)
        self.add_arc('top-right', p_39_6, p_42_10, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('right-1', p_42_10, p_42_25)
        self.add_line('right-2', p_42_25, p_42_29)
        self.add_arc('bottom-right', p_42_29, p_39_33, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('bottom-1', p_39_33, p_28_33)
        self.add_line('bottom-2', p_28_33, p_20_33)
        self.add_line('bottom-3', p_20_33, p_9_33)
        self.add_arc('bottom-left', p_9_33, p_6_29, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('left-1', p_6_29, p_6_25)
        self.add_line('left-2', p_6_25, p_6_10)
        self.add_arc('top-left', p_6_10, p_9_6, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('chin', p_6_25, p_42_25)
        self.add_line('pedestal-1', p_20_33, p_17_42)
        self.add_line('pedestal-2', p_17_42, p_31_42)
        self.add_line('pedestal-3', p_31_42, p_28_33)
        self.add_contour('screen', 'top', 'top-right', 'right-1', 'right-2', 'bottom-right', 'bottom-1', 'bottom-2', 'bottom-3', 'bottom-left', 'left-1', 'left-2', 'top-left', closed=True)
        self.add_contour('pedestal', 'pedestal-1', 'pedestal-2', 'pedestal-3', closed=False)
        self.relate('connect', 'screen', 'chin')
        self.relate('connect', 'screen', 'pedestal')
