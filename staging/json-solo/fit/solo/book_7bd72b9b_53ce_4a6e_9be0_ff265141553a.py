"""Book (content), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7bd72b9b-53ce-4a6e-9be0-ff265141553a'
SOURCE_PATH = 'icons-json/content/book_7bd72b9b-53ce-4a6e-9be0-ff265141553a.json'
AUTHOR = 'json_to_solo'

class Book7bd72b9b(Solo48):
    icon_id = 'book-7bd72b9b'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'content')

    def build(self):
        self.add_line('e0', (8, 12), (10, 14))
        self.add_line('e1', (12, 15), (40, 15))
        self.add_line('e2', (40, 13), (40, 44))
        self.add_line('e3', (40, 44), (12, 44))
        self.add_line('e4', (8, 41), (8, 9))
        self.add_line('e5', (11, 4), (40, 4))
        self.add_arc('e6', (10, 14), (12, 15), radius_x=5, sweep=False)
        self.add_arc('e7', (40, 4), (40, 13), radius_x=9, sweep=False)
        self.add_arc('e8', (12, 44), (8, 41), radius_x=5)
        self.add_line('e9-1', (8, 9), (8, 8))
        self.add_arc('e9-2', (8, 8), (11, 4), radius_x=5)
        self.add_contour('c0', 'e0', 'e6', 'e1')
        self.add_contour('c1', 'e7', 'e2', 'e3', 'e8', 'e4', 'e9-1', 'e9-2', 'e5', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
