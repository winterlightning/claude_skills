"""Eye 1 (container), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a93bf49-363b-48fa-94da-6dbc6570089f'
SOURCE_PATH = 'icons-json/container/eye 1_8a93bf49-363b-48fa-94da-6dbc6570089f.json'
AUTHOR = 'json_to_solo'

class Eye18a93bf49(Solo48):
    icon_id = 'eye-1-8a93bf49'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    aliases = ()
    keywords = ('eye', 'container')

    def build(self):
        self.add_arc('e0-1', (4, 25), (24, 40), radius_x=26, sweep=False)
        self.add_arc('e0-2', (24, 40), (44, 25), radius_x=23, sweep=False)
        self.add_arc('e0-3', (44, 25), (25, 8), radius_x=21, sweep=False)
        self.add_line('e0-4', (25, 8), (17, 9))
        self.add_arc('e0-5', (17, 9), (10, 15), radius_x=17, sweep=False)
        self.add_arc('e0-6', (10, 15), (4, 25), radius_x=65, sweep=False)
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3', 'e0-4', 'e0-5', 'e0-6', closed=True)
