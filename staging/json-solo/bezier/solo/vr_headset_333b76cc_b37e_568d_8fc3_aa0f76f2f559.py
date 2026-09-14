"""Vr headset (video-games), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '333b76cc-b37e-568d-8fc3-aa0f76f2f559'
SOURCE_PATH = 'icons-json/video-games/vr headset_333b76cc-b37e-568d-8fc3-aa0f76f2f559.json'
AUTHOR = 'json_to_solo'

class VrHeadset333b76cc(Solo48):
    icon_id = 'vr-headset-333b76cc'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('vr', 'headset', 'video-games')

    def build(self):
        self.add_line('e0', (13, 42), (13, 36))
        self.add_line('e1', (12, 33), (8, 29))
        self.add_line('e2', (22, 17), (6, 17))
        self.add_line('e3', (37, 23), (39, 30))
        self.add_line('e4', (39, 30), (35, 31))
        self.add_line('e5', (35, 31), (35, 35))
        self.add_line('e6', (28, 38), (28, 42))
        self.add_line('e7', (40, 23), (27, 23))
        self.add_line('e8', (27, 12), (40, 12))
        self.add_line('e9', (42, 13), (42, 22))
        self.add_bezier('e10', (35, 12), ((33.675, 10.904), (31.969, 9.379), (30.472, 8.512)), ((27.764, 6.941), (24.712, 6.008), (21.57, 6.008)), ((21.304, 6.008), (21.031, 6), (20.764, 6)), ((20.76, 6), (20.756, 6), (20.752, 6)), ((20.686, 6.008), (20.621, 6.008), (20.555, 6.016)), ((15.736, 6.016), (11.04, 8.905), (8.176, 12.627)), ((7.276, 13.814), (6.687, 15.057), (6.262, 16.489)), ((6.18, 16.775), (6, 17.16), (6, 17.455)), ((6, 17.725), (6, 17.73), (6, 18)))
        self.add_bezier('e11', (13, 36), ((13, 34.822), (12.695, 33.867), (12, 33)))
        self.add_bezier('e12', (8, 29), ((6.985, 27.732), (6, 24.687), (6, 23.043)), ((6, 21.455), (6, 19.587), (6, 18)))
        self.add_bezier('e13', (35, 35), ((35, 39.475), (30.913, 38.033), (28, 38)))
        self.add_bezier('e14', (27, 23), ((25.085, 23), (23.452, 22.077), (22.715, 20.187)), ((22.38, 19.32), (22.388, 18.371), (22.364, 17.455)), ((22.347, 16.685), (22.298, 15.892), (22.527, 15.147)), ((23.1, 13.249), (25.004, 12), (27, 12)))
        self.add_bezier('e15', (40, 12), ((40.916, 12), (41.28, 12.046), (41.812, 12.865)), ((41.935, 13.053), (41.91, 12.828), (42, 13)))
        self.add_bezier('e16', (42, 22), ((41.91, 22.172), (41.91, 21.897), (41.795, 22.061)), ((41.272, 22.781), (40.527, 22.846), (39.766, 23.075)), ((39.693, 23.108), (40.074, 22.967), (40, 23)))
        self.add_contour('c0', 'e10')
        self.add_contour('c1', 'e0', 'e11', 'e1', 'e12')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4', 'e5', 'e13', 'e6')
        self.add_contour('c4', 'e7', 'e14', 'e8', 'e15', 'e9', 'e16', closed=True)
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c3', 'c4')
