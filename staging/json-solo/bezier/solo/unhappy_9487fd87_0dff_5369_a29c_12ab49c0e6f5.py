"""Unhappy (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9487fd87-0dff-5369-a29c-12ab49c0e6f5'
SOURCE_PATH = 'icons-json/smileys/unhappy_9487fd87-0dff-5369-a29c-12ab49c0e6f5.json'
AUTHOR = 'json_to_solo'

class Unhappy9487fd87(Solo48):
    icon_id = 'unhappy-9487fd87'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('unhappy', 'smileys')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('sym-e2', (15, 22), ((17.255, 20.545), (17.873, 19.6), (18, 17)))
        self.add_bezier('sym-e3', (16, 33), ((16.791, 32.118), (17.036, 31.7), (18, 31)))
        self.add_bezier('sym-e4', (18, 31), ((19.602, 29.845), (21.991, 29), (24, 29)))
        self.add_bezier('sym-e5', (24, 29), ((26.009, 29), (28.398, 29.845), (30, 31)))
        self.add_bezier('sym-e6', (30, 31), ((30.964, 31.7), (31.209, 32.118), (32, 33)))
        self.add_bezier('sym-e7', (33, 22), ((30.745, 20.545), (30.127, 19.6), (30, 17)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c3', 'sym-e7')
