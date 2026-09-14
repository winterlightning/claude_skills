"""Chef gear mug (drinks), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ea635154-59f7-5bc5-ae1e-ab8af03b4397'
SOURCE_PATH = 'icons-json/drinks/chef gear mug_ea635154-59f7-5bc5-ae1e-ab8af03b4397.json'
AUTHOR = 'json_to_solo'

class ChefGearMugDrinks(Solo48):
    icon_id = 'chef-gear-mug-drinks'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    aliases = ()
    keywords = ('chef', 'gear', 'mug', 'drinks')

    def build(self):
        self.add_line('e0', (33, 31), (39, 31))
        self.add_line('e1', (44, 25), (44, 17))
        self.add_line('e2', (39, 12), (33, 12))
        self.add_line('e3', (14, 40), (25, 40))
        self.add_line('e4', (33, 31), (33, 8))
        self.add_line('e5', (33, 8), (4, 8))
        self.add_line('e6', (4, 8), (4, 31))
        self.add_bezier('e7', (39, 31), ((41.155, 30.208), (43.064, 28.581), (43.691, 26.467)), ((43.818, 26.021), (43.982, 25.516), (43.982, 25.053)), ((43.991, 24.977), (43.991, 25.067), (44, 25)))
        self.add_bezier('e8', (44, 17), ((44, 15.139), (41.064, 12), (39, 12)))
        self.add_bezier('e9', (4, 31), ((4, 31.067), (4, 30.88), (4, 30.947)), ((4, 34.594), (5.982, 38.366), (9.855, 39.646)), ((10.873, 39.983), (12.164, 39.992), (13.218, 39.992)), ((13.482, 39.992), (13.736, 40), (14, 40)))
        self.add_bezier('e10', (25, 40), ((25.164, 40), (25.227, 39.983), (25.391, 39.983)), ((29.182, 39.983), (32.364, 37.044), (32.936, 33.667)), ((33.1, 32.716), (33, 31.96), (33, 31)))
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8', 'e2')
        self.add_contour('c1', 'e9', 'e3', 'e10', 'e4', 'e5', 'e6', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
