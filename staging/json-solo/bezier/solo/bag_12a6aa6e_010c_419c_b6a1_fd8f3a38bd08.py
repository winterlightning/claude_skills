"""Bag (shopping), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '12a6aa6e-010c-419c-b6a1-fd8f3a38bd08'
SOURCE_PATH = 'icons-json/shopping/bag_12a6aa6e-010c-419c-b6a1-fd8f3a38bd08.json'
AUTHOR = 'json_to_solo'

class Bag12a6aa6e(Solo48):
    icon_id = 'bag-12a6aa6e'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('bag', 'shopping')

    def build(self):
        self.add_line('e0', (16, 19), (16, 12))
        self.add_line('e1', (32, 12), (32, 19))
        self.add_line('e2', (32, 44), (14, 44))
        self.add_line('e3', (8, 35), (11, 15))
        self.add_line('e4', (11, 15), (37, 15))
        self.add_line('e5', (37, 15), (40, 37))
        self.add_bezier('e6', (16, 12), ((16, 8.036), (20.025, 4.009), (23.587, 4.009)), ((23.72, 4.009), (23.844, 4), (23.977, 4)), ((23.979, 4), (23.981, 4), (23.983, 4)), ((24.109, 4), (24.244, 4.009), (24.371, 4.009)), ((28.177, 4.009), (32, 7.764), (32, 12)))
        self.add_bezier('e7', (40, 37), ((40, 37.764), (39.983, 38.245), (39.983, 39.009)), ((39.983, 39.464), (39.688, 40.036), (39.512, 40.445)), ((38.442, 42.873), (36.211, 43.982), (33.827, 43.982)), ((33.356, 43.982), (32.472, 44), (32, 44)))
        self.add_bezier('e8', (14, 44), ((13.933, 44), (13.76, 43.991), (13.684, 43.991)), ((11.183, 43.991), (8, 41.364), (8, 38.482)), ((8, 38.409), (8, 38.336), (8, 38.264)), ((8, 37.145), (8, 36.118), (8, 35)))
        self.add_contour('c0', 'e0', 'e6', 'e1')
        self.add_contour('c1', 'e7', 'e2', 'e8', 'e3', 'e4', 'e5', closed=True)
