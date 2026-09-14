"""Chocolate box (romance), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bcab073e-f7dd-439e-8a8a-e72d016006a4'
SOURCE_PATH = 'icons-json/romance/chocolate box_bcab073e-f7dd-439e-8a8a-e72d016006a4.json'
AUTHOR = 'json_to_solo'

class ChocolateBoxRomance(Solo48):
    icon_id = 'chocolate-box-romance'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    aliases = ()
    keywords = ('chocolate', 'box', 'romance')

    def build(self):
        self.add_line('e0', (24, 40), (24, 32))
        self.add_line('e1', (24, 40), (6, 28))
        self.add_line('e2', (4, 25), (4, 17))
        self.add_line('e3', (24, 40), (41, 28))
        self.add_line('e4', (44, 24), (44, 20))
        self.add_line('e5', (44, 20), (44, 17))
        self.add_line('e6', (44, 17), (40, 20))
        self.add_line('e7', (40, 20), (24, 32))
        self.add_line('e8', (4, 17), (8, 20))
        self.add_line('e9', (8, 20), (24, 32))
        self.add_bezier('e10', (6, 28), ((5.055, 27.385), (4, 26.055), (4, 24.96)), ((4, 24.918), (4, 25.042), (4, 25)))
        self.add_bezier('e11', (41, 28), ((42.118, 27.242), (44, 25.331), (44, 24)))
        self.add_bezier('e12', (44, 17), ((44, 15.846), (43.991, 14.956), (43.991, 13.802)), ((43.991, 13.339), (43.636, 12.733), (43.4, 12.345)), ((41.727, 9.667), (38.027, 8.017), (34.727, 8.017)), ((34.513, 8.017), (34.289, 8), (34.074, 8)), ((34.07, 8), (34.067, 8), (34.064, 8)), ((33.7, 8), (33.336, 8.017), (32.973, 8.017)), ((30.736, 8.017), (28.282, 8.758), (26.436, 9.895)), ((26, 10.164), (24.064, 11.764), (24.064, 11.764)), ((23.9, 11.638), (23.736, 11.512), (23.573, 11.385)), ((22.882, 10.846), (22.227, 10.282), (21.455, 9.844)), ((19.582, 8.775), (17.218, 8.017), (14.991, 8.017)), ((14.773, 8.017), (14.555, 8), (14.336, 8)), ((14.045, 8), (13.745, 8.017), (13.455, 8.017)), ((9.818, 8.017), (4.009, 10.282), (4.009, 14.291)), ((4.009, 14.459), (4, 14.627), (4, 14.796)), ((4, 15.04), (4.018, 15.284), (4.018, 15.528)), ((4.018, 15.604), (4.009, 15.672), (4.009, 15.747)), ((4.009, 15.916), (4, 16.084), (4, 16.244)), ((4, 16.589), (4, 16.663), (4, 17)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e10', 'e2')
        self.add_contour('c2', 'e3', 'e11', 'e4', 'e5')
        self.add_contour('c3', 'e6', 'e7')
        self.add_contour('c4', 'e12')
        self.add_contour('c5', 'e8', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
