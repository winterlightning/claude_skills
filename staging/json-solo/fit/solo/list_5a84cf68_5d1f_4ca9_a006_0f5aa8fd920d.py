"""List (content), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5a84cf68-5d1f-4ca9-a006-0f5aa8fd920d'
SOURCE_PATH = 'icons-json/content/list_5a84cf68-5d1f-4ca9-a006-0f5aa8fd920d.json'
AUTHOR = 'json_to_solo'

class ListContent(Solo48):
    icon_id = 'list-content'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('list', 'content')

    def build(self):
        self.add_line('e0', (20, 8), (9, 20))
        self.add_line('e1', (9, 20), (4, 15))
        self.add_line('e2', (28, 17), (44, 17))
        self.add_line('e3', (20, 28), (9, 40))
        self.add_line('e4', (9, 40), (4, 35))
        self.add_line('e5', (28, 37), (44, 37))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e4')
        self.add_contour('c3', 'e5')
