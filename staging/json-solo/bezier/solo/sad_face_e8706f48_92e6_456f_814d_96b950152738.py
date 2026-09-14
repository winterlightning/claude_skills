"""Sad face (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8706f48-92e6-456f-814d-96b950152738'
SOURCE_PATH = 'icons-json/smileys/sad face_e8706f48-92e6-456f-814d-96b950152738.json'
AUTHOR = 'json_to_solo'

class SadFace(Solo48):
    icon_id = 'sad-face'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('sad', 'face', 'smileys')

    def build(self):
        self.add_line('sym-e0', (42, 21), (38, 21))
        self.add_line('sym-e1', (38, 21), (10, 21))
        self.add_line('sym-e2', (10, 21), (6, 21))
        self.add_line('sym-e3', (38, 21), (35, 10))
        self.add_bezier('sym-e4', (35, 10), ((34.239, 7.529), (31.585, 6), (29, 6)))
        self.add_line('sym-e5', (29, 6), (24, 6))
        self.add_line('sym-e6', (24, 6), (19, 6))
        self.add_bezier('sym-e7', (19, 6), ((16.415, 6), (13.761, 7.529), (13, 10)))
        self.add_line('sym-e8', (13, 10), (10, 21))
        self.add_line('sym-e9', (33, 31), (33, 27))
        self.add_bezier('sym-e10', (24, 35), ((28.537, 35), (32.573, 37.858), (35, 42)))
        self.add_line('sym-e11', (15, 31), (15, 27))
        self.add_bezier('sym-e12', (24, 35), ((19.463, 35), (15.427, 37.858), (13, 42)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8')
        self.add_contour('sym-c2', 'sym-e9')
        self.add_contour('sym-c3', 'sym-e10')
        self.add_contour('sym-c4', 'sym-e11')
        self.add_contour('sym-c5', 'sym-e12')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c3', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
