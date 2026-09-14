"""Pencil sketch (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7867b811-86a3-5125-8824-2c83f4113979'
SOURCE_PATH = 'icons-json/design/pencil sketch_7867b811-86a3-5125-8824-2c83f4113979.json'
AUTHOR = 'json_to_solo'

class PencilSketch7867b811(Solo48):
    icon_id = 'pencil-sketch-7867b811'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pencil', 'sketch', 'design')

    def build(self):
        self.add_line('sym-e0', (39, 17), (31, 9))
        self.add_line('sym-e1', (31, 9), (33, 7))
        self.add_arc('sym-e2', (33, 7), (35, 6), radius_x=3)
        self.add_arc('sym-e5', (35, 6), (39, 9), radius_x=10)
        self.add_arc('sym-e6', (39, 9), (42, 13), radius_x=10)
        self.add_arc('sym-e9', (42, 13), (41, 15), radius_x=3)
        self.add_line('sym-e10', (41, 15), (39, 17))
        self.add_line('sym-e11', (39, 17), (17, 39))
        self.add_line('sym-e12', (17, 39), (13, 35))
        self.add_line('sym-e13', (13, 35), (9, 31))
        self.add_line('sym-e14', (9, 31), (31, 9))
        self.add_line('sym-e15', (17, 39), (6, 42))
        self.add_line('sym-e16', (6, 42), (9, 31))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e5', 'sym-e6', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14')
        self.add_contour('sym-c1', 'sym-e15', 'sym-e16')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
