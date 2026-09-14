"""Sad face (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
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
        self.add_line('sym-e4-1', (35, 10), (32, 7))
        self.add_arc('sym-e4-2', (32, 7), (29, 6), radius_x=6, sweep=False)
        self.add_line('sym-e5', (29, 6), (24, 6))
        self.add_line('sym-e6', (24, 6), (19, 6))
        self.add_arc('sym-e7-1', (19, 6), (16, 7), radius_x=6, sweep=False)
        self.add_line('sym-e7-2', (16, 7), (13, 10))
        self.add_line('sym-e8', (13, 10), (10, 21))
        self.add_line('sym-e9', (33, 31), (33, 27))
        self.add_arc('sym-e10', (24, 35), (35, 42), radius_x=13)
        self.add_line('sym-e11', (15, 31), (15, 27))
        self.add_arc('sym-e12', (24, 35), (13, 42), radius_x=14, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4-1', 'sym-e4-2', 'sym-e5', 'sym-e6', 'sym-e7-1', 'sym-e7-2', 'sym-e8')
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
