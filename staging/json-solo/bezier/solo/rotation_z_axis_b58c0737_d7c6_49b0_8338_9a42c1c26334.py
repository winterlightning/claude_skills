"""Rotation z axis (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b58c0737-d7c6-49b0-8338-9a42c1c26334'
SOURCE_PATH = 'icons-json/arrows/rotation z axis_b58c0737-d7c6-49b0-8338-9a42c1c26334.json'
AUTHOR = 'json_to_solo'

class RotationZAxisArrows(Solo48):
    icon_id = 'rotation-z-axis-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('rotation', 'z', 'axis', 'arrows')

    def build(self):
        self.add_line('e0', (9, 13), (8, 14))
        self.add_line('e1', (8, 14), (13, 14))
        self.add_line('e2', (8, 8), (8, 14))
        self.add_arc('e3-top', (20, 24), (28, 24), radius_x=4)
        self.add_arc('e3-bottom', (28, 24), (20, 24), radius_x=4)
        self.add_bezier('e4', (6, 22), ((6, 22.794), (6.016, 23.959), (6.016, 24.753)), ((6.016, 24.818), (6.016, 24.892), (6.016, 24.957)), ((6.016, 26.438), (6.376, 27.976), (6.835, 29.375)), ((9.109, 36.355), (15.884, 41.992), (23.411, 41.992)), ((23.508, 41.992), (23.604, 42), (23.701, 42)), ((23.702, 42), (23.704, 42), (23.705, 42)), ((24.008, 42), (24.319, 41.992), (24.622, 41.992)), ((33.785, 41.992), (41.992, 33.695), (41.992, 24.548)), ((41.992, 24.452), (42, 24.347), (42, 24.25)), ((42, 24.249), (42, 24.247), (42, 24.245)), ((42, 23.902), (41.992, 23.566), (41.992, 23.223)), ((41.992, 15.646), (36.747, 9.428), (29.817, 6.933)), ((28.263, 6.376), (26.495, 6.008), (24.843, 6.008)), ((24.714, 6.008), (24.585, 6), (24.456, 6)), ((24.454, 6), (24.452, 6), (24.45, 6)), ((24.188, 6), (23.935, 6.008), (23.673, 6.008)), ((17.962, 6.008), (12.559, 8.672), (9, 13)))
        self.add_contour('c0', 'e4', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
