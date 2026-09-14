"""Restaurant fork knife (food), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24a6b06c-3fec-43a0-aca0-b205c99c496b'
SOURCE_PATH = 'icons-json/food/restaurant fork knife_24a6b06c-3fec-43a0-aca0-b205c99c496b.json'
AUTHOR = 'json_to_solo'

class RestaurantForkKnifeFood(Solo48):
    icon_id = 'restaurant-fork-knife-food'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('restaurant', 'fork', 'knife', 'food')

    def build(self):
        self.add_line('e0', (16, 4), (16, 19))
        self.add_line('e1', (8, 4), (8, 12))
        self.add_line('e2', (16, 44), (16, 19))
        self.add_line('e3', (24, 4), (24, 12))
        self.add_line('e4', (32, 44), (32, 28))
        self.add_line('e5', (32, 4), (32, 28))
        self.add_line('e6', (32, 28), (39, 28))
        self.add_line('e7', (40, 22), (39, 15))
        self.add_bezier('e8', (8, 12), ((8, 12.609), (8.39, 13.473), (8.67, 14.009)), ((10.19, 16.927), (12.65, 18.564), (16, 19)))
        self.add_bezier('e9', (24, 12), ((24, 12.627), (23.51, 13.691), (23.21, 14.245)), ((21.58, 17.191), (19.45, 18.582), (16, 19)))
        self.add_bezier('e10', (39, 28), ((39.52, 27.7), (39.99, 27.264), (39.99, 26.609)), ((39.99, 26.555), (40, 26.5), (40, 26.445)), ((40, 26.209), (39.98, 25.973), (39.98, 25.736)), ((39.98, 25.518), (39.98, 25.291), (39.98, 25.064)), ((39.98, 24.818), (40, 24.564), (40, 24.309)), ((40, 23.6), (40, 22.709), (40, 22)))
        self.add_bezier('e11', (39, 15), ((38.59, 12.009), (37.82, 7.009), (35.06, 5.136)), ((34.12, 4.5), (33.14, 4.291), (32, 4)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e8')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e9')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5', 'e6', 'e10', 'e7', 'e11', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c4', 'c5')
