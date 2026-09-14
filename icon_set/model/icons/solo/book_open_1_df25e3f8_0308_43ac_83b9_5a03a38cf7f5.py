"""Book open 1 (content), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'df25e3f8-0308-43ac-83b9-5a03a38cf7f5'
SOURCE_PATH = 'icons-json/content/book open 1_df25e3f8-0308-43ac-83b9-5a03a38cf7f5.json'
AUTHOR = 'json_to_solo'

class BookOpen1Df25e3f8(Solo48):
    icon_id = 'book-open-1-df25e3f8'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'open', 'content')

    def build(self):
        self.add_line('e0', (24, 40), (44, 31))
        self.add_line('e1', (44, 31), (44, 8))
        self.add_line('e2', (44, 8), (24, 17))
        self.add_line('e3', (24, 17), (4, 8))
        self.add_line('e4', (4, 8), (4, 31))
        self.add_line('e5', (4, 31), (24, 40))
        self.add_line('e6', (24, 40), (24, 17))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6')
