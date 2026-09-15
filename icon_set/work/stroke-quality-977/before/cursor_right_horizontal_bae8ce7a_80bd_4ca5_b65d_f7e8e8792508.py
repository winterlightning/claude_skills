"""Cursor right horizontal (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bae8ce7a-80bd-4ca5-b65d-f7e8e8792508'
SOURCE_PATH = 'pictographic-primitives/state/cursor right horizontal_bae8ce7a-80bd-4ca5-b65d-f7e8e8792508.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class CursorRightHorizontal(Solo48):
    icon_id = 'cursor-right-horizontal'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('cursor', 'right', 'horizontal', 'state')

    def build(self):
        self.add_line('e0', (39, 20), (4, 8))
        self.add_line('e1', (4, 8), (9, 22))
        self.add_line('e2', (9, 25), (4, 40))
        self.add_line('e3', (4, 40), (44, 22))
        self.add_line('e4', (44, 22), (39, 20))
        self.add_arc('e5', (9, 22), (9, 25), radius_x=4)
        self.add_contour('c0', 'e0', 'e1', 'e5', 'e2', 'e3', 'e4', closed=True)
