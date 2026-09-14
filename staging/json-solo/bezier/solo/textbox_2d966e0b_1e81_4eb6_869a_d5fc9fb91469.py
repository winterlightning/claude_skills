"""Textbox (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2d966e0b-1e81-4eb6-869a-d5fc9fb91469'
SOURCE_PATH = 'icons-json/interface-essential/textbox_2d966e0b-1e81-4eb6-869a-d5fc9fb91469.json'
AUTHOR = 'json_to_solo'

class TextboxInterfaceEssential(Solo48):
    icon_id = 'textbox-interface-essential'
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
        self.add_bezier('sym-e3', (9, 40), ((8.955, 40), (8.045, 40), (8, 40)))
        self.add_bezier('sym-e4', (8, 40), ((6.173, 40), (4, 37.693), (4, 36)))
        self.add_bezier('sym-e5', (4, 36), ((4, 35.958), (4, 36.042), (4, 36)))
        self.add_line('sym-e6', (4, 36), (4, 12))
        self.add_bezier('sym-e7', (4, 12), ((4, 10.299), (7.173, 8), (9, 8)))
        self.add_line('sym-e8', (9, 8), (24, 8))
        self.add_line('sym-e9', (24, 8), (39, 8))
        self.add_bezier('sym-e10', (39, 8), ((40.827, 8), (44, 10.299), (44, 12)))
        self.add_line('sym-e11', (44, 12), (44, 36))
        self.add_bezier('sym-e12', (44, 36), ((44, 36.042), (44, 35.958), (44, 36)))
        self.add_bezier('sym-e13', (44, 36), ((44, 37.693), (41.827, 40), (40, 40)))
        self.add_bezier('sym-e14', (40, 40), ((39.955, 40), (39.045, 40), (39, 40)))
        self.add_line('sym-e15', (39, 40), (24, 40))
        self.add_line('sym-e16', (32, 16), (24, 16))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
        self.add_contour('sym-c2', 'sym-e16')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
