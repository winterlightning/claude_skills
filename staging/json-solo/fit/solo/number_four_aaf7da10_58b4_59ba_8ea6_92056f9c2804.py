"""Number four (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aaf7da10-58b4-59ba-8ea6-92056f9c2804'
SOURCE_PATH = 'icons-json/interface-essential/number four_aaf7da10-58b4-59ba-8ea6-92056f9c2804.json'
AUTHOR = 'json_to_solo'

class NumberFourInterfaceEssential(Solo48):
    icon_id = 'number-four-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('number', 'four', 'interface-essential')

    def build(self):
        self.add_line('e0', (33, 44), (33, 4))
        self.add_line('e1', (33, 4), (8, 33))
        self.add_line('e2', (8, 33), (40, 33))
        self.add_contour('c0', 'e0', 'e1', 'e2')
