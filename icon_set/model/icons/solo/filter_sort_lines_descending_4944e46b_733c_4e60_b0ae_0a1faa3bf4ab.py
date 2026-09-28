"""Filter sort lines descending (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4944e46b-733c-4e60-b0ae-0a1faa3bf4ab'
SOURCE_PATH = 'pictographic-primitives/interface-essential/filter sort lines descending_4944e46b-733c-4e60-b0ae-0a1faa3bf4ab.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class FilterSortLinesDescending(Solo48):
    icon_id = 'filter-sort-lines-descending'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('filter', 'sort', 'lines', 'descending', 'interface-essential')

    def build(self):
        self.add_line('e0', (4, 8), (44, 8))
        self.add_line('e1', (9, 19), (39, 19))
        self.add_line('e2', (14, 30), (34, 30))
        self.add_line('e3', (18, 40), (30, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
