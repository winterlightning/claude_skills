"""Arrow badge x top (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f5144950-51a0-5692-add9-205a6ec02a0e'
SOURCE_PATH = 'icons-json/arrows/arrow badge x top_f5144950-51a0-5692-add9-205a6ec02a0e.json'
AUTHOR = 'json_to_solo'

class ArrowBadgeXTopArrows(Solo48):
    icon_id = 'arrow-badge-x-top-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'badge', 'x', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (16, 23), (32, 37))
        self.add_line('e1', (31, 23), (16, 37))
        self.add_line('e2', (21, 6), (9, 17))
        self.add_line('e3', (8, 20), (8, 41))
        self.add_line('e4', (11, 44), (38, 44))
        self.add_line('e5', (40, 40), (40, 19))
        self.add_line('e6', (40, 19), (26, 5))
        self.add_bezier('e7', (9, 17), ((8.18, 17.745), (8, 18.909), (8, 19.891)), ((8, 20.055), (8, 19.845), (8, 20)))
        self.add_bezier('e8', (8, 41), ((8, 41.145), (8.01, 41.564), (8.01, 41.718)), ((8.01, 42.782), (9.1, 43.991), (10.31, 43.991)), ((10.38, 43.991), (10.46, 44), (10.54, 44)), ((10.69, 44), (10.85, 44), (11, 44)))
        self.add_bezier('e9', (38, 44), ((38.09, 44), (38.18, 44), (38.27, 43.991)), ((39.11, 43.991), (40, 43.291), (40, 42.5)), ((40, 41.791), (40, 40.709), (40, 40)))
        self.add_bezier('e10', (26, 5), ((25.6, 4.609), (24.75, 4.009), (24.13, 4.009)), ((24.061, 4), (23.992, 4), (23.933, 4)), ((23.932, 4), (23.931, 4), (23.93, 4)), ((23.86, 4.009), (23.79, 4.009), (23.73, 4.018)), ((22.74, 4.018), (21.64, 5.418), (21, 6)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e7', 'e3', 'e8', 'e4', 'e9', 'e5', 'e6', 'e10', closed=True)
