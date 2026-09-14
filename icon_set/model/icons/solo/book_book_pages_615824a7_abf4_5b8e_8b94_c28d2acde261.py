"""Book book pages (content), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '615824a7-abf4-5b8e-8b94-c28d2acde261'
SOURCE_PATH = 'icons-json/content/book book pages_615824a7-abf4-5b8e-8b94-c28d2acde261.json'
AUTHOR = 'json_to_solo'

class BookBookPages(Solo48):
    icon_id = 'book-book-pages'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'pages', 'content')

    def build(self):
        self.add_line('e0', (24, 40), (24, 13))
        self.add_line('e1', (44, 11), (44, 34))
        self.add_line('e2', (42, 36), (30, 37))
        self.add_line('e3', (16, 37), (7, 36))
        self.add_line('e4', (4, 33), (4, 11))
        self.add_arc('e5-1', (24, 13), (31, 9), radius_x=12)
        self.add_line('e5-2', (31, 9), (42, 8))
        self.add_arc('e5-3', (42, 8), (44, 10), radius_x=2)
        self.add_arc('e5-4', (44, 10), (44, 11), radius_x=23, sweep=False)
        self.add_arc('e6', (44, 34), (42, 36), radius_x=3)
        self.add_line('e7', (30, 37), (24, 40))
        self.add_arc('e8', (24, 40), (16, 37), radius_x=17, sweep=False)
        self.add_arc('e9-1', (7, 36), (4, 34), radius_x=3)
        self.add_line('e9-2', (4, 34), (4, 33))
        self.add_line('e10-1', (4, 11), (4, 10))
        self.add_arc('e10-2', (4, 10), (5, 9), radius_x=1)
        self.add_line('e10-3', (5, 9), (10, 8))
        self.add_arc('e10-4', (10, 8), (24, 13), radius_x=23)
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e1', 'e6', 'e2', 'e7', closed=True)
        self.add_contour('c1', 'e8', 'e3', 'e9-1', 'e9-2', 'e4', 'e10-1', 'e10-2', 'e10-3', 'e10-4')
