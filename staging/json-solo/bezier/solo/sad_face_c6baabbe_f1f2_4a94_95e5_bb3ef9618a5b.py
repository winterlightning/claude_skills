"""Sad face (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c6baabbe-f1f2-4a94-95e5-bb3ef9618a5b'
SOURCE_PATH = 'icons-json/smileys/sad face_c6baabbe-f1f2-4a94-95e5-bb3ef9618a5b.json'
AUTHOR = 'json_to_solo'

class SadFace(Solo48):
    icon_id = 'sad-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('sad', 'face', 'smileys')

    def build(self):
        self.add_line('e0', (19, 20), (19, 16))
        self.add_line('e1', (29, 20), (29, 16))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e3', (13, 32), ((14.355, 29.9), (16.064, 28.191), (18.291, 26.964)), ((22.827, 24.445), (28.573, 25.4), (32.309, 28.909)), ((33.336, 29.882), (34.227, 30.827), (35, 32)))
        self.add_contour('c0', 'e3')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
