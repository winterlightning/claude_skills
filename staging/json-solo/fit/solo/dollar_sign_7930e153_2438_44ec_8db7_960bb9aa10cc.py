"""Dollar sign (state), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7930e153-2438-44ec-8db7-960bb9aa10cc'
SOURCE_PATH = 'icons-json/state/dollar sign_7930e153-2438-44ec-8db7-960bb9aa10cc.json'
AUTHOR = 'json_to_solo'

class DollarSignState(Solo48):
    icon_id = 'dollar-sign-state'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('dollar', 'sign', 'state')

    def build(self):
        self.add_line('e0', (24, 4), (24, 8))
        self.add_line('e1', (24, 44), (24, 40))
        self.add_line('e2', (24, 8), (24, 23))
        self.add_line('e3', (24, 40), (24, 23))
        self.add_arc('e4', (8, 32), (24, 40), radius_x=14, sweep=False)
        self.add_arc('e5', (39, 15), (24, 8), radius_x=15, sweep=False)
        self.add_arc('e6-1', (24, 8), (12, 11), radius_x=20, sweep=False)
        self.add_arc('e6-2', (12, 11), (10, 18), radius_x=5, sweep=False)
        self.add_arc('e6-3', (10, 18), (24, 23), radius_x=17, sweep=False)
        self.add_arc('e7-1', (24, 40), (35, 38), radius_x=32, sweep=False)
        self.add_arc('e7-2', (35, 38), (40, 32), radius_x=8, sweep=False)
        self.add_line('e7-3', (40, 32), (40, 30))
        self.add_arc('e7-4', (40, 30), (36, 26), radius_x=8, sweep=False)
        self.add_arc('e7-5', (36, 26), (24, 23), radius_x=31, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6-1', 'e6-2', 'e6-3')
        self.add_contour('c5', 'e2')
        self.add_contour('c6', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e7-5')
        self.add_contour('c7', 'e3')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c1', 'c7')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c6', 'c7')
