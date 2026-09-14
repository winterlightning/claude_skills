"""Earth (maps), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1faa3a74-7dec-436a-b945-ba1bb83aadd7'
SOURCE_PATH = 'icons-json/maps/earth_1faa3a74-7dec-436a-b945-ba1bb83aadd7.json'
AUTHOR = 'json_to_solo'

class Earth1faa3a74(Solo48):
    icon_id = 'earth-1faa3a74'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('earth', 'maps')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e1', (10, 38), ((13.609, 36.655), (18.727, 36.755), (20.818, 33.009)), ((21.655, 31.5), (22.3, 29.536), (20.909, 28.118)), ((18.909, 26.073), (15.118, 27.936), (13.309, 24.818)), ((11.591, 21.864), (14.927, 19.755), (15.3, 17.173)), ((15.864, 13.382), (9.055, 14.127), (7, 14)))
        self.add_bezier('e2', (43, 29), ((40.591, 28.582), (38.255, 28.982), (35.945, 28.073)), ((35.473, 27.891), (33.918, 27.055), (33.691, 26.627)), ((33.064, 25.391), (34.191, 22.436), (32.891, 21.336)), ((32.518, 21.155), (32.155, 20.964), (31.782, 20.782)), ((30.273, 20.045), (28.391, 20.036), (27.245, 18.664)), ((26.209, 17.409), (26.673, 15.564), (27.309, 14.255)), ((29.327, 10.091), (34.009, 10.345), (38, 10)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
        self.relate('connect', 'c0', 'e0')
        self.relate('connect', 'c0', 'e0')
        self.relate('connect', 'c1', 'e0')
        self.relate('connect', 'c1', 'e0')
