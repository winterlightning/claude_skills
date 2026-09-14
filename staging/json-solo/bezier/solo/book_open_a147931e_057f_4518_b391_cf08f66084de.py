"""Book open (content), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a147931e-057f-4518-b391-cf08f66084de'
SOURCE_PATH = 'icons-json/content/book open_a147931e-057f-4518-b391-cf08f66084de.json'
AUTHOR = 'json_to_solo'

class BookOpen(Solo48):
    icon_id = 'book-open'
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
        self.add_bezier('e5', (4, 8), ((6.182, 8), (8.355, 8), (10.536, 8)), ((11.364, 8), (12.3, 8.303), (13.091, 8.497)), ((17.436, 9.566), (20.9, 12.027), (24, 15)))
        self.add_bezier('e6', (20, 37), ((17.673, 35.383), (12.918, 34), (10, 34)))
        self.add_bezier('e7', (24, 15), ((27.491, 11.488), (31.2, 9.162), (36.309, 8.379)), ((37.145, 8.253), (38.018, 8.017), (38.873, 8.017)), ((39.018, 8.008), (39.164, 8.008), (39.309, 8)), ((39.455, 8), (39.6, 8.008), (39.745, 8.008)), ((41.064, 8.008), (42.736, 8.655), (44, 9)))
        self.add_bezier('e8', (44, 34), ((36.282, 33.234), (29.745, 35.133), (24, 40)))
        self.add_contour('c0', 'e5', 'e0', 'e1', 'e6', 'e2', 'e3')
        self.add_contour('c1', 'e7', 'e4', 'e8')
