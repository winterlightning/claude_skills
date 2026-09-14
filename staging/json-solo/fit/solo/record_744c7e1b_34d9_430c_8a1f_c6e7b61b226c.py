"""Record (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '744c7e1b-34d9-430c-8a1f-c6e7b61b226c'
SOURCE_PATH = 'icons-json/interface-essential/record_744c7e1b-34d9-430c-8a1f-c6e7b61b226c.json'
AUTHOR = 'json_to_solo'

class RecordInterfaceEssential(Solo48):
    icon_id = 'record-interface-essential'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('record', 'interface-essential')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e1-top', (16, 24), (32, 24), radius_x=8)
        self.add_arc('e1-bottom', (32, 24), (16, 24), radius_x=8)
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
