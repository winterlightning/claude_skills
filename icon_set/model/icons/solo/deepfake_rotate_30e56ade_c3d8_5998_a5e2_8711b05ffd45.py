"""Deepfake rotate (artificial-intelligence), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30e56ade-c3d8-5998-a5e2-8711b05ffd45'
SOURCE_PATH = 'icons-json/artificial-intelligence/deepfake rotate_30e56ade-c3d8-5998-a5e2-8711b05ffd45.json'
AUTHOR = 'json_to_solo'

class DeepfakeRotate(Solo48):
    icon_id = 'deepfake-rotate'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('deepfake', 'rotate', 'artificial-intelligence')

    def build(self):
        self.add_line('e0', (27, 9), (21, 4))
        self.add_line('e1', (27, 9), (21, 13))
        self.add_bezier('e2', (34, 12), ((36.745, 15.009), (38.863, 18.127), (39.646, 22.355)), ((39.798, 23.191), (39.992, 24.091), (39.992, 24.936)), ((39.992, 25.151), (40, 25.357), (40, 25.563)), ((40, 25.566), (40, 25.569), (40, 25.573)), ((40, 25.864), (39.992, 26.145), (39.992, 26.436)), ((39.992, 29), (39.335, 31.691), (38.316, 34)), ((36.168, 38.891), (31.899, 42.618), (26.981, 43.655)), ((26.265, 43.809), (25.491, 44), (24.766, 44)), ((24.762, 44), (24.757, 44), (24.753, 44)), ((24.471, 44), (24.198, 43.982), (23.916, 43.982)), ((15.149, 43.982), (8.008, 35.627), (8.008, 26.273)), ((8.008, 26.201), (8, 26.121), (8, 26.049)), ((8, 26.048), (8, 26.047), (8, 26.045)), ((8, 25.973), (8.008, 25.891), (8.008, 25.818)), ((8.008, 20.645), (9.909, 16.773), (13, 13)))
        self.add_bezier('e3', (38, 34), ((29.175, 33.282), (21.255, 28.736), (16.345, 20.618)), ((15.259, 18.836), (14.383, 16.9), (13.659, 14.909)), ((13.592, 14.727), (13.019, 13.164), (13.053, 13.091)), ((13.229, 12.682), (15.048, 11.373), (15.478, 11.073)), ((18.981, 8.6), (22.992, 9.191), (27, 9)))
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e0')
        self.add_contour('c3', 'e1')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c0')
