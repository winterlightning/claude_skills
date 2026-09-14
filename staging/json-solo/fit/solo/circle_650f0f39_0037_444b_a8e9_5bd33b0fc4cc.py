"""Circle (other), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '650f0f39-0037-444b-a8e9-5bd33b0fc4cc'
SOURCE_PATH = 'icons-json/other/circle_650f0f39-0037-444b-a8e9-5bd33b0fc4cc.json'
AUTHOR = 'json_to_solo'

class Circle650f0f39(Solo48):
    icon_id = 'circle-650f0f39'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('circle', 'other')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
