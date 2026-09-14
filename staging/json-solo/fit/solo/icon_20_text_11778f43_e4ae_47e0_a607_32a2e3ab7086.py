"""20 (text) (other), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '11778f43-e4ae-47e0-a607-32a2e3ab7086'
SOURCE_PATH = 'icons-json/other/20 (text)_11778f43-e4ae-47e0-a607-32a2e3ab7086.json'
AUTHOR = 'json_to_solo'

class Icon20TextOther(Solo48):
    icon_id = 'icon-20-text-other'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('text', 'other')

    def build(self):
        self.add_line('e0', (15, 24), (4, 40))
        self.add_line('e1', (4, 40), (18, 40))
        self.add_arc('e2-1', (5, 14), (12, 8), radius_x=8)
        self.add_arc('e2-2', (12, 8), (15, 24), radius_x=10)
        self.add_arc('e3-1', (28, 24), (30, 12), radius_x=29)
        self.add_arc('e3-2', (30, 12), (34, 8), radius_x=7)
        self.add_line('e3-3', (34, 8), (36, 8))
        self.add_arc('e3-4', (36, 8), (43, 16), radius_x=9)
        self.add_line('e3-5', (43, 16), (44, 24))
        self.add_line('e3-6', (44, 24), (43, 32))
        self.add_arc('e3-7', (43, 32), (41, 37), radius_x=17)
        self.add_arc('e3-8', (41, 37), (36, 40), radius_x=6)
        self.add_arc('e3-9', (36, 40), (28, 24), radius_x=13)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e0', 'e1')
        self.add_contour('c1', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8', 'e3-9', closed=True)
