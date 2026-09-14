"""Book close 2 (content), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7025f460-1d25-427d-b645-3853db39a1d0'
SOURCE_PATH = 'icons-json/content/book close 2_7025f460-1d25-427d-b645-3853db39a1d0.json'
AUTHOR = 'json_to_solo'

class BookClose2Content(Solo48):
    icon_id = 'book-close-2-content'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'close', 'content')

    def build(self):
        self.add_line('e0', (6, 13), (9, 15))
        self.add_line('e1', (11, 15), (42, 15))
        self.add_line('e2', (42, 6), (42, 37))
        self.add_line('e3', (36, 42), (13, 42))
        self.add_line('e4', (6, 32), (6, 12))
        self.add_line('e5', (13, 6), (42, 6))
        self.add_bezier('e6', (9, 15), ((9.458, 15.229), (10.525, 15), (11, 15)))
        self.add_bezier('e7', (42, 37), ((41.992, 37.123), (41.992, 37.336), (41.984, 37.451)), ((41.984, 39.447), (40.871, 41.403), (38.85, 41.902)), ((38.285, 42), (37.598, 41.992), (37.025, 42)), ((36.772, 42), (36.254, 42), (36, 42)))
        self.add_bezier('e8', (13, 42), ((12.861, 42), (13.094, 41.992), (12.955, 41.992)), ((9.69, 41.992), (6.998, 39.333), (6.18, 36.305)), ((6, 35.536), (6.008, 34.62), (6.008, 33.843)), ((6.008, 33.417), (6, 32.992), (6, 32.566)), ((6, 32.435), (6, 32.131), (6, 32)))
        self.add_bezier('e9', (6, 12), ((6, 11.73), (6.016, 11.187), (6.016, 10.917)), ((6.016, 7.775), (8.667, 6.016), (11.58, 6.016)), ((11.899, 6.016), (12.681, 6), (13, 6)))
        self.add_contour('c0', 'e0', 'e6', 'e1')
        self.add_contour('c1', 'e2', 'e7', 'e3', 'e8', 'e4', 'e9', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
