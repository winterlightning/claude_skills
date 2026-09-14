"""Glass (drinks), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3ad0cd10-bf8c-4b51-9e81-06a67e3d6f68'
SOURCE_PATH = 'icons-json/drinks/glass_3ad0cd10-bf8c-4b51-9e81-06a67e3d6f68.json'
AUTHOR = 'json_to_solo'

class GlassDrinks(Solo48):
    icon_id = 'glass-drinks'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    aliases = ()
    keywords = ('glass', 'drinks')

    def build(self):
        self.add_line('e0', (24, 44), (24, 29))
        self.add_line('e1', (14, 44), (34, 44))
        self.add_line('e2', (8, 14), (8, 4))
        self.add_line('e3', (8, 4), (40, 4))
        self.add_line('e4', (40, 4), (40, 16))
        self.add_arc('e5-1', (40, 16), (20, 28), radius_x=16)
        self.add_arc('e5-2', (20, 28), (8, 14), radius_x=15)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4', 'e5-1', 'e5-2', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
