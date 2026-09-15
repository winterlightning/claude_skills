"""Panoramic (video), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1886bf3f-c98c-584f-835e-85f7ec5deb73'
SOURCE_PATH = 'pictographic-primitives/video/panoramic_1886bf3f-c98c-584f-835e-85f7ec5deb73.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Panoramic(Solo48):
    icon_id = 'panoramic'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    aliases = ()
    keywords = ('panoramic', 'video')

    def build(self):
        self.add_line('e0', (32, 11), (32, 37))
        self.add_line('e1', (16, 37), (16, 11))
        self.add_line('e2', (10, 10), (5, 8))
        self.add_line('e3', (4, 8), (4, 39))
        self.add_line('e4', (4, 39), (18, 37))
        self.add_line('e5', (39, 39), (43, 40))
        self.add_line('e6', (44, 39), (44, 8))
        self.add_arc('e7', (44, 8), (10, 10), radius_x=55)
        self.add_arc('e8', (5, 8), (4, 8), radius_x=5)
        self.add_arc('e9', (18, 37), (39, 39), radius_x=34)
        self.add_arc('e10', (43, 40), (44, 39), radius_x=1, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e7', 'e2', 'e8', 'e3', 'e4', 'e9', 'e5', 'e10', 'e6', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
