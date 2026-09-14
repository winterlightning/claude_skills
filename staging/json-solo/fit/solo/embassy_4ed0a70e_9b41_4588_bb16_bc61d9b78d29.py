"""Embassy (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ed0a70e-9b41-4588-bb16-bc61d9b78d29'
SOURCE_PATH = 'icons-json/symbol/embassy_4ed0a70e-9b41-4588-bb16-bc61d9b78d29.json'
AUTHOR = 'json_to_solo'

class EmbassySymbol(Solo48):
    icon_id = 'embassy-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('embassy', 'symbol')

    def build(self):
        self.add_line('e0', (44, 40), (4, 40))
        self.add_line('e1', (39, 24), (39, 40))
        self.add_line('e2', (29, 40), (29, 24))
        self.add_line('e3', (19, 40), (19, 24))
        self.add_line('e4', (9, 24), (9, 40))
        self.add_line('e5', (7, 24), (40, 24))
        self.add_arc('e6-1', (40, 24), (41, 24), radius_x=79, sweep=False)
        self.add_arc('e6-2', (41, 24), (41, 21), radius_x=2, sweep=False)
        self.add_arc('e6-3', (41, 21), (36, 13), radius_x=21, sweep=False)
        self.add_arc('e6-4', (36, 13), (30, 9), radius_x=18, sweep=False)
        self.add_line('e6-5', (30, 9), (23, 8))
        self.add_arc('e6-6', (23, 8), (7, 24), radius_x=17, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e6-6', closed=True)
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c3', 'c0')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c0')
