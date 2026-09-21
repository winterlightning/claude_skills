"""Ga (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c229905f-b32a-434c-b3d8-e60a3dab6312'
SOURCE_PATH = 'icons-json/symbol/ga (text u)_c229905f-b32a-434c-b3d8-e60a3dab6312.json'
AUTHOR = 'json_to_solo'

class GaTextU(Solo48):
    icon_id = 'ga-text-u'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('ga', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (21, 19), (21, 16))
        self.add_line('e1', (21, 16), (16, 16))
        self.add_line('e2', (40, 27), (40, 23))
        self.add_line('e3', (8, 44), (40, 44))
        self.add_bezier('e4', (21, 8), ((20.057, 5.836), (18.088, 4.018), (15.739, 4.018)), ((15.613, 4.009), (15.486, 4.009), (15.36, 4)), ((15.358, 4), (15.356, 4), (15.354, 4)), ((15.221, 4), (15.08, 4.009), (14.947, 4.009)), ((14.122, 4.009), (13.331, 4.255), (12.564, 4.555)), ((8.682, 6.082), (8.008, 10.855), (8.008, 14.773)), ((8.008, 15.018), (8, 15.255), (8, 15.5)), ((8, 15.945), (8.017, 16.4), (8.017, 16.855)), ((8.017, 19.636), (8.632, 22.891), (10.695, 24.764)), ((13.634, 27.427), (18.476, 26.9), (20.488, 23.236)), ((21.272, 21.8), (21, 20.636), (21, 19)))
        self.add_bezier('e5', (40, 23), ((40, 23), (40, 23.1), (39.992, 23.1)), ((39.992, 23.373), (39.208, 24.345), (39.04, 24.545)), ((37.844, 26), (36.269, 26.673), (34.493, 26.491)), ((30.973, 26.127), (29.171, 23.5), (29.145, 19.755)), ((29.128, 16.627), (30.712, 13.427), (33.541, 12.364)), ((36.135, 11.4), (39.992, 13.691), (39.992, 16.755)), ((39.992, 16.836), (40, 16.918), (40, 16.991)), ((40, 19.027), (40, 20.964), (40, 23)))
        self.add_contour('c0', 'e4', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e5', closed=True)
