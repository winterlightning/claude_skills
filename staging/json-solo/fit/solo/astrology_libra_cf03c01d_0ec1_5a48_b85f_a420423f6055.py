"""Batch-04/astrology libra (culture), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cf03c01d-0ec1-5a48-b85f-a420423f6055'
SOURCE_PATH = 'icons-json/culture/batch-04/astrology libra_cf03c01d-0ec1-5a48-b85f-a420423f6055.json'
AUTHOR = 'json_to_solo'

class Batch04AstrologyLibra(Solo48):
    icon_id = 'batch-04-astrology-libra'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('batch', 'astrology', 'libra', 'culture')

    def build(self):
        self.add_line('e0', (4, 30), (15, 30))
        self.add_line('e1', (36, 24), (34, 30))
        self.add_line('e2', (34, 30), (44, 30))
        self.add_line('e3', (4, 40), (44, 40))
        self.add_arc('e4-1', (15, 30), (24, 8), radius_x=13)
        self.add_arc('e4-2', (24, 8), (36, 24), radius_x=13)
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2', 'e1', 'e2')
        self.add_contour('c1', 'e3')
