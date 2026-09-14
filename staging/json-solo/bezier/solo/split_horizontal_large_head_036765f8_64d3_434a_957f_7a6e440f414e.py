"""Split horizontal large head (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '036765f8-64d3-434a-957f-7a6e440f414e'
SOURCE_PATH = 'icons-json/arrows/split horizontal large head_036765f8-64d3-434a-957f-7a6e440f414e.json'
AUTHOR = 'json_to_solo'

class SplitHorizontalLargeHeadArrows(Solo48):
    icon_id = 'split-horizontal-large-head-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('split', 'horizontal', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('sym-e0', (8, 24), (27, 24))
        self.add_bezier('sym-e1', (27, 24), ((29.754, 25.236), (31.897, 26.8), (33, 30)))
        self.add_bezier('sym-e2', (33, 30), ((33.135, 30.4), (33, 30.582), (33, 31)))
        self.add_line('sym-e3', (33, 31), (33, 44))
        self.add_line('sym-e4', (33, 44), (26, 37))
        self.add_line('sym-e5', (40, 37), (33, 44))
        self.add_line('sym-e6', (26, 11), (33, 4))
        self.add_line('sym-e7', (33, 4), (40, 11))
        self.add_bezier('sym-e8', (27, 24), ((29.754, 22.764), (31.897, 21.2), (33, 18)))
        self.add_bezier('sym-e9', (33, 18), ((33.135, 17.6), (33, 17.418), (33, 17)))
        self.add_line('sym-e10', (33, 17), (33, 4))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c1', 'sym-e5')
        self.add_contour('sym-c2', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c3', 'sym-e8', 'sym-e9', 'sym-e10')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
