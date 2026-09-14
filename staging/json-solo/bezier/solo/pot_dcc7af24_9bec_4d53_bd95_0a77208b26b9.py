"""Pot (furnitures), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dcc7af24-9bec-4d53-bd95-0a77208b26b9'
SOURCE_PATH = 'icons-json/furnitures/pot_dcc7af24-9bec-4d53-bd95-0a77208b26b9.json'
AUTHOR = 'json_to_solo'

class PotFurnitures(Solo48):
    icon_id = 'pot-furnitures'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('pot', 'furnitures')

    def build(self):
        self.add_line('e0', (10, 19), (12, 16))
        self.add_line('e1', (35, 33), (35, 39))
        self.add_line('e2', (32, 42), (9, 42))
        self.add_line('e3', (8, 23), (6, 19))
        self.add_line('e4', (6, 19), (31, 19))
        self.add_line('e5', (21, 6), (21, 8))
        self.add_bezier('e6', (12, 16), ((13.669, 12.67), (16.669, 8.405), (20.727, 8.455)), ((24.9, 8.504), (27.87, 11.572), (29.948, 14.885)), ((30.455, 15.687), (31.053, 16.555), (31.364, 17.455)), ((31.544, 17.995), (31.208, 18.551), (31.364, 19.091)), ((31.535, 19.705), (31.814, 20.31), (32.018, 20.915)), ((32.615, 22.699), (33.213, 24.507), (33.663, 26.34)), ((34.072, 27.993), (34.227, 29.711), (34.636, 31.364)), ((34.775, 31.945), (35, 32.378), (35, 33)))
        self.add_bezier('e7', (35, 39), ((35, 40.154), (35.43, 40.953), (34.334, 41.648)), ((34.113, 41.787), (33.753, 42), (33.483, 42)), ((33.049, 42), (32.434, 42), (32, 42)))
        self.add_bezier('e8', (9, 42), ((8.615, 42), (8.504, 42), (8.119, 42)), ((6.965, 42), (6.008, 40.544), (6.008, 39.505)), ((6.008, 39.374), (6, 39.251), (6, 39.12)), ((6, 39.063), (6.008, 38.997), (6.008, 38.932)), ((6.008, 35.348), (6.704, 31.085), (7.154, 27.494)), ((7.334, 26.045), (8.025, 24.456), (8, 23)))
        self.add_bezier('e9', (35, 31), ((38.747, 30.697), (41.992, 28.443), (41.992, 24.352)), ((41.992, 24.231), (42, 24.102), (42, 23.973)), ((42, 23.971), (42, 23.969), (42, 23.967)), ((41.992, 23.845), (41.992, 23.714), (41.984, 23.591)), ((41.984, 19.77), (38.326, 16.342), (34.563, 16.473)), ((33.385, 16.505), (32.031, 16.46), (31, 17)))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e7', 'e2', 'e8', 'e3', 'e4')
        self.add_contour('c1', 'e9')
        self.add_contour('c2', 'e5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
