"""Koala head (animals), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f02ee94d-07a6-5d6f-baf8-a6cbb0cb8ed2'
SOURCE_PATH = 'icons-json/animals/koala head_f02ee94d-07a6-5d6f-baf8-a6cbb0cb8ed2.json'
AUTHOR = 'json_to_solo'

class KoalaHeadAnimals(Solo48):
    icon_id = 'koala-head-animals'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('koala', 'head', 'animals')

    def build(self):
        self.add_line('e0-1', (39, 24), (42, 22))
        self.add_line('e0-2', (42, 22), (44, 16))
        self.add_arc('e0-3', (44, 16), (37, 8), radius_x=9, sweep=False)
        self.add_line('e0-4', (37, 8), (31, 11))
        self.add_line('e1-1', (17, 11), (11, 8))
        self.add_arc('e1-2', (11, 8), (5, 12), radius_x=7, sweep=False)
        self.add_line('e1-3', (5, 12), (4, 16))
        self.add_line('e1-4', (4, 16), (5, 20))
        self.add_arc('e1-5', (5, 20), (10, 24), radius_x=9, sweep=False)
        self.add_arc('e2-1', (18, 11), (38, 20), radius_x=14)
        self.add_arc('e2-2', (38, 20), (25, 40), radius_x=15)
        self.add_line('e2-3', (25, 40), (19, 39))
        self.add_arc('e2-4', (19, 39), (14, 36), radius_x=13)
        self.add_arc('e2-5', (14, 36), (11, 31), radius_x=13)
        self.add_arc('e2-6', (11, 31), (18, 11), radius_x=17)
        self.add_arc('e3-1', (25, 20), (21, 23), radius_x=3, sweep=False)
        self.add_arc('e3-2', (21, 23), (22, 31), radius_x=8, sweep=False)
        self.add_arc('e3-3', (22, 31), (27, 30), radius_x=3, sweep=False)
        self.add_arc('e3-4', (27, 30), (25, 20), radius_x=9, sweep=False)
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3', 'e0-4')
        self.add_contour('c1', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5')
        self.add_contour('c2', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', closed=True)
        self.add_contour('c3', 'e3-1', 'e3-2', 'e3-3', 'e3-4', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
