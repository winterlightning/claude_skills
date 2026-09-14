"""Face (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e79d0d3c-9833-42da-b29a-025ab29b3d7b'
SOURCE_PATH = 'icons-json/symbol/face_e79d0d3c-9833-42da-b29a-025ab29b3d7b.json'
AUTHOR = 'json_to_solo'

class FaceSymbol(Solo48):
    icon_id = 'face-symbol'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('face', 'symbol')

    def build(self):
        self.add_line('e0', (9, 20), (5, 20))
        self.add_arc('e1-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e1-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e2', (43, 19), ((38.136, 18.973), (35.545, 20.791), (30.909, 17.936)), ((28.936, 16.718), (27.309, 15.318), (25.827, 13.555)), ((25.645, 13.327), (24.127, 11.464), (24.127, 11.464)), ((24.055, 11.455), (23.436, 12.245), (23.209, 12.5)), ((22.255, 13.545), (21.3, 14.573), (20.255, 15.518)), ((18.009, 17.527), (12.036, 20), (9, 20)))
        self.add_contour('c0', 'e2', 'e0')
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
        self.relate('connect', 'c0', 'e1')
        self.relate('connect', 'c0', 'e1')
