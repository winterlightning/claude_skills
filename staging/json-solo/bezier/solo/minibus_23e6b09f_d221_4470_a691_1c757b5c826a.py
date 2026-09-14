"""Minibus (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '23e6b09f-d221-4470-a691-1c757b5c826a'
SOURCE_PATH = 'icons-json/symbol/minibus_23e6b09f-d221-4470-a691-1c757b5c826a.json'
AUTHOR = 'json_to_solo'

class Minibus23e6b09f(Solo48):
    icon_id = 'minibus-23e6b09f'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('minibus', 'symbol')

    def build(self):
        self.add_line('e0', (4, 20), (44, 20))
        self.add_line('e1', (31, 35), (18, 35))
        self.add_line('e2', (40, 35), (42, 35))
        self.add_line('e3', (44, 32), (44, 11))
        self.add_line('e4', (41, 8), (10, 8))
        self.add_line('e5', (9, 10), (4, 19))
        self.add_line('e6', (4, 21), (4, 32))
        self.add_line('e7', (6, 35), (9, 35))
        self.add_arc('e8-top', (31, 35), (41, 35), radius_x=5)
        self.add_arc('e8-bottom', (41, 35), (31, 35), radius_x=5)
        self.add_arc('e9-top', (8, 35), (18, 35), radius_x=5)
        self.add_arc('e9-bottom', (18, 35), (8, 35), radius_x=5)
        self.add_bezier('e10', (42, 35), ((42.864, 34.33), (43.991, 33.54), (43.991, 32.22)), ((43.991, 32.15), (44, 32.07), (44, 32)))
        self.add_bezier('e11', (44, 11), ((43.991, 10.95), (43.991, 10.91), (43.982, 10.86)), ((43.982, 9.23), (42.182, 8.38), (41, 8)))
        self.add_bezier('e12', (10, 8), ((9.064, 8.59), (9.536, 8.93), (9, 10)))
        self.add_bezier('e13', (4, 19), ((4, 19.67), (4, 20.33), (4, 21)))
        self.add_bezier('e14', (4, 32), ((4.009, 32.04), (4.009, 32.07), (4.018, 32.11)), ((4.018, 33.52), (5.018, 34.33), (6, 35)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e10', 'e3', 'e11', 'e4', 'e12', 'e5', 'e13', 'e6', 'e14', 'e7')
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.add_contour('e9', 'e9-top', 'e9-bottom', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'e8')
        self.relate('connect', 'c1', 'e9')
        self.relate('connect', 'c2', 'e8')
        self.relate('connect', 'c2', 'e9')
