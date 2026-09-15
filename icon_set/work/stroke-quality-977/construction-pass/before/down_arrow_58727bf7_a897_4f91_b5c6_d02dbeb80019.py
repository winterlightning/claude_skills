"""Down arrow (state), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '58727bf7-a897-4f91-b5c6-d02dbeb80019'
SOURCE_PATH = 'pictographic-primitives/state/down arrow_58727bf7-a897-4f91-b5c6-d02dbeb80019.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class DownArrow(Solo48):
    icon_id = 'down-arrow'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('down', 'arrow', 'state')

    def build(self):
        self.add_line('e0', (31, 4), (17, 4))
        self.add_line('e1', (17, 4), (17, 27))
        self.add_line('e2', (17, 27), (8, 27))
        self.add_line('e3', (8, 27), (24, 44))
        self.add_line('e4', (24, 44), (40, 27))
        self.add_line('e5', (40, 27), (31, 27))
        self.add_line('e6', (31, 27), (31, 4))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', closed=True)
