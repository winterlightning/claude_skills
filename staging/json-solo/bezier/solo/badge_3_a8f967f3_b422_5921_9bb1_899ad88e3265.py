"""Badge 3 (protection), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a8f967f3-b422-5921-9bb1-899ad88e3265'
SOURCE_PATH = 'icons-json/protection/badge 3_a8f967f3-b422-5921-9bb1-899ad88e3265.json'
AUTHOR = 'json_to_solo'

class Badge3Protection(Solo48):
    icon_id = 'badge-3-protection'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('badge', 'protection')

    def build(self):
        self.add_line('e0', (15, 18), (15, 13))
        self.add_line('e1', (33, 13), (33, 20))
        self.add_line('e2', (33, 19), (44, 19))
        self.add_line('e3', (38, 28), (32, 28))
        self.add_line('e4', (15, 19), (4, 19))
        self.add_line('e5', (11, 28), (16, 28))
        self.add_bezier('e6', (16, 29), ((16, 28.988), (15.827, 27.742), (15.818, 27.692)), ((15.718, 26.745), (15.318, 25.785), (15.164, 24.837)), ((14.855, 22.991), (14.9, 20.948), (14.909, 19.077)), ((14.909, 18.88), (14.918, 18.671), (14.918, 18.474)), ((14.918, 18.265), (15, 18.209), (15, 18)))
        self.add_bezier('e7', (15, 13), ((15.227, 12.742), (15.282, 12.271), (15.545, 12.062)), ((16.855, 11.015), (22.409, 8.012), (23.882, 8.012)), ((23.936, 8), (23.989, 8), (24.043, 8)), ((24.044, 8), (24.045, 8), (24.045, 8)), ((24.136, 8), (24.236, 8.012), (24.327, 8.012)), ((25.3, 8.012), (26.818, 9.083), (27.673, 9.588)), ((29.491, 10.646), (31.245, 11.745), (33, 13)))
        self.add_bezier('e8', (33, 20), ((33, 22.609), (32.836, 25.255), (32.182, 27.692)), ((31.091, 31.729), (28.918, 35.36), (26.409, 37.945)), ((25.936, 38.425), (24.364, 40), (24, 40)), ((23.993, 40), (23.986, 40), (23.978, 40)), ((23.497, 40), (21.966, 38.431), (21.545, 38.031)), ((19.073, 35.631), (17.418, 32.618), (16, 29)))
        self.add_bezier('e9', (44, 19), ((42.945, 22.372), (41.236, 28), (38, 28)))
        self.add_bezier('e10', (4, 19), ((5.073, 23.997), (6.991, 28), (11, 28)))
        self.add_contour('c0', 'e6', 'e0', 'e7', 'e1', 'e8')
        self.add_contour('c1', 'e2', 'e9', 'e3')
        self.add_contour('c2', 'e4', 'e10', 'e5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c2', 'c0')
