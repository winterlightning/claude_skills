"""Book close 2 (content), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7025f460-1d25-427d-b645-3853db39a1d0'
SOURCE_PATH = 'icons-json/content/book close 2_7025f460-1d25-427d-b645-3853db39a1d0.json'
AUTHOR = 'json_to_solo'

class BookClose2Content(Solo48):
    icon_id = 'book-close-2-content'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'close', 'content')

    def build(self):
        self.add_line('e0', (6, 13), (9, 15))
        self.add_line('e1', (11, 15), (42, 15))
        self.add_line('e2', (42, 6), (42, 37))
        self.add_line('e3', (36, 42), (13, 42))
        self.add_line('e4', (6, 32), (6, 12))
        self.add_line('e5', (13, 6), (42, 6))
        self.add_line('e6', (9, 15), (11, 15))
        self.add_arc('e7-1', (42, 37), (37, 42), radius_x=5)
        self.add_line('e7-2', (37, 42), (36, 42))
        self.add_arc('e8-1', (13, 42), (7, 38), radius_x=7)
        self.add_line('e8-2', (7, 38), (6, 33))
        self.add_line('e8-3', (6, 33), (6, 32))
        self.add_line('e9-1', (6, 12), (7, 8))
        self.add_arc('e9-2', (7, 8), (8, 7), radius_x=5)
        self.add_line('e9-3', (8, 7), (13, 6))
        self.add_contour('c0', 'e0', 'e6', 'e1')
        self.add_contour('c1', 'e2', 'e7-1', 'e7-2', 'e3', 'e8-1', 'e8-2', 'e8-3', 'e4', 'e9-1', 'e9-2', 'e9-3', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
