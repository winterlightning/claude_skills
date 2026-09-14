"""Lightning with wrench (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a4d7838-471b-4d28-87da-ddd67295cbe7'
SOURCE_PATH = 'icons-json/symbol/lightning with wrench_7a4d7838-471b-4d28-87da-ddd67295cbe7.json'
AUTHOR = 'json_to_solo'

class LightningWithWrench(Solo48):
    icon_id = 'lightning-with-wrench'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('lightning', 'with', 'wrench', 'symbol')

    def build(self):
        self.add_line('e0', (25, 11), (29, 7))
        self.add_line('e1', (17, 17), (6, 29))
        self.add_line('e2', (13, 35), (24, 22))
        self.add_line('e3', (40, 20), (34, 31))
        self.add_line('e4', (34, 31), (42, 31))
        self.add_line('e5', (42, 31), (33, 42))
        self.add_arc('e6', (31, 18), (25, 11), radius_x=6)
        self.add_arc('e7-1', (29, 7), (25, 6), radius_x=9, sweep=False)
        self.add_line('e7-2', (25, 6), (23, 6))
        self.add_arc('e7-3', (23, 6), (18, 9), radius_x=9, sweep=False)
        self.add_arc('e7-4', (18, 9), (17, 17), radius_x=7, sweep=False)
        self.add_arc('e8', (31, 18), (24, 22), radius_x=8)
        self.add_contour('c0', 'e6', 'e0', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e1')
        self.add_contour('c1', 'e8')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4', 'e5')
