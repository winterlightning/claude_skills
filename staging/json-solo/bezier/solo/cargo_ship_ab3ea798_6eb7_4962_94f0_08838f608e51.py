"""Cargo ship (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ab3ea798-6eb7-4962-94f0-08838f608e51'
SOURCE_PATH = 'icons-json/symbol/cargo ship_ab3ea798-6eb7-4962-94f0-08838f608e51.json'
AUTHOR = 'json_to_solo'

class CargoShipAb3ea798(Solo48):
    icon_id = 'cargo-ship-ab3ea798'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('cargo', 'ship', 'symbol')

    def build(self):
        self.add_line('e0', (15, 39), (11, 37))
        self.add_line('e1', (11, 37), (9, 37))
        self.add_line('e2', (39, 37), (42, 25))
        self.add_line('e3', (42, 25), (26, 23))
        self.add_line('e4', (26, 23), (23, 23))
        self.add_line('e5', (23, 23), (13, 24))
        self.add_line('e6', (13, 24), (6, 25))
        self.add_line('e7', (6, 25), (9, 37))
        self.add_line('e8', (39, 37), (44, 39))
        self.add_line('e9', (9, 37), (4, 39))
        self.add_line('e10', (19, 16), (11, 16))
        self.add_line('e11', (11, 16), (11, 24))
        self.add_line('e12', (29, 16), (37, 16))
        self.add_line('e13', (37, 16), (37, 24))
        self.add_line('e14', (29, 16), (29, 8))
        self.add_line('e15', (29, 8), (19, 8))
        self.add_line('e16', (19, 8), (19, 16))
        self.add_bezier('e17', (39, 37), ((37.945, 37.295), (37.382, 37.221), (36.418, 37.735)), ((34.927, 38.543), (33.5, 40), (31.636, 40)), ((31.635, 40), (31.634, 40), (31.633, 40)), ((31.571, 40), (31.508, 39.991), (31.445, 39.983)), ((28.609, 39.983), (27.064, 36.935), (24.291, 36.817)), ((21.791, 36.716), (20.355, 39.048), (18.064, 39.554)), ((16.991, 39.789), (16.027, 39.244), (15, 39)))
        self.add_contour('c0', 'e17', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7')
        self.add_contour('c2', 'e8')
        self.add_contour('c3', 'e9')
        self.add_contour('c4', 'e10', 'e11')
        self.add_contour('c5', 'e12')
        self.add_contour('c6', 'e13')
        self.add_contour('c7', 'e14', 'e15', 'e16')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c4', 'c1')
        self.relate('connect', 'c6', 'c1')
