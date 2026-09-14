"""Book close (content), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e5', (8, 37), ((8, 37.855), (8, 38.436), (8, 39.291)), ((8, 41.627), (9.693, 43.991), (12, 43.991)), ((12.067, 43.991), (11.933, 44), (12, 44)))
        self.add_bezier('e6', (38, 44), ((38.438, 44), (39.368, 43.773), (39.714, 43.5)), ((39.857, 43.391), (39.865, 43.118), (40, 43)))
        self.add_bezier('e7', (40, 6), ((40, 5.9), (39.992, 5.627), (39.992, 5.527)), ((39.992, 4.791), (39.217, 4.018), (38.552, 4.018)), ((38.476, 4.009), (38.076, 4.009), (38, 4)))
        self.add_bezier('e8', (12, 4), ((10.004, 4), (8.017, 6.982), (8.017, 9.027)), ((8.008, 9.173), (8.008, 8.855), (8, 9)))
        self.add_bezier('e9', (12, 35), ((10.4, 35), (9.137, 35.864), (8, 37)))
        self.add_contour('c0', 'e5', 'e0', 'e6', 'e1', 'e7', 'e2', 'e8', 'e3')
        self.add_contour('c1', 'e4', 'e9')
        self.relate('connect', 'c1', 'c0')
