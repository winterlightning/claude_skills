"""Sad face (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '90663cc1-f016-4199-8cee-55a05f0d5515'
SOURCE_PATH = 'icons-json/smileys/sad face_90663cc1-f016-4199-8cee-55a05f0d5515.json'
AUTHOR = 'json_to_solo'

class SadFace90663cc1(Solo48):
    icon_id = 'sad-face-90663cc1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('sad', 'face', 'smileys')

    def build(self):
        self.add_line('sym-e0', (8, 8), (8, 16))
        self.add_bezier('sym-e1', (4, 40), ((7.634, 32.336), (15.212, 27), (24, 27)))
        self.add_bezier('sym-e2', (24, 27), ((24.041, 27), (23.959, 27), (24, 27)))
        self.add_bezier('sym-e3', (24, 27), ((24.041, 27), (23.959, 27), (24, 27)))
        self.add_bezier('sym-e4', (24, 27), ((32.788, 27), (40.366, 32.336), (44, 40)))
        self.add_line('sym-e5', (40, 8), (40, 16))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c2', 'sym-e5')
