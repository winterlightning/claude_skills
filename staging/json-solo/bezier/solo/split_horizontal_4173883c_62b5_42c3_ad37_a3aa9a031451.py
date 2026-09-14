"""Split horizontal (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4173883c-62b5-42c3-ad37-a3aa9a031451'
SOURCE_PATH = 'icons-json/arrows/split horizontal_4173883c-62b5-42c3-ad37-a3aa9a031451.json'
AUTHOR = 'json_to_solo'

class SplitHorizontalArrows(Solo48):
    icon_id = 'split-horizontal-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('split', 'horizontal', 'arrows')

    def build(self):
        self.add_line('sym-e0', (4, 24), (31, 24))
        self.add_bezier('sym-e1', (31, 24), ((31.309, 24.084), (31.673, 23.949), (32, 24)))
        self.add_bezier('sym-e2', (32, 24), ((32.118, 24.034), (32.882, 23.966), (33, 24)))
        self.add_bezier('sym-e3', (33, 24), ((32.836, 23.891), (32.173, 24.109), (32, 24)))
        self.add_bezier('sym-e4', (32, 24), ((32.173, 23.891), (32.836, 24.109), (33, 24)))
        self.add_bezier('sym-e5', (33, 24), ((32.882, 24.034), (32.118, 23.966), (32, 24)))
        self.add_bezier('sym-e6', (32, 24), ((31.673, 24.051), (31.309, 23.916), (31, 24)))
        self.add_bezier('sym-e7', (31, 24), ((34.273, 25.154), (37.445, 25.842), (39, 29)))
        self.add_bezier('sym-e8', (39, 29), ((39.391, 29.792), (39, 31.116), (39, 32)))
        self.add_line('sym-e9', (39, 32), (39, 40))
        self.add_line('sym-e10', (39, 40), (35, 36))
        self.add_line('sym-e11', (44, 36), (39, 40))
        self.add_bezier('sym-e12', (31, 24), ((34.273, 22.846), (37.445, 22.158), (39, 19)))
        self.add_bezier('sym-e13', (39, 19), ((39.391, 18.208), (39, 16.884), (39, 16)))
        self.add_line('sym-e14', (39, 16), (39, 8))
        self.add_line('sym-e15', (39, 8), (35, 12))
        self.add_line('sym-e16', (44, 12), (39, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c1', 'sym-e11')
        self.add_contour('sym-c2', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
        self.add_contour('sym-c3', 'sym-e16')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
