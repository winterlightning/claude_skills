"""Virtual shopping (shopping), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '14954394-1829-4d67-aae8-913ee0e98be3'
SOURCE_PATH = 'icons-json/shopping/virtual shopping_14954394-1829-4d67-aae8-913ee0e98be3.json'
AUTHOR = 'json_to_solo'

class VirtualShoppingShopping(Solo48):
    icon_id = 'virtual-shopping-shopping'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('virtual', 'shopping')

    def build(self):
        self.add_line('e0', (17, 20), (17, 16))
        self.add_line('e1', (31, 20), (31, 16))
        self.add_line('e2', (17, 16), (11, 16))
        self.add_line('e3', (11, 16), (8, 42))
        self.add_line('e4', (10, 44), (38, 44))
        self.add_line('e5', (40, 41), (37, 17))
        self.add_line('e6', (36, 16), (31, 16))
        self.add_line('e7', (17, 16), (31, 16))
        self.add_bezier('e8', (8, 42), ((8.244, 42.691), (8.488, 43.682), (9.263, 43.927)), ((9.364, 43.964), (9.899, 43.955), (10, 44)))
        self.add_bezier('e9', (38, 44), ((38.135, 43.918), (38.627, 43.955), (38.771, 43.882)), ((39.545, 43.473), (40, 42.427), (40, 41.536)), ((40, 41.455), (40, 41.091), (40, 41)))
        self.add_bezier('e10', (37, 17), ((36.916, 16.755), (36.463, 16.227), (36.379, 15.982)), ((36.177, 15.927), (36.194, 16.055), (36, 16)))
        self.add_bezier('e11', (17, 16), ((17, 12.073), (16.842, 8.118), (20.051, 5.373)), ((21.036, 4.536), (22.383, 4), (23.638, 4)), ((23.64, 4), (23.642, 4), (23.645, 4)), ((23.786, 4), (23.935, 4), (24.076, 4)), ((25.44, 4), (26.796, 4.564), (27.865, 5.464)), ((31.015, 8.109), (31, 12.145), (31, 16)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e8', 'e4', 'e9', 'e5', 'e10', 'e6')
        self.add_contour('c3', 'e7')
        self.add_contour('c4', 'e11')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
