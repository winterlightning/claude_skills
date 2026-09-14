"""B4 (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8220eff5-889a-4ed4-abe8-9cb5b3c749d9'
SOURCE_PATH = 'icons-json/state/B4_8220eff5-889a-4ed4-abe8-9cb5b3c749d9.json'
AUTHOR = 'json_to_solo'

class B4State(Solo48):
    icon_id = 'b4-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('b4', 'state')

    def build(self):
        self.add_line('e0', (4, 8), (4, 40))
        self.add_line('e1', (4, 40), (10, 40))
        self.add_line('e2', (12, 8), (4, 8))
        self.add_line('e3', (13, 24), (4, 24))
        self.add_line('e4', (44, 33), (29, 33))
        self.add_line('e5', (29, 33), (41, 8))
        self.add_line('e6', (41, 8), (41, 40))
        self.add_line('e7-1', (10, 40), (16, 39))
        self.add_arc('e7-2', (16, 39), (19, 35), radius_x=8, sweep=False)
        self.add_arc('e7-3', (19, 35), (13, 24), radius_x=8, sweep=False)
        self.add_arc('e7-4', (13, 24), (18, 12), radius_x=9, sweep=False)
        self.add_arc('e7-5', (18, 12), (12, 8), radius_x=7, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e7-5', 'e2', closed=True)
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4', 'e5', 'e6')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
