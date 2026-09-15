"""Csv text (state), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ec3807a6-365c-443d-aec9-259f57b44f22'
SOURCE_PATH = 'pictographic-primitives/state/csv text_ec3807a6-365c-443d-aec9-259f57b44f22.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class CsvText(Solo48):
    icon_id = 'csv-text'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('csv', 'text', 'state')

    def build(self):
        self.add_line('e0', (42, 17), (6, 17))
        self.add_line('e1', (31, 42), (31, 6))
        self.add_line('e2', (42, 30), (6, 30))
        self.add_line('e3', (18, 6), (18, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
