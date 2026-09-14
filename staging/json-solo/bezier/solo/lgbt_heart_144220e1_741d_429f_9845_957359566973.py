"""Lgbt heart (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '144220e1-741d-429f-9845-957359566973'
SOURCE_PATH = 'icons-json/symbol/lgbt heart_144220e1-741d-429f-9845-957359566973.json'
AUTHOR = 'json_to_solo'

class LgbtHeartSymbol(Solo48):
    icon_id = 'lgbt-heart-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('lgbt', 'heart', 'symbol')

    def build(self):
        self.add_line('sym-e0', (39, 28), (9, 28))
        self.add_bezier('sym-e1', (9, 28), ((13.009, 31.882), (17.518, 35.589), (22, 39)))
        self.add_line('sym-e2', (22, 39), (24, 40))
        self.add_line('sym-e3', (24, 40), (26, 39))
        self.add_bezier('sym-e4', (26, 39), ((30.482, 35.589), (34.991, 31.882), (39, 28)))
        self.add_bezier('sym-e5', (39, 28), ((40.955, 26.105), (44, 22.762), (44, 20)))
        self.add_line('sym-e6', (44, 20), (4, 20))
        self.add_bezier('sym-e7', (4, 20), ((4, 22.762), (7.045, 26.105), (9, 28)))
        self.add_bezier('sym-e8', (44, 20), ((44, 19.107), (44, 17.893), (44, 17)))
        self.add_bezier('sym-e9', (44, 17), ((44, 12.166), (39.218, 8), (34, 8)))
        self.add_bezier('sym-e10', (34, 8), ((33.791, 8), (34.209, 8), (34, 8)))
        self.add_bezier('sym-e11', (34, 8), ((31.627, 8), (28.9, 8.712), (27, 10)))
        self.add_bezier('sym-e12', (27, 10), ((26.227, 10.522), (25.645, 11.36), (25, 12)))
        self.add_bezier('sym-e13', (25, 12), ((24.918, 12.076), (24.091, 13.008), (24, 13)))
        self.add_bezier('sym-e14', (24, 13), ((23.995, 13), (24.019, 13.015), (24, 13)))
        self.add_bezier('sym-e15', (24, 13), ((23.981, 13.015), (24.005, 13), (24, 13)))
        self.add_bezier('sym-e16', (24, 13), ((23.909, 13.008), (23.082, 12.076), (23, 12)))
        self.add_bezier('sym-e17', (23, 12), ((22.355, 11.36), (21.773, 10.522), (21, 10)))
        self.add_bezier('sym-e18', (21, 10), ((19.1, 8.712), (16.373, 8), (14, 8)))
        self.add_bezier('sym-e19', (14, 8), ((13.791, 8), (14.209, 8), (14, 8)))
        self.add_bezier('sym-e20', (14, 8), ((8.782, 8), (4, 12.166), (4, 17)))
        self.add_bezier('sym-e21', (4, 17), ((4, 17.893), (4, 19.107), (4, 20)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c1', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
