"""Cake cherry (food), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0c27f58f-0b93-5b1c-8a4f-22dd9939aa7b'
SOURCE_PATH = 'icons-json/food/cake cherry_0c27f58f-0b93-5b1c-8a4f-22dd9939aa7b.json'
AUTHOR = 'json_to_solo'

class CakeCherryFood(Solo48):
    icon_id = 'cake-cherry-food'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('cake', 'cherry', 'food')

    def build(self):
        self.add_line('e0', (7, 26), (6, 31))
        self.add_line('e1', (6, 31), (6, 42))
        self.add_line('e2', (6, 42), (42, 42))
        self.add_line('e3', (42, 42), (42, 31))
        self.add_line('e4', (42, 31), (6, 31))
        self.add_line('e5', (30, 20), (42, 31))
        self.add_arc('e6-top', (19, 17), (31, 17), radius_x=6)
        self.add_arc('e6-bottom', (31, 17), (19, 17), radius_x=6)
        self.add_bezier('e7', (26, 11), ((27.497, 8.799), (28.205, 7.383), (30.832, 6.532)), ((31.642, 6.27), (32.468, 6.008), (33.327, 6.008)), ((33.464, 6.008), (33.609, 6), (33.746, 6)), ((33.748, 6), (33.751, 6), (33.753, 6)), ((33.892, 6), (34.039, 6.016), (34.178, 6.016)), ((35.144, 6.016), (36.1, 6.689), (37, 7)))
        self.add_bezier('e8', (19, 16), ((14.418, 16.794), (10.165, 19.189), (7.849, 23.329)), ((7.473, 24), (7.131, 25.231), (7, 26)))
        self.add_contour('c0', 'e7')
        self.add_contour('c1', 'e8', 'e0', 'e1', 'e2', 'e3', 'e4')
        self.add_contour('c2', 'e5')
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.relate('connect', 'c0', 'e6')
        self.relate('connect', 'c1', 'e6')
        self.relate('connect', 'c2', 'e6')
