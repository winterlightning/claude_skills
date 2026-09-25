"""Ascending sort 1 (_uncategorized_04), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1866bbd3-0202-4c95-a154-4491732fa1c7'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/ascending sort 1_1866bbd3-0202-4c95-a154-4491732fa1c7.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class AscendingSort1(Solo48):
    icon_id = 'ascending-sort-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('ascending', 'sort', '_uncategorized_04')

    def build(self):
        self.add_line('e0', (24, 8), (44, 8))
        self.add_line('e1', (14, 24), (34, 24))
        self.add_line('e2', (4, 40), (24, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
