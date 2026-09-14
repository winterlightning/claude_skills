"""Unhappy (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9487fd87-0dff-5369-a29c-12ab49c0e6f5'
SOURCE_PATH = 'icons-json/smileys/unhappy_9487fd87-0dff-5369-a29c-12ab49c0e6f5.json'
AUTHOR = 'json_to_solo'

class UnhappySmileys(Solo48):
    icon_id = 'unhappy-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('unhappy', 'smileys')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_arc('sym-e2', (15, 22), (18, 17), radius_x=6, sweep=False)
        self.add_line('sym-e3', (16, 33), (18, 31))
        self.add_arc('sym-e4', (18, 31), (24, 29), radius_x=9)
        self.add_arc('sym-e5', (24, 29), (30, 31), radius_x=9)
        self.add_arc('sym-e6', (30, 31), (32, 33), radius_x=17, sweep=False)
        self.add_arc('sym-e7', (33, 22), (30, 17), radius_x=6)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c3', 'sym-e7')
