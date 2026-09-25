"""Sign badge circle (maps), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'abd6254d-b28c-5d35-bd1e-d95aa99e71b8'
SOURCE_PATH = 'pictographic-primitives/maps/sign badge circle_abd6254d-b28c-5d35-bd1e-d95aa99e71b8.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class SignBadgeCircle(Solo48):
    icon_id = 'sign-badge-circle'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    categories = ('maps', 'primitives')
    aliases = ()
    keywords = ('sign', 'badge', 'circle', 'maps')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
