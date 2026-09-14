"""Dizzy (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9089549c-1833-5559-89e3-3536fbecfc79'
SOURCE_PATH = 'icons-json/smileys/dizzy_9089549c-1833-5559-89e3-3536fbecfc79.json'
AUTHOR = 'json_to_solo'

class DizzySmileys(Solo48):
    icon_id = 'dizzy-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('dizzy', 'smileys')

    def build(self):
        self.add_line('e0', (29, 30), (30, 32))
        self.add_line('e1', (28, 16), (35, 23))
        self.add_line('e2', (28, 23), (35, 16))
        self.add_line('e3', (20, 16), (13, 23))
        self.add_line('e4', (13, 16), (20, 23))
        self.add_arc('e5-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e5-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e6', (14, 31), ((14.4, 31.436), (14.855, 32.382), (15.409, 32.655)), ((17.9, 33.864), (18.545, 30.245), (20.745, 30.491)), ((22.291, 30.664), (22.945, 32.736), (24.645, 32.364)), ((26.145, 32.036), (26.718, 30.136), (28.282, 30.018)), ((28.691, 29.991), (28.636, 29.873), (29, 30)))
        self.add_bezier('e7', (30, 32), ((31.673, 32.655), (32.845, 32.382), (34, 31)))
        self.add_contour('c0', 'e6', 'e0', 'e7')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
