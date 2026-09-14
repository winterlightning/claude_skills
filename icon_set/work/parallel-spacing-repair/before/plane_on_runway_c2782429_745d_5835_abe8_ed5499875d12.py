"""Plane on runway (travel), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c2782429-745d-5835-abe8-ed5499875d12'
SOURCE_PATH = 'icons-json/travel/plane on runway_c2782429-745d-5835-abe8-ed5499875d12.json'
AUTHOR = 'json_to_solo'

class PlaneOnRunway(Solo48):
    icon_id = 'plane-on-runway'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    aliases = ()
    keywords = ('plane', 'on', 'runway', 'travel')

    def build(self):
        self.add_line('e0', (5, 40), (44, 40))
        self.add_line('e1', (37, 8), (26, 14))
        self.add_line('e2', (26, 14), (15, 8))
        self.add_line('e3', (15, 8), (11, 10))
        self.add_line('e4', (11, 10), (19, 18))
        self.add_line('e5', (19, 18), (12, 21))
        self.add_line('e6', (12, 21), (6, 18))
        self.add_line('e7', (6, 18), (4, 19))
        self.add_line('e8', (4, 19), (9, 26))
        self.add_line('e9', (17, 28), (39, 16))
        self.add_arc('e10', (9, 26), (17, 28), radius_x=5, sweep=False)
        self.add_arc('e11-1', (39, 16), (44, 11), radius_x=5, sweep=False)
        self.add_arc('e11-2', (44, 11), (40, 8), radius_x=5, sweep=False)
        self.add_line('e11-3', (40, 8), (37, 8))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e10', 'e9', 'e11-1', 'e11-2', 'e11-3', closed=True)
