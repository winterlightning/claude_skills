"""Book close (content), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5a3d7973-ece6-5338-a408-973670de2b0b'
SOURCE_PATH = 'icons-json/content/book close_5a3d7973-ece6-5338-a408-973670de2b0b.json'
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
        self.add_line('e0', (12, 44), (40, 44))
        self.add_line('e1', (40, 36), (12, 36))
        self.add_line('e2', (40, 35), (40, 4))
        self.add_line('e3', (40, 4), (13, 4))
        self.add_line('e4', (8, 8), (8, 38))
        self.add_bezier('e5', (8, 38), ((8, 38.845), (8, 39.336), (8, 40.182)), ((8, 42.1), (9.57, 43.991), (11.76, 43.991)), ((11.84, 43.991), (11.92, 44), (12, 44)))
        self.add_bezier('e6', (12, 36), ((10.37, 36), (9.09, 37), (8, 38)))
        self.add_bezier('e7', (40, 44), ((39.22, 42.218), (38.89, 40.436), (39.24, 38.5)), ((39.38, 37.691), (40, 36.564), (40, 35.818)), ((40, 35.518), (40, 35.3), (40, 35)))
        self.add_bezier('e8', (13, 4), ((12.88, 4), (12.75, 4), (12.63, 4)), ((10.52, 4), (8, 5.882), (8, 8)))
        self.add_contour('c0', 'e5', 'e0')
        self.add_contour('c1', 'e1', 'e6')
        self.add_contour('c2', 'e7', 'e2', 'e3', 'e8', 'e4')
        self.relate('connect', 'c1', 'c2')
