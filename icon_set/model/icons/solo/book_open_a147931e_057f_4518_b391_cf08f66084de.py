"""Book open (content), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a147931e-057f-4518-b391-cf08f66084de'
SOURCE_PATH = 'icons-json/content/book open_a147931e-057f-4518-b391-cf08f66084de.json'
AUTHOR = 'json_to_solo'

class BookOpenA147931e(Solo48):
    icon_id = 'book-open-a147931e'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'open', 'content')

    def build(self):
        self.add_line('e0', (24, 15), (24, 40))
        self.add_line('e1', (24, 40), (20, 37))
        self.add_line('e2', (10, 34), (4, 34))
        self.add_line('e3', (4, 34), (4, 8))
        self.add_line('e4', (44, 9), (44, 34))
        self.add_line('e5-1', (4, 8), (15, 9))
        self.add_arc('e5-2', (15, 9), (24, 15), radius_x=24)
        self.add_line('e6', (20, 37), (10, 34))
        self.add_arc('e7-1', (24, 15), (39, 8), radius_x=23)
        self.add_arc('e7-2', (39, 8), (44, 9), radius_x=14)
        self.add_arc('e8', (44, 34), (24, 40), radius_x=26, sweep=False)
        self.add_contour('c0', 'e5-1', 'e5-2', 'e0', 'e1', 'e6', 'e2', 'e3')
        self.add_contour('c1', 'e7-1', 'e7-2', 'e4', 'e8')
