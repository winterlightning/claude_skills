"""Down (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bca79b7a-52ce-4815-a26d-03daa6a83285'
SOURCE_PATH = 'icons-json/arrows/down_bca79b7a-52ce-4815-a26d-03daa6a83285.json'
AUTHOR = 'json_to_solo'

class Down(Solo48):
    icon_id = 'down'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('down', 'arrows')

    def build(self):
        self.add_line('e0', (42, 8), (6, 8))
        self.add_line('e1', (4, 11), (22, 39))
        self.add_line('e2', (26, 39), (44, 11))
        self.add_arc('e3-1', (6, 8), (4, 10), radius_x=2, sweep=False)
        self.add_line('e3-2', (4, 10), (4, 11))
        self.add_arc('e4-1', (22, 39), (24, 40), radius_x=3, sweep=False)
        self.add_arc('e4-2', (24, 40), (26, 39), radius_x=3, sweep=False)
        self.add_line('e5-1', (44, 11), (44, 9))
        self.add_arc('e5-2', (44, 9), (42, 8), radius_x=3, sweep=False)
        self.add_contour('c0', 'e0', 'e3-1', 'e3-2', 'e1', 'e4-1', 'e4-2', 'e2', 'e5-1', 'e5-2', closed=True)
