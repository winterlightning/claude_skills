"""Dill (food), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ed3fa5b-9e28-4066-bff3-a2cb767df09d'
SOURCE_PATH = 'icons-json/food/dill_4ed3fa5b-9e28-4066-bff3-a2cb767df09d.json'
AUTHOR = 'json_to_solo'

class DillFood(Solo48):
    icon_id = 'dill-food'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('dill', 'food')

    def build(self):
        self.add_line('e0', (31, 34), (29, 35))
        self.add_line('e1', (29, 35), (23, 36))
        self.add_bezier('e2', (31, 4), ((29.363, 6.009), (28.812, 8.182), (27.692, 10.364)), ((26.905, 11.918), (25.846, 13.309), (25.231, 14.909)), ((23.311, 19.918), (23.151, 25.209), (22.769, 30.364)), ((22.634, 32.173), (22.769, 34.009), (22.769, 35.818)), ((22.769, 37.636), (22.745, 39.455), (22.769, 41.273)), ((22.782, 41.945), (23.705, 43.227), (24, 44)))
        self.add_bezier('e3', (19, 9), ((19.923, 12.082), (21.775, 13.055), (25, 15)))
        self.add_bezier('e4', (8, 17), ((8.012, 17.045), (8.012, 16.809), (8.025, 16.855)), ((8.025, 17.936), (8.775, 19.191), (9.292, 20.182)), ((12.123, 25.682), (16.551, 27.427), (23, 30)))
        self.add_bezier('e5', (12, 35), ((12.837, 38.064), (15.286, 40.536), (19.606, 41.136)), ((20.64, 41.282), (21.966, 40.982), (23, 41)))
        self.add_bezier('e6', (40, 26), ((38.634, 29.709), (35.406, 32.1), (31, 34)))
        self.add_bezier('e7', (36, 9), ((32.837, 10.518), (31.791, 10.1), (28, 10)))
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6', 'e0', 'e1')
        self.add_contour('c5', 'e7')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c3', 'c0')
        self.relate('connect', 'c4', 'c0')
        self.relate('connect', 'c5', 'c0')
