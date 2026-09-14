"""Fire (fire), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd57b67f9-c8ed-433b-aa42-f2f21b118e83'
SOURCE_PATH = 'icons-json/fire/fire_d57b67f9-c8ed-433b-aa42-f2f21b118e83.json'
AUTHOR = 'json_to_solo'

class FireFire(Solo48):
    icon_id = 'fire-fire'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'fire'
    aliases = ()
    keywords = ('fire',)

    def build(self):
        self.add_line('e0', (12, 22), (16, 17))
        self.add_arc('e1-1', (16, 17), (20, 4), radius_x=16, sweep=False)
        self.add_arc('e1-2', (20, 4), (28, 11), radius_x=26)
        self.add_arc('e1-3', (28, 11), (30, 25), radius_x=15)
        self.add_line('e1-4', (30, 25), (32, 24))
        self.add_arc('e1-5', (32, 24), (37, 19), radius_x=16, sweep=False)
        self.add_arc('e1-6', (37, 19), (40, 29), radius_x=20)
        self.add_arc('e1-7', (40, 29), (40, 31), radius_x=26, sweep=False)
        self.add_arc('e1-8', (40, 31), (36, 39), radius_x=14)
        self.add_arc('e1-9', (36, 39), (24, 44), radius_x=17)
        self.add_line('e1-10', (24, 44), (15, 42))
        self.add_arc('e1-11', (15, 42), (9, 36), radius_x=15)
        self.add_line('e1-12', (9, 36), (8, 31))
        self.add_arc('e1-13', (8, 31), (12, 22), radius_x=14)
        self.add_contour('c0', 'e0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e1-9', 'e1-10', 'e1-11', 'e1-12', 'e1-13', closed=True)
