"""Hexagon (design), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3b80eece-f8c5-5b40-be2c-8ab9383900e3'
SOURCE_PATH = 'icons-json/design/hexagon_3b80eece-f8c5-5b40-be2c-8ab9383900e3.json'
AUTHOR = 'json_to_solo'

class Hexagon(Solo48):
    icon_id = 'hexagon'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('hexagon', 'design')

    def build(self):
        self.add_line('e0', (23, 44), (10, 35))
        self.add_line('e1', (8, 31), (8, 16))
        self.add_line('e2', (11, 12), (22, 5))
        self.add_line('e3', (26, 5), (38, 12))
        self.add_line('e4', (40, 17), (40, 32))
        self.add_line('e5', (37, 36), (26, 43))
        self.add_bezier('e6', (26, 43), ((25.436, 43.345), (24.758, 43.982), (24.042, 43.982)), ((23.941, 43.982), (23.848, 43.982), (23.747, 43.991)), ((23.705, 43.991), (23.655, 44), (23.613, 44)), ((23.461, 44), (23.152, 44), (23, 44)))
        self.add_bezier('e7', (10, 35), ((9.242, 34.482), (8.008, 33.555), (8.008, 32.482)), ((8.017, 32.418), (8.017, 32.355), (8.017, 32.291)), ((8.008, 32.155), (8.008, 32.027), (8, 31.891)), ((8, 31.827), (8, 31.755), (8, 31.691)), ((8, 31.545), (8, 31.136), (8, 31)))
        self.add_bezier('e8', (8, 16), ((8, 15.845), (8, 15.509), (8, 15.345)), ((8, 13.873), (9.981, 12.627), (11, 12)))
        self.add_bezier('e9', (22, 5), ((22.463, 4.709), (23.368, 4), (23.949, 4)), ((23.95, 4), (23.951, 4), (23.951, 4)), ((23.993, 4), (24.026, 4), (24.067, 4)), ((24.109, 4.009), (24.152, 4.009), (24.194, 4.018)), ((24.707, 4.018), (25.579, 4.755), (26, 5)))
        self.add_bezier('e10', (38, 12), ((38.943, 12.545), (40, 13.927), (40, 15.118)), ((40, 15.655), (40, 16.464), (40, 17)))
        self.add_bezier('e11', (40, 32), ((40, 32.2), (39.983, 32.582), (39.983, 32.773)), ((39.983, 34.264), (38.011, 35.373), (37, 36)))
        self.add_contour('c0', 'e6', 'e0', 'e7', 'e1', 'e8', 'e2', 'e9', 'e3', 'e10', 'e4', 'e11', 'e5', closed=True)
