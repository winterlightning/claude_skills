"""Book close (content), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3b4996c8-c930-4df3-8c39-a94d12e8e2d2'
SOURCE_PATH = 'icons-json/content/book close_3b4996c8-c930-4df3-8c39-a94d12e8e2d2.json'
AUTHOR = 'json_to_solo'

class BookCloseContent(Solo48):
    icon_id = 'book-close-content'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'close', 'content')

    def build(self):
        self.add_line('e0', (8, 9), (8, 41))
        self.add_line('e1', (13, 44), (39, 44))
        self.add_line('e2', (40, 43), (40, 15))
        self.add_line('e3', (40, 15), (9, 15))
        self.add_line('e4', (8, 14), (8, 4))
        self.add_line('e5', (9, 4), (39, 4))
        self.add_line('e6', (40, 5), (40, 15))
        self.add_line('e7-1', (8, 41), (8, 42))
        self.add_arc('e7-2', (8, 42), (10, 44), radius_x=3, sweep=False)
        self.add_line('e7-3', (10, 44), (13, 44))
        self.add_arc('e8', (39, 44), (40, 43), radius_x=1, sweep=False)
        self.add_arc('e9', (9, 15), (8, 14), radius_x=1)
        self.add_arc('e10', (8, 4), (9, 4), radius_x=11, sweep=False)
        self.add_arc('e11', (39, 4), (40, 5), radius_x=1)
        self.add_contour('c0', 'e0', 'e7-1', 'e7-2', 'e7-3', 'e1', 'e8', 'e2')
        self.add_contour('c1', 'e3', 'e9', 'e4', 'e10', 'e5', 'e11', 'e6', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c0')
