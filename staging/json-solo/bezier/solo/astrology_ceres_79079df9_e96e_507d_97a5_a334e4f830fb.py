"""Batch-01/astrology ceres (culture), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('sym-e2', (24, 22), ((30.88, 22), (36.38, 18.745), (39, 13)))
        self.add_bezier('sym-e3', (39, 13), ((39.5, 11.9), (40, 10.191), (40, 9)))
        self.add_bezier('sym-e4', (40, 9), ((40, 8.927), (40, 9.082), (40, 9)))
        self.add_bezier('sym-e5', (40, 9), ((40, 7.364), (40, 5.636), (40, 4)))
        self.add_bezier('sym-e6', (24, 22), ((17.12, 22), (11.62, 18.745), (9, 13)))
        self.add_bezier('sym-e7', (9, 13), ((8.5, 11.9), (8, 10.191), (8, 9)))
        self.add_bezier('sym-e8', (8, 9), ((8, 8.927), (8, 9.082), (8, 9)))
        self.add_bezier('sym-e9', (8, 9), ((8, 7.364), (8, 5.636), (8, 4)))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1')
        self.add_contour('sym-c2', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c3', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
