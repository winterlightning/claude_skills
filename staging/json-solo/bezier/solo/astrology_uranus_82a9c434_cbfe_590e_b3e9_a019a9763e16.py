"""Batch-07/astrology uranus (culture), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82a9c434-cbfe-590e-b3e9-a019a9763e16'
SOURCE_PATH = 'icons-json/culture/batch-07/astrology uranus_82a9c434-cbfe-590e-b3e9-a019a9763e16.json'
AUTHOR = 'json_to_solo'

class Batch07AstrologyUranus(Solo48):
    icon_id = 'batch-07-astrology-uranus'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('batch', 'astrology', 'uranus', 'culture')

    def build(self):
        self.add_arc('sym-e0', (15, 36), (24, 28), radius_x=9, radius_y=8)
        self.add_arc('sym-e1', (24, 28), (33, 36), radius_x=9, radius_y=8)
        self.add_arc('sym-e2', (33, 36), (15, 36), radius_x=9, radius_y=8)
        self.add_line('sym-e3', (31, 15), (17, 15))
        self.add_bezier('sym-e4', (17, 15), ((17.006, 15.16), (17, 14.842), (17, 15)))
        self.add_bezier('sym-e5', (17, 15), ((17, 20.168), (13.851, 25.136), (8, 26)))
        self.add_line('sym-e6', (24, 4), (24, 28))
        self.add_bezier('sym-e7', (17, 15), ((16.79, 9.309), (14.59, 5.127), (8, 4)))
        self.add_bezier('sym-e8', (40, 26), ((34.149, 25.136), (31, 20.168), (31, 15)))
        self.add_bezier('sym-e9', (31, 15), ((31, 14.842), (30.994, 15.16), (31, 15)))
        self.add_bezier('sym-e10', (31, 15), ((31.21, 9.309), (33.41, 5.127), (40, 4)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', closed=True)
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c2', 'sym-e6')
        self.add_contour('sym-c3', 'sym-e7')
        self.add_contour('sym-c4', 'sym-e8', 'sym-e9', 'sym-e10')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
