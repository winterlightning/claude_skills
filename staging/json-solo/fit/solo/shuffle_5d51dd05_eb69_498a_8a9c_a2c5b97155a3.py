"""Shuffle (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5d51dd05-eb69-498a-8a9c-a2c5b97155a3'
SOURCE_PATH = 'icons-json/interface-essential/shuffle_5d51dd05-eb69-498a-8a9c-a2c5b97155a3.json'
AUTHOR = 'json_to_solo'

class ShuffleInterfaceEssential(Solo48):
    icon_id = 'shuffle-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('shuffle', 'interface-essential')

    def build(self):
        self.add_line('e0', (39, 8), (44, 14))
        self.add_line('e1', (14, 33), (30, 15))
        self.add_line('e2', (33, 14), (44, 14))
        self.add_line('e3', (39, 19), (44, 14))
        self.add_line('e4', (4, 12), (10, 12))
        self.add_line('e5', (15, 14), (19, 19))
        self.add_line('e6', (27, 28), (31, 33))
        self.add_line('e7', (36, 34), (44, 34))
        self.add_line('e8', (39, 40), (44, 34))
        self.add_line('e9', (39, 29), (44, 34))
        self.add_arc('e10', (4, 35), (14, 33), radius_x=15, sweep=False)
        self.add_line('e11', (30, 15), (33, 14))
        self.add_arc('e12', (10, 12), (15, 14), radius_x=5)
        self.add_arc('e13', (31, 33), (36, 34), radius_x=6, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e10', 'e1', 'e11', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e12', 'e5')
        self.add_contour('c4', 'e6', 'e13', 'e7')
        self.add_contour('c5', 'e8')
        self.add_contour('c6', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
