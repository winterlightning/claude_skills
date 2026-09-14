"""Batch-01/astrology aries (culture), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '28ab2a14-d6a4-56d6-82df-af778631fe00'
SOURCE_PATH = 'icons-json/culture/batch-01/astrology aries_28ab2a14-d6a4-56d6-82df-af778631fe00.json'
AUTHOR = 'json_to_solo'

class Batch01AstrologyAries(Solo48):
    icon_id = 'batch-01-astrology-aries'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('batch', 'astrology', 'aries', 'culture')

    def build(self):
        self.add_line('sym-e0', (24, 40), (29, 23))
        self.add_arc('sym-e1', (29, 23), (33, 15), radius_x=35)
        self.add_arc('sym-e2', (33, 15), (43, 8), radius_x=14)
        self.add_line('sym-e3', (43, 8), (44, 8))
        self.add_line('sym-e4', (24, 40), (19, 23))
        self.add_line('sym-e5', (19, 23), (15, 15))
        self.add_arc('sym-e6', (15, 15), (5, 8), radius_x=14, sweep=False)
        self.add_arc('sym-e7', (5, 8), (4, 8), radius_x=5)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c1', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.relate('connect', 'sym-c0', 'sym-c1')
