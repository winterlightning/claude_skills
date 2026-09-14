"""Thrilled (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '31446b53-42da-50a7-b237-95d0a120cf43'
SOURCE_PATH = 'icons-json/smileys/thrilled_31446b53-42da-50a7-b237-95d0a120cf43.json'
AUTHOR = 'json_to_solo'

class ThrilledSmileys(Solo48):
    icon_id = 'thrilled-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('thrilled', 'smileys')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_arc('sym-e2', (13, 26), (14, 28), radius_x=8, sweep=False)
        self.add_arc('sym-e3', (14, 28), (17, 31), radius_x=10, sweep=False)
        self.add_arc('sym-e4', (17, 31), (24, 34), radius_x=13, sweep=False)
        self.add_arc('sym-e5', (24, 34), (31, 31), radius_x=12, sweep=False)
        self.add_arc('sym-e6', (31, 31), (34, 28), radius_x=10, sweep=False)
        self.add_arc('sym-e7', (34, 28), (35, 26), radius_x=8, sweep=False)
        self.add_arc('sym-e8', (13, 19), (14, 18), radius_x=4)
        self.add_arc('sym-e9', (14, 18), (21, 18), radius_x=4)
        self.add_line('sym-e10', (21, 18), (21, 19))
        self.add_line('sym-e11', (35, 19), (34, 18))
        self.add_arc('sym-e12', (34, 18), (27, 18), radius_x=4, sweep=False)
        self.add_arc('sym-e13', (27, 18), (27, 19), radius_x=6, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c2', 'sym-e8', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c3', 'sym-e11', 'sym-e12', 'sym-e13')
