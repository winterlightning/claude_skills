"""Cursor 2 (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a1fd996b-f7ee-4257-bb4f-d644721f5983'
SOURCE_PATH = 'pictographic-primitives/symbol/cursor 2_a1fd996b-f7ee-4257-bb4f-d644721f5983.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Cursor2(Solo48):
    icon_id = 'cursor-2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('cursor', 'symbol')

    def build(self):
        self.add_line('e0', (6, 22), (42, 6))
        self.add_line('e1', (42, 6), (26, 42))
        self.add_line('e2', (26, 42), (20, 28))
        self.add_line('e3', (20, 28), (6, 22))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', closed=True)
