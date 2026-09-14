"""Book close (content), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '129c70c9-d37d-4bff-948b-1a1e0fdad1a1'
SOURCE_PATH = 'icons-json/content/book close_129c70c9-d37d-4bff-948b-1a1e0fdad1a1.json'
AUTHOR = 'json_to_solo'

class BookClose129c70c9(Solo48):
    icon_id = 'book-close-129c70c9'
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
        self.add_bezier('e6', (10, 34), ((10.54, 33.682), (11.32, 33), (12, 33)))
        self.add_bezier('e7', (40, 44), ((40, 43.745), (39.99, 43.491), (39.99, 43.236)), ((39.99, 42.982), (39.48, 42.618), (39.39, 42.336)), ((39.11, 41.5), (39.07, 40.618), (39.04, 39.755)), ((39.01, 38.864), (39.11, 37.736), (39.43, 36.9)), ((39.68, 36.245), (40, 35.718), (40, 35)))
        self.add_bezier('e8', (12, 4), ((11.96, 4), (11.92, 4), (11.88, 4)), ((10.56, 4), (9.06, 5.1), (8.34, 6)), ((8.16, 6.236), (8.13, 6.764), (8, 7)))
        self.add_bezier('e9', (8, 39), ((8, 39.127), (8, 39.709), (8, 39.827)), ((8, 41.236), (8.99, 43.236), (10.45, 43.864)), ((10.63, 43.945), (10.82, 43.927), (11, 44)))
        self.add_contour('c0', 'e0', 'e6', 'e1')
        self.add_contour('c1', 'e7', 'e2', 'e3', 'e8', 'e4', 'e9', 'e5', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
