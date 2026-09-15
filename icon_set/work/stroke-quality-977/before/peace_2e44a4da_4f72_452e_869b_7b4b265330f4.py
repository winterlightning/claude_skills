"""Peace (travel), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2e44a4da-4f72-452e-869b-7b4b265330f4'
SOURCE_PATH = 'pictographic-primitives/travel/peace_2e44a4da-4f72-452e-869b-7b4b265330f4.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class PeaceTravel(Solo48):
    icon_id = 'peace-travel'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    aliases = ()
    keywords = ('peace', 'travel')

    def build(self):
        self.add_line('e0', (24, 44), (24, 23))
        self.add_line('e1', (24, 23), (10, 38))
        self.add_line('e2', (38, 38), (24, 23))
        self.add_line('e3', (24, 23), (24, 4))
        self.add_arc('e4-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e4-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c1', 'e4')
        self.relate('connect', 'c1', 'e4')
