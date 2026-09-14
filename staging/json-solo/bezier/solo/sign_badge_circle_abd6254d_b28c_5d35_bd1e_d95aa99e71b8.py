"""Sign badge circle (maps), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'abd6254d-b28c-5d35-bd1e-d95aa99e71b8'
SOURCE_PATH = 'icons-json/maps/sign badge circle_abd6254d-b28c-5d35-bd1e-d95aa99e71b8.json'
AUTHOR = 'json_to_solo'

class SignBadgeCircleMaps(Solo48):
    icon_id = 'sign-badge-circle-maps'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('sign', 'badge', 'circle', 'maps')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
