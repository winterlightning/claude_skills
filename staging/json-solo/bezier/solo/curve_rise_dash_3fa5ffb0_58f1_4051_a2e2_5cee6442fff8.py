"""Curve rise dash (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e6', (4, 15), ((4, 14.977), (4.009, 14.823), (4.009, 14.8)), ((4.009, 13.886), (6.464, 11.583), (7, 11)))
        self.add_bezier('e7', (19, 11), ((19.809, 12.086), (20.555, 13.617), (21, 15)))
        self.add_bezier('e8', (38, 34), ((38.373, 32.983), (39, 32.143), (39, 31)))
        self.add_bezier('e9', (22, 31), ((22.164, 32.646), (22.455, 33.491), (23, 35)))
        self.add_bezier('e10', (27, 39), ((28.136, 39.491), (29.136, 39.989), (30.355, 39.989)), ((30.455, 39.989), (30.555, 40), (30.664, 40)), ((30.665, 40), (30.666, 40), (30.667, 40)), ((30.73, 40), (30.801, 40), (30.864, 39.989)), ((31.945, 39.989), (33.027, 39.526), (34, 39)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e6')
        self.add_contour('c2', 'e7')
        self.add_contour('c3', 'e1')
        self.add_contour('c4', 'e8', 'e2')
        self.add_contour('c5', 'e3')
        self.add_contour('c6', 'e4')
        self.add_contour('c7', 'e5')
        self.add_contour('c8', 'e9')
        self.add_contour('c9', 'e10')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
