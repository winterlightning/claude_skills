"""Shopping bag side (shopping), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8de2d82c-4baa-5ded-96de-26a834bd33ff'
SOURCE_PATH = 'icons-json/shopping/shopping bag side_8de2d82c-4baa-5ded-96de-26a834bd33ff.json'
AUTHOR = 'json_to_solo'

class ShoppingBagSideShopping(Solo48):
    icon_id = 'shopping-bag-side-shopping'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('shopping', 'bag', 'side')

    def build(self):
        self.add_line('e0', (31, 23), (29, 44))
        self.add_line('e1', (37, 44), (11, 44))
        self.add_line('e2', (8, 40), (12, 14))
        self.add_line('e3', (12, 14), (37, 14))
        self.add_line('e4', (37, 14), (40, 39))
        self.add_bezier('e5', (17, 14), ((17.042, 12.645), (17.213, 11.173), (17.448, 9.836)), ((18.055, 6.436), (20.876, 4.009), (24.076, 4.009)), ((24.227, 4.009), (24.379, 4), (24.531, 4)), ((24.531, 4), (24.532, 4), (24.533, 4)), ((24.582, 4), (24.624, 4), (24.665, 4)), ((25.844, 4), (27.04, 4.582), (28.008, 5.245)), ((32.404, 8.282), (31.52, 14.709), (31.074, 19.5)), ((30.956, 20.691), (31.093, 21.8), (31, 23)))
        self.add_bezier('e6', (40, 39), ((40, 39.364), (39.983, 40.182), (39.983, 40.536)), ((39.983, 42.055), (38.373, 44), (37, 44)))
        self.add_bezier('e7', (11, 44), ((10.865, 43.991), (11.099, 43.991), (10.964, 43.982)), ((9.718, 43.982), (8.017, 42.845), (8.017, 41.336)), ((8.008, 41.191), (8.008, 41.036), (8, 40.891)), ((8, 40.718), (8, 40.173), (8, 40)))
        self.add_contour('c0', 'e5', 'e0')
        self.add_contour('c1', 'e6', 'e1', 'e7', 'e2', 'e3', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
