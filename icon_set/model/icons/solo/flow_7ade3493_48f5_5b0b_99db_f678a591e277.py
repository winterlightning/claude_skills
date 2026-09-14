"""Flow (diagrams), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7ade3493-48f5-5b0b-99db-f678a591e277'
SOURCE_PATH = 'icons-json/diagrams/flow_7ade3493-48f5-5b0b-99db-f678a591e277.json'
AUTHOR = 'json_to_solo'

class Flow(Solo48):
    icon_id = 'flow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    aliases = ()
    keywords = ('flow', 'diagrams')

    def build(self):
        self.add_line('e0', (14, 12), (22, 12))
        self.add_line('e1', (22, 35), (9, 35))
        self.add_line('e2', (9, 35), (13, 40))
        self.add_line('e3', (13, 30), (9, 35))
        self.add_arc('e4-top', (22, 35), (32, 35), radius_x=5, radius_y=4)
        self.add_arc('e4-bottom', (32, 35), (22, 35), radius_x=5, radius_y=4)
        self.add_arc('e5-top', (22, 12), (32, 12), radius_x=5, radius_y=4)
        self.add_arc('e5-bottom', (32, 12), (22, 12), radius_x=5, radius_y=4)
        self.add_arc('e6-top', (4, 12), (14, 12), radius_x=5, radius_y=4)
        self.add_arc('e6-bottom', (14, 12), (4, 12), radius_x=5, radius_y=4)
        self.add_line('e7', (13, 11), (14, 12))
        self.add_arc('e8-1', (31, 12), (40, 15), radius_x=13)
        self.add_arc('e8-2', (40, 15), (43, 19), radius_x=10)
        self.add_line('e8-3', (43, 19), (44, 24))
        self.add_arc('e8-4', (44, 24), (31, 35), radius_x=12)
        self.add_contour('c0', 'e7', 'e0')
        self.add_contour('c1', 'e8-1', 'e8-2', 'e8-3', 'e8-4')
        self.add_contour('c2', 'e1', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c0', 'e6')
        self.relate('connect', 'c0', 'e5')
        self.relate('connect', 'c1', 'e5')
        self.relate('connect', 'c1', 'e4')
        self.relate('connect', 'c2', 'e4')
