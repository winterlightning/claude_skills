"""Seo search (apps), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '78eadcd2-270f-4356-8302-06a17f33acbd'
SOURCE_PATH = 'icons-json/apps/seo search_78eadcd2-270f-4356-8302-06a17f33acbd.json'
AUTHOR = 'json_to_solo'

class SeoSearchApps(Solo48):
    icon_id = 'seo-search-apps'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('seo', 'search', 'apps')

    def build(self):
        self.add_line('e0', (9, 33), (13, 37))
        self.add_line('e1', (6, 35), (13, 37))
        self.add_line('e2', (13, 29), (13, 37))
        self.add_line('e3', (31, 16), (31, 8))
        self.add_line('e4', (31, 8), (34, 12))
        self.add_line('e5', (42, 42), (35, 34))
        self.add_line('e6', (39, 9), (31, 8))
        self.add_line('e7-1', (25, 6), (17, 7))
        self.add_arc('e7-2', (17, 7), (11, 11), radius_x=16, sweep=False)
        self.add_arc('e7-3', (11, 11), (6, 23), radius_x=20, sweep=False)
        self.add_arc('e7-4', (6, 23), (9, 33), radius_x=19, sweep=False)
        self.add_arc('e8', (34, 12), (35, 34), radius_x=17)
        self.add_arc('e9', (20, 40), (35, 34), radius_x=17, sweep=False)
        self.add_contour('c0', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4', 'e8')
        self.add_contour('c4', 'e9')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
