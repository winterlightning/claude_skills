"""Chef gear mug (drinks), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('e7', (39, 31), (44, 25), radius_x=7, sweep=False)
        self.add_arc('e8', (44, 17), (39, 12), radius_x=7, sweep=False)
        self.add_arc('e9-1', (4, 31), (7, 38), radius_x=10, sweep=False)
        self.add_arc('e9-2', (7, 38), (11, 40), radius_x=8, sweep=False)
        self.add_arc('e9-3', (11, 40), (14, 40), radius_x=25)
        self.add_line('e10-1', (25, 40), (29, 39))
        self.add_arc('e10-2', (29, 39), (32, 36), radius_x=8, sweep=False)
        self.add_arc('e10-3', (32, 36), (33, 31), radius_x=9, sweep=False)
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8', 'e2')
        self.add_contour('c1', 'e9-1', 'e9-2', 'e9-3', 'e3', 'e10-1', 'e10-2', 'e10-3', 'e4', 'e5', 'e6', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
