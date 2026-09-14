"""Dizzy (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9089549c-1833-5559-89e3-3536fbecfc79'
SOURCE_PATH = 'icons-json/smileys/dizzy_9089549c-1833-5559-89e3-3536fbecfc79.json'
AUTHOR = 'json_to_solo'

class Dizzy(Solo48):
    icon_id = 'dizzy'
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
        self.add_arc('e6-1', (14, 31), (16, 33), radius_x=3, sweep=False)
        self.add_line('e6-2', (16, 33), (20, 31))
        self.add_arc('e6-3', (20, 31), (23, 32), radius_x=3)
        self.add_arc('e6-4', (23, 32), (25, 32), radius_x=2, sweep=False)
        self.add_line('e6-5', (25, 32), (29, 30))
        self.add_arc('e7', (30, 32), (34, 31), radius_x=3, sweep=False)
        self.add_contour('c0', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e0', 'e7')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
