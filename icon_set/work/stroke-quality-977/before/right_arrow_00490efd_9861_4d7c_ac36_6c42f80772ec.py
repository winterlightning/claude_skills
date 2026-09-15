"""Right arrow (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00490efd-9861-4d7c-ac36-6c42f80772ec'
SOURCE_PATH = 'pictographic-primitives/transportation/right arrow_00490efd-9861-4d7c-ac36-6c42f80772ec.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class RightArrow(Solo48):
    icon_id = 'right-arrow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('right', 'arrow', 'transportation')

    def build(self):
        self.add_line('e0', (4, 17), (4, 31))
        self.add_line('e1', (4, 31), (27, 31))
        self.add_line('e2', (27, 31), (27, 40))
        self.add_line('e3', (27, 40), (44, 24))
        self.add_line('e4', (44, 24), (27, 8))
        self.add_line('e5', (27, 8), (27, 17))
        self.add_line('e6', (27, 17), (4, 17))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', closed=True)
