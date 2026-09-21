"""32 (text) (text), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1caf07ae-b765-4e87-8322-6a4c81ec96e2'
SOURCE_PATH = 'icons-json/text/32 (text)_1caf07ae-b765-4e87-8322-6a4c81ec96e2.json'
AUTHOR = 'json_to_solo'

class Icon32Text(Solo48):
    icon_id = 'icon-32-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'text'
    aliases = ()
    keywords = ('text',)

    def build(self):
        self.add_line('e0', (41, 24), (29, 40))
        self.add_line('e1', (29, 40), (44, 40))
        self.add_arc('e2-1', (5, 13), (8, 9), radius_x=7)
        self.add_line('e2-2', (8, 9), (12, 8))
        self.add_arc('e2-3', (12, 8), (18, 16), radius_x=7)
        self.add_arc('e2-4', (18, 16), (11, 24), radius_x=7)
        self.add_arc('e2-5', (11, 24), (18, 35), radius_x=8)
        self.add_arc('e2-6', (18, 35), (15, 39), radius_x=9)
        self.add_line('e2-7', (15, 39), (11, 40))
        self.add_arc('e2-8', (11, 40), (4, 34), radius_x=8)
        self.add_arc('e3-1', (29, 14), (37, 8), radius_x=10)
        self.add_arc('e3-2', (37, 8), (40, 9), radius_x=5)
        self.add_arc('e3-3', (40, 9), (44, 16), radius_x=9)
        self.add_arc('e3-4', (44, 16), (41, 24), radius_x=13)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e2-8')
        self.add_contour('c1', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e0', 'e1')
