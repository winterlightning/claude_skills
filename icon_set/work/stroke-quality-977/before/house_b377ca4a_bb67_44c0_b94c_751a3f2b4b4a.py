"""House (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b377ca4a-bb67-44c0-b94c-751a3f2b4b4a'
SOURCE_PATH = 'pictographic-primitives/interface-essential/house_b377ca4a-bb67-44c0-b94c-751a3f2b4b4a.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class HouseB377ca4a(Solo48):
    icon_id = 'house-b377ca4a'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('house', 'interface-essential')

    def build(self):
        self.add_line('e0', (44, 25), (24, 8))
        self.add_line('e1', (24, 8), (4, 25))
        self.add_line('e2', (38, 20), (38, 40))
        self.add_line('e3', (38, 40), (9, 40))
        self.add_line('e4', (9, 40), (9, 21))
        self.add_line('e5', (29, 30), (19, 30))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e4')
        self.add_contour('c2', 'e5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
