"""Batch-01/astrology ceres (culture), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '79079df9-e96e-507d-97a5-a334e4f830fb'
SOURCE_PATH = 'icons-json/culture/batch-01/astrology ceres_79079df9-e96e-507d-97a5-a334e4f830fb.json'
AUTHOR = 'json_to_solo'

class Batch01AstrologyCeres(Solo48):
    icon_id = 'batch-01-astrology-ceres'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('batch', 'astrology', 'ceres', 'culture')

    def build(self):
        self.add_line('sym-e0', (24, 22), (24, 44))
        self.add_line('sym-e1', (15, 35), (33, 35))
        self.add_arc('sym-e2', (24, 22), (39, 13), radius_x=15, sweep=False)
        self.add_line('sym-e3', (39, 13), (40, 9))
        self.add_line('sym-e5', (40, 9), (40, 4))
        self.add_arc('sym-e6', (24, 22), (9, 13), radius_x=16)
        self.add_arc('sym-e7', (9, 13), (8, 9), radius_x=12)
        self.add_line('sym-e9-1', (8, 9), (8, 8))
        self.add_line('sym-e9-2', (8, 8), (8, 4))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1')
        self.add_contour('sym-c2', 'sym-e2', 'sym-e3', 'sym-e5')
        self.add_contour('sym-c3', 'sym-e6', 'sym-e7', 'sym-e9-1', 'sym-e9-2')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
