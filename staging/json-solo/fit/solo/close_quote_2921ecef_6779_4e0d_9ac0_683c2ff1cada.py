"""Close quote (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2921ecef-6779-4e0d-9ac0-683c2ff1cada'
SOURCE_PATH = 'icons-json/interface-essential/close quote_2921ecef-6779-4e0d-9ac0-683c2ff1cada.json'
AUTHOR = 'json_to_solo'

class CloseQuoteInterfaceEssential(Solo48):
    icon_id = 'close-quote-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('close', 'quote', 'interface-essential')

    def build(self):
        self.add_line('e0', (44, 22), (44, 10))
        self.add_line('e1', (42, 8), (36, 8))
        self.add_line('e2', (21, 22), (21, 10))
        self.add_line('e3', (19, 8), (12, 8))
        self.add_line('e4-1', (29, 40), (34, 39))
        self.add_arc('e4-2', (34, 39), (44, 23), radius_x=19, sweep=False)
        self.add_line('e4-3', (44, 23), (44, 22))
        self.add_arc('e5', (44, 10), (42, 8), radius_x=2, sweep=False)
        self.add_arc('e6-1', (36, 8), (27, 17), radius_x=10, sweep=False)
        self.add_arc('e6-2', (27, 17), (39, 27), radius_x=10, sweep=False)
        self.add_arc('e7', (6, 40), (21, 22), radius_x=17, sweep=False)
        self.add_arc('e8', (21, 10), (19, 8), radius_x=2, sweep=False)
        self.add_arc('e9-1', (12, 8), (4, 17), radius_x=10, sweep=False)
        self.add_line('e9-2', (4, 17), (5, 22))
        self.add_line('e9-3', (5, 22), (8, 25))
        self.add_line('e9-4', (8, 25), (15, 27))
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e0', 'e5', 'e1', 'e6-1', 'e6-2')
        self.add_contour('c1', 'e7', 'e2', 'e8', 'e3', 'e9-1', 'e9-2', 'e9-3', 'e9-4')
