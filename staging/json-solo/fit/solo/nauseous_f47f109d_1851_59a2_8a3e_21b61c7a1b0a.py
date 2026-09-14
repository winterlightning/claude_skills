"""Nauseous (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f47f109d-1851-59a2-8a3e-21b61c7a1b0a'
SOURCE_PATH = 'icons-json/smileys/nauseous_f47f109d-1851-59a2-8a3e-21b61c7a1b0a.json'
AUTHOR = 'json_to_solo'

class NauseousF47f109d(Solo48):
    icon_id = 'nauseous-f47f109d'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('nauseous', 'smileys')

    def build(self):
        self.add_line('e0', (35, 15), (28, 19))
        self.add_line('e1', (28, 19), (35, 24))
        self.add_line('e2', (14, 15), (20, 19))
        self.add_line('e3', (20, 19), (14, 24))
        self.add_arc('e4-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e4-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e5-1', (14, 33), (24, 33), radius_x=6)
        self.add_line('e5-2', (24, 33), (29, 30))
        self.add_line('e5-3', (29, 30), (34, 33))
        self.add_contour('c0', 'e5-1', 'e5-2', 'e5-3')
        self.add_contour('c1', 'e0', 'e1')
        self.add_contour('c2', 'e2', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
