"""Manual entry (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9976934a-a502-452e-8772-da5f6a51dce2'
SOURCE_PATH = 'icons-json/_uncategorized_26/manual entry_9976934a-a502-452e-8772-da5f6a51dce2.json'
AUTHOR = 'json_to_solo'

class ManualEntryUncategorized(Solo48):
    icon_id = 'manual-entry-uncategorized'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('manual', 'entry', '_uncategorized')

    def build(self):
        self.add_line('e0', (44, 8), (44, 40))
        self.add_line('e1', (44, 40), (4, 40))
        self.add_line('e2', (4, 40), (4, 18))
        self.add_line('e3', (4, 18), (44, 8))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', closed=True)
