"""Stepped gaming keyboard and looping cable; extremes (2,2)-(46,46). Lucide keyboard sparse keys; one key row retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a5a55431-2991-499a-9492-ddc2bc86cb9e'
SOURCE_PATH = 'pictographic-primitives/computers/batch-05/keyboard gaming_a5a55431-2991-499a-9492-ddc2bc86cb9e.svg'

class GamingKeyboardWithCable(Solo48):
    icon_id = 'gaming-keyboard-with-cable'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('keyboard', 'gaming', 'cable', 'typing', 'input', 'peripheral', 'computer', 'wired')

    def build(self) -> None:
        self.add_line('keyboard-1', (6, 25), (12, 25))
        self.add_line('keyboard-2', (12, 25), (16, 22))
        self.add_line('keyboard-3', (16, 22), (34, 22))
        self.add_line('keyboard-4', (34, 22), (38, 25))
        self.add_line('keyboard-5', (38, 25), (42, 25))
        self.add_arc('ne', (42, 25), (46, 29), radius_x=4, radius_y=4, sweep=True)
        self.add_line('right', (46, 29), (46, 42))
        self.add_arc('se', (46, 42), (42, 46), radius_x=4, radius_y=4, sweep=True)
        self.add_line('bottom', (42, 46), (6, 46))
        self.add_arc('sw', (6, 46), (2, 42), radius_x=4, radius_y=4, sweep=True)
        self.add_line('left', (2, 42), (2, 29))
        self.add_arc('nw', (2, 29), (6, 25), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('case', 'keyboard-1', 'keyboard-2', 'keyboard-3', 'keyboard-4', 'keyboard-5', 'ne', 'right', 'se', 'bottom', 'sw', 'left', 'nw', closed=True)
        self.add_line('cable-rise', (8, 25), (8, 20))
        self.add_arc('cable-turn', (8, 20), (14, 14), radius_x=6, radius_y=6, sweep=True)
        self.add_line('cable-run', (14, 14), (30, 14))
        self.add_arc('cable-loop', (30, 14), (30, 2), radius_x=6, radius_y=6, sweep=False)
        self.add_line('cable-tip', (30, 2), (18, 2))
        self.add_contour('cable', 'cable-rise', 'cable-turn', 'cable-run', 'cable-loop', 'cable-tip', closed=False)
        self.relate('connect', 'case', 'cable')
        self.add_line('key-12', (11, 32), (13, 32))
        self.add_line('key-24', (23, 32), (25, 32))
        self.add_line('key-36', (35, 32), (37, 32))
        self.add_line('spacebar', (14, 39), (34, 39))
