"""3d (text) (text), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb238e45-d5b9-4df3-ac32-6ad48db5fac4'
SOURCE_PATH = 'icons-json/text/3D (text)_bb238e45-d5b9-4df3-ac32-6ad48db5fac4.json'
AUTHOR = 'json_to_solo'

class Icon3dTextText(Solo48):
    icon_id = 'icon-3d-text-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'text'
    aliases = ()
    keywords = ('3d', 'text')

    def build(self):
        self.add_line('e0', (28, 40), (36, 40))
        self.add_line('e1', (44, 26), (44, 20))
        self.add_line('e2', (34, 8), (28, 8))
        self.add_line('e3', (28, 8), (28, 40))
        self.add_arc('e4-1', (5, 13), (11, 8), radius_x=7)
        self.add_arc('e4-2', (11, 8), (17, 16), radius_x=7)
        self.add_arc('e4-3', (17, 16), (10, 24), radius_x=7)
        self.add_arc('e4-4', (10, 24), (17, 29), radius_x=7)
        self.add_arc('e4-5', (17, 29), (14, 39), radius_x=10)
        self.add_arc('e4-6', (14, 39), (11, 40), radius_x=5)
        self.add_arc('e4-7', (11, 40), (4, 34), radius_x=8)
        self.add_arc('e5-1', (36, 40), (42, 35), radius_x=9, sweep=False)
        self.add_line('e5-2', (42, 35), (44, 27))
        self.add_arc('e5-3', (44, 27), (44, 26), radius_x=30)
        self.add_arc('e6-1', (44, 20), (41, 12), radius_x=13, sweep=False)
        self.add_arc('e6-2', (41, 12), (34, 8), radius_x=9, sweep=False)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e4-7')
        self.add_contour('c1', 'e0', 'e5-1', 'e5-2', 'e5-3', 'e1', 'e6-1', 'e6-2', 'e2', 'e3', closed=True)
