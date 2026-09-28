"""Side road left (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '15230b28-84f8-47ed-8433-5c2249268be2'
SOURCE_PATH = 'pictographic-primitives/transportation/side road left_15230b28-84f8-47ed-8433-5c2249268be2.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class SideRoadLeftTransportation(Solo48):
    icon_id = 'side-road-left-transportation'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('side', 'road', 'left', 'transportation')

    def build(self):
        self.add_line('e0', (40, 4), (40, 44))
        self.add_line('e1', (8, 24), (40, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.relate('connect', 'c1', 'c0')
