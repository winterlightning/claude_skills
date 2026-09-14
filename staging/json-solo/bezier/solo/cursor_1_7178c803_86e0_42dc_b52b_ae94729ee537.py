"""Cursor 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7178c803-86e0-42dc-b52b-ae94729ee537'
SOURCE_PATH = 'icons-json/interface-essential/cursor 1_7178c803-86e0-42dc-b52b-ae94729ee537.json'
AUTHOR = 'json_to_solo'

class Cursor1InterfaceEssential(Solo48):
    icon_id = 'cursor-1-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('cursor', 'interface-essential')

    def build(self):
        self.add_line('e0', (40, 21), (8, 4))
        self.add_line('e1', (8, 4), (11, 44))
        self.add_line('e2', (11, 44), (21, 26))
        self.add_line('e3', (21, 26), (40, 21))
        self.add_line('e4', (21, 26), (31, 41))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
