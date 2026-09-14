"""Rss feed (websites), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9d226a73-61ef-4fe3-8c19-16a945e40d13'
SOURCE_PATH = 'icons-json/websites/rss feed_9d226a73-61ef-4fe3-8c19-16a945e40d13.json'
AUTHOR = 'json_to_solo'

class RssFeed9d226a73(Solo48):
    icon_id = 'rss-feed-9d226a73'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'websites'
    aliases = ()
    keywords = ('rss', 'feed', 'websites')

    def build(self):
        self.add_line('sym-e0', (10, 38), (10, 38))
        self.add_line('sym-e1', (6, 6), (7, 6))
        self.add_arc('sym-e2', (7, 6), (18, 8), radius_x=35)
        self.add_arc('sym-e3', (18, 8), (31, 17), radius_x=36)
        self.add_arc('sym-e4', (31, 17), (40, 30), radius_x=36)
        self.add_line('sym-e5', (40, 30), (42, 41))
        self.add_line('sym-e6', (42, 41), (42, 42))
        self.add_arc('sym-e7', (6, 17), (23, 25), radius_x=25)
        self.add_arc('sym-e8', (23, 25), (31, 42), radius_x=25)
        self.add_contour('sym-c0', 'sym-e0', closed=True)
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c2', 'sym-e7', 'sym-e8')
