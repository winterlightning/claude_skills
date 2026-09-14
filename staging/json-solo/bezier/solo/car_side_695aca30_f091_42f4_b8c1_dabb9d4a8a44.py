"""Car side (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '695aca30-f091-42f4-b8c1-dabb9d4a8a44'
SOURCE_PATH = 'icons-json/symbol/car side_695aca30-f091-42f4-b8c1-dabb9d4a8a44.json'
AUTHOR = 'json_to_solo'

class CarSideSymbol(Solo48):
    icon_id = 'car-side-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('car', 'side', 'symbol')

    def build(self):
        self.add_line('e0', (39, 34), (42, 34))
        self.add_line('e1', (28, 34), (19, 34))
        self.add_line('e2', (10, 19), (15, 10))
        self.add_line('e3', (18, 8), (29, 8))
        self.add_line('e4', (30, 9), (37, 19))
        self.add_line('e5', (10, 19), (37, 19))
        self.add_arc('e6-top', (28, 34), (38, 34), radius_x=5, radius_y=6)
        self.add_arc('e6-bottom', (38, 34), (28, 34), radius_x=5, radius_y=6)
        self.add_arc('e7-top', (8, 34), (18, 34), radius_x=5, radius_y=6)
        self.add_arc('e7-bottom', (18, 34), (8, 34), radius_x=5, radius_y=6)
        self.add_bezier('e8', (42, 34), ((42.873, 33.56), (43.982, 33.08), (43.982, 31.82)), ((43.991, 31.74), (43.991, 31.67), (44, 31.59)), ((44, 31.07), (43.982, 30.54), (43.982, 30.01)), ((43.982, 29.49), (43.982, 28.96), (43.982, 28.44)), ((43.982, 28.07), (44, 27.69), (44, 27.32)), ((44, 27.316), (44, 27.313), (44, 27.309)), ((44, 27.083), (43.991, 26.857), (43.991, 26.64)), ((43.991, 22.64), (40.536, 19), (37, 19)))
        self.add_bezier('e9', (8, 34), ((5.673, 34), (4.009, 34.23), (4.009, 30.88)), ((4.009, 30.742), (4, 30.595), (4, 30.447)), ((4, 30.445), (4, 30.442), (4, 30.44)), ((4, 30.29), (4.018, 30.14), (4.018, 30)), ((4.018, 28.84), (4.018, 27.68), (4.018, 26.53)), ((4.018, 26.15), (4, 25.78), (4, 25.41)), ((4, 25.22), (4.018, 25.04), (4.018, 24.85)), ((4.018, 22.53), (5.773, 19.65), (7.882, 19.11)), ((8.664, 18.91), (9.2, 19), (10, 19)))
        self.add_bezier('e10', (15, 10), ((15.564, 8.89), (16.982, 8.37), (18, 8)))
        self.add_bezier('e11', (29, 8), ((29.027, 8), (28.6, 8.01), (28.627, 8.01)), ((29.309, 8.01), (29.491, 8.59), (30, 9)))
        self.add_contour('c0', 'e0', 'e8')
        self.add_contour('c1', 'e9')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e2', 'e10', 'e3', 'e11', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.add_contour('e7', 'e7-top', 'e7-bottom', closed=True)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c0', 'e6')
        self.relate('connect', 'c1', 'e7')
        self.relate('connect', 'c2', 'e6')
        self.relate('connect', 'c2', 'e7')
