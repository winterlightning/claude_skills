"""Curve rise dash (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3fa5ffb0-58f1-4051-a2e2-5cee6442fff8'
SOURCE_PATH = 'icons-json/arrows/curve rise dash_3fa5ffb0-58f1-4051-a2e2-5cee6442fff8.json'
AUTHOR = 'json_to_solo'

class CurveRiseDashArrows(Solo48):
    icon_id = 'curve-rise-dash-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curve', 'rise', 'dash', 'arrows')

    def build(self):
        self.add_line('e0', (11, 8), (15, 8))
        self.add_line('e1', (33, 22), (39, 15))
        self.add_line('e2', (39, 31), (39, 15))
        self.add_line('e3', (44, 22), (39, 15))
        self.add_line('e4', (4, 21), (4, 25))
        self.add_line('e5', (22, 21), (22, 25))
        self.add_line('e6', (4, 15), (7, 11))
        self.add_line('e7', (19, 11), (21, 15))
        self.add_line('e8', (38, 34), (39, 31))
        self.add_arc('e9', (22, 31), (23, 35), radius_x=17, sweep=False)
        self.add_line('e10-1', (27, 39), (31, 40))
        self.add_line('e10-2', (31, 40), (34, 39))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e6')
        self.add_contour('c2', 'e7')
        self.add_contour('c3', 'e1')
        self.add_contour('c4', 'e8', 'e2')
        self.add_contour('c5', 'e3')
        self.add_contour('c6', 'e4')
        self.add_contour('c7', 'e5')
        self.add_contour('c8', 'e9')
        self.add_contour('c9', 'e10-1', 'e10-2')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
