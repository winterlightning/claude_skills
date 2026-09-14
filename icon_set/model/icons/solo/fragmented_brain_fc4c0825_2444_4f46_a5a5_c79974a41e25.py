"""Fragmented brain (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fc4c0825-2444-4f46-a5a5-c79974a41e25'
SOURCE_PATH = 'icons-json/symbol/fragmented brain_fc4c0825-2444-4f46-a5a5-c79974a41e25.json'
AUTHOR = 'json_to_solo'

class FragmentedBrain(Solo48):
    icon_id = 'fragmented-brain'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('fragmented', 'brain', 'symbol')

    def build(self):
        self.add_line('e0', (13, 39), (26, 22))
        self.add_line('e1', (13, 39), (36, 26))
        self.add_line('e2', (9, 19), (26, 22))
        self.add_line('e3', (26, 22), (38, 10))
        self.add_line('e4', (26, 22), (36, 26))
        self.add_line('e5', (36, 26), (40, 24))
        self.add_line('e6-1', (13, 39), (9, 40))
        self.add_line('e6-2', (9, 40), (6, 39))
        self.add_line('e6-3', (6, 39), (4, 34))
        self.add_arc('e6-4', (4, 34), (9, 19), radius_x=27)
        self.add_arc('e7-1', (9, 19), (29, 8), radius_x=25)
        self.add_line('e7-2', (29, 8), (38, 10))
        self.add_line('e8-1', (40, 24), (43, 22))
        self.add_line('e8-2', (43, 22), (44, 18))
        self.add_arc('e8-3', (44, 18), (43, 15), radius_x=5, sweep=False)
        self.add_line('e8-4', (43, 15), (38, 10))
        self.add_contour('c0', 'e6-1', 'e6-2', 'e6-3', 'e6-4')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e7-1', 'e7-2')
        self.add_contour('c4', 'e2')
        self.add_contour('c5', 'e3')
        self.add_contour('c6', 'e4')
        self.add_contour('c7', 'e5', 'e8-1', 'e8-2', 'e8-3', 'e8-4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c7')
        self.relate('connect', 'c5', 'c7')
