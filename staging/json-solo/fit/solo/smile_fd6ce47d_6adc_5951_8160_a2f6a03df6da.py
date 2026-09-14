"""Smile (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fd6ce47d-6adc-5951-8160-a2f6a03df6da'
SOURCE_PATH = 'icons-json/smileys/smile_fd6ce47d-6adc-5951-8160-a2f6a03df6da.json'
AUTHOR = 'json_to_solo'

class Smile(Solo48):
    icon_id = 'smile'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('smile', 'smileys')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_arc('sym-e2', (13, 20), (14, 19), radius_x=3)
        self.add_arc('sym-e3', (14, 19), (19, 19), radius_x=3)
        self.add_line('sym-e4', (19, 19), (19, 20))
        self.add_arc('sym-e5', (14, 29), (24, 35), radius_x=11, sweep=False)
        self.add_arc('sym-e6', (24, 35), (34, 29), radius_x=11, sweep=False)
        self.add_arc('sym-e7', (35, 20), (34, 19), radius_x=3, sweep=False)
        self.add_arc('sym-e8', (34, 19), (29, 19), radius_x=3, sweep=False)
        self.add_line('sym-e9', (29, 19), (29, 20))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c2', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c3', 'sym-e7', 'sym-e8', 'sym-e9')
