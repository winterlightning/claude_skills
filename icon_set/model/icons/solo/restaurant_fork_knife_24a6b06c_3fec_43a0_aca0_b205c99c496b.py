"""Restaurant fork knife (food), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24a6b06c-3fec-43a0-aca0-b205c99c496b'
SOURCE_PATH = 'icons-json/food/restaurant fork knife_24a6b06c-3fec-43a0-aca0-b205c99c496b.json'
AUTHOR = 'json_to_solo'

class RestaurantForkKnife(Solo48):
    icon_id = 'restaurant-fork-knife'
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
        self.add_arc('e8', (8, 12), (16, 19), radius_x=9, sweep=False)
        self.add_arc('e9', (24, 12), (16, 19), radius_x=9)
        self.add_line('e10-1', (39, 28), (40, 24))
        self.add_arc('e10-2', (40, 24), (40, 22), radius_x=26)
        self.add_arc('e11', (39, 15), (32, 4), radius_x=10, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e8')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e9')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5', 'e6', 'e10-1', 'e10-2', 'e7', 'e11', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c4', 'c5')
