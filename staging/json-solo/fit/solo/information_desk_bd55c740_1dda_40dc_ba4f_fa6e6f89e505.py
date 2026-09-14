"""Information desk (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd55c740-1dda-40dc-ba4f-fa6e6f89e505'
SOURCE_PATH = 'icons-json/_uncategorized_23/information desk_bd55c740-1dda-40dc-ba4f-fa6e6f89e505.json'
AUTHOR = 'json_to_solo'

class InformationDeskBd55c740(Solo48):
    icon_id = 'information-desk-bd55c740'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('information', 'desk', '_uncategorized')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
