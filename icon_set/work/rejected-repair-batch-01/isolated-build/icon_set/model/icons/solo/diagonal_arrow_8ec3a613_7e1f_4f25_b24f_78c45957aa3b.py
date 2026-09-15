"""Diagonal arrow (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ec3a613-7e1f-4f25-b24f-78c45957aa3b'
SOURCE_PATH = 'pictographic-primitives/symbol/diagonal arrow_8ec3a613-7e1f-4f25-b24f-78c45957aa3b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class DiagonalArrow(Solo48):
    icon_id = 'diagonal-arrow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('diagonal', 'arrow', 'symbol')

    def build(self):
        self.add_line('e0', (13, 8), (4, 16))
        self.add_line('e1', (4, 16), (13, 24))
        self.add_line('e2', (4, 16), (44, 16))
        self.add_line('e3', (35, 24), (44, 32))
        self.add_line('e4', (44, 32), (4, 32))
        self.add_line('e5', (44, 32), (35, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
