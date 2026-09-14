"""Pin 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6e467420-67cd-4e7a-9d1f-07675500260d'
SOURCE_PATH = 'icons-json/interface-essential/pin 1_6e467420-67cd-4e7a-9d1f-07675500260d.json'
AUTHOR = 'json_to_solo'

class Pin1InterfaceEssential(Solo48):
    icon_id = 'pin-1-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('pin', 'interface-essential')

    def build(self):
        self.add_line('e0', (29, 39), (24, 44))
        self.add_arc('e1-1', (24, 44), (12, 31), radius_x=78)
        self.add_arc('e1-2', (12, 31), (8, 20), radius_x=18)
        self.add_arc('e1-3', (8, 20), (24, 4), radius_x=16)
        self.add_arc('e1-4', (24, 4), (40, 20), radius_x=16)
        self.add_arc('e1-5', (40, 20), (29, 39), radius_x=28)
        self.add_dot('e2', (24, 19))
        self.add_contour('c0', 'e0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', closed=True)
