"""Right turn (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b99fa92-96a7-40b2-a193-2a3590db1d2b'
SOURCE_PATH = 'pictographic-primitives/transportation/right turn_4b99fa92-96a7-40b2-a193-2a3590db1d2b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class RightTurn(Solo48):
    icon_id = 'right-turn'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('right', 'turn', 'transportation')

    def build(self):
        self.add_line('e0', (29, 16), (33, 20))
        self.add_line('e1', (18, 33), (18, 24))
        self.add_line('e2', (22, 20), (33, 20))
        self.add_line('e3', (29, 25), (33, 20))
        self.add_arc('e4-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e4-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e5', (18, 24), (22, 20), radius_x=5)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e5', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
