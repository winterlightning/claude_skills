"""Angles up down (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '32a9f52e-9a62-4650-b64c-fba18e983c8a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__angles-up-down/20260926T064521Z-thuan-mac/reference/angles up down_32a9f52e-9a62-4650-b64c-fba18e983c8a.svg'
AUTHOR = 'claude-opus-5-5'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class AnglesUpDown(Solo48):
    icon_id = 'angles-up-down'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('angles', 'up', 'down', '_uncategorized_03')

    def build(self):
        # Revision per review: the vertical shaft is one straight stroke on the centre line x 24,
        # its own path from tip to tip (4 to 44); the two chevron heads are separate polylines
        # sharing the tips, with 45-degree arms (14 each way) as in the reference, mirrored top
        # to bottom and left to right.
        self.add_line('shaft', (24, 4), (24, 44))
        self.add_polyline('head-up', (10, 18), (24, 4), (38, 18))
        self.add_polyline('head-down', (10, 30), (24, 44), (38, 30))
        self.relate('connect', 'shaft', 'head-up')
        self.relate('connect', 'shaft', 'head-down')
