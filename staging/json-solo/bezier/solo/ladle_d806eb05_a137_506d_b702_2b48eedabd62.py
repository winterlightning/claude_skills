"""Ladle (food), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd806eb05-a137-506d-b702-2b48eedabd62'
SOURCE_PATH = 'icons-json/food/ladle_d806eb05-a137-506d-b702-2b48eedabd62.json'
AUTHOR = 'json_to_solo'

class LadleFood(Solo48):
    icon_id = 'ladle-food'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('ladle', 'food')

    def build(self):
        self.add_line('e0', (30, 9), (26, 36))
        self.add_line('e1', (8, 33), (26, 33))
        self.add_bezier('e2', (40, 10), ((40, 9.445), (39.992, 9.245), (39.992, 8.691)), ((39.992, 6.173), (38.434, 4), (36, 4)), ((35.999, 4), (35.998, 4), (35.997, 4)), ((35.931, 4), (35.873, 4), (35.806, 4)), ((35.36, 4), (34.905, 4.018), (34.451, 4.018)), ((32.076, 4.018), (30.379, 6.555), (30, 9)))
        self.add_bezier('e3', (26, 36), ((25.251, 40.864), (21.583, 43.991), (16.968, 43.991)), ((16.778, 43.991), (16.579, 44), (16.388, 44)), ((16.385, 44), (16.382, 44), (16.379, 44)), ((15.739, 44), (15.04, 43.809), (14.425, 43.655)), ((10.072, 42.564), (8.017, 38.482), (8.017, 33.9)), ((8.017, 33.636), (8, 33.273), (8, 33)))
        self.add_contour('c0', 'e2', 'e0', 'e3', 'e1')
