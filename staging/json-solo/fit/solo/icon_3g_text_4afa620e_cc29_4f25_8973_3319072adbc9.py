"""3g (text) (other), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4afa620e-cc29-4f25-8973-3319072adbc9'
SOURCE_PATH = 'icons-json/other/3g (text)_4afa620e-cc29-4f25-8973-3319072adbc9.json'
AUTHOR = 'json_to_solo'

class Icon3gTextOther(Solo48):
    icon_id = 'icon-3g-text-other'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('3g', 'text', 'other')

    def build(self):
        self.add_line('e0', (44, 33), (44, 25))
        self.add_line('e1', (44, 25), (37, 25))
        self.add_arc('e2-1', (5, 13), (11, 8), radius_x=7)
        self.add_arc('e2-2', (11, 8), (17, 16), radius_x=7)
        self.add_arc('e2-3', (17, 16), (10, 24), radius_x=7)
        self.add_arc('e2-4', (10, 24), (14, 39), radius_x=8)
        self.add_arc('e2-5', (14, 39), (11, 40), radius_x=5)
        self.add_arc('e2-6', (11, 40), (4, 34), radius_x=8)
        self.add_arc('e3-1', (43, 13), (37, 8), radius_x=7, sweep=False)
        self.add_line('e3-2', (37, 8), (33, 9))
        self.add_arc('e3-3', (33, 9), (29, 13), radius_x=8, sweep=False)
        self.add_arc('e3-4', (29, 13), (28, 32), radius_x=39, sweep=False)
        self.add_arc('e3-5', (28, 32), (36, 40), radius_x=9, sweep=False)
        self.add_line('e3-6', (36, 40), (40, 39))
        self.add_arc('e3-7', (40, 39), (43, 36), radius_x=8, sweep=False)
        self.add_line('e3-8', (43, 36), (44, 33))
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6')
        self.add_contour('c1', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8', 'e0', 'e1')
