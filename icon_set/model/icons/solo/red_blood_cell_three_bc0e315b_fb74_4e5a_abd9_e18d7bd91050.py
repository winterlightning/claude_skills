"""Red blood cell three (health), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc0e315b-fb74-4e5a-abd9-e18d7bd91050'
SOURCE_PATH = 'icons-json/health/red blood cell three_bc0e315b-fb74-4e5a-abd9-e18d7bd91050.json'
AUTHOR = 'json_to_solo'

class RedBloodCellThree(Solo48):
    icon_id = 'red-blood-cell-three'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('red', 'blood', 'cell', 'three', 'health')

    def build(self):
        self.add_arc('e0-1', (20, 11), (12, 8), radius_x=13, sweep=False)
        self.add_line('e0-2', (12, 8), (6, 9))
        self.add_arc('e0-3', (6, 9), (4, 12), radius_x=4, sweep=False)
        self.add_arc('e0-4', (4, 12), (9, 16), radius_x=5, sweep=False)
        self.add_arc('e0-5', (9, 16), (19, 16), radius_x=17, sweep=False)
        self.add_arc('e0-6', (19, 16), (20, 11), radius_x=3, sweep=False)
        self.add_arc('e1-1', (43, 13), (34, 13), radius_x=11, sweep=False)
        self.add_arc('e1-2', (34, 13), (27, 20), radius_x=8, sweep=False)
        self.add_arc('e1-3', (27, 20), (35, 22), radius_x=6, sweep=False)
        self.add_arc('e1-4', (35, 22), (43, 18), radius_x=18, sweep=False)
        self.add_arc('e1-5', (43, 18), (44, 15), radius_x=5, sweep=False)
        self.add_line('e1-6', (44, 15), (43, 13))
        self.add_line('e2-1', (28, 38), (22, 40))
        self.add_arc('e2-2', (22, 40), (11, 37), radius_x=22)
        self.add_arc('e2-3', (11, 37), (6, 31), radius_x=10)
        self.add_arc('e2-4', (6, 31), (11, 25), radius_x=6)
        self.add_arc('e2-5', (11, 25), (26, 29), radius_x=20)
        self.add_arc('e2-6', (26, 29), (28, 38), radius_x=6)
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3', 'e0-4', 'e0-5', 'e0-6', closed=True)
        self.add_contour('c1', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', closed=True)
        self.add_contour('c2', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', closed=True)
