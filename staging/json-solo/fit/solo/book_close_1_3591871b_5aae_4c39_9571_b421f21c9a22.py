"""Book close 1 (content), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3591871b-5aae-4c39-9571-b421f21c9a22'
SOURCE_PATH = 'icons-json/content/book close 1_3591871b-5aae-4c39-9571-b421f21c9a22.json'
AUTHOR = 'json_to_solo'

class BookClose1Content(Solo48):
    icon_id = 'book-close-1-content'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'close', 'content')

    def build(self):
        self.add_line('e0', (8, 36), (10, 34))
        self.add_line('e1', (12, 33), (40, 33))
        self.add_line('e2', (40, 35), (40, 4))
        self.add_line('e3', (40, 4), (12, 4))
        self.add_line('e4', (8, 7), (8, 39))
        self.add_line('e5', (11, 44), (40, 44))
        self.add_arc('e6', (10, 34), (12, 33), radius_x=5)
        self.add_arc('e7', (40, 44), (40, 35), radius_x=9)
        self.add_arc('e8', (12, 4), (8, 7), radius_x=5, sweep=False)
        self.add_line('e9-1', (8, 39), (8, 40))
        self.add_arc('e9-2', (8, 40), (11, 44), radius_x=5, sweep=False)
        self.add_contour('c0', 'e0', 'e6', 'e1')
        self.add_contour('c1', 'e7', 'e2', 'e3', 'e8', 'e4', 'e9-1', 'e9-2', 'e5', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
