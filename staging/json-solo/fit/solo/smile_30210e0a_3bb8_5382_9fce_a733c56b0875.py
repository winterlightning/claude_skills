"""Smile (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30210e0a-3bb8-5382-9fce-a733c56b0875'
SOURCE_PATH = 'icons-json/smileys/smile_30210e0a-3bb8-5382-9fce-a733c56b0875.json'
AUTHOR = 'json_to_solo'

class Smile30210e0a(Solo48):
    icon_id = 'smile-30210e0a'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('smile', 'smileys')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_line('sym-e2', (14, 20), (14, 19))
        self.add_arc('sym-e3', (14, 19), (19, 19), radius_x=3)
        self.add_line('sym-e4', (19, 19), (19, 20))
        self.add_arc('sym-e5', (13, 28), (24, 35), radius_x=13, sweep=False)
        self.add_arc('sym-e6', (24, 35), (35, 28), radius_x=13, sweep=False)
        self.add_line('sym-e7', (34, 20), (34, 19))
        self.add_arc('sym-e8', (34, 19), (29, 19), radius_x=3, sweep=False)
        self.add_line('sym-e9', (29, 19), (29, 20))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c2', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c3', 'sym-e7', 'sym-e8', 'sym-e9')
