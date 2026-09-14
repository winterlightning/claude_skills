"""Delete (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5504165f-dfd0-55fb-a70b-8d05ba635053'
SOURCE_PATH = 'icons-json/interface-essential/delete_5504165f-dfd0-55fb-a70b-8d05ba635053.json'
AUTHOR = 'json_to_solo'

class DeleteInterfaceEssential(Solo48):
    icon_id = 'delete-interface-essential'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('delete', 'interface-essential')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
