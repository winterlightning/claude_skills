"""Diving flag buoys (outdoors), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '52c0621c-d20e-5335-bc17-eee5dc1d2f26'
SOURCE_PATH = 'icons-json/outdoors/diving flag buoys_52c0621c-d20e-5335-bc17-eee5dc1d2f26.json'
AUTHOR = 'json_to_solo'

class DivingFlagBuoysOutdoors(Solo48):
    icon_id = 'diving-flag-buoys-outdoors'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('diving', 'flag', 'buoys', 'outdoors')

    def build(self):
        self.add_line('e0', (16, 5), (40, 5))
        self.add_line('e1', (40, 5), (40, 22))
        self.add_line('e2', (40, 22), (13, 22))
        self.add_line('e3', (36, 22), (16, 5))
        self.add_line('e4', (16, 5), (13, 5))
        self.add_line('e5', (13, 4), (13, 32))
        self.add_line('e6', (13, 39), (13, 44))
        self.add_line('e7', (8, 44), (19, 44))
        self.add_arc('e8-top', (9, 36), (17, 36), radius_x=4)
        self.add_arc('e8-bottom', (17, 36), (9, 36), radius_x=4)
        self.add_arc('e9', (13, 32), (14, 32), radius_x=18, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3', 'e4')
        self.add_contour('c2', 'e5', 'e9')
        self.add_contour('c3', 'e6')
        self.add_contour('c4', 'e7')
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c2', 'e8')
        self.relate('connect', 'c2', 'e8')
        self.relate('connect', 'c3', 'e8')
        self.relate('connect', 'c3', 'c4')
