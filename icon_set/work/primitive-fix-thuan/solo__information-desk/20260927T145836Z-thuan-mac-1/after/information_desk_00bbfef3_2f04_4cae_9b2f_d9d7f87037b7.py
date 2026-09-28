"""Information desk (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '00bbfef3-2f04-4cae-9b2f-d9d7f87037b7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__information-desk/20260927T145836Z-thuan-mac-1/reference/information desk_00bbfef3-2f04-4cae-9b2f-d9d7f87037b7.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class InformationDesk(Solo48):
    icon_id = 'information-desk'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('information', 'desk', '_uncategorized')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
        # The rejected empty circle did not convey information.
        self.add_dot('information-dot', (24, 15))
        self.add_line('information-stem', (24, 25), (24, 34))
