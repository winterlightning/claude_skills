"""Meeting camera (office), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b66459c5-1f15-5c48-9f19-7850e99d58b3'
SOURCE_PATH = 'icons-json/office/meeting camera_b66459c5-1f15-5c48-9f19-7850e99d58b3.json'
AUTHOR = 'json_to_solo'

class MeetingCameraOffice(Solo48):
    icon_id = 'meeting-camera-office'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('meeting', 'camera', 'office')

    def build(self):
        self.add_line('e0', (32, 30), (42, 38))
        self.add_line('e1', (44, 35), (44, 13))
        self.add_line('e2', (42, 12), (32, 19))
        self.add_line('e3', (32, 19), (32, 13))
        self.add_line('e4', (27, 8), (9, 8))
        self.add_line('e5', (4, 14), (4, 34))
        self.add_line('e6', (10, 40), (28, 40))
        self.add_line('e7', (32, 31), (32, 19))
        self.add_bezier('e8', (42, 38), ((42.564, 37.877), (43.982, 37.329), (43.982, 36.16)), ((43.982, 35.938), (44, 35.717), (44, 35.508)), ((44, 35.36), (44, 35.148), (44, 35)))
        self.add_bezier('e9', (44, 13), ((43.909, 12.852), (43.891, 12.529), (43.8, 12.369)), ((43.318, 11.557), (42.655, 12.049), (42, 12)))
        self.add_bezier('e10', (32, 13), ((32, 10.662), (30.473, 8), (28.691, 8)), ((28.036, 8), (27.655, 8), (27, 8)))
        self.add_bezier('e11', (9, 8), ((8.709, 8), (7.973, 8.025), (7.682, 8.025)), ((6.145, 8.025), (4, 9.883), (4, 12.209)), ((4, 12.295), (4, 12.382), (4, 12.468)), ((4, 12.566), (4.009, 12.652), (4.009, 12.751)), ((4.009, 12.935), (4.009, 13.12), (4.009, 13.305)), ((4, 13.403), (4, 13.489), (4, 13.588)), ((4, 13.772), (4, 13.815), (4, 14)))
        self.add_bezier('e12', (4, 34), ((4.009, 34.185), (4.009, 34.215), (4.018, 34.4)), ((4.018, 38.289), (7.509, 39.988), (9.864, 39.988)), ((10.027, 39.988), (9.836, 40), (10, 40)))
        self.add_bezier('e13', (28, 40), ((28.145, 39.988), (27.936, 39.988), (28.082, 39.975)), ((29.964, 39.975), (31.764, 37.502), (32.109, 35.102)), ((32.291, 33.908), (32, 32.206), (32, 31)))
        self.add_contour('c0', 'e0', 'e8', 'e1', 'e9', 'e2', 'e3', 'e10', 'e4', 'e11', 'e5', 'e12', 'e6', 'e13', 'e7')
