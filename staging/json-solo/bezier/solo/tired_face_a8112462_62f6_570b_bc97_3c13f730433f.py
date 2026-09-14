"""Tired face (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a8112462-62f6-570b-bc97-3c13f730433f'
SOURCE_PATH = 'icons-json/smileys/tired face_a8112462-62f6-570b-bc97-3c13f730433f.json'
AUTHOR = 'json_to_solo'

class TiredFaceSmileys(Solo48):
    icon_id = 'tired-face-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('tired', 'face', 'smileys')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e1', (29, 16), ((30.427, 19.064), (33.736, 19.8), (37, 20)))
        self.add_bezier('e2', (11, 20), ((14.373, 20.264), (16.6, 18.809), (18, 16)))
        self.add_bezier('e3', (29, 24), ((30.373, 27.055), (32.936, 27.891), (35, 25)))
        self.add_bezier('e4', (13, 25), ((13.255, 25.345), (13.527, 25.591), (13.864, 25.873)), ((15.318, 27.064), (17.464, 26.573), (18.664, 25.282)), ((19.027, 24.891), (18.755, 24.455), (19, 24)))
        self.add_bezier('e5', (18, 35), ((21.655, 31.473), (25.318, 31.536), (29, 35)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
