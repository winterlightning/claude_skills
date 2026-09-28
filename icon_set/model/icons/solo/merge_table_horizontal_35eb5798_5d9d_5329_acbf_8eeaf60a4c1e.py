"""Merge table horizontal (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '35eb5798-5d9d-5329-acbf-8eeaf60a4c1e'
SOURCE_PATH = 'pictographic-primitives/interface-essential/merge table horizontal_35eb5798-5d9d-5329-acbf-8eeaf60a4c1e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class MergeTableHorizontal(Solo48):
    icon_id = 'merge-table-horizontal'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('merge', 'table', 'horizontal', 'interface-essential')

    def build(self):
        self.add_line('e0', (13, 8), (19, 24))
        self.add_line('e1', (19, 24), (4, 24))
        self.add_line('e2', (19, 24), (13, 40))
        self.add_line('e3', (35, 8), (29, 24))
        self.add_line('e4', (29, 24), (44, 24))
        self.add_line('e5', (35, 40), (29, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4')
        self.add_contour('c4', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
