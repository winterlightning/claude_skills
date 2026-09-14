"""Curve rise dash large head (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('e3', (4, 13), (10, 12), radius_x=8)
        self.add_line('e4', (15, 15), (18, 20))
        self.add_arc('e5', (18, 26), (18, 32), radius_x=25, sweep=False)
        self.add_arc('e6', (37, 32), (38, 27), radius_x=20)
        self.add_line('e7', (20, 37), (25, 40))
        self.add_arc('e8', (29, 40), (34, 37), radius_x=7, sweep=False)
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
