"""Angle brackets (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7173b451-8abc-5d28-bf77-d7caa41bbb6a'
SOURCE_PATH = 'pictographic-primitives/interface-essential/angle brackets_7173b451-8abc-5d28-bf77-d7caa41bbb6a.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class AngleBrackets(Solo48):
    icon_id = 'angle-brackets'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('angle', 'brackets', 'interface-essential')

    def build(self):
        self.add_line('e0', (18, 8), (4, 24))
        self.add_line('e1', (4, 24), (18, 40))
        self.add_line('e2', (30, 8), (44, 24))
        self.add_line('e3', (44, 24), (31, 40))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3')
