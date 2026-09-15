"""Pin (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9b4b8603-58f9-4f81-8664-658ab7045658'
SOURCE_PATH = 'pictographic-primitives/interface-essential/pin_9b4b8603-58f9-4f81-8664-658ab7045658.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Pin9b4b8603(Solo48):
    icon_id = 'pin-9b4b8603'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('pin', 'interface-essential')

    def build(self):
        self.add_line('e0', (29, 39), (24, 44))
        self.add_arc('e1-1', (24, 44), (12, 31), radius_x=78)
        self.add_arc('e1-2', (12, 31), (8, 20), radius_x=18)
        self.add_arc('e1-3', (8, 20), (24, 4), radius_x=16)
        self.add_arc('e1-4', (24, 4), (40, 20), radius_x=16)
        self.add_arc('e1-5', (40, 20), (29, 39), radius_x=28)
        self.add_dot('e2', (24, 19))
        self.add_contour('c0', 'e0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', closed=True)
