"""Expand (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fcf922f1-c091-4a41-9a2c-3b6016b7cf68'
SOURCE_PATH = 'icons-json/interface-essential/expand_fcf922f1-c091-4a41-9a2c-3b6016b7cf68.json'
AUTHOR = 'json_to_solo'

class ExpandInterfaceEssential(Solo48):
    icon_id = 'expand-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('expand', 'interface-essential')

    def build(self):
        self.add_line('e0', (4, 17), (4, 9))
        self.add_line('e1', (5, 8), (15, 8))
        self.add_line('e2', (33, 8), (43, 8))
        self.add_line('e3', (44, 10), (44, 17))
        self.add_line('e4', (4, 31), (4, 39))
        self.add_line('e5', (6, 40), (15, 40))
        self.add_line('e6', (33, 40), (42, 40))
        self.add_line('e7', (44, 38), (44, 31))
        self.add_line('e8', (36, 31), (12, 31))
        self.add_line('e9', (11, 29), (11, 19))
        self.add_line('e10', (13, 17), (36, 17))
        self.add_line('e11', (37, 19), (37, 30))
        self.add_bezier('e12', (4, 9), ((4.2, 8.66), (4.182, 8.35), (4.564, 8.13)), ((4.673, 8.07), (4.9, 8.08), (5, 8)))
        self.add_bezier('e13', (43, 8), ((43.755, 8.92), (43.782, 8.75), (44, 10)))
        self.add_bezier('e14', (4, 39), ((4.127, 39.12), (4.109, 39.23), (4.209, 39.37)), ((4.455, 39.72), (5.136, 39.99), (5.527, 39.99)), ((5.627, 39.99), (5.9, 40), (6, 40)))
        self.add_bezier('e15', (42, 40), ((42.164, 39.91), (42.555, 39.96), (42.718, 39.88)), ((43.109, 39.68), (43.7, 39.04), (43.882, 38.62)), ((43.964, 38.43), (43.918, 38.19), (44, 38)))
        self.add_bezier('e16', (12, 31), ((11.245, 30.17), (11.164, 30.16), (11, 29)))
        self.add_bezier('e17', (11, 19), ((11.473, 17.64), (11.782, 17.55), (13, 17)))
        self.add_bezier('e18', (36, 17), ((36.7, 17.81), (36.836, 17.86), (37, 19)))
        self.add_bezier('e19', (37, 30), ((36.536, 30.66), (36.618, 30.48), (36, 31)))
        self.add_contour('c0', 'e0', 'e12', 'e1')
        self.add_contour('c1', 'e2', 'e13', 'e3')
        self.add_contour('c2', 'e4', 'e14', 'e5')
        self.add_contour('c3', 'e6', 'e15', 'e7')
        self.add_contour('c4', 'e8', 'e16', 'e9', 'e17', 'e10', 'e18', 'e11', 'e19', closed=True)
