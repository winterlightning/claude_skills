"""Information desk (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00bbfef3-2f04-4cae-9b2f-d9d7f87037b7'
SOURCE_PATH = 'icons-json/_uncategorized_23/information desk_00bbfef3-2f04-4cae-9b2f-d9d7f87037b7.json'
AUTHOR = 'json_to_solo'

class InformationDesk00bbfef3(Solo48):
    icon_id = 'information-desk-00bbfef3'
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
