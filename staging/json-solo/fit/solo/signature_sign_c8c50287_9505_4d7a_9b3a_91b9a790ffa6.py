"""Signature sign (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c8c50287-9505-4d7a-9b3a-91b9a790ffa6'
SOURCE_PATH = 'icons-json/interface-essential/signature sign_c8c50287-9505-4d7a-9b3a-91b9a790ffa6.json'
AUTHOR = 'json_to_solo'

class SignatureSignC8c50287(Solo48):
    icon_id = 'signature-sign-c8c50287'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('signature', 'sign', 'interface-essential')

    def build(self):
        self.add_line('e0', (36, 34), (38, 29))
        self.add_line('e1', (30, 28), (25, 36))
        self.add_line('e2', (19, 33), (25, 18))
        self.add_line('e3', (14, 15), (4, 40))
        self.add_arc('e4-1', (44, 35), (39, 40), radius_x=7)
        self.add_arc('e4-2', (39, 40), (36, 34), radius_x=4)
        self.add_arc('e5-1', (38, 29), (36, 22), radius_x=6, sweep=False)
        self.add_arc('e5-2', (36, 22), (30, 28), radius_x=8, sweep=False)
        self.add_arc('e6-1', (25, 36), (21, 40), radius_x=12)
        self.add_arc('e6-2', (21, 40), (19, 33), radius_x=5)
        self.add_arc('e7-1', (25, 18), (25, 10), radius_x=12, sweep=False)
        self.add_arc('e7-2', (25, 10), (22, 8), radius_x=4, sweep=False)
        self.add_arc('e7-3', (22, 8), (14, 15), radius_x=9, sweep=False)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e0', 'e5-1', 'e5-2', 'e1', 'e6-1', 'e6-2', 'e2', 'e7-1', 'e7-2', 'e7-3', 'e3')
