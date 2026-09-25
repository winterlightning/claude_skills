"""Slash back (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c338e2e-bacb-45cc-a922-6fa6db5023d3'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_34/slash back_1c338e2e-bacb-45cc-a922-6fa6db5023d3.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class SlashBack(Solo48):
    icon_id = 'slash-back'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('slash', 'back', '_uncategorized')

    def build(self):
        self.add_line('e0', (6, 6), (42, 42))
        self.add_contour('c0', 'e0')
