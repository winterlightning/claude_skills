'Gaming keyboard with cable.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a5a55431-2991-499a-9492-ddc2bc86cb9e'
SOURCE_PATH = 'pictographic-primitives/computers/batch-05/keyboard gaming_a5a55431-2991-499a-9492-ddc2bc86cb9e.svg'
AUTHOR = 'gpt-6'

class GamingKeyboardWithCable(Solo48):
    icon_id = 'gaming-keyboard-with-cable'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    aliases = ()
    keywords = ('keyboard', 'gaming', 'cable', 'typing', 'input', 'peripheral', 'computer', 'wired')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_9_25 = (9, 25)
        p_14_25 = (14, 25)
        p_17_22 = (17, 22)
        p_32_22 = (32, 22)
        p_35_25 = (35, 25)
        p_39_25 = (39, 25)
        p_42_28 = (42, 28)
        p_42_39 = (42, 39)
        p_39_42 = (39, 42)
        p_9_42 = (9, 42)
        p_6_39 = (6, 39)
        p_6_28 = (6, 28)
        p_11_25 = (11, 25)
        p_11_20 = (11, 20)
        p_16_14 = (16, 14)
        p_29_14 = (29, 14)
        p_29_6 = (29, 6)
        p_19_6 = (19, 6)
        p_16_33 = (16, 33)
        p_32_33 = (32, 33)
        self.add_line('keyboard-1', p_9_25, p_14_25)
        self.add_line('keyboard-2', p_14_25, p_17_22)
        self.add_line('keyboard-3', p_17_22, p_32_22)
        self.add_line('keyboard-4', p_32_22, p_35_25)
        self.add_line('keyboard-5', p_35_25, p_39_25)
        self.add_arc('ne', p_39_25, p_42_28, radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('right', p_42_28, p_42_39)
        self.add_arc('se', p_42_39, p_39_42, radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('bottom', p_39_42, p_9_42)
        self.add_arc('sw', p_9_42, p_6_39, radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('left', p_6_39, p_6_28)
        self.add_arc('nw', p_6_28, p_9_25, radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('cable-rise', p_11_25, p_11_20)
        self.add_arc('cable-turn', p_11_20, p_16_14, radius_x=5, radius_y=6, sweep=True, large_arc=False)
        self.add_line('cable-run', p_16_14, p_29_14)
        self.add_arc('cable-loop', p_29_14, p_29_6, radius_x=5, radius_y=4, sweep=False, large_arc=False)
        self.add_line('cable-tip', p_29_6, p_19_6)
        self.add_line('keys', p_16_33, p_32_33)
        self.add_contour('case', 'keyboard-1', 'keyboard-2', 'keyboard-3', 'keyboard-4', 'keyboard-5', 'ne', 'right', 'se', 'bottom', 'sw', 'left', 'nw', closed=True)
        self.add_contour('cable', 'cable-rise', 'cable-turn', 'cable-run', 'cable-loop', 'cable-tip', closed=False)
        self.relate('connect', 'case', 'cable')
