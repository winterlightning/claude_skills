"""Signature sign (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '854e9a2a-e250-5f3f-9ead-c9b63e43eb2f'
SOURCE_PATH = 'icons-json/interface-essential/signature sign_854e9a2a-e250-5f3f-9ead-c9b63e43eb2f.json'
AUTHOR = 'json_to_solo'

class SignatureSign854e9a2a(Solo48):
    icon_id = 'signature-sign-854e9a2a'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('signature', 'sign', 'interface-essential')

    def build(self):
        self.add_line('e0', (39, 31), (38, 28))
        self.add_line('e1', (25, 30), (26, 25))
        self.add_line('e2', (20, 21), (15, 24))
        self.add_arc('e3', (44, 32), (39, 31), radius_x=3)
        self.add_arc('e4-1', (38, 28), (35, 28), radius_x=2, sweep=False)
        self.add_arc('e4-2', (35, 28), (27, 33), radius_x=17)
        self.add_arc('e4-3', (27, 33), (25, 30), radius_x=2)
        self.add_arc('e5', (26, 25), (20, 21), radius_x=4, sweep=False)
        self.add_arc('e6-1', (15, 24), (4, 36), radius_x=21, sweep=False)
        self.add_arc('e6-2', (4, 36), (5, 39), radius_x=5, sweep=False)
        self.add_line('e6-3', (5, 39), (7, 40))
        self.add_arc('e6-4', (7, 40), (17, 24), radius_x=15, sweep=False)
        self.add_arc('e6-5', (17, 24), (16, 13), radius_x=31, sweep=False)
        self.add_arc('e6-6', (16, 13), (10, 8), radius_x=7, sweep=False)
        self.add_arc('e6-7', (10, 8), (4, 14), radius_x=6, sweep=False)
        self.add_arc('e6-8', (4, 14), (7, 20), radius_x=8, sweep=False)
        self.add_contour('c0', 'e3', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e1', 'e5', 'e2', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e6-6', 'e6-7', 'e6-8')
