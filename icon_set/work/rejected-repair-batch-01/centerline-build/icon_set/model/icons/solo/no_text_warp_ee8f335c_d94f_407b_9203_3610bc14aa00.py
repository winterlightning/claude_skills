"""No text warp (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ee8f335c-d94f-407b-9203-3610bc14aa00'
SOURCE_PATH = 'pictographic-primitives/interface-essential/no text warp_ee8f335c-d94f-407b-9203-3610bc14aa00.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class NoTextWarp(Solo48):
    icon_id = 'no-text-warp'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('no', 'text', 'warp', 'interface-essential')

    def build(self):
        self.add_line('e0', (4, 8), (44, 8))
        self.add_line('e1', (4, 24), (12, 24))
        self.add_line('e2', (44, 24), (36, 24))
        self.add_line('e3', (12, 24), (12, 32))
        self.add_line('e4', (12, 32), (36, 32))
        self.add_line('e5', (36, 32), (36, 24))
        self.add_line('e6', (12, 24), (12, 17))
        self.add_line('e7', (12, 17), (36, 17))
        self.add_line('e8', (36, 17), (36, 24))
        self.add_line('e9', (4, 40), (44, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4', 'e5')
        self.add_contour('c4', 'e6', 'e7', 'e8')
        self.add_contour('c5', 'e9')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
