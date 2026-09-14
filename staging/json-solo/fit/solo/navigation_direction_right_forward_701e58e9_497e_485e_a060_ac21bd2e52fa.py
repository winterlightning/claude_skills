"""Navigation direction right forward (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '701e58e9-497e-485e-a060-ac21bd2e52fa'
SOURCE_PATH = 'icons-json/interface-essential/navigation direction right forward_701e58e9-497e-485e-a060-ac21bd2e52fa.json'
AUTHOR = 'json_to_solo'

class NavigationDirectionRightForwardInterfaceEssential(Solo48):
    icon_id = 'navigation-direction-right-forward-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'direction', 'right', 'forward', 'interface-essential')

    def build(self):
        self.add_line('e0', (28, 8), (28, 17))
        self.add_line('e1', (28, 17), (20, 17))
        self.add_line('e2', (17, 31), (28, 31))
        self.add_line('e3', (28, 31), (28, 40))
        self.add_line('e4', (28, 40), (43, 25))
        self.add_line('e5', (44, 24), (28, 8))
        self.add_line('e6', (4, 40), (4, 39))
        self.add_arc('e7-1', (20, 17), (4, 33), radius_x=16, sweep=False)
        self.add_line('e7-2', (4, 33), (4, 39))
        self.add_arc('e7-3', (4, 39), (17, 31), radius_x=16)
        self.add_arc('e8', (43, 25), (44, 24), radius_x=32)
        self.add_contour('c0', 'e6')
        self.add_contour('c1', 'e0', 'e1', 'e7-1', 'e7-2', 'e7-3', 'e2', 'e3', 'e4', 'e8', 'e5', closed=True)
        self.relate('connect', 'c0', 'c1')
