"""Number five (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b3a2762-be7a-5e8b-8eba-1cd030378e07'
SOURCE_PATH = 'icons-json/interface-essential/number five_4b3a2762-be7a-5e8b-8eba-1cd030378e07.json'
AUTHOR = 'json_to_solo'

class NumberFiveInterfaceEssential(Solo48):
    icon_id = 'number-five-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('number', 'five', 'interface-essential')

    def build(self):
        self.add_line('e0', (9, 22), (14, 4))
        self.add_line('e1', (14, 4), (38, 4))
        self.add_arc('e2-1', (8, 37), (14, 42), radius_x=18, sweep=False)
        self.add_line('e2-2', (14, 42), (23, 44))
        self.add_line('e2-3', (23, 44), (33, 42))
        self.add_arc('e2-4', (33, 42), (37, 39), radius_x=15, sweep=False)
        self.add_arc('e2-5', (37, 39), (40, 33), radius_x=11, sweep=False)
        self.add_arc('e2-6', (40, 33), (40, 31), radius_x=25)
        self.add_arc('e2-7', (40, 31), (27, 19), radius_x=13, sweep=False)
        self.add_arc('e2-8', (27, 19), (9, 22), radius_x=29, sweep=False)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e2-8', 'e0', 'e1')
