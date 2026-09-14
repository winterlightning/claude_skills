"""Batch-03/glasses sun circle (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30c30b8f-1761-4b11-b367-77273103d6f1'
SOURCE_PATH = 'icons-json/accessories/batch-03/glasses sun circle_30c30b8f-1761-4b11-b367-77273103d6f1.json'
AUTHOR = 'json_to_solo'

class Batch03GlassesSunCircle(Solo48):
    icon_id = 'batch-03-glasses-sun-circle'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'glasses', 'sun', 'circle', 'accessories')

    def build(self):
        self.add_arc('sym-e0', (6, 24), (20, 24), radius_x=7, radius_y=16)
        self.add_arc('sym-e1', (20, 24), (6, 24), radius_x=7, radius_y=16)
        self.add_arc('sym-e2', (42, 24), (28, 24), radius_x=7, radius_y=16, sweep=False)
        self.add_arc('sym-e3', (28, 24), (42, 24), radius_x=7, radius_y=16, sweep=False)
        self.add_line('sym-e4', (4, 24), (6, 24))
        self.add_line('sym-e5', (24, 22), (20, 24))
        self.add_line('sym-e6', (44, 24), (42, 24))
        self.add_line('sym-e7', (24, 22), (28, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', closed=True)
        self.add_contour('sym-c2', 'sym-e4')
        self.add_contour('sym-c3', 'sym-e5')
        self.add_contour('sym-c4', 'sym-e6')
        self.add_contour('sym-c5', 'sym-e7')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c5')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c3', 'sym-c5')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c3')
