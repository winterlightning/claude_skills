"""Slider horizontal alternative (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a080813-829a-5ae2-ab20-234d7a5f3a0c'
SOURCE_PATH = 'pictographic-primitives/interface-essential/slider horizontal alternative_7a080813-829a-5ae2-ab20-234d7a5f3a0c.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class SliderHorizontalAlternative(Solo48):
    icon_id = 'slider-horizontal-alternative'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('slider', 'horizontal', 'alternative', 'interface-essential')

    def build(self):
        self.add_line('e0', (15, 8), (15, 16))
        self.add_line('e1', (4, 12), (44, 12))
        self.add_line('e2', (33, 20), (33, 28))
        self.add_line('e3', (4, 24), (44, 24))
        self.add_line('e4', (15, 32), (15, 40))
        self.add_line('e5', (4, 36), (44, 36))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
