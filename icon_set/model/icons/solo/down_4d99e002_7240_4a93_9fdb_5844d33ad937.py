"""Down (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4d99e002-7240-4a93-9fdb-5844d33ad937'
SOURCE_PATH = 'icons-json/arrows/down_4d99e002-7240-4a93-9fdb-5844d33ad937.json'
AUTHOR = 'json_to_solo'

class Down4d99e002(Solo48):
    icon_id = 'down-4d99e002'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('down', 'arrows')

    def build(self):
        self.add_line('e0', (4, 8), (24, 27))
        self.add_line('e1', (24, 27), (44, 8))
        self.add_line('e2', (44, 8), (44, 21))
        self.add_line('e3', (43, 23), (26, 39))
        self.add_line('e4', (23, 39), (5, 23))
        self.add_line('e5', (5, 23), (4, 21))
        self.add_line('e6', (4, 21), (4, 8))
        self.add_line('e7', (44, 21), (43, 23))
        self.add_arc('e8-1', (26, 39), (25, 40), radius_x=4, sweep=False)
        self.add_line('e8-2', (25, 40), (23, 39))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e7', 'e3', 'e8-1', 'e8-2', 'e4', 'e5', 'e6', closed=True)
