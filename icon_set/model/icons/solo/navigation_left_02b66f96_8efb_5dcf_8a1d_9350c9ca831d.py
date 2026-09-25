"""Navigation left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '02b66f96-8efb-5dcf-8a1d-9350c9ca831d'
SOURCE_PATH = 'pictographic-primitives/interface-essential/navigation left_02b66f96-8efb-5dcf-8a1d-9350c9ca831d.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class NavigationLeft(Solo48):
    icon_id = 'navigation-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('navigation', 'left', 'interface-essential')

    def build(self):
        self.add_line('e0', (19, 8), (4, 24))
        self.add_line('e1', (4, 24), (19, 40))
        self.add_line('e2', (15, 24), (44, 24))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
