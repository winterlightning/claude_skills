"""50 (text) (text), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4fe09bc5-d901-46d3-b7df-29f4ed696a4a'
SOURCE_PATH = 'icons-json/text/50 (text)_4fe09bc5-d901-46d3-b7df-29f4ed696a4a.json'
AUTHOR = 'json_to_solo'

class Icon50TextText(Solo48):
    icon_id = 'icon-50-text-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'text'
    aliases = ()
    keywords = ('text',)

    def build(self):
        self.add_line('e0', (17, 8), (6, 8))
        self.add_line('e1', (6, 8), (5, 23))
        self.add_arc('e2-1', (5, 23), (17, 25), radius_x=7)
        self.add_arc('e2-2', (17, 25), (11, 40), radius_x=11)
        self.add_line('e2-3', (11, 40), (7, 39))
        self.add_arc('e2-4', (7, 39), (4, 35), radius_x=5)
        self.add_arc('e3-1', (28, 24), (30, 12), radius_x=29)
        self.add_arc('e3-2', (30, 12), (34, 8), radius_x=7)
        self.add_line('e3-3', (34, 8), (36, 8))
        self.add_arc('e3-4', (36, 8), (43, 16), radius_x=9)
        self.add_line('e3-5', (43, 16), (44, 24))
        self.add_line('e3-6', (44, 24), (43, 32))
        self.add_arc('e3-7', (43, 32), (41, 37), radius_x=17)
        self.add_arc('e3-8', (41, 37), (36, 40), radius_x=6)
        self.add_arc('e3-9', (36, 40), (28, 24), radius_x=13)
        self.add_contour('c0', 'e0', 'e1', 'e2-1', 'e2-2', 'e2-3', 'e2-4')
        self.add_contour('c1', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8', 'e3-9', closed=True)
