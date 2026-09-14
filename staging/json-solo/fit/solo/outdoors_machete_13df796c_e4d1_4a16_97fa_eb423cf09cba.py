"""Outdoors machete (outdoors), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '13df796c-e4d1-4a16-97fa-eb423cf09cba'
SOURCE_PATH = 'icons-json/outdoors/outdoors machete_13df796c-e4d1-4a16-97fa-eb423cf09cba.json'
AUTHOR = 'json_to_solo'

class OutdoorsMacheteOutdoors(Solo48):
    icon_id = 'outdoors-machete-outdoors'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('outdoors', 'machete')

    def build(self):
        self.add_line('e0', (17, 26), (21, 31))
        self.add_line('e1', (17, 26), (7, 35))
        self.add_line('e2', (6, 39), (8, 42))
        self.add_line('e3', (13, 38), (21, 31))
        self.add_line('e4', (17, 26), (40, 6))
        self.add_line('e5', (39, 19), (22, 33))
        self.add_line('e6', (22, 33), (21, 31))
        self.add_arc('e7-1', (7, 35), (6, 36), radius_x=2, sweep=False)
        self.add_line('e7-2', (6, 36), (6, 39))
        self.add_arc('e8-1', (8, 42), (9, 42), radius_x=22)
        self.add_line('e8-2', (9, 42), (11, 42))
        self.add_line('e8-3', (11, 42), (12, 40))
        self.add_arc('e8-4', (12, 40), (13, 38), radius_x=17)
        self.add_arc('e9-1', (40, 6), (42, 10), radius_x=5)
        self.add_arc('e9-2', (42, 10), (39, 19), radius_x=15)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7-1', 'e7-2', 'e2', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e3')
        self.add_contour('c2', 'e4', 'e9-1', 'e9-2', 'e5', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
