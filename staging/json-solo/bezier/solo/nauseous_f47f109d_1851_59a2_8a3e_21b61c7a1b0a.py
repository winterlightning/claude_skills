"""Nauseous (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e5', (14, 33), ((14.436, 32.764), (14.864, 32.664), (15.255, 32.345)), ((17.064, 30.882), (17.627, 29.382), (20.4, 30.382)), ((21.927, 30.936), (22.536, 32.945), (24.336, 32.955)), ((26.282, 32.964), (26.909, 30.536), (28.745, 30.127)), ((30.827, 29.664), (31.627, 31.436), (32.991, 32.518)), ((33.291, 32.755), (33.664, 32.818), (34, 33)))
        self.add_contour('c0', 'e5')
        self.add_contour('c1', 'e0', 'e1')
        self.add_contour('c2', 'e2', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
