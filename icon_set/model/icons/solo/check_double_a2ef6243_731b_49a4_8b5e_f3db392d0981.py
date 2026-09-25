"""Check double (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2ef6243-731b-49a4-8b5e-f3db392d0981'
SOURCE_PATH = 'pictographic-primitives/interface-essential/check double_a2ef6243-731b-49a4-8b5e-f3db392d0981.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class CheckDouble(Solo48):
    icon_id = 'check-double'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('check', 'double', 'interface-essential')

    def build(self):
        self.add_line('e0', (40, 4), (18, 23))
        self.add_line('e1', (18, 23), (8, 14))
        self.add_line('e2', (40, 25), (18, 44))
        self.add_line('e3', (18, 44), (8, 35))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3')
