'Monitor with desk keyboard.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '42b12fe3-b736-5239-ab2e-91d8f0f66555'
SOURCE_PATH = 'pictographic-primitives/computers/batch-06/desktop monitor keyboard_42b12fe3-b736-5239-ab2e-91d8f0f66555.svg'
AUTHOR = 'gpt-6'

class MonitorWithDeskKeyboard(Solo48):
    icon_id = 'monitor-with-desk-keyboard'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('monitor', 'keyboard', 'desktop', 'computer', 'workstation', 'screen', 'typing', 'pc')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_9_6 = (9, 6)
        p_39_6 = (39, 6)
        p_42_9 = (42, 9)
        p_42_23 = (42, 23)
        p_39_26 = (39, 26)
        p_24_26 = (24, 26)
        p_9_26 = (9, 26)
        p_6_23 = (6, 23)
        p_6_9 = (6, 9)
        p_24_34 = (24, 34)
        p_11_34 = (11, 34)
        p_37_34 = (37, 34)
        p_40_42 = (40, 42)
        p_8_42 = (8, 42)
        self.add_line('screen-top0', p_9_6, p_39_6)
        self.add_arc('screen-ne', p_39_6, p_42_9, radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('screen-right', p_42_9, p_42_23)
        self.add_arc('screen-se', p_42_23, p_39_26, radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('screen-bottom0', p_39_26, p_24_26)
        self.add_line('screen-bottom1', p_24_26, p_9_26)
        self.add_arc('screen-sw', p_9_26, p_6_23, radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('screen-left', p_6_23, p_6_9)
        self.add_arc('screen-nw', p_6_9, p_9_6, radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('stand', p_24_26, p_24_34)
        self.add_line('keyboard-1', p_11_34, p_24_34)
        self.add_line('keyboard-2', p_24_34, p_37_34)
        self.add_line('keyboard-3', p_37_34, p_40_42)
        self.add_line('keyboard-4', p_40_42, p_8_42)
        self.add_line('keyboard-5', p_8_42, p_11_34)
        self.add_contour('screen', 'screen-top0', 'screen-ne', 'screen-right', 'screen-se', 'screen-bottom0', 'screen-bottom1', 'screen-sw', 'screen-left', 'screen-nw', closed=True)
        self.add_contour('keyboard', 'keyboard-1', 'keyboard-2', 'keyboard-3', 'keyboard-4', 'keyboard-5', closed=True)
        self.relate('connect', 'screen', 'stand')
        self.relate('connect', 'stand', 'keyboard')
