"""Skull (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7b01deac-dd2c-4265-92f5-d17735f0c07e'
SOURCE_PATH = 'icons-json/interface-essential/skull_7b01deac-dd2c-4265-92f5-d17735f0c07e.json'
AUTHOR = 'json_to_solo'

class Skull7b01deac(Solo48):
    icon_id = 'skull-7b01deac'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('skull', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 44), (24, 39))
        self.add_arc('e1-1', (14, 44), (14, 40), radius_x=63)
        self.add_arc('e1-2', (14, 40), (13, 36), radius_x=6, sweep=False)
        self.add_arc('e1-3', (13, 36), (9, 29), radius_x=19)
        self.add_line('e1-4', (9, 29), (8, 23))
        self.add_line('e1-5', (8, 23), (9, 15))
        self.add_line('e1-6', (9, 15), (13, 9))
        self.add_arc('e1-7', (13, 9), (24, 4), radius_x=15)
        self.add_arc('e1-8', (24, 4), (39, 16), radius_x=16)
        self.add_arc('e1-9', (39, 16), (40, 22), radius_x=19)
        self.add_line('e1-10', (40, 22), (39, 29))
        self.add_line('e1-11', (39, 29), (34, 39))
        self.add_line('e1-12', (34, 39), (34, 44))
        self.add_dot('e2', (16, 21))
        self.add_dot('e3', (32, 21))
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e1-9', 'e1-10', 'e1-11', 'e1-12')
        self.add_contour('c1', 'e0')
