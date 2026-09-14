"""Responsive design expand (websites), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '500a391a-b10e-4295-b94f-b4c317cce2c7'
SOURCE_PATH = 'icons-json/websites/responsive design expand_500a391a-b10e-4295-b94f-b4c317cce2c7.json'
AUTHOR = 'json_to_solo'

class ResponsiveDesignExpandWebsites(Solo48):
    icon_id = 'responsive-design-expand-websites'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'websites'
    aliases = ()
    keywords = ('responsive', 'design', 'expand', 'websites')

    def build(self):
        self.add_line('e0', (4, 18), (4, 11))
        self.add_line('e1', (8, 8), (41, 8))
        self.add_line('e2', (44, 11), (44, 18))
        self.add_line('e3', (4, 18), (44, 18))
        self.add_line('e4', (4, 18), (4, 32))
        self.add_line('e5', (9, 40), (40, 40))
        self.add_line('e6', (44, 37), (44, 18))
        self.add_bezier('e7', (4, 11), ((4.745, 9.198), (5.991, 8.64), (8, 8)))
        self.add_bezier('e8', (41, 8), ((41.227, 8.093), (41.727, 8.101), (41.955, 8.219)), ((43.018, 8.792), (44, 9.829), (44, 11)))
        self.add_bezier('e9', (4, 32), ((4, 32.749), (4.009, 33.069), (4.009, 33.819)), ((4.009, 36.362), (5.836, 40), (8.991, 40)), ((9.073, 40), (9.145, 40), (9.218, 40)), ((9.3, 40), (8.918, 40), (9, 40)))
        self.add_bezier('e10', (40, 40), ((42.055, 39.385), (43.327, 38.903), (44, 37)))
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4', 'e9', 'e5', 'e10', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
