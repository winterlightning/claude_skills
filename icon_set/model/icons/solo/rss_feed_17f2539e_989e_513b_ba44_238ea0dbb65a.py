"""Rss feed (websites), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '17f2539e-989e-513b-ba44-238ea0dbb65a'
SOURCE_PATH = 'icons-json/websites/rss feed_17f2539e-989e-513b-ba44-238ea0dbb65a.json'
AUTHOR = 'json_to_solo'

class RssFeed(Solo48):
    icon_id = 'rss-feed'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'websites'
    aliases = ()
    keywords = ('rss', 'feed', 'websites')

    def build(self):
        self.add_arc('e0-top', (6, 37), (16, 37), radius_x=5)
        self.add_arc('e0-bottom', (16, 37), (6, 37), radius_x=5)
        self.add_arc('e1-1', (9, 6), (33, 17), radius_x=34)
        self.add_arc('e1-2', (33, 17), (42, 40), radius_x=34)
        self.add_arc('e2', (9, 19), (29, 40), radius_x=21)
        self.add_contour('c0', 'e1-1', 'e1-2')
        self.add_contour('c1', 'e2')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
