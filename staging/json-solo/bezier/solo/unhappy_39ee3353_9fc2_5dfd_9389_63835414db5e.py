"""Unhappy (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39ee3353-9fc2-5dfd-9389-63835414db5e'
SOURCE_PATH = 'icons-json/smileys/unhappy_39ee3353-9fc2-5dfd-9389-63835414db5e.json'
AUTHOR = 'json_to_solo'

class Unhappy39ee3353(Solo48):
    icon_id = 'unhappy-39ee3353'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('unhappy', 'smileys')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('sym-e2', (24, 30), ((26.435, 30), (29.039, 30.27), (31, 32)))
        self.add_bezier('sym-e3', (31, 32), ((31.9, 32.791), (32.336, 34.009), (33, 35)))
        self.add_bezier('sym-e4', (29, 17), ((30.355, 18.227), (32.309, 18.336), (34, 19)))
        self.add_line('sym-e5', (31, 21), (31, 23))
        self.add_bezier('sym-e6', (24, 30), ((21.565, 30), (18.961, 30.27), (17, 32)))
        self.add_bezier('sym-e7', (17, 32), ((16.1, 32.791), (15.664, 34.009), (15, 35)))
        self.add_bezier('sym-e8', (19, 17), ((17.645, 18.227), (15.691, 18.336), (14, 19)))
        self.add_line('sym-e9', (17, 21), (17, 23))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4')
        self.add_contour('sym-c3', 'sym-e5')
        self.add_contour('sym-c4', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c5', 'sym-e8')
        self.add_contour('sym-c6', 'sym-e9')
        self.relate('connect', 'sym-c1', 'sym-c4')
