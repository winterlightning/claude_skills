"""Book open (content), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b5768591-30d0-458a-8f42-f8fa19890c4e'
SOURCE_PATH = 'icons-json/content/book open_b5768591-30d0-458a-8f42-f8fa19890c4e.json'
AUTHOR = 'json_to_solo'

class BookOpenB5768591(Solo48):
    icon_id = 'book-open-b5768591'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'open', 'content')

    def build(self):
        self.add_line('e0', (4, 11), (4, 33))
        self.add_line('e1', (7, 36), (16, 37))
        self.add_line('e2', (44, 11), (44, 29))
        self.add_line('e3', (42, 36), (30, 37))
        self.add_arc('e4-1', (24, 13), (10, 8), radius_x=23, sweep=False)
        self.add_line('e4-2', (10, 8), (5, 9))
        self.add_arc('e4-3', (5, 9), (4, 10), radius_x=1, sweep=False)
        self.add_line('e4-4', (4, 10), (4, 11))
        self.add_arc('e5', (4, 33), (7, 36), radius_x=3, sweep=False)
        self.add_arc('e6', (16, 37), (24, 40), radius_x=17)
        self.add_arc('e7-1', (24, 13), (31, 9), radius_x=11)
        self.add_arc('e7-2', (31, 9), (42, 8), radius_x=74)
        self.add_arc('e7-3', (42, 8), (44, 10), radius_x=2)
        self.add_line('e7-4', (44, 10), (44, 11))
        self.add_line('e8-1', (44, 29), (44, 34))
        self.add_line('e8-2', (44, 34), (42, 36))
        self.add_line('e9', (30, 37), (24, 40))
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e0', 'e5', 'e1', 'e6')
        self.add_contour('c1', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e2', 'e8-1', 'e8-2', 'e3', 'e9')
