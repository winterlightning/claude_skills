"""Batch-06/astrology cane (culture), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7169d0df-e69e-5ecc-8180-aa3f755ddd80'
SOURCE_PATH = 'icons-json/culture/batch-06/astrology cane_7169d0df-e69e-5ecc-8180-aa3f755ddd80.json'
AUTHOR = 'json_to_solo'

class Batch06AstrologyCane(Solo48):
    icon_id = 'batch-06-astrology-cane'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('batch', 'astrology', 'cane', 'culture')

    def build(self):
        self.add_line('e0', (23, 9), (8, 44))
        self.add_arc('e1-1', (38, 17), (40, 11), radius_x=12, sweep=False)
        self.add_arc('e1-2', (40, 11), (32, 4), radius_x=9, sweep=False)
        self.add_line('e1-3', (32, 4), (27, 5))
        self.add_line('e1-4', (27, 5), (23, 9))
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e0')
