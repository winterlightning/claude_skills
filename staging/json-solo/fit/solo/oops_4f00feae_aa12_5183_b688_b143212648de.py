"""Oops (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4f00feae-aa12-5183-b688-b143212648de'
SOURCE_PATH = 'icons-json/smileys/oops_4f00feae-aa12-5183-b688-b143212648de.json'
AUTHOR = 'json_to_solo'

class OopsSmileys(Solo48):
    icon_id = 'oops-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('oops', 'smileys')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_line('sym-e2', (15, 15), (19, 19))
        self.add_line('sym-e3', (19, 19), (16, 24))
        self.add_arc('sym-e4', (21, 37), (16, 33), radius_x=5)
        self.add_line('sym-e5', (16, 33), (16, 31))
        self.add_arc('sym-e6', (16, 31), (24, 28), radius_x=9)
        self.add_arc('sym-e7', (24, 28), (32, 31), radius_x=9)
        self.add_line('sym-e8', (32, 31), (32, 33))
        self.add_arc('sym-e9', (32, 33), (27, 37), radius_x=5)
        self.add_line('sym-e10', (27, 37), (24, 37))
        self.add_line('sym-e11', (24, 37), (21, 37))
        self.add_line('sym-e12', (33, 15), (29, 19))
        self.add_line('sym-e13', (29, 19), (32, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', closed=True)
        self.add_contour('sym-c3', 'sym-e12', 'sym-e13')
