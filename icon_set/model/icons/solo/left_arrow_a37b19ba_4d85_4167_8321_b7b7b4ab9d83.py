"""Left arrow (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a37b19ba-4d85-4167-8321-b7b7b4ab9d83'
SOURCE_PATH = 'pictographic-primitives/transportation/left arrow_a37b19ba-4d85-4167-8321-b7b7b4ab9d83.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class LeftArrow(Solo48):
    icon_id = 'left-arrow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('left', 'arrow', 'transportation')

    def build(self):
        self.add_line('e0', (21, 8), (21, 17))
        self.add_line('e1', (21, 17), (44, 17))
        self.add_line('e2', (44, 17), (44, 31))
        self.add_line('e3', (44, 31), (21, 31))
        self.add_line('e4', (21, 31), (21, 40))
        self.add_line('e5', (21, 40), (4, 24))
        self.add_line('e6', (4, 24), (21, 8))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', closed=True)
