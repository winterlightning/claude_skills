"""Badge star 2 (protection), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e9c2606-3dd8-5da8-9c75-2314a86e8c6e'
SOURCE_PATH = 'icons-json/protection/badge star 2_8e9c2606-3dd8-5da8-9c75-2314a86e8c6e.json'
AUTHOR = 'json_to_solo'

class BadgeStar2Protection(Solo48):
    icon_id = 'badge-star-2-protection'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('badge', 'star', 'protection')

    def build(self):
        self.add_line('e0', (24, 4), (21, 7))
        self.add_line('e1', (8, 12), (8, 23))
        self.add_line('e2', (40, 23), (40, 11))
        self.add_line('e3', (39, 9), (34, 9))
        self.add_line('e4', (27, 20), (24, 13))
        self.add_line('e5', (24, 13), (21, 20))
        self.add_line('e6', (21, 20), (14, 20))
        self.add_line('e7', (14, 20), (20, 25))
        self.add_line('e8', (20, 25), (18, 32))
        self.add_line('e9', (18, 32), (24, 28))
        self.add_line('e10', (24, 28), (30, 32))
        self.add_line('e11', (30, 32), (28, 25))
        self.add_line('e12', (28, 25), (34, 20))
        self.add_line('e13', (34, 20), (27, 20))
        self.add_bezier('e14', (21, 7), ((20.192, 7.655), (18.762, 7.673), (17.811, 7.991)), ((15.663, 8.709), (13.566, 9.155), (11.318, 9.336)), ((9.794, 9.455), (8.017, 9.309), (8.017, 11.555)), ((8.008, 11.627), (8.008, 11.691), (8, 11.764)), ((8, 11.9), (8, 11.864), (8, 12)))
        self.add_bezier('e15', (8, 23), ((8.008, 23.145), (8.008, 23.382), (8.017, 23.527)), ((8.017, 24.391), (8.202, 25.318), (8.345, 26.173)), ((9.465, 32.618), (13.785, 37.709), (18.804, 41.1)), ((19.865, 41.818), (22.863, 44), (24.059, 44)), ((24.059, 44), (24.06, 44), (24.06, 44)), ((24.085, 44), (24.11, 43.991), (24.135, 43.982)), ((25.12, 43.982), (28.404, 41.682), (29.398, 40.991)), ((35.006, 37.073), (39.983, 30.936), (39.983, 23.309)), ((39.992, 23.236), (39.992, 23.073), (40, 23)))
        self.add_bezier('e16', (40, 11), ((40, 10.9), (40, 11.082), (39.992, 10.982)), ((39.992, 10.264), (39.421, 9.464), (39, 9)))
        self.add_bezier('e17', (34, 9), ((31.861, 8.618), (29.735, 7.391), (27.865, 6.2)), ((27.225, 5.782), (25.019, 4), (24.497, 4)), ((24.328, 4), (24.168, 4), (24, 4)))
        self.add_contour('c0', 'e0', 'e14', 'e1', 'e15', 'e2', 'e16', 'e3', 'e17', closed=True)
        self.add_contour('c1', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11', 'e12', 'e13', closed=True)
