"""Surprised (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a7e14f7a-6621-5c08-847e-46b73e98c27e'
SOURCE_PATH = 'icons-json/smileys/surprised_a7e14f7a-6621-5c08-847e-46b73e98c27e.json'
AUTHOR = 'json_to_solo'

class Surprised(Solo48):
    icon_id = 'surprised'
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
        self.add_arc('e3-1', (26, 37), (19, 32), radius_x=5)
        self.add_arc('e3-2', (19, 32), (24, 25), radius_x=6)
        self.add_arc('e3-3', (24, 25), (29, 29), radius_x=6)
        self.add_arc('e3-4', (29, 29), (26, 37), radius_x=7)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', closed=True)
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
