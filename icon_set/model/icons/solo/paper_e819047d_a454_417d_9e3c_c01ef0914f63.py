"""Paper (content), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e819047d-a454-417d-9e3c-c01ef0914f63'
SOURCE_PATH = 'icons-json/content/paper_e819047d-a454-417d-9e3c-c01ef0914f63.json'
AUTHOR = 'json_to_solo'

class PaperContent(Solo48):
    icon_id = 'paper-content'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('paper', 'content')

    def build(self):
        self.add_line('e0', (15, 35), (33, 35))
        self.add_line('e1', (15, 26), (28, 26))
        self.add_line('e2', (15, 15), (24, 15))
        self.add_line('e3', (40, 16), (40, 42))
        self.add_line('e4', (38, 44), (10, 44))
        self.add_line('e5', (8, 42), (8, 6))
        self.add_line('e6', (11, 4), (28, 4))
        self.add_line('e7', (29, 5), (40, 16))
        self.add_arc('e8', (40, 42), (38, 44), radius_x=2)
        self.add_arc('e9', (10, 44), (8, 42), radius_x=2)
        self.add_line('e10', (8, 6), (11, 4))
        self.add_arc('e11', (28, 4), (29, 5), radius_x=22, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e8', 'e4', 'e9', 'e5', 'e10', 'e6', 'e11', 'e7', closed=True)
