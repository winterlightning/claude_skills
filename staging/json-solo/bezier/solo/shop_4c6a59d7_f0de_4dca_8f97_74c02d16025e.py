"""Shop (shopping), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4c6a59d7-f0de-4dca-8f97-74c02d16025e'
SOURCE_PATH = 'icons-json/shopping/shop_4c6a59d7-f0de-4dca-8f97-74c02d16025e.json'
AUTHOR = 'json_to_solo'

class Shop(Solo48):
    icon_id = 'shop'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('shop', 'shopping')

    def build(self):
        self.add_line('e0', (29, 40), (29, 30))
        self.add_line('e1', (29, 30), (19, 30))
        self.add_line('e2', (19, 30), (19, 40))
        self.add_line('e3', (29, 40), (19, 40))
        self.add_line('e4', (29, 40), (41, 40))
        self.add_line('e5', (41, 40), (41, 21))
        self.add_line('e6', (19, 40), (8, 40))
        self.add_line('e7', (8, 40), (8, 22))
        self.add_line('e8', (44, 16), (41, 8))
        self.add_line('e9', (41, 8), (7, 8))
        self.add_line('e10', (7, 8), (4, 17))
        self.add_bezier('e11', (34, 18), ((34, 18.278), (34, 18.722), (34, 19)))
        self.add_bezier('e12', (24, 18), ((24, 18.564), (24, 19.419), (24, 20)))
        self.add_bezier('e13', (14, 18), ((14, 18.025), (14, 18.156), (14, 18.181)), ((14, 18.72), (14, 19.461), (14, 20)))
        self.add_bezier('e14', (41, 21), ((40.791, 21.076), (40.191, 21.895), (39.7, 22.004)), ((37.082, 22.552), (35.373, 20.667), (34, 19)))
        self.add_bezier('e15', (41, 21), ((42.282, 20.352), (43.991, 19.638), (43.991, 18.131)), ((43.991, 18.088), (44, 18.046), (44, 18.004)), ((44, 17.474), (44, 16.531), (44, 16)))
        self.add_bezier('e16', (4, 17), ((4, 17.278), (4.009, 17.811), (4.009, 18.088)), ((4.009, 20.185), (6.2, 21.082), (8, 22)))
        self.add_bezier('e17', (14, 20), ((11.891, 22.56), (11.491, 22.876), (8, 22)))
        self.add_bezier('e18', (14, 20), ((14.464, 20.514), (15.055, 21.103), (15.664, 21.592)), ((17.345, 22.947), (19.945, 23.175), (21.8, 21.954)), ((22.655, 21.389), (23.336, 20.716), (24, 20)))
        self.add_bezier('e19', (24, 20), ((24.582, 20.623), (25.164, 21.171), (25.927, 21.642)), ((27.782, 22.779), (30.309, 22.375), (31.964, 21.103)), ((32.755, 20.505), (33.373, 19.716), (34, 19)))
        self.add_contour('c0', 'e11')
        self.add_contour('c1', 'e12')
        self.add_contour('c2', 'e13')
        self.add_contour('c3', 'e0', 'e1', 'e2')
        self.add_contour('c4', 'e3')
        self.add_contour('c5', 'e4', 'e5')
        self.add_contour('c6', 'e6', 'e7')
        self.add_contour('c7', 'e14')
        self.add_contour('c8', 'e15', 'e8', 'e9', 'e10', 'e16')
        self.add_contour('c9', 'e17')
        self.add_contour('c10', 'e18')
        self.add_contour('c11', 'e19')
        self.relate('connect', 'c0', 'c11')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c11', 'c7')
        self.relate('connect', 'c1', 'c10')
        self.relate('connect', 'c1', 'c11')
        self.relate('connect', 'c10', 'c11')
        self.relate('connect', 'c10', 'c2')
        self.relate('connect', 'c10', 'c9')
        self.relate('connect', 'c2', 'c9')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c5', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c6', 'c9')
        self.relate('connect', 'c8', 'c9')
