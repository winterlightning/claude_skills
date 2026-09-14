"""Lgbt heart (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '144220e1-741d-429f-9845-957359566973'
SOURCE_PATH = 'icons-json/symbol/lgbt heart_144220e1-741d-429f-9845-957359566973.json'
AUTHOR = 'json_to_solo'

class LgbtHeart(Solo48):
    icon_id = 'lgbt-heart'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('lgbt', 'heart', 'symbol')

    def build(self):
        self.add_line('sym-e0', (39, 28), (9, 28))
        self.add_line('sym-e1', (9, 28), (22, 39))
        self.add_line('sym-e2', (22, 39), (24, 40))
        self.add_line('sym-e3', (24, 40), (26, 39))
        self.add_line('sym-e4', (26, 39), (39, 28))
        self.add_arc('sym-e5', (39, 28), (44, 20), radius_x=15, sweep=False)
        self.add_line('sym-e6', (44, 20), (4, 20))
        self.add_arc('sym-e7', (4, 20), (9, 28), radius_x=16, sweep=False)
        self.add_line('sym-e8', (44, 20), (44, 17))
        self.add_arc('sym-e9-1', (44, 17), (41, 11), radius_x=8, sweep=False)
        self.add_arc('sym-e9-2', (41, 11), (34, 8), radius_x=10, sweep=False)
        self.add_line('sym-e11', (34, 8), (27, 10))
        self.add_arc('sym-e12', (27, 10), (25, 12), radius_x=14)
        self.add_line('sym-e13', (25, 12), (24, 13))
        self.add_line('sym-e16', (24, 13), (23, 12))
        self.add_arc('sym-e17', (23, 12), (21, 10), radius_x=15)
        self.add_line('sym-e18', (21, 10), (14, 8))
        self.add_arc('sym-e20-1', (14, 8), (7, 11), radius_x=10, sweep=False)
        self.add_arc('sym-e20-2', (7, 11), (4, 17), radius_x=9, sweep=False)
        self.add_line('sym-e21', (4, 17), (4, 20))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c1', 'sym-e8', 'sym-e9-1', 'sym-e9-2', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e20-1', 'sym-e20-2', 'sym-e21')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
