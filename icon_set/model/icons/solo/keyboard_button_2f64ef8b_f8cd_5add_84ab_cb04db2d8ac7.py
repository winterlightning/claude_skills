"""Keyboard button (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f64ef8b-f8cd-5add-84ab-cb04db2d8ac7'
SOURCE_PATH = 'icons-json/interface-essential/keyboard button_2f64ef8b-f8cd-5add-84ab-cb04db2d8ac7.json'
AUTHOR = 'json_to_solo'

class KeyboardButton(Solo48):
    icon_id = 'keyboard-button'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'button', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (6, 24), (6, 13))
        self.add_line('sym-e1', (6, 13), (6, 12))
        self.add_arc('sym-e2', (6, 12), (11, 6), radius_x=7)
        self.add_arc('sym-e3-1', (11, 6), (13, 6), radius_x=10, sweep=False)
        self.add_arc('sym-e3-2', (13, 6), (14, 6), radius_x=11, sweep=False)
        self.add_line('sym-e4', (14, 6), (15, 6))
        self.add_line('sym-e5', (15, 6), (24, 6))
        self.add_line('sym-e6', (24, 6), (33, 6))
        self.add_line('sym-e7', (33, 6), (34, 6))
        self.add_line('sym-e8-1', (34, 6), (35, 6))
        self.add_line('sym-e8-2', (35, 6), (37, 6))
        self.add_arc('sym-e9', (37, 6), (42, 12), radius_x=7)
        self.add_arc('sym-e10', (42, 12), (42, 13), radius_x=23, sweep=False)
        self.add_line('sym-e11', (42, 13), (42, 24))
        self.add_line('sym-e12', (42, 24), (42, 35))
        self.add_line('sym-e13', (42, 35), (42, 36))
        self.add_arc('sym-e14', (42, 36), (37, 42), radius_x=7)
        self.add_line('sym-e15-1', (37, 42), (35, 42))
        self.add_line('sym-e15-2', (35, 42), (34, 42))
        self.add_line('sym-e16', (34, 42), (33, 42))
        self.add_line('sym-e17', (33, 42), (24, 42))
        self.add_line('sym-e18', (24, 42), (15, 42))
        self.add_line('sym-e19', (15, 42), (14, 42))
        self.add_arc('sym-e20-1', (14, 42), (13, 42), radius_x=11, sweep=False)
        self.add_line('sym-e20-2', (13, 42), (11, 42))
        self.add_arc('sym-e21', (11, 42), (6, 36), radius_x=7)
        self.add_line('sym-e22', (6, 36), (6, 35))
        self.add_line('sym-e23', (6, 35), (6, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3-1', 'sym-e3-2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8-1', 'sym-e8-2', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15-1', 'sym-e15-2', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20-1', 'sym-e20-2', 'sym-e21', 'sym-e22', 'sym-e23', closed=True)
