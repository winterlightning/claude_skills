"""Camera (photography), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8b077ef0-ba0d-405b-8332-a61869ec5707'
SOURCE_PATH = 'icons-json/photography/camera_8b077ef0-ba0d-405b-8332-a61869ec5707.json'
AUTHOR = 'json_to_solo'

class Camera(Solo48):
    icon_id = 'camera'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('camera', 'photography')

    def build(self):
        self.add_line('e0', (18, 8), (30, 8))
        self.add_line('e1', (30, 8), (34, 14))
        self.add_line('e2', (34, 14), (39, 14))
        self.add_line('e3', (44, 21), (44, 35))
        self.add_line('e4', (38, 40), (9, 40))
        self.add_line('e5', (4, 35), (4, 19))
        self.add_line('e6', (14, 14), (18, 8))
        self.add_bezier('e7', (39, 14), ((42.045, 14), (43.982, 16.935), (43.982, 19.326)), ((43.982, 19.571), (44, 19.823), (44, 20.067)), ((44, 20.253), (44, 20.815), (44, 21)))
        self.add_bezier('e8', (44, 35), ((44, 35.143), (43.982, 35.234), (43.982, 35.377)), ((43.982, 37.339), (42.345, 39.469), (40.245, 39.899)), ((39.691, 40), (39.036, 39.992), (38.473, 39.992)), ((38.191, 39.992), (38.282, 40), (38, 40)))
        self.add_bezier('e9', (9, 40), ((8.936, 40), (8.418, 39.992), (8.345, 39.992)), ((5.773, 39.992), (4.009, 37.347), (4.009, 35.166)), ((4.009, 35.091), (4, 35.076), (4, 35)))
        self.add_bezier('e10', (4, 19), ((4, 18.924), (4.009, 18.796), (4.009, 18.72)), ((4.009, 17.701), (4.364, 16.733), (4.945, 15.882)), ((6.355, 13.853), (8.136, 13.928), (10.482, 13.954)), ((11.655, 13.971), (12.827, 14.051), (14, 14)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e7', 'e3', 'e8', 'e4', 'e9', 'e5', 'e10', 'e6', closed=True)
