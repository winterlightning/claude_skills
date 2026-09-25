"""Manual entry (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9976934a-a502-452e-8772-da5f6a51dce2'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_26/manual entry_9976934a-a502-452e-8772-da5f6a51dce2.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ManualEntry(Solo48):
    icon_id = 'manual-entry'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('manual', 'entry', '_uncategorized')

    def build(self):
        self.add_line('e0', (44, 8), (44, 40))
        self.add_line('e1', (44, 40), (4, 40))
        self.add_line('e2', (4, 40), (4, 18))
        self.add_line('e3', (4, 18), (44, 8))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', closed=True)
