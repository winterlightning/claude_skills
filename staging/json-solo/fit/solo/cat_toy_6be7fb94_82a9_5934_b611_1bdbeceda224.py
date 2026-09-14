"""Cat toy (pets), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6be7fb94-82a9-5934-b611-1bdbeceda224'
SOURCE_PATH = 'icons-json/pets/cat toy_6be7fb94-82a9-5934-b611-1bdbeceda224.json'
AUTHOR = 'json_to_solo'

class CatToyPets(Solo48):
    icon_id = 'cat-toy-pets'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('cat', 'toy', 'pets')

    def build(self):
        self.add_line('e0', (34, 35), (25, 35))
        self.add_line('e1', (25, 44), (28, 44))
        self.add_arc('e2-top', (8, 14), (26, 14), radius_x=9, radius_y=10)
        self.add_arc('e2-bottom', (26, 14), (8, 14), radius_x=9, radius_y=10)
        self.add_line('e3-1', (26, 19), (29, 23))
        self.add_line('e3-2', (29, 23), (38, 26))
        self.add_arc('e3-3', (38, 26), (40, 30), radius_x=5)
        self.add_arc('e3-4', (40, 30), (34, 35), radius_x=6)
        self.add_arc('e4-1', (25, 35), (20, 39), radius_x=4, sweep=False)
        self.add_arc('e4-2', (20, 39), (24, 44), radius_x=6, sweep=False)
        self.add_line('e4-3', (24, 44), (25, 44))
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
        self.relate('connect', 'c0', 'e2')
