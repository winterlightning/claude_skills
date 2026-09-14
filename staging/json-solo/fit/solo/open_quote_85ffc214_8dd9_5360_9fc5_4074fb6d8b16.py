"""Open quote (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '85ffc214-8dd9-5360-9fc5-4074fb6d8b16'
SOURCE_PATH = 'icons-json/interface-essential/open quote_85ffc214-8dd9-5360-9fc5-4074fb6d8b16.json'
AUTHOR = 'json_to_solo'

class OpenQuoteInterfaceEssential(Solo48):
    icon_id = 'open-quote-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('open', 'quote', 'interface-essential')

    def build(self):
        self.add_line('e0', (7, 24), (5, 26))
        self.add_line('e1', (30, 24), (28, 26))
        self.add_arc('e2', (18, 8), (5, 26), radius_x=20, sweep=False)
        self.add_arc('e3-1', (5, 26), (4, 31), radius_x=14, sweep=False)
        self.add_arc('e3-2', (4, 31), (7, 38), radius_x=10, sweep=False)
        self.add_line('e3-3', (7, 38), (12, 40))
        self.add_arc('e3-4', (12, 40), (20, 28), radius_x=9, sweep=False)
        self.add_arc('e3-5', (20, 28), (7, 24), radius_x=8, sweep=False)
        self.add_arc('e4', (41, 8), (28, 26), radius_x=22, sweep=False)
        self.add_arc('e5-1', (28, 26), (36, 40), radius_x=10, sweep=False)
        self.add_arc('e5-2', (36, 40), (41, 38), radius_x=8, sweep=False)
        self.add_arc('e5-3', (41, 38), (44, 31), radius_x=10, sweep=False)
        self.add_line('e5-4', (44, 31), (42, 25))
        self.add_line('e5-5', (42, 25), (40, 23))
        self.add_arc('e5-6', (40, 23), (30, 24), radius_x=8, sweep=False)
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e0', closed=True)
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e1', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c3')
