"""Amazon lightsail (programing), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09e1b73f-4483-571c-9e3d-5bc2c49901b9'
SOURCE_PATH = 'icons-json/programing/amazon lightsail_09e1b73f-4483-571c-9e3d-5bc2c49901b9.json'
AUTHOR = 'json_to_solo'

class AmazonLightsailPrograming(Solo48):
    icon_id = 'amazon-lightsail-programing'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('amazon', 'lightsail', 'programing')

    def build(self):
        self.add_line('e0', (28, 35), (26, 38))
        self.add_arc('e1-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e1-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e2', (26, 38), ((24.836, 34.409), (23.909, 30.227), (21.064, 27.518)), ((19.727, 26.236), (18.1, 25.309), (16.491, 24.418)), ((16.082, 24.182), (15.082, 23.664), (15.082, 23.645)), ((15.182, 23.591), (15.273, 23.545), (15.373, 23.5)), ((15.945, 23.2), (16.509, 22.9), (17.082, 22.591)), ((19.118, 21.5), (20.945, 20.2), (22.464, 18.436)), ((23.973, 16.682), (24.909, 14.636), (25.618, 12.464)), ((25.818, 11.845), (26.018, 11.236), (26.209, 10.618)), ((26.245, 10.491), (26.291, 10.364), (26.327, 10.236)), ((26.327, 10.236), (26.773, 11.145), (27, 11.627)), ((27.7, 13.082), (28.464, 14.564), (28.936, 16.118)), ((30.536, 21.345), (30.555, 26.409), (28.936, 31.636)), ((28.582, 32.782), (28.673, 33.991), (28, 35)))
        self.add_contour('c0', 'e2', 'e0', closed=True)
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
