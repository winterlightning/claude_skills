"""Video (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '77cac2c6-9ef1-4a3f-85bf-963aeda09df3'
SOURCE_PATH = 'icons-json/symbol/video_77cac2c6-9ef1-4a3f-85bf-963aeda09df3.json'
AUTHOR = 'json_to_solo'

class Video77cac2c6(Solo48):
    icon_id = 'video-77cac2c6'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('video', 'symbol')

    def build(self):
        self.add_line('e0', (33, 26), (44, 34))
        self.add_line('e1', (44, 34), (44, 15))
        self.add_line('e2', (44, 15), (33, 23))
        self.add_line('e3', (9, 40), (31, 40))
        self.add_line('e4', (33, 35), (33, 12))
        self.add_line('e5', (29, 8), (8, 8))
        self.add_line('e6', (4, 13), (4, 36))
        self.add_bezier('e7', (4, 36), ((4.091, 36.246), (4.073, 36.837), (4.173, 37.083)), ((4.709, 38.375), (6.055, 40), (7.218, 40)), ((7.373, 39.988), (7.518, 39.988), (7.664, 39.975)), ((7.809, 39.988), (7.964, 39.988), (8.109, 40)), ((8.255, 40), (8.855, 40), (9, 40)))
        self.add_bezier('e8', (31, 40), ((31.191, 39.815), (31.664, 39.902), (31.836, 39.692)), ((32.8, 38.56), (33, 36.625), (33, 35)))
        self.add_bezier('e9', (33, 12), ((32.509, 10.08), (31.727, 8.025), (30.045, 8.025)), ((29.918, 8.012), (29.782, 8.012), (29.655, 8)), ((29.591, 8), (29.064, 8), (29, 8)))
        self.add_bezier('e10', (8, 8), ((6.255, 8), (4.009, 9.785), (4.009, 12.345)), ((4.009, 12.443), (4, 12.542), (4, 12.628)), ((4, 12.726), (4, 12.902), (4, 13)))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e7', 'e3', 'e8', 'e4', 'e9', 'e5', 'e10', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
