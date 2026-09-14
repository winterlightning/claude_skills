"""Batch-07/astrology uranus (culture), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('sym-e5', (17, 15), (8, 26), radius_x=10)
        self.add_line('sym-e6', (24, 4), (24, 28))
        self.add_arc('sym-e7', (17, 15), (8, 4), radius_x=10, sweep=False)
        self.add_arc('sym-e8', (40, 26), (31, 15), radius_x=11)
        self.add_arc('sym-e10', (31, 15), (40, 4), radius_x=10)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', closed=True)
        self.add_contour('sym-c1', 'sym-e3', 'sym-e5')
        self.add_contour('sym-c2', 'sym-e6')
        self.add_contour('sym-c3', 'sym-e7')
        self.add_contour('sym-c4', 'sym-e8', 'sym-e10')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
