"""Book close (content), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5a3d7973-ece6-5338-a408-973670de2b0b'
SOURCE_PATH = 'icons-json/content/book close_5a3d7973-ece6-5338-a408-973670de2b0b.json'
AUTHOR = 'json_to_solo'

class BookClose5a3d7973(Solo48):
    icon_id = 'book-close-5a3d7973'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'close', 'content')

    def build(self):
        self.add_line('e0', (12, 44), (40, 44))
        self.add_line('e1', (40, 36), (12, 36))
        self.add_line('e2', (40, 35), (40, 4))
        self.add_line('e3', (40, 4), (13, 4))
        self.add_line('e4', (8, 8), (8, 38))
        self.add_line('e5-1', (8, 38), (8, 41))
        self.add_line('e5-2', (8, 41), (9, 43))
        self.add_line('e5-3', (9, 43), (12, 44))
        self.add_arc('e6', (12, 36), (8, 38), radius_x=5, sweep=False)
        self.add_arc('e7-1', (40, 44), (40, 36), radius_x=9)
        self.add_line('e7-2', (40, 36), (40, 35))
        self.add_arc('e8-1', (13, 4), (10, 5), radius_x=5, sweep=False)
        self.add_arc('e8-2', (10, 5), (8, 8), radius_x=4, sweep=False)
        self.add_contour('c0', 'e5-1', 'e5-2', 'e5-3', 'e0')
        self.add_contour('c1', 'e1', 'e6')
        self.add_contour('c2', 'e7-1', 'e7-2', 'e2', 'e3', 'e8-1', 'e8-2', 'e4')
        self.relate('connect', 'c1', 'c2')
