"""Tired face (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('e1', (29, 16), (37, 20), radius_x=8, sweep=False)
        self.add_arc('e2', (11, 20), (18, 16), radius_x=7, sweep=False)
        self.add_arc('e3-1', (29, 24), (32, 27), radius_x=4, sweep=False)
        self.add_line('e3-2', (32, 27), (35, 25))
        self.add_arc('e4', (13, 25), (19, 24), radius_x=4, sweep=False)
        self.add_arc('e5', (18, 35), (29, 35), radius_x=7)
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3-1', 'e3-2')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
