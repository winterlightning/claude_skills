"""Rss feed (websites), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('sym-e1', (6, 6), ((6.221, 6), (6.779, 6), (7, 6)))
        self.add_bezier('sym-e2', (7, 6), ((10.993, 6), (14.261, 6.625), (18, 8)))
        self.add_bezier('sym-e3', (18, 8), ((23.023, 9.84), (27.368, 13.412), (31, 17)))
        self.add_bezier('sym-e4', (31, 17), ((34.588, 20.632), (38.16, 24.977), (40, 30)))
        self.add_bezier('sym-e5', (40, 30), ((41.375, 33.739), (42, 37.007), (42, 41)))
        self.add_bezier('sym-e6', (42, 41), ((42, 41.221), (42, 41.779), (42, 42)))
        self.add_bezier('sym-e7', (6, 17), ((12.829, 17.057), (18.586, 20.584), (23, 25)))
        self.add_bezier('sym-e8', (23, 25), ((27.416, 29.414), (30.943, 35.171), (31, 42)))
        self.add_contour('sym-c0', 'sym-e0', closed=True)
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c2', 'sym-e7', 'sym-e8')
