"""Deepfake face (artificial-intelligence), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'efa0e2aa-ab3d-4293-a005-4044f8760a5e'
SOURCE_PATH = 'icons-json/artificial-intelligence/deepfake face_efa0e2aa-ab3d-4293-a005-4044f8760a5e.json'
AUTHOR = 'json_to_solo'

class DeepfakeFaceEfa0e2aa(Solo48):
    icon_id = 'deepfake-face-efa0e2aa'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('deepfake', 'face', 'artificial-intelligence')

    def build(self):
        self.add_line('e0', (40, 19), (8, 19))
        self.add_line('e1', (24, 28), (24, 4))
        self.add_line('e2', (40, 26), (40, 12))
        self.add_line('e3', (8, 19), (8, 29))
        self.add_bezier('e4', (16, 30), ((19.806, 36.3), (28.152, 36.182), (32, 30)))
        self.add_bezier('e5', (40, 12), ((40, 11.164), (39.192, 9.818), (38.787, 9.109)), ((36.185, 4.609), (32.657, 4.018), (28.109, 4.018)), ((26.846, 4.018), (25.583, 4), (24.32, 4)), ((24.211, 4), (24.109, 4), (24, 4)), ((22.324, 4), (20.64, 4.018), (18.964, 4.018)), ((17.432, 4.018), (15.882, 4.055), (14.417, 4.609)), ((10.535, 6.082), (8.017, 10.382), (8.017, 14.736)), ((8.017, 15.418), (8, 16.091), (8, 16.773)), ((8, 17.364), (8, 17.955), (8, 18.545)), ((8.008, 20.555), (8, 16.936), (8, 19)))
        self.add_bezier('e6', (8, 29), ((8, 30.564), (8.884, 32.282), (9.491, 33.691)), ((11.983, 39.436), (17.297, 43.982), (23.368, 43.982)), ((23.646, 43.982), (23.916, 44), (24.185, 44)), ((24.19, 44), (24.194, 44), (24.199, 44)), ((24.489, 44), (24.771, 43.982), (25.053, 43.982)), ((26.055, 43.982), (27.091, 43.691), (28.051, 43.427)), ((35.057, 41.5), (39.992, 33.991), (39.992, 26.264)), ((39.992, 26.118), (40, 26.145), (40, 26)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e2', 'e5', 'e3', 'e6', closed=True)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
