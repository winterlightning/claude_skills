"""Wind (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bfffa211-4688-49bd-87eb-16a4c14d3a9b'
SOURCE_PATH = 'icons-json/state/wind_bfffa211-4688-49bd-87eb-16a4c14d3a9b.json'
AUTHOR = 'json_to_solo'

class Wind(Solo48):
    icon_id = 'wind'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('wind', 'state')

    def build(self):
        self.add_arc('e0-1', (4, 23), (14, 20), radius_x=21)
        self.add_arc('e0-2', (14, 20), (19, 21), radius_x=16)
        self.add_line('e0-3', (19, 21), (29, 26))
        self.add_arc('e0-4', (29, 26), (39, 26), radius_x=20, sweep=False)
        self.add_arc('e0-5', (39, 26), (44, 21), radius_x=6, sweep=False)
        self.add_arc('e1-1', (7, 36), (16, 34), radius_x=17)
        self.add_arc('e1-2', (16, 34), (28, 39), radius_x=22)
        self.add_line('e1-3', (28, 39), (34, 40))
        self.add_line('e1-4', (34, 40), (40, 39))
        self.add_arc('e1-5', (40, 39), (43, 35), radius_x=5, sweep=False)
        self.add_arc('e2-1', (8, 10), (16, 8), radius_x=17)
        self.add_line('e2-2', (16, 8), (22, 9))
        self.add_line('e2-3', (22, 9), (30, 13))
        self.add_arc('e2-4', (30, 13), (44, 9), radius_x=10, sweep=False)
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3', 'e0-4', 'e0-5')
        self.add_contour('c1', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5')
        self.add_contour('c2', 'e2-1', 'e2-2', 'e2-3', 'e2-4')
