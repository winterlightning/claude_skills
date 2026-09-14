"""Synchronize arrow (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '185b4c70-8b6e-44d8-a39b-cf7d4767f520'
SOURCE_PATH = 'icons-json/interface-essential/synchronize arrow_185b4c70-8b6e-44d8-a39b-cf7d4767f520.json'
AUTHOR = 'json_to_solo'

class SynchronizeArrow(Solo48):
    icon_id = 'synchronize-arrow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('synchronize', 'arrow', 'interface-essential')

    def build(self):
        self.add_line('e0', (4, 19), (9, 25))
        self.add_line('e1', (14, 21), (9, 25))
        self.add_arc('e2-top', (22, 24), (32, 24), radius_x=5, radius_y=4)
        self.add_arc('e2-bottom', (32, 24), (22, 24), radius_x=5, radius_y=4)
        self.add_line('e3-1', (27, 40), (33, 39))
        self.add_arc('e3-2', (33, 39), (38, 36), radius_x=17, sweep=False)
        self.add_arc('e3-3', (38, 36), (44, 24), radius_x=15, sweep=False)
        self.add_line('e3-4', (44, 24), (43, 18))
        self.add_arc('e3-5', (43, 18), (41, 15), radius_x=16)
        self.add_arc('e3-6', (41, 15), (27, 8), radius_x=18, sweep=False)
        self.add_line('e3-7', (27, 8), (20, 9))
        self.add_arc('e3-8', (20, 9), (15, 12), radius_x=19, sweep=False)
        self.add_arc('e3-9', (15, 12), (9, 25), radius_x=16, sweep=False)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8', 'e3-9')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
