"""Mouse 1 (animals), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd1fc63f6-12db-5dd9-8649-42850ceca103'
SOURCE_PATH = 'icons-json/animals/mouse 1_d1fc63f6-12db-5dd9-8649-42850ceca103.json'
AUTHOR = 'json_to_solo'

class Mouse1(Solo48):
    icon_id = 'mouse-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('mouse', 'animals')

    def build(self):
        self.add_line('e0', (31, 23), (41, 34))
        self.add_line('e1', (41, 40), (13, 40))
        self.add_arc('e2-1', (23, 28), (18, 17), radius_x=12)
        self.add_arc('e2-2', (18, 17), (24, 8), radius_x=8)
        self.add_arc('e2-3', (24, 8), (31, 23), radius_x=10)
        self.add_arc('e3-1', (41, 34), (44, 38), radius_x=69, sweep=False)
        self.add_arc('e3-2', (44, 38), (41, 40), radius_x=6)
        self.add_arc('e4-1', (13, 40), (5, 32), radius_x=10)
        self.add_arc('e4-2', (5, 32), (4, 26), radius_x=19)
        self.add_line('e4-3', (4, 26), (5, 19))
        self.add_arc('e4-4', (5, 19), (8, 14), radius_x=14)
        self.add_arc('e4-5', (8, 14), (19, 14), radius_x=7)
        self.add_line('e5', (29, 31), (30, 33))
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e0', 'e3-1', 'e3-2', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5')
        self.add_contour('c1', 'e5')
