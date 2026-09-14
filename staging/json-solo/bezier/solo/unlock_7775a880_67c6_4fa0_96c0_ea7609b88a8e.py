"""Unlock (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7775a880-67c6-4fa0-96c0-ea7609b88a8e'
SOURCE_PATH = 'icons-json/symbol/unlock_7775a880-67c6-4fa0-96c0-ea7609b88a8e.json'
AUTHOR = 'json_to_solo'

class Unlock7775a880(Solo48):
    icon_id = 'unlock-7775a880'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('unlock', 'symbol')

    def build(self):
        self.add_line('e0', (27, 14), (27, 22))
        self.add_line('e1', (17, 25), (17, 39))
        self.add_line('e2', (22, 44), (36, 44))
        self.add_line('e3', (40, 40), (40, 25))
        self.add_line('e4', (37, 22), (21, 22))
        self.add_bezier('e5', (8, 19), ((8, 18.936), (8.008, 18.427), (8.008, 18.364)), ((8.008, 17.445), (8.017, 16.527), (8.017, 15.618)), ((8.017, 15.3), (8, 14.991), (8, 14.682)), ((8, 14.373), (8.017, 14.055), (8.017, 13.745)), ((8.017, 8.836), (11.924, 4.009), (16.615, 4.009)), ((16.747, 4.009), (16.88, 4), (17.013, 4)), ((17.015, 4), (17.017, 4), (17.019, 4)), ((17.145, 4), (17.28, 4.009), (17.415, 4.009)), ((22.131, 4.009), (27, 8.973), (27, 14)))
        self.add_bezier('e6', (21, 22), ((19.114, 22), (17.547, 23.073), (17, 25)))
        self.add_bezier('e7', (17, 39), ((17, 41.309), (19.411, 43.991), (21.549, 43.991)), ((21.676, 43.991), (21.811, 44), (21.937, 44)), ((22.063, 44), (21.874, 44), (22, 44)))
        self.add_bezier('e8', (36, 44), ((36.118, 44), (36.017, 43.991), (36.135, 43.991)), ((37.886, 43.991), (40, 42.091), (40, 40)))
        self.add_bezier('e9', (40, 25), ((40, 24.8), (39.983, 24.509), (39.983, 24.318)), ((39.983, 23.027), (38.796, 22.227), (37.735, 22.118)), ((37.356, 22.082), (37.371, 22), (37, 22)))
        self.add_contour('c0', 'e5', 'e0')
        self.add_contour('c1', 'e6', 'e1', 'e7', 'e2', 'e8', 'e3', 'e9', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
