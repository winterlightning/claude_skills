"""Slash (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc9de04e-9c7d-482f-9203-2ac10fa873d6'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_34/slash_cc9de04e-9c7d-482f-9203-2ac10fa873d6.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Slash(Solo48):
    icon_id = 'slash-uncategorized'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('slash', '_uncategorized')

    def build(self):
        self.add_line('e0', (6, 42), (42, 6))
        self.add_contour('c0', 'e0')
