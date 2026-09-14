"""Fish bowl (pets), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a12a46a8-8ec0-50ee-9332-2e08aade7d73'
SOURCE_PATH = 'icons-json/pets/fish bowl_a12a46a8-8ec0-50ee-9332-2e08aade7d73.json'
AUTHOR = 'json_to_solo'

class FishBowlPets(Solo48):
    icon_id = 'fish-bowl-pets'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('fish', 'bowl', 'pets')

    def build(self):
        self.add_line('e0', (44, 16), (4, 16))
        self.add_line('e1', (18, 25), (20, 28))
        self.add_line('e2', (19, 28), (18, 30))
        self.add_line('e3', (7, 8), (41, 8))
        self.add_arc('e4-1', (20, 28), (28, 25), radius_x=7)
        self.add_arc('e4-2', (28, 25), (32, 28), radius_x=10)
        self.add_arc('e4-3', (32, 28), (27, 31), radius_x=9)
        self.add_arc('e4-4', (27, 31), (19, 28), radius_x=9)
        self.add_arc('e5-1', (41, 8), (43, 10), radius_x=2)
        self.add_arc('e5-2', (43, 10), (44, 16), radius_x=26)
        self.add_line('e5-3', (44, 16), (43, 25))
        self.add_arc('e5-4', (43, 25), (25, 40), radius_x=20)
        self.add_arc('e5-5', (25, 40), (4, 19), radius_x=21)
        self.add_line('e5-6', (4, 19), (4, 15))
        self.add_arc('e5-7', (4, 15), (7, 8), radius_x=22)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e2')
        self.add_contour('c2', 'e3', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
