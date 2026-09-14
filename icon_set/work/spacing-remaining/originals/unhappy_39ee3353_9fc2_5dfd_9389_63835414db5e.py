"""Unhappy (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39ee3353-9fc2-5dfd-9389-63835414db5e'
SOURCE_PATH = 'icons-json/smileys/unhappy_39ee3353-9fc2-5dfd-9389-63835414db5e.json'
AUTHOR = 'json_to_solo'

class Unhappy(Solo48):
    icon_id = 'unhappy'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('unhappy', 'smileys')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_arc('sym-e2', (24, 30), (31, 32), radius_x=10)
        self.add_line('sym-e3', (31, 32), (33, 35))
        self.add_line('sym-e4', (29, 17), (34, 19))
        self.add_line('sym-e5', (31, 21), (31, 23))
        self.add_arc('sym-e6', (24, 30), (17, 32), radius_x=10, sweep=False)
        self.add_line('sym-e7', (17, 32), (15, 35))
        self.add_line('sym-e8', (19, 17), (14, 19))
        self.add_line('sym-e9', (17, 21), (17, 23))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4')
        self.add_contour('sym-c3', 'sym-e5')
        self.add_contour('sym-c4', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c5', 'sym-e8')
        self.add_contour('sym-c6', 'sym-e9')
        self.relate('connect', 'sym-c1', 'sym-c4')
