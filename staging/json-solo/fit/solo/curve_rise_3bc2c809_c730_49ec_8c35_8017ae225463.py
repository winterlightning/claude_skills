"""Curve rise (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3bc2c809-c730-49ec-8c35-8017ae225463'
SOURCE_PATH = 'icons-json/arrows/curve rise_3bc2c809-c730-49ec-8c35-8017ae225463.json'
AUTHOR = 'json_to_solo'

class CurveRiseArrows(Solo48):
    icon_id = 'curve-rise-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curve', 'rise', 'arrows')

    def build(self):
        self.add_line('e0', (21, 18), (21, 29))
        self.add_line('e1', (39, 29), (39, 13))
        self.add_line('e2', (44, 20), (39, 13))
        self.add_line('e3', (33, 20), (39, 13))
        self.add_line('e4-1', (4, 23), (5, 13))
        self.add_arc('e4-2', (5, 13), (12, 8), radius_x=8)
        self.add_arc('e4-3', (12, 8), (21, 18), radius_x=10)
        self.add_arc('e5-1', (21, 29), (30, 40), radius_x=10, sweep=False)
        self.add_arc('e5-2', (30, 40), (39, 29), radius_x=11, sweep=False)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e0', 'e5-1', 'e5-2', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
