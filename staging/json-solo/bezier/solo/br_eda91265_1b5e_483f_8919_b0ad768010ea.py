"""Br (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eda91265-1b5e-483f-8919-b0ad768010ea'
SOURCE_PATH = 'icons-json/symbol/Br_eda91265-1b5e-483f-8919-b0ad768010ea.json'
AUTHOR = 'json_to_solo'

class BrSymbol(Solo48):
    icon_id = 'br-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('br', 'symbol')

    def build(self):
        self.add_line('e0', (4, 8), (4, 40))
        self.add_line('e1', (4, 40), (11, 40))
        self.add_line('e2', (13, 8), (4, 8))
        self.add_line('e3', (14, 24), (4, 24))
        self.add_line('e4', (34, 20), (34, 40))
        self.add_bezier('e5', (11, 40), ((11.664, 40), (12.6, 39.99), (13.255, 39.99)), ((15.155, 39.99), (17.145, 39.71), (18.782, 38.57)), ((22.064, 36.28), (23.364, 30.56), (20.618, 27.2)), ((19.545, 25.88), (17.991, 25.1), (16.464, 24.66)), ((15.945, 24.52), (14.318, 24.3), (14, 24)), ((14.127, 23.96), (14.255, 23.93), (14.382, 23.89)), ((14.591, 23.84), (14.855, 23.75), (15.064, 23.68)), ((15.727, 23.44), (16.373, 23.13), (16.955, 22.72)), ((18.718, 21.49), (20.073, 19.61), (20.545, 17.37)), ((21.7, 11.86), (17.891, 8), (13, 8)))
        self.add_bezier('e6', (44, 21), ((44, 21), (44, 20.99), (43.991, 20.99)), ((43.991, 20.78), (43.227, 20.31), (43.1, 20.22)), ((41.9, 19.39), (40.473, 19.02), (39.082, 19.37)), ((36.173, 20.11), (34.755, 23.11), (34, 26)))
        self.add_contour('c0', 'e0', 'e1', 'e5', 'e2', closed=True)
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e6')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c2')
