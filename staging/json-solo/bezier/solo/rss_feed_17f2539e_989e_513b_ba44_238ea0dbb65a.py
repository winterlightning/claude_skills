"""Rss feed (websites), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '17f2539e-989e-513b-ba44-238ea0dbb65a'
SOURCE_PATH = 'icons-json/websites/rss feed_17f2539e-989e-513b-ba44-238ea0dbb65a.json'
AUTHOR = 'json_to_solo'

class RssFeed17f2539e(Solo48):
    icon_id = 'rss-feed-17f2539e'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'websites'
    aliases = ()
    keywords = ('rss', 'feed', 'websites')

    def build(self):
        self.add_arc('e0-top', (6, 37), (16, 37), radius_x=5)
        self.add_arc('e0-bottom', (16, 37), (6, 37), radius_x=5)
        self.add_bezier('e1', (9, 6), ((9.172, 6), (9.616, 6.016), (9.796, 6.016)), ((13.347, 6.016), (17.07, 7.039), (20.343, 8.348)), ((31.233, 12.725), (39.292, 21.955), (41.395, 33.597)), ((41.714, 35.365), (41.984, 37.173), (41.984, 38.973)), ((41.984, 39.161), (42, 39.812), (42, 40)))
        self.add_bezier('e2', (9, 19), ((20.471, 19.556), (28.697, 28.644), (29, 40)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
