"""Keyboard button (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2f64ef8b-f8cd-5add-84ab-cb04db2d8ac7'
SOURCE_PATH = 'icons-json/interface-essential/keyboard button_2f64ef8b-f8cd-5add-84ab-cb04db2d8ac7.json'
AUTHOR = 'gpt-6'

class KeyboardButton(Solo48):
    icon_id = 'keyboard-button'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'button', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (6, 24), (6, 12))
        self.add_arc('sym-e2', (6, 12), (11, 6), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('sym-e3-1', (11, 6), (13, 6), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('sym-e3-2', (13, 6), (14, 6), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_line('sym-e4', (14, 6), (37, 6))
        self.add_arc('sym-e9', (37, 6), (42, 12), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('sym-e10', (42, 12), (42, 13), radius_x=23, radius_y=23, large_arc=False, sweep=False)
        self.add_line('sym-e11', (42, 13), (42, 36))
        self.add_arc('sym-e14', (42, 36), (37, 42), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('sym-e15-1', (37, 42), (14, 42))
        self.add_arc('sym-e20-1', (14, 42), (13, 42), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_line('sym-e20-2', (13, 42), (11, 42))
        self.add_arc('sym-e21', (11, 42), (6, 36), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('sym-e22', (6, 36), (6, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3-1', 'sym-e3-2', 'sym-e4', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e14', 'sym-e15-1', 'sym-e20-1', 'sym-e20-2', 'sym-e21', 'sym-e22', closed=True)
