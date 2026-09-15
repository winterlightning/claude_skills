"""Decrease (state), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4762972f-9ac5-49f3-81e6-908440ac9d34'
SOURCE_PATH = 'pictographic-primitives/state/decrease_4762972f-9ac5-49f3-81e6-908440ac9d34.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Decrease(Solo48):
    icon_id = 'decrease'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('decrease', 'state')

    def build(self):
        self.add_line('e0', (6, 6), (42, 42))
        self.add_line('e1', (25, 42), (42, 42))
        self.add_line('e2', (42, 25), (42, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
