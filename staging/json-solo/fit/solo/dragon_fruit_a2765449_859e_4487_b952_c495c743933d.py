"""Dragon fruit (food), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2765449-859e-4487-b952-c495c743933d'
SOURCE_PATH = 'icons-json/food/dragon fruit_a2765449-859e-4487-b952-c495c743933d.json'
AUTHOR = 'json_to_solo'

class DragonFruitFood(Solo48):
    icon_id = 'dragon-fruit-food'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('dragon', 'fruit', 'food')

    def build(self):
        self.add_line('e0', (19, 15), (23, 5))
        self.add_line('e1', (25, 6), (29, 15))
        self.add_line('e2', (38, 22), (40, 22))
        self.add_line('e3', (38, 27), (37, 32))
        self.add_line('e4', (11, 32), (11, 27))
        self.add_line('e5-1', (23, 5), (25, 4))
        self.add_line('e5-2', (25, 4), (25, 6))
        self.add_arc('e6-1', (29, 15), (31, 10), radius_x=15, sweep=False)
        self.add_arc('e6-2', (31, 10), (32, 11), radius_x=1)
        self.add_arc('e6-3', (32, 11), (36, 24), radius_x=36)
        self.add_arc('e6-4', (36, 24), (38, 22), radius_x=8)
        self.add_arc('e7', (40, 22), (38, 27), radius_x=11, sweep=False)
        self.add_arc('e8-1', (37, 32), (31, 42), radius_x=15)
        self.add_line('e8-2', (31, 42), (24, 44))
        self.add_arc('e8-3', (24, 44), (14, 39), radius_x=13)
        self.add_arc('e8-4', (14, 39), (11, 32), radius_x=21)
        self.add_line('e9-1', (11, 27), (8, 22))
        self.add_arc('e9-2', (8, 22), (12, 23), radius_x=7)
        self.add_arc('e9-3', (12, 23), (17, 10), radius_x=27)
        self.add_arc('e9-4', (17, 10), (19, 15), radius_x=15, sweep=False)
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e1', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e2', 'e7', 'e3', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e4', 'e9-1', 'e9-2', 'e9-3', 'e9-4', closed=True)
