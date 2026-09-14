"""Arrow badge x right (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '679552c7-d7b5-5fbf-ac01-9c78f39fa2b4'
SOURCE_PATH = 'icons-json/arrows/arrow badge x right_679552c7-d7b5-5fbf-ac01-9c78f39fa2b4.json'
AUTHOR = 'json_to_solo'

class ArrowBadgeXRightArrows(Solo48):
    icon_id = 'arrow-badge-x-right-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'badge', 'x', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (25, 16), (11, 32))
        self.add_line('e1', (25, 31), (11, 16))
        self.add_line('e2', (42, 21), (31, 9))
        self.add_line('e3', (28, 8), (7, 8))
        self.add_line('e4', (4, 11), (4, 38))
        self.add_line('e5', (8, 40), (29, 40))
        self.add_line('e6', (29, 40), (43, 26))
        self.add_bezier('e7', (31, 9), ((30.255, 8.18), (29.091, 8), (28.109, 8)), ((27.945, 8), (28.155, 8), (28, 8)))
        self.add_bezier('e8', (7, 8), ((6.855, 8), (6.436, 8.01), (6.282, 8.01)), ((5.218, 8.01), (4.009, 9.1), (4.009, 10.31)), ((4.009, 10.38), (4, 10.46), (4, 10.54)), ((4, 10.69), (4, 10.85), (4, 11)))
        self.add_bezier('e9', (4, 38), ((4, 38.09), (4, 38.18), (4.009, 38.27)), ((4.009, 39.11), (4.709, 40), (5.5, 40)), ((6.209, 40), (7.291, 40), (8, 40)))
        self.add_bezier('e10', (43, 26), ((43.391, 25.6), (43.991, 24.75), (43.991, 24.13)), ((44, 24.061), (44, 23.992), (44, 23.933)), ((44, 23.932), (44, 23.931), (44, 23.93)), ((43.991, 23.86), (43.991, 23.79), (43.982, 23.73)), ((43.982, 22.74), (42.582, 21.64), (42, 21)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e7', 'e3', 'e8', 'e4', 'e9', 'e5', 'e6', 'e10', closed=True)
