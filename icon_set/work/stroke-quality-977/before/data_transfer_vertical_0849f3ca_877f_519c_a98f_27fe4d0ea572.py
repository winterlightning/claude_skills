"""Data transfer vertical (internet), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0849f3ca-877f-519c-a98f-27fe4d0ea572'
SOURCE_PATH = 'pictographic-primitives/internet/data transfer vertical_0849f3ca-877f-519c-a98f-27fe4d0ea572.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class DataTransferVertical(Solo48):
    icon_id = 'data-transfer-vertical'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'internet'
    aliases = ()
    keywords = ('data', 'transfer', 'vertical', 'internet')

    def build(self):
        self.add_line('e0', (20, 11), (30, 4))
        self.add_line('e1', (30, 29), (30, 4))
        self.add_line('e2', (30, 4), (40, 11))
        self.add_line('e3', (18, 19), (18, 44))
        self.add_line('e4', (18, 44), (8, 37))
        self.add_line('e5', (18, 44), (28, 38))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
