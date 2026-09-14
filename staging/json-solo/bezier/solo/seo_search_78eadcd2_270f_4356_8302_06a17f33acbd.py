"""Seo search (apps), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e7', (25, 6), ((24.517, 6), (23.853, 6), (23.378, 6)), ((22.904, 6), (22.429, 6.008), (21.963, 6.008)), ((21.889, 6.008), (21.824, 6), (21.75, 6)), ((21.619, 6), (21.488, 6.008), (21.349, 6.008)), ((19.909, 6.008), (18.387, 6.425), (17.054, 6.941)), ((11.506, 9.068), (7.751, 14.067), (6.507, 19.77)), ((6.319, 20.621), (6.016, 21.529), (6.016, 22.405)), ((6.016, 22.544), (6, 22.675), (6, 22.814)), ((6, 22.953), (6.008, 23.084), (6.008, 23.223)), ((6.008, 25.767), (7.2, 31.2), (9, 33)))
        self.add_bezier('e8', (34, 12), ((35.579, 13.972), (36.935, 15.704), (37.754, 18.125)), ((39.095, 22.077), (38.457, 26.765), (36.715, 30.488)), ((36.15, 31.683), (35.753, 32.928), (35, 34)))
        self.add_bezier('e9', (20, 40), ((24.197, 40.417), (28.475, 39.063), (31.838, 36.387)), ((32.836, 35.594), (34.092, 34.892), (35, 34)))
        self.add_contour('c0', 'e7', 'e0')
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
