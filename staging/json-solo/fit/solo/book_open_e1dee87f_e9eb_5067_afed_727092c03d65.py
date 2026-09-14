"""Book open (content), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e1dee87f-e9eb-5067-afed-727092c03d65'
SOURCE_PATH = 'icons-json/content/book open_e1dee87f-e9eb-5067-afed-727092c03d65.json'
AUTHOR = 'json_to_solo'

class BookOpen(Solo48):
    icon_id = 'book-open'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'open', 'content')

    def build(self):
        self.add_line('e0', (4, 10), (4, 34))
        self.add_line('e1', (7, 35), (10, 35))
        self.add_line('e2', (24, 14), (24, 40))
        self.add_line('e3', (44, 10), (44, 34))
        self.add_arc('e4-1', (24, 14), (11, 8), radius_x=18, sweep=False)
        self.add_arc('e4-2', (11, 8), (5, 9), radius_x=45, sweep=False)
        self.add_arc('e4-3', (5, 9), (4, 10), radius_x=1, sweep=False)
        self.add_arc('e5', (4, 34), (7, 35), radius_x=3, sweep=False)
        self.add_arc('e6', (10, 35), (24, 40), radius_x=18)
        self.add_arc('e7-1', (24, 14), (29, 10), radius_x=13)
        self.add_line('e7-2', (29, 10), (40, 8))
        self.add_line('e7-3', (40, 8), (43, 8))
        self.add_line('e7-4', (43, 8), (44, 10))
        self.add_arc('e8-1', (44, 34), (43, 35), radius_x=1)
        self.add_line('e8-2', (43, 35), (32, 36))
        self.add_arc('e8-3', (32, 36), (24, 40), radius_x=15, sweep=False)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e0', 'e5', 'e1', 'e6')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e3', 'e8-1', 'e8-2', 'e8-3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
