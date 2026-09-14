"""Curve rise large head (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dd13c23c-99cd-4dd8-932b-e39c965b1587'
SOURCE_PATH = 'icons-json/arrows/curve rise large head_dd13c23c-99cd-4dd8-932b-e39c965b1587.json'
AUTHOR = 'json_to_solo'

class CurveRiseLargeHeadArrows(Solo48):
    icon_id = 'curve-rise-large-head-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curve', 'rise', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (18, 17), (18, 30))
        self.add_line('e1', (37, 29), (37, 8))
        self.add_line('e2', (44, 18), (37, 8))
        self.add_line('e3', (29, 18), (37, 8))
        self.add_line('e4-1', (4, 10), (10, 8))
        self.add_line('e4-2', (10, 8), (14, 9))
        self.add_arc('e4-3', (14, 9), (16, 11), radius_x=6)
        self.add_line('e4-4', (16, 11), (18, 17))
        self.add_arc('e5-1', (18, 30), (27, 40), radius_x=10, sweep=False)
        self.add_arc('e5-2', (27, 40), (37, 29), radius_x=11, sweep=False)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e0', 'e5-1', 'e5-2', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
