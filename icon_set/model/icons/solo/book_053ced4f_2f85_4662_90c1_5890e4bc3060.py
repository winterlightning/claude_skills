"""Book (content), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '053ced4f-2f85-4662-90c1-5890e4bc3060'
SOURCE_PATH = 'icons-json/content/book_053ced4f-2f85-4662-90c1-5890e4bc3060.json'
AUTHOR = 'json_to_solo'

class Book(Solo48):
    icon_id = 'book'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'content')

    def build(self):
        self.add_line('e0', (40, 15), (40, 43))
        self.add_line('e1', (39, 44), (13, 44))
        self.add_line('e2', (8, 41), (8, 11))
        self.add_line('e3', (40, 15), (14, 15))
        self.add_line('e4', (40, 15), (40, 5))
        self.add_line('e5', (39, 4), (11, 4))
        self.add_line('e6', (8, 9), (8, 11))
        self.add_arc('e7', (40, 43), (39, 44), radius_x=1)
        self.add_line('e8-1', (13, 44), (10, 44))
        self.add_arc('e8-2', (10, 44), (8, 42), radius_x=3)
        self.add_line('e8-3', (8, 42), (8, 41))
        self.add_arc('e9', (14, 15), (8, 11), radius_x=5)
        self.add_arc('e10', (40, 5), (39, 4), radius_x=1, sweep=False)
        self.add_line('e11-1', (11, 4), (9, 5))
        self.add_line('e11-2', (9, 5), (8, 9))
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8-1', 'e8-2', 'e8-3', 'e2')
        self.add_contour('c1', 'e3', 'e9')
        self.add_contour('c2', 'e4', 'e10', 'e5', 'e11-1', 'e11-2', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
