"""Book open (content), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '03b427a0-f791-44b1-9798-ea43bb973886'
SOURCE_PATH = 'icons-json/content/book open_03b427a0-f791-44b1-9798-ea43bb973886.json'
AUTHOR = 'json_to_solo'

class BookOpen03b427a0(Solo48):
    icon_id = 'book-open-03b427a0'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'open', 'content')

    def build(self):
        self.add_line('e0', (44, 11), (44, 37))
        self.add_line('e1', (24, 12), (24, 40))
        self.add_line('e2', (4, 11), (4, 37))
        self.add_arc('e3-1', (24, 12), (35, 8), radius_x=22)
        self.add_line('e3-2', (35, 8), (38, 8))
        self.add_arc('e3-3', (38, 8), (42, 9), radius_x=9)
        self.add_arc('e3-4', (42, 9), (44, 11), radius_x=2)
        self.add_arc('e4', (44, 37), (24, 40), radius_x=21, sweep=False)
        self.add_arc('e5-1', (24, 12), (18, 9), radius_x=35, sweep=False)
        self.add_line('e5-2', (18, 9), (11, 8))
        self.add_arc('e5-3', (11, 8), (6, 9), radius_x=17, sweep=False)
        self.add_arc('e5-4', (6, 9), (4, 11), radius_x=2, sweep=False)
        self.add_arc('e6', (4, 37), (24, 40), radius_x=22)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e0', 'e4')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e2', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
