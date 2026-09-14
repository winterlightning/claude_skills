"""Textbox (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2d966e0b-1e81-4eb6-869a-d5fc9fb91469'
SOURCE_PATH = 'icons-json/interface-essential/textbox_2d966e0b-1e81-4eb6-869a-d5fc9fb91469.json'
AUTHOR = 'json_to_solo'

class Textbox(Solo48):
    icon_id = 'textbox'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('textbox', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (24, 32), (24, 16))
        self.add_line('sym-e1', (24, 16), (16, 16))
        self.add_line('sym-e2', (24, 40), (9, 40))
        self.add_arc('sym-e3', (9, 40), (8, 40), radius_x=20, sweep=False)
        self.add_arc('sym-e4', (8, 40), (4, 36), radius_x=5)
        self.add_line('sym-e6', (4, 36), (4, 12))
        self.add_arc('sym-e7', (4, 12), (9, 8), radius_x=6)
        self.add_line('sym-e8', (9, 8), (24, 8))
        self.add_line('sym-e9', (24, 8), (39, 8))
        self.add_arc('sym-e10', (39, 8), (44, 12), radius_x=6)
        self.add_line('sym-e11', (44, 12), (44, 36))
        self.add_arc('sym-e13', (44, 36), (40, 40), radius_x=5)
        self.add_line('sym-e14', (40, 40), (39, 40))
        self.add_line('sym-e15', (39, 40), (24, 40))
        self.add_line('sym-e16', (32, 16), (24, 16))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
        self.add_contour('sym-c2', 'sym-e16')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
