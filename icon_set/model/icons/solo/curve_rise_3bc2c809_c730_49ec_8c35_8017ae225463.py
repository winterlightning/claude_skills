"""Curve rise (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3bc2c809-c730-49ec-8c35-8017ae225463'
SOURCE_PATH = 'icons-json/arrows/curve rise_3bc2c809-c730-49ec-8c35-8017ae225463.json'
AUTHOR = 'json_to_solo'

class CurveRise(Solo48):
    icon_id = 'curve-rise'
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
        self.add_bezier('e4', (4, 23), ((4, 21.646), (4.009, 20.049), (4.009, 18.695)), ((4.009, 12.825), (7.491, 8.025), (11.882, 8.025)), ((12.018, 8.012), (12.145, 8.012), (12.282, 8)), ((12.286, 8), (12.29, 8), (12.294, 8)), ((12.554, 8), (12.813, 8.025), (13.073, 8.025)), ((16.664, 8.025), (20.136, 11.68), (21.036, 16.332)), ((21.127, 16.8), (21, 17.52), (21, 18)))
        self.add_bezier('e5', (21, 29), ((21, 35.08), (24.909, 39.988), (29.382, 39.988)), ((29.444, 39.988), (29.516, 40), (29.579, 40)), ((29.58, 40), (29.581, 40), (29.582, 40)), ((29.782, 40), (29.973, 39.988), (30.173, 39.988)), ((34.027, 39.988), (37.273, 36.16), (38.236, 31.225)), ((38.373, 30.511), (39, 29.751), (39, 29)))
        self.add_contour('c0', 'e4', 'e0', 'e5', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
