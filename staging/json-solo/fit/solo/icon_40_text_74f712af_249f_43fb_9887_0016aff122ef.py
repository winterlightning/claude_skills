"""40 (text) (text), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '74f712af-249f-43fb-9887-0016aff122ef'
SOURCE_PATH = 'icons-json/text/40 (text)_74f712af-249f-43fb-9887-0016aff122ef.json'
AUTHOR = 'json_to_solo'

class Icon40TextText(Solo48):
    icon_id = 'icon-40-text-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'text'
    aliases = ()
    keywords = ('text',)

    def build(self):
        self.add_line('e0', (19, 33), (4, 33))
        self.add_line('e1', (4, 33), (16, 8))
        self.add_line('e2', (16, 8), (16, 40))
        self.add_arc('e3-1', (28, 24), (36, 8), radius_x=13)
        self.add_arc('e3-2', (36, 8), (40, 10), radius_x=5)
        self.add_arc('e3-3', (40, 10), (43, 16), radius_x=16)
        self.add_line('e3-4', (43, 16), (44, 24))
        self.add_line('e3-5', (44, 24), (43, 32))
        self.add_arc('e3-6', (43, 32), (41, 37), radius_x=17)
        self.add_arc('e3-7', (41, 37), (36, 40), radius_x=6)
        self.add_arc('e3-8', (36, 40), (28, 24), radius_x=13)
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8', closed=True)
