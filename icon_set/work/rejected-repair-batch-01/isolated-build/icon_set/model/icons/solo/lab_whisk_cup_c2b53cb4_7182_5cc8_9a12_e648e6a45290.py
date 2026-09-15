"""Lab whisk cup (science), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c2b53cb4-7182-5cc8-9a12-e648e6a45290'
SOURCE_PATH = 'pictographic-primitives/science/lab whisk cup_c2b53cb4-7182-5cc8-9a12-e648e6a45290.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class LabWhiskCup(Solo48):
    icon_id = 'lab-whisk-cup'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('lab', 'whisk', 'cup', 'science')

    def build(self):
        self.add_line('e0', (40, 26), (11, 26))
        self.add_line('e1', (25, 26), (40, 4))
        self.add_line('e2', (11, 39), (11, 18))
        self.add_line('e3', (11, 18), (8, 13))
        self.add_line('e4', (8, 13), (40, 13))
        self.add_line('e5', (40, 13), (40, 39))
        self.add_line('e6', (34, 44), (17, 44))
        self.add_arc('e7', (17, 44), (11, 39), radius_x=7)
        self.add_arc('e8-1', (40, 39), (35, 44), radius_x=5)
        self.add_arc('e8-2', (35, 44), (34, 44), radius_x=9, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e7', 'e2', 'e3', 'e4', 'e5', 'e8-1', 'e8-2', 'e6', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c0')
