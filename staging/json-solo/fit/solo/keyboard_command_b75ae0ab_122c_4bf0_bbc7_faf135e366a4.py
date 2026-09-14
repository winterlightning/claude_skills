"""Keyboard command (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b75ae0ab-122c-4bf0-bbc7-faf135e366a4'
SOURCE_PATH = 'icons-json/interface-essential/keyboard command_b75ae0ab-122c-4bf0-bbc7-faf135e366a4.json'
AUTHOR = 'json_to_solo'

class KeyboardCommandB75ae0ab(Solo48):
    icon_id = 'keyboard-command-b75ae0ab'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'command', 'interface-essential')

    def build(self):
        self.add_line('e0', (36, 31), (17, 31))
        self.add_line('e1', (17, 36), (17, 12))
        self.add_line('e2', (12, 17), (31, 17))
        self.add_line('e3', (31, 12), (31, 37))
        self.add_arc('e4-1', (17, 31), (6, 36), radius_x=8, sweep=False)
        self.add_line('e4-2', (6, 36), (7, 40))
        self.add_line('e4-3', (7, 40), (11, 42))
        self.add_arc('e4-4', (11, 42), (17, 36), radius_x=6, sweep=False)
        self.add_arc('e5-1', (17, 12), (12, 6), radius_x=6, sweep=False)
        self.add_arc('e5-2', (12, 6), (6, 12), radius_x=6, sweep=False)
        self.add_arc('e5-3', (6, 12), (12, 17), radius_x=6, sweep=False)
        self.add_arc('e6-1', (31, 17), (42, 12), radius_x=8, sweep=False)
        self.add_arc('e6-2', (42, 12), (36, 6), radius_x=6, sweep=False)
        self.add_arc('e6-3', (36, 6), (31, 12), radius_x=6, sweep=False)
        self.add_arc('e7-1', (31, 37), (36, 42), radius_x=5, sweep=False)
        self.add_arc('e7-2', (36, 42), (42, 36), radius_x=6, sweep=False)
        self.add_arc('e7-3', (42, 36), (36, 31), radius_x=6, sweep=False)
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e1', 'e5-1', 'e5-2', 'e5-3', 'e2', 'e6-1', 'e6-2', 'e6-3', 'e3', 'e7-1', 'e7-2', 'e7-3', closed=True)
