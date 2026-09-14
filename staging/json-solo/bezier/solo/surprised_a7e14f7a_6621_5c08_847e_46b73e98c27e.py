"""Surprised (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a7e14f7a-6621-5c08-847e-46b73e98c27e'
SOURCE_PATH = 'icons-json/smileys/surprised_a7e14f7a-6621-5c08-847e-46b73e98c27e.json'
AUTHOR = 'json_to_solo'

class SurprisedSmileys(Solo48):
    icon_id = 'surprised-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('surprised', 'smileys')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e1-top', (14, 19), (20, 19), radius_x=3)
        self.add_arc('e1-bottom', (20, 19), (14, 19), radius_x=3)
        self.add_arc('e2-top', (28, 19), (34, 19), radius_x=3)
        self.add_arc('e2-bottom', (34, 19), (28, 19), radius_x=3)
        self.add_bezier('e3', (26, 37), ((25.473, 37.136), (24.764, 37.064), (24.209, 37.082)), ((18.409, 37.327), (17.291, 27.936), (21.991, 25.555)), ((25.464, 23.791), (28.673, 26.682), (29.191, 30.091)), ((29.636, 33.045), (28.518, 35.582), (26, 37)))
        self.add_contour('c0', 'e3', closed=True)
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
