"""Align stroke to center (design), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4af1a60a-c1ae-530e-94cc-6b5ec0012b97'
SOURCE_PATH = 'pictographic-primitives/design/align stroke to center_4af1a60a-c1ae-530e-94cc-6b5ec0012b97.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class AlignStrokeToCenter(Solo48):
    icon_id = 'align-stroke-to-center'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('align', 'stroke', 'to', 'center', 'design')

    def build(self):
        self.add_line('e0', (12, 4), (12, 34))
        self.add_line('e1', (17, 39), (40, 39))
        self.add_line('e2', (17, 34), (8, 34))
        self.add_line('e3', (8, 34), (8, 44))
        self.add_line('e4', (8, 44), (17, 44))
        self.add_line('e5', (17, 44), (17, 34))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4', 'e5', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
