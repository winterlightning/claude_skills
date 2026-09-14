"""Au (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9e32ea71-47a5-4017-9550-316b71c862e7'
SOURCE_PATH = 'icons-json/symbol/Au_9e32ea71-47a5-4017-9550-316b71c862e7.json'
AUTHOR = 'json_to_solo'

class AuSymbol(Solo48):
    icon_id = 'au-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('au', 'symbol')

    def build(self):
        self.add_line('e0', (23, 40), (15, 10))
        self.add_line('e1', (11, 9), (4, 40))
        self.add_line('e2', (7, 29), (19, 29))
        self.add_line('e3', (33, 19), (33, 34))
        self.add_line('e4', (44, 19), (44, 40))
        self.add_line('e5-1', (15, 10), (13, 8))
        self.add_line('e5-2', (13, 8), (11, 9))
        self.add_arc('e6-1', (33, 34), (38, 40), radius_x=6, sweep=False)
        self.add_arc('e6-2', (38, 40), (44, 34), radius_x=6, sweep=False)
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e6-1', 'e6-2')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c3')
