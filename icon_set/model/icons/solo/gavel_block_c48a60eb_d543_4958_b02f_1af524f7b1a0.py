"""Gavel block (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c48a60eb-d543-4958-b02f-1af524f7b1a0'
SOURCE_PATH = 'icons-json/state/gavel block_c48a60eb-d543-4958-b02f-1af524f7b1a0.json'
AUTHOR = 'json_to_solo'

class GavelBlock(Solo48):
    icon_id = 'gavel-block'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('gavel', 'block', 'state')

    def build(self):
        self.add_line('e0', (5, 8), (43, 8))
        self.add_line('e1', (44, 10), (44, 38))
        self.add_line('e2', (43, 40), (5, 40))
        self.add_line('e3', (4, 38), (4, 10))
        self.add_arc('e4', (43, 8), (44, 10), radius_x=3)
        self.add_arc('e5', (44, 38), (43, 40), radius_x=3)
        self.add_arc('e6', (5, 40), (4, 38), radius_x=3)
        self.add_arc('e7', (4, 10), (5, 8), radius_x=3)
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e5', 'e2', 'e6', 'e3', 'e7', closed=True)
