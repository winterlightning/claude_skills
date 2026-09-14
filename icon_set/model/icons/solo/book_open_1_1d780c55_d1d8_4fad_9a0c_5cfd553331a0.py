"""Book open 1 (content), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1d780c55-d1d8-4fad-9a0c-5cfd553331a0'
SOURCE_PATH = 'icons-json/content/book open 1_1d780c55-d1d8-4fad-9a0c-5cfd553331a0.json'
AUTHOR = 'json_to_solo'

class BookOpen1(Solo48):
    icon_id = 'book-open-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'open', 'content')

    def build(self):
        self.add_line('e0', (6, 8), (6, 35))
        self.add_line('e1', (8, 38), (17, 39))
        self.add_line('e2', (42, 8), (42, 35))
        self.add_line('e3', (40, 38), (31, 39))
        self.add_arc('e4-1', (24, 10), (21, 7), radius_x=7, sweep=False)
        self.add_line('e4-2', (21, 7), (13, 6))
        self.add_arc('e4-3', (13, 6), (9, 6), radius_x=55)
        self.add_arc('e4-4', (9, 6), (8, 6), radius_x=14)
        self.add_arc('e4-5', (8, 6), (6, 8), radius_x=2, sweep=False)
        self.add_line('e5', (6, 35), (8, 38))
        self.add_arc('e6', (17, 39), (24, 42), radius_x=13)
        self.add_arc('e7-1', (24, 10), (27, 7), radius_x=7)
        self.add_line('e7-2', (27, 7), (35, 6))
        self.add_line('e7-3', (35, 6), (39, 6))
        self.add_arc('e7-4', (39, 6), (40, 6), radius_x=14, sweep=False)
        self.add_arc('e7-5', (40, 6), (42, 8), radius_x=2)
        self.add_line('e8', (42, 35), (40, 38))
        self.add_arc('e9', (31, 39), (24, 42), radius_x=13, sweep=False)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e0', 'e5', 'e1', 'e6')
        self.add_contour('c1', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e7-5', 'e2', 'e8', 'e3', 'e9')
