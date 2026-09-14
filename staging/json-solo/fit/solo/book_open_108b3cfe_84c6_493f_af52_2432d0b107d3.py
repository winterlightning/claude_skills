"""Book open (content), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '108b3cfe-84c6-493f-af52-2432d0b107d3'
SOURCE_PATH = 'icons-json/content/book open_108b3cfe-84c6-493f-af52-2432d0b107d3.json'
AUTHOR = 'json_to_solo'

class BookOpen108b3cfe(Solo48):
    icon_id = 'book-open-108b3cfe'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'open', 'content')

    def build(self):
        self.add_line('e0', (24, 13), (4, 8))
        self.add_line('e1', (4, 8), (4, 35))
        self.add_line('e2', (4, 35), (24, 40))
        self.add_line('e3', (24, 13), (24, 40))
        self.add_line('e4', (24, 13), (44, 8))
        self.add_line('e5', (44, 8), (44, 35))
        self.add_line('e6', (44, 35), (24, 40))
        self.add_line('e7', (11, 19), (18, 21))
        self.add_line('e8', (30, 21), (37, 19))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4', 'e5', 'e6')
        self.add_contour('c3', 'e7')
        self.add_contour('c4', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
