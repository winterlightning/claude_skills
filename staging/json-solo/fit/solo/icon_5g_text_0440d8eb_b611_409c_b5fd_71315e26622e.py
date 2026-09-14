"""5g (text) (other), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0440d8eb-b611-409c-b5fd-71315e26622e'
SOURCE_PATH = 'icons-json/other/5g (text)_0440d8eb-b611-409c-b5fd-71315e26622e.json'
AUTHOR = 'json_to_solo'

class Icon5gTextOther(Solo48):
    icon_id = 'icon-5g-text-other'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('5g', 'text', 'other')

    def build(self):
        self.add_line('e0', (17, 8), (6, 8))
        self.add_line('e1', (6, 8), (5, 23))
        self.add_line('e2', (44, 33), (44, 25))
        self.add_line('e3', (44, 25), (37, 25))
        self.add_arc('e4-1', (5, 23), (16, 23), radius_x=6)
        self.add_arc('e4-2', (16, 23), (11, 40), radius_x=11)
        self.add_line('e4-3', (11, 40), (7, 39))
        self.add_arc('e4-4', (7, 39), (4, 35), radius_x=5)
        self.add_arc('e5-1', (43, 13), (40, 9), radius_x=7, sweep=False)
        self.add_arc('e5-2', (40, 9), (37, 8), radius_x=5, sweep=False)
        self.add_line('e5-3', (37, 8), (33, 9))
        self.add_arc('e5-4', (33, 9), (29, 13), radius_x=9, sweep=False)
        self.add_arc('e5-5', (29, 13), (28, 31), radius_x=40, sweep=False)
        self.add_arc('e5-6', (28, 31), (36, 40), radius_x=9, sweep=False)
        self.add_line('e5-7', (36, 40), (40, 39))
        self.add_arc('e5-8', (40, 39), (43, 36), radius_x=7, sweep=False)
        self.add_line('e5-9', (43, 36), (44, 33))
        self.add_contour('c0', 'e0', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e4-4')
        self.add_contour('c1', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7', 'e5-8', 'e5-9', 'e2', 'e3')
