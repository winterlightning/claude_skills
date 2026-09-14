"""Circle smiley face (state), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '26f40b93-a3b7-419f-a55b-3b6e5693c80a'
SOURCE_PATH = 'icons-json/state/circle smiley face_26f40b93-a3b7-419f-a55b-3b6e5693c80a.json'
AUTHOR = 'json_to_solo'

class CircleSmileyFaceState(Solo48):
    icon_id = 'circle-smiley-face-state'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('circle', 'smiley', 'face', 'state')

    def build(self):
        self.add_line('e0', (18, 18), (18, 21))
        self.add_line('e1', (30, 18), (30, 21))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e3', (15, 30), ((20.355, 35.245), (27.618, 35.182), (33, 30)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e3')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
