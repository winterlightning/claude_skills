"""Side road angle right (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25347198-3f9f-4498-af06-d3003038e769'
SOURCE_PATH = 'pictographic-primitives/transportation/side road angle right_25347198-3f9f-4498-af06-d3003038e769.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class SideRoadAngleRight(Solo48):
    icon_id = 'side-road-angle-right'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('side', 'road', 'angle', 'right', 'transportation')

    def build(self):
        self.add_line('e0', (8, 4), (8, 29))
        self.add_line('e1', (8, 44), (8, 29))
        self.add_line('e2', (40, 16), (8, 29))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
