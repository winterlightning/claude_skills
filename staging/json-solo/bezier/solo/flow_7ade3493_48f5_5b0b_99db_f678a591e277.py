"""Flow (diagrams), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7ade3493-48f5-5b0b-99db-f678a591e277'
SOURCE_PATH = 'icons-json/diagrams/flow_7ade3493-48f5-5b0b-99db-f678a591e277.json'
AUTHOR = 'json_to_solo'

class FlowDiagrams(Solo48):
    icon_id = 'flow-diagrams'
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
        self.add_bezier('e7', (13, 11), ((13.3, 11.278), (13.7, 11.722), (14, 12)))
        self.add_bezier('e8', (31, 12), ((38.064, 11.528), (43.991, 16.775), (43.991, 23.343)), ((43.991, 23.476), (44, 23.608), (44, 23.741)), ((44, 23.743), (44, 23.745), (44, 23.747)), ((44, 23.941), (43.991, 24.143), (43.991, 24.337)), ((43.991, 25.701), (43.5, 27.242), (42.891, 28.472)), ((40.755, 32.724), (36, 35.143), (31, 35)))
        self.add_contour('c0', 'e7', 'e0')
        self.add_contour('c1', 'e8')
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
