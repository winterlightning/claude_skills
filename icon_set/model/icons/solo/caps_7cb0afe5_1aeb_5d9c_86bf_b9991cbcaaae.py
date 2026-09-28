"""Caps (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7cb0afe5-1aeb-5d9c-86bf-b9991cbcaaae'
SOURCE_PATH = 'pictographic-primitives/interface-essential/caps_7cb0afe5-1aeb-5d9c-86bf-b9991cbcaaae.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Caps(Solo48):
    icon_id = 'caps'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('caps', 'interface-essential')

    def build(self):
        self.add_line('e0', (4, 13), (4, 8))
        self.add_line('e1', (4, 8), (20, 8))
        self.add_line('e2', (20, 8), (20, 13))
        self.add_line('e3', (12, 8), (12, 40))
        self.add_line('e4', (9, 40), (15, 40))
        self.add_line('e5', (28, 13), (28, 8))
        self.add_line('e6', (28, 8), (44, 8))
        self.add_line('e7', (44, 8), (44, 13))
        self.add_line('e8', (36, 40), (36, 8))
        self.add_line('e9', (33, 40), (39, 40))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5', 'e6', 'e7')
        self.add_contour('c4', 'e8')
        self.add_contour('c5', 'e9')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c3')
