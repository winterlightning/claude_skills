"""Book close (content), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '49781b64-ccc2-5e53-93f8-360efdda93fc'
SOURCE_PATH = 'icons-json/content/book close_49781b64-ccc2-5e53-93f8-360efdda93fc.json'
AUTHOR = 'json_to_solo'

class BookClose(Solo48):
    icon_id = 'book-close'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'close', 'content')

    def build(self):
        self.add_line('e0', (12, 44), (38, 44))
        self.add_line('e1', (40, 43), (40, 6))
        self.add_line('e2', (38, 4), (12, 4))
        self.add_line('e3', (8, 9), (8, 38))
        self.add_line('e4', (40, 35), (12, 35))
        self.add_line('e5-1', (8, 37), (8, 40))
        self.add_arc('e5-2', (8, 40), (12, 44), radius_x=5, sweep=False)
        self.add_line('e6', (38, 44), (40, 43))
        self.add_arc('e7', (40, 6), (38, 4), radius_x=2, sweep=False)
        self.add_arc('e8', (12, 4), (8, 9), radius_x=6, sweep=False)
        self.add_arc('e9', (12, 35), (8, 37), radius_x=5, sweep=False)
        self.add_contour('c0', 'e5-1', 'e5-2', 'e0', 'e6', 'e1', 'e7', 'e2', 'e8', 'e3')
        self.add_contour('c1', 'e4', 'e9')
        self.relate('connect', 'c1', 'c0')
