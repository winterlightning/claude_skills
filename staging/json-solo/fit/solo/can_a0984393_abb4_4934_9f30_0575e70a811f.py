"""Can (food), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0984393-abb4-4934-9f30-0575e70a811f'
SOURCE_PATH = 'icons-json/food/can_a0984393-abb4-4934-9f30-0575e70a811f.json'
AUTHOR = 'json_to_solo'

class CanFood(Solo48):
    icon_id = 'can-food'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('can', 'food')

    def build(self):
        self.add_line('e0', (8, 8), (8, 40))
        self.add_line('e1', (40, 39), (40, 7))
        self.add_arc('e2', (40, 9), (8, 9), radius_x=49)
        self.add_arc('e3-1', (40, 7), (36, 5), radius_x=8, sweep=False)
        self.add_line('e3-2', (36, 5), (24, 4))
        self.add_line('e3-3', (24, 4), (14, 5))
        self.add_arc('e3-4', (14, 5), (8, 8), radius_x=9, sweep=False)
        self.add_arc('e4-1', (8, 40), (13, 43), radius_x=8, sweep=False)
        self.add_line('e4-2', (13, 43), (25, 44))
        self.add_line('e4-3', (25, 44), (35, 43))
        self.add_arc('e4-4', (35, 43), (40, 40), radius_x=6, sweep=False)
        self.add_arc('e4-5', (40, 40), (40, 39), radius_x=39)
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e1', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
