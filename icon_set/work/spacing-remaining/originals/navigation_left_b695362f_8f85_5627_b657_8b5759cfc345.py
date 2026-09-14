"""Navigation left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b695362f-8f85-5627-b657-8b5759cfc345'
SOURCE_PATH = 'icons-json/interface-essential/navigation left_b695362f-8f85-5627-b657-8b5759cfc345.json'
AUTHOR = 'json_to_solo'

class NavigationLeftB695362f(Solo48):
    icon_id = 'navigation-left-b695362f'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'left', 'interface-essential')

    def build(self):
        self.add_line('e0', (14, 8), (4, 20))
        self.add_line('e1', (5, 23), (14, 34))
        self.add_line('e2', (4, 20), (5, 23))
        self.add_arc('e3-1', (13, 22), (30, 20), radius_x=74)
        self.add_arc('e3-2', (30, 20), (40, 25), radius_x=11)
        self.add_arc('e3-3', (40, 25), (44, 39), radius_x=33)
        self.add_arc('e3-4', (44, 39), (44, 40), radius_x=39, sweep=False)
        self.add_contour('c0', 'e0', 'e2', 'e1')
        self.add_contour('c1', 'e3-1', 'e3-2', 'e3-3', 'e3-4')
