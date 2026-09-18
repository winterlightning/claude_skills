"""Independent 32px profile of rss-feed-websites.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '9d226a73-61ef-4fe3-8c19-16a945e40d13'
SOURCE_PATH = 'pictographic-primitives/websites/rss feed_9d226a73-61ef-4fe3-8c19-16a945e40d13.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9d226a73-61ef-4fe3-8c19-16a945e40d13', 'pictographic-primitives/websites/rss feed_9d226a73-61ef-4fe3-8c19-16a945e40d13.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rss-feed-websites',)
SOLO_SOURCE_ICON_IDS = ('rss-feed-websites',)
REFERENCE_EXPORT_SHA256 = 'ded3ed51c642d5c3ae6ff31510d92c1225faef779f8b245aa19453dcabe4479b'

class Drawing(Sub32):
    icon_id = 'rss-feed-websites-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'websites'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 2), (30, 30), radius_x=28, radius_y=28, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_arc('p2-r1-1', (2, 11), (21, 30), radius_x=19, radius_y=19, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (5, 27), (5, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
