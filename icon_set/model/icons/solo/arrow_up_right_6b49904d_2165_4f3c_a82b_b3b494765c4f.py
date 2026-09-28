"""Arrow up right (state), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b49904d-2165-4f3c-a82b-b3b494765c4f'
SOURCE_PATH = 'pictographic-primitives/state/arrow up right_6b49904d-2165-4f3c-a82b-b3b494765c4f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ArrowUpRight(Solo48):
    icon_id = 'arrow-up-right-state'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('arrow', 'up', 'right', 'state')

    def build(self):
        self.add_line('e0', (6, 42), (42, 6))
        self.add_line('e1', (42, 23), (42, 6))
        self.add_line('e2', (25, 6), (42, 6))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
