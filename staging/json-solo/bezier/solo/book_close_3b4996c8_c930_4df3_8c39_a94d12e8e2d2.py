"""Book close (content), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3b4996c8-c930-4df3-8c39-a94d12e8e2d2'
SOURCE_PATH = 'icons-json/content/book close_3b4996c8-c930-4df3-8c39-a94d12e8e2d2.json'
AUTHOR = 'json_to_solo'

class BookClose3b4996c8(Solo48):
    icon_id = 'book-close-3b4996c8'
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
        self.add_bezier('e7', (8, 41), ((8, 41.1), (8.008, 41.473), (8.008, 41.573)), ((8.008, 43.918), (10.4, 43.991), (11.949, 43.991)), ((12.312, 43.991), (12.629, 44), (13, 44)))
        self.add_bezier('e8', (39, 44), ((39.051, 43.991), (39.259, 43.991), (39.309, 43.982)), ((39.621, 43.982), (39.992, 43.591), (39.992, 43.255)), ((39.992, 43.2), (40, 43.055), (40, 43)))
        self.add_bezier('e9', (9, 15), ((8.688, 14.782), (8.177, 14.855), (8.034, 14.345)), ((8.017, 14.236), (8.008, 14.118), (8, 14)))
        self.add_bezier('e10', (8, 4), ((8.278, 4), (8.722, 4), (9, 4)))
        self.add_bezier('e11', (39, 4), ((39.051, 4), (39.259, 4.009), (39.309, 4.018)), ((39.621, 4.018), (39.992, 4.409), (39.992, 4.745)), ((39.992, 4.8), (40, 4.945), (40, 5)))
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8', 'e2')
        self.add_contour('c1', 'e3', 'e9', 'e4', 'e10', 'e5', 'e11', 'e6', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c0')
