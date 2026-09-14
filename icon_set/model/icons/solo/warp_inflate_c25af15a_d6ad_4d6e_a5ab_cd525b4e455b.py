"""Warp inflate (design), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c25af15a-d6ad-4d6e-a5ab-cd525b4e455b'
SOURCE_PATH = 'icons-json/design/warp inflate_c25af15a-d6ad-4d6e-a5ab-cd525b4e455b.json'
AUTHOR = 'json_to_solo'

class WarpInflate(Solo48):
    icon_id = 'warp-inflate'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'inflate', 'design')

    def build(self):
        self.add_bezier('e0', (11, 11), ((6.609, 13.745), (4.009, 18.189), (4.009, 23.217)), ((4.009, 23.316), (4, 23.408), (4, 23.507)), ((4, 23.508), (4, 23.51), (4, 23.512)), ((4, 23.891), (4.009, 24.261), (4.009, 24.64)), ((4.009, 34.131), (13.191, 39.992), (22.745, 39.992)), ((22.924, 39.992), (23.103, 40), (23.282, 40)), ((23.285, 40), (23.288, 40), (23.291, 40)), ((23.773, 40), (24.245, 39.992), (24.727, 39.992)), ((32.418, 39.992), (40.091, 36.758), (42.9, 29.726)), ((43.545, 28.101), (43.991, 26.299), (43.991, 24.556)), ((43.991, 24.456), (44, 24.365), (44, 24.266)), ((44, 24.264), (44, 24.263), (44, 24.261)), ((44, 23.975), (43.991, 23.697), (43.991, 23.411)), ((43.991, 13.92), (34.436, 8.017), (24.918, 8.017)), ((24.712, 8.017), (24.498, 8), (24.292, 8)), ((24.288, 8), (24.285, 8), (24.282, 8)), ((23.782, 8), (23.273, 8.017), (22.773, 8.017)), ((18.691, 8.017), (14.418, 9.021), (11, 11)))
        self.add_contour('c0', 'e0', closed=True)
