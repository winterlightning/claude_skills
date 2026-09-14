"""Shout (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0170253f-5b18-54db-9549-084ab4e62b33'
SOURCE_PATH = 'icons-json/smileys/shout_0170253f-5b18-54db-9549-084ab4e62b33.json'
AUTHOR = 'json_to_solo'

class ShoutSmileys(Solo48):
    icon_id = 'shout-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('shout', 'smileys')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_line('sym-e2', (17, 15), (17, 22))
        self.add_line('sym-e3', (17, 36), (24, 36))
        self.add_line('sym-e4', (24, 36), (31, 36))
        self.add_bezier('sym-e5', (31, 36), ((31.073, 34.373), (31.655, 32.527), (31, 31)))
        self.add_bezier('sym-e6', (31, 31), ((29.697, 27.928), (26.765, 26), (24, 26)))
        self.add_bezier('sym-e7', (24, 26), ((21.235, 26), (18.303, 27.928), (17, 31)))
        self.add_bezier('sym-e8', (17, 31), ((16.345, 32.527), (16.927, 34.373), (17, 36)))
        self.add_line('sym-e9', (31, 15), (31, 22))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', closed=True)
        self.add_contour('sym-c3', 'sym-e9')
