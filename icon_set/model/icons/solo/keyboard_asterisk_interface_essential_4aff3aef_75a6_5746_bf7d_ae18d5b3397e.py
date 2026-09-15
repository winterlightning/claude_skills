"""Keyboard asterisk (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4aff3aef-75a6-5746-bf7d-ae18d5b3397e'
SOURCE_PATH = 'icons-json/interface-essential/keyboard asterisk_4aff3aef-75a6-5746-bf7d-ae18d5b3397e.json'
AUTHOR = 'gpt-6'

class KeyboardAsteriskInterfaceEssential(Solo48):
    icon_id = 'keyboard-asterisk-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'asterisk', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (20, 28), (20, 40))
        self.add_arc('sym-e1', (20, 40), (22, 42), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('sym-e3-1', (22, 42), (23, 42), radius_x=27, radius_y=27, large_arc=False, sweep=True)
        self.add_arc('sym-e3-2', (23, 42), (25, 42), radius_x=27, radius_y=27, large_arc=False, sweep=True)
        self.add_line('sym-e5', (25, 42), (26, 42))
        self.add_arc('sym-e6', (26, 42), (28, 40), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('sym-e7', (28, 40), (28, 28))
        self.add_line('sym-e8', (28, 28), (39, 28))
        self.add_arc('sym-e9', (39, 28), (42, 26), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_arc('sym-e10-1', (42, 26), (42, 25), radius_x=28, radius_y=28, large_arc=False, sweep=True)
        self.add_line('sym-e10-2', (42, 25), (42, 23))
        self.add_arc('sym-e13', (42, 23), (39, 20), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e14', (39, 20), (28, 20))
        self.add_line('sym-e15', (28, 20), (28, 9))
        self.add_arc('sym-e16', (28, 9), (25, 6), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e18', (25, 6), (24, 6))
        self.add_arc('sym-e19', (24, 6), (22, 6), radius_x=47, radius_y=47, large_arc=False, sweep=True)
        self.add_arc('sym-e20', (22, 6), (20, 9), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e21', (20, 9), (20, 20))
        self.add_line('sym-e22', (20, 20), (8, 20))
        self.add_arc('sym-e23', (8, 20), (6, 22), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('sym-e24', (6, 22), (6, 26))
        self.add_arc('sym-e28', (6, 26), (8, 28), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('sym-e29', (8, 28), (20, 28))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e3-1', 'sym-e3-2', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10-1', 'sym-e10-2', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e28', 'sym-e29', closed=True)
