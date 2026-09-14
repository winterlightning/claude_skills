"""Shout (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0170253f-5b18-54db-9549-084ab4e62b33'
SOURCE_PATH = 'icons-json/smileys/shout_0170253f-5b18-54db-9549-084ab4e62b33.json'
AUTHOR = 'json_to_solo'

class Shout(Solo48):
    icon_id = 'shout'
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
        self.add_arc('sym-e5', (31, 36), (31, 31), radius_x=10, sweep=False)
        self.add_arc('sym-e6', (31, 31), (24, 26), radius_x=8, sweep=False)
        self.add_arc('sym-e7', (24, 26), (17, 31), radius_x=8, sweep=False)
        self.add_arc('sym-e8', (17, 31), (17, 36), radius_x=10, sweep=False)
        self.add_line('sym-e9', (31, 15), (31, 22))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', closed=True)
        self.add_contour('sym-c3', 'sym-e9')
