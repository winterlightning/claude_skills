"""Line (diagrams), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22755210-a40c-5f93-b3a1-cca015f5f4a2'
SOURCE_PATH = 'icons-json/diagrams/line_22755210-a40c-5f93-b3a1-cca015f5f4a2.json'
AUTHOR = 'json_to_solo'

class Line22755210(Solo48):
    icon_id = 'line-22755210'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    aliases = ()
    keywords = ('line', 'diagrams')

    def build(self):
        self.add_arc('sym-e0', (32, 11), (42, 11), radius_x=5)
        self.add_arc('sym-e1', (42, 11), (32, 11), radius_x=5)
        self.add_arc('sym-e2', (11, 32), (11, 42), radius_x=5, sweep=False)
        self.add_arc('sym-e3', (11, 42), (11, 32), radius_x=5, sweep=False)
        self.add_line('sym-e4', (24, 24), (34, 15))
        self.add_arc('sym-e5', (34, 15), (33, 14), radius_x=49)
        self.add_line('sym-e6', (24, 24), (15, 34))
        self.add_arc('sym-e7', (15, 34), (14, 33), radius_x=49, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', closed=True)
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c3', 'sym-e6', 'sym-e7')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
