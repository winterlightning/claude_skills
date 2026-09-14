"""Trouble (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7062d366-ddbc-51df-b6fd-09ce8c2ccd5d'
SOURCE_PATH = 'icons-json/smileys/trouble_7062d366-ddbc-51df-b6fd-09ce8c2ccd5d.json'
AUTHOR = 'json_to_solo'

class Trouble(Solo48):
    icon_id = 'trouble'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('trouble', 'smileys')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_arc('sym-e2', (31, 16), (30, 16), radius_x=3)
        self.add_line('sym-e3', (30, 16), (29, 18))
        self.add_line('sym-e4', (29, 18), (30, 20))
        self.add_line('sym-e5', (30, 20), (31, 21))
        self.add_arc('sym-e6', (24, 27), (34, 33), radius_x=12)
        self.add_arc('sym-e7', (17, 16), (18, 16), radius_x=3, sweep=False)
        self.add_line('sym-e8', (18, 16), (19, 18))
        self.add_line('sym-e9', (19, 18), (18, 20))
        self.add_arc('sym-e10', (18, 20), (17, 21), radius_x=4, sweep=False)
        self.add_arc('sym-e11', (24, 27), (14, 33), radius_x=12, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c2', 'sym-e6')
        self.add_contour('sym-c3', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c4', 'sym-e11')
        self.relate('connect', 'sym-c2', 'sym-c4')
