"""Outdoors camp fire (outdoors), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e79029cc-1cc4-41cb-87c3-cb06d318b0ed'
SOURCE_PATH = 'icons-json/outdoors/outdoors camp fire_e79029cc-1cc4-41cb-87c3-cb06d318b0ed.json'
AUTHOR = 'json_to_solo'

class OutdoorsCampFireOutdoors(Solo48):
    icon_id = 'outdoors-camp-fire-outdoors'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('outdoors', 'camp', 'fire')

    def build(self):
        self.add_line('e0', (40, 35), (23, 39))
        self.add_line('e1', (23, 39), (8, 44))
        self.add_line('e2', (23, 39), (40, 44))
        self.add_line('e3', (8, 36), (23, 39))
        self.add_line('e4', (26, 4), (24, 5))
        self.add_bezier('e5', (23, 39), ((23.126, 38.991), (23.419, 39.436), (23.545, 39.427)), ((23.545, 39.373), (23.537, 39.318), (23.537, 39.264)), ((23.646, 39.3), (23.756, 39.345), (23.857, 39.382)), ((23.907, 39.409), (23.949, 38.973), (24, 39)))
        self.add_bezier('e6', (24, 5), ((21.112, 6.4), (18.888, 8.682), (17.137, 11.491)), ((15.276, 14.464), (13.903, 17.664), (13.305, 21.209)), ((12.994, 23.055), (13.238, 25.055), (13.811, 26.809)), ((15.394, 31.673), (19.562, 34.936), (24.286, 35.155)), ((30.526, 35.445), (36.286, 28.882), (35.537, 22.136)), ((35.192, 19.009), (33.752, 15.982), (31.798, 13.655)), ((31.394, 13.173), (30.173, 11.645), (30.063, 11.655)), ((29.996, 12.164), (29.928, 12.673), (29.861, 13.182)), ((29.861, 13.209), (29.853, 13.227), (29.853, 13.255)), ((29.709, 14.245), (29.28, 16.136), (28.446, 16.736)), ((27.503, 17.418), (26.038, 14.936), (25.718, 14.255)), ((24.051, 10.691), (24.821, 7.618), (26, 4)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e5')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e3')
        self.add_contour('c5', 'e6', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c3')
