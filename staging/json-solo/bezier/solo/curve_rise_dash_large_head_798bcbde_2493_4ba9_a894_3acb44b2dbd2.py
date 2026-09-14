"""Curve rise dash large head (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '798bcbde-2493-4ba9-a894-3acb44b2dbd2'
SOURCE_PATH = 'icons-json/arrows/curve rise dash large head_798bcbde-2493-4ba9-a894-3acb44b2dbd2.json'
AUTHOR = 'json_to_solo'

class CurveRiseDashLargeHeadArrows(Solo48):
    icon_id = 'curve-rise-dash-large-head-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curve', 'rise', 'dash', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (31, 16), (38, 8))
        self.add_line('e1', (38, 21), (38, 8))
        self.add_line('e2', (44, 15), (38, 8))
        self.add_bezier('e3', (4, 13), ((6.136, 11.86), (7.627, 11.48), (10, 12)))
        self.add_bezier('e4', (15, 15), ((16.291, 16.52), (17.591, 17.95), (18, 20)))
        self.add_bezier('e5', (18, 26), ((17.864, 28.04), (17.691, 29.98), (18, 32)))
        self.add_bezier('e6', (37, 32), ((37.518, 30.34), (37.9, 28.75), (38, 27)))
        self.add_bezier('e7', (20, 37), ((21.373, 38.48), (23.164, 39.39), (25, 40)))
        self.add_bezier('e8', (29, 40), ((29.018, 40), (29.482, 39.99), (29.5, 39.99)), ((30.945, 39.99), (32.936, 37.94), (34, 37)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7')
        self.add_contour('c8', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
