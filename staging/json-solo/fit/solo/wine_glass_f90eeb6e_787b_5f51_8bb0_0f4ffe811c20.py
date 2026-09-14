"""Wine glass (drinks), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f90eeb6e-787b-5f51-8bb0-0f4ffe811c20'
SOURCE_PATH = 'icons-json/drinks/wine glass_f90eeb6e-787b-5f51-8bb0-0f4ffe811c20.json'
AUTHOR = 'json_to_solo'

class WineGlassDrinks(Solo48):
    icon_id = 'wine-glass-drinks'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    aliases = ()
    keywords = ('wine', 'glass', 'drinks')

    def build(self):
        self.add_line('e0', (13, 44), (22, 44))
        self.add_line('e1', (24, 44), (24, 29))
        self.add_line('e2', (10, 4), (36, 4))
        self.add_line('e3', (8, 15), (10, 4))
        self.add_arc('e4-1', (22, 44), (23, 44), radius_x=28)
        self.add_line('e4-2', (23, 44), (35, 44))
        self.add_arc('e5-1', (36, 4), (40, 17), radius_x=32)
        self.add_arc('e5-2', (40, 17), (19, 28), radius_x=16)
        self.add_arc('e5-3', (19, 28), (8, 18), radius_x=12)
        self.add_line('e5-4', (8, 18), (8, 15))
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e3', closed=True)
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c2')
