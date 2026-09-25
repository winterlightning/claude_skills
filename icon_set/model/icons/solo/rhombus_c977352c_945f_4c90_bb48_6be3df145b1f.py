"""Rhombus (container), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c977352c-945f-4c90-bb48-6be3df145b1f'
SOURCE_PATH = 'pictographic-primitives/container/rhombus_c977352c-945f-4c90-bb48-6be3df145b1f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Rhombus(Solo48):
    icon_id = 'rhombus'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('rhombus', 'container')

    def build(self):
        self.add_line('e0', (42, 24), (24, 6))
        self.add_line('e1', (24, 6), (6, 24))
        self.add_line('e2', (6, 24), (24, 42))
        self.add_line('e3', (24, 42), (42, 24))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', closed=True)
