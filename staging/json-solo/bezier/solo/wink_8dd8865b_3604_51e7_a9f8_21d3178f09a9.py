"""Wink (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8dd8865b-3604-51e7-a9f8-21d3178f09a9'
SOURCE_PATH = 'icons-json/smileys/wink_8dd8865b-3604-51e7-a9f8-21d3178f09a9.json'
AUTHOR = 'json_to_solo'

class WinkSmileys(Solo48):
    icon_id = 'wink-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('wink', 'smileys')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e1', (16, 20), ((16.055, 19.164), (15.864, 18.609), (16.345, 17.882)), ((16.582, 17.518), (16.936, 17.264), (17.355, 17.145)), ((19.036, 16.709), (18.991, 18.845), (19, 20)))
        self.add_bezier('e2', (28, 19), ((30.491, 16.755), (32.482, 16.827), (35, 19)))
        self.add_bezier('e3', (15, 29), ((15.555, 30.409), (16.118, 31.245), (17.191, 32.345)), ((21.327, 36.555), (28.709, 35.709), (32.409, 31.345)), ((33.127, 30.491), (33.582, 30.018), (34, 29)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
